#!/usr/bin/env python
# coding: utf-8

import collections
import datetime
import json
import luigi

class InputFile(luigi.ExternalTask):

    def output(self):
        return luigi.LocalTarget('plays.ldj')

class DailyPlays(luigi.Task):

    date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        return InputFile()

    def run(self):
        with self.input().open() as handle:
            with self.output().open('w') as output:
                for line in handle:
                    doc = json.loads(line)
                    if doc['date'] == str(self.date):
                        output.write(line + "\n")

    def output(self):
        return luigi.LocalTarget('DailyPlays/%s.ldj' % self.date)

class DailyTopArtists(luigi.Task):

    date = luigi.DateParameter(default=datetime.date.today())

    def requires(self):
        return DailyPlays(date=self.date)

    def run(self):
        counter = collections.Counter()

        with self.input().open() as handle:
            for line in handle:
                if line.strip() == "":
                    continue
                doc = json.loads(line)
                counter[doc['artist']] += 1

        with self.output().open('w') as output:
            for name, plays in counter.most_common():
                output.write('%s\t%s\n' % (name, plays))

    def output(self):
        return luigi.LocalTarget('DailyTopArtists/%s.tsv' % self.date)

class IntervalTopArtists(luigi.Task):

    date_interval = luigi.DateIntervalParameter(description="from-to")

    def requires(self):
        return [DailyPlays(date=date) for date in self.date_interval]

    def run(self):
        counter = collections.Counter()

        for target in self.input():
            with target.open() as handle:
                for line in handle:
                    if line.strip() == "":
                        continue
                    doc = json.loads(line)
                    counter[doc['artist']] += 1

        with self.output().open('w') as output:
            for name, plays in counter.most_common():
                output.write('%s\t%s\n' % (name, plays))

    def output(self):
        return luigi.LocalTarget('IntervalTopArtists/%s.tsv' % self.date_interval)

if __name__ == '__main__':
    luigi.run()
