# SNMP MIB module (PACKETFLUX-STANDBYPOWER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PACKETFLUX-STANDBYPOWER
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:04 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(packetfluxMgmt,) = mibBuilder.importSymbols(
    "PACKETFLUX-SMI",
    "packetfluxMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

standbypower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2)
)
standbypower.setRevisions(
        ("2013-06-04 16:49",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _Powercontrollerstate_Type(Integer32):
    """Custom type powercontrollerstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("onprimarypower", 1),
          ("onstandbypower", 4),
          ("startingstandby", 2),
          ("transferringtoprimary", 5),
          ("transferringtostandby", 3))
    )


_Powercontrollerstate_Type.__name__ = "Integer32"
_Powercontrollerstate_Object = MibScalar
powercontrollerstate = _Powercontrollerstate_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 1),
    _Powercontrollerstate_Type()
)
powercontrollerstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powercontrollerstate.setStatus("current")


class _Transferswitchstate_Type(Integer32):
    """Custom type transferswitchstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("standby", 5),
          ("transfertoprimary1", 6),
          ("transfertoprimary2", 7),
          ("transfertoprimary3", 8),
          ("transfertostandby1", 2),
          ("transfertostandby2", 3),
          ("transfertostandby3", 4))
    )


_Transferswitchstate_Type.__name__ = "Integer32"
_Transferswitchstate_Object = MibScalar
transferswitchstate = _Transferswitchstate_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 2),
    _Transferswitchstate_Type()
)
transferswitchstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferswitchstate.setStatus("current")


class _Standbypowerstate_Type(Integer32):
    """Custom type standbypowerstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("checkrun", 8),
          ("cooldown1", 17),
          ("cooldown2", 18),
          ("cooldown3", 19),
          ("postshutdown1", 24),
          ("postshutdown2", 25),
          ("postshutdown3", 26),
          ("prepare1", 2),
          ("prepare2", 3),
          ("prepare3", 4),
          ("reprepare1", 9),
          ("reprepare2", 10),
          ("reprepare3", 11),
          ("running", 16),
          ("shutdown1", 20),
          ("shutdown2", 21),
          ("shutdown3", 22),
          ("startup1", 5),
          ("startup2", 6),
          ("startup3", 7),
          ("stopped", 1),
          ("verifyrun", 15),
          ("verifystopped", 23),
          ("warmup1", 12),
          ("warmup2", 13),
          ("warmup3", 14))
    )


_Standbypowerstate_Type.__name__ = "Integer32"
_Standbypowerstate_Object = MibScalar
standbypowerstate = _Standbypowerstate_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 3),
    _Standbypowerstate_Type()
)
standbypowerstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbypowerstate.setStatus("current")
_Ac1voltage_Type = Gauge32
_Ac1voltage_Object = MibScalar
ac1voltage = _Ac1voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 4),
    _Ac1voltage_Type()
)
ac1voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac1voltage.setStatus("current")
_Ac1frequency_Type = Gauge32
_Ac1frequency_Object = MibScalar
ac1frequency = _Ac1frequency_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 5),
    _Ac1frequency_Type()
)
ac1frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac1frequency.setStatus("current")
_Ac2voltage_Type = Gauge32
_Ac2voltage_Object = MibScalar
ac2voltage = _Ac2voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 6),
    _Ac2voltage_Type()
)
ac2voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac2voltage.setStatus("current")
_Ac2frequency_Type = Gauge32
_Ac2frequency_Object = MibScalar
ac2frequency = _Ac2frequency_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 7),
    _Ac2frequency_Type()
)
ac2frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ac2frequency.setStatus("current")
_Mtr1voltage_Type = Gauge32
_Mtr1voltage_Object = MibScalar
mtr1voltage = _Mtr1voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 8),
    _Mtr1voltage_Type()
)
mtr1voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtr1voltage.setStatus("current")
_Mtr2voltage_Type = Gauge32
_Mtr2voltage_Object = MibScalar
mtr2voltage = _Mtr2voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 9),
    _Mtr2voltage_Type()
)
mtr2voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtr2voltage.setStatus("current")
_Pwr1voltage_Type = Gauge32
_Pwr1voltage_Object = MibScalar
pwr1voltage = _Pwr1voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 10),
    _Pwr1voltage_Type()
)
pwr1voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwr1voltage.setStatus("current")
_Pwr2voltage_Type = Gauge32
_Pwr2voltage_Object = MibScalar
pwr2voltage = _Pwr2voltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 11),
    _Pwr2voltage_Type()
)
pwr2voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwr2voltage.setStatus("current")
_Shuntvoltage_Type = Integer32
_Shuntvoltage_Object = MibScalar
shuntvoltage = _Shuntvoltage_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 12),
    _Shuntvoltage_Type()
)
shuntvoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shuntvoltage.setStatus("current")
_Temperature_Type = Gauge32
_Temperature_Object = MibScalar
temperature = _Temperature_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 13),
    _Temperature_Type()
)
temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature.setStatus("current")
_Recentunsuccessfulstarts_Type = Integer32
_Recentunsuccessfulstarts_Object = MibScalar
recentunsuccessfulstarts = _Recentunsuccessfulstarts_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 14),
    _Recentunsuccessfulstarts_Type()
)
recentunsuccessfulstarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recentunsuccessfulstarts.setStatus("current")
_Totalunsuccessfulstarts_Type = Integer32
_Totalunsuccessfulstarts_Object = MibScalar
totalunsuccessfulstarts = _Totalunsuccessfulstarts_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 15),
    _Totalunsuccessfulstarts_Type()
)
totalunsuccessfulstarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totalunsuccessfulstarts.setStatus("current")
_Recentstalls_Type = Integer32
_Recentstalls_Object = MibScalar
recentstalls = _Recentstalls_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 16),
    _Recentstalls_Type()
)
recentstalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recentstalls.setStatus("current")
_Totalstalls_Type = Integer32
_Totalstalls_Object = MibScalar
totalstalls = _Totalstalls_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 17),
    _Totalstalls_Type()
)
totalstalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totalstalls.setStatus("current")
_Numberofstarts_Type = Integer32
_Numberofstarts_Object = MibScalar
numberofstarts = _Numberofstarts_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 18),
    _Numberofstarts_Type()
)
numberofstarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberofstarts.setStatus("current")
_Numberoftransfers_Type = Integer32
_Numberoftransfers_Object = MibScalar
numberoftransfers = _Numberoftransfers_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 19),
    _Numberoftransfers_Type()
)
numberoftransfers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numberoftransfers.setStatus("current")
_Currenttimeonprimary_Type = TimeTicks
_Currenttimeonprimary_Object = MibScalar
currenttimeonprimary = _Currenttimeonprimary_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 20),
    _Currenttimeonprimary_Type()
)
currenttimeonprimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currenttimeonprimary.setStatus("current")
_Totaltimeonprimary_Type = TimeTicks
_Totaltimeonprimary_Object = MibScalar
totaltimeonprimary = _Totaltimeonprimary_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 21),
    _Totaltimeonprimary_Type()
)
totaltimeonprimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totaltimeonprimary.setStatus("current")
_Currenttimeonstandby_Type = TimeTicks
_Currenttimeonstandby_Object = MibScalar
currenttimeonstandby = _Currenttimeonstandby_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 22),
    _Currenttimeonstandby_Type()
)
currenttimeonstandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currenttimeonstandby.setStatus("current")
_Totaltimeonstandby_Type = TimeTicks
_Totaltimeonstandby_Object = MibScalar
totaltimeonstandby = _Totaltimeonstandby_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 23),
    _Totaltimeonstandby_Type()
)
totaltimeonstandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totaltimeonstandby.setStatus("current")
_Currentstandbyruntime_Type = TimeTicks
_Currentstandbyruntime_Object = MibScalar
currentstandbyruntime = _Currentstandbyruntime_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 24),
    _Currentstandbyruntime_Type()
)
currentstandbyruntime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currentstandbyruntime.setStatus("current")
_Totalstandbyruntime_Type = TimeTicks
_Totalstandbyruntime_Object = MibScalar
totalstandbyruntime = _Totalstandbyruntime_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 25),
    _Totalstandbyruntime_Type()
)
totalstandbyruntime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    totalstandbyruntime.setStatus("current")
_Laststandbyrun_Type = TimeTicks
_Laststandbyrun_Object = MibScalar
laststandbyrun = _Laststandbyrun_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 26),
    _Laststandbyrun_Type()
)
laststandbyrun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laststandbyrun.setStatus("current")
_Laststandbygracefulstop_Type = TimeTicks
_Laststandbygracefulstop_Object = MibScalar
laststandbygracefulstop = _Laststandbygracefulstop_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 27),
    _Laststandbygracefulstop_Type()
)
laststandbygracefulstop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laststandbygracefulstop.setStatus("current")
_Laststandbyunsuccessfulstart_Type = TimeTicks
_Laststandbyunsuccessfulstart_Object = MibScalar
laststandbyunsuccessfulstart = _Laststandbyunsuccessfulstart_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 28),
    _Laststandbyunsuccessfulstart_Type()
)
laststandbyunsuccessfulstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laststandbyunsuccessfulstart.setStatus("current")
_Laststandbyfailure_Type = TimeTicks
_Laststandbyfailure_Object = MibScalar
laststandbyfailure = _Laststandbyfailure_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 29),
    _Laststandbyfailure_Type()
)
laststandbyfailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laststandbyfailure.setStatus("current")
_Switch1closed_Type = TruthValue
_Switch1closed_Object = MibScalar
switch1closed = _Switch1closed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 30),
    _Switch1closed_Type()
)
switch1closed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch1closed.setStatus("current")
_Switch2closed_Type = TruthValue
_Switch2closed_Object = MibScalar
switch2closed = _Switch2closed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 31),
    _Switch2closed_Type()
)
switch2closed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch2closed.setStatus("current")
_Switch3closed_Type = TruthValue
_Switch3closed_Object = MibScalar
switch3closed = _Switch3closed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 32),
    _Switch3closed_Type()
)
switch3closed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch3closed.setStatus("current")
_Switch4closed_Type = TruthValue
_Switch4closed_Object = MibScalar
switch4closed = _Switch4closed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 33),
    _Switch4closed_Type()
)
switch4closed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch4closed.setStatus("current")
_Switch5closed_Type = TruthValue
_Switch5closed_Object = MibScalar
switch5closed = _Switch5closed_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 34),
    _Switch5closed_Type()
)
switch5closed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch5closed.setStatus("current")
_Enabled_Type = TruthValue
_Enabled_Object = MibScalar
enabled = _Enabled_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 35),
    _Enabled_Type()
)
enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enabled.setStatus("current")
_Relay1on_Type = TruthValue
_Relay1on_Object = MibScalar
relay1on = _Relay1on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 36),
    _Relay1on_Type()
)
relay1on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay1on.setStatus("current")
_Relay2on_Type = TruthValue
_Relay2on_Object = MibScalar
relay2on = _Relay2on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 37),
    _Relay2on_Type()
)
relay2on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay2on.setStatus("current")
_Relay3on_Type = TruthValue
_Relay3on_Object = MibScalar
relay3on = _Relay3on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 38),
    _Relay3on_Type()
)
relay3on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay3on.setStatus("current")
_Relay4on_Type = TruthValue
_Relay4on_Object = MibScalar
relay4on = _Relay4on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 39),
    _Relay4on_Type()
)
relay4on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay4on.setStatus("current")
_Relay5on_Type = TruthValue
_Relay5on_Object = MibScalar
relay5on = _Relay5on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 40),
    _Relay5on_Type()
)
relay5on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay5on.setStatus("current")
_Relay6on_Type = TruthValue
_Relay6on_Object = MibScalar
relay6on = _Relay6on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 41),
    _Relay6on_Type()
)
relay6on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay6on.setStatus("current")
_Relay7on_Type = TruthValue
_Relay7on_Object = MibScalar
relay7on = _Relay7on_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 42),
    _Relay7on_Type()
)
relay7on.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay7on.setStatus("current")
_Ruleswitchstandby_Type = TruthValue
_Ruleswitchstandby_Object = MibScalar
ruleswitchstandby = _Ruleswitchstandby_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 43),
    _Ruleswitchstandby_Type()
)
ruleswitchstandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleswitchstandby.setStatus("current")
_Rulereturnprimary_Type = TruthValue
_Rulereturnprimary_Object = MibScalar
rulereturnprimary = _Rulereturnprimary_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 44),
    _Rulereturnprimary_Type()
)
rulereturnprimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulereturnprimary.setStatus("current")
_Rulestandbygood_Type = TruthValue
_Rulestandbygood_Object = MibScalar
rulestandbygood = _Rulestandbygood_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 45),
    _Rulestandbygood_Type()
)
rulestandbygood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulestandbygood.setStatus("current")
_Rulestopstandby_Type = TruthValue
_Rulestopstandby_Object = MibScalar
rulestopstandby = _Rulestopstandby_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 46),
    _Rulestopstandby_Type()
)
rulestopstandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rulestopstandby.setStatus("current")
_Ruleexercisestandby_Type = TruthValue
_Ruleexercisestandby_Object = MibScalar
ruleexercisestandby = _Ruleexercisestandby_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 47),
    _Ruleexercisestandby_Type()
)
ruleexercisestandby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruleexercisestandby.setStatus("current")
_Webcontrol1_Type = TruthValue
_Webcontrol1_Object = MibScalar
webcontrol1 = _Webcontrol1_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 48),
    _Webcontrol1_Type()
)
webcontrol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol1.setStatus("current")
_Webcontrol2_Type = TruthValue
_Webcontrol2_Object = MibScalar
webcontrol2 = _Webcontrol2_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 49),
    _Webcontrol2_Type()
)
webcontrol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol2.setStatus("current")
_Webcontrol3_Type = TruthValue
_Webcontrol3_Object = MibScalar
webcontrol3 = _Webcontrol3_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 50),
    _Webcontrol3_Type()
)
webcontrol3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol3.setStatus("current")
_Webcontrol4_Type = TruthValue
_Webcontrol4_Object = MibScalar
webcontrol4 = _Webcontrol4_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 51),
    _Webcontrol4_Type()
)
webcontrol4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol4.setStatus("current")
_Webcontrol5_Type = TruthValue
_Webcontrol5_Object = MibScalar
webcontrol5 = _Webcontrol5_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 52),
    _Webcontrol5_Type()
)
webcontrol5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol5.setStatus("current")
_Webcontrol6_Type = TruthValue
_Webcontrol6_Object = MibScalar
webcontrol6 = _Webcontrol6_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 53),
    _Webcontrol6_Type()
)
webcontrol6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol6.setStatus("current")
_Webcontrol7_Type = TruthValue
_Webcontrol7_Object = MibScalar
webcontrol7 = _Webcontrol7_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 54),
    _Webcontrol7_Type()
)
webcontrol7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol7.setStatus("current")
_Webcontrol8_Type = TruthValue
_Webcontrol8_Object = MibScalar
webcontrol8 = _Webcontrol8_Object(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 55),
    _Webcontrol8_Type()
)
webcontrol8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webcontrol8.setStatus("current")
_StandbypowerConformance_ObjectIdentity = ObjectIdentity
standbypowerConformance = _StandbypowerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 256)
)
_StandbypowerGroups_ObjectIdentity = ObjectIdentity
standbypowerGroups = _StandbypowerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1)
)

# Managed Objects groups

packetfluxStandbypowerAllObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32050, 2, 2, 256, 1, 1)
)
packetfluxStandbypowerAllObjects.setObjects(
      *(("PACKETFLUX-STANDBYPOWER", "powercontrollerstate"),
        ("PACKETFLUX-STANDBYPOWER", "transferswitchstate"),
        ("PACKETFLUX-STANDBYPOWER", "standbypowerstate"),
        ("PACKETFLUX-STANDBYPOWER", "ac1voltage"),
        ("PACKETFLUX-STANDBYPOWER", "ac1frequency"),
        ("PACKETFLUX-STANDBYPOWER", "ac2voltage"),
        ("PACKETFLUX-STANDBYPOWER", "ac2frequency"),
        ("PACKETFLUX-STANDBYPOWER", "mtr1voltage"),
        ("PACKETFLUX-STANDBYPOWER", "mtr2voltage"),
        ("PACKETFLUX-STANDBYPOWER", "pwr1voltage"),
        ("PACKETFLUX-STANDBYPOWER", "pwr2voltage"),
        ("PACKETFLUX-STANDBYPOWER", "shuntvoltage"),
        ("PACKETFLUX-STANDBYPOWER", "temperature"),
        ("PACKETFLUX-STANDBYPOWER", "recentunsuccessfulstarts"),
        ("PACKETFLUX-STANDBYPOWER", "totalunsuccessfulstarts"),
        ("PACKETFLUX-STANDBYPOWER", "recentstalls"),
        ("PACKETFLUX-STANDBYPOWER", "totalstalls"),
        ("PACKETFLUX-STANDBYPOWER", "numberofstarts"),
        ("PACKETFLUX-STANDBYPOWER", "numberoftransfers"),
        ("PACKETFLUX-STANDBYPOWER", "currenttimeonprimary"),
        ("PACKETFLUX-STANDBYPOWER", "totaltimeonprimary"),
        ("PACKETFLUX-STANDBYPOWER", "currenttimeonstandby"),
        ("PACKETFLUX-STANDBYPOWER", "totaltimeonstandby"),
        ("PACKETFLUX-STANDBYPOWER", "currentstandbyruntime"),
        ("PACKETFLUX-STANDBYPOWER", "totalstandbyruntime"),
        ("PACKETFLUX-STANDBYPOWER", "laststandbyrun"),
        ("PACKETFLUX-STANDBYPOWER", "laststandbygracefulstop"),
        ("PACKETFLUX-STANDBYPOWER", "laststandbyunsuccessfulstart"),
        ("PACKETFLUX-STANDBYPOWER", "laststandbyfailure"),
        ("PACKETFLUX-STANDBYPOWER", "switch1closed"),
        ("PACKETFLUX-STANDBYPOWER", "switch2closed"),
        ("PACKETFLUX-STANDBYPOWER", "switch3closed"),
        ("PACKETFLUX-STANDBYPOWER", "switch4closed"),
        ("PACKETFLUX-STANDBYPOWER", "switch5closed"),
        ("PACKETFLUX-STANDBYPOWER", "enabled"),
        ("PACKETFLUX-STANDBYPOWER", "relay1on"),
        ("PACKETFLUX-STANDBYPOWER", "relay2on"),
        ("PACKETFLUX-STANDBYPOWER", "relay3on"),
        ("PACKETFLUX-STANDBYPOWER", "relay4on"),
        ("PACKETFLUX-STANDBYPOWER", "relay5on"),
        ("PACKETFLUX-STANDBYPOWER", "relay6on"),
        ("PACKETFLUX-STANDBYPOWER", "relay7on"),
        ("PACKETFLUX-STANDBYPOWER", "ruleswitchstandby"),
        ("PACKETFLUX-STANDBYPOWER", "rulereturnprimary"),
        ("PACKETFLUX-STANDBYPOWER", "rulestandbygood"),
        ("PACKETFLUX-STANDBYPOWER", "rulestopstandby"),
        ("PACKETFLUX-STANDBYPOWER", "ruleexercisestandby"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol1"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol2"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol3"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol4"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol5"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol6"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol7"),
        ("PACKETFLUX-STANDBYPOWER", "webcontrol8"))
)
if mibBuilder.loadTexts:
    packetfluxStandbypowerAllObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETFLUX-STANDBYPOWER",
    **{"standbypower": standbypower,
       "powercontrollerstate": powercontrollerstate,
       "transferswitchstate": transferswitchstate,
       "standbypowerstate": standbypowerstate,
       "ac1voltage": ac1voltage,
       "ac1frequency": ac1frequency,
       "ac2voltage": ac2voltage,
       "ac2frequency": ac2frequency,
       "mtr1voltage": mtr1voltage,
       "mtr2voltage": mtr2voltage,
       "pwr1voltage": pwr1voltage,
       "pwr2voltage": pwr2voltage,
       "shuntvoltage": shuntvoltage,
       "temperature": temperature,
       "recentunsuccessfulstarts": recentunsuccessfulstarts,
       "totalunsuccessfulstarts": totalunsuccessfulstarts,
       "recentstalls": recentstalls,
       "totalstalls": totalstalls,
       "numberofstarts": numberofstarts,
       "numberoftransfers": numberoftransfers,
       "currenttimeonprimary": currenttimeonprimary,
       "totaltimeonprimary": totaltimeonprimary,
       "currenttimeonstandby": currenttimeonstandby,
       "totaltimeonstandby": totaltimeonstandby,
       "currentstandbyruntime": currentstandbyruntime,
       "totalstandbyruntime": totalstandbyruntime,
       "laststandbyrun": laststandbyrun,
       "laststandbygracefulstop": laststandbygracefulstop,
       "laststandbyunsuccessfulstart": laststandbyunsuccessfulstart,
       "laststandbyfailure": laststandbyfailure,
       "switch1closed": switch1closed,
       "switch2closed": switch2closed,
       "switch3closed": switch3closed,
       "switch4closed": switch4closed,
       "switch5closed": switch5closed,
       "enabled": enabled,
       "relay1on": relay1on,
       "relay2on": relay2on,
       "relay3on": relay3on,
       "relay4on": relay4on,
       "relay5on": relay5on,
       "relay6on": relay6on,
       "relay7on": relay7on,
       "ruleswitchstandby": ruleswitchstandby,
       "rulereturnprimary": rulereturnprimary,
       "rulestandbygood": rulestandbygood,
       "rulestopstandby": rulestopstandby,
       "ruleexercisestandby": ruleexercisestandby,
       "webcontrol1": webcontrol1,
       "webcontrol2": webcontrol2,
       "webcontrol3": webcontrol3,
       "webcontrol4": webcontrol4,
       "webcontrol5": webcontrol5,
       "webcontrol6": webcontrol6,
       "webcontrol7": webcontrol7,
       "webcontrol8": webcontrol8,
       "standbypowerConformance": standbypowerConformance,
       "standbypowerGroups": standbypowerGroups,
       "packetfluxStandbypowerAllObjects": packetfluxStandbypowerAllObjects}
)
