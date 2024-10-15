# SNMP MIB module (HP-ICF-OID) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-OID
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:56 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

icf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
icf.setRevisions(
        ("2017-11-08 00:00",
         "2017-07-18 00:00",
         "2017-05-01 00:00",
         "2017-03-28 00:00",
         "2017-03-08 00:00",
         "2017-01-18 00:00",
         "2016-12-07 00:00",
         "2016-10-07 00:00",
         "2016-06-06 00:00",
         "2016-02-02 00:00",
         "2015-12-08 00:00",
         "2015-11-18 00:00",
         "2015-11-12 00:00",
         "2015-11-10 00:00",
         "2015-10-15 00:00",
         "2015-09-21 00:00",
         "2015-05-22 00:00",
         "2015-05-19 00:00",
         "2015-05-07 00:00",
         "2015-04-30 00:00",
         "2015-04-23 00:00",
         "2015-04-06 00:00",
         "2015-03-24 00:00",
         "2015-02-20 00:00",
         "2015-02-13 00:00",
         "2015-01-30 00:00",
         "2014-10-01 00:00",
         "2014-07-31 00:00",
         "2014-06-25 00:00",
         "2014-06-23 00:00",
         "2014-05-27 00:00",
         "2014-03-25 00:00",
         "2014-03-04 00:00",
         "2014-02-13 00:00",
         "2013-09-14 00:00",
         "2013-07-22 00:00",
         "2013-07-15 00:00",
         "2013-07-08 00:00",
         "2013-06-12 00:00",
         "2013-04-05 00:00",
         "2013-04-04 00:00",
         "2013-03-20 00:00",
         "2013-02-11 00:00",
         "2013-01-21 00:00",
         "2012-12-07 00:00",
         "2012-12-06 00:00",
         "2012-10-17 00:00",
         "2012-08-21 00:00",
         "2012-04-02 00:00",
         "2012-03-22 00:00",
         "2012-02-17 00:00",
         "2011-07-03 00:00",
         "2011-05-27 00:00",
         "2011-05-09 00:00",
         "2011-03-03 00:00",
         "2010-12-14 00:00",
         "2010-09-06 16:32",
         "2010-08-04 00:00",
         "2010-07-22 00:00",
         "2010-06-25 00:00",
         "2010-06-22 00:00",
         "2010-05-18 00:00",
         "2010-05-17 00:00",
         "2010-04-22 00:00",
         "2010-04-21 00:00",
         "2010-04-11 00:00",
         "2010-03-22 00:00",
         "2010-02-08 00:00",
         "2009-12-08 00:00",
         "2009-10-16 00:00",
         "2009-09-25 00:00",
         "2009-09-24 00:00",
         "2009-09-09 00:00",
         "2009-07-08 00:00",
         "2009-04-08 00:00",
         "2009-02-17 00:00",
         "2009-02-04 00:00",
         "2009-02-02 00:00",
         "2008-12-15 00:01",
         "2008-12-15 00:00",
         "2008-10-30 00:00",
         "2008-10-24 00:00",
         "2008-10-21 00:00",
         "2008-10-02 00:00",
         "2008-08-06 00:00",
         "2008-05-12 00:00",
         "2008-03-10 00:00",
         "2008-03-06 00:00",
         "2008-02-15 00:00",
         "2008-02-04 15:25",
         "2007-10-23 00:01",
         "2007-10-23 00:00",
         "2007-09-07 00:00",
         "2007-05-21 00:00",
         "2007-04-30 00:00",
         "2007-04-17 00:00",
         "2006-10-31 00:00",
         "2006-09-25 12:00",
         "2006-09-08 12:00",
         "2006-08-22 12:00",
         "2006-08-04 00:00",
         "2006-07-27 12:00",
         "2006-07-26 00:00",
         "2006-06-30 00:00",
         "2006-06-05 12:33",
         "2006-05-17 12:33",
         "2006-03-20 16:27",
         "2006-01-10 18:53",
         "2005-08-04 16:19",
         "2005-06-08 12:44",
         "2005-05-20 21:23",
         "2005-03-22 19:26",
         "2005-03-08 15:30",
         "2005-02-25 00:41",
         "2005-01-11 17:45",
         "2005-01-10 20:43",
         "2004-09-10 20:43",
         "2004-09-02 10:30",
         "2004-08-09 10:30",
         "2004-07-28 20:43",
         "2004-03-31 00:51",
         "2004-03-31 00:50",
         "2004-02-12 21:15",
         "2004-01-20 18:55",
         "2003-12-29 17:05",
         "2003-06-09 16:17",
         "2003-04-10 11:18",
         "2003-02-04 17:16",
         "2003-01-28 15:10",
         "2003-01-21 16:33",
         "2002-04-06 01:00",
         "2000-11-03 22:25",
         "1999-09-03 00:04",
         "1998-09-24 00:04",
         "1997-10-21 02:42",
         "1997-03-06 03:42",
         "1996-09-13 23:03")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_HpSystem_ObjectIdentity = ObjectIdentity
hpSystem = _HpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetElement_ObjectIdentity = ObjectIdentity
netElement = _NetElement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7)
)
_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1)
)
_Bridge1010_ObjectIdentity = ObjectIdentity
bridge1010 = _Bridge1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    bridge1010.setStatus("current")
_BridgeRemote_ObjectIdentity = ObjectIdentity
bridgeRemote = _BridgeRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    bridgeRemote.setStatus("current")
_Eswitch_ObjectIdentity = ObjectIdentity
eswitch = _Eswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    eswitch.setStatus("current")
_Eswitch2_ObjectIdentity = ObjectIdentity
eswitch2 = _Eswitch2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 8)
)
if mibBuilder.loadTexts:
    eswitch2.setStatus("current")
_NetSwitch100_ObjectIdentity = ObjectIdentity
netSwitch100 = _NetSwitch100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 9)
)
if mibBuilder.loadTexts:
    netSwitch100.setStatus("current")
_NetSwitch200_ObjectIdentity = ObjectIdentity
netSwitch200 = _NetSwitch200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 1, 10)
)
if mibBuilder.loadTexts:
    netSwitch200.setStatus("current")
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2)
)
_IcfRouterER_ObjectIdentity = ObjectIdentity
icfRouterER = _IcfRouterER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    icfRouterER.setStatus("current")
_IcfRouterTR_ObjectIdentity = ObjectIdentity
icfRouterTR = _IcfRouterTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    icfRouterTR.setStatus("current")
_IcfRouterSR_ObjectIdentity = ObjectIdentity
icfRouterSR = _IcfRouterSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 3)
)
if mibBuilder.loadTexts:
    icfRouterSR.setStatus("current")
_IcfRouterFR_ObjectIdentity = ObjectIdentity
icfRouterFR = _IcfRouterFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 4)
)
if mibBuilder.loadTexts:
    icfRouterFR.setStatus("current")
_IcfRouterLR_ObjectIdentity = ObjectIdentity
icfRouterLR = _IcfRouterLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 5)
)
if mibBuilder.loadTexts:
    icfRouterLR.setStatus("current")
_IcfRouterBR_ObjectIdentity = ObjectIdentity
icfRouterBR = _IcfRouterBR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 6)
)
if mibBuilder.loadTexts:
    icfRouterBR.setStatus("current")
_IcfRouterPR_ObjectIdentity = ObjectIdentity
icfRouterPR = _IcfRouterPR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 7)
)
if mibBuilder.loadTexts:
    icfRouterPR.setStatus("current")
_IcfRouter650_ObjectIdentity = ObjectIdentity
icfRouter650 = _IcfRouter650_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8)
)
if mibBuilder.loadTexts:
    icfRouter650.setStatus("current")
_IcfRouter650Engine_ObjectIdentity = ObjectIdentity
icfRouter650Engine = _IcfRouter650Engine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 2)
)
if mibBuilder.loadTexts:
    icfRouter650Engine.setStatus("current")
_IcfRouter650Port4E_ObjectIdentity = ObjectIdentity
icfRouter650Port4E = _IcfRouter650Port4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 3)
)
if mibBuilder.loadTexts:
    icfRouter650Port4E.setStatus("current")
_IcfRouter650Port4S_ObjectIdentity = ObjectIdentity
icfRouter650Port4S = _IcfRouter650Port4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 4)
)
if mibBuilder.loadTexts:
    icfRouter650Port4S.setStatus("current")
_IcfRouter650Port4T_ObjectIdentity = ObjectIdentity
icfRouter650Port4T = _IcfRouter650Port4T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 5)
)
if mibBuilder.loadTexts:
    icfRouter650Port4T.setStatus("current")
_IcfRouter650PortFDDI_ObjectIdentity = ObjectIdentity
icfRouter650PortFDDI = _IcfRouter650PortFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 6)
)
if mibBuilder.loadTexts:
    icfRouter650PortFDDI.setStatus("current")
_IcfRouter650Port100VG_ObjectIdentity = ObjectIdentity
icfRouter650Port100VG = _IcfRouter650Port100VG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 8, 7)
)
if mibBuilder.loadTexts:
    icfRouter650Port100VG.setStatus("current")
_IcfRouter230_ObjectIdentity = ObjectIdentity
icfRouter230 = _IcfRouter230_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 9)
)
if mibBuilder.loadTexts:
    icfRouter230.setStatus("current")
_IcfRouter250_ObjectIdentity = ObjectIdentity
icfRouter250 = _IcfRouter250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 10)
)
if mibBuilder.loadTexts:
    icfRouter250.setStatus("current")
_IcfRouter255_ObjectIdentity = ObjectIdentity
icfRouter255 = _IcfRouter255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 11)
)
if mibBuilder.loadTexts:
    icfRouter255.setStatus("current")
_IcfRouter210_ObjectIdentity = ObjectIdentity
icfRouter210 = _IcfRouter210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 2, 12)
)
if mibBuilder.loadTexts:
    icfRouter210.setStatus("current")
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5)
)
_EtherTwist12_ObjectIdentity = ObjectIdentity
etherTwist12 = _EtherTwist12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 1)
)
if mibBuilder.loadTexts:
    etherTwist12.setStatus("current")
_FiberOptic_ObjectIdentity = ObjectIdentity
fiberOptic = _FiberOptic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 3)
)
if mibBuilder.loadTexts:
    fiberOptic.setStatus("current")
_EtherTwist48_ObjectIdentity = ObjectIdentity
etherTwist48 = _EtherTwist48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 4)
)
if mibBuilder.loadTexts:
    etherTwist48.setStatus("current")
_ThinLAN_ObjectIdentity = ObjectIdentity
thinLAN = _ThinLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 5)
)
if mibBuilder.loadTexts:
    thinLAN.setStatus("current")
_EtherTwist24S_ObjectIdentity = ObjectIdentity
etherTwist24S = _EtherTwist24S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 6)
)
if mibBuilder.loadTexts:
    etherTwist24S.setStatus("current")
_AdvStack12_ObjectIdentity = ObjectIdentity
advStack12 = _AdvStack12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 7)
)
if mibBuilder.loadTexts:
    advStack12.setStatus("current")
_AdvStack24_ObjectIdentity = ObjectIdentity
advStack24 = _AdvStack24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 8)
)
if mibBuilder.loadTexts:
    advStack24.setStatus("current")
_AdvStack48_ObjectIdentity = ObjectIdentity
advStack48 = _AdvStack48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 9)
)
if mibBuilder.loadTexts:
    advStack48.setStatus("current")
_AdvStackVg15_ObjectIdentity = ObjectIdentity
advStackVg15 = _AdvStackVg15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 10)
)
if mibBuilder.loadTexts:
    advStackVg15.setStatus("current")
_AdvStackU8_ObjectIdentity = ObjectIdentity
advStackU8 = _AdvStackU8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 11)
)
if mibBuilder.loadTexts:
    advStackU8.setStatus("current")
_AdvStackU16_ObjectIdentity = ObjectIdentity
advStackU16 = _AdvStackU16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 12)
)
if mibBuilder.loadTexts:
    advStackU16.setStatus("current")
_AdvStackVg6_ObjectIdentity = ObjectIdentity
advStackVg6 = _AdvStackVg6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 13)
)
if mibBuilder.loadTexts:
    advStackVg6.setStatus("current")
_AdvStackVg12_ObjectIdentity = ObjectIdentity
advStackVg12 = _AdvStackVg12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 14)
)
if mibBuilder.loadTexts:
    advStackVg12.setStatus("current")
_HpAdvStkEnetSH12R_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSH12R = _HpAdvStkEnetSH12R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 15)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH12R.setStatus("current")
_HpAdvStkEnetSH24R_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSH24R = _HpAdvStkEnetSH24R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 16)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH24R.setStatus("current")
_HpAdvStkEnetSH24T_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSH24T = _HpAdvStkEnetSH24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 17)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSH24T.setStatus("current")
_HpAdvStk100Tx12TM_ObjectIdentity = ObjectIdentity
hpAdvStk100Tx12TM = _HpAdvStk100Tx12TM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 18)
)
if mibBuilder.loadTexts:
    hpAdvStk100Tx12TM.setStatus("current")
_Hp10THub16M_ObjectIdentity = ObjectIdentity
hp10THub16M = _Hp10THub16M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 19)
)
if mibBuilder.loadTexts:
    hp10THub16M.setStatus("current")
_Hp10BaseTHub12M_ObjectIdentity = ObjectIdentity
hp10BaseTHub12M = _Hp10BaseTHub12M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 20)
)
if mibBuilder.loadTexts:
    hp10BaseTHub12M.setStatus("current")
_Hp10BaseTHub24M_ObjectIdentity = ObjectIdentity
hp10BaseTHub24M = _Hp10BaseTHub24M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 21)
)
if mibBuilder.loadTexts:
    hp10BaseTHub24M.setStatus("current")
_HpProCurve10T100THub12M_ObjectIdentity = ObjectIdentity
hpProCurve10T100THub12M = _HpProCurve10T100THub12M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 22)
)
if mibBuilder.loadTexts:
    hpProCurve10T100THub12M.setStatus("current")
_HpProCurve10T100THub24M_ObjectIdentity = ObjectIdentity
hpProCurve10T100THub24M = _HpProCurve10T100THub24M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 5, 23)
)
if mibBuilder.loadTexts:
    hpProCurve10T100THub24M.setStatus("current")
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8)
)
_RepeaterAgent_ObjectIdentity = ObjectIdentity
repeaterAgent = _RepeaterAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 1)
)
if mibBuilder.loadTexts:
    repeaterAgent.setStatus("current")
_ChassisAgents_ObjectIdentity = ObjectIdentity
chassisAgents = _ChassisAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2)
)
_IcfVgAgent_ObjectIdentity = ObjectIdentity
icfVgAgent = _IcfVgAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 1)
)
if mibBuilder.loadTexts:
    icfVgAgent.setStatus("current")
_IcfVgAgent2_ObjectIdentity = ObjectIdentity
icfVgAgent2 = _IcfVgAgent2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 3)
)
if mibBuilder.loadTexts:
    icfVgAgent2.setStatus("current")
_HpicfEnetSMM_ObjectIdentity = ObjectIdentity
hpicfEnetSMM = _HpicfEnetSMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfEnetSMM.setStatus("current")
_HpAdvStkEnetSHAgent_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHAgent = _HpAdvStkEnetSHAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 5)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHAgent.setStatus("current")
_HpAdvStkSwStackTopMgmt_ObjectIdentity = ObjectIdentity
hpAdvStkSwStackTopMgmt = _HpAdvStkSwStackTopMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 6)
)
if mibBuilder.loadTexts:
    hpAdvStkSwStackTopMgmt.setStatus("current")
_HpSwitch8000CpuCard_ObjectIdentity = ObjectIdentity
hpSwitch8000CpuCard = _HpSwitch8000CpuCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 2, 7)
)
if mibBuilder.loadTexts:
    hpSwitch8000CpuCard.setStatus("current")
_IcfSensors_ObjectIdentity = ObjectIdentity
icfSensors = _IcfSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3)
)
_IcfPowerSupplySensor_ObjectIdentity = ObjectIdentity
icfPowerSupplySensor = _IcfPowerSupplySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 1)
)
if mibBuilder.loadTexts:
    icfPowerSupplySensor.setStatus("current")
_IcfFanSensor_ObjectIdentity = ObjectIdentity
icfFanSensor = _IcfFanSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 2)
)
if mibBuilder.loadTexts:
    icfFanSensor.setStatus("current")
_IcfTemperatureSensor_ObjectIdentity = ObjectIdentity
icfTemperatureSensor = _IcfTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 3)
)
if mibBuilder.loadTexts:
    icfTemperatureSensor.setStatus("current")
_IcfFutureSlotSensor_ObjectIdentity = ObjectIdentity
icfFutureSlotSensor = _IcfFutureSlotSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 3, 4)
)
if mibBuilder.loadTexts:
    icfFutureSlotSensor.setStatus("current")
_IcfCards_ObjectIdentity = ObjectIdentity
icfCards = _IcfCards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 4)
)
_IcfUnidentifiedCard_ObjectIdentity = ObjectIdentity
icfUnidentifiedCard = _IcfUnidentifiedCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 4, 1)
)
if mibBuilder.loadTexts:
    icfUnidentifiedCard.setStatus("current")
_HpAdvStkEnetSHSwitch_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHSwitch = _HpAdvStkEnetSHSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 4, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHSwitch.setStatus("current")
_HpAdvStkSwStackExpander_ObjectIdentity = ObjectIdentity
hpAdvStkSwStackExpander = _HpAdvStkSwStackExpander_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 4, 3)
)
if mibBuilder.loadTexts:
    hpAdvStkSwStackExpander.setStatus("current")
_HpicfStacks_ObjectIdentity = ObjectIdentity
hpicfStacks = _HpicfStacks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5)
)
_HpAdvStkEnetSHStack_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHStack = _HpAdvStkEnetSHStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 1)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHStack.setStatus("current")
_HpStack_ObjectIdentity = ObjectIdentity
hpStack = _HpStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 2)
)
if mibBuilder.loadTexts:
    hpStack.setStatus("current")
_HpStack2920_ObjectIdentity = ObjectIdentity
hpStack2920 = _HpStack2920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 3)
)
if mibBuilder.loadTexts:
    hpStack2920.setStatus("current")
_ArubaStack3810_ObjectIdentity = ObjectIdentity
arubaStack3810 = _ArubaStack3810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 4)
)
if mibBuilder.loadTexts:
    arubaStack3810.setStatus("current")
_ArubaStack2930_ObjectIdentity = ObjectIdentity
arubaStack2930 = _ArubaStack2930_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 5)
)
if mibBuilder.loadTexts:
    arubaStack2930.setStatus("current")
_HpStackVSF5400R_ObjectIdentity = ObjectIdentity
hpStackVSF5400R = _HpStackVSF5400R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 6)
)
if mibBuilder.loadTexts:
    hpStackVSF5400R.setStatus("current")
_ArubaStack2930M_ObjectIdentity = ObjectIdentity
arubaStack2930M = _ArubaStack2930M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 5, 7)
)
if mibBuilder.loadTexts:
    arubaStack2930M.setStatus("current")
_HpicfBackplanes_ObjectIdentity = ObjectIdentity
hpicfBackplanes = _HpicfBackplanes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6)
)
_HpAdvStkEnetSHExtSeg_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHExtSeg = _HpAdvStkEnetSHExtSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6, 1)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHExtSeg.setStatus("current")
_HpAdvStkEnetSHIntSeg_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHIntSeg = _HpAdvStkEnetSHIntSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHIntSeg.setStatus("current")
_Hp10BaseTHubSeg_ObjectIdentity = ObjectIdentity
hp10BaseTHubSeg = _Hp10BaseTHubSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6, 3)
)
if mibBuilder.loadTexts:
    hp10BaseTHubSeg.setStatus("current")
_HpSwitchBackplane_ObjectIdentity = ObjectIdentity
hpSwitchBackplane = _HpSwitchBackplane_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6, 4)
)
if mibBuilder.loadTexts:
    hpSwitchBackplane.setStatus("current")
_Hp100BaseTHubSeg_ObjectIdentity = ObjectIdentity
hp100BaseTHubSeg = _Hp100BaseTHubSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 6, 5)
)
if mibBuilder.loadTexts:
    hp100BaseTHubSeg.setStatus("current")
_HpicfSlots_ObjectIdentity = ObjectIdentity
hpicfSlots = _HpicfSlots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7)
)
_HpAdvStkEnetSHAgentSlot_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHAgentSlot = _HpAdvStkEnetSHAgentSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHAgentSlot.setStatus("current")
_HpAdvStkEnetSHIOSlot_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHIOSlot = _HpAdvStkEnetSHIOSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHIOSlot.setStatus("current")
_HpAdvStkSwStackMgmtSlot_ObjectIdentity = ObjectIdentity
hpAdvStkSwStackMgmtSlot = _HpAdvStkSwStackMgmtSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 3)
)
if mibBuilder.loadTexts:
    hpAdvStkSwStackMgmtSlot.setStatus("current")
_HpAdvStkSwStackExpSlot_ObjectIdentity = ObjectIdentity
hpAdvStkSwStackExpSlot = _HpAdvStkSwStackExpSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 4)
)
if mibBuilder.loadTexts:
    hpAdvStkSwStackExpSlot.setStatus("current")
_HpSwitch8000PowerSupplyBay_ObjectIdentity = ObjectIdentity
hpSwitch8000PowerSupplyBay = _HpSwitch8000PowerSupplyBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 5)
)
if mibBuilder.loadTexts:
    hpSwitch8000PowerSupplyBay.setStatus("current")
_HpSwitch8000CpuSlot_ObjectIdentity = ObjectIdentity
hpSwitch8000CpuSlot = _HpSwitch8000CpuSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 6)
)
if mibBuilder.loadTexts:
    hpSwitch8000CpuSlot.setStatus("current")
_HpSwitch8000PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch8000PortSlot = _HpSwitch8000PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 7)
)
if mibBuilder.loadTexts:
    hpSwitch8000PortSlot.setStatus("current")
_HpSwitch2524PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2524PortSlot = _HpSwitch2524PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 8)
)
if mibBuilder.loadTexts:
    hpSwitch2524PortSlot.setStatus("current")
_HpSwitch5308PowerSupplyBay_ObjectIdentity = ObjectIdentity
hpSwitch5308PowerSupplyBay = _HpSwitch5308PowerSupplyBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 9)
)
if mibBuilder.loadTexts:
    hpSwitch5308PowerSupplyBay.setStatus("current")
_HpSwitch5308PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch5308PortSlot = _HpSwitch5308PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 10)
)
if mibBuilder.loadTexts:
    hpSwitch5308PortSlot.setStatus("current")
_HpSwitch4865PowerSupplyBay_ObjectIdentity = ObjectIdentity
hpSwitch4865PowerSupplyBay = _HpSwitch4865PowerSupplyBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 11)
)
if mibBuilder.loadTexts:
    hpSwitch4865PowerSupplyBay.setStatus("current")
_HpSwitch4865PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch4865PortSlot = _HpSwitch4865PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 12)
)
if mibBuilder.loadTexts:
    hpSwitch4865PortSlot.setStatus("current")
_HpSwitch2650PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2650PortSlot = _HpSwitch2650PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 13)
)
if mibBuilder.loadTexts:
    hpSwitch2650PortSlot.setStatus("current")
_HpSwitch6108PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch6108PortSlot = _HpSwitch6108PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 14)
)
if mibBuilder.loadTexts:
    hpSwitch6108PortSlot.setStatus("current")
_HpSwitch2824PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2824PortSlot = _HpSwitch2824PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 15)
)
if mibBuilder.loadTexts:
    hpSwitch2824PortSlot.setStatus("current")
_HpSwitch2626PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2626PortSlot = _HpSwitch2626PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 16)
)
if mibBuilder.loadTexts:
    hpSwitch2626PortSlot.setStatus("current")
_HpSwitch2650PPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2650PPortSlot = _HpSwitch2650PPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 17)
)
if mibBuilder.loadTexts:
    hpSwitch2650PPortSlot.setStatus("current")
_HpSwitch2626PPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2626PPortSlot = _HpSwitch2626PPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 18)
)
if mibBuilder.loadTexts:
    hpSwitch2626PPortSlot.setStatus("current")
_HpSwitch3324PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch3324PortSlot = _HpSwitch3324PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 19)
)
if mibBuilder.loadTexts:
    hpSwitch3324PortSlot.setStatus("current")
_HpSwitch2650CRPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2650CRPortSlot = _HpSwitch2650CRPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 20)
)
if mibBuilder.loadTexts:
    hpSwitch2650CRPortSlot.setStatus("current")
_HpSwitch2626CRPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2626CRPortSlot = _HpSwitch2626CRPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 21)
)
if mibBuilder.loadTexts:
    hpSwitch2626CRPortSlot.setStatus("current")
_HpSwitch2600n8PPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2600n8PPortSlot = _HpSwitch2600n8PPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 22)
)
if mibBuilder.loadTexts:
    hpSwitch2600n8PPortSlot.setStatus("current")
_HpSwitch869xPowerSupplyBay_ObjectIdentity = ObjectIdentity
hpSwitch869xPowerSupplyBay = _HpSwitch869xPowerSupplyBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 23)
)
if mibBuilder.loadTexts:
    hpSwitch869xPowerSupplyBay.setStatus("current")
_HpSwitch869xPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch869xPortSlot = _HpSwitch869xPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 24)
)
if mibBuilder.loadTexts:
    hpSwitch869xPortSlot.setStatus("current")
_HpSwitch2510PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2510PortSlot = _HpSwitch2510PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 25)
)
if mibBuilder.loadTexts:
    hpSwitch2510PortSlot.setStatus("current")
_HpSwitch2810PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2810PortSlot = _HpSwitch2810PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 26)
)
if mibBuilder.loadTexts:
    hpSwitch2810PortSlot.setStatus("current")
_HpSwitch5400CpuCardBay_ObjectIdentity = ObjectIdentity
hpSwitch5400CpuCardBay = _HpSwitch5400CpuCardBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 27)
)
if mibBuilder.loadTexts:
    hpSwitch5400CpuCardBay.setStatus("current")
_HpSwitch8212FabricBay_ObjectIdentity = ObjectIdentity
hpSwitch8212FabricBay = _HpSwitch8212FabricBay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 28)
)
if mibBuilder.loadTexts:
    hpSwitch8212FabricBay.setStatus("current")
_HpSwitch2610PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2610PortSlot = _HpSwitch2610PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 29)
)
if mibBuilder.loadTexts:
    hpSwitch2610PortSlot.setStatus("current")
_HpSwitch2610PPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2610PPortSlot = _HpSwitch2610PPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 30)
)
if mibBuilder.loadTexts:
    hpSwitch2610PPortSlot.setStatus("current")
_HpSwitch2510BPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2510BPortSlot = _HpSwitch2510BPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 31)
)
if mibBuilder.loadTexts:
    hpSwitch2510BPortSlot.setStatus("current")
_HpSwitch2626CPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2626CPortSlot = _HpSwitch2626CPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 32)
)
if mibBuilder.loadTexts:
    hpSwitch2626CPortSlot.setStatus("current")
_HpSwitch2650CPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2650CPortSlot = _HpSwitch2650CPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 33)
)
if mibBuilder.loadTexts:
    hpSwitch2650CPortSlot.setStatus("current")
_HpSwitch2910PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2910PortSlot = _HpSwitch2910PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 34)
)
if mibBuilder.loadTexts:
    hpSwitch2910PortSlot.setStatus("current")
_HpSwitch2510GPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2510GPortSlot = _HpSwitch2510GPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 35)
)
if mibBuilder.loadTexts:
    hpSwitch2510GPortSlot.setStatus("current")
_HpSwitch2520PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2520PortSlot = _HpSwitch2520PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 36)
)
if mibBuilder.loadTexts:
    hpSwitch2520PortSlot.setStatus("current")
_HpSwitch2520GPortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2520GPortSlot = _HpSwitch2520GPortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 37)
)
if mibBuilder.loadTexts:
    hpSwitch2520GPortSlot.setStatus("current")
_HpSwitch2615PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2615PortSlot = _HpSwitch2615PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 38)
)
if mibBuilder.loadTexts:
    hpSwitch2615PortSlot.setStatus("current")
_HpSwitch2915PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2915PortSlot = _HpSwitch2915PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 39)
)
if mibBuilder.loadTexts:
    hpSwitch2915PortSlot.setStatus("current")
_HpSwitchJ9580PowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9580PowerSupply = _HpSwitchJ9580PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 40)
)
if mibBuilder.loadTexts:
    hpSwitchJ9580PowerSupply.setStatus("current")
_HpSwitchJ9581PowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9581PowerSupply = _HpSwitchJ9581PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 41)
)
if mibBuilder.loadTexts:
    hpSwitchJ9581PowerSupply.setStatus("current")
_HpSwitchJ9582FanTray_ObjectIdentity = ObjectIdentity
hpSwitchJ9582FanTray = _HpSwitchJ9582FanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 42)
)
if mibBuilder.loadTexts:
    hpSwitchJ9582FanTray.setStatus("current")
_HpSwitch2620PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2620PortSlot = _HpSwitch2620PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 43)
)
if mibBuilder.loadTexts:
    hpSwitch2620PortSlot.setStatus("current")
_HpSwitch2530PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2530PortSlot = _HpSwitch2530PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 45)
)
if mibBuilder.loadTexts:
    hpSwitch2530PortSlot.setStatus("current")
_HpSwitch2920StackingSlot_ObjectIdentity = ObjectIdentity
hpSwitch2920StackingSlot = _HpSwitch2920StackingSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 46)
)
if mibBuilder.loadTexts:
    hpSwitch2920StackingSlot.setStatus("current")
_HpSwitchJ9737APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9737APowerSupply = _HpSwitchJ9737APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 47)
)
if mibBuilder.loadTexts:
    hpSwitchJ9737APowerSupply.setStatus("current")
_HpSwitchJ9738APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9738APowerSupply = _HpSwitchJ9738APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 48)
)
if mibBuilder.loadTexts:
    hpSwitchJ9738APowerSupply.setStatus("current")
_HpSwitchJ9739APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9739APowerSupply = _HpSwitchJ9739APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 49)
)
if mibBuilder.loadTexts:
    hpSwitchJ9739APowerSupply.setStatus("current")
_HpSwitch2920PortSlot_ObjectIdentity = ObjectIdentity
hpSwitch2920PortSlot = _HpSwitch2920PortSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 50)
)
if mibBuilder.loadTexts:
    hpSwitch2920PortSlot.setStatus("current")
_HpSwitch3800StackingSlot_ObjectIdentity = ObjectIdentity
hpSwitch3800StackingSlot = _HpSwitch3800StackingSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 51)
)
if mibBuilder.loadTexts:
    hpSwitch3800StackingSlot.setStatus("current")
_HpSwitchJ9828APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9828APowerSupply = _HpSwitchJ9828APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 52)
)
if mibBuilder.loadTexts:
    hpSwitchJ9828APowerSupply.setStatus("current")
_HpSwitchJ9829APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9829APowerSupply = _HpSwitchJ9829APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 53)
)
if mibBuilder.loadTexts:
    hpSwitchJ9829APowerSupply.setStatus("current")
_HpSwitchJ9830APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9830APowerSupply = _HpSwitchJ9830APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 54)
)
if mibBuilder.loadTexts:
    hpSwitchJ9830APowerSupply.setStatus("current")
_HpSwitchJ9831AFanTray_ObjectIdentity = ObjectIdentity
hpSwitchJ9831AFanTray = _HpSwitchJ9831AFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 55)
)
if mibBuilder.loadTexts:
    hpSwitchJ9831AFanTray.setStatus("current")
_HpSwitchJ9832AFanTray_ObjectIdentity = ObjectIdentity
hpSwitchJ9832AFanTray = _HpSwitchJ9832AFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 56)
)
if mibBuilder.loadTexts:
    hpSwitchJ9832AFanTray.setStatus("current")
_HpSwitchJ9805APowerSupply_ObjectIdentity = ObjectIdentity
hpSwitchJ9805APowerSupply = _HpSwitchJ9805APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 57)
)
if mibBuilder.loadTexts:
    hpSwitchJ9805APowerSupply.setStatus("current")
_HpSwitchJ9806APowerCable_ObjectIdentity = ObjectIdentity
hpSwitchJ9806APowerCable = _HpSwitchJ9806APowerCable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 58)
)
if mibBuilder.loadTexts:
    hpSwitchJ9806APowerCable.setStatus("current")
_ArubaJL085APowerSupply_ObjectIdentity = ObjectIdentity
arubaJL085APowerSupply = _ArubaJL085APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 59)
)
if mibBuilder.loadTexts:
    arubaJL085APowerSupply.setStatus("current")
_ArubaJL086APowerSupply_ObjectIdentity = ObjectIdentity
arubaJL086APowerSupply = _ArubaJL086APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 60)
)
if mibBuilder.loadTexts:
    arubaJL086APowerSupply.setStatus("current")
_ArubaJL087APowerSupply_ObjectIdentity = ObjectIdentity
arubaJL087APowerSupply = _ArubaJL087APowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 7, 61)
)
if mibBuilder.loadTexts:
    arubaJL087APowerSupply.setStatus("current")
_HpicfHubPorts_ObjectIdentity = ObjectIdentity
hpicfHubPorts = _HpicfHubPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8)
)
_HpAdvStkEnetSHExtPort_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHExtPort = _HpAdvStkEnetSHExtPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 1)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHExtPort.setStatus("current")
_HpAdvStkEnetSHIntPort_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHIntPort = _HpAdvStkEnetSHIntPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 2)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHIntPort.setStatus("current")
_HpAdvStkEnetSHAgentPort_ObjectIdentity = ObjectIdentity
hpAdvStkEnetSHAgentPort = _HpAdvStkEnetSHAgentPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 3)
)
if mibBuilder.loadTexts:
    hpAdvStkEnetSHAgentPort.setStatus("current")
_Hp10BaseTHubPort_ObjectIdentity = ObjectIdentity
hp10BaseTHubPort = _Hp10BaseTHubPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 4)
)
if mibBuilder.loadTexts:
    hp10BaseTHubPort.setStatus("current")
_Hp10BaseTHubAgentPort_ObjectIdentity = ObjectIdentity
hp10BaseTHubAgentPort = _Hp10BaseTHubAgentPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 5)
)
if mibBuilder.loadTexts:
    hp10BaseTHubAgentPort.setStatus("current")
_Hp10T100THubPort_ObjectIdentity = ObjectIdentity
hp10T100THubPort = _Hp10T100THubPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 6)
)
if mibBuilder.loadTexts:
    hp10T100THubPort.setStatus("current")
_Hp100BaseTHubAgentPort_ObjectIdentity = ObjectIdentity
hp100BaseTHubAgentPort = _Hp100BaseTHubAgentPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 8, 7)
)
if mibBuilder.loadTexts:
    hp100BaseTHubAgentPort.setStatus("current")
_HpicfEnetChipSets_ObjectIdentity = ObjectIdentity
hpicfEnetChipSets = _HpicfEnetChipSets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 9)
)
_HpicfEnetChipSetHydra_ObjectIdentity = ObjectIdentity
hpicfEnetChipSetHydra = _HpicfEnetChipSetHydra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 9, 1)
)
if mibBuilder.loadTexts:
    hpicfEnetChipSetHydra.setStatus("current")
_HpicfEnetChipSetGT48001_ObjectIdentity = ObjectIdentity
hpicfEnetChipSetGT48001 = _HpicfEnetChipSetGT48001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 9, 2)
)
if mibBuilder.loadTexts:
    hpicfEnetChipSetGT48001.setStatus("current")
_HpicfEnetChipSetPentagon_ObjectIdentity = ObjectIdentity
hpicfEnetChipSetPentagon = _HpicfEnetChipSetPentagon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 9, 3)
)
if mibBuilder.loadTexts:
    hpicfEnetChipSetPentagon.setStatus("current")
_HpicfSwitchPorts_ObjectIdentity = ObjectIdentity
hpicfSwitchPorts = _HpicfSwitchPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10)
)
_HpicfSwitchPort10T100TX_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10T100TX = _HpicfSwitchPort10T100TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 1)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10T100TX.setStatus("current")
_HpicfSwitchPort100FX_ObjectIdentity = ObjectIdentity
hpicfSwitchPort100FX = _HpicfSwitchPort100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 2)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort100FX.setStatus("current")
_HpicfSwitchPort10FL_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10FL = _HpicfSwitchPort10FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 3)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10FL.setStatus("current")
_HpicfSwitchPort1000SX_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000SX = _HpicfSwitchPort1000SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 4)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000SX.setStatus("current")
_HpicfSwitchPort10T_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10T = _HpicfSwitchPort10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 5)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10T.setStatus("current")
_HpicfSwitchPort1000LX_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000LX = _HpicfSwitchPort1000LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 6)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000LX.setStatus("current")
_HpicfSwitchPort1000T_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000T = _HpicfSwitchPort1000T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 7)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000T.setStatus("current")
_HpicfSwitchPort1000Stk_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000Stk = _HpicfSwitchPort1000Stk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 8)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000Stk.setStatus("current")
_HpicfSwitchPort1000LH_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000LH = _HpicfSwitchPort1000LH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 9)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000LH.setStatus("current")
_HpicfSwitchPort10GigBaseCX4_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseCX4 = _HpicfSwitchPort10GigBaseCX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 10)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseCX4.setStatus("current")
_HpicfSwitchPort1000ESP_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000ESP = _HpicfSwitchPort1000ESP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 11)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000ESP.setStatus("current")
_HpicfSwitchPort10GigBaseSR_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseSR = _HpicfSwitchPort10GigBaseSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 12)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseSR.setStatus("current")
_HpicfSwitchPort10GigBaseER_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseER = _HpicfSwitchPort10GigBaseER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 13)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseER.setStatus("current")
_HpicfSwitchPort10GigBaseLR_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseLR = _HpicfSwitchPort10GigBaseLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 14)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseLR.setStatus("current")
_HpicfSwitchPort100GEN_ObjectIdentity = ObjectIdentity
hpicfSwitchPort100GEN = _HpicfSwitchPort100GEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 15)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort100GEN.setStatus("current")
_HpicfSwitchPort1000GEN_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000GEN = _HpicfSwitchPort1000GEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 16)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000GEN.setStatus("current")
_HpicfSwitchPort10GigBaseGEN_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseGEN = _HpicfSwitchPort10GigBaseGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 17)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseGEN.setStatus("current")
_HpicfSwitchPort100BXD_ObjectIdentity = ObjectIdentity
hpicfSwitchPort100BXD = _HpicfSwitchPort100BXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 18)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort100BXD.setStatus("current")
_HpicfSwitchPort100BXU_ObjectIdentity = ObjectIdentity
hpicfSwitchPort100BXU = _HpicfSwitchPort100BXU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 19)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort100BXU.setStatus("current")
_HpicfSwitchPort1000BXD_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000BXD = _HpicfSwitchPort1000BXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 20)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000BXD.setStatus("current")
_HpicfSwitchPort1000BXU_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000BXU = _HpicfSwitchPort1000BXU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 21)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000BXU.setStatus("current")
_HpicfSwitchPort10GigBaseLRM_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseLRM = _HpicfSwitchPort10GigBaseLRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 22)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseLRM.setStatus("current")
_HpicfSwitchPortSFPplusSR_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusSR = _HpicfSwitchPortSFPplusSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 23)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusSR.setStatus("current")
_HpicfSwitchPortSFPplusLR_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusLR = _HpicfSwitchPortSFPplusLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 24)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusLR.setStatus("current")
_HpicfSwitchPortSFPplusLRM_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusLRM = _HpicfSwitchPortSFPplusLRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 25)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusLRM.setStatus("current")
_HpicfSwitchPortSFPplusDAC_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDAC = _HpicfSwitchPortSFPplusDAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 26)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDAC.setStatus("current")
_HpicfSwitchPortSFPplusDA1_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA1 = _HpicfSwitchPortSFPplusDA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 27)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA1.setStatus("current")
_HpicfSwitchPortSFPplusDA2_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA2 = _HpicfSwitchPortSFPplusDA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 28)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA2.setStatus("current")
_HpicfSwitchPortSFPplusDA3_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA3 = _HpicfSwitchPortSFPplusDA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 29)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA3.setStatus("current")
_HpicfSwitchPortSFPplusDA5_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA5 = _HpicfSwitchPortSFPplusDA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 30)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA5.setStatus("current")
_HpicfSwitchPortSFPplusDA7_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA7 = _HpicfSwitchPortSFPplusDA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 31)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA7.setStatus("current")
_HpicfSwitchPortSFPplusDA10_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA10 = _HpicfSwitchPortSFPplusDA10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 32)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA10.setStatus("current")
_HpicfSwitchPortSFPplusDA15_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA15 = _HpicfSwitchPortSFPplusDA15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 33)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA15.setStatus("current")
_HpicfSwitchPortSFPplusDA20_ObjectIdentity = ObjectIdentity
hpicfSwitchPortSFPplusDA20 = _HpicfSwitchPortSFPplusDA20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 34)
)
if mibBuilder.loadTexts:
    hpicfSwitchPortSFPplusDA20.setStatus("current")
_HpicfSwitchPort10GigBaseT_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseT = _HpicfSwitchPort10GigBaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 35)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseT.setStatus("current")
_HpicfSwitchPort10GigBaseTSH_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseTSH = _HpicfSwitchPort10GigBaseTSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 36)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseTSH.setStatus("current")
_HpicfSwitchPort10GigBaseTLH_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseTLH = _HpicfSwitchPort10GigBaseTLH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 37)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseTLH.setStatus("current")
_HpicfSwitchPort10GigBaseSTK_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigBaseSTK = _HpicfSwitchPort10GigBaseSTK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 38)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigBaseSTK.setStatus("current")
_HpicfSwitchPort1000CWDM1470_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1470 = _HpicfSwitchPort1000CWDM1470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 39)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1470.setStatus("current")
_HpicfSwitchPort1000CWDM1490_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1490 = _HpicfSwitchPort1000CWDM1490_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 40)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1490.setStatus("current")
_HpicfSwitchPort1000CWDM1510_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1510 = _HpicfSwitchPort1000CWDM1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 41)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1510.setStatus("current")
_HpicfSwitchPort1000CWDM1530_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1530 = _HpicfSwitchPort1000CWDM1530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 42)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1530.setStatus("current")
_HpicfSwitchPort1000CWDM1550_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1550 = _HpicfSwitchPort1000CWDM1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 43)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1550.setStatus("current")
_HpicfSwitchPort1000CWDM1570_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1570 = _HpicfSwitchPort1000CWDM1570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 44)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1570.setStatus("current")
_HpicfSwitchPort1000CWDM1590_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1590 = _HpicfSwitchPort1000CWDM1590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 45)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1590.setStatus("current")
_HpicfSwitchPort1000CWDM1610_ObjectIdentity = ObjectIdentity
hpicfSwitchPort1000CWDM1610 = _HpicfSwitchPort1000CWDM1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 46)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort1000CWDM1610.setStatus("current")
_HpicfSwitchPort10GigCWDM1470_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1470 = _HpicfSwitchPort10GigCWDM1470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 47)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1470.setStatus("current")
_HpicfSwitchPort10GigCWDM1490_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1490 = _HpicfSwitchPort10GigCWDM1490_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 48)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1490.setStatus("current")
_HpicfSwitchPort10GigCWDM1510_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1510 = _HpicfSwitchPort10GigCWDM1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 49)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1510.setStatus("current")
_HpicfSwitchPort10GigCWDM1530_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1530 = _HpicfSwitchPort10GigCWDM1530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 50)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1530.setStatus("current")
_HpicfSwitchPort10GigCWDM1550_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1550 = _HpicfSwitchPort10GigCWDM1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 51)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1550.setStatus("current")
_HpicfSwitchPort10GigCWDM1570_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1570 = _HpicfSwitchPort10GigCWDM1570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 52)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1570.setStatus("current")
_HpicfSwitchPort10GigCWDM1590_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1590 = _HpicfSwitchPort10GigCWDM1590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 53)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1590.setStatus("current")
_HpicfSwitchPort10GigCWDM1611_ObjectIdentity = ObjectIdentity
hpicfSwitchPort10GigCWDM1611 = _HpicfSwitchPort10GigCWDM1611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 54)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort10GigCWDM1611.setStatus("current")
_HpicfSwitchPort5GigBaseT_ObjectIdentity = ObjectIdentity
hpicfSwitchPort5GigBaseT = _HpicfSwitchPort5GigBaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 10, 55)
)
if mibBuilder.loadTexts:
    hpicfSwitchPort5GigBaseT.setStatus("current")
_HpicfMAUTypes_ObjectIdentity = ObjectIdentity
hpicfMAUTypes = _HpicfMAUTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11)
)
_HpicfMauType1000BaseSXHD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseSXHD = _HpicfMauType1000BaseSXHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 1)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseSXHD.setStatus("deprecated")
_HpicfMauType1000BaseSXFD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseSXFD = _HpicfMauType1000BaseSXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 2)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseSXFD.setStatus("deprecated")
_HpicfMauType1000BaseLXHD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseLXHD = _HpicfMauType1000BaseLXHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 3)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseLXHD.setStatus("deprecated")
_HpicfMauType1000BaseLXFD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseLXFD = _HpicfMauType1000BaseLXFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 4)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseLXFD.setStatus("deprecated")
_HpicfMauType1000BaseTHD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseTHD = _HpicfMauType1000BaseTHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 5)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseTHD.setStatus("deprecated")
_HpicfMauType1000BaseTFD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseTFD = _HpicfMauType1000BaseTFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 6)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseTFD.setStatus("deprecated")
_HpicfMauType1000BaseStkHD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseStkHD = _HpicfMauType1000BaseStkHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 7)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseStkHD.setStatus("current")
_HpicfMauType1000BaseStkFD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseStkFD = _HpicfMauType1000BaseStkFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 8)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseStkFD.setStatus("current")
_HpicfMauType1000BaseLHFD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseLHFD = _HpicfMauType1000BaseLHFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 9)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseLHFD.setStatus("current")
_HpicfMauType1000BaseEspPCS_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseEspPCS = _HpicfMauType1000BaseEspPCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 10)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseEspPCS.setStatus("current")
_HpicfMauType1000BaseEspG_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseEspG = _HpicfMauType1000BaseEspG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 11)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseEspG.setStatus("current")
_HpicfMauType10GigBaseCX4_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseCX4 = _HpicfMauType10GigBaseCX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 12)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseCX4.setStatus("current")
_HpicfMauType10GigBaseSR_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseSR = _HpicfMauType10GigBaseSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 13)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseSR.setStatus("current")
_HpicfMauType10GigBaseER_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseER = _HpicfMauType10GigBaseER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 14)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseER.setStatus("current")
_HpicfMauType10GigBaseLR_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseLR = _HpicfMauType10GigBaseLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 15)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseLR.setStatus("current")
_HpicfMauType100BaseGEN_ObjectIdentity = ObjectIdentity
hpicfMauType100BaseGEN = _HpicfMauType100BaseGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 16)
)
if mibBuilder.loadTexts:
    hpicfMauType100BaseGEN.setStatus("current")
_HpicfMauType1000BaseGEN_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseGEN = _HpicfMauType1000BaseGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 17)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseGEN.setStatus("current")
_HpicfMauType10GigBaseGEN_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseGEN = _HpicfMauType10GigBaseGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 18)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseGEN.setStatus("current")
_HpicfMauType100BaseBXD_ObjectIdentity = ObjectIdentity
hpicfMauType100BaseBXD = _HpicfMauType100BaseBXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 19)
)
if mibBuilder.loadTexts:
    hpicfMauType100BaseBXD.setStatus("current")
_HpicfMauType100BaseBXU_ObjectIdentity = ObjectIdentity
hpicfMauType100BaseBXU = _HpicfMauType100BaseBXU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 20)
)
if mibBuilder.loadTexts:
    hpicfMauType100BaseBXU.setStatus("current")
_HpicfMauType1000BaseBXD_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseBXD = _HpicfMauType1000BaseBXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 21)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseBXD.setStatus("current")
_HpicfMauType1000BaseBXU_ObjectIdentity = ObjectIdentity
hpicfMauType1000BaseBXU = _HpicfMauType1000BaseBXU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 22)
)
if mibBuilder.loadTexts:
    hpicfMauType1000BaseBXU.setStatus("current")
_HpicfMauType10GigBaseLRM_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseLRM = _HpicfMauType10GigBaseLRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 23)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseLRM.setStatus("current")
_HpicfMauTypeSFPplusSR_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusSR = _HpicfMauTypeSFPplusSR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 24)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusSR.setStatus("current")
_HpicfMauTypeSFPplusLR_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusLR = _HpicfMauTypeSFPplusLR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 25)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusLR.setStatus("current")
_HpicfMauTypeSFPplusLRM_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusLRM = _HpicfMauTypeSFPplusLRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 26)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusLRM.setStatus("current")
_HpicfMauTypeSFPplusDAC_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDAC = _HpicfMauTypeSFPplusDAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 27)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDAC.setStatus("current")
_HpicfMauTypeSFPplusDA1_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA1 = _HpicfMauTypeSFPplusDA1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 28)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA1.setStatus("current")
_HpicfMauTypeSFPplusDA2_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA2 = _HpicfMauTypeSFPplusDA2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 29)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA2.setStatus("current")
_HpicfMauTypeSFPplusDA3_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA3 = _HpicfMauTypeSFPplusDA3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 30)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA3.setStatus("current")
_HpicfMauTypeSFPplusDA5_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA5 = _HpicfMauTypeSFPplusDA5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 31)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA5.setStatus("current")
_HpicfMauTypeSFPplusDA7_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA7 = _HpicfMauTypeSFPplusDA7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 32)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA7.setStatus("current")
_HpicfMauTypeSFPplusDA10_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA10 = _HpicfMauTypeSFPplusDA10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 33)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA10.setStatus("current")
_HpicfMauTypeSFPplusDA15_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA15 = _HpicfMauTypeSFPplusDA15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 34)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA15.setStatus("current")
_HpicfMauTypeSFPplusDA20_ObjectIdentity = ObjectIdentity
hpicfMauTypeSFPplusDA20 = _HpicfMauTypeSFPplusDA20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 35)
)
if mibBuilder.loadTexts:
    hpicfMauTypeSFPplusDA20.setStatus("current")
_HpicfMauType10GigBaseT_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseT = _HpicfMauType10GigBaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 36)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseT.setStatus("current")
_HpicfMauType10GigBaseTSH_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseTSH = _HpicfMauType10GigBaseTSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 37)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseTSH.setStatus("current")
_HpicfMauType10GigBaseTLH_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseTLH = _HpicfMauType10GigBaseTLH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 38)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseTLH.setStatus("current")
_HpicfMauType10GigBaseSTK_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseSTK = _HpicfMauType10GigBaseSTK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 39)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseSTK.setStatus("current")
_HpicfMauType1000CWDM1470_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1470 = _HpicfMauType1000CWDM1470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 40)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1470.setStatus("current")
_HpicfMauType1000CWDM1490_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1490 = _HpicfMauType1000CWDM1490_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 41)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1490.setStatus("current")
_HpicfMauType1000CWDM1510_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1510 = _HpicfMauType1000CWDM1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 42)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1510.setStatus("current")
_HpicfMauType1000CWDM1530_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1530 = _HpicfMauType1000CWDM1530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 43)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1530.setStatus("current")
_HpicfMauType1000CWDM1550_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1550 = _HpicfMauType1000CWDM1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 44)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1550.setStatus("current")
_HpicfMauType1000CWDM1570_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1570 = _HpicfMauType1000CWDM1570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 45)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1570.setStatus("current")
_HpicfMauType1000CWDM1590_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1590 = _HpicfMauType1000CWDM1590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 46)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1590.setStatus("current")
_HpicfMauType1000CWDM1610_ObjectIdentity = ObjectIdentity
hpicfMauType1000CWDM1610 = _HpicfMauType1000CWDM1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 47)
)
if mibBuilder.loadTexts:
    hpicfMauType1000CWDM1610.setStatus("current")
_HpicfMauType10GigCWDM1470_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1470 = _HpicfMauType10GigCWDM1470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 48)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1470.setStatus("current")
_HpicfMauType10GigCWDM1490_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1490 = _HpicfMauType10GigCWDM1490_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 49)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1490.setStatus("current")
_HpicfMauType10GigCWDM1510_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1510 = _HpicfMauType10GigCWDM1510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 50)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1510.setStatus("current")
_HpicfMauType10GigCWDM1530_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1530 = _HpicfMauType10GigCWDM1530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 51)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1530.setStatus("current")
_HpicfMauType10GigCWDM1550_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1550 = _HpicfMauType10GigCWDM1550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 52)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1550.setStatus("current")
_HpicfMauType10GigCWDM1570_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1570 = _HpicfMauType10GigCWDM1570_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 53)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1570.setStatus("current")
_HpicfMauType10GigCWDM1590_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1590 = _HpicfMauType10GigCWDM1590_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 54)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1590.setStatus("current")
_HpicfMauType10GigCWDM1610_ObjectIdentity = ObjectIdentity
hpicfMauType10GigCWDM1610 = _HpicfMauType10GigCWDM1610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 55)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigCWDM1610.setStatus("current")
_HpicfMauType10GigBaseESP_ObjectIdentity = ObjectIdentity
hpicfMauType10GigBaseESP = _HpicfMauType10GigBaseESP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 56)
)
if mibBuilder.loadTexts:
    hpicfMauType10GigBaseESP.setStatus("current")
_HpicfMauTypeQSFPpluseSR4_ObjectIdentity = ObjectIdentity
hpicfMauTypeQSFPpluseSR4 = _HpicfMauTypeQSFPpluseSR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 57)
)
if mibBuilder.loadTexts:
    hpicfMauTypeQSFPpluseSR4.setStatus("current")
_HpicfMauTypeQSFPplusGEN_ObjectIdentity = ObjectIdentity
hpicfMauTypeQSFPplusGEN = _HpicfMauTypeQSFPplusGEN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 58)
)
if mibBuilder.loadTexts:
    hpicfMauTypeQSFPplusGEN.setStatus("current")
_HpicfMauTypeQSFPplusBIDI_ObjectIdentity = ObjectIdentity
hpicfMauTypeQSFPplusBIDI = _HpicfMauTypeQSFPplusBIDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 59)
)
if mibBuilder.loadTexts:
    hpicfMauTypeQSFPplusBIDI.setStatus("current")
_HpicfMauType5GigBaseT_ObjectIdentity = ObjectIdentity
hpicfMauType5GigBaseT = _HpicfMauType5GigBaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 8, 11, 60)
)
if mibBuilder.loadTexts:
    hpicfMauType5GigBaseT.setStatus("current")
_HpEtherSwitch_ObjectIdentity = ObjectIdentity
hpEtherSwitch = _HpEtherSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11)
)
_HpAdvSwitch2000_ObjectIdentity = ObjectIdentity
hpAdvSwitch2000 = _HpAdvSwitch2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1)
)
if mibBuilder.loadTexts:
    hpAdvSwitch2000.setStatus("current")
_HpSwitchPortModuleET4_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleET4 = _HpSwitchPortModuleET4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleET4.setStatus("current")
_HpSwitchPortModuleVG2_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleVG2 = _HpSwitchPortModuleVG2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleVG2.setStatus("current")
_HpSwitchPortModule10FL_ObjectIdentity = ObjectIdentity
hpSwitchPortModule10FL = _HpSwitchPortModule10FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 3)
)
if mibBuilder.loadTexts:
    hpSwitchPortModule10FL.setStatus("current")
_HpSwitchPortModuleFDDI_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleFDDI = _HpSwitchPortModuleFDDI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 4)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleFDDI.setStatus("current")
_HpSwitchPortModuleTX2_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleTX2 = _HpSwitchPortModuleTX2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 5)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleTX2.setStatus("current")
_HpSwitchPortModuleATM_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleATM = _HpSwitchPortModuleATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 1, 6)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleATM.setStatus("current")
_HpAdvSwitch2000B_ObjectIdentity = ObjectIdentity
hpAdvSwitch2000B = _HpAdvSwitch2000B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 2)
)
if mibBuilder.loadTexts:
    hpAdvSwitch2000B.setStatus("current")
_HpAdvSwitch800T_ObjectIdentity = ObjectIdentity
hpAdvSwitch800T = _HpAdvSwitch800T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 3)
)
if mibBuilder.loadTexts:
    hpAdvSwitch800T.setStatus("current")
_HpAdvSwitch200_ObjectIdentity = ObjectIdentity
hpAdvSwitch200 = _HpAdvSwitch200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4)
)
if mibBuilder.loadTexts:
    hpAdvSwitch200.setStatus("current")
_HpAdvSwitch208T_ObjectIdentity = ObjectIdentity
hpAdvSwitch208T = _HpAdvSwitch208T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4, 1)
)
_HpAdvSwitch208VG_ObjectIdentity = ObjectIdentity
hpAdvSwitch208VG = _HpAdvSwitch208VG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4, 2)
)
_HpAdvSwitch224T_ObjectIdentity = ObjectIdentity
hpAdvSwitch224T = _HpAdvSwitch224T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4, 3)
)
_HpAdvSwitch224VG_ObjectIdentity = ObjectIdentity
hpAdvSwitch224VG = _HpAdvSwitch224VG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 4, 4)
)
_HpSwitch212M_ObjectIdentity = ObjectIdentity
hpSwitch212M = _HpSwitch212M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 5)
)
if mibBuilder.loadTexts:
    hpSwitch212M.setStatus("current")
_HpSwitch224M_ObjectIdentity = ObjectIdentity
hpSwitch224M = _HpSwitch224M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 6)
)
if mibBuilder.loadTexts:
    hpSwitch224M.setStatus("current")
_HpSwitch8000_ObjectIdentity = ObjectIdentity
hpSwitch8000 = _HpSwitch8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7)
)
if mibBuilder.loadTexts:
    hpSwitch8000.setStatus("current")
_HpSwitchPortModule100TX8_ObjectIdentity = ObjectIdentity
hpSwitchPortModule100TX8 = _HpSwitchPortModule100TX8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 1)
)
if mibBuilder.loadTexts:
    hpSwitchPortModule100TX8.setStatus("current")
_HpSwitchPortModule100FX4_ObjectIdentity = ObjectIdentity
hpSwitchPortModule100FX4 = _HpSwitchPortModule100FX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 2)
)
if mibBuilder.loadTexts:
    hpSwitchPortModule100FX4.setStatus("current")
_HpSwitchPortModule10FL4_ObjectIdentity = ObjectIdentity
hpSwitchPortModule10FL4 = _HpSwitchPortModule10FL4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 3)
)
if mibBuilder.loadTexts:
    hpSwitchPortModule10FL4.setStatus("current")
_HpSwitchPortModuleGigSX_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleGigSX = _HpSwitchPortModuleGigSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 4)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleGigSX.setStatus("current")
_HpSwitchPortModuleGigLX_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleGigLX = _HpSwitchPortModuleGigLX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 5)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleGigLX.setStatus("current")
_HpSwitchPortModuleTwoGig_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleTwoGig = _HpSwitchPortModuleTwoGig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 6)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleTwoGig.setStatus("current")
_HpSwitchPortModuleGigStk_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleGigStk = _HpSwitchPortModuleGigStk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 7)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleGigStk.setStatus("current")
_HpSwitchPortModuleGigT_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleGigT = _HpSwitchPortModuleGigT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 7, 8)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleGigT.setStatus("current")
_HpSwitch1600_ObjectIdentity = ObjectIdentity
hpSwitch1600 = _HpSwitch1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 8)
)
if mibBuilder.loadTexts:
    hpSwitch1600.setStatus("current")
_HpSwitch4000_ObjectIdentity = ObjectIdentity
hpSwitch4000 = _HpSwitch4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 9)
)
if mibBuilder.loadTexts:
    hpSwitch4000.setStatus("current")
_HpSwitch2400_ObjectIdentity = ObjectIdentity
hpSwitch2400 = _HpSwitch2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 10)
)
if mibBuilder.loadTexts:
    hpSwitch2400.setStatus("current")
_HpSwitch2424_ObjectIdentity = ObjectIdentity
hpSwitch2424 = _HpSwitch2424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 11)
)
if mibBuilder.loadTexts:
    hpSwitch2424.setStatus("current")
_HpSwitch9308_ObjectIdentity = ObjectIdentity
hpSwitch9308 = _HpSwitch9308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 13)
)
if mibBuilder.loadTexts:
    hpSwitch9308.setStatus("current")
_HpSwitch9304_ObjectIdentity = ObjectIdentity
hpSwitch9304 = _HpSwitch9304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 14)
)
if mibBuilder.loadTexts:
    hpSwitch9304.setStatus("current")
_HpSwitch6308_ObjectIdentity = ObjectIdentity
hpSwitch6308 = _HpSwitch6308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 15)
)
if mibBuilder.loadTexts:
    hpSwitch6308.setStatus("current")
_HpSwitch6208_ObjectIdentity = ObjectIdentity
hpSwitch6208 = _HpSwitch6208_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 16)
)
if mibBuilder.loadTexts:
    hpSwitch6208.setStatus("current")
_HpSwitchJ4819A_ObjectIdentity = ObjectIdentity
hpSwitchJ4819A = _HpSwitchJ4819A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17)
)
if mibBuilder.loadTexts:
    hpSwitchJ4819A.setStatus("current")
_HpSwitchPortModuleJ4820A_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4820A = _HpSwitchPortModuleJ4820A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 1)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4820A.setStatus("current")
_HpSwitchPortModuleJ4821A_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4821A = _HpSwitchPortModuleJ4821A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 2)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4821A.setStatus("current")
_HpSwitchPortModuleJ4878A_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4878A = _HpSwitchPortModuleJ4878A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 3)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4878A.setStatus("current")
_HpSwitchModuleJ4852A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4852A = _HpSwitchModuleJ4852A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4852A.setStatus("current")
_HpSwitchModuleJ8161A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8161A = _HpSwitchModuleJ8161A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8161A.setStatus("current")
_HpSwitchModuleJ4907A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4907A = _HpSwitchModuleJ4907A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4907A.setStatus("current")
_HpSwitchModuleJ8162A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8162A = _HpSwitchModuleJ8162A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 7)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8162A.setStatus("current")
_HpSwitchPortModuleJ4820B_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4820B = _HpSwitchPortModuleJ4820B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 8)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4820B.setStatus("current")
_HpSwitchPortModuleJ4821B_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4821B = _HpSwitchPortModuleJ4821B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 9)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4821B.setStatus("current")
_HpSwitchPortModuleJ4878B_ObjectIdentity = ObjectIdentity
hpSwitchPortModuleJ4878B = _HpSwitchPortModuleJ4878B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 10)
)
if mibBuilder.loadTexts:
    hpSwitchPortModuleJ4878B.setStatus("current")
_HpSwitchModuleJ9001A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9001A = _HpSwitchModuleJ9001A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 11)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9001A.setStatus("current")
_HpSwitchModuleJ9003A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9003A = _HpSwitchModuleJ9003A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 12)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9003A.setStatus("current")
_HpSwitchModuleJ8988A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8988A = _HpSwitchModuleJ8988A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 17, 13)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8988A.setStatus("current")
_HpSwitchJ4812A_ObjectIdentity = ObjectIdentity
hpSwitchJ4812A = _HpSwitchJ4812A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 18)
)
if mibBuilder.loadTexts:
    hpSwitchJ4812A.setStatus("current")
_HpSwitchModuleJ4812A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4812A = _HpSwitchModuleJ4812A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 18, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4812A.setStatus("current")
_HpSwitchJ4813A_ObjectIdentity = ObjectIdentity
hpSwitchJ4813A = _HpSwitchJ4813A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 19)
)
if mibBuilder.loadTexts:
    hpSwitchJ4813A.setStatus("current")
_HpSwitchModuleJ4813A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4813A = _HpSwitchModuleJ4813A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 19, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4813A.setStatus("current")
_HpSwitchJ4850A_ObjectIdentity = ObjectIdentity
hpSwitchJ4850A = _HpSwitchJ4850A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 20)
)
if mibBuilder.loadTexts:
    hpSwitchJ4850A.setStatus("current")
_HpSwitchJ4815A_ObjectIdentity = ObjectIdentity
hpSwitchJ4815A = _HpSwitchJ4815A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 21)
)
if mibBuilder.loadTexts:
    hpSwitchJ4815A.setStatus("current")
_HpSwitchJ4851A_ObjectIdentity = ObjectIdentity
hpSwitchJ4851A = _HpSwitchJ4851A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 22)
)
if mibBuilder.loadTexts:
    hpSwitchJ4851A.setStatus("current")
_HpSwitchJ4865A_ObjectIdentity = ObjectIdentity
hpSwitchJ4865A = _HpSwitchJ4865A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23)
)
if mibBuilder.loadTexts:
    hpSwitchJ4865A.setStatus("current")
_HpSwitchModuleJ4862A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4862A = _HpSwitchModuleJ4862A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4862A.setStatus("current")
_HpSwitchModuleJ4863A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4863A = _HpSwitchModuleJ4863A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4863A.setStatus("current")
_HpSwitchModuleJ4864A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4864A = _HpSwitchModuleJ4864A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4864A.setStatus("current")
_HpSwitchModuleJ4862B_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4862B = _HpSwitchModuleJ4862B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4862B.setStatus("current")
_HpSwitchModuleJ4893A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4893A = _HpSwitchModuleJ4893A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4893A.setStatus("current")
_HpSwitchModuleJ4892A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4892A = _HpSwitchModuleJ4892A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4892A.setStatus("current")
_HpSwitchModuleJ4908A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4908A = _HpSwitchModuleJ4908A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 23, 7)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4908A.setStatus("current")
_HpSwitchA6713A_ObjectIdentity = ObjectIdentity
hpSwitchA6713A = _HpSwitchA6713A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 24)
)
if mibBuilder.loadTexts:
    hpSwitchA6713A.setStatus("current")
_HpSwitchModuleA6713A_ObjectIdentity = ObjectIdentity
hpSwitchModuleA6713A = _HpSwitchModuleA6713A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 24, 11)
)
if mibBuilder.loadTexts:
    hpSwitchModuleA6713A.setStatus("current")
_HpSwitchA6716A_ObjectIdentity = ObjectIdentity
hpSwitchA6716A = _HpSwitchA6716A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 25)
)
if mibBuilder.loadTexts:
    hpSwitchA6716A.setStatus("current")
_HpSwitchModuleA6716A_ObjectIdentity = ObjectIdentity
hpSwitchModuleA6716A = _HpSwitchModuleA6716A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 25, 12)
)
if mibBuilder.loadTexts:
    hpSwitchModuleA6716A.setStatus("current")
_HpSwitchA6717A_ObjectIdentity = ObjectIdentity
hpSwitchA6717A = _HpSwitchA6717A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 26)
)
if mibBuilder.loadTexts:
    hpSwitchA6717A.setStatus("current")
_HpSwitchModuleA6717A_ObjectIdentity = ObjectIdentity
hpSwitchModuleA6717A = _HpSwitchModuleA6717A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 26, 13)
)
if mibBuilder.loadTexts:
    hpSwitchModuleA6717A.setStatus("current")
_HpSwitchJ4887A_ObjectIdentity = ObjectIdentity
hpSwitchJ4887A = _HpSwitchJ4887A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 27)
)
if mibBuilder.loadTexts:
    hpSwitchJ4887A.setStatus("current")
_HpSwitchJ4874A_ObjectIdentity = ObjectIdentity
hpSwitchJ4874A = _HpSwitchJ4874A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 28)
)
if mibBuilder.loadTexts:
    hpSwitchJ4874A.setStatus("current")
_HpSwitchJ4899A_ObjectIdentity = ObjectIdentity
hpSwitchJ4899A = _HpSwitchJ4899A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 29)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899A.setStatus("current")
_HpSwitchModuleJ4899A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4899A = _HpSwitchModuleJ4899A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 29, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4899A.setStatus("current")
_HpSwitchJ4902A_ObjectIdentity = ObjectIdentity
hpSwitchJ4902A = _HpSwitchJ4902A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 30)
)
if mibBuilder.loadTexts:
    hpSwitchJ4902A.setStatus("current")
_HpSwitchModuleJ4902A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4902A = _HpSwitchModuleJ4902A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 30, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4902A.setStatus("current")
_HpSwitchJ4903A_ObjectIdentity = ObjectIdentity
hpSwitchJ4903A = _HpSwitchJ4903A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 31)
)
if mibBuilder.loadTexts:
    hpSwitchJ4903A.setStatus("current")
_HpSwitchModuleJ4903A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4903A = _HpSwitchModuleJ4903A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 31, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4903A.setStatus("current")
_HpSwitchModuleJ8434A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8434A = _HpSwitchModuleJ8434A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 31, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8434A.setStatus("current")
_HpSwitchModuleJ8435A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8435A = _HpSwitchModuleJ8435A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 31, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8435A.setStatus("current")
_HpSwitchJ4904A_ObjectIdentity = ObjectIdentity
hpSwitchJ4904A = _HpSwitchJ4904A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 32)
)
if mibBuilder.loadTexts:
    hpSwitchJ4904A.setStatus("current")
_HpSwitchModuleJ4904A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4904A = _HpSwitchModuleJ4904A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 32, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4904A.setStatus("current")
_HpSwitchProliant_ObjectIdentity = ObjectIdentity
hpSwitchProliant = _HpSwitchProliant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 33)
)
if mibBuilder.loadTexts:
    hpSwitchProliant.setStatus("current")
_HpSwitchJ4900A_ObjectIdentity = ObjectIdentity
hpSwitchJ4900A = _HpSwitchJ4900A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 34)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900A.setStatus("current")
_HpSwitchModuleJ4900A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4900A = _HpSwitchModuleJ4900A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 34, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4900A.setStatus("current")
_HpSwitchJ8165A_ObjectIdentity = ObjectIdentity
hpSwitchJ8165A = _HpSwitchJ8165A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 35)
)
if mibBuilder.loadTexts:
    hpSwitchJ8165A.setStatus("current")
_HpSwitchModuleJ8165A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8165A = _HpSwitchModuleJ8165A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 35, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8165A.setStatus("current")
_HpSwitchJ8164A_ObjectIdentity = ObjectIdentity
hpSwitchJ8164A = _HpSwitchJ8164A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 36)
)
if mibBuilder.loadTexts:
    hpSwitchJ8164A.setStatus("current")
_HpSwitchModuleJ8164A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8164A = _HpSwitchModuleJ8164A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 36, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8164A.setStatus("current")
_HpSwitchJ8130A_ObjectIdentity = ObjectIdentity
hpSwitchJ8130A = _HpSwitchJ8130A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 37)
)
if mibBuilder.loadTexts:
    hpSwitchJ8130A.setStatus("obsolete")
_HpSwitchJ8133A_ObjectIdentity = ObjectIdentity
hpSwitchJ8133A = _HpSwitchJ8133A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 38)
)
if mibBuilder.loadTexts:
    hpSwitchJ8133A.setStatus("current")
_HpSwitchJ8153A_ObjectIdentity = ObjectIdentity
hpSwitchJ8153A = _HpSwitchJ8153A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 39)
)
if mibBuilder.loadTexts:
    hpSwitchJ8153A.setStatus("current")
_HpSwitchJ8154A_ObjectIdentity = ObjectIdentity
hpSwitchJ8154A = _HpSwitchJ8154A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 40)
)
if mibBuilder.loadTexts:
    hpSwitchJ8154A.setStatus("current")
_HpSwitchJ8155A_ObjectIdentity = ObjectIdentity
hpSwitchJ8155A = _HpSwitchJ8155A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 41)
)
if mibBuilder.loadTexts:
    hpSwitchJ8155A.setStatus("current")
_HpSwitchJ4905A_ObjectIdentity = ObjectIdentity
hpSwitchJ4905A = _HpSwitchJ4905A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 42)
)
if mibBuilder.loadTexts:
    hpSwitchJ4905A.setStatus("current")
_HpSwitchModuleJ4905A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4905A = _HpSwitchModuleJ4905A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 42, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4905A.setStatus("current")
_HpSwitchJ4906A_ObjectIdentity = ObjectIdentity
hpSwitchJ4906A = _HpSwitchJ4906A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 43)
)
if mibBuilder.loadTexts:
    hpSwitchJ4906A.setStatus("current")
_HpSwitchModuleJ4906A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4906A = _HpSwitchModuleJ4906A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 43, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4906A.setStatus("current")
_HpSwitchJ4899B_ObjectIdentity = ObjectIdentity
hpSwitchJ4899B = _HpSwitchJ4899B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 44)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899B.setStatus("current")
_HpSwitchModuleJ4899B_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4899B = _HpSwitchModuleJ4899B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 44, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4899B.setStatus("current")
_HpSwitchJ4900B_ObjectIdentity = ObjectIdentity
hpSwitchJ4900B = _HpSwitchJ4900B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 45)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900B.setStatus("current")
_HpSwitchModuleJ4900B_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4900B = _HpSwitchModuleJ4900B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 45, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4900B.setStatus("current")
_HpSwitchJ8433A_ObjectIdentity = ObjectIdentity
hpSwitchJ8433A = _HpSwitchJ8433A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 48)
)
if mibBuilder.loadTexts:
    hpSwitchJ8433A.setStatus("current")
_HpSwitchModuleJ8433A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8433A = _HpSwitchModuleJ8433A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 48, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8433A.setStatus("current")
_HpSwitchJ8474A_ObjectIdentity = ObjectIdentity
hpSwitchJ8474A = _HpSwitchJ8474A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 49)
)
if mibBuilder.loadTexts:
    hpSwitchJ8474A.setStatus("current")
_HpSwitchModuleJ8474A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8474A = _HpSwitchModuleJ8474A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 49, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8474A.setStatus("current")
_HpSwitchJ8697A_ObjectIdentity = ObjectIdentity
hpSwitchJ8697A = _HpSwitchJ8697A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50)
)
if mibBuilder.loadTexts:
    hpSwitchJ8697A.setStatus("current")
_HpSwitchModuleJ8701A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8701A = _HpSwitchModuleJ8701A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8701A.setStatus("current")
_HpSwitchModuleJ8702A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8702A = _HpSwitchModuleJ8702A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8702A.setStatus("current")
_HpSwitchModuleJ8705A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8705A = _HpSwitchModuleJ8705A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8705A.setStatus("current")
_HpSwitchModuleJ8706A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8706A = _HpSwitchModuleJ8706A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8706A.setStatus("current")
_HpSwitchModuleJ8707A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8707A = _HpSwitchModuleJ8707A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8707A.setStatus("current")
_HpSwitchModuleJ8708A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8708A = _HpSwitchModuleJ8708A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8708A.setStatus("current")
_HpSwitchModuleJ87xxA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ87xxA = _HpSwitchModuleJ87xxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 7)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ87xxA.setStatus("current")
_HpSwitchModuleJ87yyA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ87yyA = _HpSwitchModuleJ87yyA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 8)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ87yyA.setStatus("current")
_HpSwitchModuleJ8694A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8694A = _HpSwitchModuleJ8694A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 9)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8694A.setStatus("current")
_HpSwitchModuleJ8726A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8726A = _HpSwitchModuleJ8726A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 10)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8726A.setStatus("current")
_HpSwitchModuleJ9051A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9051A = _HpSwitchModuleJ9051A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 14)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9051A.setStatus("current")
_HpSwitchModuleJ9052A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9052A = _HpSwitchModuleJ9052A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 15)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9052A.setStatus("current")
_HpSwitchModuleJ9154A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9154A = _HpSwitchModuleJ9154A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 16)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9154A.setStatus("current")
_HpSwitchModuleJ9155A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9155A = _HpSwitchModuleJ9155A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 17)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9155A.setStatus("current")
_HpSwitchModuleJ9446A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9446A = _HpSwitchModuleJ9446A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 18)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9446A.setStatus("current")
_HpSwitchModuleJ9307A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9307A = _HpSwitchModuleJ9307A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 19)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9307A.setStatus("current")
_HpSwitchModuleJ9308A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9308A = _HpSwitchModuleJ9308A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 20)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9308A.setStatus("current")
_HpSwitchModuleJ9478A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9478A = _HpSwitchModuleJ9478A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 21)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9478A.setStatus("current")
_HpSwitchModuleJ9309A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9309A = _HpSwitchModuleJ9309A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 22)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9309A.setStatus("current")
_HpSwitchModuleJ9312A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9312A = _HpSwitchModuleJ9312A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 23)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9312A.setStatus("current")
_HpSwitchModuleJ9534A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9534A = _HpSwitchModuleJ9534A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 24)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9534A.setStatus("current")
_HpSwitchModuleJ9535A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9535A = _HpSwitchModuleJ9535A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 25)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9535A.setStatus("current")
_HpSwitchModuleJ9536A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9536A = _HpSwitchModuleJ9536A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 26)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9536A.setStatus("current")
_HpSwitchModuleJ9537A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9537A = _HpSwitchModuleJ9537A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 27)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9537A.setStatus("current")
_HpSwitchModuleJ9538A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9538A = _HpSwitchModuleJ9538A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 28)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9538A.setStatus("current")
_HpSwitchModuleJ9546A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9546A = _HpSwitchModuleJ9546A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 29)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9546A.setStatus("current")
_HpSwitchModuleJ9547A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9547A = _HpSwitchModuleJ9547A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 30)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9547A.setStatus("current")
_HpSwitchModuleJ9548A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9548A = _HpSwitchModuleJ9548A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 31)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9548A.setStatus("current")
_HpSwitchModuleJ9549A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9549A = _HpSwitchModuleJ9549A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 32)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9549A.setStatus("current")
_HpSwitchModuleJ9550A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9550A = _HpSwitchModuleJ9550A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 33)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9550A.setStatus("current")
_HpSwitchAdvServicesModule_ObjectIdentity = ObjectIdentity
hpSwitchAdvServicesModule = _HpSwitchAdvServicesModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 34)
)
if mibBuilder.loadTexts:
    hpSwitchAdvServicesModule.setStatus("current")
_HpSwitchExtServicesModule_ObjectIdentity = ObjectIdentity
hpSwitchExtServicesModule = _HpSwitchExtServicesModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 35)
)
if mibBuilder.loadTexts:
    hpSwitchExtServicesModule.setStatus("current")
_HpSwitchModuleJ9485A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9485A = _HpSwitchModuleJ9485A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 36)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9485A.setStatus("current")
_HpSwitchModuleJ9637A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9637A = _HpSwitchModuleJ9637A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 37)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9637A.setStatus("current")
_HpSwitchV2ServicesModule_ObjectIdentity = ObjectIdentity
hpSwitchV2ServicesModule = _HpSwitchV2ServicesModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 50, 41)
)
if mibBuilder.loadTexts:
    hpSwitchV2ServicesModule.setStatus("current")
_HpSwitchJ8698A_ObjectIdentity = ObjectIdentity
hpSwitchJ8698A = _HpSwitchJ8698A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 51)
)
if mibBuilder.loadTexts:
    hpSwitchJ8698A.setStatus("current")
_HpSwitchJ8770A_ObjectIdentity = ObjectIdentity
hpSwitchJ8770A = _HpSwitchJ8770A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52)
)
if mibBuilder.loadTexts:
    hpSwitchJ8770A.setStatus("current")
_HpSwitchModuleJ8765A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8765A = _HpSwitchModuleJ8765A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8765A.setStatus("current")
_HpSwitchModuleJ8764A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8764A = _HpSwitchModuleJ8764A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8764A.setStatus("current")
_HpSwitchModuleJ8776A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8776A = _HpSwitchModuleJ8776A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8776A.setStatus("current")
_HpSwitchModuleJ8763A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8763A = _HpSwitchModuleJ8763A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8763A.setStatus("current")
_HpSwitchModuleJ8768A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8768A = _HpSwitchModuleJ8768A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8768A.setStatus("current")
_HpSwitchModuleJ9033A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9033A = _HpSwitchModuleJ9033A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9033A.setStatus("current")
_HpSwitchModuleJ8766A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8766A = _HpSwitchModuleJ8766A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 52, 10)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8766A.setStatus("current")
_HpSwitchJ8773A_ObjectIdentity = ObjectIdentity
hpSwitchJ8773A = _HpSwitchJ8773A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 53)
)
if mibBuilder.loadTexts:
    hpSwitchJ8773A.setStatus("current")
_HpSwitchJ8680A_ObjectIdentity = ObjectIdentity
hpSwitchJ8680A = _HpSwitchJ8680A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 54)
)
if mibBuilder.loadTexts:
    hpSwitchJ8680A.setStatus("current")
_HpSwitchJ8762A_ObjectIdentity = ObjectIdentity
hpSwitchJ8762A = _HpSwitchJ8762A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 55)
)
if mibBuilder.loadTexts:
    hpSwitchJ8762A.setStatus("current")
_HpSwitchModuleJ8762A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ8762A = _HpSwitchModuleJ8762A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 55, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ8762A.setStatus("current")
_HpSwitchJ8771A_ObjectIdentity = ObjectIdentity
hpSwitchJ8771A = _HpSwitchJ8771A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 56)
)
if mibBuilder.loadTexts:
    hpSwitchJ8771A.setStatus("current")
_HpSwitchJ8772A_ObjectIdentity = ObjectIdentity
hpSwitchJ8772A = _HpSwitchJ8772A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 57)
)
if mibBuilder.loadTexts:
    hpSwitchJ8772A.setStatus("current")
_HpSwitchJ8692A_ObjectIdentity = ObjectIdentity
hpSwitchJ8692A = _HpSwitchJ8692A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 58)
)
if mibBuilder.loadTexts:
    hpSwitchJ8692A.setStatus("current")
_HpSwitchJ8693A_ObjectIdentity = ObjectIdentity
hpSwitchJ8693A = _HpSwitchJ8693A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 59)
)
if mibBuilder.loadTexts:
    hpSwitchJ8693A.setStatus("current")
_HpSwitchJ8992A_ObjectIdentity = ObjectIdentity
hpSwitchJ8992A = _HpSwitchJ8992A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 60)
)
if mibBuilder.loadTexts:
    hpSwitchJ8992A.setStatus("current")
_HpSwitchJ9019A_ObjectIdentity = ObjectIdentity
hpSwitchJ9019A = _HpSwitchJ9019A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 61)
)
if mibBuilder.loadTexts:
    hpSwitchJ9019A.setStatus("current")
_HpSwitchModuleJ9019A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9019A = _HpSwitchModuleJ9019A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 61, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9019A.setStatus("current")
_HpSwitchJ9020A_ObjectIdentity = ObjectIdentity
hpSwitchJ9020A = _HpSwitchJ9020A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 62)
)
if mibBuilder.loadTexts:
    hpSwitchJ9020A.setStatus("current")
_HpSwitchModuleJ9020A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9020A = _HpSwitchModuleJ9020A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 62, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9020A.setStatus("current")
_HpSwitchJ9021A_ObjectIdentity = ObjectIdentity
hpSwitchJ9021A = _HpSwitchJ9021A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 63)
)
if mibBuilder.loadTexts:
    hpSwitchJ9021A.setStatus("current")
_HpSwitchModuleJ9021A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9021A = _HpSwitchModuleJ9021A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 63, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9021A.setStatus("current")
_HpSwitchJ9022A_ObjectIdentity = ObjectIdentity
hpSwitchJ9022A = _HpSwitchJ9022A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 64)
)
if mibBuilder.loadTexts:
    hpSwitchJ9022A.setStatus("current")
_HpSwitchModuleJ9022A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9022A = _HpSwitchModuleJ9022A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 64, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9022A.setStatus("current")
_HpSwitchJ9028A_ObjectIdentity = ObjectIdentity
hpSwitchJ9028A = _HpSwitchJ9028A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 65)
)
if mibBuilder.loadTexts:
    hpSwitchJ9028A.setStatus("current")
_HpSwitchJ9029A_ObjectIdentity = ObjectIdentity
hpSwitchJ9029A = _HpSwitchJ9029A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 66)
)
if mibBuilder.loadTexts:
    hpSwitchJ9029A.setStatus("current")
_HpSwitchJ9038A_ObjectIdentity = ObjectIdentity
hpSwitchJ9038A = _HpSwitchJ9038A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 67)
)
if mibBuilder.loadTexts:
    hpSwitchJ9038A.setStatus("current")
_HpSwitchJ9050A_ObjectIdentity = ObjectIdentity
hpSwitchJ9050A = _HpSwitchJ9050A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 68)
)
if mibBuilder.loadTexts:
    hpSwitchJ9050A.setStatus("current")
_HpSwitchModuleJ90xxA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ90xxA = _HpSwitchModuleJ90xxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 68, 11)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ90xxA.setStatus("current")
_HpSwitchModuleJ90yyA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ90yyA = _HpSwitchModuleJ90yyA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 68, 12)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ90yyA.setStatus("current")
_HpSwitchModuleJ90zzA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ90zzA = _HpSwitchModuleJ90zzA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 68, 13)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ90zzA.setStatus("current")
_HpSwitchJ9049A_ObjectIdentity = ObjectIdentity
hpSwitchJ9049A = _HpSwitchJ9049A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 69)
)
if mibBuilder.loadTexts:
    hpSwitchJ9049A.setStatus("current")
_HpSwitchJ9091A_ObjectIdentity = ObjectIdentity
hpSwitchJ9091A = _HpSwitchJ9091A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 72)
)
if mibBuilder.loadTexts:
    hpSwitchJ9091A.setStatus("current")
_HpManagementModuleJ9092A_ObjectIdentity = ObjectIdentity
hpManagementModuleJ9092A = _HpManagementModuleJ9092A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 72, 1)
)
if mibBuilder.loadTexts:
    hpManagementModuleJ9092A.setStatus("current")
_HpFabricModuleJ9093A_ObjectIdentity = ObjectIdentity
hpFabricModuleJ9093A = _HpFabricModuleJ9093A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 72, 2)
)
if mibBuilder.loadTexts:
    hpFabricModuleJ9093A.setStatus("current")
_HpSSMModuleJ8784A_ObjectIdentity = ObjectIdentity
hpSSMModuleJ8784A = _HpSSMModuleJ8784A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 72, 3)
)
if mibBuilder.loadTexts:
    hpSSMModuleJ8784A.setStatus("current")
_HpSwitchJ9065A_ObjectIdentity = ObjectIdentity
hpSwitchJ9065A = _HpSwitchJ9065A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 73)
)
if mibBuilder.loadTexts:
    hpSwitchJ9065A.setStatus("current")
_HpSwitchJ9079A_ObjectIdentity = ObjectIdentity
hpSwitchJ9079A = _HpSwitchJ9079A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 74)
)
if mibBuilder.loadTexts:
    hpSwitchJ9079A.setStatus("current")
_HpSwitchJ9080A_ObjectIdentity = ObjectIdentity
hpSwitchJ9080A = _HpSwitchJ9080A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 75)
)
if mibBuilder.loadTexts:
    hpSwitchJ9080A.setStatus("current")
_HpSwitchJ9085A_ObjectIdentity = ObjectIdentity
hpSwitchJ9085A = _HpSwitchJ9085A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 76)
)
if mibBuilder.loadTexts:
    hpSwitchJ9085A.setStatus("current")
_HpSwitchModuleJ9085A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9085A = _HpSwitchModuleJ9085A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 76, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9085A.setStatus("current")
_HpSwitchJ9088A_ObjectIdentity = ObjectIdentity
hpSwitchJ9088A = _HpSwitchJ9088A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 77)
)
if mibBuilder.loadTexts:
    hpSwitchJ9088A.setStatus("current")
_HpSwitchModuleJ9088A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9088A = _HpSwitchModuleJ9088A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 77, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9088A.setStatus("current")
_HpSwitchJ9087A_ObjectIdentity = ObjectIdentity
hpSwitchJ9087A = _HpSwitchJ9087A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 78)
)
if mibBuilder.loadTexts:
    hpSwitchJ9087A.setStatus("current")
_HpSwitchModuleJ9087A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9087A = _HpSwitchModuleJ9087A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 78, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9087A.setStatus("current")
_HpSwitchJ9089A_ObjectIdentity = ObjectIdentity
hpSwitchJ9089A = _HpSwitchJ9089A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 79)
)
if mibBuilder.loadTexts:
    hpSwitchJ9089A.setStatus("current")
_HpSwitchModuleJ9089A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9089A = _HpSwitchModuleJ9089A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 79, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9089A.setStatus("current")
_HpSwitchJ9086A_ObjectIdentity = ObjectIdentity
hpSwitchJ9086A = _HpSwitchJ9086A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 80)
)
if mibBuilder.loadTexts:
    hpSwitchJ9086A.setStatus("current")
_HpSwitchModuleJ9086A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9086A = _HpSwitchModuleJ9086A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 80, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9086A.setStatus("current")
_HpSwitchJ9028B_ObjectIdentity = ObjectIdentity
hpSwitchJ9028B = _HpSwitchJ9028B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 81)
)
if mibBuilder.loadTexts:
    hpSwitchJ9028B.setStatus("current")
_HpSwitchJ4900C_ObjectIdentity = ObjectIdentity
hpSwitchJ4900C = _HpSwitchJ4900C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 82)
)
if mibBuilder.loadTexts:
    hpSwitchJ4900C.setStatus("current")
_HpSwitchModuleJ4900C_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4900C = _HpSwitchModuleJ4900C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 82, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4900C.setStatus("current")
_HpSwitchJ4899C_ObjectIdentity = ObjectIdentity
hpSwitchJ4899C = _HpSwitchJ4899C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 83)
)
if mibBuilder.loadTexts:
    hpSwitchJ4899C.setStatus("current")
_HpSwitchModuleJ4899C_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ4899C = _HpSwitchModuleJ4899C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 83, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ4899C.setStatus("current")
_HpSwitchJ9146A_ObjectIdentity = ObjectIdentity
hpSwitchJ9146A = _HpSwitchJ9146A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84)
)
if mibBuilder.loadTexts:
    hpSwitchJ9146A.setStatus("current")
_HpSwitchModuleJ9146A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9146A = _HpSwitchModuleJ9146A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9146A.setStatus("current")
_HpSwitchModuleJ9149A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9149A = _HpSwitchModuleJ9149A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9149A.setStatus("current")
_HpSwitchModuleJ9008A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9008A = _HpSwitchModuleJ9008A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9008A.setStatus("current")
_HpSwitchModuleJ9165A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9165A = _HpSwitchModuleJ9165A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 84, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9165A.setStatus("current")
_HpSwitchJ9148A_ObjectIdentity = ObjectIdentity
hpSwitchJ9148A = _HpSwitchJ9148A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 85)
)
if mibBuilder.loadTexts:
    hpSwitchJ9148A.setStatus("current")
_HpSwitchModuleJ9148A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9148A = _HpSwitchModuleJ9148A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 85, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9148A.setStatus("current")
_HpSwitchJ9145A_ObjectIdentity = ObjectIdentity
hpSwitchJ9145A = _HpSwitchJ9145A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 86)
)
if mibBuilder.loadTexts:
    hpSwitchJ9145A.setStatus("current")
_HpSwitchModuleJ9145A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9145A = _HpSwitchModuleJ9145A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 86, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9145A.setStatus("current")
_HpSwitchJ9147A_ObjectIdentity = ObjectIdentity
hpSwitchJ9147A = _HpSwitchJ9147A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 87)
)
if mibBuilder.loadTexts:
    hpSwitchJ9147A.setStatus("current")
_HpSwitchModuleJ9147A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9147A = _HpSwitchModuleJ9147A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 87, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9147A.setStatus("current")
_HpSwitchJ9279A_ObjectIdentity = ObjectIdentity
hpSwitchJ9279A = _HpSwitchJ9279A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 88)
)
if mibBuilder.loadTexts:
    hpSwitchJ9279A.setStatus("current")
_HpSwitchModuleJ9279A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9279A = _HpSwitchModuleJ9279A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 88, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9279A.setStatus("current")
_HpSwitchJ9280A_ObjectIdentity = ObjectIdentity
hpSwitchJ9280A = _HpSwitchJ9280A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 89)
)
if mibBuilder.loadTexts:
    hpSwitchJ9280A.setStatus("current")
_HpSwitchModuleJ9280A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9280A = _HpSwitchModuleJ9280A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 89, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9280A.setStatus("current")
_HpSwitchJ9019B_ObjectIdentity = ObjectIdentity
hpSwitchJ9019B = _HpSwitchJ9019B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 90)
)
if mibBuilder.loadTexts:
    hpSwitchJ9019B.setStatus("current")
_HpSwitchJ9137A_ObjectIdentity = ObjectIdentity
hpSwitchJ9137A = _HpSwitchJ9137A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 94)
)
if mibBuilder.loadTexts:
    hpSwitchJ9137A.setStatus("current")
_HpSwitchModuleJ9137A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9137A = _HpSwitchModuleJ9137A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 94, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9137A.setStatus("current")
_HpSwitchJ9138A_ObjectIdentity = ObjectIdentity
hpSwitchJ9138A = _HpSwitchJ9138A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 95)
)
if mibBuilder.loadTexts:
    hpSwitchJ9138A.setStatus("current")
_HpSwitchModuleJ9138A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9138A = _HpSwitchModuleJ9138A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 95, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9138A.setStatus("current")
_HpSwitchJ9298A_ObjectIdentity = ObjectIdentity
hpSwitchJ9298A = _HpSwitchJ9298A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 96)
)
if mibBuilder.loadTexts:
    hpSwitchJ9298A.setStatus("current")
_HpSwitchModuleJ9298A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9298A = _HpSwitchModuleJ9298A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 96, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9298A.setStatus("current")
_HpSwitchJ9299A_ObjectIdentity = ObjectIdentity
hpSwitchJ9299A = _HpSwitchJ9299A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 97)
)
if mibBuilder.loadTexts:
    hpSwitchJ9299A.setStatus("current")
_HpSwitchModuleJ9299A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9299A = _HpSwitchModuleJ9299A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 97, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9299A.setStatus("current")
_HpSwitchJ9265A_ObjectIdentity = ObjectIdentity
hpSwitchJ9265A = _HpSwitchJ9265A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98)
)
if mibBuilder.loadTexts:
    hpSwitchJ9265A.setStatus("current")
_HpSwitchModuleJ92yyA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92yyA = _HpSwitchModuleJ92yyA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92yyA.setStatus("current")
_HpSwitchModuleJ92xxA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92xxA = _HpSwitchModuleJ92xxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92xxA.setStatus("current")
_HpSwitchModuleJ92wwA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92wwA = _HpSwitchModuleJ92wwA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92wwA.setStatus("current")
_HpSwitchModuleJ92vvA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92vvA = _HpSwitchModuleJ92vvA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92vvA.setStatus("current")
_HpSwitchModuleJ92uuA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92uuA = _HpSwitchModuleJ92uuA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92uuA.setStatus("current")
_HpSwitchModuleJ92ttA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ92ttA = _HpSwitchModuleJ92ttA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 98, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ92ttA.setStatus("current")
_HpEtherSwitchPortType_ObjectIdentity = ObjectIdentity
hpEtherSwitchPortType = _HpEtherSwitchPortType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 99)
)
_HpEtherSwitchPort10T_ObjectIdentity = ObjectIdentity
hpEtherSwitchPort10T = _HpEtherSwitchPort10T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 99, 1)
)
_HpEtherSwitchPort100T_ObjectIdentity = ObjectIdentity
hpEtherSwitchPort100T = _HpEtherSwitchPort100T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 99, 2)
)
_HpEtherSwitchPort100VG_ObjectIdentity = ObjectIdentity
hpEtherSwitchPort100VG = _HpEtherSwitchPort100VG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 99, 3)
)
_HpEtherSwitchPort100F_ObjectIdentity = ObjectIdentity
hpEtherSwitchPort100F = _HpEtherSwitchPort100F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 99, 4)
)
_HpSwitchJ9263A_ObjectIdentity = ObjectIdentity
hpSwitchJ9263A = _HpSwitchJ9263A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 100)
)
if mibBuilder.loadTexts:
    hpSwitchJ9263A.setStatus("current")
_HpSwitchJ9264A_ObjectIdentity = ObjectIdentity
hpSwitchJ9264A = _HpSwitchJ9264A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 101)
)
if mibBuilder.loadTexts:
    hpSwitchJ9264A.setStatus("current")
_HpSwitchJ9445A_ObjectIdentity = ObjectIdentity
hpSwitchJ9445A = _HpSwitchJ9445A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 102)
)
if mibBuilder.loadTexts:
    hpSwitchJ9445A.setStatus("current")
_HpSwitchJ9449A_ObjectIdentity = ObjectIdentity
hpSwitchJ9449A = _HpSwitchJ9449A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 103)
)
if mibBuilder.loadTexts:
    hpSwitchJ9449A.setStatus("current")
_HpSwitchJ9450A_ObjectIdentity = ObjectIdentity
hpSwitchJ9450A = _HpSwitchJ9450A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 104)
)
if mibBuilder.loadTexts:
    hpSwitchJ9450A.setStatus("current")
_HpSwitchJ9452A_ObjectIdentity = ObjectIdentity
hpSwitchJ9452A = _HpSwitchJ9452A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 105)
)
if mibBuilder.loadTexts:
    hpSwitchJ9452A.setStatus("current")
_HpSwitchJ9451A_ObjectIdentity = ObjectIdentity
hpSwitchJ9451A = _HpSwitchJ9451A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 106)
)
if mibBuilder.loadTexts:
    hpSwitchJ9451A.setStatus("current")
_HpSwitch516733_B21_ObjectIdentity = ObjectIdentity
hpSwitch516733_B21 = _HpSwitch516733_B21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 107)
)
if mibBuilder.loadTexts:
    hpSwitch516733_B21.setStatus("current")
_HpSwitch498358_B21_ObjectIdentity = ObjectIdentity
hpSwitch498358_B21 = _HpSwitch498358_B21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 108)
)
if mibBuilder.loadTexts:
    hpSwitch498358_B21.setStatus("current")
_HpSwitchJ9471A_ObjectIdentity = ObjectIdentity
hpSwitchJ9471A = _HpSwitchJ9471A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 109)
)
if mibBuilder.loadTexts:
    hpSwitchJ9471A.setStatus("current")
_HpSwitchJ9473A_ObjectIdentity = ObjectIdentity
hpSwitchJ9473A = _HpSwitchJ9473A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 110)
)
if mibBuilder.loadTexts:
    hpSwitchJ9473A.setStatus("current")
_HpSwitchModuleJ94yxA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ94yxA = _HpSwitchModuleJ94yxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 110, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ94yxA.setStatus("current")
_HpSwitchModuleJ94yyA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ94yyA = _HpSwitchModuleJ94yyA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 110, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ94yyA.setStatus("current")
_HpSwitchJ9470A_ObjectIdentity = ObjectIdentity
hpSwitchJ9470A = _HpSwitchJ9470A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 111)
)
if mibBuilder.loadTexts:
    hpSwitchJ9470A.setStatus("current")
_HpSwitchJ9472A_ObjectIdentity = ObjectIdentity
hpSwitchJ9472A = _HpSwitchJ9472A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 112)
)
if mibBuilder.loadTexts:
    hpSwitchJ9472A.setStatus("current")
_HpSwitchModuleJ94xxA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ94xxA = _HpSwitchModuleJ94xxA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 112, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ94xxA.setStatus("current")
_HpSwitchModuleJ94xyA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ94xyA = _HpSwitchModuleJ94xyA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 112, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ94xyA.setStatus("current")
_HpSwitchJ9477A_ObjectIdentity = ObjectIdentity
hpSwitchJ9477A = _HpSwitchJ9477A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 113)
)
if mibBuilder.loadTexts:
    hpSwitchJ9477A.setStatus("current")
_HpSwitchJ9310A_ObjectIdentity = ObjectIdentity
hpSwitchJ9310A = _HpSwitchJ9310A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 114)
)
if mibBuilder.loadTexts:
    hpSwitchJ9310A.setStatus("current")
_HpSwitchJ9311A_ObjectIdentity = ObjectIdentity
hpSwitchJ9311A = _HpSwitchJ9311A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 115)
)
if mibBuilder.loadTexts:
    hpSwitchJ9311A.setStatus("current")
_HpSwitchModuleJ93aaA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ93aaA = _HpSwitchModuleJ93aaA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 115, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ93aaA.setStatus("current")
_HpSwitchModuleJ93bbA_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ93bbA = _HpSwitchModuleJ93bbA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 115, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ93bbA.setStatus("current")
_HpSwitchJ9565A_ObjectIdentity = ObjectIdentity
hpSwitchJ9565A = _HpSwitchJ9565A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 117)
)
if mibBuilder.loadTexts:
    hpSwitchJ9565A.setStatus("current")
_HpSwitchModuleJ9565A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9565A = _HpSwitchModuleJ9565A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 117, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9565A.setStatus("current")
_HpSwitchJ9562A_ObjectIdentity = ObjectIdentity
hpSwitchJ9562A = _HpSwitchJ9562A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 118)
)
if mibBuilder.loadTexts:
    hpSwitchJ9562A.setStatus("current")
_HpSwitchModuleJ9562A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9562A = _HpSwitchModuleJ9562A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 118, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9562A.setStatus("current")
_HpSwitchJ9573_ObjectIdentity = ObjectIdentity
hpSwitchJ9573 = _HpSwitchJ9573_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 119)
)
if mibBuilder.loadTexts:
    hpSwitchJ9573.setStatus("current")
_HpSwitchModuleJ9573_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9573 = _HpSwitchModuleJ9573_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 119, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9573.setStatus("current")
_HpSwitchJ9574_ObjectIdentity = ObjectIdentity
hpSwitchJ9574 = _HpSwitchJ9574_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 120)
)
if mibBuilder.loadTexts:
    hpSwitchJ9574.setStatus("current")
_HpSwitchModuleJ9574x_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9574x = _HpSwitchModuleJ9574x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 120, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9574x.setStatus("current")
_HpSwitchModuleJ9574y_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9574y = _HpSwitchModuleJ9574y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 120, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9574y.setStatus("current")
_HpSwitchJ9575_ObjectIdentity = ObjectIdentity
hpSwitchJ9575 = _HpSwitchJ9575_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 121)
)
if mibBuilder.loadTexts:
    hpSwitchJ9575.setStatus("current")
_HpSwitchModuleJ9575_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9575 = _HpSwitchModuleJ9575_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 121, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9575.setStatus("current")
_HpSwitchJ9576_ObjectIdentity = ObjectIdentity
hpSwitchJ9576 = _HpSwitchJ9576_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 122)
)
if mibBuilder.loadTexts:
    hpSwitchJ9576.setStatus("current")
_HpSwitchModuleJ9576x_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9576x = _HpSwitchModuleJ9576x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 122, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9576x.setStatus("current")
_HpSwitchModuleJ9576y_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9576y = _HpSwitchModuleJ9576y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 122, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9576y.setStatus("current")
_HpSwitchJ9584_ObjectIdentity = ObjectIdentity
hpSwitchJ9584 = _HpSwitchJ9584_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 123)
)
if mibBuilder.loadTexts:
    hpSwitchJ9584.setStatus("current")
_HpSwitchModuleJ9584_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9584 = _HpSwitchModuleJ9584_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 123, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9584.setStatus("current")
_HpSwitchJ9585_ObjectIdentity = ObjectIdentity
hpSwitchJ9585 = _HpSwitchJ9585_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 124)
)
if mibBuilder.loadTexts:
    hpSwitchJ9585.setStatus("current")
_HpSwitchModuleJ9585_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9585 = _HpSwitchModuleJ9585_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 124, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9585.setStatus("current")
_HpSwitchJ9586_ObjectIdentity = ObjectIdentity
hpSwitchJ9586 = _HpSwitchJ9586_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 125)
)
if mibBuilder.loadTexts:
    hpSwitchJ9586.setStatus("current")
_HpSwitchModuleJ9586x_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9586x = _HpSwitchModuleJ9586x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 125, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9586x.setStatus("current")
_HpSwitchModuleJ9586y_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9586y = _HpSwitchModuleJ9586y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 125, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9586y.setStatus("current")
_HpSwitchJ9587_ObjectIdentity = ObjectIdentity
hpSwitchJ9587 = _HpSwitchJ9587_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 126)
)
if mibBuilder.loadTexts:
    hpSwitchJ9587.setStatus("current")
_HpSwitchModuleJ9587_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9587 = _HpSwitchModuleJ9587_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 126, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9587.setStatus("current")
_HpSwitchJ9588_ObjectIdentity = ObjectIdentity
hpSwitchJ9588 = _HpSwitchJ9588_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 127)
)
if mibBuilder.loadTexts:
    hpSwitchJ9588.setStatus("current")
_HpSwitchModuleJ9588x_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9588x = _HpSwitchModuleJ9588x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 127, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9588x.setStatus("current")
_HpSwitchModuleJ9588y_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9588y = _HpSwitchModuleJ9588y_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 127, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9588y.setStatus("current")
_HpSwitchJ9577_ObjectIdentity = ObjectIdentity
hpSwitchJ9577 = _HpSwitchJ9577_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 128)
)
if mibBuilder.loadTexts:
    hpSwitchJ9577.setStatus("current")
_HpSwitchModuleJ9577A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9577A = _HpSwitchModuleJ9577A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 128, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9577A.setStatus("current")
_HpSwitchJ9623A_ObjectIdentity = ObjectIdentity
hpSwitchJ9623A = _HpSwitchJ9623A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 129)
)
if mibBuilder.loadTexts:
    hpSwitchJ9623A.setStatus("current")
_HpSwitchModuleJ9623A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9623A = _HpSwitchModuleJ9623A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 129, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9623A.setStatus("current")
_HpSwitchJ9624A_ObjectIdentity = ObjectIdentity
hpSwitchJ9624A = _HpSwitchJ9624A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 130)
)
if mibBuilder.loadTexts:
    hpSwitchJ9624A.setStatus("current")
_HpSwitchModuleJ9624A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9624A = _HpSwitchModuleJ9624A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 130, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9624A.setStatus("current")
_HpSwitchJ9625A_ObjectIdentity = ObjectIdentity
hpSwitchJ9625A = _HpSwitchJ9625A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 131)
)
if mibBuilder.loadTexts:
    hpSwitchJ9625A.setStatus("current")
_HpSwitchModuleJ9625A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9625A = _HpSwitchModuleJ9625A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 131, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9625A.setStatus("current")
_HpSwitchJ9626A_ObjectIdentity = ObjectIdentity
hpSwitchJ9626A = _HpSwitchJ9626A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 132)
)
if mibBuilder.loadTexts:
    hpSwitchJ9626A.setStatus("current")
_HpSwitchModuleJ9626A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9626A = _HpSwitchModuleJ9626A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 132, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9626A.setStatus("current")
_HpSwitchJ9627A_ObjectIdentity = ObjectIdentity
hpSwitchJ9627A = _HpSwitchJ9627A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 133)
)
if mibBuilder.loadTexts:
    hpSwitchJ9627A.setStatus("current")
_HpSwitchModuleJ9627A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9627A = _HpSwitchModuleJ9627A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 133, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9627A.setStatus("current")
_HpSwitchJ9660A_ObjectIdentity = ObjectIdentity
hpSwitchJ9660A = _HpSwitchJ9660A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 134)
)
if mibBuilder.loadTexts:
    hpSwitchJ9660A.setStatus("current")
_HpSwitchJ9772A_ObjectIdentity = ObjectIdentity
hpSwitchJ9772A = _HpSwitchJ9772A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 136)
)
if mibBuilder.loadTexts:
    hpSwitchJ9772A.setStatus("current")
_HpSwitchModuleJ9772A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9772A = _HpSwitchModuleJ9772A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 136, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9772A.setStatus("current")
_HpSwitchJ9773A_ObjectIdentity = ObjectIdentity
hpSwitchJ9773A = _HpSwitchJ9773A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 137)
)
if mibBuilder.loadTexts:
    hpSwitchJ9773A.setStatus("current")
_HpSwitchModuleJ9773A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9773A = _HpSwitchModuleJ9773A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 137, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9773A.setStatus("current")
_HpSwitchJ9774A_ObjectIdentity = ObjectIdentity
hpSwitchJ9774A = _HpSwitchJ9774A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 138)
)
if mibBuilder.loadTexts:
    hpSwitchJ9774A.setStatus("current")
_HpSwitchModuleJ9774A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9774A = _HpSwitchModuleJ9774A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 138, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9774A.setStatus("current")
_HpSwitchJ9775A_ObjectIdentity = ObjectIdentity
hpSwitchJ9775A = _HpSwitchJ9775A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 139)
)
if mibBuilder.loadTexts:
    hpSwitchJ9775A.setStatus("current")
_HpSwitchModuleJ9775A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9775A = _HpSwitchModuleJ9775A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 139, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9775A.setStatus("current")
_HpSwitchJ9776A_ObjectIdentity = ObjectIdentity
hpSwitchJ9776A = _HpSwitchJ9776A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 140)
)
if mibBuilder.loadTexts:
    hpSwitchJ9776A.setStatus("current")
_HpSwitchModuleJ9776A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9776A = _HpSwitchModuleJ9776A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 140, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9776A.setStatus("current")
_HpSwitchJ9777A_ObjectIdentity = ObjectIdentity
hpSwitchJ9777A = _HpSwitchJ9777A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 141)
)
if mibBuilder.loadTexts:
    hpSwitchJ9777A.setStatus("current")
_HpSwitchModuleJ9777A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9777A = _HpSwitchModuleJ9777A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 141, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9777A.setStatus("current")
_HpSwitchJ9778A_ObjectIdentity = ObjectIdentity
hpSwitchJ9778A = _HpSwitchJ9778A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 142)
)
if mibBuilder.loadTexts:
    hpSwitchJ9778A.setStatus("current")
_HpSwitchModuleJ9778A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9778A = _HpSwitchModuleJ9778A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 142, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9778A.setStatus("current")
_HpSwitchJ9779A_ObjectIdentity = ObjectIdentity
hpSwitchJ9779A = _HpSwitchJ9779A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 143)
)
if mibBuilder.loadTexts:
    hpSwitchJ9779A.setStatus("current")
_HpSwitchModuleJ9779A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9779A = _HpSwitchModuleJ9779A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 143, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9779A.setStatus("current")
_HpSwitchJ9780A_ObjectIdentity = ObjectIdentity
hpSwitchJ9780A = _HpSwitchJ9780A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 144)
)
if mibBuilder.loadTexts:
    hpSwitchJ9780A.setStatus("current")
_HpSwitchModuleJ9780A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9780A = _HpSwitchModuleJ9780A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 144, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9780A.setStatus("current")
_HpSwitchJ9781A_ObjectIdentity = ObjectIdentity
hpSwitchJ9781A = _HpSwitchJ9781A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 145)
)
if mibBuilder.loadTexts:
    hpSwitchJ9781A.setStatus("current")
_HpSwitchModuleJ9781A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9781A = _HpSwitchModuleJ9781A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 145, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9781A.setStatus("current")
_HpSwitchJ9782A_ObjectIdentity = ObjectIdentity
hpSwitchJ9782A = _HpSwitchJ9782A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 146)
)
if mibBuilder.loadTexts:
    hpSwitchJ9782A.setStatus("current")
_HpSwitchModuleJ9782A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9782A = _HpSwitchModuleJ9782A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 146, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9782A.setStatus("current")
_HpSwitchJ9783A_ObjectIdentity = ObjectIdentity
hpSwitchJ9783A = _HpSwitchJ9783A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 147)
)
if mibBuilder.loadTexts:
    hpSwitchJ9783A.setStatus("current")
_HpSwitchModuleJ9783A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9783A = _HpSwitchModuleJ9783A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 147, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9783A.setStatus("current")
_HpSwitchJ9800A_ObjectIdentity = ObjectIdentity
hpSwitchJ9800A = _HpSwitchJ9800A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 148)
)
if mibBuilder.loadTexts:
    hpSwitchJ9800A.setStatus("current")
_HpSwitchJ9801A_ObjectIdentity = ObjectIdentity
hpSwitchJ9801A = _HpSwitchJ9801A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 149)
)
if mibBuilder.loadTexts:
    hpSwitchJ9801A.setStatus("current")
_HpSwitchJ9802A_ObjectIdentity = ObjectIdentity
hpSwitchJ9802A = _HpSwitchJ9802A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 150)
)
if mibBuilder.loadTexts:
    hpSwitchJ9802A.setStatus("current")
_HpSwitchJ9803A_ObjectIdentity = ObjectIdentity
hpSwitchJ9803A = _HpSwitchJ9803A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 151)
)
if mibBuilder.loadTexts:
    hpSwitchJ9803A.setStatus("current")
_HpSwitchJ9726A_ObjectIdentity = ObjectIdentity
hpSwitchJ9726A = _HpSwitchJ9726A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 152)
)
if mibBuilder.loadTexts:
    hpSwitchJ9726A.setStatus("current")
_HpSwitchModuleJ9726A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9726A = _HpSwitchModuleJ9726A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 152, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9726A.setStatus("current")
_HpSwitchJ9727A_ObjectIdentity = ObjectIdentity
hpSwitchJ9727A = _HpSwitchJ9727A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 153)
)
if mibBuilder.loadTexts:
    hpSwitchJ9727A.setStatus("current")
_HpSwitchModuleJ9727A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9727A = _HpSwitchModuleJ9727A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 153, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9727A.setStatus("current")
_HpSwitchJ9728A_ObjectIdentity = ObjectIdentity
hpSwitchJ9728A = _HpSwitchJ9728A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 154)
)
if mibBuilder.loadTexts:
    hpSwitchJ9728A.setStatus("current")
_HpSwitchModuleJ9728A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9728A = _HpSwitchModuleJ9728A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 154, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9728A.setStatus("current")
_HpSwitchJ9729A_ObjectIdentity = ObjectIdentity
hpSwitchJ9729A = _HpSwitchJ9729A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155)
)
if mibBuilder.loadTexts:
    hpSwitchJ9729A.setStatus("current")
_HpSwitchModuleJ9729A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9729A = _HpSwitchModuleJ9729A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9729A.setStatus("current")
_HpSwitchModuleJ9730A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9730A = _HpSwitchModuleJ9730A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9730A.setStatus("current")
_HpSwitchModuleJ9731A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9731A = _HpSwitchModuleJ9731A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9731A.setStatus("current")
_HpSwitchModuleJ9732A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9732A = _HpSwitchModuleJ9732A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9732A.setStatus("current")
_HpSwitchModuleJ9733A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9733A = _HpSwitchModuleJ9733A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 155, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9733A.setStatus("current")
_HpSwitchJ9833A_ObjectIdentity = ObjectIdentity
hpSwitchJ9833A = _HpSwitchJ9833A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 158)
)
if mibBuilder.loadTexts:
    hpSwitchJ9833A.setStatus("current")
_HpSwitchJ9834A_ObjectIdentity = ObjectIdentity
hpSwitchJ9834A = _HpSwitchJ9834A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 159)
)
if mibBuilder.loadTexts:
    hpSwitchJ9834A.setStatus("current")
_HpSwitchJ9850A_ObjectIdentity = ObjectIdentity
hpSwitchJ9850A = _HpSwitchJ9850A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160)
)
if mibBuilder.loadTexts:
    hpSwitchJ9850A.setStatus("current")
_HpSwitchModuleJ9827A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9827A = _HpSwitchModuleJ9827A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9827A.setStatus("current")
_HpSwitchModuleJ9986A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9986A = _HpSwitchModuleJ9986A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9986A.setStatus("current")
_HpSwitchModuleJ9987A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9987A = _HpSwitchModuleJ9987A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 3)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9987A.setStatus("current")
_HpSwitchModuleJ9988A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9988A = _HpSwitchModuleJ9988A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 4)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9988A.setStatus("current")
_HpSwitchModuleJ9989A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9989A = _HpSwitchModuleJ9989A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 5)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9989A.setStatus("current")
_HpSwitchModuleJ9990A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9990A = _HpSwitchModuleJ9990A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 6)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9990A.setStatus("current")
_HpSwitchModuleJ9991A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9991A = _HpSwitchModuleJ9991A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 7)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9991A.setStatus("current")
_HpSwitchModuleJ9992A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9992A = _HpSwitchModuleJ9992A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 8)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9992A.setStatus("current")
_HpSwitchModuleJ9993A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9993A = _HpSwitchModuleJ9993A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 9)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9993A.setStatus("current")
_HpSwitchModuleJ9995A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9995A = _HpSwitchModuleJ9995A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 10)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9995A.setStatus("current")
_HpSwitchModuleJ9996A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9996A = _HpSwitchModuleJ9996A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 160, 11)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9996A.setStatus("current")
_HpSwitchJ9851A_ObjectIdentity = ObjectIdentity
hpSwitchJ9851A = _HpSwitchJ9851A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 161)
)
if mibBuilder.loadTexts:
    hpSwitchJ9851A.setStatus("current")
_HpSwitchJ9853A_ObjectIdentity = ObjectIdentity
hpSwitchJ9853A = _HpSwitchJ9853A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 163)
)
if mibBuilder.loadTexts:
    hpSwitchJ9853A.setStatus("current")
_HpSwitchModuleJ9853A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9853A = _HpSwitchModuleJ9853A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 163, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9853A.setStatus("current")
_HpSwitchJ9854A_ObjectIdentity = ObjectIdentity
hpSwitchJ9854A = _HpSwitchJ9854A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 164)
)
if mibBuilder.loadTexts:
    hpSwitchJ9854A.setStatus("current")
_HpSwitchModuleJ9854A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9854A = _HpSwitchModuleJ9854A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 164, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9854A.setStatus("current")
_HpSwitchJ9855A_ObjectIdentity = ObjectIdentity
hpSwitchJ9855A = _HpSwitchJ9855A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 165)
)
if mibBuilder.loadTexts:
    hpSwitchJ9855A.setStatus("current")
_HpSwitchModuleJ9855A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9855A = _HpSwitchModuleJ9855A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 165, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9855A.setStatus("current")
_HpSwitchJ9856A_ObjectIdentity = ObjectIdentity
hpSwitchJ9856A = _HpSwitchJ9856A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 166)
)
if mibBuilder.loadTexts:
    hpSwitchJ9856A.setStatus("current")
_HpSwitchModuleJ9856A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJ9856A = _HpSwitchModuleJ9856A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 166, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJ9856A.setStatus("current")
_HpSwitchJ9979A_ObjectIdentity = ObjectIdentity
hpSwitchJ9979A = _HpSwitchJ9979A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 167)
)
if mibBuilder.loadTexts:
    hpSwitchJ9979A.setStatus("current")
_HpSwitchJ9980A_ObjectIdentity = ObjectIdentity
hpSwitchJ9980A = _HpSwitchJ9980A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 168)
)
if mibBuilder.loadTexts:
    hpSwitchJ9980A.setStatus("current")
_HpSwitchJ9981A_ObjectIdentity = ObjectIdentity
hpSwitchJ9981A = _HpSwitchJ9981A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 169)
)
if mibBuilder.loadTexts:
    hpSwitchJ9981A.setStatus("current")
_HpSwitchJ9982A_ObjectIdentity = ObjectIdentity
hpSwitchJ9982A = _HpSwitchJ9982A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 170)
)
if mibBuilder.loadTexts:
    hpSwitchJ9982A.setStatus("current")
_HpSwitchJ9983A_ObjectIdentity = ObjectIdentity
hpSwitchJ9983A = _HpSwitchJ9983A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 171)
)
if mibBuilder.loadTexts:
    hpSwitchJ9983A.setStatus("current")
_HpSwitchJ9984A_ObjectIdentity = ObjectIdentity
hpSwitchJ9984A = _HpSwitchJ9984A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 172)
)
if mibBuilder.loadTexts:
    hpSwitchJ9984A.setStatus("current")
_HpSwitchJL070A_ObjectIdentity = ObjectIdentity
hpSwitchJL070A = _HpSwitchJL070A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 173)
)
if mibBuilder.loadTexts:
    hpSwitchJL070A.setStatus("current")
_HpSwitchModuleJL070A_ObjectIdentity = ObjectIdentity
hpSwitchModuleJL070A = _HpSwitchModuleJL070A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 173, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleJL070A.setStatus("current")
_Aruba3810_ObjectIdentity = ObjectIdentity
aruba3810 = _Aruba3810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174)
)
if mibBuilder.loadTexts:
    aruba3810.setStatus("current")
_ArubaJL071A_ObjectIdentity = ObjectIdentity
arubaJL071A = _ArubaJL071A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 1)
)
if mibBuilder.loadTexts:
    arubaJL071A.setStatus("current")
_ArubaJL071AModule_ObjectIdentity = ObjectIdentity
arubaJL071AModule = _ArubaJL071AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 1, 1)
)
if mibBuilder.loadTexts:
    arubaJL071AModule.setStatus("current")
_ArubaJL072A_ObjectIdentity = ObjectIdentity
arubaJL072A = _ArubaJL072A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 2)
)
if mibBuilder.loadTexts:
    arubaJL072A.setStatus("current")
_ArubaJL072AModule_ObjectIdentity = ObjectIdentity
arubaJL072AModule = _ArubaJL072AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 2, 1)
)
if mibBuilder.loadTexts:
    arubaJL072AModule.setStatus("current")
_ArubaJL073A_ObjectIdentity = ObjectIdentity
arubaJL073A = _ArubaJL073A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 3)
)
if mibBuilder.loadTexts:
    arubaJL073A.setStatus("current")
_ArubaJL073AModule_ObjectIdentity = ObjectIdentity
arubaJL073AModule = _ArubaJL073AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 3, 1)
)
if mibBuilder.loadTexts:
    arubaJL073AModule.setStatus("current")
_ArubaJL074A_ObjectIdentity = ObjectIdentity
arubaJL074A = _ArubaJL074A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 4)
)
if mibBuilder.loadTexts:
    arubaJL074A.setStatus("current")
_ArubaJL074AModule_ObjectIdentity = ObjectIdentity
arubaJL074AModule = _ArubaJL074AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 4, 1)
)
if mibBuilder.loadTexts:
    arubaJL074AModule.setStatus("current")
_ArubaJL075A_ObjectIdentity = ObjectIdentity
arubaJL075A = _ArubaJL075A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 5)
)
if mibBuilder.loadTexts:
    arubaJL075A.setStatus("current")
_ArubaJL075AModule_ObjectIdentity = ObjectIdentity
arubaJL075AModule = _ArubaJL075AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 5, 1)
)
if mibBuilder.loadTexts:
    arubaJL075AModule.setStatus("current")
_ArubaJL076A_ObjectIdentity = ObjectIdentity
arubaJL076A = _ArubaJL076A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 6)
)
if mibBuilder.loadTexts:
    arubaJL076A.setStatus("current")
_ArubaJL076AModule_ObjectIdentity = ObjectIdentity
arubaJL076AModule = _ArubaJL076AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 6, 1)
)
if mibBuilder.loadTexts:
    arubaJL076AModule.setStatus("current")
_ArubaJL077A_ObjectIdentity = ObjectIdentity
arubaJL077A = _ArubaJL077A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 7)
)
if mibBuilder.loadTexts:
    arubaJL077A.setStatus("current")
_ArubaJL077AModule_ObjectIdentity = ObjectIdentity
arubaJL077AModule = _ArubaJL077AModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 7, 1)
)
if mibBuilder.loadTexts:
    arubaJL077AModule.setStatus("current")
_ArubaJL084AStackingModule_ObjectIdentity = ObjectIdentity
arubaJL084AStackingModule = _ArubaJL084AStackingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 8)
)
if mibBuilder.loadTexts:
    arubaJL084AStackingModule.setStatus("current")
_ArubaJL088AFanTray_ObjectIdentity = ObjectIdentity
arubaJL088AFanTray = _ArubaJL088AFanTray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 174, 9)
)
if mibBuilder.loadTexts:
    arubaJL088AFanTray.setStatus("current")
_ArubaFPModule_ObjectIdentity = ObjectIdentity
arubaFPModule = _ArubaFPModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180)
)
if mibBuilder.loadTexts:
    arubaFPModule.setStatus("current")
_ArubaFPModuleJL078A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL078A = _ArubaFPModuleJL078A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 1)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL078A.setStatus("current")
_ArubaFPModuleJL079A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL079A = _ArubaFPModuleJL079A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 2)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL079A.setStatus("current")
_ArubaFPModuleJL080A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL080A = _ArubaFPModuleJL080A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 3)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL080A.setStatus("current")
_ArubaFPModuleJL081A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL081A = _ArubaFPModuleJL081A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 4)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL081A.setStatus("current")
_ArubaFPModuleJL082A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL082A = _ArubaFPModuleJL082A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 5)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL082A.setStatus("current")
_ArubaFPModuleJL083A_ObjectIdentity = ObjectIdentity
arubaFPModuleJL083A = _ArubaFPModuleJL083A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 180, 6)
)
if mibBuilder.loadTexts:
    arubaFPModuleJL083A.setStatus("current")
_ArubaSwitch2930_ObjectIdentity = ObjectIdentity
arubaSwitch2930 = _ArubaSwitch2930_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181)
)
if mibBuilder.loadTexts:
    arubaSwitch2930.setStatus("current")
_ArubaStackingModuleJL325A_ObjectIdentity = ObjectIdentity
arubaStackingModuleJL325A = _ArubaStackingModuleJL325A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 1)
)
if mibBuilder.loadTexts:
    arubaStackingModuleJL325A.setStatus("current")
_ArubaSwitchJL319A_ObjectIdentity = ObjectIdentity
arubaSwitchJL319A = _ArubaSwitchJL319A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 2)
)
if mibBuilder.loadTexts:
    arubaSwitchJL319A.setStatus("current")
_ArubaModuleJL319A_ObjectIdentity = ObjectIdentity
arubaModuleJL319A = _ArubaModuleJL319A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 2, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL319A.setStatus("current")
_ArubaSwitchJL321A_ObjectIdentity = ObjectIdentity
arubaSwitchJL321A = _ArubaSwitchJL321A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 3)
)
if mibBuilder.loadTexts:
    arubaSwitchJL321A.setStatus("current")
_ArubaModuleJL321A_ObjectIdentity = ObjectIdentity
arubaModuleJL321A = _ArubaModuleJL321A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 3, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL321A.setStatus("current")
_ArubaSwitchJL320A_ObjectIdentity = ObjectIdentity
arubaSwitchJL320A = _ArubaSwitchJL320A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 4)
)
if mibBuilder.loadTexts:
    arubaSwitchJL320A.setStatus("current")
_ArubaModuleJL320A_ObjectIdentity = ObjectIdentity
arubaModuleJL320A = _ArubaModuleJL320A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 4, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL320A.setStatus("current")
_ArubaSwitchJL322A_ObjectIdentity = ObjectIdentity
arubaSwitchJL322A = _ArubaSwitchJL322A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 5)
)
if mibBuilder.loadTexts:
    arubaSwitchJL322A.setStatus("current")
_ArubaModuleJL322A_ObjectIdentity = ObjectIdentity
arubaModuleJL322A = _ArubaModuleJL322A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 5, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL322A.setStatus("current")
_ArubaSwitchJL324A_ObjectIdentity = ObjectIdentity
arubaSwitchJL324A = _ArubaSwitchJL324A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 6)
)
if mibBuilder.loadTexts:
    arubaSwitchJL324A.setStatus("current")
_ArubaModuleJL324A_ObjectIdentity = ObjectIdentity
arubaModuleJL324A = _ArubaModuleJL324A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 6, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL324A.setStatus("current")
_ArubaSwitchJL323A_ObjectIdentity = ObjectIdentity
arubaSwitchJL323A = _ArubaSwitchJL323A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 9)
)
if mibBuilder.loadTexts:
    arubaSwitchJL323A.setStatus("current")
_ArubaModuleJL323A_ObjectIdentity = ObjectIdentity
arubaModuleJL323A = _ArubaModuleJL323A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 9, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL323A.setStatus("current")
_ArubaSwitchJL258A_ObjectIdentity = ObjectIdentity
arubaSwitchJL258A = _ArubaSwitchJL258A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 16)
)
if mibBuilder.loadTexts:
    arubaSwitchJL258A.setStatus("current")
_ArubaModuleJL258A_ObjectIdentity = ObjectIdentity
arubaModuleJL258A = _ArubaModuleJL258A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 16, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL258A.setStatus("current")
_ArubaSwitchJL253A_ObjectIdentity = ObjectIdentity
arubaSwitchJL253A = _ArubaSwitchJL253A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 18)
)
if mibBuilder.loadTexts:
    arubaSwitchJL253A.setStatus("current")
_ArubaModuleJL253A_ObjectIdentity = ObjectIdentity
arubaModuleJL253A = _ArubaModuleJL253A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 18, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL253A.setStatus("current")
_ArubaSwitchJL254A_ObjectIdentity = ObjectIdentity
arubaSwitchJL254A = _ArubaSwitchJL254A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 19)
)
if mibBuilder.loadTexts:
    arubaSwitchJL254A.setStatus("current")
_ArubaModuleJL254A_ObjectIdentity = ObjectIdentity
arubaModuleJL254A = _ArubaModuleJL254A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 19, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL254A.setStatus("current")
_ArubaSwitchJL255A_ObjectIdentity = ObjectIdentity
arubaSwitchJL255A = _ArubaSwitchJL255A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 20)
)
if mibBuilder.loadTexts:
    arubaSwitchJL255A.setStatus("current")
_ArubaModuleJL255A_ObjectIdentity = ObjectIdentity
arubaModuleJL255A = _ArubaModuleJL255A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 20, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL255A.setStatus("current")
_ArubaSwitchJL256A_ObjectIdentity = ObjectIdentity
arubaSwitchJL256A = _ArubaSwitchJL256A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 21)
)
if mibBuilder.loadTexts:
    arubaSwitchJL256A.setStatus("current")
_ArubaModuleJL256A_ObjectIdentity = ObjectIdentity
arubaModuleJL256A = _ArubaModuleJL256A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 21, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL256A.setStatus("current")
_ArubaSwitchJL259A_ObjectIdentity = ObjectIdentity
arubaSwitchJL259A = _ArubaSwitchJL259A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 22)
)
if mibBuilder.loadTexts:
    arubaSwitchJL259A.setStatus("current")
_ArubaModuleJL259A_ObjectIdentity = ObjectIdentity
arubaModuleJL259A = _ArubaModuleJL259A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 22, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL259A.setStatus("current")
_ArubaSwitchJL260A_ObjectIdentity = ObjectIdentity
arubaSwitchJL260A = _ArubaSwitchJL260A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 23)
)
if mibBuilder.loadTexts:
    arubaSwitchJL260A.setStatus("current")
_ArubaModuleJL260A_ObjectIdentity = ObjectIdentity
arubaModuleJL260A = _ArubaModuleJL260A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 23, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL260A.setStatus("current")
_ArubaSwitchJL261A_ObjectIdentity = ObjectIdentity
arubaSwitchJL261A = _ArubaSwitchJL261A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 24)
)
if mibBuilder.loadTexts:
    arubaSwitchJL261A.setStatus("current")
_ArubaModuleJL261A_ObjectIdentity = ObjectIdentity
arubaModuleJL261A = _ArubaModuleJL261A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 24, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL261A.setStatus("current")
_ArubaSwitchJL262A_ObjectIdentity = ObjectIdentity
arubaSwitchJL262A = _ArubaSwitchJL262A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 25)
)
if mibBuilder.loadTexts:
    arubaSwitchJL262A.setStatus("current")
_ArubaModuleJL262A_ObjectIdentity = ObjectIdentity
arubaModuleJL262A = _ArubaModuleJL262A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 25, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL262A.setStatus("current")
_ArubaSwitchJL558A_ObjectIdentity = ObjectIdentity
arubaSwitchJL558A = _ArubaSwitchJL558A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 26)
)
if mibBuilder.loadTexts:
    arubaSwitchJL558A.setStatus("current")
_ArubaModuleJL558A_ObjectIdentity = ObjectIdentity
arubaModuleJL558A = _ArubaModuleJL558A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 26, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL558A.setStatus("current")
_ArubaSwitchJL557A_ObjectIdentity = ObjectIdentity
arubaSwitchJL557A = _ArubaSwitchJL557A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 27)
)
if mibBuilder.loadTexts:
    arubaSwitchJL557A.setStatus("current")
_ArubaModuleJL557A_ObjectIdentity = ObjectIdentity
arubaModuleJL557A = _ArubaModuleJL557A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 27, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL557A.setStatus("current")
_ArubaSwitchJL263A_ObjectIdentity = ObjectIdentity
arubaSwitchJL263A = _ArubaSwitchJL263A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 276)
)
if mibBuilder.loadTexts:
    arubaSwitchJL263A.setStatus("current")
_ArubaModuleJL263A_ObjectIdentity = ObjectIdentity
arubaModuleJL263A = _ArubaModuleJL263A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 276, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL263A.setStatus("current")
_ArubaSwitchJL264A_ObjectIdentity = ObjectIdentity
arubaSwitchJL264A = _ArubaSwitchJL264A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 277)
)
if mibBuilder.loadTexts:
    arubaSwitchJL264A.setStatus("current")
_ArubaModuleJL264A_ObjectIdentity = ObjectIdentity
arubaModuleJL264A = _ArubaModuleJL264A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 277, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL264A.setStatus("current")
_ArubaSwitchJL559A_ObjectIdentity = ObjectIdentity
arubaSwitchJL559A = _ArubaSwitchJL559A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 282)
)
if mibBuilder.loadTexts:
    arubaSwitchJL559A.setStatus("current")
_ArubaModuleJL559A_ObjectIdentity = ObjectIdentity
arubaModuleJL559A = _ArubaModuleJL559A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 181, 282, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL559A.setStatus("current")
_ArubaSwitch2540_ObjectIdentity = ObjectIdentity
arubaSwitch2540 = _ArubaSwitch2540_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182)
)
if mibBuilder.loadTexts:
    arubaSwitch2540.setStatus("current")
_ArubaSwitchJL354A_ObjectIdentity = ObjectIdentity
arubaSwitchJL354A = _ArubaSwitchJL354A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 18)
)
if mibBuilder.loadTexts:
    arubaSwitchJL354A.setStatus("current")
_ArubaModuleJL354A_ObjectIdentity = ObjectIdentity
arubaModuleJL354A = _ArubaModuleJL354A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 18, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL354A.setStatus("current")
_ArubaSwitchJL355A_ObjectIdentity = ObjectIdentity
arubaSwitchJL355A = _ArubaSwitchJL355A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 19)
)
if mibBuilder.loadTexts:
    arubaSwitchJL355A.setStatus("current")
_ArubaModuleJL355A_ObjectIdentity = ObjectIdentity
arubaModuleJL355A = _ArubaModuleJL355A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 19, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL355A.setStatus("current")
_ArubaSwitchJL356A_ObjectIdentity = ObjectIdentity
arubaSwitchJL356A = _ArubaSwitchJL356A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 20)
)
if mibBuilder.loadTexts:
    arubaSwitchJL356A.setStatus("current")
_ArubaModuleJL356A_ObjectIdentity = ObjectIdentity
arubaModuleJL356A = _ArubaModuleJL356A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 20, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL356A.setStatus("current")
_ArubaSwitchJL357A_ObjectIdentity = ObjectIdentity
arubaSwitchJL357A = _ArubaSwitchJL357A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 21)
)
if mibBuilder.loadTexts:
    arubaSwitchJL357A.setStatus("current")
_ArubaModuleJL357A_ObjectIdentity = ObjectIdentity
arubaModuleJL357A = _ArubaModuleJL357A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 182, 21, 1)
)
if mibBuilder.loadTexts:
    arubaModuleJL357A.setStatus("current")
_IcfCommon_ObjectIdentity = ObjectIdentity
icfCommon = _IcfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 1)
)
_IcfHub_ObjectIdentity = ObjectIdentity
icfHub = _IcfHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 2)
)
_IcfBridge_ObjectIdentity = ObjectIdentity
icfBridge = _IcfBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 3)
)
_IcfSecurity_ObjectIdentity = ObjectIdentity
icfSecurity = _IcfSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 4)
)
_IcfConfig_ObjectIdentity = ObjectIdentity
icfConfig = _IcfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 5)
)
_IcfEsSwitch_ObjectIdentity = ObjectIdentity
icfEsSwitch = _IcfEsSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6)
)
_HpEs_ObjectIdentity = ObjectIdentity
hpEs = _HpEs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 1)
)
_HpEs2_ObjectIdentity = ObjectIdentity
hpEs2 = _HpEs2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 2)
)
_HpNetSwitch_ObjectIdentity = ObjectIdentity
hpNetSwitch = _HpNetSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 6, 3)
)
_IcfRouter_ObjectIdentity = ObjectIdentity
icfRouter = _IcfRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 7)
)
_IcfDot12Draft_ObjectIdentity = ObjectIdentity
icfDot12Draft = _IcfDot12Draft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8)
)
_IcfVgRepeater_ObjectIdentity = ObjectIdentity
icfVgRepeater = _IcfVgRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 1)
)
_IcfVgInterface_ObjectIdentity = ObjectIdentity
icfVgInterface = _IcfVgInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 8, 2)
)
_HpEntityMIB_ObjectIdentity = ObjectIdentity
hpEntityMIB = _HpEntityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 9)
)
_HpicfAdmin_ObjectIdentity = ObjectIdentity
hpicfAdmin = _HpicfAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10)
)
_HpicfDomains_ObjectIdentity = ObjectIdentity
hpicfDomains = _HpicfDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 1)
)
_HpicfLLCDomain_ObjectIdentity = ObjectIdentity
hpicfLLCDomain = _HpicfLLCDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfLLCDomain.setStatus("current")
_HpicfObjectModules_ObjectIdentity = ObjectIdentity
hpicfObjectModules = _HpicfObjectModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2)
)
_IcfSecurityMib_ObjectIdentity = ObjectIdentity
icfSecurityMib = _IcfSecurityMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 1)
)
_HpicfChainMib_ObjectIdentity = ObjectIdentity
hpicfChainMib = _HpicfChainMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 2)
)
_HpicfChassisMib_ObjectIdentity = ObjectIdentity
hpicfChassisMib = _HpicfChassisMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 3)
)
_HpicfDownloadMib_ObjectIdentity = ObjectIdentity
hpicfDownloadMib = _HpicfDownloadMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 4)
)
_HpicfBasicMib_ObjectIdentity = ObjectIdentity
hpicfBasicMib = _HpicfBasicMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5)
)
_HpicfStackMib_ObjectIdentity = ObjectIdentity
hpicfStackMib = _HpicfStackMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 6)
)
_HpicfLinkTestMib_ObjectIdentity = ObjectIdentity
hpicfLinkTestMib = _HpicfLinkTestMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 7)
)
_HpicfGenRptrMib_ObjectIdentity = ObjectIdentity
hpicfGenRptrMib = _HpicfGenRptrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 8)
)
_Hpicf8023RptrMib_ObjectIdentity = ObjectIdentity
hpicf8023RptrMib = _Hpicf8023RptrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 9)
)
_IcfVgRepeaterMib_ObjectIdentity = ObjectIdentity
icfVgRepeaterMib = _IcfVgRepeaterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 10)
)
_HpicfVgRptrMib_ObjectIdentity = ObjectIdentity
hpicfVgRptrMib = _HpicfVgRptrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 11)
)
_HpicfFaultFinderMib_ObjectIdentity = ObjectIdentity
hpicfFaultFinderMib = _HpicfFaultFinderMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 12)
)
_HpicfJumboMIB_ObjectIdentity = ObjectIdentity
hpicfJumboMIB = _HpicfJumboMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 13)
)
_HpicfRateLimitMIB_ObjectIdentity = ObjectIdentity
hpicfRateLimitMIB = _HpicfRateLimitMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14)
)
_HpicfAgentModules_ObjectIdentity = ObjectIdentity
hpicfAgentModules = _HpicfAgentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 3)
)
_HpicfETwistHubAgentsMib_ObjectIdentity = ObjectIdentity
hpicfETwistHubAgentsMib = _HpicfETwistHubAgentsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 3, 1)
)
_HpicfETwistBridgeAgentsMib_ObjectIdentity = ObjectIdentity
hpicfETwistBridgeAgentsMib = _HpicfETwistBridgeAgentsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 3, 2)
)
_HpicfAdvStk8023AgentsMib_ObjectIdentity = ObjectIdentity
hpicfAdvStk8023AgentsMib = _HpicfAdvStk8023AgentsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 3, 3)
)
_HpicfAdvStkVGAgentsMib_ObjectIdentity = ObjectIdentity
hpicfAdvStkVGAgentsMib = _HpicfAdvStkVGAgentsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 3, 4)
)
_HpicfTextualConventions_ObjectIdentity = ObjectIdentity
hpicfTextualConventions = _HpicfTextualConventions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 4)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)
_HpicfCommon_ObjectIdentity = ObjectIdentity
hpicfCommon = _HpicfCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1)
)
_HpicfChain_ObjectIdentity = ObjectIdentity
hpicfChain = _HpicfChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 1)
)
_HpicfChassis_ObjectIdentity = ObjectIdentity
hpicfChassis = _HpicfChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 2)
)
_HpicfDownload_ObjectIdentity = ObjectIdentity
hpicfDownload = _HpicfDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 3)
)
_HpicfBasic_ObjectIdentity = ObjectIdentity
hpicfBasic = _HpicfBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4)
)
_HpicfStack_ObjectIdentity = ObjectIdentity
hpicfStack = _HpicfStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 5)
)
_HpicfLinktest_ObjectIdentity = ObjectIdentity
hpicfLinktest = _HpicfLinktest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 6)
)
_HpicfFaultFinder_ObjectIdentity = ObjectIdentity
hpicfFaultFinder = _HpicfFaultFinder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 7)
)
_HpicfPOE_ObjectIdentity = ObjectIdentity
hpicfPOE = _HpicfPOE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 9)
)
_HpicfCommonSecurity_ObjectIdentity = ObjectIdentity
hpicfCommonSecurity = _HpicfCommonSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 12)
)
_HpicfSrcIpMIB_ObjectIdentity = ObjectIdentity
hpicfSrcIpMIB = _HpicfSrcIpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 13)
)
_HpicfCoreDumpMIB_ObjectIdentity = ObjectIdentity
hpicfCoreDumpMIB = _HpicfCoreDumpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 14)
)
_HpicfRepeater_ObjectIdentity = ObjectIdentity
hpicfRepeater = _HpicfRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 2)
)
_HpicfVg_ObjectIdentity = ObjectIdentity
hpicfVg = _HpicfVg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 3)
)
_HpicfGenericRepeater_ObjectIdentity = ObjectIdentity
hpicfGenericRepeater = _HpicfGenericRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 4)
)
_HpicfSwitch_ObjectIdentity = ObjectIdentity
hpicfSwitch = _HpicfSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5)
)
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1)
)
_HpOpSystem_ObjectIdentity = ObjectIdentity
hpOpSystem = _HpOpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1)
)
_HpHwSystem_ObjectIdentity = ObjectIdentity
hpHwSystem = _HpHwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2)
)
_HpVLAN_ObjectIdentity = ObjectIdentity
hpVLAN = _HpVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 3)
)
_HpConfig_ObjectIdentity = ObjectIdentity
hpConfig = _HpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7)
)
_HpSwitchStatistics_ObjectIdentity = ObjectIdentity
hpSwitchStatistics = _HpSwitchStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 9)
)
_HpSwitchVirtualStackMib_ObjectIdentity = ObjectIdentity
hpSwitchVirtualStackMib = _HpSwitchVirtualStackMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 10)
)
_HpicfDhcpRelay_ObjectIdentity = ObjectIdentity
hpicfDhcpRelay = _HpicfDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 11)
)
_HpicfBridge_ObjectIdentity = ObjectIdentity
hpicfBridge = _HpicfBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 12)
)
_HpicfRip_ObjectIdentity = ObjectIdentity
hpicfRip = _HpicfRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 13)
)
_HpicfOspf_ObjectIdentity = ObjectIdentity
hpicfOspf = _HpicfOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 14)
)
_HpicfIpRouting_ObjectIdentity = ObjectIdentity
hpicfIpRouting = _HpicfIpRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15)
)
_HpSwitchAuthenticationMIB_ObjectIdentity = ObjectIdentity
hpSwitchAuthenticationMIB = _HpSwitchAuthenticationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 16)
)
_HpSwitchAccountingMIB_ObjectIdentity = ObjectIdentity
hpSwitchAccountingMIB = _HpSwitchAccountingMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 17)
)
_HpicfXrrpMIB_ObjectIdentity = ObjectIdentity
hpicfXrrpMIB = _HpicfXrrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 18)
)
_HpicfUsrAuthMIB_ObjectIdentity = ObjectIdentity
hpicfUsrAuthMIB = _HpicfUsrAuthMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 19)
)
_HpicfPimMIB_ObjectIdentity = ObjectIdentity
hpicfPimMIB = _HpicfPimMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20)
)
_HpicfUdpFwd_ObjectIdentity = ObjectIdentity
hpicfUdpFwd = _HpicfUdpFwd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23)
)
_HpicfConnectionRateFilter_ObjectIdentity = ObjectIdentity
hpicfConnectionRateFilter = _HpicfConnectionRateFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 24)
)
_HpicfDot1xMIB_ObjectIdentity = ObjectIdentity
hpicfDot1xMIB = _HpicfDot1xMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 25)
)
_HpicfVrrpMIB_ObjectIdentity = ObjectIdentity
hpicfVrrpMIB = _HpicfVrrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 31)
)
_HpSwitchAuthorizationMIB_ObjectIdentity = ObjectIdentity
hpSwitchAuthorizationMIB = _HpSwitchAuthorizationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 32)
)
_HpicfUdldMIB_ObjectIdentity = ObjectIdentity
hpicfUdldMIB = _HpicfUdldMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 33)
)
_HpicfIpDhcpSnoop_ObjectIdentity = ObjectIdentity
hpicfIpDhcpSnoop = _HpicfIpDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 34)
)
_HpicfInstMonMIB_ObjectIdentity = ObjectIdentity
hpicfInstMonMIB = _HpicfInstMonMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35)
)
_HpicfL3MacConfigMIB_ObjectIdentity = ObjectIdentity
hpicfL3MacConfigMIB = _HpicfL3MacConfigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 36)
)
_HpicfArpProtect_ObjectIdentity = ObjectIdentity
hpicfArpProtect = _HpicfArpProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37)
)
_HpicfSnmpMIB_ObjectIdentity = ObjectIdentity
hpicfSnmpMIB = _HpicfSnmpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 38)
)
_HpicfIpLockdown_ObjectIdentity = ObjectIdentity
hpicfIpLockdown = _HpicfIpLockdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 39)
)
_HpicfProviderBridge_ObjectIdentity = ObjectIdentity
hpicfProviderBridge = _HpicfProviderBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 40)
)
_HpicfGppcMIB_ObjectIdentity = ObjectIdentity
hpicfGppcMIB = _HpicfGppcMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 41)
)
_HpicfAutorun_ObjectIdentity = ObjectIdentity
hpicfAutorun = _HpicfAutorun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 42)
)
_HpicfInstMIB_ObjectIdentity = ObjectIdentity
hpicfInstMIB = _HpicfInstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 45)
)
_HpicfFtrCo_ObjectIdentity = ObjectIdentity
hpicfFtrCo = _HpicfFtrCo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46)
)
_HpicfMldMIB_ObjectIdentity = ObjectIdentity
hpicfMldMIB = _HpicfMldMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 48)
)
_HpicfDhcpv6Relay_ObjectIdentity = ObjectIdentity
hpicfDhcpv6Relay = _HpicfDhcpv6Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50)
)
_HpicfScriptMIB_ObjectIdentity = ObjectIdentity
hpicfScriptMIB = _HpicfScriptMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 51)
)
_HpicfUSBPortMIB_ObjectIdentity = ObjectIdentity
hpicfUSBPortMIB = _HpicfUSBPortMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 53)
)
_HpicfFanMIB_ObjectIdentity = ObjectIdentity
hpicfFanMIB = _HpicfFanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54)
)
_HpicfPsMIB_ObjectIdentity = ObjectIdentity
hpicfPsMIB = _HpicfPsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55)
)
_HpicfSavepowerMIB_ObjectIdentity = ObjectIdentity
hpicfSavepowerMIB = _HpicfSavepowerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 56)
)
_HpicfDhcpClient_ObjectIdentity = ObjectIdentity
hpicfDhcpClient = _HpicfDhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57)
)
_HpicfOobmMIB_ObjectIdentity = ObjectIdentity
hpicfOobmMIB = _HpicfOobmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 58)
)
_HpSwitchImage_ObjectIdentity = ObjectIdentity
hpSwitchImage = _HpSwitchImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 59)
)
_HpicfDosFilterMib_ObjectIdentity = ObjectIdentity
hpicfDosFilterMib = _HpicfDosFilterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 60)
)
_HpicfGppcv2MIB_ObjectIdentity = ObjectIdentity
hpicfGppcv2MIB = _HpicfGppcv2MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61)
)
_HpicfDebugLog_ObjectIdentity = ObjectIdentity
hpicfDebugLog = _HpicfDebugLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 64)
)
_HpicfMacNotifyMIB_ObjectIdentity = ObjectIdentity
hpicfMacNotifyMIB = _HpicfMacNotifyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 66)
)
_HpicfGenericVlanMIB_ObjectIdentity = ObjectIdentity
hpicfGenericVlanMIB = _HpicfGenericVlanMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 67)
)
_HpSwitchErrorMsgMIB_ObjectIdentity = ObjectIdentity
hpSwitchErrorMsgMIB = _HpSwitchErrorMsgMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 68)
)
_HpStackMIB_ObjectIdentity = ObjectIdentity
hpStackMIB = _HpStackMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 69)
)
_HpicfLayer3VlanConfigMIB_ObjectIdentity = ObjectIdentity
hpicfLayer3VlanConfigMIB = _HpicfLayer3VlanConfigMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 70)
)
_HpEntityPowerMIB_ObjectIdentity = ObjectIdentity
hpEntityPowerMIB = _HpEntityPowerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 71)
)
_HpicfTrafficTemplateMIB_ObjectIdentity = ObjectIdentity
hpicfTrafficTemplateMIB = _HpicfTrafficTemplateMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72)
)
_HpicfDcbxMIB_ObjectIdentity = ObjectIdentity
hpicfDcbxMIB = _HpicfDcbxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 73)
)
_HpicfUfdMIB_ObjectIdentity = ObjectIdentity
hpicfUfdMIB = _HpicfUfdMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74)
)
_HpSBMMIB_ObjectIdentity = ObjectIdentity
hpSBMMIB = _HpSBMMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 75)
)
_HpicfLoadBalanceMod_ObjectIdentity = ObjectIdentity
hpicfLoadBalanceMod = _HpicfLoadBalanceMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 76)
)
_HpTunnelMIB_ObjectIdentity = ObjectIdentity
hpTunnelMIB = _HpTunnelMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 77)
)
_HpicfTcpMib_ObjectIdentity = ObjectIdentity
hpicfTcpMib = _HpicfTcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79)
)
_HpicfTransceiverMIB_ObjectIdentity = ObjectIdentity
hpicfTransceiverMIB = _HpicfTransceiverMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 82)
)
_HpicfSvcsAppMIB_ObjectIdentity = ObjectIdentity
hpicfSvcsAppMIB = _HpicfSvcsAppMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 86)
)
_HpicfIpv6RAGuard_ObjectIdentity = ObjectIdentity
hpicfIpv6RAGuard = _HpicfIpv6RAGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 87)
)
_HpicfRpvstMIB_ObjectIdentity = ObjectIdentity
hpicfRpvstMIB = _HpicfRpvstMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 88)
)
_HpicfOpenFlowMIB_ObjectIdentity = ObjectIdentity
hpicfOpenFlowMIB = _HpicfOpenFlowMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 89)
)
_HpicfVrrpv3MIB_ObjectIdentity = ObjectIdentity
hpicfVrrpv3MIB = _HpicfVrrpv3MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 90)
)
_HpicfSflowMIB_ObjectIdentity = ObjectIdentity
hpicfSflowMIB = _HpicfSflowMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 92)
)
_HpicfMstpExtnMIB_ObjectIdentity = ObjectIdentity
hpicfMstpExtnMIB = _HpicfMstpExtnMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 94)
)
_HpicfMadMIB_ObjectIdentity = ObjectIdentity
hpicfMadMIB = _HpicfMadMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 95)
)
_HpicfSmartLinkMIB_ObjectIdentity = ObjectIdentity
hpicfSmartLinkMIB = _HpicfSmartLinkMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96)
)
_HpicfTR069MIB_ObjectIdentity = ObjectIdentity
hpicfTR069MIB = _HpicfTR069MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 98)
)
_HpicfDhcpv4ServerMIB_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerMIB = _HpicfDhcpv4ServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99)
)
_HpicfServiceTunnel_ObjectIdentity = ObjectIdentity
hpicfServiceTunnel = _HpicfServiceTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 100)
)
_HpicfDSnoopV6_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6 = _HpicfDSnoopV6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102)
)
_HpicfIpv6Lockdown_ObjectIdentity = ObjectIdentity
hpicfIpv6Lockdown = _HpicfIpv6Lockdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103)
)
_HpSwitchTrapMIB_ObjectIdentity = ObjectIdentity
hpSwitchTrapMIB = _HpSwitchTrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 104)
)
_HpicfJobSchedulerMIB_ObjectIdentity = ObjectIdentity
hpicfJobSchedulerMIB = _HpicfJobSchedulerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105)
)
_HpicfByodMIB_ObjectIdentity = ObjectIdentity
hpicfByodMIB = _HpicfByodMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106)
)
_HpicfVirtualNetwork_ObjectIdentity = ObjectIdentity
hpicfVirtualNetwork = _HpicfVirtualNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 107)
)
_HpicfDldpMIB_ObjectIdentity = ObjectIdentity
hpicfDldpMIB = _HpicfDldpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108)
)
_HpicfDot1qIsolatedPorts_ObjectIdentity = ObjectIdentity
hpicfDot1qIsolatedPorts = _HpicfDot1qIsolatedPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 109)
)
_HpicfTlsMinMIB_ObjectIdentity = ObjectIdentity
hpicfTlsMinMIB = _HpicfTlsMinMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 112)
)
_HpicfRipng_ObjectIdentity = ObjectIdentity
hpicfRipng = _HpicfRipng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 113)
)
_HpicfPrivateVlan_ObjectIdentity = ObjectIdentity
hpicfPrivateVlan = _HpicfPrivateVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 114)
)
_HpicfVsfVCMIB_ObjectIdentity = ObjectIdentity
hpicfVsfVCMIB = _HpicfVsfVCMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 116)
)
_HpicfMvrpMIB_ObjectIdentity = ObjectIdentity
hpicfMvrpMIB = _HpicfMvrpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 117)
)
_HpicfArpThrottle_ObjectIdentity = ObjectIdentity
hpicfArpThrottle = _HpicfArpThrottle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 119)
)
_HpicfBfd_ObjectIdentity = ObjectIdentity
hpicfBfd = _HpicfBfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 120)
)
_HpicfNtpMIB_ObjectIdentity = ObjectIdentity
hpicfNtpMIB = _HpicfNtpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 121)
)
_HpicfPim6MIB_ObjectIdentity = ObjectIdentity
hpicfPim6MIB = _HpicfPim6MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 122)
)
_HpicfMdns_ObjectIdentity = ObjectIdentity
hpicfMdns = _HpicfMdns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 124)
)
_HpicfAMPServerMIB_ObjectIdentity = ObjectIdentity
hpicfAMPServerMIB = _HpicfAMPServerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 125)
)
_HpicfDevConf_ObjectIdentity = ObjectIdentity
hpicfDevConf = _HpicfDevConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 126)
)
_HpicfIpSla_ObjectIdentity = ObjectIdentity
hpicfIpSla = _HpicfIpSla_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 127)
)
_HpicfTunneledNode_ObjectIdentity = ObjectIdentity
hpicfTunneledNode = _HpicfTunneledNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128)
)
_HpicfActivateMIB_ObjectIdentity = ObjectIdentity
hpicfActivateMIB = _HpicfActivateMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129)
)
_HpicfMcastMIB_ObjectIdentity = ObjectIdentity
hpicfMcastMIB = _HpicfMcastMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 130)
)
_HpicfUrpfMIB_ObjectIdentity = ObjectIdentity
hpicfUrpfMIB = _HpicfUrpfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 131)
)
_HpicfMinKeyMIB_ObjectIdentity = ObjectIdentity
hpicfMinKeyMIB = _HpicfMinKeyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 132)
)
_HpicfDeviceIdentityMIB_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityMIB = _HpicfDeviceIdentityMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135)
)
_HpicfConfig_ObjectIdentity = ObjectIdentity
hpicfConfig = _HpicfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 136)
)
_HpSwitchExperimental_ObjectIdentity = ObjectIdentity
hpSwitchExperimental = _HpSwitchExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2)
)
_HpicfSaviMIB_ObjectIdentity = ObjectIdentity
hpicfSaviMIB = _HpicfSaviMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 2, 1)
)
_HpicfAccess_ObjectIdentity = ObjectIdentity
hpicfAccess = _HpicfAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 6)
)
_HpicfWAN_ObjectIdentity = ObjectIdentity
hpicfWAN = _HpicfWAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7)
)
_HpWANRouters_ObjectIdentity = ObjectIdentity
hpWANRouters = _HpWANRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1)
)
_HpSRJ8751A_ObjectIdentity = ObjectIdentity
hpSRJ8751A = _HpSRJ8751A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpSRJ8751A.setStatus("current")
_HpSRJ8752A_ObjectIdentity = ObjectIdentity
hpSRJ8752A = _HpSRJ8752A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hpSRJ8752A.setStatus("current")
_HpSRJ8753A_ObjectIdentity = ObjectIdentity
hpSRJ8753A = _HpSRJ8753A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1, 3)
)
if mibBuilder.loadTexts:
    hpSRJ8753A.setStatus("current")
_HpSRJ8754A_ObjectIdentity = ObjectIdentity
hpSRJ8754A = _HpSRJ8754A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1, 4)
)
if mibBuilder.loadTexts:
    hpSRJ8754A.setStatus("current")
_HpSRPowerSupply8756A_ObjectIdentity = ObjectIdentity
hpSRPowerSupply8756A = _HpSRPowerSupply8756A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpSRPowerSupply8756A.setStatus("current")
_HpWANModules_ObjectIdentity = ObjectIdentity
hpWANModules = _HpWANModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2)
)
_HpSRmoduleJ8451A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8451A = _HpSRmoduleJ8451A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8451A.setStatus("current")
_HpSRmoduleJ8452A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8452A = _HpSRmoduleJ8452A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 2)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8452A.setStatus("current")
_HpSRmoduleJ8453A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8453A = _HpSRmoduleJ8453A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8453A.setStatus("current")
_HpSRmoduleJ8454A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8454A = _HpSRmoduleJ8454A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 4)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8454A.setStatus("current")
_HpSRmoduleJ8455A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8455A = _HpSRmoduleJ8455A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 5)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8455A.setStatus("current")
_HpSRmoduleJ8456A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8456A = _HpSRmoduleJ8456A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 6)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8456A.setStatus("current")
_HpSRmoduleJ8457A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8457A = _HpSRmoduleJ8457A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 7)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8457A.setStatus("current")
_HpSRmoduleJ8458A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8458A = _HpSRmoduleJ8458A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 8)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8458A.setStatus("current")
_HpSRmoduleJ8459A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8459A = _HpSRmoduleJ8459A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 9)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8459A.setStatus("current")
_HpSRmoduleJ8759A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8759A = _HpSRmoduleJ8759A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 10)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8759A.setStatus("current")
_HpSRmoduleJ8460A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8460A = _HpSRmoduleJ8460A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 11)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8460A.setStatus("current")
_HpSRmoduleJ8461A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8461A = _HpSRmoduleJ8461A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 12)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8461A.setStatus("current")
_HpSRmoduleJ8462A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8462A = _HpSRmoduleJ8462A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 13)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8462A.setStatus("current")
_HpSRmoduleJ8463A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8463A = _HpSRmoduleJ8463A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 14)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8463A.setStatus("current")
_HpSRmoduleJ8464A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8464A = _HpSRmoduleJ8464A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 15)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8464A.setStatus("current")
_HpSRmoduleJ8465A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8465A = _HpSRmoduleJ8465A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 16)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8465A.setStatus("current")
_HpSRmoduleJ8471A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8471A = _HpSRmoduleJ8471A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 17)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8471A.setStatus("current")
_HpSRmoduleJ8472A_ObjectIdentity = ObjectIdentity
hpSRmoduleJ8472A = _HpSRmoduleJ8472A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 7, 2, 18)
)
if mibBuilder.loadTexts:
    hpSRmoduleJ8472A.setStatus("current")
_HpicfFabric_ObjectIdentity = ObjectIdentity
hpicfFabric = _HpicfFabric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 8)
)
_HpicfSecurityDevice_ObjectIdentity = ObjectIdentity
hpicfSecurityDevice = _HpicfSecurityDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 9)
)
_HpicfSysMgmt_ObjectIdentity = ObjectIdentity
hpicfSysMgmt = _HpicfSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 10)
)
_HpicfNotifications_ObjectIdentity = ObjectIdentity
hpicfNotifications = _HpicfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12)
)
_HpicfCommonTraps_ObjectIdentity = ObjectIdentity
hpicfCommonTraps = _HpicfCommonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1)
)
_HpicfCommonTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicfCommonTrapsPrefix = _HpicfCommonTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0)
)
_Hpicf8023RptrTraps_ObjectIdentity = ObjectIdentity
hpicf8023RptrTraps = _Hpicf8023RptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2)
)
_Hpicf8023RptrTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicf8023RptrTrapsPrefix = _Hpicf8023RptrTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 2, 0)
)
_HpicfVgRptrTraps_ObjectIdentity = ObjectIdentity
hpicfVgRptrTraps = _HpicfVgRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3)
)
_HpicfVgRptrTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicfVgRptrTrapsPrefix = _HpicfVgRptrTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 3, 0)
)
_HpicfGenRptrTraps_ObjectIdentity = ObjectIdentity
hpicfGenRptrTraps = _HpicfGenRptrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 4)
)
_HpicfGenRptrTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicfGenRptrTrapsPrefix = _HpicfGenRptrTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 4, 0)
)
_HpicfRateLimitTraps_ObjectIdentity = ObjectIdentity
hpicfRateLimitTraps = _HpicfRateLimitTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 5)
)
_HpicfRateLimitTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicfRateLimitTrapsPrefix = _HpicfRateLimitTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 5, 0)
)
_HpicfSecLoggingTraps_ObjectIdentity = ObjectIdentity
hpicfSecLoggingTraps = _HpicfSecLoggingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 6)
)
_HpicfSecLoggingTrapsPrefix_ObjectIdentity = ObjectIdentity
hpicfSecLoggingTrapsPrefix = _HpicfSecLoggingTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 6, 0)
)
_HpicfOEMs_ObjectIdentity = ObjectIdentity
hpicfOEMs = _HpicfOEMs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 13)
)
_HpicfFEHub_ObjectIdentity = ObjectIdentity
hpicfFEHub = _HpicfFEHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 13, 1)
)
_HpicfSyslog_ObjectIdentity = ObjectIdentity
hpicfSyslog = _HpicfSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 14)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-OID",
    **{"hp": hp,
       "nm": nm,
       "hpSystem": hpSystem,
       "netElement": netElement,
       "bridge": bridge,
       "bridge1010": bridge1010,
       "bridgeRemote": bridgeRemote,
       "eswitch": eswitch,
       "eswitch2": eswitch2,
       "netSwitch100": netSwitch100,
       "netSwitch200": netSwitch200,
       "router": router,
       "icfRouterER": icfRouterER,
       "icfRouterTR": icfRouterTR,
       "icfRouterSR": icfRouterSR,
       "icfRouterFR": icfRouterFR,
       "icfRouterLR": icfRouterLR,
       "icfRouterBR": icfRouterBR,
       "icfRouterPR": icfRouterPR,
       "icfRouter650": icfRouter650,
       "icfRouter650Engine": icfRouter650Engine,
       "icfRouter650Port4E": icfRouter650Port4E,
       "icfRouter650Port4S": icfRouter650Port4S,
       "icfRouter650Port4T": icfRouter650Port4T,
       "icfRouter650PortFDDI": icfRouter650PortFDDI,
       "icfRouter650Port100VG": icfRouter650Port100VG,
       "icfRouter230": icfRouter230,
       "icfRouter250": icfRouter250,
       "icfRouter255": icfRouter255,
       "icfRouter210": icfRouter210,
       "hub": hub,
       "etherTwist12": etherTwist12,
       "fiberOptic": fiberOptic,
       "etherTwist48": etherTwist48,
       "thinLAN": thinLAN,
       "etherTwist24S": etherTwist24S,
       "advStack12": advStack12,
       "advStack24": advStack24,
       "advStack48": advStack48,
       "advStackVg15": advStackVg15,
       "advStackU8": advStackU8,
       "advStackU16": advStackU16,
       "advStackVg6": advStackVg6,
       "advStackVg12": advStackVg12,
       "hpAdvStkEnetSH12R": hpAdvStkEnetSH12R,
       "hpAdvStkEnetSH24R": hpAdvStkEnetSH24R,
       "hpAdvStkEnetSH24T": hpAdvStkEnetSH24T,
       "hpAdvStk100Tx12TM": hpAdvStk100Tx12TM,
       "hp10THub16M": hp10THub16M,
       "hp10BaseTHub12M": hp10BaseTHub12M,
       "hp10BaseTHub24M": hp10BaseTHub24M,
       "hpProCurve10T100THub12M": hpProCurve10T100THub12M,
       "hpProCurve10T100THub24M": hpProCurve10T100THub24M,
       "chassis": chassis,
       "repeaterAgent": repeaterAgent,
       "chassisAgents": chassisAgents,
       "icfVgAgent": icfVgAgent,
       "icfVgAgent2": icfVgAgent2,
       "hpicfEnetSMM": hpicfEnetSMM,
       "hpAdvStkEnetSHAgent": hpAdvStkEnetSHAgent,
       "hpAdvStkSwStackTopMgmt": hpAdvStkSwStackTopMgmt,
       "hpSwitch8000CpuCard": hpSwitch8000CpuCard,
       "icfSensors": icfSensors,
       "icfPowerSupplySensor": icfPowerSupplySensor,
       "icfFanSensor": icfFanSensor,
       "icfTemperatureSensor": icfTemperatureSensor,
       "icfFutureSlotSensor": icfFutureSlotSensor,
       "icfCards": icfCards,
       "icfUnidentifiedCard": icfUnidentifiedCard,
       "hpAdvStkEnetSHSwitch": hpAdvStkEnetSHSwitch,
       "hpAdvStkSwStackExpander": hpAdvStkSwStackExpander,
       "hpicfStacks": hpicfStacks,
       "hpAdvStkEnetSHStack": hpAdvStkEnetSHStack,
       "hpStack": hpStack,
       "hpStack2920": hpStack2920,
       "arubaStack3810": arubaStack3810,
       "arubaStack2930": arubaStack2930,
       "hpStackVSF5400R": hpStackVSF5400R,
       "arubaStack2930M": arubaStack2930M,
       "hpicfBackplanes": hpicfBackplanes,
       "hpAdvStkEnetSHExtSeg": hpAdvStkEnetSHExtSeg,
       "hpAdvStkEnetSHIntSeg": hpAdvStkEnetSHIntSeg,
       "hp10BaseTHubSeg": hp10BaseTHubSeg,
       "hpSwitchBackplane": hpSwitchBackplane,
       "hp100BaseTHubSeg": hp100BaseTHubSeg,
       "hpicfSlots": hpicfSlots,
       "hpAdvStkEnetSHAgentSlot": hpAdvStkEnetSHAgentSlot,
       "hpAdvStkEnetSHIOSlot": hpAdvStkEnetSHIOSlot,
       "hpAdvStkSwStackMgmtSlot": hpAdvStkSwStackMgmtSlot,
       "hpAdvStkSwStackExpSlot": hpAdvStkSwStackExpSlot,
       "hpSwitch8000PowerSupplyBay": hpSwitch8000PowerSupplyBay,
       "hpSwitch8000CpuSlot": hpSwitch8000CpuSlot,
       "hpSwitch8000PortSlot": hpSwitch8000PortSlot,
       "hpSwitch2524PortSlot": hpSwitch2524PortSlot,
       "hpSwitch5308PowerSupplyBay": hpSwitch5308PowerSupplyBay,
       "hpSwitch5308PortSlot": hpSwitch5308PortSlot,
       "hpSwitch4865PowerSupplyBay": hpSwitch4865PowerSupplyBay,
       "hpSwitch4865PortSlot": hpSwitch4865PortSlot,
       "hpSwitch2650PortSlot": hpSwitch2650PortSlot,
       "hpSwitch6108PortSlot": hpSwitch6108PortSlot,
       "hpSwitch2824PortSlot": hpSwitch2824PortSlot,
       "hpSwitch2626PortSlot": hpSwitch2626PortSlot,
       "hpSwitch2650PPortSlot": hpSwitch2650PPortSlot,
       "hpSwitch2626PPortSlot": hpSwitch2626PPortSlot,
       "hpSwitch3324PortSlot": hpSwitch3324PortSlot,
       "hpSwitch2650CRPortSlot": hpSwitch2650CRPortSlot,
       "hpSwitch2626CRPortSlot": hpSwitch2626CRPortSlot,
       "hpSwitch2600n8PPortSlot": hpSwitch2600n8PPortSlot,
       "hpSwitch869xPowerSupplyBay": hpSwitch869xPowerSupplyBay,
       "hpSwitch869xPortSlot": hpSwitch869xPortSlot,
       "hpSwitch2510PortSlot": hpSwitch2510PortSlot,
       "hpSwitch2810PortSlot": hpSwitch2810PortSlot,
       "hpSwitch5400CpuCardBay": hpSwitch5400CpuCardBay,
       "hpSwitch8212FabricBay": hpSwitch8212FabricBay,
       "hpSwitch2610PortSlot": hpSwitch2610PortSlot,
       "hpSwitch2610PPortSlot": hpSwitch2610PPortSlot,
       "hpSwitch2510BPortSlot": hpSwitch2510BPortSlot,
       "hpSwitch2626CPortSlot": hpSwitch2626CPortSlot,
       "hpSwitch2650CPortSlot": hpSwitch2650CPortSlot,
       "hpSwitch2910PortSlot": hpSwitch2910PortSlot,
       "hpSwitch2510GPortSlot": hpSwitch2510GPortSlot,
       "hpSwitch2520PortSlot": hpSwitch2520PortSlot,
       "hpSwitch2520GPortSlot": hpSwitch2520GPortSlot,
       "hpSwitch2615PortSlot": hpSwitch2615PortSlot,
       "hpSwitch2915PortSlot": hpSwitch2915PortSlot,
       "hpSwitchJ9580PowerSupply": hpSwitchJ9580PowerSupply,
       "hpSwitchJ9581PowerSupply": hpSwitchJ9581PowerSupply,
       "hpSwitchJ9582FanTray": hpSwitchJ9582FanTray,
       "hpSwitch2620PortSlot": hpSwitch2620PortSlot,
       "hpSwitch2530PortSlot": hpSwitch2530PortSlot,
       "hpSwitch2920StackingSlot": hpSwitch2920StackingSlot,
       "hpSwitchJ9737APowerSupply": hpSwitchJ9737APowerSupply,
       "hpSwitchJ9738APowerSupply": hpSwitchJ9738APowerSupply,
       "hpSwitchJ9739APowerSupply": hpSwitchJ9739APowerSupply,
       "hpSwitch2920PortSlot": hpSwitch2920PortSlot,
       "hpSwitch3800StackingSlot": hpSwitch3800StackingSlot,
       "hpSwitchJ9828APowerSupply": hpSwitchJ9828APowerSupply,
       "hpSwitchJ9829APowerSupply": hpSwitchJ9829APowerSupply,
       "hpSwitchJ9830APowerSupply": hpSwitchJ9830APowerSupply,
       "hpSwitchJ9831AFanTray": hpSwitchJ9831AFanTray,
       "hpSwitchJ9832AFanTray": hpSwitchJ9832AFanTray,
       "hpSwitchJ9805APowerSupply": hpSwitchJ9805APowerSupply,
       "hpSwitchJ9806APowerCable": hpSwitchJ9806APowerCable,
       "arubaJL085APowerSupply": arubaJL085APowerSupply,
       "arubaJL086APowerSupply": arubaJL086APowerSupply,
       "arubaJL087APowerSupply": arubaJL087APowerSupply,
       "hpicfHubPorts": hpicfHubPorts,
       "hpAdvStkEnetSHExtPort": hpAdvStkEnetSHExtPort,
       "hpAdvStkEnetSHIntPort": hpAdvStkEnetSHIntPort,
       "hpAdvStkEnetSHAgentPort": hpAdvStkEnetSHAgentPort,
       "hp10BaseTHubPort": hp10BaseTHubPort,
       "hp10BaseTHubAgentPort": hp10BaseTHubAgentPort,
       "hp10T100THubPort": hp10T100THubPort,
       "hp100BaseTHubAgentPort": hp100BaseTHubAgentPort,
       "hpicfEnetChipSets": hpicfEnetChipSets,
       "hpicfEnetChipSetHydra": hpicfEnetChipSetHydra,
       "hpicfEnetChipSetGT48001": hpicfEnetChipSetGT48001,
       "hpicfEnetChipSetPentagon": hpicfEnetChipSetPentagon,
       "hpicfSwitchPorts": hpicfSwitchPorts,
       "hpicfSwitchPort10T100TX": hpicfSwitchPort10T100TX,
       "hpicfSwitchPort100FX": hpicfSwitchPort100FX,
       "hpicfSwitchPort10FL": hpicfSwitchPort10FL,
       "hpicfSwitchPort1000SX": hpicfSwitchPort1000SX,
       "hpicfSwitchPort10T": hpicfSwitchPort10T,
       "hpicfSwitchPort1000LX": hpicfSwitchPort1000LX,
       "hpicfSwitchPort1000T": hpicfSwitchPort1000T,
       "hpicfSwitchPort1000Stk": hpicfSwitchPort1000Stk,
       "hpicfSwitchPort1000LH": hpicfSwitchPort1000LH,
       "hpicfSwitchPort10GigBaseCX4": hpicfSwitchPort10GigBaseCX4,
       "hpicfSwitchPort1000ESP": hpicfSwitchPort1000ESP,
       "hpicfSwitchPort10GigBaseSR": hpicfSwitchPort10GigBaseSR,
       "hpicfSwitchPort10GigBaseER": hpicfSwitchPort10GigBaseER,
       "hpicfSwitchPort10GigBaseLR": hpicfSwitchPort10GigBaseLR,
       "hpicfSwitchPort100GEN": hpicfSwitchPort100GEN,
       "hpicfSwitchPort1000GEN": hpicfSwitchPort1000GEN,
       "hpicfSwitchPort10GigBaseGEN": hpicfSwitchPort10GigBaseGEN,
       "hpicfSwitchPort100BXD": hpicfSwitchPort100BXD,
       "hpicfSwitchPort100BXU": hpicfSwitchPort100BXU,
       "hpicfSwitchPort1000BXD": hpicfSwitchPort1000BXD,
       "hpicfSwitchPort1000BXU": hpicfSwitchPort1000BXU,
       "hpicfSwitchPort10GigBaseLRM": hpicfSwitchPort10GigBaseLRM,
       "hpicfSwitchPortSFPplusSR": hpicfSwitchPortSFPplusSR,
       "hpicfSwitchPortSFPplusLR": hpicfSwitchPortSFPplusLR,
       "hpicfSwitchPortSFPplusLRM": hpicfSwitchPortSFPplusLRM,
       "hpicfSwitchPortSFPplusDAC": hpicfSwitchPortSFPplusDAC,
       "hpicfSwitchPortSFPplusDA1": hpicfSwitchPortSFPplusDA1,
       "hpicfSwitchPortSFPplusDA2": hpicfSwitchPortSFPplusDA2,
       "hpicfSwitchPortSFPplusDA3": hpicfSwitchPortSFPplusDA3,
       "hpicfSwitchPortSFPplusDA5": hpicfSwitchPortSFPplusDA5,
       "hpicfSwitchPortSFPplusDA7": hpicfSwitchPortSFPplusDA7,
       "hpicfSwitchPortSFPplusDA10": hpicfSwitchPortSFPplusDA10,
       "hpicfSwitchPortSFPplusDA15": hpicfSwitchPortSFPplusDA15,
       "hpicfSwitchPortSFPplusDA20": hpicfSwitchPortSFPplusDA20,
       "hpicfSwitchPort10GigBaseT": hpicfSwitchPort10GigBaseT,
       "hpicfSwitchPort10GigBaseTSH": hpicfSwitchPort10GigBaseTSH,
       "hpicfSwitchPort10GigBaseTLH": hpicfSwitchPort10GigBaseTLH,
       "hpicfSwitchPort10GigBaseSTK": hpicfSwitchPort10GigBaseSTK,
       "hpicfSwitchPort1000CWDM1470": hpicfSwitchPort1000CWDM1470,
       "hpicfSwitchPort1000CWDM1490": hpicfSwitchPort1000CWDM1490,
       "hpicfSwitchPort1000CWDM1510": hpicfSwitchPort1000CWDM1510,
       "hpicfSwitchPort1000CWDM1530": hpicfSwitchPort1000CWDM1530,
       "hpicfSwitchPort1000CWDM1550": hpicfSwitchPort1000CWDM1550,
       "hpicfSwitchPort1000CWDM1570": hpicfSwitchPort1000CWDM1570,
       "hpicfSwitchPort1000CWDM1590": hpicfSwitchPort1000CWDM1590,
       "hpicfSwitchPort1000CWDM1610": hpicfSwitchPort1000CWDM1610,
       "hpicfSwitchPort10GigCWDM1470": hpicfSwitchPort10GigCWDM1470,
       "hpicfSwitchPort10GigCWDM1490": hpicfSwitchPort10GigCWDM1490,
       "hpicfSwitchPort10GigCWDM1510": hpicfSwitchPort10GigCWDM1510,
       "hpicfSwitchPort10GigCWDM1530": hpicfSwitchPort10GigCWDM1530,
       "hpicfSwitchPort10GigCWDM1550": hpicfSwitchPort10GigCWDM1550,
       "hpicfSwitchPort10GigCWDM1570": hpicfSwitchPort10GigCWDM1570,
       "hpicfSwitchPort10GigCWDM1590": hpicfSwitchPort10GigCWDM1590,
       "hpicfSwitchPort10GigCWDM1611": hpicfSwitchPort10GigCWDM1611,
       "hpicfSwitchPort5GigBaseT": hpicfSwitchPort5GigBaseT,
       "hpicfMAUTypes": hpicfMAUTypes,
       "hpicfMauType1000BaseSXHD": hpicfMauType1000BaseSXHD,
       "hpicfMauType1000BaseSXFD": hpicfMauType1000BaseSXFD,
       "hpicfMauType1000BaseLXHD": hpicfMauType1000BaseLXHD,
       "hpicfMauType1000BaseLXFD": hpicfMauType1000BaseLXFD,
       "hpicfMauType1000BaseTHD": hpicfMauType1000BaseTHD,
       "hpicfMauType1000BaseTFD": hpicfMauType1000BaseTFD,
       "hpicfMauType1000BaseStkHD": hpicfMauType1000BaseStkHD,
       "hpicfMauType1000BaseStkFD": hpicfMauType1000BaseStkFD,
       "hpicfMauType1000BaseLHFD": hpicfMauType1000BaseLHFD,
       "hpicfMauType1000BaseEspPCS": hpicfMauType1000BaseEspPCS,
       "hpicfMauType1000BaseEspG": hpicfMauType1000BaseEspG,
       "hpicfMauType10GigBaseCX4": hpicfMauType10GigBaseCX4,
       "hpicfMauType10GigBaseSR": hpicfMauType10GigBaseSR,
       "hpicfMauType10GigBaseER": hpicfMauType10GigBaseER,
       "hpicfMauType10GigBaseLR": hpicfMauType10GigBaseLR,
       "hpicfMauType100BaseGEN": hpicfMauType100BaseGEN,
       "hpicfMauType1000BaseGEN": hpicfMauType1000BaseGEN,
       "hpicfMauType10GigBaseGEN": hpicfMauType10GigBaseGEN,
       "hpicfMauType100BaseBXD": hpicfMauType100BaseBXD,
       "hpicfMauType100BaseBXU": hpicfMauType100BaseBXU,
       "hpicfMauType1000BaseBXD": hpicfMauType1000BaseBXD,
       "hpicfMauType1000BaseBXU": hpicfMauType1000BaseBXU,
       "hpicfMauType10GigBaseLRM": hpicfMauType10GigBaseLRM,
       "hpicfMauTypeSFPplusSR": hpicfMauTypeSFPplusSR,
       "hpicfMauTypeSFPplusLR": hpicfMauTypeSFPplusLR,
       "hpicfMauTypeSFPplusLRM": hpicfMauTypeSFPplusLRM,
       "hpicfMauTypeSFPplusDAC": hpicfMauTypeSFPplusDAC,
       "hpicfMauTypeSFPplusDA1": hpicfMauTypeSFPplusDA1,
       "hpicfMauTypeSFPplusDA2": hpicfMauTypeSFPplusDA2,
       "hpicfMauTypeSFPplusDA3": hpicfMauTypeSFPplusDA3,
       "hpicfMauTypeSFPplusDA5": hpicfMauTypeSFPplusDA5,
       "hpicfMauTypeSFPplusDA7": hpicfMauTypeSFPplusDA7,
       "hpicfMauTypeSFPplusDA10": hpicfMauTypeSFPplusDA10,
       "hpicfMauTypeSFPplusDA15": hpicfMauTypeSFPplusDA15,
       "hpicfMauTypeSFPplusDA20": hpicfMauTypeSFPplusDA20,
       "hpicfMauType10GigBaseT": hpicfMauType10GigBaseT,
       "hpicfMauType10GigBaseTSH": hpicfMauType10GigBaseTSH,
       "hpicfMauType10GigBaseTLH": hpicfMauType10GigBaseTLH,
       "hpicfMauType10GigBaseSTK": hpicfMauType10GigBaseSTK,
       "hpicfMauType1000CWDM1470": hpicfMauType1000CWDM1470,
       "hpicfMauType1000CWDM1490": hpicfMauType1000CWDM1490,
       "hpicfMauType1000CWDM1510": hpicfMauType1000CWDM1510,
       "hpicfMauType1000CWDM1530": hpicfMauType1000CWDM1530,
       "hpicfMauType1000CWDM1550": hpicfMauType1000CWDM1550,
       "hpicfMauType1000CWDM1570": hpicfMauType1000CWDM1570,
       "hpicfMauType1000CWDM1590": hpicfMauType1000CWDM1590,
       "hpicfMauType1000CWDM1610": hpicfMauType1000CWDM1610,
       "hpicfMauType10GigCWDM1470": hpicfMauType10GigCWDM1470,
       "hpicfMauType10GigCWDM1490": hpicfMauType10GigCWDM1490,
       "hpicfMauType10GigCWDM1510": hpicfMauType10GigCWDM1510,
       "hpicfMauType10GigCWDM1530": hpicfMauType10GigCWDM1530,
       "hpicfMauType10GigCWDM1550": hpicfMauType10GigCWDM1550,
       "hpicfMauType10GigCWDM1570": hpicfMauType10GigCWDM1570,
       "hpicfMauType10GigCWDM1590": hpicfMauType10GigCWDM1590,
       "hpicfMauType10GigCWDM1610": hpicfMauType10GigCWDM1610,
       "hpicfMauType10GigBaseESP": hpicfMauType10GigBaseESP,
       "hpicfMauTypeQSFPpluseSR4": hpicfMauTypeQSFPpluseSR4,
       "hpicfMauTypeQSFPplusGEN": hpicfMauTypeQSFPplusGEN,
       "hpicfMauTypeQSFPplusBIDI": hpicfMauTypeQSFPplusBIDI,
       "hpicfMauType5GigBaseT": hpicfMauType5GigBaseT,
       "hpEtherSwitch": hpEtherSwitch,
       "hpAdvSwitch2000": hpAdvSwitch2000,
       "hpSwitchPortModuleET4": hpSwitchPortModuleET4,
       "hpSwitchPortModuleVG2": hpSwitchPortModuleVG2,
       "hpSwitchPortModule10FL": hpSwitchPortModule10FL,
       "hpSwitchPortModuleFDDI": hpSwitchPortModuleFDDI,
       "hpSwitchPortModuleTX2": hpSwitchPortModuleTX2,
       "hpSwitchPortModuleATM": hpSwitchPortModuleATM,
       "hpAdvSwitch2000B": hpAdvSwitch2000B,
       "hpAdvSwitch800T": hpAdvSwitch800T,
       "hpAdvSwitch200": hpAdvSwitch200,
       "hpAdvSwitch208T": hpAdvSwitch208T,
       "hpAdvSwitch208VG": hpAdvSwitch208VG,
       "hpAdvSwitch224T": hpAdvSwitch224T,
       "hpAdvSwitch224VG": hpAdvSwitch224VG,
       "hpSwitch212M": hpSwitch212M,
       "hpSwitch224M": hpSwitch224M,
       "hpSwitch8000": hpSwitch8000,
       "hpSwitchPortModule100TX8": hpSwitchPortModule100TX8,
       "hpSwitchPortModule100FX4": hpSwitchPortModule100FX4,
       "hpSwitchPortModule10FL4": hpSwitchPortModule10FL4,
       "hpSwitchPortModuleGigSX": hpSwitchPortModuleGigSX,
       "hpSwitchPortModuleGigLX": hpSwitchPortModuleGigLX,
       "hpSwitchPortModuleTwoGig": hpSwitchPortModuleTwoGig,
       "hpSwitchPortModuleGigStk": hpSwitchPortModuleGigStk,
       "hpSwitchPortModuleGigT": hpSwitchPortModuleGigT,
       "hpSwitch1600": hpSwitch1600,
       "hpSwitch4000": hpSwitch4000,
       "hpSwitch2400": hpSwitch2400,
       "hpSwitch2424": hpSwitch2424,
       "hpSwitch9308": hpSwitch9308,
       "hpSwitch9304": hpSwitch9304,
       "hpSwitch6308": hpSwitch6308,
       "hpSwitch6208": hpSwitch6208,
       "hpSwitchJ4819A": hpSwitchJ4819A,
       "hpSwitchPortModuleJ4820A": hpSwitchPortModuleJ4820A,
       "hpSwitchPortModuleJ4821A": hpSwitchPortModuleJ4821A,
       "hpSwitchPortModuleJ4878A": hpSwitchPortModuleJ4878A,
       "hpSwitchModuleJ4852A": hpSwitchModuleJ4852A,
       "hpSwitchModuleJ8161A": hpSwitchModuleJ8161A,
       "hpSwitchModuleJ4907A": hpSwitchModuleJ4907A,
       "hpSwitchModuleJ8162A": hpSwitchModuleJ8162A,
       "hpSwitchPortModuleJ4820B": hpSwitchPortModuleJ4820B,
       "hpSwitchPortModuleJ4821B": hpSwitchPortModuleJ4821B,
       "hpSwitchPortModuleJ4878B": hpSwitchPortModuleJ4878B,
       "hpSwitchModuleJ9001A": hpSwitchModuleJ9001A,
       "hpSwitchModuleJ9003A": hpSwitchModuleJ9003A,
       "hpSwitchModuleJ8988A": hpSwitchModuleJ8988A,
       "hpSwitchJ4812A": hpSwitchJ4812A,
       "hpSwitchModuleJ4812A": hpSwitchModuleJ4812A,
       "hpSwitchJ4813A": hpSwitchJ4813A,
       "hpSwitchModuleJ4813A": hpSwitchModuleJ4813A,
       "hpSwitchJ4850A": hpSwitchJ4850A,
       "hpSwitchJ4815A": hpSwitchJ4815A,
       "hpSwitchJ4851A": hpSwitchJ4851A,
       "hpSwitchJ4865A": hpSwitchJ4865A,
       "hpSwitchModuleJ4862A": hpSwitchModuleJ4862A,
       "hpSwitchModuleJ4863A": hpSwitchModuleJ4863A,
       "hpSwitchModuleJ4864A": hpSwitchModuleJ4864A,
       "hpSwitchModuleJ4862B": hpSwitchModuleJ4862B,
       "hpSwitchModuleJ4893A": hpSwitchModuleJ4893A,
       "hpSwitchModuleJ4892A": hpSwitchModuleJ4892A,
       "hpSwitchModuleJ4908A": hpSwitchModuleJ4908A,
       "hpSwitchA6713A": hpSwitchA6713A,
       "hpSwitchModuleA6713A": hpSwitchModuleA6713A,
       "hpSwitchA6716A": hpSwitchA6716A,
       "hpSwitchModuleA6716A": hpSwitchModuleA6716A,
       "hpSwitchA6717A": hpSwitchA6717A,
       "hpSwitchModuleA6717A": hpSwitchModuleA6717A,
       "hpSwitchJ4887A": hpSwitchJ4887A,
       "hpSwitchJ4874A": hpSwitchJ4874A,
       "hpSwitchJ4899A": hpSwitchJ4899A,
       "hpSwitchModuleJ4899A": hpSwitchModuleJ4899A,
       "hpSwitchJ4902A": hpSwitchJ4902A,
       "hpSwitchModuleJ4902A": hpSwitchModuleJ4902A,
       "hpSwitchJ4903A": hpSwitchJ4903A,
       "hpSwitchModuleJ4903A": hpSwitchModuleJ4903A,
       "hpSwitchModuleJ8434A": hpSwitchModuleJ8434A,
       "hpSwitchModuleJ8435A": hpSwitchModuleJ8435A,
       "hpSwitchJ4904A": hpSwitchJ4904A,
       "hpSwitchModuleJ4904A": hpSwitchModuleJ4904A,
       "hpSwitchProliant": hpSwitchProliant,
       "hpSwitchJ4900A": hpSwitchJ4900A,
       "hpSwitchModuleJ4900A": hpSwitchModuleJ4900A,
       "hpSwitchJ8165A": hpSwitchJ8165A,
       "hpSwitchModuleJ8165A": hpSwitchModuleJ8165A,
       "hpSwitchJ8164A": hpSwitchJ8164A,
       "hpSwitchModuleJ8164A": hpSwitchModuleJ8164A,
       "hpSwitchJ8130A": hpSwitchJ8130A,
       "hpSwitchJ8133A": hpSwitchJ8133A,
       "hpSwitchJ8153A": hpSwitchJ8153A,
       "hpSwitchJ8154A": hpSwitchJ8154A,
       "hpSwitchJ8155A": hpSwitchJ8155A,
       "hpSwitchJ4905A": hpSwitchJ4905A,
       "hpSwitchModuleJ4905A": hpSwitchModuleJ4905A,
       "hpSwitchJ4906A": hpSwitchJ4906A,
       "hpSwitchModuleJ4906A": hpSwitchModuleJ4906A,
       "hpSwitchJ4899B": hpSwitchJ4899B,
       "hpSwitchModuleJ4899B": hpSwitchModuleJ4899B,
       "hpSwitchJ4900B": hpSwitchJ4900B,
       "hpSwitchModuleJ4900B": hpSwitchModuleJ4900B,
       "hpSwitchJ8433A": hpSwitchJ8433A,
       "hpSwitchModuleJ8433A": hpSwitchModuleJ8433A,
       "hpSwitchJ8474A": hpSwitchJ8474A,
       "hpSwitchModuleJ8474A": hpSwitchModuleJ8474A,
       "hpSwitchJ8697A": hpSwitchJ8697A,
       "hpSwitchModuleJ8701A": hpSwitchModuleJ8701A,
       "hpSwitchModuleJ8702A": hpSwitchModuleJ8702A,
       "hpSwitchModuleJ8705A": hpSwitchModuleJ8705A,
       "hpSwitchModuleJ8706A": hpSwitchModuleJ8706A,
       "hpSwitchModuleJ8707A": hpSwitchModuleJ8707A,
       "hpSwitchModuleJ8708A": hpSwitchModuleJ8708A,
       "hpSwitchModuleJ87xxA": hpSwitchModuleJ87xxA,
       "hpSwitchModuleJ87yyA": hpSwitchModuleJ87yyA,
       "hpSwitchModuleJ8694A": hpSwitchModuleJ8694A,
       "hpSwitchModuleJ8726A": hpSwitchModuleJ8726A,
       "hpSwitchModuleJ9051A": hpSwitchModuleJ9051A,
       "hpSwitchModuleJ9052A": hpSwitchModuleJ9052A,
       "hpSwitchModuleJ9154A": hpSwitchModuleJ9154A,
       "hpSwitchModuleJ9155A": hpSwitchModuleJ9155A,
       "hpSwitchModuleJ9446A": hpSwitchModuleJ9446A,
       "hpSwitchModuleJ9307A": hpSwitchModuleJ9307A,
       "hpSwitchModuleJ9308A": hpSwitchModuleJ9308A,
       "hpSwitchModuleJ9478A": hpSwitchModuleJ9478A,
       "hpSwitchModuleJ9309A": hpSwitchModuleJ9309A,
       "hpSwitchModuleJ9312A": hpSwitchModuleJ9312A,
       "hpSwitchModuleJ9534A": hpSwitchModuleJ9534A,
       "hpSwitchModuleJ9535A": hpSwitchModuleJ9535A,
       "hpSwitchModuleJ9536A": hpSwitchModuleJ9536A,
       "hpSwitchModuleJ9537A": hpSwitchModuleJ9537A,
       "hpSwitchModuleJ9538A": hpSwitchModuleJ9538A,
       "hpSwitchModuleJ9546A": hpSwitchModuleJ9546A,
       "hpSwitchModuleJ9547A": hpSwitchModuleJ9547A,
       "hpSwitchModuleJ9548A": hpSwitchModuleJ9548A,
       "hpSwitchModuleJ9549A": hpSwitchModuleJ9549A,
       "hpSwitchModuleJ9550A": hpSwitchModuleJ9550A,
       "hpSwitchAdvServicesModule": hpSwitchAdvServicesModule,
       "hpSwitchExtServicesModule": hpSwitchExtServicesModule,
       "hpSwitchModuleJ9485A": hpSwitchModuleJ9485A,
       "hpSwitchModuleJ9637A": hpSwitchModuleJ9637A,
       "hpSwitchV2ServicesModule": hpSwitchV2ServicesModule,
       "hpSwitchJ8698A": hpSwitchJ8698A,
       "hpSwitchJ8770A": hpSwitchJ8770A,
       "hpSwitchModuleJ8765A": hpSwitchModuleJ8765A,
       "hpSwitchModuleJ8764A": hpSwitchModuleJ8764A,
       "hpSwitchModuleJ8776A": hpSwitchModuleJ8776A,
       "hpSwitchModuleJ8763A": hpSwitchModuleJ8763A,
       "hpSwitchModuleJ8768A": hpSwitchModuleJ8768A,
       "hpSwitchModuleJ9033A": hpSwitchModuleJ9033A,
       "hpSwitchModuleJ8766A": hpSwitchModuleJ8766A,
       "hpSwitchJ8773A": hpSwitchJ8773A,
       "hpSwitchJ8680A": hpSwitchJ8680A,
       "hpSwitchJ8762A": hpSwitchJ8762A,
       "hpSwitchModuleJ8762A": hpSwitchModuleJ8762A,
       "hpSwitchJ8771A": hpSwitchJ8771A,
       "hpSwitchJ8772A": hpSwitchJ8772A,
       "hpSwitchJ8692A": hpSwitchJ8692A,
       "hpSwitchJ8693A": hpSwitchJ8693A,
       "hpSwitchJ8992A": hpSwitchJ8992A,
       "hpSwitchJ9019A": hpSwitchJ9019A,
       "hpSwitchModuleJ9019A": hpSwitchModuleJ9019A,
       "hpSwitchJ9020A": hpSwitchJ9020A,
       "hpSwitchModuleJ9020A": hpSwitchModuleJ9020A,
       "hpSwitchJ9021A": hpSwitchJ9021A,
       "hpSwitchModuleJ9021A": hpSwitchModuleJ9021A,
       "hpSwitchJ9022A": hpSwitchJ9022A,
       "hpSwitchModuleJ9022A": hpSwitchModuleJ9022A,
       "hpSwitchJ9028A": hpSwitchJ9028A,
       "hpSwitchJ9029A": hpSwitchJ9029A,
       "hpSwitchJ9038A": hpSwitchJ9038A,
       "hpSwitchJ9050A": hpSwitchJ9050A,
       "hpSwitchModuleJ90xxA": hpSwitchModuleJ90xxA,
       "hpSwitchModuleJ90yyA": hpSwitchModuleJ90yyA,
       "hpSwitchModuleJ90zzA": hpSwitchModuleJ90zzA,
       "hpSwitchJ9049A": hpSwitchJ9049A,
       "hpSwitchJ9091A": hpSwitchJ9091A,
       "hpManagementModuleJ9092A": hpManagementModuleJ9092A,
       "hpFabricModuleJ9093A": hpFabricModuleJ9093A,
       "hpSSMModuleJ8784A": hpSSMModuleJ8784A,
       "hpSwitchJ9065A": hpSwitchJ9065A,
       "hpSwitchJ9079A": hpSwitchJ9079A,
       "hpSwitchJ9080A": hpSwitchJ9080A,
       "hpSwitchJ9085A": hpSwitchJ9085A,
       "hpSwitchModuleJ9085A": hpSwitchModuleJ9085A,
       "hpSwitchJ9088A": hpSwitchJ9088A,
       "hpSwitchModuleJ9088A": hpSwitchModuleJ9088A,
       "hpSwitchJ9087A": hpSwitchJ9087A,
       "hpSwitchModuleJ9087A": hpSwitchModuleJ9087A,
       "hpSwitchJ9089A": hpSwitchJ9089A,
       "hpSwitchModuleJ9089A": hpSwitchModuleJ9089A,
       "hpSwitchJ9086A": hpSwitchJ9086A,
       "hpSwitchModuleJ9086A": hpSwitchModuleJ9086A,
       "hpSwitchJ9028B": hpSwitchJ9028B,
       "hpSwitchJ4900C": hpSwitchJ4900C,
       "hpSwitchModuleJ4900C": hpSwitchModuleJ4900C,
       "hpSwitchJ4899C": hpSwitchJ4899C,
       "hpSwitchModuleJ4899C": hpSwitchModuleJ4899C,
       "hpSwitchJ9146A": hpSwitchJ9146A,
       "hpSwitchModuleJ9146A": hpSwitchModuleJ9146A,
       "hpSwitchModuleJ9149A": hpSwitchModuleJ9149A,
       "hpSwitchModuleJ9008A": hpSwitchModuleJ9008A,
       "hpSwitchModuleJ9165A": hpSwitchModuleJ9165A,
       "hpSwitchJ9148A": hpSwitchJ9148A,
       "hpSwitchModuleJ9148A": hpSwitchModuleJ9148A,
       "hpSwitchJ9145A": hpSwitchJ9145A,
       "hpSwitchModuleJ9145A": hpSwitchModuleJ9145A,
       "hpSwitchJ9147A": hpSwitchJ9147A,
       "hpSwitchModuleJ9147A": hpSwitchModuleJ9147A,
       "hpSwitchJ9279A": hpSwitchJ9279A,
       "hpSwitchModuleJ9279A": hpSwitchModuleJ9279A,
       "hpSwitchJ9280A": hpSwitchJ9280A,
       "hpSwitchModuleJ9280A": hpSwitchModuleJ9280A,
       "hpSwitchJ9019B": hpSwitchJ9019B,
       "hpSwitchJ9137A": hpSwitchJ9137A,
       "hpSwitchModuleJ9137A": hpSwitchModuleJ9137A,
       "hpSwitchJ9138A": hpSwitchJ9138A,
       "hpSwitchModuleJ9138A": hpSwitchModuleJ9138A,
       "hpSwitchJ9298A": hpSwitchJ9298A,
       "hpSwitchModuleJ9298A": hpSwitchModuleJ9298A,
       "hpSwitchJ9299A": hpSwitchJ9299A,
       "hpSwitchModuleJ9299A": hpSwitchModuleJ9299A,
       "hpSwitchJ9265A": hpSwitchJ9265A,
       "hpSwitchModuleJ92yyA": hpSwitchModuleJ92yyA,
       "hpSwitchModuleJ92xxA": hpSwitchModuleJ92xxA,
       "hpSwitchModuleJ92wwA": hpSwitchModuleJ92wwA,
       "hpSwitchModuleJ92vvA": hpSwitchModuleJ92vvA,
       "hpSwitchModuleJ92uuA": hpSwitchModuleJ92uuA,
       "hpSwitchModuleJ92ttA": hpSwitchModuleJ92ttA,
       "hpEtherSwitchPortType": hpEtherSwitchPortType,
       "hpEtherSwitchPort10T": hpEtherSwitchPort10T,
       "hpEtherSwitchPort100T": hpEtherSwitchPort100T,
       "hpEtherSwitchPort100VG": hpEtherSwitchPort100VG,
       "hpEtherSwitchPort100F": hpEtherSwitchPort100F,
       "hpSwitchJ9263A": hpSwitchJ9263A,
       "hpSwitchJ9264A": hpSwitchJ9264A,
       "hpSwitchJ9445A": hpSwitchJ9445A,
       "hpSwitchJ9449A": hpSwitchJ9449A,
       "hpSwitchJ9450A": hpSwitchJ9450A,
       "hpSwitchJ9452A": hpSwitchJ9452A,
       "hpSwitchJ9451A": hpSwitchJ9451A,
       "hpSwitch516733-B21": hpSwitch516733_B21,
       "hpSwitch498358-B21": hpSwitch498358_B21,
       "hpSwitchJ9471A": hpSwitchJ9471A,
       "hpSwitchJ9473A": hpSwitchJ9473A,
       "hpSwitchModuleJ94yxA": hpSwitchModuleJ94yxA,
       "hpSwitchModuleJ94yyA": hpSwitchModuleJ94yyA,
       "hpSwitchJ9470A": hpSwitchJ9470A,
       "hpSwitchJ9472A": hpSwitchJ9472A,
       "hpSwitchModuleJ94xxA": hpSwitchModuleJ94xxA,
       "hpSwitchModuleJ94xyA": hpSwitchModuleJ94xyA,
       "hpSwitchJ9477A": hpSwitchJ9477A,
       "hpSwitchJ9310A": hpSwitchJ9310A,
       "hpSwitchJ9311A": hpSwitchJ9311A,
       "hpSwitchModuleJ93aaA": hpSwitchModuleJ93aaA,
       "hpSwitchModuleJ93bbA": hpSwitchModuleJ93bbA,
       "hpSwitchJ9565A": hpSwitchJ9565A,
       "hpSwitchModuleJ9565A": hpSwitchModuleJ9565A,
       "hpSwitchJ9562A": hpSwitchJ9562A,
       "hpSwitchModuleJ9562A": hpSwitchModuleJ9562A,
       "hpSwitchJ9573": hpSwitchJ9573,
       "hpSwitchModuleJ9573": hpSwitchModuleJ9573,
       "hpSwitchJ9574": hpSwitchJ9574,
       "hpSwitchModuleJ9574x": hpSwitchModuleJ9574x,
       "hpSwitchModuleJ9574y": hpSwitchModuleJ9574y,
       "hpSwitchJ9575": hpSwitchJ9575,
       "hpSwitchModuleJ9575": hpSwitchModuleJ9575,
       "hpSwitchJ9576": hpSwitchJ9576,
       "hpSwitchModuleJ9576x": hpSwitchModuleJ9576x,
       "hpSwitchModuleJ9576y": hpSwitchModuleJ9576y,
       "hpSwitchJ9584": hpSwitchJ9584,
       "hpSwitchModuleJ9584": hpSwitchModuleJ9584,
       "hpSwitchJ9585": hpSwitchJ9585,
       "hpSwitchModuleJ9585": hpSwitchModuleJ9585,
       "hpSwitchJ9586": hpSwitchJ9586,
       "hpSwitchModuleJ9586x": hpSwitchModuleJ9586x,
       "hpSwitchModuleJ9586y": hpSwitchModuleJ9586y,
       "hpSwitchJ9587": hpSwitchJ9587,
       "hpSwitchModuleJ9587": hpSwitchModuleJ9587,
       "hpSwitchJ9588": hpSwitchJ9588,
       "hpSwitchModuleJ9588x": hpSwitchModuleJ9588x,
       "hpSwitchModuleJ9588y": hpSwitchModuleJ9588y,
       "hpSwitchJ9577": hpSwitchJ9577,
       "hpSwitchModuleJ9577A": hpSwitchModuleJ9577A,
       "hpSwitchJ9623A": hpSwitchJ9623A,
       "hpSwitchModuleJ9623A": hpSwitchModuleJ9623A,
       "hpSwitchJ9624A": hpSwitchJ9624A,
       "hpSwitchModuleJ9624A": hpSwitchModuleJ9624A,
       "hpSwitchJ9625A": hpSwitchJ9625A,
       "hpSwitchModuleJ9625A": hpSwitchModuleJ9625A,
       "hpSwitchJ9626A": hpSwitchJ9626A,
       "hpSwitchModuleJ9626A": hpSwitchModuleJ9626A,
       "hpSwitchJ9627A": hpSwitchJ9627A,
       "hpSwitchModuleJ9627A": hpSwitchModuleJ9627A,
       "hpSwitchJ9660A": hpSwitchJ9660A,
       "hpSwitchJ9772A": hpSwitchJ9772A,
       "hpSwitchModuleJ9772A": hpSwitchModuleJ9772A,
       "hpSwitchJ9773A": hpSwitchJ9773A,
       "hpSwitchModuleJ9773A": hpSwitchModuleJ9773A,
       "hpSwitchJ9774A": hpSwitchJ9774A,
       "hpSwitchModuleJ9774A": hpSwitchModuleJ9774A,
       "hpSwitchJ9775A": hpSwitchJ9775A,
       "hpSwitchModuleJ9775A": hpSwitchModuleJ9775A,
       "hpSwitchJ9776A": hpSwitchJ9776A,
       "hpSwitchModuleJ9776A": hpSwitchModuleJ9776A,
       "hpSwitchJ9777A": hpSwitchJ9777A,
       "hpSwitchModuleJ9777A": hpSwitchModuleJ9777A,
       "hpSwitchJ9778A": hpSwitchJ9778A,
       "hpSwitchModuleJ9778A": hpSwitchModuleJ9778A,
       "hpSwitchJ9779A": hpSwitchJ9779A,
       "hpSwitchModuleJ9779A": hpSwitchModuleJ9779A,
       "hpSwitchJ9780A": hpSwitchJ9780A,
       "hpSwitchModuleJ9780A": hpSwitchModuleJ9780A,
       "hpSwitchJ9781A": hpSwitchJ9781A,
       "hpSwitchModuleJ9781A": hpSwitchModuleJ9781A,
       "hpSwitchJ9782A": hpSwitchJ9782A,
       "hpSwitchModuleJ9782A": hpSwitchModuleJ9782A,
       "hpSwitchJ9783A": hpSwitchJ9783A,
       "hpSwitchModuleJ9783A": hpSwitchModuleJ9783A,
       "hpSwitchJ9800A": hpSwitchJ9800A,
       "hpSwitchJ9801A": hpSwitchJ9801A,
       "hpSwitchJ9802A": hpSwitchJ9802A,
       "hpSwitchJ9803A": hpSwitchJ9803A,
       "hpSwitchJ9726A": hpSwitchJ9726A,
       "hpSwitchModuleJ9726A": hpSwitchModuleJ9726A,
       "hpSwitchJ9727A": hpSwitchJ9727A,
       "hpSwitchModuleJ9727A": hpSwitchModuleJ9727A,
       "hpSwitchJ9728A": hpSwitchJ9728A,
       "hpSwitchModuleJ9728A": hpSwitchModuleJ9728A,
       "hpSwitchJ9729A": hpSwitchJ9729A,
       "hpSwitchModuleJ9729A": hpSwitchModuleJ9729A,
       "hpSwitchModuleJ9730A": hpSwitchModuleJ9730A,
       "hpSwitchModuleJ9731A": hpSwitchModuleJ9731A,
       "hpSwitchModuleJ9732A": hpSwitchModuleJ9732A,
       "hpSwitchModuleJ9733A": hpSwitchModuleJ9733A,
       "hpSwitchJ9833A": hpSwitchJ9833A,
       "hpSwitchJ9834A": hpSwitchJ9834A,
       "hpSwitchJ9850A": hpSwitchJ9850A,
       "hpSwitchModuleJ9827A": hpSwitchModuleJ9827A,
       "hpSwitchModuleJ9986A": hpSwitchModuleJ9986A,
       "hpSwitchModuleJ9987A": hpSwitchModuleJ9987A,
       "hpSwitchModuleJ9988A": hpSwitchModuleJ9988A,
       "hpSwitchModuleJ9989A": hpSwitchModuleJ9989A,
       "hpSwitchModuleJ9990A": hpSwitchModuleJ9990A,
       "hpSwitchModuleJ9991A": hpSwitchModuleJ9991A,
       "hpSwitchModuleJ9992A": hpSwitchModuleJ9992A,
       "hpSwitchModuleJ9993A": hpSwitchModuleJ9993A,
       "hpSwitchModuleJ9995A": hpSwitchModuleJ9995A,
       "hpSwitchModuleJ9996A": hpSwitchModuleJ9996A,
       "hpSwitchJ9851A": hpSwitchJ9851A,
       "hpSwitchJ9853A": hpSwitchJ9853A,
       "hpSwitchModuleJ9853A": hpSwitchModuleJ9853A,
       "hpSwitchJ9854A": hpSwitchJ9854A,
       "hpSwitchModuleJ9854A": hpSwitchModuleJ9854A,
       "hpSwitchJ9855A": hpSwitchJ9855A,
       "hpSwitchModuleJ9855A": hpSwitchModuleJ9855A,
       "hpSwitchJ9856A": hpSwitchJ9856A,
       "hpSwitchModuleJ9856A": hpSwitchModuleJ9856A,
       "hpSwitchJ9979A": hpSwitchJ9979A,
       "hpSwitchJ9980A": hpSwitchJ9980A,
       "hpSwitchJ9981A": hpSwitchJ9981A,
       "hpSwitchJ9982A": hpSwitchJ9982A,
       "hpSwitchJ9983A": hpSwitchJ9983A,
       "hpSwitchJ9984A": hpSwitchJ9984A,
       "hpSwitchJL070A": hpSwitchJL070A,
       "hpSwitchModuleJL070A": hpSwitchModuleJL070A,
       "aruba3810": aruba3810,
       "arubaJL071A": arubaJL071A,
       "arubaJL071AModule": arubaJL071AModule,
       "arubaJL072A": arubaJL072A,
       "arubaJL072AModule": arubaJL072AModule,
       "arubaJL073A": arubaJL073A,
       "arubaJL073AModule": arubaJL073AModule,
       "arubaJL074A": arubaJL074A,
       "arubaJL074AModule": arubaJL074AModule,
       "arubaJL075A": arubaJL075A,
       "arubaJL075AModule": arubaJL075AModule,
       "arubaJL076A": arubaJL076A,
       "arubaJL076AModule": arubaJL076AModule,
       "arubaJL077A": arubaJL077A,
       "arubaJL077AModule": arubaJL077AModule,
       "arubaJL084AStackingModule": arubaJL084AStackingModule,
       "arubaJL088AFanTray": arubaJL088AFanTray,
       "arubaFPModule": arubaFPModule,
       "arubaFPModuleJL078A": arubaFPModuleJL078A,
       "arubaFPModuleJL079A": arubaFPModuleJL079A,
       "arubaFPModuleJL080A": arubaFPModuleJL080A,
       "arubaFPModuleJL081A": arubaFPModuleJL081A,
       "arubaFPModuleJL082A": arubaFPModuleJL082A,
       "arubaFPModuleJL083A": arubaFPModuleJL083A,
       "arubaSwitch2930": arubaSwitch2930,
       "arubaStackingModuleJL325A": arubaStackingModuleJL325A,
       "arubaSwitchJL319A": arubaSwitchJL319A,
       "arubaModuleJL319A": arubaModuleJL319A,
       "arubaSwitchJL321A": arubaSwitchJL321A,
       "arubaModuleJL321A": arubaModuleJL321A,
       "arubaSwitchJL320A": arubaSwitchJL320A,
       "arubaModuleJL320A": arubaModuleJL320A,
       "arubaSwitchJL322A": arubaSwitchJL322A,
       "arubaModuleJL322A": arubaModuleJL322A,
       "arubaSwitchJL324A": arubaSwitchJL324A,
       "arubaModuleJL324A": arubaModuleJL324A,
       "arubaSwitchJL323A": arubaSwitchJL323A,
       "arubaModuleJL323A": arubaModuleJL323A,
       "arubaSwitchJL258A": arubaSwitchJL258A,
       "arubaModuleJL258A": arubaModuleJL258A,
       "arubaSwitchJL253A": arubaSwitchJL253A,
       "arubaModuleJL253A": arubaModuleJL253A,
       "arubaSwitchJL254A": arubaSwitchJL254A,
       "arubaModuleJL254A": arubaModuleJL254A,
       "arubaSwitchJL255A": arubaSwitchJL255A,
       "arubaModuleJL255A": arubaModuleJL255A,
       "arubaSwitchJL256A": arubaSwitchJL256A,
       "arubaModuleJL256A": arubaModuleJL256A,
       "arubaSwitchJL259A": arubaSwitchJL259A,
       "arubaModuleJL259A": arubaModuleJL259A,
       "arubaSwitchJL260A": arubaSwitchJL260A,
       "arubaModuleJL260A": arubaModuleJL260A,
       "arubaSwitchJL261A": arubaSwitchJL261A,
       "arubaModuleJL261A": arubaModuleJL261A,
       "arubaSwitchJL262A": arubaSwitchJL262A,
       "arubaModuleJL262A": arubaModuleJL262A,
       "arubaSwitchJL558A": arubaSwitchJL558A,
       "arubaModuleJL558A": arubaModuleJL558A,
       "arubaSwitchJL557A": arubaSwitchJL557A,
       "arubaModuleJL557A": arubaModuleJL557A,
       "arubaSwitchJL263A": arubaSwitchJL263A,
       "arubaModuleJL263A": arubaModuleJL263A,
       "arubaSwitchJL264A": arubaSwitchJL264A,
       "arubaModuleJL264A": arubaModuleJL264A,
       "arubaSwitchJL559A": arubaSwitchJL559A,
       "arubaModuleJL559A": arubaModuleJL559A,
       "arubaSwitch2540": arubaSwitch2540,
       "arubaSwitchJL354A": arubaSwitchJL354A,
       "arubaModuleJL354A": arubaModuleJL354A,
       "arubaSwitchJL355A": arubaSwitchJL355A,
       "arubaModuleJL355A": arubaModuleJL355A,
       "arubaSwitchJL356A": arubaSwitchJL356A,
       "arubaModuleJL356A": arubaModuleJL356A,
       "arubaSwitchJL357A": arubaSwitchJL357A,
       "arubaModuleJL357A": arubaModuleJL357A,
       "icf": icf,
       "icfCommon": icfCommon,
       "icfHub": icfHub,
       "icfBridge": icfBridge,
       "icfSecurity": icfSecurity,
       "icfConfig": icfConfig,
       "icfEsSwitch": icfEsSwitch,
       "hpEs": hpEs,
       "hpEs2": hpEs2,
       "hpNetSwitch": hpNetSwitch,
       "icfRouter": icfRouter,
       "icfDot12Draft": icfDot12Draft,
       "icfVgRepeater": icfVgRepeater,
       "icfVgInterface": icfVgInterface,
       "hpEntityMIB": hpEntityMIB,
       "hpicfAdmin": hpicfAdmin,
       "hpicfDomains": hpicfDomains,
       "hpicfLLCDomain": hpicfLLCDomain,
       "hpicfObjectModules": hpicfObjectModules,
       "icfSecurityMib": icfSecurityMib,
       "hpicfChainMib": hpicfChainMib,
       "hpicfChassisMib": hpicfChassisMib,
       "hpicfDownloadMib": hpicfDownloadMib,
       "hpicfBasicMib": hpicfBasicMib,
       "hpicfStackMib": hpicfStackMib,
       "hpicfLinkTestMib": hpicfLinkTestMib,
       "hpicfGenRptrMib": hpicfGenRptrMib,
       "hpicf8023RptrMib": hpicf8023RptrMib,
       "icfVgRepeaterMib": icfVgRepeaterMib,
       "hpicfVgRptrMib": hpicfVgRptrMib,
       "hpicfFaultFinderMib": hpicfFaultFinderMib,
       "hpicfJumboMIB": hpicfJumboMIB,
       "hpicfRateLimitMIB": hpicfRateLimitMIB,
       "hpicfAgentModules": hpicfAgentModules,
       "hpicfETwistHubAgentsMib": hpicfETwistHubAgentsMib,
       "hpicfETwistBridgeAgentsMib": hpicfETwistBridgeAgentsMib,
       "hpicfAdvStk8023AgentsMib": hpicfAdvStk8023AgentsMib,
       "hpicfAdvStkVGAgentsMib": hpicfAdvStkVGAgentsMib,
       "hpicfTextualConventions": hpicfTextualConventions,
       "hpicfObjects": hpicfObjects,
       "hpicfCommon": hpicfCommon,
       "hpicfChain": hpicfChain,
       "hpicfChassis": hpicfChassis,
       "hpicfDownload": hpicfDownload,
       "hpicfBasic": hpicfBasic,
       "hpicfStack": hpicfStack,
       "hpicfLinktest": hpicfLinktest,
       "hpicfFaultFinder": hpicfFaultFinder,
       "hpicfPOE": hpicfPOE,
       "hpicfCommonSecurity": hpicfCommonSecurity,
       "hpicfSrcIpMIB": hpicfSrcIpMIB,
       "hpicfCoreDumpMIB": hpicfCoreDumpMIB,
       "hpicfRepeater": hpicfRepeater,
       "hpicfVg": hpicfVg,
       "hpicfGenericRepeater": hpicfGenericRepeater,
       "hpicfSwitch": hpicfSwitch,
       "hpSwitch": hpSwitch,
       "hpOpSystem": hpOpSystem,
       "hpHwSystem": hpHwSystem,
       "hpVLAN": hpVLAN,
       "hpConfig": hpConfig,
       "hpSwitchStatistics": hpSwitchStatistics,
       "hpSwitchVirtualStackMib": hpSwitchVirtualStackMib,
       "hpicfDhcpRelay": hpicfDhcpRelay,
       "hpicfBridge": hpicfBridge,
       "hpicfRip": hpicfRip,
       "hpicfOspf": hpicfOspf,
       "hpicfIpRouting": hpicfIpRouting,
       "hpSwitchAuthenticationMIB": hpSwitchAuthenticationMIB,
       "hpSwitchAccountingMIB": hpSwitchAccountingMIB,
       "hpicfXrrpMIB": hpicfXrrpMIB,
       "hpicfUsrAuthMIB": hpicfUsrAuthMIB,
       "hpicfPimMIB": hpicfPimMIB,
       "hpicfUdpFwd": hpicfUdpFwd,
       "hpicfConnectionRateFilter": hpicfConnectionRateFilter,
       "hpicfDot1xMIB": hpicfDot1xMIB,
       "hpicfVrrpMIB": hpicfVrrpMIB,
       "hpSwitchAuthorizationMIB": hpSwitchAuthorizationMIB,
       "hpicfUdldMIB": hpicfUdldMIB,
       "hpicfIpDhcpSnoop": hpicfIpDhcpSnoop,
       "hpicfInstMonMIB": hpicfInstMonMIB,
       "hpicfL3MacConfigMIB": hpicfL3MacConfigMIB,
       "hpicfArpProtect": hpicfArpProtect,
       "hpicfSnmpMIB": hpicfSnmpMIB,
       "hpicfIpLockdown": hpicfIpLockdown,
       "hpicfProviderBridge": hpicfProviderBridge,
       "hpicfGppcMIB": hpicfGppcMIB,
       "hpicfAutorun": hpicfAutorun,
       "hpicfInstMIB": hpicfInstMIB,
       "hpicfFtrCo": hpicfFtrCo,
       "hpicfMldMIB": hpicfMldMIB,
       "hpicfDhcpv6Relay": hpicfDhcpv6Relay,
       "hpicfScriptMIB": hpicfScriptMIB,
       "hpicfUSBPortMIB": hpicfUSBPortMIB,
       "hpicfFanMIB": hpicfFanMIB,
       "hpicfPsMIB": hpicfPsMIB,
       "hpicfSavepowerMIB": hpicfSavepowerMIB,
       "hpicfDhcpClient": hpicfDhcpClient,
       "hpicfOobmMIB": hpicfOobmMIB,
       "hpSwitchImage": hpSwitchImage,
       "hpicfDosFilterMib": hpicfDosFilterMib,
       "hpicfGppcv2MIB": hpicfGppcv2MIB,
       "hpicfDebugLog": hpicfDebugLog,
       "hpicfMacNotifyMIB": hpicfMacNotifyMIB,
       "hpicfGenericVlanMIB": hpicfGenericVlanMIB,
       "hpSwitchErrorMsgMIB": hpSwitchErrorMsgMIB,
       "hpStackMIB": hpStackMIB,
       "hpicfLayer3VlanConfigMIB": hpicfLayer3VlanConfigMIB,
       "hpEntityPowerMIB": hpEntityPowerMIB,
       "hpicfTrafficTemplateMIB": hpicfTrafficTemplateMIB,
       "hpicfDcbxMIB": hpicfDcbxMIB,
       "hpicfUfdMIB": hpicfUfdMIB,
       "hpSBMMIB": hpSBMMIB,
       "hpicfLoadBalanceMod": hpicfLoadBalanceMod,
       "hpTunnelMIB": hpTunnelMIB,
       "hpicfTcpMib": hpicfTcpMib,
       "hpicfTransceiverMIB": hpicfTransceiverMIB,
       "hpicfSvcsAppMIB": hpicfSvcsAppMIB,
       "hpicfIpv6RAGuard": hpicfIpv6RAGuard,
       "hpicfRpvstMIB": hpicfRpvstMIB,
       "hpicfOpenFlowMIB": hpicfOpenFlowMIB,
       "hpicfVrrpv3MIB": hpicfVrrpv3MIB,
       "hpicfSflowMIB": hpicfSflowMIB,
       "hpicfMstpExtnMIB": hpicfMstpExtnMIB,
       "hpicfMadMIB": hpicfMadMIB,
       "hpicfSmartLinkMIB": hpicfSmartLinkMIB,
       "hpicfTR069MIB": hpicfTR069MIB,
       "hpicfDhcpv4ServerMIB": hpicfDhcpv4ServerMIB,
       "hpicfServiceTunnel": hpicfServiceTunnel,
       "hpicfDSnoopV6": hpicfDSnoopV6,
       "hpicfIpv6Lockdown": hpicfIpv6Lockdown,
       "hpSwitchTrapMIB": hpSwitchTrapMIB,
       "hpicfJobSchedulerMIB": hpicfJobSchedulerMIB,
       "hpicfByodMIB": hpicfByodMIB,
       "hpicfVirtualNetwork": hpicfVirtualNetwork,
       "hpicfDldpMIB": hpicfDldpMIB,
       "hpicfDot1qIsolatedPorts": hpicfDot1qIsolatedPorts,
       "hpicfTlsMinMIB": hpicfTlsMinMIB,
       "hpicfRipng": hpicfRipng,
       "hpicfPrivateVlan": hpicfPrivateVlan,
       "hpicfVsfVCMIB": hpicfVsfVCMIB,
       "hpicfMvrpMIB": hpicfMvrpMIB,
       "hpicfArpThrottle": hpicfArpThrottle,
       "hpicfBfd": hpicfBfd,
       "hpicfNtpMIB": hpicfNtpMIB,
       "hpicfPim6MIB": hpicfPim6MIB,
       "hpicfMdns": hpicfMdns,
       "hpicfAMPServerMIB": hpicfAMPServerMIB,
       "hpicfDevConf": hpicfDevConf,
       "hpicfIpSla": hpicfIpSla,
       "hpicfTunneledNode": hpicfTunneledNode,
       "hpicfActivateMIB": hpicfActivateMIB,
       "hpicfMcastMIB": hpicfMcastMIB,
       "hpicfUrpfMIB": hpicfUrpfMIB,
       "hpicfMinKeyMIB": hpicfMinKeyMIB,
       "hpicfDeviceIdentityMIB": hpicfDeviceIdentityMIB,
       "hpicfConfig": hpicfConfig,
       "hpSwitchExperimental": hpSwitchExperimental,
       "hpicfSaviMIB": hpicfSaviMIB,
       "hpicfAccess": hpicfAccess,
       "hpicfWAN": hpicfWAN,
       "hpWANRouters": hpWANRouters,
       "hpSRJ8751A": hpSRJ8751A,
       "hpSRJ8752A": hpSRJ8752A,
       "hpSRJ8753A": hpSRJ8753A,
       "hpSRJ8754A": hpSRJ8754A,
       "hpSRPowerSupply8756A": hpSRPowerSupply8756A,
       "hpWANModules": hpWANModules,
       "hpSRmoduleJ8451A": hpSRmoduleJ8451A,
       "hpSRmoduleJ8452A": hpSRmoduleJ8452A,
       "hpSRmoduleJ8453A": hpSRmoduleJ8453A,
       "hpSRmoduleJ8454A": hpSRmoduleJ8454A,
       "hpSRmoduleJ8455A": hpSRmoduleJ8455A,
       "hpSRmoduleJ8456A": hpSRmoduleJ8456A,
       "hpSRmoduleJ8457A": hpSRmoduleJ8457A,
       "hpSRmoduleJ8458A": hpSRmoduleJ8458A,
       "hpSRmoduleJ8459A": hpSRmoduleJ8459A,
       "hpSRmoduleJ8759A": hpSRmoduleJ8759A,
       "hpSRmoduleJ8460A": hpSRmoduleJ8460A,
       "hpSRmoduleJ8461A": hpSRmoduleJ8461A,
       "hpSRmoduleJ8462A": hpSRmoduleJ8462A,
       "hpSRmoduleJ8463A": hpSRmoduleJ8463A,
       "hpSRmoduleJ8464A": hpSRmoduleJ8464A,
       "hpSRmoduleJ8465A": hpSRmoduleJ8465A,
       "hpSRmoduleJ8471A": hpSRmoduleJ8471A,
       "hpSRmoduleJ8472A": hpSRmoduleJ8472A,
       "hpicfFabric": hpicfFabric,
       "hpicfSecurityDevice": hpicfSecurityDevice,
       "hpicfSysMgmt": hpicfSysMgmt,
       "hpicfNotifications": hpicfNotifications,
       "hpicfCommonTraps": hpicfCommonTraps,
       "hpicfCommonTrapsPrefix": hpicfCommonTrapsPrefix,
       "hpicf8023RptrTraps": hpicf8023RptrTraps,
       "hpicf8023RptrTrapsPrefix": hpicf8023RptrTrapsPrefix,
       "hpicfVgRptrTraps": hpicfVgRptrTraps,
       "hpicfVgRptrTrapsPrefix": hpicfVgRptrTrapsPrefix,
       "hpicfGenRptrTraps": hpicfGenRptrTraps,
       "hpicfGenRptrTrapsPrefix": hpicfGenRptrTrapsPrefix,
       "hpicfRateLimitTraps": hpicfRateLimitTraps,
       "hpicfRateLimitTrapsPrefix": hpicfRateLimitTrapsPrefix,
       "hpicfSecLoggingTraps": hpicfSecLoggingTraps,
       "hpicfSecLoggingTrapsPrefix": hpicfSecLoggingTrapsPrefix,
       "hpicfOEMs": hpicfOEMs,
       "hpicfFEHub": hpicfFEHub,
       "hpicfSyslog": hpicfSyslog}
)
