# SNMP MIB module (S5-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-REG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:08 2024
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

(s5reg,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5reg")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

s5RegMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 4)
)
s5RegMib.setRevisions(
        ("2015-05-05 00:00",
         "2014-07-29 00:00",
         "2014-03-21 00:00",
         "2014-02-13 00:00",
         "2013-08-26 00:00",
         "2013-01-24 00:00",
         "2011-10-10 00:00",
         "2011-07-29 00:00",
         "2011-06-29 00:00",
         "2011-04-28 00:00",
         "2011-03-08 00:00",
         "2011-01-25 00:00",
         "2010-08-27 00:00",
         "2009-10-13 00:00",
         "2009-06-09 00:00",
         "2009-05-28 00:00",
         "2009-04-15 00:00",
         "2009-03-30 00:00",
         "2008-12-16 00:00",
         "2008-11-21 00:00",
         "2008-10-29 00:00",
         "2008-10-14 00:00",
         "2008-05-22 00:00",
         "2007-11-21 00:00",
         "2007-10-16 00:00",
         "2007-06-04 00:00",
         "2007-05-08 00:00",
         "2007-02-22 00:00",
         "2006-09-12 00:00",
         "2006-09-01 00:00",
         "2006-07-06 00:00",
         "2006-05-25 00:00",
         "2006-04-12 00:00",
         "2006-04-06 00:00",
         "2005-11-04 00:00",
         "2005-04-25 00:00",
         "2004-10-19 00:00",
         "2004-10-13 00:00",
         "2004-10-12 00:00",
         "2004-08-31 00:02",
         "2004-08-31 00:01",
         "2004-08-31 00:00",
         "2004-07-20 00:00",
         "2003-05-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5ChasTypeVal_ObjectIdentity = ObjectIdentity
s5ChasTypeVal = _S5ChasTypeVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1)
)
_S5ChasTypeUnknown_ObjectIdentity = ObjectIdentity
s5ChasTypeUnknown = _S5ChasTypeUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 1)
)
_S5ChasTypeM3000Orig_ObjectIdentity = ObjectIdentity
s5ChasTypeM3000Orig = _S5ChasTypeM3000Orig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 2)
)
_S5ChasTypeM3030_ObjectIdentity = ObjectIdentity
s5ChasTypeM3030 = _S5ChasTypeM3030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 3)
)
_S5ChasTypeM5000_ObjectIdentity = ObjectIdentity
s5ChasTypeM5000 = _S5ChasTypeM5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 12)
)
_S5ChasTypeM1032x_ObjectIdentity = ObjectIdentity
s5ChasTypeM1032x = _S5ChasTypeM1032x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 16)
)
_S5ChasTypeM5005_ObjectIdentity = ObjectIdentity
s5ChasTypeM5005 = _S5ChasTypeM5005_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 17)
)
_S5ChasType5DN000_ObjectIdentity = ObjectIdentity
s5ChasType5DN000 = _S5ChasType5DN000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 24)
)
_S5ChasType5DN002Unit_1U2_ObjectIdentity = ObjectIdentity
s5ChasType5DN002Unit_1U2 = _S5ChasType5DN002Unit_1U2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 24, 1)
)
_S5ChasType5DN003Unit_2U3_ObjectIdentity = ObjectIdentity
s5ChasType5DN003Unit_2U3 = _S5ChasType5DN003Unit_2U3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 24, 2)
)
_S5ChasType5DN001_08Unit_2U0_ObjectIdentity = ObjectIdentity
s5ChasType5DN001_08Unit_2U0 = _S5ChasType5DN001_08Unit_2U0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 24, 3)
)
_S5ChasTypeNBayStack_ObjectIdentity = ObjectIdentity
s5ChasTypeNBayStack = _S5ChasTypeNBayStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 25)
)
_S5ChasTypeNBayStackUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeNBayStackUnit_12Port = _S5ChasTypeNBayStackUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 25, 1)
)
_S5ChasTypeNBayStackUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeNBayStackUnit_24Port = _S5ChasTypeNBayStackUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 25, 2)
)
_S5ChasTypeBayStack100Hub_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack100Hub = _S5ChasTypeBayStack100Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 27)
)
_S5ChasTypeBayStack100Unit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack100Unit_12Port = _S5ChasTypeBayStack100Unit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 27, 1)
)
_S5ChasTypeM3000_ObjectIdentity = ObjectIdentity
s5ChasTypeM3000 = _S5ChasTypeM3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 28)
)
_S5ChasTypeXedia_ObjectIdentity = ObjectIdentity
s5ChasTypeXedia = _S5ChasTypeXedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 29)
)
_S5ChasTypeNotUsed_ObjectIdentity = ObjectIdentity
s5ChasTypeNotUsed = _S5ChasTypeNotUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 30)
)
_S5ChasType28200_ObjectIdentity = ObjectIdentity
s5ChasType28200 = _S5ChasType28200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 31)
)
_S5ChasType28200Unit_4slot_ObjectIdentity = ObjectIdentity
s5ChasType28200Unit_4slot = _S5ChasType28200Unit_4slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 31, 1)
)
_S5ChasTypeCent_sixSlot_ObjectIdentity = ObjectIdentity
s5ChasTypeCent_sixSlot = _S5ChasTypeCent_sixSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 32)
)
_S5ChasTypeCent_twelveSlot_ObjectIdentity = ObjectIdentity
s5ChasTypeCent_twelveSlot = _S5ChasTypeCent_twelveSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 33)
)
_S5ChasTypeCent_singleSlot_ObjectIdentity = ObjectIdentity
s5ChasTypeCent_singleSlot = _S5ChasTypeCent_singleSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 34)
)
_S5ChasTypeBayStack301_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack301 = _S5ChasTypeBayStack301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 35)
)
_S5ChasTypeBayStackTr_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStackTr = _S5ChasTypeBayStackTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 36)
)
_S5ChasTypeBayStackTrUnit_24_port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStackTrUnit_24_port = _S5ChasTypeBayStackTrUnit_24_port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 36, 1)
)
_S5ChasTypeFVC10625_ObjectIdentity = ObjectIdentity
s5ChasTypeFVC10625 = _S5ChasTypeFVC10625_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 37)
)
_S5ChasTypeSwitchNode_ObjectIdentity = ObjectIdentity
s5ChasTypeSwitchNode = _S5ChasTypeSwitchNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 38)
)
_S5ChasTypeBayStack302_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack302 = _S5ChasTypeBayStack302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 39)
)
_S5ChasTypeBayStack302_ethSwitch_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack302_ethSwitch = _S5ChasTypeBayStack302_ethSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 39, 1)
)
_S5ChasTypeBayStack350_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack350 = _S5ChasTypeBayStack350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 40)
)
_S5ChasTypeBayStack350_ethSwitch_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack350_ethSwitch = _S5ChasTypeBayStack350_ethSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 40, 1)
)
_S5ChasTypeBayStack150_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack150 = _S5ChasTypeBayStack150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 41)
)
_S5ChasTypeBayStack150MasterUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack150MasterUnit_24Port = _S5ChasTypeBayStack150MasterUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 41, 1)
)
_S5ChasTypeBayStack150MasterUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack150MasterUnit_12Port = _S5ChasTypeBayStack150MasterUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 41, 2)
)
_S5ChasTypeBayStack150SlaveUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack150SlaveUnit_24Port = _S5ChasTypeBayStack150SlaveUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 41, 3)
)
_S5ChasTypeBayStack150SlaveUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack150SlaveUnit_12Port = _S5ChasTypeBayStack150SlaveUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 41, 4)
)
_S5ChasTypeC50N_ObjectIdentity = ObjectIdentity
s5ChasTypeC50N = _S5ChasTypeC50N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 42)
)
_S5ChasTypeC50T_ObjectIdentity = ObjectIdentity
s5ChasTypeC50T = _S5ChasTypeC50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 43)
)
_S5ChasTypeBayStack303_304_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack303_304 = _S5ChasTypeBayStack303_304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 44)
)
_S5ChasTypeBayStack200_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack200 = _S5ChasTypeBayStack200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 45)
)
_S5ChasTypeBayStack200NMMHostUnit_12TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack200NMMHostUnit_12TxPort = _S5ChasTypeBayStack200NMMHostUnit_12TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 45, 1)
)
_S5ChasTypeBayStack200NMMHostUnit_12Tx1FxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack200NMMHostUnit_12Tx1FxPort = _S5ChasTypeBayStack200NMMHostUnit_12Tx1FxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 45, 2)
)
_S5ChasTypeBayStack200HostUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack200HostUnit_24Port = _S5ChasTypeBayStack200HostUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 45, 3)
)
_S5ChasTypeBayStack200HostUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack200HostUnit_12Port = _S5ChasTypeBayStack200HostUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 45, 4)
)
_S5ChasTypeBayStack250_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack250 = _S5ChasTypeBayStack250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46)
)
_S5ChasTypeBayStack250NMMHostUnit_12TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack250NMMHostUnit_12TxPort = _S5ChasTypeBayStack250NMMHostUnit_12TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 1)
)
_S5ChasTypeBayStack250HostUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack250HostUnit_24Port = _S5ChasTypeBayStack250HostUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 2)
)
_S5ChasTypeBayStack250HostUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack250HostUnit_12Port = _S5ChasTypeBayStack250HostUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 3)
)
_S5ChasTypeBayStack250NMMHostUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack250NMMHostUnit_24Port = _S5ChasTypeBayStack250NMMHostUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 4)
)
_S5ChasTypeBayStack254HostUnit_12Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack254HostUnit_12Port = _S5ChasTypeBayStack254HostUnit_12Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 5)
)
_S5ChasTypeBayStack255HostUnit_24Port_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack255HostUnit_24Port = _S5ChasTypeBayStack255HostUnit_24Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 46, 6)
)
_S5ChasTypeStackProbe_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe = _S5ChasTypeStackProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47)
)
_S5ChasTypeStackProbeOgp_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgp = _S5ChasTypeStackProbeOgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1)
)
_S5ChasTypeStackProbeOgpEth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpEth = _S5ChasTypeStackProbeOgpEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 1)
)
_S5ChasTypeStackProbeOgpEth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpEth_1Port = _S5ChasTypeStackProbeOgpEth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 1, 1)
)
_S5ChasTypeStackProbeOgpEth_2Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpEth_2Port = _S5ChasTypeStackProbeOgpEth_2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 1, 2)
)
_S5ChasTypeStackProbeOgpEth_4Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpEth_4Port = _S5ChasTypeStackProbeOgpEth_4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 1, 4)
)
_S5ChasTypeStackProbeOgpTr_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpTr = _S5ChasTypeStackProbeOgpTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 2)
)
_S5ChasTypeStackProbeOgpTr_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpTr_1Port = _S5ChasTypeStackProbeOgpTr_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 2, 1)
)
_S5ChasTypeStackProbeOgpTr_2Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpTr_2Port = _S5ChasTypeStackProbeOgpTr_2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 2, 2)
)
_S5ChasTypeStackProbeOgpFddi_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFddi = _S5ChasTypeStackProbeOgpFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 3)
)
_S5ChasTypeStackProbeOgpFddiSas_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFddiSas = _S5ChasTypeStackProbeOgpFddiSas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 3, 1)
)
_S5ChasTypeStackProbeOgpFddiDas_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFddiDas = _S5ChasTypeStackProbeOgpFddiDas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 3, 2)
)
_S5ChasTypeStackProbeOgpFeth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFeth = _S5ChasTypeStackProbeOgpFeth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 4)
)
_S5ChasTypeStackProbeOgpFeth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFeth_1Port = _S5ChasTypeStackProbeOgpFeth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 4, 1)
)
_S5ChasTypeStackProbeOgpFeth_2Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbeOgpFeth_2Port = _S5ChasTypeStackProbeOgpFeth_2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 1, 4, 2)
)
_S5ChasTypeStackProbe1000_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe1000 = _S5ChasTypeStackProbe1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 2)
)
_S5ChasTypeStackProbe1000Eth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe1000Eth = _S5ChasTypeStackProbe1000Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 2, 1)
)
_S5ChasTypeStackProbe1000Eth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe1000Eth_1Port = _S5ChasTypeStackProbe1000Eth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 2, 1, 1)
)
_S5ChasTypeStackProbe1000Feth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe1000Feth = _S5ChasTypeStackProbe1000Feth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 2, 2)
)
_S5ChasTypeStackProbe1000Feth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe1000Feth_1Port = _S5ChasTypeStackProbe1000Feth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 2, 2, 1)
)
_S5ChasTypeStackProbe2000_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000 = _S5ChasTypeStackProbe2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3)
)
_S5ChasTypeStackProbe2000Eth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000Eth = _S5ChasTypeStackProbe2000Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 1)
)
_S5ChasTypeStackProbe2000Eth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000Eth_1Port = _S5ChasTypeStackProbe2000Eth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 1, 1)
)
_S5ChasTypeStackProbe2000Eth_2Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000Eth_2Port = _S5ChasTypeStackProbe2000Eth_2Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 1, 2)
)
_S5ChasTypeStackProbe2000Eth_4Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000Eth_4Port = _S5ChasTypeStackProbe2000Eth_4Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 1, 4)
)
_S5ChasTypeStackProbe2000Fddi_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000Fddi = _S5ChasTypeStackProbe2000Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 2)
)
_S5ChasTypeStackProbe2000FddiSas_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000FddiSas = _S5ChasTypeStackProbe2000FddiSas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 2, 1)
)
_S5ChasTypeStackProbe2000FddiDas_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe2000FddiDas = _S5ChasTypeStackProbe2000FddiDas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 3, 2, 2)
)
_S5ChasTypeStackProbe3000_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe3000 = _S5ChasTypeStackProbe3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 4)
)
_S5ChasTypeStackProbe3000Geth_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe3000Geth = _S5ChasTypeStackProbe3000Geth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 4, 1)
)
_S5ChasTypeStackProbe3000Geth_1Port_ObjectIdentity = ObjectIdentity
s5ChasTypeStackProbe3000Geth_1Port = _S5ChasTypeStackProbe3000Geth_1Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 47, 4, 1, 1)
)
_S5ChasTypeBayStack450_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack450 = _S5ChasTypeBayStack450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 48)
)
_S5ChasTypeBayStack450_12TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack450_12TxPort = _S5ChasTypeBayStack450_12TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 48, 1)
)
_S5ChasTypeBayStack450_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack450_24TxPort = _S5ChasTypeBayStack450_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 48, 2)
)
_S5ChasTypeBayStack303_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack303_24T = _S5ChasTypeBayStack303_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 49)
)
_S5ChasTypeAccelar8010_ObjectIdentity = ObjectIdentity
s5ChasTypeAccelar8010 = _S5ChasTypeAccelar8010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 58)
)
_S5ChasTypeAccelar8006_ObjectIdentity = ObjectIdentity
s5ChasTypeAccelar8006 = _S5ChasTypeAccelar8006_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 59)
)
_S5ChasTypeBayStack670_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack670 = _S5ChasTypeBayStack670_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 60)
)
_S5ChasTypeBPS2000_ObjectIdentity = ObjectIdentity
s5ChasTypeBPS2000 = _S5ChasTypeBPS2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 64)
)
_S5ChasTypeBPS2000_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBPS2000_24TxPort = _S5ChasTypeBPS2000_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 64, 1)
)
_S5ChasTypeBayStack3580_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack3580 = _S5ChasTypeBayStack3580_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 67)
)
_S5ChasTypeBayStack3580_16F_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack3580_16F = _S5ChasTypeBayStack3580_16F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 67, 1)
)
_S5ChasTypeBayStack420_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack420 = _S5ChasTypeBayStack420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 69)
)
_S5ChasTypeBayStack420_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack420_24TxPort = _S5ChasTypeBayStack420_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 69, 1)
)
_S5ChasTypeMetro1200ESM_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1200ESM = _S5ChasTypeMetro1200ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 70)
)
_S5ChasTypeMetro1200ESM_12TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1200ESM_12TxPort = _S5ChasTypeMetro1200ESM_12TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 70, 1)
)
_S5ChasTypeBayStack380_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack380 = _S5ChasTypeBayStack380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 71)
)
_S5ChasTypeBayStack380_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack380_24TxPort = _S5ChasTypeBayStack380_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 71, 1)
)
_S5ChasTypeBayStack470_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470 = _S5ChasTypeBayStack470_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 72)
)
_S5ChasTypeBayStack470_48TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_48TxPort = _S5ChasTypeBayStack470_48TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 72, 1)
)
_S5ChasTypeMetro1450ESM_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1450ESM = _S5ChasTypeMetro1450ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 73)
)
_S5ChasTypeMetro1450ESM_12TxPort2Gbic_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1450ESM_12TxPort2Gbic = _S5ChasTypeMetro1450ESM_12TxPort2Gbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 73, 1)
)
_S5ChasTypeMetro1400ESM_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1400ESM = _S5ChasTypeMetro1400ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 74)
)
_S5ChasTypeMetro1400ESM_12TxPort2Gbic_ObjectIdentity = ObjectIdentity
s5ChasTypeMetro1400ESM_12TxPort2Gbic = _S5ChasTypeMetro1400ESM_12TxPort2Gbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 74, 1)
)
_S5ChasTypeBayStack460_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack460_24T_PWR = _S5ChasTypeBayStack460_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 75)
)
_S5ChasTypeBayStack460_24T_PWR_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack460_24T_PWR_24TxPort = _S5ChasTypeBayStack460_24T_PWR_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 75, 1)
)
_S5ChasTypeBayStack10_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack10 = _S5ChasTypeBayStack10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 76)
)
_S5ChasTypeBayStack10_powerSupplyUnit_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack10_powerSupplyUnit = _S5ChasTypeBayStack10_powerSupplyUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 76, 1)
)
_S5ChasTypeBayStack380_24F_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack380_24F = _S5ChasTypeBayStack380_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 77)
)
_S5ChasTypeBayStack380_24F_20MiniGbic4Gbic_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack380_24F_20MiniGbic4Gbic = _S5ChasTypeBayStack380_24F_20MiniGbic4Gbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 77, 1)
)
_S5ChasTypeBayStack5510_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5510_24T = _S5ChasTypeBayStack5510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 78)
)
_S5ChasTypeBayStack5510_24T_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5510_24T_24TxPort = _S5ChasTypeBayStack5510_24T_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 78, 1)
)
_S5ChasTypeBayStack5510_48T_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5510_48T = _S5ChasTypeBayStack5510_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 79)
)
_S5ChasTypeBayStack5510_48T_48TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5510_48T_48TxPort = _S5ChasTypeBayStack5510_48T_48TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 79, 1)
)
_S5ChasTypeBayStack470_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_24T = _S5ChasTypeBayStack470_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 80)
)
_S5ChasTypeBayStack470_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_24TxPort = _S5ChasTypeBayStack470_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 80, 1)
)
_S5ChasTypeWLANAccessPoint2220_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2220 = _S5ChasTypeWLANAccessPoint2220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 81)
)
_S5ChasTypeWLANAccessPoint2220_wirelessAP_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2220_wirelessAP = _S5ChasTypeWLANAccessPoint2220_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 81, 1)
)
_S5ChasTypeWLANSecuritySwitch2250_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANSecuritySwitch2250 = _S5ChasTypeWLANSecuritySwitch2250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 82)
)
_S5ChasTypeWLANSecuritySwitch2250_securitySwitch_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANSecuritySwitch2250_securitySwitch = _S5ChasTypeWLANSecuritySwitch2250_securitySwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 82, 1)
)
_S5ChasTypeBayStack425_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack425 = _S5ChasTypeBayStack425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 83)
)
_S5ChasTypeBayStack425_24_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack425_24 = _S5ChasTypeBayStack425_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 83, 1)
)
_S5ChasTypeBayStack425_48_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack425_48 = _S5ChasTypeBayStack425_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 83, 2)
)
_S5ChasTypeWLANAccessPoint2221_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2221 = _S5ChasTypeWLANAccessPoint2221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 84)
)
_S5ChasTypeWLANAccessPoint2221_wirelessAP_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2221_wirelessAP = _S5ChasTypeWLANAccessPoint2221_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 84, 1)
)
_S5ChasTypeBayStack5520_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5520 = _S5ChasTypeBayStack5520_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 85)
)
_S5ChasTypeBayStack5520_24T_PWR_24TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5520_24T_PWR_24TxPort = _S5ChasTypeBayStack5520_24T_PWR_24TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 85, 1)
)
_S5ChasTypeBayStack5520_48T_PWR_48TxPort_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack5520_48T_PWR_48TxPort = _S5ChasTypeBayStack5520_48T_PWR_48TxPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 85, 2)
)
_S5ChasTypeBayStack325_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack325 = _S5ChasTypeBayStack325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 86)
)
_S5ChasTypeBayStack325_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack325_24T = _S5ChasTypeBayStack325_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 86, 1)
)
_S5ChasTypeBayStack325_24G_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack325_24G = _S5ChasTypeBayStack325_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 86, 2)
)
_S5ChasTypeWLANAccessPoint2225_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2225 = _S5ChasTypeWLANAccessPoint2225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 87)
)
_S5ChasTypeWLANAccessPoint2225_wirelessAP_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANAccessPoint2225_wirelessAP = _S5ChasTypeWLANAccessPoint2225_wirelessAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 87, 1)
)
_S5ChasTypeBayStack470_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_24T_PWR = _S5ChasTypeBayStack470_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 88)
)
_S5ChasTypeBayStack470_24TxPort_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_24TxPort_PWR = _S5ChasTypeBayStack470_24TxPort_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 88, 1)
)
_S5ChasTypeBayStack470_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_48T_PWR = _S5ChasTypeBayStack470_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 89)
)
_S5ChasTypeBayStack470_48TxPort_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBayStack470_48TxPort_PWR = _S5ChasTypeBayStack470_48TxPort_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 89, 1)
)
_S5ChasTypeWLANSecuritySwitch2270_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANSecuritySwitch2270 = _S5ChasTypeWLANSecuritySwitch2270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 90)
)
_S5ChasTypeWLANSecuritySwitch2270_securitySwitch_ObjectIdentity = ObjectIdentity
s5ChasTypeWLANSecuritySwitch2270_securitySwitch = _S5ChasTypeWLANSecuritySwitch2270_securitySwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 90, 1)
)
_S5ChasTypeEthernetRoutingSwitch5530_ObjectIdentity = ObjectIdentity
s5ChasTypeEthernetRoutingSwitch5530 = _S5ChasTypeEthernetRoutingSwitch5530_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 91)
)
_S5ChasTypeEthernetRoutingSwitch5530_24TFD_ObjectIdentity = ObjectIdentity
s5ChasTypeEthernetRoutingSwitch5530_24TFD = _S5ChasTypeEthernetRoutingSwitch5530_24TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 91, 1)
)
_S5ChasTypeEthernetSwitch3510_ObjectIdentity = ObjectIdentity
s5ChasTypeEthernetSwitch3510 = _S5ChasTypeEthernetSwitch3510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 92)
)
_S5ChasTypeEthernetSwitch3510_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeEthernetSwitch3510_24T = _S5ChasTypeEthernetSwitch3510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 92, 1)
)
_S5ChasTypeBES1010_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1010 = _S5ChasTypeBES1010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 93)
)
_S5ChasTypeBES1010_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1010_24T = _S5ChasTypeBES1010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 93, 1)
)
_S5ChasTypeBES1010_48T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1010_48T = _S5ChasTypeBES1010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 93, 2)
)
_S5ChasTypeBES1020_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1020 = _S5ChasTypeBES1020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 94)
)
_S5ChasTypeBES1020_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1020_24T_PWR = _S5ChasTypeBES1020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 94, 1)
)
_S5ChasTypeBES1020_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES1020_48T_PWR = _S5ChasTypeBES1020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 94, 2)
)
_S5ChasTypeBES2010_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2010 = _S5ChasTypeBES2010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 95)
)
_S5ChasTypeBES2010_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2010_24T = _S5ChasTypeBES2010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 95, 1)
)
_S5ChasTypeBES2010_48T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2010_48T = _S5ChasTypeBES2010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 95, 2)
)
_S5ChasTypeBES2020_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2020 = _S5ChasTypeBES2020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 96)
)
_S5ChasTypeBES2020_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2020_24T_PWR = _S5ChasTypeBES2020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 96, 1)
)
_S5ChasTypeBES2020_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES2020_48T_PWR = _S5ChasTypeBES2020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 96, 2)
)
_S5ChasTypeBES110_ObjectIdentity = ObjectIdentity
s5ChasTypeBES110 = _S5ChasTypeBES110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 97)
)
_S5ChasTypeBES110_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES110_24T = _S5ChasTypeBES110_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 97, 1)
)
_S5ChasTypeBES110_48T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES110_48T = _S5ChasTypeBES110_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 97, 2)
)
_S5ChasTypeBES120_ObjectIdentity = ObjectIdentity
s5ChasTypeBES120 = _S5ChasTypeBES120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 98)
)
_S5ChasTypeBES120_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES120_24T_PWR = _S5ChasTypeBES120_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 98, 1)
)
_S5ChasTypeBES120_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES120_48T_PWR = _S5ChasTypeBES120_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 98, 2)
)
_S5ChasTypeBES210_ObjectIdentity = ObjectIdentity
s5ChasTypeBES210 = _S5ChasTypeBES210_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 99)
)
_S5ChasTypeBES210_24T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES210_24T = _S5ChasTypeBES210_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 99, 1)
)
_S5ChasTypeBES210_48T_ObjectIdentity = ObjectIdentity
s5ChasTypeBES210_48T = _S5ChasTypeBES210_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 99, 2)
)
_S5ChasTypeBES220_ObjectIdentity = ObjectIdentity
s5ChasTypeBES220 = _S5ChasTypeBES220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 100)
)
_S5ChasTypeBES220_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES220_24T_PWR = _S5ChasTypeBES220_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 100, 1)
)
_S5ChasTypeBES220_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeBES220_48T_PWR = _S5ChasTypeBES220_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 100, 2)
)
_S5ChasTypeERS45xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS45xx = _S5ChasTypeERS45xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101)
)
_S5ChasTypeERS4548GT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4548GT = _S5ChasTypeERS4548GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 1)
)
_S5ChasTypeERS4548GT_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4548GT_PWR = _S5ChasTypeERS4548GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 2)
)
_S5ChasTypeERS4550T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4550T = _S5ChasTypeERS4550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 3)
)
_S5ChasTypeERS4550T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4550T_PWR = _S5ChasTypeERS4550T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 4)
)
_S5ChasTypeERS4526FX_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526FX = _S5ChasTypeERS4526FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 5)
)
_S5ChasTypeERS4526GTX_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526GTX_PWR = _S5ChasTypeERS4526GTX_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 6)
)
_S5ChasTypeERS4526GTX_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526GTX = _S5ChasTypeERS4526GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 7)
)
_S5ChasTypeERS4524GT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4524GT = _S5ChasTypeERS4524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 8)
)
_S5ChasTypeERS4526T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526T_PWR = _S5ChasTypeERS4526T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 9)
)
_S5ChasTypeERS4526T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526T = _S5ChasTypeERS4526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 10)
)
_S5ChasTypeERS4524GT_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4524GT_PWR = _S5ChasTypeERS4524GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 11)
)
_S5ChasTypeERS4526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4526T_PWR_PLUS = _S5ChasTypeERS4526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 12)
)
_S5ChasTypeERS4550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4550T_PWR_PLUS = _S5ChasTypeERS4550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 101, 13)
)
_S5ChasTypeERS25xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS25xx = _S5ChasTypeERS25xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 102)
)
_S5ChasTypeERS2500_26T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS2500_26T = _S5ChasTypeERS2500_26T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 102, 1)
)
_S5ChasTypeERS2500_26T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS2500_26T_PWR = _S5ChasTypeERS2500_26T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 102, 2)
)
_S5ChasTypeERS2500_50T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS2500_50T = _S5ChasTypeERS2500_50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 102, 3)
)
_S5ChasTypeERS2500_50T_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS2500_50T_PWR = _S5ChasTypeERS2500_50T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 102, 4)
)
_S5ChasTypeERS56xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS56xx = _S5ChasTypeERS56xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103)
)
_S5ChasTypeERS5698_TFD_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5698_TFD_PWR = _S5ChasTypeERS5698_TFD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103, 1)
)
_S5ChasTypeERS5698_TFD_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5698_TFD = _S5ChasTypeERS5698_TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103, 2)
)
_S5ChasTypeERS5650_TD_PWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5650_TD_PWR = _S5ChasTypeERS5650_TD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103, 3)
)
_S5ChasTypeERS5650_TD_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5650_TD = _S5ChasTypeERS5650_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103, 4)
)
_S5ChasTypeERS5632_FD_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5632_FD = _S5ChasTypeERS5632_FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 103, 5)
)
_S5ChasTypeESU1860_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1860 = _S5ChasTypeESU1860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 104)
)
_S5ChasTypeESU1860S_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1860S = _S5ChasTypeESU1860S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 104, 1)
)
_S5ChasTypeESU1860B_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1860B = _S5ChasTypeESU1860B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 104, 2)
)
_S5ChasTypeESU1860T_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1860T = _S5ChasTypeESU1860T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 104, 3)
)
_S5ChasTypeESU1860V_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1860V = _S5ChasTypeESU1860V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 104, 4)
)
_S5ChasTypeESU1880_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1880 = _S5ChasTypeESU1880_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 105)
)
_S5ChasTypeESU1880S_ObjectIdentity = ObjectIdentity
s5ChasTypeESU1880S = _S5ChasTypeESU1880S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 105, 1)
)
_S5ChasTypeERS66xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS66xx = _S5ChasTypeERS66xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 106)
)
_S5ChasTypeERS642_XSGT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS642_XSGT = _S5ChasTypeERS642_XSGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 106, 1)
)
_S5ChasTypeERS6632_XTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS6632_XTS = _S5ChasTypeERS6632_XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 106, 2)
)
_S5ChasTypeWC8xxx_ObjectIdentity = ObjectIdentity
s5ChasTypeWC8xxx = _S5ChasTypeWC8xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 107)
)
_S5ChasTypeWC8180_ObjectIdentity = ObjectIdentity
s5ChasTypeWC8180 = _S5ChasTypeWC8180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 107, 1)
)
_S5ChasTypeERS48xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS48xx = _S5ChasTypeERS48xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 108)
)
_S5ChasTypeERS4826GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4826GTS_PWR_PLUS = _S5ChasTypeERS4826GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 108, 1)
)
_S5ChasTypeERS4850GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4850GTS_PWR_PLUS = _S5ChasTypeERS4850GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 108, 2)
)
_S5ChasTypeERS4826GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4826GTS = _S5ChasTypeERS4826GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 108, 3)
)
_S5ChasTypeERS4850GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4850GTS = _S5ChasTypeERS4850GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 108, 4)
)
_S5ChasTypeVSP7xxx_ObjectIdentity = ObjectIdentity
s5ChasTypeVSP7xxx = _S5ChasTypeVSP7xxx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 109)
)
_S5ChasTypeVSP7024XLS_ObjectIdentity = ObjectIdentity
s5ChasTypeVSP7024XLS = _S5ChasTypeVSP7024XLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 109, 1)
)
_S5ChasTypeERS35xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS35xx = _S5ChasTypeERS35xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110)
)
_S5ChasTypeERS3510GT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3510GT = _S5ChasTypeERS3510GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 1)
)
_S5ChasTypeERS3510GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3510GT_PWR_PLUS = _S5ChasTypeERS3510GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 2)
)
_S5ChasTypeERS3524GT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3524GT = _S5ChasTypeERS3524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 3)
)
_S5ChasTypeERS3524GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3524GT_PWR_PLUS = _S5ChasTypeERS3524GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 4)
)
_S5ChasTypeERS3526GT_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3526GT = _S5ChasTypeERS3526GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 5)
)
_S5ChasTypeERS3526GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3526GT_PWR_PLUS = _S5ChasTypeERS3526GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 6)
)
_S5ChasTypeERS3526T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3526T = _S5ChasTypeERS3526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 7)
)
_S5ChasTypeERS3526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3526T_PWR_PLUS = _S5ChasTypeERS3526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 8)
)
_S5ChasTypeERS3549GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3549GTS = _S5ChasTypeERS3549GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 9)
)
_S5ChasTypeERS3549GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3549GTS_PWR_PLUS = _S5ChasTypeERS3549GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 10)
)
_S5ChasTypeERS3550T_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3550T = _S5ChasTypeERS3550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 11)
)
_S5ChasTypeERS3550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS3550T_PWR_PLUS = _S5ChasTypeERS3550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 110, 12)
)
_S5ChasTypeERS59xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS59xx = _S5ChasTypeERS59xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111)
)
_S5ChasTypeERS5928GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5928GTS = _S5ChasTypeERS5928GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 1)
)
_S5ChasTypeERS5928GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5928GTS_PWR_PLUS = _S5ChasTypeERS5928GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 2)
)
_S5ChasTypeERS5952GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5952GTS = _S5ChasTypeERS5952GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 3)
)
_S5ChasTypeERS5952GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5952GTS_PWR_PLUS = _S5ChasTypeERS5952GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 4)
)
_S5ChasTypeERS5928GTS_UPWR_ObjectIdentity = ObjectIdentity
s5ChasTypeERS5928GTS_UPWR = _S5ChasTypeERS5928GTS_UPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 5)
)
_S5ChasTypeERS59100GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS59100GTS = _S5ChasTypeERS59100GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 6)
)
_S5ChasTypeERS59100GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS59100GTS_PWR_PLUS = _S5ChasTypeERS59100GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 111, 7)
)
_S5ChasTypeERS49xx_ObjectIdentity = ObjectIdentity
s5ChasTypeERS49xx = _S5ChasTypeERS49xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 112)
)
_S5ChasTypeERS4926GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4926GTS = _S5ChasTypeERS4926GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 112, 1)
)
_S5ChasTypeERS4926GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4926GTS_PWR_PLUS = _S5ChasTypeERS4926GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 112, 2)
)
_S5ChasTypeERS4950GTS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4950GTS = _S5ChasTypeERS4950GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 112, 3)
)
_S5ChasTypeERS4950GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasTypeERS4950GTS_PWR_PLUS = _S5ChasTypeERS4950GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 1, 112, 4)
)
_S5ChasGrpTypeVal_ObjectIdentity = ObjectIdentity
s5ChasGrpTypeVal = _S5ChasGrpTypeVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2)
)
_S5ChasGrpSup_ObjectIdentity = ObjectIdentity
s5ChasGrpSup = _S5ChasGrpSup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 1)
)
_S5ChasGrpBkpl_ObjectIdentity = ObjectIdentity
s5ChasGrpBkpl = _S5ChasGrpBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 2)
)
_S5ChasGrpBrd_ObjectIdentity = ObjectIdentity
s5ChasGrpBrd = _S5ChasGrpBrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 3)
)
_S5ChasGrpPwr_ObjectIdentity = ObjectIdentity
s5ChasGrpPwr = _S5ChasGrpPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 4)
)
_S5ChasGrpTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasGrpTmpSnr = _S5ChasGrpTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 5)
)
_S5ChasGrpFan_ObjectIdentity = ObjectIdentity
s5ChasGrpFan = _S5ChasGrpFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 6)
)
_S5ChasGrpClk_ObjectIdentity = ObjectIdentity
s5ChasGrpClk = _S5ChasGrpClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 7)
)
_S5ChasGrpUnit_ObjectIdentity = ObjectIdentity
s5ChasGrpUnit = _S5ChasGrpUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 2, 8)
)
_S5ChasComTypeVal_ObjectIdentity = ObjectIdentity
s5ChasComTypeVal = _S5ChasComTypeVal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3)
)
_S5ChasComBkpl_ObjectIdentity = ObjectIdentity
s5ChasComBkpl = _S5ChasComBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1)
)
_S5ChasComBkplM5000low_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000low = _S5ChasComBkplM5000low_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 1)
)
_S5ChasComBkplM5000lowCmbEthTok_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000lowCmbEthTok = _S5ChasComBkplM5000lowCmbEthTok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 1, 4)
)
_S5ChasComBkplM5000lowCmbEth_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000lowCmbEth = _S5ChasComBkplM5000lowCmbEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 1, 5)
)
_S5ChasComBkplM5000midLeft_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000midLeft = _S5ChasComBkplM5000midLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 2)
)
_S5ChasComBkplM5000midLeftFddiFull_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000midLeftFddiFull = _S5ChasComBkplM5000midLeftFddiFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 2, 0)
)
_S5ChasComBkplM5000midRight_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000midRight = _S5ChasComBkplM5000midRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 3)
)
_S5ChasComBkplM5000midRightFddi_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000midRightFddi = _S5ChasComBkplM5000midRightFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 3, 0)
)
_S5ChasComBkplM5000highLeft_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000highLeft = _S5ChasComBkplM5000highLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 4)
)
_S5ChasComBkplM5000highRight_ObjectIdentity = ObjectIdentity
s5ChasComBkplM5000highRight = _S5ChasComBkplM5000highRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 5)
)
_S5ChasComBkplCentATM_ObjectIdentity = ObjectIdentity
s5ChasComBkplCentATM = _S5ChasComBkplCentATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 6)
)
_S5ChasComBkpl2x65000BH_ObjectIdentity = ObjectIdentity
s5ChasComBkpl2x65000BH = _S5ChasComBkpl2x65000BH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 7)
)
_S5ChasComBkpl1x125000BH_ObjectIdentity = ObjectIdentity
s5ChasComBkpl1x125000BH = _S5ChasComBkpl1x125000BH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 8)
)
_S5ChasComBkplC50_ObjectIdentity = ObjectIdentity
s5ChasComBkplC50 = _S5ChasComBkplC50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 1, 9)
)
_S5ChasComPwr_ObjectIdentity = ObjectIdentity
s5ChasComPwr = _S5ChasComPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2)
)
_S5ChasComPwrM5000_950A_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950A = _S5ChasComPwrM5000_950A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 0)
)
_S5ChasComPwrM5000_950AFan_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950AFan = _S5ChasComPwrM5000_950AFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 0, 1)
)
_S5ChasComPwrM5000_950ATmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950ATmpSnr = _S5ChasComPwrM5000_950ATmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 0, 2)
)
_S5ChasComPwrM5000_950_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950 = _S5ChasComPwrM5000_950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 1)
)
_S5ChasComPwrM5000_950Fan_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950Fan = _S5ChasComPwrM5000_950Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 1, 1)
)
_S5ChasComPwrM5000_950TmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComPwrM5000_950TmpSnr = _S5ChasComPwrM5000_950TmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 1, 2)
)
_S5ChasComPwrCent_ObjectIdentity = ObjectIdentity
s5ChasComPwrCent = _S5ChasComPwrCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 2)
)
_S5ChasComPwrCent50N_ObjectIdentity = ObjectIdentity
s5ChasComPwrCent50N = _S5ChasComPwrCent50N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 3)
)
_S5ChasComPwrCent50T_ObjectIdentity = ObjectIdentity
s5ChasComPwrCent50T = _S5ChasComPwrCent50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 2, 4)
)
_S5ChasComTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnr = _S5ChasComTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3)
)
_S5ChasComTmpSnrM5000_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrM5000 = _S5ChasComTmpSnrM5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 1)
)
_S5ChasComTmpSnrMetro1200ESM_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrMetro1200ESM = _S5ChasComTmpSnrMetro1200ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 2)
)
_S5ChasComTmpSnrMetro1450ESM_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrMetro1450ESM = _S5ChasComTmpSnrMetro1450ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 3)
)
_S5ChasComTmpSnrMetro1400ESM_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrMetro1400ESM = _S5ChasComTmpSnrMetro1400ESM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 4)
)
_S5ChasComTmpSnrBayStack460_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack460_24T_PWR = _S5ChasComTmpSnrBayStack460_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 5)
)
_S5ChasComTmpSnrBayStack5510_24T_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack5510_24T = _S5ChasComTmpSnrBayStack5510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 6)
)
_S5ChasComTmpSnrBayStack5510_48T_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack5510_48T = _S5ChasComTmpSnrBayStack5510_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 7)
)
_S5ChasComTmpSnrBayStack425_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack425 = _S5ChasComTmpSnrBayStack425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 8)
)
_S5ChasComTmpSnrBayStack5520_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack5520_24T_PWR = _S5ChasComTmpSnrBayStack5520_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 9)
)
_S5ChasComTmpSnrBayStack5520_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack5520_48T_PWR = _S5ChasComTmpSnrBayStack5520_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 10)
)
_S5ChasComTmpSnrBayStack325_ObjectIdentity = ObjectIdentity
s5ChasComTmpSnrBayStack325 = _S5ChasComTmpSnrBayStack325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 3, 11)
)
_S5ChasComFan_ObjectIdentity = ObjectIdentity
s5ChasComFan = _S5ChasComFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 4)
)
_S5ChasComFanM5000_ObjectIdentity = ObjectIdentity
s5ChasComFanM5000 = _S5ChasComFanM5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 4, 1)
)
_S5ChasComFanCent_ObjectIdentity = ObjectIdentity
s5ChasComFanCent = _S5ChasComFanCent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 4, 2)
)
_S5ChasComCent50NFan_ObjectIdentity = ObjectIdentity
s5ChasComCent50NFan = _S5ChasComCent50NFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 4, 3)
)
_S5ChasComCent50TFan_ObjectIdentity = ObjectIdentity
s5ChasComCent50TFan = _S5ChasComCent50TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 4, 4)
)
_S5ChasComClk_ObjectIdentity = ObjectIdentity
s5ChasComClk = _S5ChasComClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 5)
)
_S5ChasComClkM5000_ObjectIdentity = ObjectIdentity
s5ChasComClkM5000 = _S5ChasComClkM5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 5, 1)
)
_S5ChasComMod_ObjectIdentity = ObjectIdentity
s5ChasComMod = _S5ChasComMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6)
)
_S5ChasComM331X_ObjectIdentity = ObjectIdentity
s5ChasComM331X = _S5ChasComM331X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 1)
)
_S5ChasComMDA331X_ObjectIdentity = ObjectIdentity
s5ChasComMDA331X = _S5ChasComMDA331X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 1, 255)
)
_S5ChasComM3302_ObjectIdentity = ObjectIdentity
s5ChasComM3302 = _S5ChasComM3302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 2)
)
_S5ChasComMDA3302_ObjectIdentity = ObjectIdentity
s5ChasComMDA3302 = _S5ChasComMDA3302_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 2, 255)
)
_S5ChasComM33XX_ObjectIdentity = ObjectIdentity
s5ChasComM33XX = _S5ChasComM33XX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 3)
)
_S5ChasComMDA3324_ST_ObjectIdentity = ObjectIdentity
s5ChasComMDA3324_ST = _S5ChasComMDA3324_ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 3, 0)
)
_S5ChasComMDA3323_ObjectIdentity = ObjectIdentity
s5ChasComMDA3323 = _S5ChasComMDA3323_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 3, 3)
)
_S5ChasComM3304_ObjectIdentity = ObjectIdentity
s5ChasComM3304 = _S5ChasComM3304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 4)
)
_S5ChasComMDA3304_ObjectIdentity = ObjectIdentity
s5ChasComMDA3304 = _S5ChasComMDA3304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 4, 255)
)
_S5ChasComM3305_ObjectIdentity = ObjectIdentity
s5ChasComM3305 = _S5ChasComM3305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 5)
)
_S5ChasComMDA3305_ObjectIdentity = ObjectIdentity
s5ChasComMDA3305 = _S5ChasComMDA3305_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 5, 255)
)
_S5ChasComM333X_ObjectIdentity = ObjectIdentity
s5ChasComM333X = _S5ChasComM333X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 6)
)
_S5ChasComMDA3334_ST_ObjectIdentity = ObjectIdentity
s5ChasComMDA3334_ST = _S5ChasComMDA3334_ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 6, 0)
)
_S5ChasComMDA3333_ObjectIdentity = ObjectIdentity
s5ChasComMDA3333 = _S5ChasComMDA3333_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 6, 3)
)
_S5ChasComM3307_ObjectIdentity = ObjectIdentity
s5ChasComM3307 = _S5ChasComM3307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 7)
)
_S5ChasComMDA3307_ObjectIdentity = ObjectIdentity
s5ChasComMDA3307 = _S5ChasComMDA3307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 7, 255)
)
_S5ChasComM3308_ObjectIdentity = ObjectIdentity
s5ChasComM3308 = _S5ChasComM3308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 8)
)
_S5ChasComMDA3308_ObjectIdentity = ObjectIdentity
s5ChasComMDA3308 = _S5ChasComMDA3308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 8, 255)
)
_S5ChasComM3301_ObjectIdentity = ObjectIdentity
s5ChasComM3301 = _S5ChasComM3301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 9)
)
_S5ChasComMDA3301_ObjectIdentity = ObjectIdentity
s5ChasComMDA3301 = _S5ChasComMDA3301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 9, 255)
)
_S5ChasComM3904_ObjectIdentity = ObjectIdentity
s5ChasComM3904 = _S5ChasComM3904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 10)
)
_S5ChasComMDA3904_ObjectIdentity = ObjectIdentity
s5ChasComMDA3904 = _S5ChasComMDA3904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 10, 85)
)
_S5ChasComMDA3904_2SM_ObjectIdentity = ObjectIdentity
s5ChasComMDA3904_2SM = _S5ChasComMDA3904_2SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 10, 90)
)
_S5ChasComMDA3904_4SM_ObjectIdentity = ObjectIdentity
s5ChasComMDA3904_4SM = _S5ChasComMDA3904_4SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 10, 170)
)
_S5ChasComM3902_ObjectIdentity = ObjectIdentity
s5ChasComM3902 = _S5ChasComM3902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 11)
)
_S5ChasComMDA3902_ObjectIdentity = ObjectIdentity
s5ChasComMDA3902 = _S5ChasComMDA3902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 11, 255)
)
_S5ChasComM3910S_ObjectIdentity = ObjectIdentity
s5ChasComM3910S = _S5ChasComM3910S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 12)
)
_S5ChasComMDA3910S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3910S = _S5ChasComMDA3910S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 12, 80)
)
_S5ChasComMDA3910S_SM_ObjectIdentity = ObjectIdentity
s5ChasComMDA3910S_SM = _S5ChasComMDA3910S_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 12, 160)
)
_S5ChasComM331XS_ObjectIdentity = ObjectIdentity
s5ChasComM331XS = _S5ChasComM331XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 14)
)
_S5ChasComMDA3314S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3314S = _S5ChasComMDA3314S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 14, 0)
)
_S5ChasComMDA3313S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3313S = _S5ChasComMDA3313S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 14, 3)
)
_S5ChasComM3100R_ObjectIdentity = ObjectIdentity
s5ChasComM3100R = _S5ChasComM3100R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 15)
)
_S5ChasComMDA3100R_ObjectIdentity = ObjectIdentity
s5ChasComMDA3100R = _S5ChasComMDA3100R_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 15, 255)
)
_S5ChasComM3502_ObjectIdentity = ObjectIdentity
s5ChasComM3502 = _S5ChasComM3502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 16)
)
_S5ChasComMDA3502_ObjectIdentity = ObjectIdentity
s5ChasComMDA3502 = _S5ChasComMDA3502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 16, 255)
)
_S5ChasComM3502A_ObjectIdentity = ObjectIdentity
s5ChasComM3502A = _S5ChasComM3502A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 17)
)
_S5ChasComMDA3502A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3502A = _S5ChasComMDA3502A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 17, 255)
)
_S5ChasComM353X_ObjectIdentity = ObjectIdentity
s5ChasComM353X = _S5ChasComM353X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 18)
)
_S5ChasComMDA3532_ObjectIdentity = ObjectIdentity
s5ChasComMDA3532 = _S5ChasComMDA3532_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 18, 2)
)
_S5ChasComMDA3534_ObjectIdentity = ObjectIdentity
s5ChasComMDA3534 = _S5ChasComMDA3534_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 18, 4)
)
_S5ChasComM3040_ObjectIdentity = ObjectIdentity
s5ChasComM3040 = _S5ChasComM3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 19)
)
_S5ChasComMDA3040_ObjectIdentity = ObjectIdentity
s5ChasComMDA3040 = _S5ChasComMDA3040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 19, 255)
)
_S5ChasComM3505_ObjectIdentity = ObjectIdentity
s5ChasComM3505 = _S5ChasComM3505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 20)
)
_S5ChasComMDA3505_ObjectIdentity = ObjectIdentity
s5ChasComMDA3505 = _S5ChasComMDA3505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 20, 255)
)
_S5ChasComM3505A_ObjectIdentity = ObjectIdentity
s5ChasComM3505A = _S5ChasComM3505A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 21)
)
_S5ChasComMDA3505A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3505A = _S5ChasComMDA3505A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 21, 255)
)
_S5ChasComM355X_ObjectIdentity = ObjectIdentity
s5ChasComM355X = _S5ChasComM355X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 22)
)
_S5ChasComMDA3552_ObjectIdentity = ObjectIdentity
s5ChasComMDA3552 = _S5ChasComMDA3552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 22, 2)
)
_S5ChasComMDA3554_ObjectIdentity = ObjectIdentity
s5ChasComMDA3554 = _S5ChasComMDA3554_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 22, 4)
)
_S5ChasComM3040S_ObjectIdentity = ObjectIdentity
s5ChasComM3040S = _S5ChasComM3040S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 23)
)
_S5ChasComMDA3040S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3040S = _S5ChasComMDA3040S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 23, 255)
)
_S5ChasComM351X_ObjectIdentity = ObjectIdentity
s5ChasComM351X = _S5ChasComM351X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 24)
)
_S5ChasComMDA3512_ObjectIdentity = ObjectIdentity
s5ChasComMDA3512 = _S5ChasComMDA3512_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 24, 2)
)
_S5ChasComMDA3513_ObjectIdentity = ObjectIdentity
s5ChasComMDA3513 = _S5ChasComMDA3513_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 24, 3)
)
_S5ChasComMDA3514_ObjectIdentity = ObjectIdentity
s5ChasComMDA3514 = _S5ChasComMDA3514_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 24, 4)
)
_S5ChasComM33XXS_ObjectIdentity = ObjectIdentity
s5ChasComM33XXS = _S5ChasComM33XXS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 25)
)
_S5ChasComMDA3324S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3324S = _S5ChasComMDA3324S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 25, 0)
)
_S5ChasComMDA3323S_ObjectIdentity = ObjectIdentity
s5ChasComMDA3323S = _S5ChasComMDA3323S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 25, 3)
)
_S5ChasComM338X_ObjectIdentity = ObjectIdentity
s5ChasComM338X = _S5ChasComM338X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 26)
)
_S5ChasComMDA3384_ObjectIdentity = ObjectIdentity
s5ChasComMDA3384 = _S5ChasComMDA3384_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 26, 0)
)
_S5ChasComMDA3383_ObjectIdentity = ObjectIdentity
s5ChasComMDA3383 = _S5ChasComMDA3383_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 26, 3)
)
_S5ChasComMDA3386_ObjectIdentity = ObjectIdentity
s5ChasComMDA3386 = _S5ChasComMDA3386_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 26, 4)
)
_S5ChasComM3328_ObjectIdentity = ObjectIdentity
s5ChasComM3328 = _S5ChasComM3328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 27)
)
_S5ChasComMDA3328_ObjectIdentity = ObjectIdentity
s5ChasComMDA3328 = _S5ChasComMDA3328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 27, 255)
)
_S5ChasComM3395_ObjectIdentity = ObjectIdentity
s5ChasComM3395 = _S5ChasComM3395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 28)
)
_S5ChasComMDA3395_ObjectIdentity = ObjectIdentity
s5ChasComMDA3395 = _S5ChasComMDA3395_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 28, 255)
)
_S5ChasComM3394_ObjectIdentity = ObjectIdentity
s5ChasComM3394 = _S5ChasComM3394_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 29)
)
_S5ChasComMDA3394_ObjectIdentity = ObjectIdentity
s5ChasComMDA3394 = _S5ChasComMDA3394_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 29, 255)
)
_S5ChasComM3522_ObjectIdentity = ObjectIdentity
s5ChasComM3522 = _S5ChasComM3522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 30)
)
_S5ChasComMDA3522_ObjectIdentity = ObjectIdentity
s5ChasComMDA3522 = _S5ChasComMDA3522_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 30, 255)
)
_S5ChasComM3395A_ObjectIdentity = ObjectIdentity
s5ChasComM3395A = _S5ChasComM3395A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 31)
)
_S5ChasComMDA3395A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3395A = _S5ChasComMDA3395A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 31, 255)
)
_S5ChasComM3800_ObjectIdentity = ObjectIdentity
s5ChasComM3800 = _S5ChasComM3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32)
)
_S5ChasComMDA3803_ObjectIdentity = ObjectIdentity
s5ChasComMDA3803 = _S5ChasComMDA3803_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32, 0)
)
_S5ChasComMDA3805_ObjectIdentity = ObjectIdentity
s5ChasComMDA3805 = _S5ChasComMDA3805_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32, 1)
)
_S5ChasComMDA3809_ObjectIdentity = ObjectIdentity
s5ChasComMDA3809 = _S5ChasComMDA3809_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32, 2)
)
_S5ChasComMDA3806_ObjectIdentity = ObjectIdentity
s5ChasComMDA3806 = _S5ChasComMDA3806_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32, 3)
)
_S5ChasComMDA3800_ObjectIdentity = ObjectIdentity
s5ChasComMDA3800 = _S5ChasComMDA3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 32, 255)
)
_S5ChasComM3368_ObjectIdentity = ObjectIdentity
s5ChasComM3368 = _S5ChasComM3368_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 36)
)
_S5ChasComMDA3368_ObjectIdentity = ObjectIdentity
s5ChasComMDA3368 = _S5ChasComMDA3368_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 36, 255)
)
_S5ChasComM3307A_ObjectIdentity = ObjectIdentity
s5ChasComM3307A = _S5ChasComM3307A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 37)
)
_S5ChasComMDA3307A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3307A = _S5ChasComMDA3307A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 37, 255)
)
_S5ChasComM3308A_ObjectIdentity = ObjectIdentity
s5ChasComM3308A = _S5ChasComM3308A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 38)
)
_S5ChasComMDA3308A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3308A = _S5ChasComMDA3308A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 38, 255)
)
_S5ChasComM3301_75_ObjectIdentity = ObjectIdentity
s5ChasComM3301_75 = _S5ChasComM3301_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 41)
)
_S5ChasComMDA3301_75_ObjectIdentity = ObjectIdentity
s5ChasComMDA3301_75 = _S5ChasComMDA3301_75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 41, 255)
)
_S5ChasComM3301_93_ObjectIdentity = ObjectIdentity
s5ChasComM3301_93 = _S5ChasComM3301_93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 42)
)
_S5ChasComMDA3301_93_ObjectIdentity = ObjectIdentity
s5ChasComMDA3301_93 = _S5ChasComMDA3301_93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 42, 255)
)
_S5ChasComM3502B_ObjectIdentity = ObjectIdentity
s5ChasComM3502B = _S5ChasComM3502B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 45)
)
_S5ChasComMDA3502B_ObjectIdentity = ObjectIdentity
s5ChasComMDA3502B = _S5ChasComMDA3502B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 45, 255)
)
_S5ChasComM3505B_ObjectIdentity = ObjectIdentity
s5ChasComM3505B = _S5ChasComM3505B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 46)
)
_S5ChasComMDA3505B_ObjectIdentity = ObjectIdentity
s5ChasComMDA3505B = _S5ChasComMDA3505B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 46, 255)
)
_S5ChasComM3307HD_ObjectIdentity = ObjectIdentity
s5ChasComM3307HD = _S5ChasComM3307HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 47)
)
_S5ChasComMDA3307HD_ObjectIdentity = ObjectIdentity
s5ChasComMDA3307HD = _S5ChasComMDA3307HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 47, 255)
)
_S5ChasComM3356_ObjectIdentity = ObjectIdentity
s5ChasComM3356 = _S5ChasComM3356_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56)
)
_S5ChasSubComMDA3356X21_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356X21 = _S5ChasSubComMDA3356X21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 1)
)
_S5ChasSubComMDA3356X21U_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356X21U = _S5ChasSubComMDA3356X21U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 2)
)
_S5ChasSubComMDA3356RS232_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356RS232 = _S5ChasSubComMDA3356RS232_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 3)
)
_S5ChasSubComMDA3356RS449_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356RS449 = _S5ChasSubComMDA3356RS449_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 4)
)
_S5ChasSubComMDA3356V35_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356V35 = _S5ChasSubComMDA3356V35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 5)
)
_S5ChasSubComMDA3356G703_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356G703 = _S5ChasSubComMDA3356G703_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 6)
)
_S5ChasSubComMDA3356T1_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356T1 = _S5ChasSubComMDA3356T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 7)
)
_S5ChasSubComMDA3356_ObjectIdentity = ObjectIdentity
s5ChasSubComMDA3356 = _S5ChasSubComMDA3356_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 56, 255)
)
_S5ChasComM3902A_ObjectIdentity = ObjectIdentity
s5ChasComM3902A = _S5ChasComM3902A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 63)
)
_S5ChasComMDA3902A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3902A = _S5ChasComMDA3902A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 63, 255)
)
_S5ChasComM3910S_SD_ObjectIdentity = ObjectIdentity
s5ChasComM3910S_SD = _S5ChasComM3910S_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 67)
)
_S5ChasComMDA3910S_SD_ObjectIdentity = ObjectIdentity
s5ChasComMDA3910S_SD = _S5ChasComMDA3910S_SD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 67, 255)
)
_S5ChasComM3313A_ObjectIdentity = ObjectIdentity
s5ChasComM3313A = _S5ChasComM3313A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 68)
)
_S5ChasComMDA3313A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3313A = _S5ChasComMDA3313A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 68, 255)
)
_S5ChasComM3314A_ObjectIdentity = ObjectIdentity
s5ChasComM3314A = _S5ChasComM3314A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 69)
)
_S5ChasComMDA3314A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3314A = _S5ChasComMDA3314A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 69, 255)
)
_S5ChasComM3304A_ObjectIdentity = ObjectIdentity
s5ChasComM3304A = _S5ChasComM3304A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 70)
)
_S5ChasComMDA3304A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3304A = _S5ChasComMDA3304A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 70, 255)
)
_S5ChasComM3910SA_ObjectIdentity = ObjectIdentity
s5ChasComM3910SA = _S5ChasComM3910SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 71)
)
_S5ChasComMDA3910SA_ObjectIdentity = ObjectIdentity
s5ChasComMDA3910SA = _S5ChasComMDA3910SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 71, 80)
)
_S5ChasComMDA3910SA_SM_ObjectIdentity = ObjectIdentity
s5ChasComMDA3910SA_SM = _S5ChasComMDA3910SA_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 71, 160)
)
_S5ChasComM3905_ObjectIdentity = ObjectIdentity
s5ChasComM3905 = _S5ChasComM3905_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 73)
)
_S5ChasComMDA3905_ObjectIdentity = ObjectIdentity
s5ChasComMDA3905 = _S5ChasComMDA3905_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 73, 0)
)
_S5ChasComM3486_ObjectIdentity = ObjectIdentity
s5ChasComM3486 = _S5ChasComM3486_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 82)
)
_S5ChasComMDA3486_ObjectIdentity = ObjectIdentity
s5ChasComMDA3486 = _S5ChasComMDA3486_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 82, 255)
)
_S5ChasComM3504_ST_ObjectIdentity = ObjectIdentity
s5ChasComM3504_ST = _S5ChasComM3504_ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 83)
)
_S5ChasComMDA3504_ST_ObjectIdentity = ObjectIdentity
s5ChasComMDA3504_ST = _S5ChasComMDA3504_ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 83, 255)
)
_S5ChasComM3517SA_ObjectIdentity = ObjectIdentity
s5ChasComM3517SA = _S5ChasComM3517SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 101)
)
_S5ChasComMDA3517SA_ObjectIdentity = ObjectIdentity
s5ChasComMDA3517SA = _S5ChasComMDA3517SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 101, 255)
)
_S5ChasComM3308B_ObjectIdentity = ObjectIdentity
s5ChasComM3308B = _S5ChasComM3308B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 102)
)
_S5ChasComMDA3308B_ObjectIdentity = ObjectIdentity
s5ChasComMDA3308B = _S5ChasComMDA3308B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 102, 255)
)
_S5ChasComM3313SA_ObjectIdentity = ObjectIdentity
s5ChasComM3313SA = _S5ChasComM3313SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 105)
)
_S5ChasComMDA3313SA_ObjectIdentity = ObjectIdentity
s5ChasComMDA3313SA = _S5ChasComMDA3313SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 105, 255)
)
_S5ChasComM3314SA_ObjectIdentity = ObjectIdentity
s5ChasComM3314SA = _S5ChasComM3314SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 106)
)
_S5ChasComMDA3314SA_ObjectIdentity = ObjectIdentity
s5ChasComMDA3314SA = _S5ChasComMDA3314SA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 106, 255)
)
_S5ChasComM3174_ObjectIdentity = ObjectIdentity
s5ChasComM3174 = _S5ChasComM3174_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 107)
)
_S5ChasComMDA3174_ObjectIdentity = ObjectIdentity
s5ChasComMDA3174 = _S5ChasComMDA3174_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 107, 255)
)
_S5ChasComM3522A_ObjectIdentity = ObjectIdentity
s5ChasComM3522A = _S5ChasComM3522A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 108)
)
_S5ChasComMDA3522A_ObjectIdentity = ObjectIdentity
s5ChasComMDA3522A = _S5ChasComMDA3522A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 108, 255)
)
_S5ChasComM3299_C_ObjectIdentity = ObjectIdentity
s5ChasComM3299_C = _S5ChasComM3299_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 116)
)
_S5ChasComMDA3299_C_ObjectIdentity = ObjectIdentity
s5ChasComMDA3299_C = _S5ChasComMDA3299_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 116, 255)
)
_S5ChasComM3299_U_ObjectIdentity = ObjectIdentity
s5ChasComM3299_U = _S5ChasComM3299_U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 117)
)
_S5ChasComMDA3299_U_ObjectIdentity = ObjectIdentity
s5ChasComMDA3299_U = _S5ChasComMDA3299_U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 117, 255)
)
_S5ChasComM3299_F_ObjectIdentity = ObjectIdentity
s5ChasComM3299_F = _S5ChasComM3299_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 119)
)
_S5ChasComMDA3299_F_ObjectIdentity = ObjectIdentity
s5ChasComMDA3299_F = _S5ChasComMDA3299_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 119, 255)
)
_S5ChasComM3410_ObjectIdentity = ObjectIdentity
s5ChasComM3410 = _S5ChasComM3410_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 120)
)
_S5ChasComM3410Store_ObjectIdentity = ObjectIdentity
s5ChasComM3410Store = _S5ChasComM3410Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 120, 0)
)
_S5ChasComM3410StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM3410StoreBoot = _S5ChasComM3410StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 120, 0, 1)
)
_S5ChasComM3410StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM3410StoreFlash = _S5ChasComM3410StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 120, 0, 2)
)
_S5ChasComM3410StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComM3410StoreDram = _S5ChasComM3410StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 120, 0, 3)
)
_S5ChasComM3405Tx12_ObjectIdentity = ObjectIdentity
s5ChasComM3405Tx12 = _S5ChasComM3405Tx12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 121)
)
_S5ChasComM3405Tx12Store_ObjectIdentity = ObjectIdentity
s5ChasComM3405Tx12Store = _S5ChasComM3405Tx12Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 121, 0)
)
_S5ChasComM3405Tx12StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComM3405Tx12StoreRom = _S5ChasComM3405Tx12StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 121, 0, 1)
)
_S5ChasComM3475FxTx11_ObjectIdentity = ObjectIdentity
s5ChasComM3475FxTx11 = _S5ChasComM3475FxTx11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 122)
)
_S5ChasComM3475FxTx11Store_ObjectIdentity = ObjectIdentity
s5ChasComM3475FxTx11Store = _S5ChasComM3475FxTx11Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 122, 0)
)
_S5ChasComM3475FxTx11StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComM3475FxTx11StoreRom = _S5ChasComM3475FxTx11StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 122, 0, 1)
)
_S5ChasComM3308S_ObjectIdentity = ObjectIdentity
s5ChasComM3308S = _S5ChasComM3308S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130)
)
_S5ChasComM3308SStore_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStore = _S5ChasComM3308SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0)
)
_S5ChasComM3308SStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStoreDram = _S5ChasComM3308SStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0, 1)
)
_S5ChasComM3308SStoreFlash1_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStoreFlash1 = _S5ChasComM3308SStoreFlash1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0, 2)
)
_S5ChasComM3308SStoreFlash2_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStoreFlash2 = _S5ChasComM3308SStoreFlash2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0, 3)
)
_S5ChasComM3308SStoreFlash3_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStoreFlash3 = _S5ChasComM3308SStoreFlash3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0, 4)
)
_S5ChasComM3308SStoreFlash4_ObjectIdentity = ObjectIdentity
s5ChasComM3308SStoreFlash4 = _S5ChasComM3308SStoreFlash4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 130, 0, 5)
)
_S5ChasComM3000ASM_ObjectIdentity = ObjectIdentity
s5ChasComM3000ASM = _S5ChasComM3000ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 200)
)
_S5ChasComMDA3000ASM_ObjectIdentity = ObjectIdentity
s5ChasComMDA3000ASM = _S5ChasComMDA3000ASM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 200, 255)
)
_S5ChasComSupM5110_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110 = _S5ChasComSupM5110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258)
)
_S5ChasComSupM5110Store_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110Store = _S5ChasComSupM5110Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258, 0)
)
_S5ChasComSupM5110StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110StoreDram = _S5ChasComSupM5110StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258, 0, 1)
)
_S5ChasComSupM5110StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110StoreFlash = _S5ChasComSupM5110StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258, 0, 2)
)
_S5ChasComSupM5110StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110StoreNvram = _S5ChasComSupM5110StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258, 0, 3)
)
_S5ChasComSupM5110StoreChaEeProm_ObjectIdentity = ObjectIdentity
s5ChasComSupM5110StoreChaEeProm = _S5ChasComSupM5110StoreChaEeProm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 258, 0, 4)
)
_S5ChasComBrdM5304P_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5304P = _S5ChasComBrdM5304P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 259)
)
_S5ChasComBrdM5304PStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5304PStore = _S5ChasComBrdM5304PStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 259, 0)
)
_S5ChasComBrdM5304PStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5304PStore8051Rom = _S5ChasComBrdM5304PStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 259, 0, 1)
)
_S5ChasComBrdM5304PStoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5304PStoreDspRom = _S5ChasComBrdM5304PStoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 259, 0, 2)
)
_S5ChasComBrdM5308_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308 = _S5ChasComBrdM5308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 260)
)
_S5ChasComBrdM5308Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308Store = _S5ChasComBrdM5308Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 260, 0)
)
_S5ChasComBrdM5308Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308Store8051Rom = _S5ChasComBrdM5308Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 260, 0, 1)
)
_S5ChasComBrdM5308StoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308StoreDspRom = _S5ChasComBrdM5308StoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 260, 0, 2)
)
_S5ChasComBrdM5308AF_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308AF = _S5ChasComBrdM5308AF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 261)
)
_S5ChasComBrdM5308AFStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308AFStore = _S5ChasComBrdM5308AFStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 261, 0)
)
_S5ChasComBrdM5308AFStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308AFStore8051Rom = _S5ChasComBrdM5308AFStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 261, 0, 1)
)
_S5ChasComBrdM5308AFStoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308AFStoreDspRom = _S5ChasComBrdM5308AFStoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 261, 0, 2)
)
_S5ChasComBrdM5378F_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5378F = _S5ChasComBrdM5378F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 262)
)
_S5ChasComBrdM5378FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5378FStore = _S5ChasComBrdM5378FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 262, 0)
)
_S5ChasComBrdM5378FStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5378FStore8051Rom = _S5ChasComBrdM5378FStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 262, 0, 1)
)
_S5ChasComBrdM5378FStoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5378FStoreDspRom = _S5ChasComBrdM5378FStoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 262, 0, 2)
)
_S5ChasComBrdM5502_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5502 = _S5ChasComBrdM5502_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 263)
)
_S5ChasComBrdM5502Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5502Store = _S5ChasComBrdM5502Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 263, 0)
)
_S5ChasComBrdM5502Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5502Store8051Rom = _S5ChasComBrdM5502Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 263, 0, 1)
)
_S5ChasComBrdM5505P_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505P = _S5ChasComBrdM5505P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 264)
)
_S5ChasComBrdM5505PStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505PStore = _S5ChasComBrdM5505PStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 264, 0)
)
_S5ChasComBrdM5505PStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505PStore8051Rom = _S5ChasComBrdM5505PStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 264, 0, 1)
)
_S5ChasComBrdM5575F_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575F = _S5ChasComBrdM5575F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 265)
)
_S5ChasComBrdM5575FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575FStore = _S5ChasComBrdM5575FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 265, 0)
)
_S5ChasComBrdM5575FStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575FStore8051Rom = _S5ChasComBrdM5575FStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 265, 0, 1)
)
_S5ChasComBrdM5902_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5902 = _S5ChasComBrdM5902_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 266)
)
_S5ChasComBrdM5902Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5902Store = _S5ChasComBrdM5902Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 266, 0)
)
_S5ChasComBrdM5902StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5902StoreDram = _S5ChasComBrdM5902StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 266, 0, 1)
)
_S5ChasComBrdM5902StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5902StoreFlash = _S5ChasComBrdM5902StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 266, 0, 2)
)
_S5ChasComBrdM5902StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5902StoreNvram = _S5ChasComBrdM5902StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 266, 0, 3)
)
_S5ChasComBrdM5904_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5904 = _S5ChasComBrdM5904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 267)
)
_S5ChasComBrdM5904Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5904Store = _S5ChasComBrdM5904Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 267, 0)
)
_S5ChasComBrdM5904StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5904StoreDram = _S5ChasComBrdM5904StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 267, 0, 1)
)
_S5ChasComBrdM5904StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5904StoreFlash = _S5ChasComBrdM5904StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 267, 0, 2)
)
_S5ChasComBrdM5904StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5904StoreNvram = _S5ChasComBrdM5904StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 267, 0, 3)
)
_S5ChasComBrdM59042SM_ObjectIdentity = ObjectIdentity
s5ChasComBrdM59042SM = _S5ChasComBrdM59042SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 268)
)
_S5ChasComBrdM59042SMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM59042SMStore = _S5ChasComBrdM59042SMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 268, 0)
)
_S5ChasComBrdM59042SMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM59042SMStoreDram = _S5ChasComBrdM59042SMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 268, 0, 1)
)
_S5ChasComBrdM59042SMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM59042SMStoreFlash = _S5ChasComBrdM59042SMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 268, 0, 2)
)
_S5ChasComBrdM59042SMStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM59042SMStoreNvram = _S5ChasComBrdM59042SMStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 268, 0, 3)
)
_S5ChasComBrdM5310_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310 = _S5ChasComBrdM5310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 269)
)
_S5ChasComBrdM5310Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310Store = _S5ChasComBrdM5310Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 269, 0)
)
_S5ChasComBrdM5310StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310StoreFlash = _S5ChasComBrdM5310StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 269, 0, 2)
)
_S5ChasComBrdM5310StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310StoreDram = _S5ChasComBrdM5310StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 269, 0, 3)
)
_S5ChasComBrdM5310StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310StoreBoot = _S5ChasComBrdM5310StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 269, 1)
)
_S5ChasComBrdM5510_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5510 = _S5ChasComBrdM5510_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 270)
)
_S5ChasComBrdM5510Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5510Store = _S5ChasComBrdM5510Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 270, 0)
)
_S5ChasComBrdM5510StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5510StoreBoot = _S5ChasComBrdM5510StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 270, 0, 1)
)
_S5ChasComBrdM5510StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5510StoreFlash = _S5ChasComBrdM5510StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 270, 0, 2)
)
_S5ChasComBrdM5510StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5510StoreDram = _S5ChasComBrdM5510StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 270, 0, 3)
)
_S5ChasComBrdM5910S_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910S = _S5ChasComBrdM5910S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 271)
)
_S5ChasComBrdM5910SStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SStore = _S5ChasComBrdM5910SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 271, 0)
)
_S5ChasComBrdM5910SStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SStoreDram = _S5ChasComBrdM5910SStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 271, 0, 1)
)
_S5ChasComBrdM5910SStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SStoreFlash = _S5ChasComBrdM5910SStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 271, 0, 2)
)
_S5ChasComBrdM5910SStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SStoreNvram = _S5ChasComBrdM5910SStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 271, 0, 3)
)
_S5ChasComBrdM5910SSM_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SSM = _S5ChasComBrdM5910SSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 272)
)
_S5ChasComBrdM5910SSMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SSMStore = _S5ChasComBrdM5910SSMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 272, 0)
)
_S5ChasComBrdM5910SSMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SSMStoreDram = _S5ChasComBrdM5910SSMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 272, 0, 1)
)
_S5ChasComBrdM5910SSMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SSMStoreFlash = _S5ChasComBrdM5910SSMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 272, 0, 2)
)
_S5ChasComBrdM5910SSMStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5910SSMStoreNvram = _S5ChasComBrdM5910SSMStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 272, 0, 3)
)
_S5ChasComBrdSubM5311_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5311 = _S5ChasComBrdSubM5311_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 273)
)
_S5ChasComBrdSubM5511_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5511 = _S5ChasComBrdSubM5511_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 274)
)
_S5ChasComBrdM5905_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5905 = _S5ChasComBrdM5905_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 275)
)
_S5ChasComBrdM5905Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5905Store = _S5ChasComBrdM5905Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 275, 0)
)
_S5ChasComBrdM5905StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5905StoreDram = _S5ChasComBrdM5905StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 275, 0, 1)
)
_S5ChasComBrdM5905StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5905StoreFlash = _S5ChasComBrdM5905StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 275, 0, 2)
)
_S5ChasComBrdM5905StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5905StoreNvram = _S5ChasComBrdM5905StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 275, 0, 3)
)
_S5ChasComBrdM5575C_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575C = _S5ChasComBrdM5575C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 276)
)
_S5ChasComBrdM5575CStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575CStore = _S5ChasComBrdM5575CStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 276, 0)
)
_S5ChasComBrdM5575CStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5575CStore8051Rom = _S5ChasComBrdM5575CStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 276, 0, 1)
)
_S5ChasComBrdM559_ObjectIdentity = ObjectIdentity
s5ChasComBrdM559 = _S5ChasComBrdM559_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 277)
)
_S5ChasComBrdM5390_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5390 = _S5ChasComBrdM5390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 278)
)
_S5ChasComBrdM5390Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5390Store = _S5ChasComBrdM5390Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 278, 0)
)
_S5ChasComBrdM5390StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5390StoreDram = _S5ChasComBrdM5390StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 278, 0, 1)
)
_S5ChasComBrdM5390StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5390StoreFlash = _S5ChasComBrdM5390StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 278, 0, 2)
)
_S5ChasComBrdM5390StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5390StoreNvram = _S5ChasComBrdM5390StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 278, 0, 3)
)
_S5ChasComBrdM5307_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307 = _S5ChasComBrdM5307_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 279)
)
_S5ChasComBrdM5307Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307Store = _S5ChasComBrdM5307Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 279, 0)
)
_S5ChasComBrdM5307Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307Store8051Rom = _S5ChasComBrdM5307Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 279, 0, 1)
)
_S5ChasComBrdM5307StoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307StoreDspRom = _S5ChasComBrdM5307StoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 279, 0, 2)
)
_S5ChasComBrdMCR5308_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5308 = _S5ChasComBrdMCR5308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 280)
)
_S5ChasComBrdMCR5308Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5308Store = _S5ChasComBrdMCR5308Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 280, 0)
)
_S5ChasComBrdMCR5308Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5308Store8051Rom = _S5ChasComBrdMCR5308Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 280, 0, 1)
)
_S5ChasComBrdMCR5308StoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5308StoreDspRom = _S5ChasComBrdMCR5308StoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 280, 0, 2)
)
_S5ChasComBrdMCR5378F_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5378F = _S5ChasComBrdMCR5378F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 281)
)
_S5ChasComBrdMCR5378FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5378FStore = _S5ChasComBrdMCR5378FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 281, 0)
)
_S5ChasComBrdMCR5378FStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5378FStore8051Rom = _S5ChasComBrdMCR5378FStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 281, 0, 1)
)
_S5ChasComBrdMCR5378FStoreDspRom_ObjectIdentity = ObjectIdentity
s5ChasComBrdMCR5378FStoreDspRom = _S5ChasComBrdMCR5378FStoreDspRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 281, 0, 2)
)
_S5ChasComBrdM5505_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505 = _S5ChasComBrdM5505_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 282)
)
_S5ChasComBrdM5505Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505Store = _S5ChasComBrdM5505Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 282, 0)
)
_S5ChasComBrdM5505Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5505Store8051Rom = _S5ChasComBrdM5505Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 282, 0, 1)
)
_S5ChasComSupM5115_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115 = _S5ChasComSupM5115_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284)
)
_S5ChasComSupM5115Store_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115Store = _S5ChasComSupM5115Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284, 0)
)
_S5ChasComSupM5115StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115StoreDram = _S5ChasComSupM5115StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284, 0, 1)
)
_S5ChasComSupM5115StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115StoreFlash = _S5ChasComSupM5115StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284, 0, 2)
)
_S5ChasComSupM5115StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115StoreNvram = _S5ChasComSupM5115StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284, 0, 3)
)
_S5ChasComSupM5115StoreChaEeProm_ObjectIdentity = ObjectIdentity
s5ChasComSupM5115StoreChaEeProm = _S5ChasComSupM5115StoreChaEeProm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 284, 0, 4)
)
_S5ChasComBrdM5740_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740 = _S5ChasComBrdM5740_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285)
)
_S5ChasComBrdM5740Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740Store = _S5ChasComBrdM5740Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0)
)
_S5ChasComBrdM5740Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740Store8051Rom = _S5ChasComBrdM5740Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 1)
)
_S5ChasComBrdM5740StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740StoreBoot = _S5ChasComBrdM5740StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 2)
)
_S5ChasComBrdM5740StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740StoreDram = _S5ChasComBrdM5740StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 3)
)
_S5ChasComBrdM5740StoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740StoreNvram = _S5ChasComBrdM5740StoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 4)
)
_S5ChasComBrdM5740StoreDisk1_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740StoreDisk1 = _S5ChasComBrdM5740StoreDisk1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 5)
)
_S5ChasComBrdM5740StoreDisk2_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5740StoreDisk2 = _S5ChasComBrdM5740StoreDisk2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 285, 0, 6)
)
_S5ChasComBrdM5720_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5720 = _S5ChasComBrdM5720_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 287)
)
_S5ChasComBrdM5720Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5720Store = _S5ChasComBrdM5720Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 287, 0)
)
_S5ChasComBrdM5720Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5720Store8051Rom = _S5ChasComBrdM5720Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 287, 0, 1)
)
_S5ChasComBrdM5720StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5720StoreEprom = _S5ChasComBrdM5720StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 287, 0, 2)
)
_S5ChasComBrdM5720StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5720StoreSram = _S5ChasComBrdM5720StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 287, 0, 3)
)
_S5ChasComBrdM5700_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5700 = _S5ChasComBrdM5700_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 288)
)
_S5ChasComBrdM5700Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5700Store = _S5ChasComBrdM5700Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 288, 0)
)
_S5ChasComBrdM5700Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5700Store8051Rom = _S5ChasComBrdM5700Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 288, 0, 1)
)
_S5ChasComBrdM5700StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5700StoreEprom = _S5ChasComBrdM5700StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 288, 0, 2)
)
_S5ChasComBrdM5700StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5700StoreSram = _S5ChasComBrdM5700StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 288, 0, 3)
)
_S5ChasComBrdSubM5700_17_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5700_17 = _S5ChasComBrdSubM5700_17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 289)
)
_S5ChasComBrdSubM5700_24_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5700_24 = _S5ChasComBrdSubM5700_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 290)
)
_S5ChasComBrdSubM5700_14_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5700_14 = _S5ChasComBrdSubM5700_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 291)
)
_S5ChasComBrdSubM5700_31_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5700_31 = _S5ChasComBrdSubM5700_31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 292)
)
_S5ChasComBrdSubM5700_15_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5700_15 = _S5ChasComBrdSubM5700_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 293)
)
_S5ChasComBrdM5715_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5715 = _S5ChasComBrdM5715_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 294)
)
_S5ChasComBrdM5715Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5715Store = _S5ChasComBrdM5715Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 294, 0)
)
_S5ChasComBrdM5715Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5715Store8051Rom = _S5ChasComBrdM5715Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 294, 0, 1)
)
_S5ChasComBrdM5715StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5715StoreEprom = _S5ChasComBrdM5715StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 294, 0, 2)
)
_S5ChasComBrdM5715StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5715StoreSram = _S5ChasComBrdM5715StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 294, 0, 3)
)
_S5ChasComBrdM5714_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5714 = _S5ChasComBrdM5714_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 295)
)
_S5ChasComBrdM5714Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5714Store = _S5ChasComBrdM5714Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 295, 0)
)
_S5ChasComBrdM5714Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5714Store8051Rom = _S5ChasComBrdM5714Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 295, 0, 1)
)
_S5ChasComBrdM5714StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5714StoreEprom = _S5ChasComBrdM5714StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 295, 0, 2)
)
_S5ChasComBrdM5714StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5714StoreSram = _S5ChasComBrdM5714StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 295, 0, 3)
)
_S5ChasComBrdM5328_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328 = _S5ChasComBrdM5328_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 296)
)
_S5ChasComBrdM5328Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328Store = _S5ChasComBrdM5328Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 296, 0)
)
_S5ChasComBrdM5328Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328Store8051Rom = _S5ChasComBrdM5328Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 296, 0, 1)
)
_S5ChasComBrdM5328StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328StoreEprom = _S5ChasComBrdM5328StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 296, 0, 2)
)
_S5ChasComBrdM5328StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328StoreSram = _S5ChasComBrdM5328StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 296, 0, 3)
)
_S5ChasComBrdM5324_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5324 = _S5ChasComBrdM5324_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 297)
)
_S5ChasComBrdM5324Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5324Store = _S5ChasComBrdM5324Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 297, 0)
)
_S5ChasComBrdM5324Store8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5324Store8051Rom = _S5ChasComBrdM5324Store8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 297, 0, 1)
)
_S5ChasComBrdM5324StoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5324StoreEprom = _S5ChasComBrdM5324StoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 297, 0, 2)
)
_S5ChasComBrdM5324StoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5324StoreSram = _S5ChasComBrdM5324StoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 297, 0, 3)
)
_S5ChasComBrdM10328F_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328F = _S5ChasComBrdM10328F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298)
)
_S5ChasComBrdM10328FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStore = _S5ChasComBrdM10328FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0)
)
_S5ChasComBrdM10328FStoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStoreSram = _S5ChasComBrdM10328FStoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0, 1)
)
_S5ChasComBrdM10328FStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStoreDram = _S5ChasComBrdM10328FStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0, 2)
)
_S5ChasComBrdM10328FStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStoreNvram = _S5ChasComBrdM10328FStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0, 3)
)
_S5ChasComBrdM10328FStoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStoreEprom = _S5ChasComBrdM10328FStoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0, 4)
)
_S5ChasComBrdM10328FStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328FStoreFlash = _S5ChasComBrdM10328FStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 298, 0, 5)
)
_S5ChasComBrdM10328SM_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SM = _S5ChasComBrdM10328SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301)
)
_S5ChasComBrdM10328SMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStore = _S5ChasComBrdM10328SMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0)
)
_S5ChasComBrdM10328SMStoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStoreSram = _S5ChasComBrdM10328SMStoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0, 1)
)
_S5ChasComBrdM10328SMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStoreDram = _S5ChasComBrdM10328SMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0, 2)
)
_S5ChasComBrdM10328SMStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStoreNvram = _S5ChasComBrdM10328SMStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0, 3)
)
_S5ChasComBrdM10328SMStoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStoreEprom = _S5ChasComBrdM10328SMStoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0, 4)
)
_S5ChasComBrdM10328SMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10328SMStoreFlash = _S5ChasComBrdM10328SMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 301, 0, 5)
)
_S5ChasComBrdM10324F_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324F = _S5ChasComBrdM10324F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302)
)
_S5ChasComBrdM10324FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStore = _S5ChasComBrdM10324FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0)
)
_S5ChasComBrdM10324FStoreSram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStoreSram = _S5ChasComBrdM10324FStoreSram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0, 1)
)
_S5ChasComBrdM10324FStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStoreDram = _S5ChasComBrdM10324FStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0, 2)
)
_S5ChasComBrdM10324FStoreNvram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStoreNvram = _S5ChasComBrdM10324FStoreNvram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0, 3)
)
_S5ChasComBrdM10324FStoreEprom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStoreEprom = _S5ChasComBrdM10324FStoreEprom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0, 4)
)
_S5ChasComBrdM10324FStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM10324FStoreFlash = _S5ChasComBrdM10324FStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 302, 0, 5)
)
_S5ChasComBrdM5308P_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308P = _S5ChasComBrdM5308P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 306)
)
_S5ChasComBrdM5308PStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308PStore = _S5ChasComBrdM5308PStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 306, 0)
)
_S5ChasComBrdM5308PStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308PStore8051Rom = _S5ChasComBrdM5308PStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 306, 0, 1)
)
_S5ChasComBrdM5310ASA_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310ASA = _S5ChasComBrdM5310ASA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 317)
)
_S5ChasComBrdM5310ASAStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310ASAStore = _S5ChasComBrdM5310ASAStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 317, 0)
)
_S5ChasComBrdM5310ASAStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310ASAStoreBoot = _S5ChasComBrdM5310ASAStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 317, 0, 1)
)
_S5ChasComBrdM5310ASAStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310ASAStoreFlash = _S5ChasComBrdM5310ASAStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 317, 0, 2)
)
_S5ChasComBrdM5310ASAStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5310ASAStoreDram = _S5ChasComBrdM5310ASAStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 317, 0, 3)
)
_S5ChasComBrdSubMMCE_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubMMCE = _S5ChasComBrdSubMMCE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 318)
)
_S5ChasComBrdSubM5740AtmBkplIntf_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5740AtmBkplIntf = _S5ChasComBrdSubM5740AtmBkplIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 319)
)
_S5ChasComM5DN002m_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002m = _S5ChasComM5DN002m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 342)
)
_S5ChasComM5DN002mStore_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002mStore = _S5ChasComM5DN002mStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 342, 0)
)
_S5ChasComM5DN002mStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002mStoreFlash = _S5ChasComM5DN002mStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 342, 0, 1)
)
_S5ChasComM5DN002mStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002mStoreBoot = _S5ChasComM5DN002mStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 342, 0, 2)
)
_S5ChasComM5DN003m_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003m = _S5ChasComM5DN003m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 343)
)
_S5ChasComM5DN003mStore_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003mStore = _S5ChasComM5DN003mStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 343, 0)
)
_S5ChasComM5DN003mStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003mStoreFlash = _S5ChasComM5DN003mStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 343, 0, 1)
)
_S5ChasComM5DN003mStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003mStoreBoot = _S5ChasComM5DN003mStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 343, 0, 2)
)
_S5ChasComM5DN308P_ObjectIdentity = ObjectIdentity
s5ChasComM5DN308P = _S5ChasComM5DN308P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 344)
)
_S5ChasComM5DN304P_ObjectIdentity = ObjectIdentity
s5ChasComM5DN304P = _S5ChasComM5DN304P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 345)
)
_S5ChasComM5DN378P_F_ObjectIdentity = ObjectIdentity
s5ChasComM5DN378P_F = _S5ChasComM5DN378P_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 346)
)
_S5ChasComM5DN307P_ObjectIdentity = ObjectIdentity
s5ChasComM5DN307P = _S5ChasComM5DN307P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 347)
)
_S5ChasComM5DN310_ObjectIdentity = ObjectIdentity
s5ChasComM5DN310 = _S5ChasComM5DN310_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 348)
)
_S5ChasComM5DN310Store_ObjectIdentity = ObjectIdentity
s5ChasComM5DN310Store = _S5ChasComM5DN310Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 348, 0)
)
_S5ChasComM5DN310StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM5DN310StoreBoot = _S5ChasComM5DN310StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 348, 0, 1)
)
_S5ChasComM5DN310StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5DN310StoreFlash = _S5ChasComM5DN310StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 348, 0, 2)
)
_S5ChasComM5DN310StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComM5DN310StoreDram = _S5ChasComM5DN310StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 348, 0, 3)
)
_S5ChasComMN11_ObjectIdentity = ObjectIdentity
s5ChasComMN11 = _S5ChasComMN11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 349)
)
_S5ChasComMN11Store_ObjectIdentity = ObjectIdentity
s5ChasComMN11Store = _S5ChasComMN11Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 349, 0)
)
_S5ChasComMN11StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMN11StoreFlash = _S5ChasComMN11StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 349, 0, 1)
)
_S5ChasComMN11StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComMN11StoreDram = _S5ChasComMN11StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 349, 0, 2)
)
_S5ChasComMNBayStackm1_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm1 = _S5ChasComMNBayStackm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 350)
)
_S5ChasComMNBayStackm1Store_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm1Store = _S5ChasComMNBayStackm1Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 350, 0)
)
_S5ChasComMNBayStackm1StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm1StoreRom = _S5ChasComMNBayStackm1StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 350, 0, 1)
)
_S5ChasComMNBayStackm2_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm2 = _S5ChasComMNBayStackm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 351)
)
_S5ChasComMNBayStackm2Store_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm2Store = _S5ChasComMNBayStackm2Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 351, 0)
)
_S5ChasComMNBayStackm2StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm2StoreRom = _S5ChasComMNBayStackm2StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 351, 0, 1)
)
_S5ChasComMNBayStackAui_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAui = _S5ChasComMNBayStackAui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 352)
)
_S5ChasComMNBayStackThin_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackThin = _S5ChasComMNBayStackThin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 353)
)
_S5ChasComMNBayStackFL_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackFL = _S5ChasComMNBayStackFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 354)
)
_S5ChasComMNBayStackStdNmm_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackStdNmm = _S5ChasComMNBayStackStdNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 355)
)
_S5ChasComMNBayStackStdNmmStore_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackStdNmmStore = _S5ChasComMNBayStackStdNmmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 355, 0)
)
_S5ChasComMNBayStackStdnmmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackStdnmmStoreBoot = _S5ChasComMNBayStackStdnmmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 355, 0, 1)
)
_S5ChasComMNBayStackStdNmmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackStdNmmStoreFlash = _S5ChasComMNBayStackStdNmmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 355, 0, 2)
)
_S5ChasComMNBayStackStdNmmStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackStdNmmStoreDram = _S5ChasComMNBayStackStdNmmStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 355, 0, 3)
)
_S5ChasComMNBayStackAdvNmm_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAdvNmm = _S5ChasComMNBayStackAdvNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 356)
)
_S5ChasComMNBayStackAdvNmmStore_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAdvNmmStore = _S5ChasComMNBayStackAdvNmmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 356, 0)
)
_S5ChasComMNBayStackAdvNmmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAdvNmmStoreBoot = _S5ChasComMNBayStackAdvNmmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 356, 0, 1)
)
_S5ChasComMNBayStackAdvNmmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAdvNmmStoreFlash = _S5ChasComMNBayStackAdvNmmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 356, 0, 2)
)
_S5ChasComMNBayStackAdvNmmStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackAdvNmmStoreDram = _S5ChasComMNBayStackAdvNmmStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 356, 0, 3)
)
_S5ChasComMF_10BaseT_ObjectIdentity = ObjectIdentity
s5ChasComMF_10BaseT = _S5ChasComMF_10BaseT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 357)
)
_S5ChasComBrdM58000_ObjectIdentity = ObjectIdentity
s5ChasComBrdM58000 = _S5ChasComBrdM58000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 359)
)
_S5ChasComBrdM58000Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM58000Store = _S5ChasComBrdM58000Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 359, 0)
)
_S5ChasComBrdM58000StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM58000StoreBoot = _S5ChasComBrdM58000StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 359, 0, 1)
)
_S5ChasComBrdM58000StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM58000StoreFlash = _S5ChasComBrdM58000StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 359, 0, 2)
)
_S5ChasComBrdSubM5800014_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5800014 = _S5ChasComBrdSubM5800014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 360)
)
_S5ChasComBrdSubM5800015_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5800015 = _S5ChasComBrdSubM5800015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 361)
)
_S5ChasComBrdSubM5800016_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM5800016 = _S5ChasComBrdSubM5800016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 362)
)
_S5ChasComBrdSubM58000MdaExp_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM58000MdaExp = _S5ChasComBrdSubM58000MdaExp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 363)
)
_S5ChasComM5DN378P_A_ObjectIdentity = ObjectIdentity
s5ChasComM5DN378P_A = _S5ChasComM5DN378P_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 364)
)
_S5ChasComMBayStack100m1_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100m1 = _S5ChasComMBayStack100m1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 365)
)
_S5ChasComMBayStack100m1Store_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100m1Store = _S5ChasComMBayStack100m1Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 365, 0)
)
_S5ChasComMBayStack100m1StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100m1StoreRom = _S5ChasComMBayStack100m1StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 365, 0, 1)
)
_S5ChasComMBayStack100Nmm_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100Nmm = _S5ChasComMBayStack100Nmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 366)
)
_S5ChasComMBayStack100NmmStore_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100NmmStore = _S5ChasComMBayStack100NmmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 366, 0)
)
_S5ChasComMBayStack100NmmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100NmmStoreBoot = _S5ChasComMBayStack100NmmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 366, 0, 1)
)
_S5ChasComMBayStack100NmmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100NmmStoreFlash = _S5ChasComMBayStack100NmmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 366, 0, 2)
)
_S5ChasComMBayStack100NmmStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100NmmStoreDram = _S5ChasComMBayStack100NmmStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 366, 0, 3)
)
_S5ChasComMBayStack100_FxMda_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100_FxMda = _S5ChasComMBayStack100_FxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 368)
)
_S5ChasComMBayStack100_TxMda_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100_TxMda = _S5ChasComMBayStack100_TxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 369)
)
_S5ChasComMBayStack100_Tx12_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100_Tx12 = _S5ChasComMBayStack100_Tx12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 371)
)
_S5ChasComM5DN301P_ObjectIdentity = ObjectIdentity
s5ChasComM5DN301P = _S5ChasComM5DN301P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 372)
)
_S5ChasComBrdM5307PS_HD_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PS_HD = _S5ChasComBrdM5307PS_HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 373)
)
_S5ChasComBrdM5307PS_HDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PS_HDStore = _S5ChasComBrdM5307PS_HDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 373, 0)
)
_S5ChasComBrdM5307PS_HDStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PS_HDStore8051Rom = _S5ChasComBrdM5307PS_HDStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 373, 0, 1)
)
_S5ChasComBrdM5300P_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5300P = _S5ChasComBrdM5300P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 374)
)
_S5ChasComBrdM5300PStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5300PStore = _S5ChasComBrdM5300PStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 374, 0)
)
_S5ChasComBrdM5300PStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5300PStore8051Rom = _S5ChasComBrdM5300PStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 374, 0, 1)
)
_S5ChasComMod_5328mEther16PC10BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_5328mEther16PC10BT = _S5ChasComMod_5328mEther16PC10BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 375)
)
_S5ChasComMod_5724mATM4PMMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5724mATM4PMMFiber = _S5ChasComMod_5724mATM4PMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 376)
)
_S5ChasComMod_5724MmATMMCP4PMMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5724MmATMMCP4PMMFiber = _S5ChasComMod_5724MmATMMCP4PMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 377)
)
_S5ChasComMod_5328MmEtherMCP8PC10BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_5328MmEtherMCP8PC10BT = _S5ChasComMod_5328MmEtherMCP8PC10BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 378)
)
_S5ChasComMod_5328FXmEther12P2FXP_ObjectIdentity = ObjectIdentity
s5ChasComMod_5328FXmEther12P2FXP = _S5ChasComMod_5328FXmEther12P2FXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 379)
)
_S5ChasComMod_5324mEther12PFL_ObjectIdentity = ObjectIdentity
s5ChasComMod_5324mEther12PFL = _S5ChasComMod_5324mEther12PFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 380)
)
_S5ChasComMod_5525mTR8PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_5525mTR8PCopper = _S5ChasComMod_5525mTR8PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 381)
)
_S5ChasComMod_5525MmTRMCP4PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_5525MmTRMCP4PCopper = _S5ChasComMod_5525MmTRMCP4PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 382)
)
_S5ChasComMod_5524mTR8PFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5524mTR8PFiber = _S5ChasComMod_5524mTR8PFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 383)
)
_S5ChasComMod_5524MmTR4PFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5524MmTR4PFiber = _S5ChasComMod_5524MmTR4PFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 384)
)
_S5ChasComMod_5924mFDDI1P_ObjectIdentity = ObjectIdentity
s5ChasComMod_5924mFDDI1P = _S5ChasComMod_5924mFDDI1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 385)
)
_S5ChasComMod_5824mEther4PFX_ObjectIdentity = ObjectIdentity
s5ChasComMod_5824mEther4PFX = _S5ChasComMod_5824mEther4PFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 386)
)
_S5ChasComMod_5828FmEther2PTX2PFX_ObjectIdentity = ObjectIdentity
s5ChasComMod_5828FmEther2PTX2PFX = _S5ChasComMod_5828FmEther2PTX2PFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 387)
)
_S5ChasComMod_5824MmEtherMCP2PFX_ObjectIdentity = ObjectIdentity
s5ChasComMod_5824MmEtherMCP2PFX = _S5ChasComMod_5824MmEtherMCP2PFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 388)
)
_S5ChasComMod_5724SMmATM4PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5724SMmATM4PSMFiber = _S5ChasComMod_5724SMmATM4PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 389)
)
_S5ChasComMod_5725mATM4PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_5725mATM4PCopper = _S5ChasComMod_5725mATM4PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 390)
)
_S5ChasComMod_5721DS3mATM2P_ObjectIdentity = ObjectIdentity
s5ChasComMod_5721DS3mATM2P = _S5ChasComMod_5721DS3mATM2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 391)
)
_S5ChasComMod_5721E3mATM2P_ObjectIdentity = ObjectIdentity
s5ChasComMod_5721E3mATM2P = _S5ChasComMod_5721E3mATM2P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 392)
)
_S5ChasComMod_5380E4Bkp2N_ObjectIdentity = ObjectIdentity
s5ChasComMod_5380E4Bkp2N = _S5ChasComMod_5380E4Bkp2N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 395)
)
_S5ChasComMod_5380TR4Bkp2N_ObjectIdentity = ObjectIdentity
s5ChasComMod_5380TR4Bkp2N = _S5ChasComMod_5380TR4Bkp2N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 396)
)
_S5ChasComMod_5000ENetD10_T_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ENetD10_T = _S5ChasComMod_5000ENetD10_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 397)
)
_S5ChasComMod_5000ENetS100_T_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ENetS100_T = _S5ChasComMod_5000ENetS100_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 398)
)
_S5ChasComMod_5000TRNetD_DB9_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000TRNetD_DB9 = _S5ChasComMod_5000TRNetD_DB9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 399)
)
_S5ChasComMod_5000MMFibNetD_DASMIC_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000MMFibNetD_DASMIC = _S5ChasComMod_5000MMFibNetD_DASMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 400)
)
_S5ChasComMod_5000SMFibNetS_DASMIC_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000SMFibNetS_DASMIC = _S5ChasComMod_5000SMFibNetS_DASMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 401)
)
_S5ChasComMod_5000SMMMFibNetS_DASMIC_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000SMMMFibNetS_DASMIC = _S5ChasComMod_5000SMMMFibNetS_DASMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 402)
)
_S5ChasComMod_5000MMSMFibNetS_DASMIC_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000MMSMFibNetS_DASMIC = _S5ChasComMod_5000MMSMFibNetS_DASMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 403)
)
_S5ChasComMod_5000SynNetD_WAN44_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000SynNetD_WAN44 = _S5ChasComMod_5000SynNetD_WAN44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 404)
)
_S5ChasComMod_5000SynNetQ_ISDNBRI8_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000SynNetQ_ISDNBRI8 = _S5ChasComMod_5000SynNetQ_ISDNBRI8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 405)
)
_S5ChasComMod_5000MCE1NetQ_75120_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000MCE1NetQ_75120 = _S5ChasComMod_5000MCE1NetQ_75120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 406)
)
_S5ChasComMod_5000MCT1NetQ_RJ48C_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000MCT1NetQ_RJ48C = _S5ChasComMod_5000MCT1NetQ_RJ48C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 407)
)
_S5ChasComMod_5000SynNet4_50Pin_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000SynNet4_50Pin = _S5ChasComMod_5000SynNet4_50Pin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 408)
)
_S5ChasComMod_5000Co_Processor_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000Co_Processor = _S5ChasComMod_5000Co_Processor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 409)
)
_S5ChasComMod_5000ATMNet1_MMOC3_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ATMNet1_MMOC3 = _S5ChasComMod_5000ATMNet1_MMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 410)
)
_S5ChasComMod_5000ATMNet1_SMOC3_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ATMNet1_SMOC3 = _S5ChasComMod_5000ATMNet1_SMOC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 411)
)
_S5ChasComMod_5000ATMNet1_DS3_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ATMNet1_DS3 = _S5ChasComMod_5000ATMNet1_DS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 412)
)
_S5ChasComMod_5000ATMNet1_E3_ObjectIdentity = ObjectIdentity
s5ChasComMod_5000ATMNet1_E3 = _S5ChasComMod_5000ATMNet1_E3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 413)
)
_S5ChasComBrdSubM58000Fddi_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM58000Fddi = _S5ChasComBrdSubM58000Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 414)
)
_S5ChasComBrdM28200_ObjectIdentity = ObjectIdentity
s5ChasComBrdM28200 = _S5ChasComBrdM28200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 415)
)
_S5ChasComBrdM28200Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM28200Store = _S5ChasComBrdM28200Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 415, 0)
)
_S5ChasComBrdM28200StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM28200StoreBoot = _S5ChasComBrdM28200StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 415, 0, 1)
)
_S5ChasComBrdM28200StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM28200StoreFlash = _S5ChasComBrdM28200StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 415, 0, 2)
)
_S5ChasComBrdM28200StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM28200StoreDram = _S5ChasComBrdM28200StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 415, 0, 3)
)
_S5ChasComBrdSubM2820015_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM2820015 = _S5ChasComBrdSubM2820015_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 416)
)
_S5ChasComBrdSubM2820014_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM2820014 = _S5ChasComBrdSubM2820014_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 417)
)
_S5ChasComBrdSubM28200105_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200105 = _S5ChasComBrdSubM28200105_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 418)
)
_S5ChasComBrdSubM28200104_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200104 = _S5ChasComBrdSubM28200104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 419)
)
_S5ChasComBrdSubM28200106_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200106 = _S5ChasComBrdSubM28200106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 420)
)
_S5ChasComBrdSubM28200Exp_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200Exp = _S5ChasComBrdSubM28200Exp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 421)
)
_S5ChasComBrdSubM28200Atm_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200Atm = _S5ChasComBrdSubM28200Atm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 422)
)
_S5ChasComBrdSubM28200Fddi_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200Fddi = _S5ChasComBrdSubM28200Fddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 423)
)
_S5ChasComBrdSubM28200N11_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200N11 = _S5ChasComBrdSubM28200N11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 424)
)
_S5ChasComBrdSubM28200N111_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubM28200N111 = _S5ChasComBrdSubM28200N111_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 425)
)
_S5ChasComMod_c100mTR4PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mTR4PC = _S5ChasComMod_c100mTR4PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 426)
)
_S5ChasComMod_c100mTRMCP4PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mTRMCP4PC = _S5ChasComMod_c100mTRMCP4PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 427)
)
_S5ChasComMod_c100mATM_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM = _S5ChasComMod_c100mATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 428)
)
_S5ChasComMod_c100mTRFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mTRFiber = _S5ChasComMod_c100mTRFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 429)
)
_S5ChasComMod_c100mTRMCPFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mTRMCPFiber = _S5ChasComMod_c100mTRMCPFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 430)
)
_S5ChasComMod_c100mEther16PC10BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther16PC10BT = _S5ChasComMod_c100mEther16PC10BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 431)
)
_S5ChasComMod_c100mEtherMCP8PC10BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEtherMCP8PC10BT = _S5ChasComMod_c100mEtherMCP8PC10BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 432)
)
_S5ChasComMod_c100mATM2PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM2PSMFiber = _S5ChasComMod_c100mATM2PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 433)
)
_S5ChasComMod_c100mATM2PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM2PCopper = _S5ChasComMod_c100mATM2PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 434)
)
_S5ChasComMod_c100mATM4PMMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM4PMMFiber = _S5ChasComMod_c100mATM4PMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 435)
)
_S5ChasComMod_c100mATM4PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM4PSMFiber = _S5ChasComMod_c100mATM4PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 436)
)
_S5ChasComMod_c100mATM4PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM4PCopper = _S5ChasComMod_c100mATM4PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 437)
)
_S5ChasComMod_c100mATMMCP2PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP2PSMFiber = _S5ChasComMod_c100mATMMCP2PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 438)
)
_S5ChasComMod_c100mATMMCP2PMMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP2PMMFiber = _S5ChasComMod_c100mATMMCP2PMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 439)
)
_S5ChasComMod_c100mATMMCP2PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP2PCopper = _S5ChasComMod_c100mATMMCP2PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 440)
)
_S5ChasComMod_c100mATMMCP4PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP4PSMFiber = _S5ChasComMod_c100mATMMCP4PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 441)
)
_S5ChasComMod_c100mATMMCP4PMMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP4PMMFiber = _S5ChasComMod_c100mATMMCP4PMMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 442)
)
_S5ChasComMod_c100mATMMCP4PCopper_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP4PCopper = _S5ChasComMod_c100mATMMCP4PCopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 443)
)
_S5ChasComMod_c100mATM2PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM2PC = _S5ChasComMod_c100mATM2PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 444)
)
_S5ChasComMod_c100mATM4PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATM4PC = _S5ChasComMod_c100mATM4PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 445)
)
_S5ChasComMod_c100mATMMCP2PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP2PC = _S5ChasComMod_c100mATMMCP2PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 446)
)
_S5ChasComMod_c100mATMMCP4PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mATMMCP4PC = _S5ChasComMod_c100mATMMCP4PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 447)
)
_S5ChasComBrdSubDummy_ObjectIdentity = ObjectIdentity
s5ChasComBrdSubDummy = _S5ChasComBrdSubDummy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 448)
)
_S5ChasComBrdSub5300_T_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_T = _S5ChasComBrdSub5300_T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 449)
)
_S5ChasComBrdSub5300_A_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_A = _S5ChasComBrdSub5300_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 450)
)
_S5ChasComBrdSub5300_D_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_D = _S5ChasComBrdSub5300_D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 451)
)
_S5ChasComBrdSub5300_F_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_F = _S5ChasComBrdSub5300_F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 452)
)
_S5ChasComBrdSub5300_S_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_S = _S5ChasComBrdSub5300_S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 453)
)
_S5ChasComBrdSub5300_2_ObjectIdentity = ObjectIdentity
s5ChasComBrdSub5300_2 = _S5ChasComBrdSub5300_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 454)
)
_S5ChasComMBayStackTrm1_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrm1 = _S5ChasComMBayStackTrm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 456)
)
_S5ChasComMBayStackTrm1Store_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrm1Store = _S5ChasComMBayStackTrm1Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 456, 0)
)
_S5ChasComMBayStackTrm1StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrm1StoreFlash = _S5ChasComMBayStackTrm1StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 456, 0, 1)
)
_S5ChasComMBayStackTrm1StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrm1StoreBoot = _S5ChasComMBayStackTrm1StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 456, 0, 2)
)
_S5ChasComMBayStackTrNmm_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrNmm = _S5ChasComMBayStackTrNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 457)
)
_S5ChasComMBayStackTrNmmStore_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrNmmStore = _S5ChasComMBayStackTrNmmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 457, 0)
)
_S5ChasComMBayStackTrNmmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrNmmStoreBoot = _S5ChasComMBayStackTrNmmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 457, 0, 1)
)
_S5ChasComMBayStackTrNmmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrNmmStoreFlash = _S5ChasComMBayStackTrNmmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 457, 0, 2)
)
_S5ChasComMBayStackTrNmmStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrNmmStoreDram = _S5ChasComMBayStackTrNmmStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 457, 0, 3)
)
_S5ChasComMBayStackTrMDAFiber_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrMDAFiber = _S5ChasComMBayStackTrMDAFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 458)
)
_S5ChasComMBayStackTrMDACopper_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrMDACopper = _S5ChasComMBayStackTrMDACopper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 459)
)
_S5ChasComMBayStackTrDCM_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrDCM = _S5ChasComMBayStackTrDCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 460)
)
_S5ChasComMBayStackTrMRM_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrMRM = _S5ChasComMBayStackTrMRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 461)
)
_S5ChasComMNBayStackm3_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm3 = _S5ChasComMNBayStackm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 462)
)
_S5ChasComMNBayStackm3Store_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm3Store = _S5ChasComMNBayStackm3Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 462, 0)
)
_S5ChasComMNBayStackm3StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm3StoreRom = _S5ChasComMNBayStackm3StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 462, 0, 1)
)
_S5ChasComMNBayStackm4_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm4 = _S5ChasComMNBayStackm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 463)
)
_S5ChasComMNBayStackm4Store_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm4Store = _S5ChasComMNBayStackm4Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 463, 0)
)
_S5ChasComMNBayStackm4StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm4StoreRom = _S5ChasComMNBayStackm4StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 463, 0, 1)
)
_S5ChasComMNBayStackRedFL_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackRedFL = _S5ChasComMNBayStackRedFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 464)
)
_S5ChasComMNBayStackSMFL_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackSMFL = _S5ChasComMNBayStackSMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 465)
)
_S5ChasComMNBayStackSMRedFL_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackSMRedFL = _S5ChasComMNBayStackSMRedFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 466)
)
_S5ChasComBrdM5308S_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308S = _S5ChasComBrdM5308S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 467)
)
_S5ChasComBrdM5308SStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308SStore = _S5ChasComBrdM5308SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 467, 0)
)
_S5ChasComBrdM5308SStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308SStore8051Rom = _S5ChasComBrdM5308SStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 467, 0, 1)
)
_S5ChasComBrdM5307S_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307S = _S5ChasComBrdM5307S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 468)
)
_S5ChasComBrdM5307SStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307SStore = _S5ChasComBrdM5307SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 468, 0)
)
_S5ChasComBrdM5307SStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307SStore8051Rom = _S5ChasComBrdM5307SStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 468, 0, 1)
)
_S5ChasComBrdM5308PS_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308PS = _S5ChasComBrdM5308PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 469)
)
_S5ChasComBrdM5308PSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308PSStore = _S5ChasComBrdM5308PSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 469, 0)
)
_S5ChasComBrdM5308PSStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5308PSStore8051Rom = _S5ChasComBrdM5308PSStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 469, 0, 1)
)
_S5ChasComBrdM5307PS_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PS = _S5ChasComBrdM5307PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 470)
)
_S5ChasComBrdM5307PSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PSStore = _S5ChasComBrdM5307PSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 470, 0)
)
_S5ChasComBrdM5307PSStore8051Rom_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5307PSStore8051Rom = _S5ChasComBrdM5307PSStore8051Rom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 470, 0, 1)
)
_S5ChasComM5DN308PS_ObjectIdentity = ObjectIdentity
s5ChasComM5DN308PS = _S5ChasComM5DN308PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 471)
)
_S5ChasComM5DN307PS_ObjectIdentity = ObjectIdentity
s5ChasComM5DN307PS = _S5ChasComM5DN307PS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 472)
)
_S5ChasComM5DN378P_SM_ObjectIdentity = ObjectIdentity
s5ChasComM5DN378P_SM = _S5ChasComM5DN378P_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 473)
)
_S5ChasComMNBayStackm5_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm5 = _S5ChasComMNBayStackm5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 477)
)
_S5ChasComMNBayStackm5Store_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm5Store = _S5ChasComMNBayStackm5Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 477, 0)
)
_S5ChasComMNBayStackm5StoreRom_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackm5StoreRom = _S5ChasComMNBayStackm5StoreRom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 477, 0, 1)
)
_S5ChasComMBayStack301_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301 = _S5ChasComMBayStack301_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 478)
)
_S5ChasComMBayStack301Store_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301Store = _S5ChasComMBayStack301Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 478, 0)
)
_S5ChasComMBayStack301MaxRAM_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301MaxRAM = _S5ChasComMBayStack301MaxRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 478, 0, 1)
)
_S5ChasComMBayStack301InstalledRAM_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301InstalledRAM = _S5ChasComMBayStack301InstalledRAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 478, 0, 2)
)
_S5ChasComMBayStack301Flash_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301Flash = _S5ChasComMBayStack301Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 478, 0, 3)
)
_S5ChasComM5DN003Am_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003Am = _S5ChasComM5DN003Am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 485)
)
_S5ChasComM5DN003AmStore_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003AmStore = _S5ChasComM5DN003AmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 485, 0)
)
_S5ChasComM5DN003AmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003AmStoreFlash = _S5ChasComM5DN003AmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 485, 0, 1)
)
_S5ChasComM5DN003AmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003AmStoreBoot = _S5ChasComM5DN003AmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 485, 0, 2)
)
_S5ChasComM5DN002Am_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002Am = _S5ChasComM5DN002Am_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 486)
)
_S5ChasComM5DN002AmStore_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002AmStore = _S5ChasComM5DN002AmStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 486, 0)
)
_S5ChasComM5DN002AmStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002AmStoreFlash = _S5ChasComM5DN002AmStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 486, 0, 1)
)
_S5ChasComM5DN002AmStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002AmStoreBoot = _S5ChasComM5DN002AmStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 486, 0, 2)
)
_S5ChasComBrdM5405_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5405 = _S5ChasComBrdM5405_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 500)
)
_S5ChasComBrdM5405Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5405Store = _S5ChasComBrdM5405Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 500, 0)
)
_S5ChasComBrdM5405StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5405StoreBoot = _S5ChasComBrdM5405StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 500, 0, 1)
)
_S5ChasComBrdM5405StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5405StoreFlash = _S5ChasComBrdM5405StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 500, 0, 2)
)
_S5ChasComBrdM5405StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5405StoreDram = _S5ChasComBrdM5405StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 500, 0, 3)
)
_S5ChasComBrdM5475FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5475FX = _S5ChasComBrdM5475FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 501)
)
_S5ChasComBrdM5475FXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5475FXStore = _S5ChasComBrdM5475FXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 501, 0)
)
_S5ChasComBrdM5475FXStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5475FXStoreBoot = _S5ChasComBrdM5475FXStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 501, 0, 1)
)
_S5ChasComBrdM5475FXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5475FXStoreFlash = _S5ChasComBrdM5475FXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 501, 0, 2)
)
_S5ChasComBrdM5475FXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5475FXStoreDram = _S5ChasComBrdM5475FXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 501, 0, 3)
)
_S5ChasComMod_c100mEther12P2FXP_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther12P2FXP = _S5ChasComMod_c100mEther12P2FXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 507)
)
_S5ChasComMod_c100mEther14P2TXP_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther14P2TXP = _S5ChasComMod_c100mEther14P2TXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 508)
)
_S5ChasComBrdM5605P_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5605P = _S5ChasComBrdM5605P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 510)
)
_S5ChasComBrdM5605PStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5605PStore = _S5ChasComBrdM5605PStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 510, 0)
)
_S5ChasComBrdM5605PStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5605PStoreBoot = _S5ChasComBrdM5605PStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 510, 0, 1)
)
_S5ChasComBrdM5605PStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5605PStoreFlash = _S5ChasComBrdM5605PStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 510, 0, 2)
)
_S5ChasComBrdM5605PStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5605PStoreDram = _S5ChasComBrdM5605PStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 510, 0, 3)
)
_S5ChasComBrdM5675PFX_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5675PFX = _S5ChasComBrdM5675PFX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 511)
)
_S5ChasComBrdM5675PFXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5675PFXStore = _S5ChasComBrdM5675PFXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 511, 0)
)
_S5ChasComBrdM5675PFXStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5675PFXStoreBoot = _S5ChasComBrdM5675PFXStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 511, 0, 1)
)
_S5ChasComBrdM5675PFXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5675PFXStoreFlash = _S5ChasComBrdM5675PFXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 511, 0, 2)
)
_S5ChasComBrdM5675PFXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5675PFXStoreDram = _S5ChasComBrdM5675PFXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 511, 0, 3)
)
_S5ChasComBrdM5616_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5616 = _S5ChasComBrdM5616_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 512)
)
_S5ChasComBrdM5616Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5616Store = _S5ChasComBrdM5616Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 512, 0)
)
_S5ChasComBrdM5616StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5616StoreFlash = _S5ChasComBrdM5616StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 512, 0, 2)
)
_S5ChasComBrdM5616StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5616StoreDram = _S5ChasComBrdM5616StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 512, 0, 3)
)
_S5ChasComBrdM5616StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5616StoreBoot = _S5ChasComBrdM5616StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 512, 1)
)
_S5ChasComBrdM5316_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5316 = _S5ChasComBrdM5316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 513)
)
_S5ChasComBrdM5316Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5316Store = _S5ChasComBrdM5316Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 513, 0)
)
_S5ChasComBrdM5316StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5316StoreFlash = _S5ChasComBrdM5316StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 513, 0, 2)
)
_S5ChasComBrdM5316StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5316StoreDram = _S5ChasComBrdM5316StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 513, 0, 3)
)
_S5ChasComBrdM5316StoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5316StoreBoot = _S5ChasComBrdM5316StoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 513, 1)
)
_S5ChasComM3308S_FxMda_ObjectIdentity = ObjectIdentity
s5ChasComM3308S_FxMda = _S5ChasComM3308S_FxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 514)
)
_S5ChasComBrdBayStack302T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302T = _S5ChasComBrdBayStack302T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 515)
)
_S5ChasComBrdBayStack302TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302TStore = _S5ChasComBrdBayStack302TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 515, 0)
)
_S5ChasComBrdBayStack302TFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302TFlash = _S5ChasComBrdBayStack302TFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 515, 0, 1)
)
_S5ChasComBrdBayStack302TDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302TDram = _S5ChasComBrdBayStack302TDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 515, 0, 2)
)
_S5ChasComBrdBayStack302F_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302F = _S5ChasComBrdBayStack302F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 516)
)
_S5ChasComBrdBayStack302FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302FStore = _S5ChasComBrdBayStack302FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 516, 0)
)
_S5ChasComBrdBayStack302FFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302FFlash = _S5ChasComBrdBayStack302FFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 516, 0, 1)
)
_S5ChasComBrdBayStack302FDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack302FDram = _S5ChasComBrdBayStack302FDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 516, 0, 2)
)
_S5ChasComMod_c100mEther8P10FL_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther8P10FL = _S5ChasComMod_c100mEther8P10FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 517)
)
_S5ChasComMod_c100mEther12P2BTP_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther12P2BTP = _S5ChasComMod_c100mEther12P2BTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 518)
)
_S5ChasComMod_c100mEther4P100BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther4P100BT = _S5ChasComMod_c100mEther4P100BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 519)
)
_S5ChasComMod_5425mEther4PC100BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_5425mEther4PC100BT = _S5ChasComMod_5425mEther4PC100BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 520)
)
_S5ChasComMod_c100mEther8P2TXP_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther8P2TXP = _S5ChasComMod_c100mEther8P2TXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 527)
)
_S5ChasComBrdBayStack350T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350T = _S5ChasComBrdBayStack350T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 528)
)
_S5ChasComBrdBayStack350TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350TStore = _S5ChasComBrdBayStack350TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 528, 0)
)
_S5ChasComBrdBayStack350TFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350TFlash = _S5ChasComBrdBayStack350TFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 528, 0, 1)
)
_S5ChasComBrdBayStack350TBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350TBootFW = _S5ChasComBrdBayStack350TBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 528, 0, 2)
)
_S5ChasComBrdBayStack350TDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350TDram = _S5ChasComBrdBayStack350TDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 528, 0, 3)
)
_S5ChasComBrdBayStack350F_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350F = _S5ChasComBrdBayStack350F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 529)
)
_S5ChasComBrdBayStack350FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FStore = _S5ChasComBrdBayStack350FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 529, 0)
)
_S5ChasComBrdBayStack350FFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FFlash = _S5ChasComBrdBayStack350FFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 529, 0, 1)
)
_S5ChasComBrdBayStack350FBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FBootFW = _S5ChasComBrdBayStack350FBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 529, 0, 2)
)
_S5ChasComBrdBayStack350FDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FDram = _S5ChasComBrdBayStack350FDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 529, 0, 3)
)
_S5ChasComBrdBayStack350FHD_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FHD = _S5ChasComBrdBayStack350FHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 530)
)
_S5ChasComBrdBayStack350FHDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FHDStore = _S5ChasComBrdBayStack350FHDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 530, 0)
)
_S5ChasComBrdBayStack350FHDFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FHDFlash = _S5ChasComBrdBayStack350FHDFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 530, 0, 1)
)
_S5ChasComBrdBayStack350FHDBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FHDBootFW = _S5ChasComBrdBayStack350FHDBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 530, 0, 2)
)
_S5ChasComBrdBayStack350FHDDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350FHDDram = _S5ChasComBrdBayStack350FHDDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 530, 0, 3)
)
_S5ChasComBrdBayStack350THD_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350THD = _S5ChasComBrdBayStack350THD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 531)
)
_S5ChasComBrdBayStack350THDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350THDStore = _S5ChasComBrdBayStack350THDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 531, 0)
)
_S5ChasComBrdBayStack350THDFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350THDFlash = _S5ChasComBrdBayStack350THDFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 531, 0, 1)
)
_S5ChasComBrdBayStack350THDBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350THDBootFW = _S5ChasComBrdBayStack350THDBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 531, 0, 2)
)
_S5ChasComBrdBayStack350THDDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350THDDram = _S5ChasComBrdBayStack350THDDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 531, 0, 3)
)
_S5ChasComMod_5724M_SMmATMMCP4PSMFiber_ObjectIdentity = ObjectIdentity
s5ChasComMod_5724M_SMmATMMCP4PSMFiber = _S5ChasComMod_5724M_SMmATMMCP4PSMFiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 533)
)
_S5ChasComMod_SwNode10t16_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNode10t16 = _S5ChasComMod_SwNode10t16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 534)
)
_S5ChasComMod_SwNode100tx2_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNode100tx2 = _S5ChasComMod_SwNode100tx2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 535)
)
_S5ChasComMod_SwNode10f8_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNode10f8 = _S5ChasComMod_SwNode10f8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 536)
)
_S5ChasComMod_SwNode100tx16_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNode100tx16 = _S5ChasComMod_SwNode100tx16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 537)
)
_S5ChasComMod_SwNode100fx3_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNode100fx3 = _S5ChasComMod_SwNode100fx3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 541)
)
_S5ChasComDCMX220SwNode_ObjectIdentity = ObjectIdentity
s5ChasComDCMX220SwNode = _S5ChasComDCMX220SwNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 542)
)
_S5ChasComMod_c100mEther4x4P100BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther4x4P100BT = _S5ChasComMod_c100mEther4x4P100BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 544)
)
_S5ChasComMod_c100mEther4P100FX_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther4P100FX = _S5ChasComMod_c100mEther4P100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 545)
)
_S5ChasComBrdBayStack150_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150 = _S5ChasComBrdBayStack150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 546)
)
_S5ChasComBrdBayStack152_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack152 = _S5ChasComBrdBayStack152_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 547)
)
_S5ChasComBrdBayStack151_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack151 = _S5ChasComBrdBayStack151_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 548)
)
_S5ChasComBrdBayStack153_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack153 = _S5ChasComBrdBayStack153_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 549)
)
_S5ChasComBrdBayStack150NMM_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMM = _S5ChasComBrdBayStack150NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 550)
)
_S5ChasComBrdBayStack150NMMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMMStore = _S5ChasComBrdBayStack150NMMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 550, 0)
)
_S5ChasComBrdBayStack150NMMStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMMStoreBoot = _S5ChasComBrdBayStack150NMMStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 550, 0, 1)
)
_S5ChasComBrdBayStack150NMMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMMStoreFlash = _S5ChasComBrdBayStack150NMMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 550, 0, 2)
)
_S5ChasComBrdBayStack150NMMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMMStoreDram = _S5ChasComBrdBayStack150NMMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 550, 0, 3)
)
_S5ChasComBrdBayStack150NMMExpMod_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack150NMMExpMod = _S5ChasComBrdBayStack150NMMExpMod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 551)
)
_S5ChasComMod_C100ATMMDAhost_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMMDAhost = _S5ChasComMod_C100ATMMDAhost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 552)
)
_S5ChasComMod_C100ATMMDAMcp_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMMDAMcp = _S5ChasComMod_C100ATMMDAMcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 553)
)
_S5ChasComMod_5720ATMMDAhost_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720ATMMDAhost = _S5ChasComMod_5720ATMMDAhost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 554)
)
_S5ChasComMod_5720MATMMDAMcp_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720MATMMDAMcp = _S5ChasComMod_5720MATMMDAMcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 555)
)
_S5ChasComMod_5720_14MultiModeMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720_14MultiModeMda = _S5ChasComMod_5720_14MultiModeMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 556)
)
_S5ChasComMod_5720_15UTPMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720_15UTPMda = _S5ChasComMod_5720_15UTPMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 557)
)
_S5ChasComMod_5720_17SingleModeMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720_17SingleModeMda = _S5ChasComMod_5720_17SingleModeMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 558)
)
_S5ChasComMod_5720_31DS3Mda_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720_31DS3Mda = _S5ChasComMod_5720_31DS3Mda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 559)
)
_S5ChasComMod_5720_41E3Mda_ObjectIdentity = ObjectIdentity
s5ChasComMod_5720_41E3Mda = _S5ChasComMod_5720_41E3Mda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 560)
)
_S5ChasComMod_SwNodeCPU_ObjectIdentity = ObjectIdentity
s5ChasComMod_SwNodeCPU = _S5ChasComMod_SwNodeCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 561)
)
_S5ChasComMod_c1008PUTPTRMcp_ObjectIdentity = ObjectIdentity
s5ChasComMod_c1008PUTPTRMcp = _S5ChasComMod_c1008PUTPTRMcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 562)
)
_S5ChasComMod_c1008PUTPTR_ObjectIdentity = ObjectIdentity
s5ChasComMod_c1008PUTPTR = _S5ChasComMod_c1008PUTPTR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 563)
)
_S5ChasComBrdM5328_HD_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328_HD = _S5ChasComBrdM5328_HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 564)
)
_S5ChasComBrdM5328_HDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328_HDStore = _S5ChasComBrdM5328_HDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 564, 0)
)
_S5ChasComBrdM5328_HDStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328_HDStoreFlash = _S5ChasComBrdM5328_HDStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 564, 0, 1)
)
_S5ChasComBrdM5328_HDStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5328_HDStoreDram = _S5ChasComBrdM5328_HDStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 564, 0, 2)
)
_S5ChasComBrdM5625_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5625 = _S5ChasComBrdM5625_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 565)
)
_S5ChasComBrdM5455_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5455 = _S5ChasComBrdM5455_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 568)
)
_S5ChasComBrdM5455Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5455Store = _S5ChasComBrdM5455Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 568, 0)
)
_S5ChasComBrdM5455StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5455StoreFlash = _S5ChasComBrdM5455StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 568, 0, 1)
)
_S5ChasComBrdM5455StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5455StoreDram = _S5ChasComBrdM5455StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 568, 0, 2)
)
_S5ChasComM5611_DCM_ObjectIdentity = ObjectIdentity
s5ChasComM5611_DCM = _S5ChasComM5611_DCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 569)
)
_S5ChasComM5611_DCMStore_ObjectIdentity = ObjectIdentity
s5ChasComM5611_DCMStore = _S5ChasComM5611_DCMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 569, 0)
)
_S5ChasComM5611_DCMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComM5611_DCMStoreFlash = _S5ChasComM5611_DCMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 569, 0, 1)
)
_S5ChasComM5611_DCMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComM5611_DCMStoreDram = _S5ChasComM5611_DCMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 569, 0, 2)
)
_S5ChasComBrdBayStack202_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack202 = _S5ChasComBrdBayStack202_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 570)
)
_S5ChasComBrdBayStack203_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack203 = _S5ChasComBrdBayStack203_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 571)
)
_S5ChasComBrdBayStack204_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack204 = _S5ChasComBrdBayStack204_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 572)
)
_S5ChasComBrdBayStack205_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack205 = _S5ChasComBrdBayStack205_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 573)
)
_S5ChasComBrdBayStack200NMM_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack200NMM = _S5ChasComBrdBayStack200NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 574)
)
_S5ChasComBrdBayStack200NMMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack200NMMStore = _S5ChasComBrdBayStack200NMMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 574, 0)
)
_S5ChasComBrdBayStack200NMMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack200NMMStoreFlash = _S5ChasComBrdBayStack200NMMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 574, 0, 1)
)
_S5ChasComBrdBayStack200NMMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack200NMMStoreDram = _S5ChasComBrdBayStack200NMMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 574, 0, 2)
)
_S5ChasComMBayStack303_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303 = _S5ChasComMBayStack303_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 575)
)
_S5ChasComMBayStack304_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack304 = _S5ChasComMBayStack304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 576)
)
_S5ChasComMBayStack303A_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303A = _S5ChasComMBayStack303A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 577)
)
_S5ChasComMBayStack304A_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack304A = _S5ChasComMBayStack304A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 578)
)
_S5ChasComMBayStack303_304FxMda_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_304FxMda = _S5ChasComMBayStack303_304FxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 579)
)
_S5ChasComMBayStack303_304TxMda_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_304TxMda = _S5ChasComMBayStack303_304TxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 580)
)
_S5ChasComBrdM5665_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5665 = _S5ChasComBrdM5665_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 581)
)
_S5ChasComBrdM5665Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5665Store = _S5ChasComBrdM5665Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 581, 0)
)
_S5ChasComBrdM5665StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5665StoreFlash = _S5ChasComBrdM5665StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 581, 0, 1)
)
_S5ChasComBrdM5665StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5665StoreDram = _S5ChasComBrdM5665StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 581, 0, 2)
)
_S5ChasComBrdM5660FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5660FX = _S5ChasComBrdM5660FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 583)
)
_S5ChasComBrdM5660FXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5660FXStore = _S5ChasComBrdM5660FXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 583, 0)
)
_S5ChasComBrdM5660FXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5660FXStoreFlash = _S5ChasComBrdM5660FXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 583, 0, 1)
)
_S5ChasComBrdM5660FXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5660FXStoreDram = _S5ChasComBrdM5660FXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 583, 0, 2)
)
_S5ChasComBrdM5620FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5620FX = _S5ChasComBrdM5620FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 584)
)
_S5ChasComBrdM5620FXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5620FXStore = _S5ChasComBrdM5620FXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 584, 0)
)
_S5ChasComBrdM5620FXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5620FXStoreFlash = _S5ChasComBrdM5620FXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 584, 0, 1)
)
_S5ChasComBrdM5620FXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5620FXStoreDram = _S5ChasComBrdM5620FXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 584, 0, 2)
)
_S5ChasComBrdBayStack250_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250 = _S5ChasComBrdBayStack250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 595)
)
_S5ChasComBrdBayStack251_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack251 = _S5ChasComBrdBayStack251_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 596)
)
_S5ChasComBrdBayStack252_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack252 = _S5ChasComBrdBayStack252_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 597)
)
_S5ChasComBrdBayStack250NMM_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250NMM = _S5ChasComBrdBayStack250NMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 598)
)
_S5ChasComBrdBayStack250NMMStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250NMMStore = _S5ChasComBrdBayStack250NMMStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 598, 0)
)
_S5ChasComBrdBayStack250NMMStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250NMMStoreFlash = _S5ChasComBrdBayStack250NMMStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 598, 0, 1)
)
_S5ChasComBrdBayStack250NMMStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250NMMStoreDram = _S5ChasComBrdBayStack250NMMStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 598, 0, 2)
)
_S5ChasComBrdBayStack250NMMStoreBoot_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack250NMMStoreBoot = _S5ChasComBrdBayStack250NMMStoreBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 598, 0, 3)
)
_S5ChasComMod_c100mEther24P10BT_ObjectIdentity = ObjectIdentity
s5ChasComMod_c100mEther24P10BT = _S5ChasComMod_c100mEther24P10BT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 631)
)
_S5ChasComMod_C100ATMMultiModeMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMMultiModeMda = _S5ChasComMod_C100ATMMultiModeMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 632)
)
_S5ChasComMod_C100ATMUTPMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMUTPMda = _S5ChasComMod_C100ATMUTPMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 633)
)
_S5ChasComMod_C100ATMSingleModeMda_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMSingleModeMda = _S5ChasComMod_C100ATMSingleModeMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 634)
)
_S5ChasComMod_C100ATMDS3Mda_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATMDS3Mda = _S5ChasComMod_C100ATMDS3Mda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 635)
)
_S5ChasComMod_C100ATME3Mda_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100ATME3Mda = _S5ChasComMod_C100ATME3Mda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 636)
)
_S5ChasComBrdTR24PC_ObjectIdentity = ObjectIdentity
s5ChasComBrdTR24PC = _S5ChasComBrdTR24PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 637)
)
_S5ChasComBrd_C100TR16PC_ObjectIdentity = ObjectIdentity
s5ChasComBrd_C100TR16PC = _S5ChasComBrd_C100TR16PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 638)
)
_S5ChasComBrd57622M_SM_ObjectIdentity = ObjectIdentity
s5ChasComBrd57622M_SM = _S5ChasComBrd57622M_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 645)
)
_S5ChasComBrd57622M_MM_ObjectIdentity = ObjectIdentity
s5ChasComBrd57622M_MM = _S5ChasComBrd57622M_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 646)
)
_S5ChasComBrd57622_MM_ObjectIdentity = ObjectIdentity
s5ChasComBrd57622_MM = _S5ChasComBrd57622_MM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 647)
)
_S5ChasComBrd_C100ATMMCP1PSM_ObjectIdentity = ObjectIdentity
s5ChasComBrd_C100ATMMCP1PSM = _S5ChasComBrd_C100ATMMCP1PSM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 648)
)
_S5ChasComBrd_C100ATMMCP1PMM_ObjectIdentity = ObjectIdentity
s5ChasComBrd_C100ATMMCP1PMM = _S5ChasComBrd_C100ATMMCP1PMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 649)
)
_S5ChasComBrd_C100ATM1PMM_ObjectIdentity = ObjectIdentity
s5ChasComBrd_C100ATM1PMM = _S5ChasComBrd_C100ATM1PMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 650)
)
_S5ChasComBrdBayStack450_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24T = _S5ChasComBrdBayStack450_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 653)
)
_S5ChasComBrdBayStack450_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24TStore = _S5ChasComBrdBayStack450_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 653, 0)
)
_S5ChasComBrdBayStack450_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24TStoreFlash = _S5ChasComBrdBayStack450_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 653, 0, 1)
)
_S5ChasComBrdBayStack450_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24TStoreBootFW = _S5ChasComBrdBayStack450_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 653, 0, 2)
)
_S5ChasComBrdBayStack450_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24TStoreDram = _S5ChasComBrdBayStack450_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 653, 0, 3)
)
_S5ChasComBrdBayStack450_12T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12T = _S5ChasComBrdBayStack450_12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 654)
)
_S5ChasComBrdBayStack450_12TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12TStore = _S5ChasComBrdBayStack450_12TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 654, 0)
)
_S5ChasComBrdBayStack450_12TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12TStoreFlash = _S5ChasComBrdBayStack450_12TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 654, 0, 1)
)
_S5ChasComBrdBayStack450_12TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12TStoreBootFW = _S5ChasComBrdBayStack450_12TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 654, 0, 2)
)
_S5ChasComBrdBayStack450_12TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12TStoreDram = _S5ChasComBrdBayStack450_12TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 654, 0, 3)
)
_S5ChasComBrdBayStack410_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack410_24T = _S5ChasComBrdBayStack410_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 655)
)
_S5ChasComBrdBayStack450_1SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_1SX = _S5ChasComBrdBayStack450_1SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 656)
)
_S5ChasComBrdBayStack450_1SR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_1SR = _S5ChasComBrdBayStack450_1SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 657)
)
_S5ChasComBrdBayStack400_4TX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack400_4TX = _S5ChasComBrdBayStack400_4TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 658)
)
_S5ChasComBrdBayStack400_2FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack400_2FX = _S5ChasComBrdBayStack400_2FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 659)
)
_S5ChasComBrdBayStack400_ST1_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack400_ST1 = _S5ChasComBrdBayStack400_ST1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 660)
)
_S5ChasComBrdBayStack400_ST2_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack400_ST2 = _S5ChasComBrdBayStack400_ST2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 661)
)
_S5ChasComBrdBayStack450_1LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_1LX = _S5ChasComBrdBayStack450_1LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 662)
)
_S5ChasComBrdBayStack450_1LR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_1LR = _S5ChasComBrdBayStack450_1LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 663)
)
_S5ChasComBrdBayStack450_2SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_2SX = _S5ChasComBrdBayStack450_2SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 664)
)
_S5ChasComBrdBayStack450_2LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_2LX = _S5ChasComBrdBayStack450_2LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 665)
)
_S5ChasComBrdBayStack450_OC3_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_OC3 = _S5ChasComBrdBayStack450_OC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 666)
)
_S5ChasComBrdBayStack450_24TQP_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_24TQP = _S5ChasComBrdBayStack450_24TQP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 667)
)
_S5ChasComBrdBPS2000_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_24T = _S5ChasComBrdBPS2000_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 668)
)
_S5ChasComBrdBPS2000_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_24TStore = _S5ChasComBrdBPS2000_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 668, 0)
)
_S5ChasComBrdBPS2000_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_24TStoreFlash = _S5ChasComBrdBPS2000_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 668, 0, 1)
)
_S5ChasComBrdBPS2000_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_24TStoreBootFW = _S5ChasComBrdBPS2000_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 668, 0, 2)
)
_S5ChasComBrdBPS2000_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_24TStoreDram = _S5ChasComBrdBPS2000_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 668, 0, 3)
)
_S5ChasComBrd5424_ObjectIdentity = ObjectIdentity
s5ChasComBrd5424 = _S5ChasComBrd5424_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 669)
)
_S5ChasComBrdBayStack525_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack525 = _S5ChasComBrdBayStack525_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 670)
)
_S5ChasComBrdBayStack350_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24T = _S5ChasComBrdBayStack350_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 671)
)
_S5ChasComBrdBayStack350_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TStore = _S5ChasComBrdBayStack350_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 671, 0)
)
_S5ChasComBrdBayStack350_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TStoreFlash = _S5ChasComBrdBayStack350_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 671, 0, 1)
)
_S5ChasComBrdBayStack350_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TStoreBootFW = _S5ChasComBrdBayStack350_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 671, 0, 2)
)
_S5ChasComBrdBayStack350_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TStoreDram = _S5ChasComBrdBayStack350_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 671, 0, 3)
)
_S5ChasComBrdBayStack350_12T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12T = _S5ChasComBrdBayStack350_12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 672)
)
_S5ChasComBrdBayStack350_12TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TStore = _S5ChasComBrdBayStack350_12TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 672, 0)
)
_S5ChasComBrdBayStack350_12TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TStoreFlash = _S5ChasComBrdBayStack350_12TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 672, 0, 1)
)
_S5ChasComBrdBayStack350_12TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TStoreBootFW = _S5ChasComBrdBayStack350_12TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 672, 0, 2)
)
_S5ChasComBrdBayStack350_12TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TStoreDram = _S5ChasComBrdBayStack350_12TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 672, 0, 3)
)
_S5ChasComBrdBayStack253_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack253 = _S5ChasComBrdBayStack253_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 673)
)
_S5ChasComBrdBayStack450_12TQP_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12TQP = _S5ChasComBrdBayStack450_12TQP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 674)
)
_S5ChasComBrdBayStack350_24TQP_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TQP = _S5ChasComBrdBayStack350_24TQP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 675)
)
_S5ChasComBrdBayStack350_24TQPStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TQPStore = _S5ChasComBrdBayStack350_24TQPStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 675, 0)
)
_S5ChasComBrdBayStack350_24TQPStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TQPStoreFlash = _S5ChasComBrdBayStack350_24TQPStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 675, 0, 1)
)
_S5ChasComBrdBayStack350_24TQPStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TQPStoreBootFW = _S5ChasComBrdBayStack350_24TQPStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 675, 0, 2)
)
_S5ChasComBrdBayStack350_24TQPStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_24TQPStoreDram = _S5ChasComBrdBayStack350_24TQPStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 675, 0, 3)
)
_S5ChasComBrdBayStack350_12TQP_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TQP = _S5ChasComBrdBayStack350_12TQP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 676)
)
_S5ChasComBrdBayStack350_12TQPStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TQPStore = _S5ChasComBrdBayStack350_12TQPStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 676, 0)
)
_S5ChasComBrdBayStack350_12TQPStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TQPStoreFlash = _S5ChasComBrdBayStack350_12TQPStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 676, 0, 1)
)
_S5ChasComBrdBayStack350_12TQPStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TQPStoreBootFW = _S5ChasComBrdBayStack350_12TQPStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 676, 0, 2)
)
_S5ChasComBrdBayStack350_12TQPStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack350_12TQPStoreDram = _S5ChasComBrdBayStack350_12TQPStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 676, 0, 3)
)
_S5ChasComBrdBayStack450_12F_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12F = _S5ChasComBrdBayStack450_12F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 681)
)
_S5ChasComBrdBayStack450_12FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12FStore = _S5ChasComBrdBayStack450_12FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 681, 0)
)
_S5ChasComBrdBayStack450_12FStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12FStoreFlash = _S5ChasComBrdBayStack450_12FStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 681, 0, 1)
)
_S5ChasComBrdBayStack450_12FStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12FStoreBootFW = _S5ChasComBrdBayStack450_12FStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 681, 0, 2)
)
_S5ChasComBrdBayStack450_12FStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_12FStoreDram = _S5ChasComBrdBayStack450_12FStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 681, 0, 3)
)
_S5ChasComBrdBayStack400_4FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack400_4FX = _S5ChasComBrdBayStack400_4FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 682)
)
_S5ChasComMBayStack303_24T_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_24T = _S5ChasComMBayStack303_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 691)
)
_S5ChasComBrdBayStack_100FxMda_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack_100FxMda = _S5ChasComBrdBayStack_100FxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 692)
)
_S5ChasComBrdAccelar8132TX_ObjectIdentity = ObjectIdentity
s5ChasComBrdAccelar8132TX = _S5ChasComBrdAccelar8132TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 693)
)
_S5ChasComBrdAccelar8148TX_ObjectIdentity = ObjectIdentity
s5ChasComBrdAccelar8148TX = _S5ChasComBrdAccelar8148TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 694)
)
_S5ChasComBrdBayStack254_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack254 = _S5ChasComBrdBayStack254_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 695)
)
_S5ChasComBrdBayStack255_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack255 = _S5ChasComBrdBayStack255_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 696)
)
_S5ChasComBrdBayStack25x_100FxMda_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack25x_100FxMda = _S5ChasComBrdBayStack25x_100FxMda_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 697)
)
_S5ChasComBrdM5625HD_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5625HD = _S5ChasComBrdM5625HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 701)
)
_S5ChasComBrdM5424HD_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5424HD = _S5ChasComBrdM5424HD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 702)
)
_S5ChasComMod_C100mEther20PC_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100mEther20PC = _S5ChasComMod_C100mEther20PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 703)
)
_S5ChasComMod_C100mEther16P100FX_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100mEther16P100FX = _S5ChasComMod_C100mEther16P100FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 704)
)
_S5ChasComBrdBayStack670_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack670 = _S5ChasComBrdBayStack670_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 705)
)
_S5ChasComBrdBayStack670Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack670Store = _S5ChasComBrdBayStack670Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 705, 0)
)
_S5ChasComBrdBayStack670StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack670StoreFlash = _S5ChasComBrdBayStack670StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 705, 0, 1)
)
_S5ChasComBrdM5420_ObjectIdentity = ObjectIdentity
s5ChasComBrdM5420 = _S5ChasComBrdM5420_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 706)
)
_S5ChasComMod_C100mEther3PGBIC_ObjectIdentity = ObjectIdentity
s5ChasComMod_C100mEther3PGBIC = _S5ChasComMod_C100mEther3PGBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 707)
)
_S5ChasComBrdBPS2000_4TX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_4TX = _S5ChasComBrdBPS2000_4TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 708)
)
_S5ChasComBrdBPS2000_4FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_4FX = _S5ChasComBrdBPS2000_4FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 709)
)
_S5ChasComBrdBPS2000_2FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_2FX = _S5ChasComBrdBPS2000_2FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 710)
)
_S5ChasComBrdBayStack3580_16F_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack3580_16F = _S5ChasComBrdBayStack3580_16F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 711)
)
_S5ChasComBrdBayStack3580_16FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack3580_16FStore = _S5ChasComBrdBayStack3580_16FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 711, 0)
)
_S5ChasComBrdBayStack3580_16FStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack3580_16FStoreFlash = _S5ChasComBrdBayStack3580_16FStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 711, 0, 1)
)
_S5ChasComBrdBayStack3580_16FStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack3580_16FStoreBootFW = _S5ChasComBrdBayStack3580_16FStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 711, 0, 2)
)
_S5ChasComBrdBayStack3580_16FStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack3580_16FStoreDram = _S5ChasComBrdBayStack3580_16FStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 711, 0, 3)
)
_S5ChasComBrdBayStack450_OC3S_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_OC3S = _S5ChasComBrdBayStack450_OC3S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 717)
)
_S5ChasComBrdBayStack450_OC12_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_OC12 = _S5ChasComBrdBayStack450_OC12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 718)
)
_S5ChasComBrdBayStack450_OC12S_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_OC12S = _S5ChasComBrdBayStack450_OC12S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 719)
)
_S5ChasComBrdBayStack420_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack420_24T = _S5ChasComBrdBayStack420_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 720)
)
_S5ChasComBrdBayStack420_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack420_24TStore = _S5ChasComBrdBayStack420_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 720, 0)
)
_S5ChasComBrdBayStack420_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack420_24TStoreFlash = _S5ChasComBrdBayStack420_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 720, 0, 1)
)
_S5ChasComBrdBayStack420_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack420_24TStoreBootFW = _S5ChasComBrdBayStack420_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 720, 0, 2)
)
_S5ChasComBrdBayStack420_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack420_24TStoreDram = _S5ChasComBrdBayStack420_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 720, 0, 3)
)
_S5ChasComBrdBayStack450_GBIC_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBIC = _S5ChasComBrdBayStack450_GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721)
)
_S5ChasComBrdBayStack450_GBICno_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICno = _S5ChasComBrdBayStack450_GBICno_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 1)
)
_S5ChasComBrdBayStack450_GBICun_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICun = _S5ChasComBrdBayStack450_GBICun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 2)
)
_S5ChasComBrdBayStack450_GBICsx_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICsx = _S5ChasComBrdBayStack450_GBICsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 3)
)
_S5ChasComBrdBayStack450_GBIClx_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBIClx = _S5ChasComBrdBayStack450_GBIClx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 4)
)
_S5ChasComBrdBayStack450_GBICzx_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICzx = _S5ChasComBrdBayStack450_GBICzx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 5)
)
_S5ChasComBrdBayStack450_GBICxd_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICxd = _S5ChasComBrdBayStack450_GBICxd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 6)
)
_S5ChasComBrdBayStack450_GBICbt_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack450_GBICbt = _S5ChasComBrdBayStack450_GBICbt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 721, 7)
)
_S5ChasComBrdMetro1200ESM_12T_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1200ESM_12T = _S5ChasComBrdMetro1200ESM_12T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 722)
)
_S5ChasComBrdMetro1200ESM_12TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1200ESM_12TStore = _S5ChasComBrdMetro1200ESM_12TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 722, 0)
)
_S5ChasComBrdMetro1200ESM_12TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1200ESM_12TStoreFlash = _S5ChasComBrdMetro1200ESM_12TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 722, 0, 1)
)
_S5ChasComBrdMetro1200ESM_12TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1200ESM_12TStoreBootFW = _S5ChasComBrdMetro1200ESM_12TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 722, 0, 2)
)
_S5ChasComBrdMetro1200ESM_12TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1200ESM_12TStoreDram = _S5ChasComBrdMetro1200ESM_12TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 722, 0, 3)
)
_S5ChasComBrdBayStack380_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24T = _S5ChasComBrdBayStack380_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 723)
)
_S5ChasComBrdBayStack380_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24TStore = _S5ChasComBrdBayStack380_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 723, 0)
)
_S5ChasComBrdBayStack380_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24TStoreFlash = _S5ChasComBrdBayStack380_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 723, 0, 1)
)
_S5ChasComBrdBayStack380_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24TStoreBootFW = _S5ChasComBrdBayStack380_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 723, 0, 2)
)
_S5ChasComBrdBayStack380_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24TStoreDram = _S5ChasComBrdBayStack380_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 723, 0, 3)
)
_S5ChasComBrdTalonMDA_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA = _S5ChasComBrdTalonMDA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724)
)
_S5ChasComBrdTalonMDA_1GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_1GT = _S5ChasComBrdTalonMDA_1GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 1)
)
_S5ChasComBrdTalonMDA_2GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GT = _S5ChasComBrdTalonMDA_2GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 2)
)
_S5ChasComBrdTalonMDA_2GE_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE = _S5ChasComBrdTalonMDA_2GE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3)
)
_S5ChasComBrdTalonMDA_2GE_NO_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_NO = _S5ChasComBrdTalonMDA_2GE_NO_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 1)
)
_S5ChasComBrdTalonMDA_2GE_NO_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_UN = _S5ChasComBrdTalonMDA_2GE_NO_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 2)
)
_S5ChasComBrdTalonMDA_2GE_NO_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_SX = _S5ChasComBrdTalonMDA_2GE_NO_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 3)
)
_S5ChasComBrdTalonMDA_2GE_NO_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_LX = _S5ChasComBrdTalonMDA_2GE_NO_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 4)
)
_S5ChasComBrdTalonMDA_2GE_NO_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_ZX = _S5ChasComBrdTalonMDA_2GE_NO_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 5)
)
_S5ChasComBrdTalonMDA_2GE_NO_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_NO_XD = _S5ChasComBrdTalonMDA_2GE_NO_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 1, 6)
)
_S5ChasComBrdTalonMDA_2GE_UN_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_NO = _S5ChasComBrdTalonMDA_2GE_UN_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 1)
)
_S5ChasComBrdTalonMDA_2GE_UN_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_UN = _S5ChasComBrdTalonMDA_2GE_UN_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 2)
)
_S5ChasComBrdTalonMDA_2GE_UN_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_SX = _S5ChasComBrdTalonMDA_2GE_UN_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 3)
)
_S5ChasComBrdTalonMDA_2GE_UN_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_LX = _S5ChasComBrdTalonMDA_2GE_UN_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 4)
)
_S5ChasComBrdTalonMDA_2GE_UN_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_ZX = _S5ChasComBrdTalonMDA_2GE_UN_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 5)
)
_S5ChasComBrdTalonMDA_2GE_UN_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_UN_XD = _S5ChasComBrdTalonMDA_2GE_UN_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 2, 6)
)
_S5ChasComBrdTalonMDA_2GE_SX_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_NO = _S5ChasComBrdTalonMDA_2GE_SX_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 1)
)
_S5ChasComBrdTalonMDA_2GE_SX_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_UN = _S5ChasComBrdTalonMDA_2GE_SX_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 2)
)
_S5ChasComBrdTalonMDA_2GE_SX_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_SX = _S5ChasComBrdTalonMDA_2GE_SX_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 3)
)
_S5ChasComBrdTalonMDA_2GE_SX_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_LX = _S5ChasComBrdTalonMDA_2GE_SX_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 4)
)
_S5ChasComBrdTalonMDA_2GE_SX_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_ZX = _S5ChasComBrdTalonMDA_2GE_SX_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 5)
)
_S5ChasComBrdTalonMDA_2GE_SX_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_SX_XD = _S5ChasComBrdTalonMDA_2GE_SX_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 3, 6)
)
_S5ChasComBrdTalonMDA_2GE_LX_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_NO = _S5ChasComBrdTalonMDA_2GE_LX_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 1)
)
_S5ChasComBrdTalonMDA_2GE_LX_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_UN = _S5ChasComBrdTalonMDA_2GE_LX_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 2)
)
_S5ChasComBrdTalonMDA_2GE_LX_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_SX = _S5ChasComBrdTalonMDA_2GE_LX_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 3)
)
_S5ChasComBrdTalonMDA_2GE_LX_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_LX = _S5ChasComBrdTalonMDA_2GE_LX_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 4)
)
_S5ChasComBrdTalonMDA_2GE_LX_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_ZX = _S5ChasComBrdTalonMDA_2GE_LX_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 5)
)
_S5ChasComBrdTalonMDA_2GE_LX_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_LX_XD = _S5ChasComBrdTalonMDA_2GE_LX_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 4, 6)
)
_S5ChasComBrdTalonMDA_2GE_ZX_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_NO = _S5ChasComBrdTalonMDA_2GE_ZX_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 1)
)
_S5ChasComBrdTalonMDA_2GE_ZX_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_UN = _S5ChasComBrdTalonMDA_2GE_ZX_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 2)
)
_S5ChasComBrdTalonMDA_2GE_ZX_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_SX = _S5ChasComBrdTalonMDA_2GE_ZX_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 3)
)
_S5ChasComBrdTalonMDA_2GE_ZX_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_LX = _S5ChasComBrdTalonMDA_2GE_ZX_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 4)
)
_S5ChasComBrdTalonMDA_2GE_ZX_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_ZX = _S5ChasComBrdTalonMDA_2GE_ZX_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 5)
)
_S5ChasComBrdTalonMDA_2GE_ZX_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_ZX_XD = _S5ChasComBrdTalonMDA_2GE_ZX_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 5, 6)
)
_S5ChasComBrdTalonMDA_2GE_XD_NO_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_NO = _S5ChasComBrdTalonMDA_2GE_XD_NO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 1)
)
_S5ChasComBrdTalonMDA_2GE_XD_UN_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_UN = _S5ChasComBrdTalonMDA_2GE_XD_UN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 2)
)
_S5ChasComBrdTalonMDA_2GE_XD_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_SX = _S5ChasComBrdTalonMDA_2GE_XD_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 3)
)
_S5ChasComBrdTalonMDA_2GE_XD_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_LX = _S5ChasComBrdTalonMDA_2GE_XD_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 4)
)
_S5ChasComBrdTalonMDA_2GE_XD_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_ZX = _S5ChasComBrdTalonMDA_2GE_XD_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 5)
)
_S5ChasComBrdTalonMDA_2GE_XD_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdTalonMDA_2GE_XD_XD = _S5ChasComBrdTalonMDA_2GE_XD_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 724, 3, 6, 6)
)
_S5ChasComBrdBPS2000_4FX_SM_ObjectIdentity = ObjectIdentity
s5ChasComBrdBPS2000_4FX_SM = _S5ChasComBrdBPS2000_4FX_SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 725)
)
_S5ChasComBrdBayStack470_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T = _S5ChasComBrdBayStack470_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 726)
)
_S5ChasComBrdBayStack470_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48TStore = _S5ChasComBrdBayStack470_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 726, 0)
)
_S5ChasComBrdBayStack470_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48TStoreFlash = _S5ChasComBrdBayStack470_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 726, 0, 1)
)
_S5ChasComBrdBayStack470_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48TStoreBootFW = _S5ChasComBrdBayStack470_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 726, 0, 2)
)
_S5ChasComBrdBayStack470_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48TStoreDram = _S5ChasComBrdBayStack470_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 726, 0, 3)
)
_S5ChasComBrdGbic_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic = _S5ChasComBrdGbic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727)
)
_S5ChasComBrdGbic_None_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_None = _S5ChasComBrdGbic_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 1)
)
_S5ChasComBrdGbic_Unsupported_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_Unsupported = _S5ChasComBrdGbic_Unsupported_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 2)
)
_S5ChasComBrdGbic_SX_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_SX = _S5ChasComBrdGbic_SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 3)
)
_S5ChasComBrdGbic_LX_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_LX = _S5ChasComBrdGbic_LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 4)
)
_S5ChasComBrdGbic_ZX_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_ZX = _S5ChasComBrdGbic_ZX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 5)
)
_S5ChasComBrdGbic_XD_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_XD = _S5ChasComBrdGbic_XD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 6)
)
_S5ChasComBrdGbic_TX_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_TX = _S5ChasComBrdGbic_TX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 7)
)
_S5ChasComBrdGbic_CWDM_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_CWDM = _S5ChasComBrdGbic_CWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 8)
)
_S5ChasComBrdGbic_DWDM_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_DWDM = _S5ChasComBrdGbic_DWDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 9)
)
_S5ChasComBrdGbic_10G_SR_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_SR = _S5ChasComBrdGbic_10G_SR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 10)
)
_S5ChasComBrdGbic_10G_LR_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_LR = _S5ChasComBrdGbic_10G_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 11)
)
_S5ChasComBrdGbic_10G_ER_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_ER = _S5ChasComBrdGbic_10G_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 12)
)
_S5ChasComBrdGbic_10G_LX4_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_LX4 = _S5ChasComBrdGbic_10G_LX4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 13)
)
_S5ChasComBrdGbic_10G_ZR_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_ZR = _S5ChasComBrdGbic_10G_ZR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 14)
)
_S5ChasComBrdGbic_10G_LRM_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_10G_LRM = _S5ChasComBrdGbic_10G_LRM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 15)
)
_S5ChasComBrdGbic_T1_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_T1 = _S5ChasComBrdGbic_T1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 16)
)
_S5ChasComBrdGbic_EX_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_EX = _S5ChasComBrdGbic_EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 17)
)
_S5ChasComBrdGbic_DIRECT_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_DIRECT = _S5ChasComBrdGbic_DIRECT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 18)
)
_S5ChasComBrdGbic_40G_SR4_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_40G_SR4 = _S5ChasComBrdGbic_40G_SR4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 19)
)
_S5ChasComBrdGbic_40G_LR_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_40G_LR = _S5ChasComBrdGbic_40G_LR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 20)
)
_S5ChasComBrdGbic_40G_ER_ObjectIdentity = ObjectIdentity
s5ChasComBrdGbic_40G_ER = _S5ChasComBrdGbic_40G_ER_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 727, 21)
)
_S5ChasComBrdMetro1450ESM_12T2GBIC_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1450ESM_12T2GBIC = _S5ChasComBrdMetro1450ESM_12T2GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 728)
)
_S5ChasComBrdMetro1450ESM_12T2GBICStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1450ESM_12T2GBICStore = _S5ChasComBrdMetro1450ESM_12T2GBICStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 728, 0)
)
_S5ChasComBrdMetro1450ESM_12T2GBICStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1450ESM_12T2GBICStoreFlash = _S5ChasComBrdMetro1450ESM_12T2GBICStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 728, 0, 1)
)
_S5ChasComBrdMetro1450ESM_12T2GBICStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1450ESM_12T2GBICStoreBootFW = _S5ChasComBrdMetro1450ESM_12T2GBICStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 728, 0, 2)
)
_S5ChasComBrdMetro1450ESM_12T2GBICStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1450ESM_12T2GBICStoreDram = _S5ChasComBrdMetro1450ESM_12T2GBICStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 728, 0, 3)
)
_S5ChasComBrdMetro1400ESM_12T2GBIC_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1400ESM_12T2GBIC = _S5ChasComBrdMetro1400ESM_12T2GBIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 729)
)
_S5ChasComBrdMetro1400ESM_12T2GBICStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1400ESM_12T2GBICStore = _S5ChasComBrdMetro1400ESM_12T2GBICStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 729, 0)
)
_S5ChasComBrdMetro1400ESM_12T2GBICStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1400ESM_12T2GBICStoreFlash = _S5ChasComBrdMetro1400ESM_12T2GBICStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 729, 0, 1)
)
_S5ChasComBrdMetro1400ESM_12T2GBICStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1400ESM_12T2GBICStoreBootFW = _S5ChasComBrdMetro1400ESM_12T2GBICStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 729, 0, 2)
)
_S5ChasComBrdMetro1400ESM_12T2GBICStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdMetro1400ESM_12T2GBICStoreDram = _S5ChasComBrdMetro1400ESM_12T2GBICStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 729, 0, 3)
)
_S5ChasComBrdBayStack460_24T_PWR_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24T = _S5ChasComBrdBayStack460_24T_PWR_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730)
)
_S5ChasComBrdBayStack460_24T_PWR_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24TStore = _S5ChasComBrdBayStack460_24T_PWR_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730, 0)
)
_S5ChasComBrdBayStack460_24T_PWR_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24TStoreFlash = _S5ChasComBrdBayStack460_24T_PWR_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730, 0, 1)
)
_S5ChasComBrdBayStack460_24T_PWR_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24TStoreBootFW = _S5ChasComBrdBayStack460_24T_PWR_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730, 0, 2)
)
_S5ChasComBrdBayStack460_24T_PWR_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24TStoreDram = _S5ChasComBrdBayStack460_24T_PWR_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730, 0, 3)
)
_S5ChasComBrdBayStack460_24T_PWR_24TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack460_24T_PWR_24TStorePoLFlash = _S5ChasComBrdBayStack460_24T_PWR_24TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 730, 0, 4)
)
_S5ChasComBrdBayStack380_24F_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24F = _S5ChasComBrdBayStack380_24F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 731)
)
_S5ChasComBrdBayStack380_24FStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24FStore = _S5ChasComBrdBayStack380_24FStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 731, 0)
)
_S5ChasComBrdBayStack380_24FStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24FStoreFlash = _S5ChasComBrdBayStack380_24FStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 731, 0, 1)
)
_S5ChasComBrdBayStack380_24FStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24FStoreBootFW = _S5ChasComBrdBayStack380_24FStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 731, 0, 2)
)
_S5ChasComBrdBayStack380_24FStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack380_24FStoreDram = _S5ChasComBrdBayStack380_24FStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 731, 0, 3)
)
_S5ChasComBrdBayStack5510_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_24T = _S5ChasComBrdBayStack5510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 732)
)
_S5ChasComBrdBayStack5510_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_24TStore = _S5ChasComBrdBayStack5510_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 732, 0)
)
_S5ChasComBrdBayStack5510_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_24TStoreFlash = _S5ChasComBrdBayStack5510_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 732, 0, 1)
)
_S5ChasComBrdBayStack5510_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_24TStoreBootFW = _S5ChasComBrdBayStack5510_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 732, 0, 2)
)
_S5ChasComBrdBayStack5510_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_24TStoreDram = _S5ChasComBrdBayStack5510_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 732, 0, 3)
)
_S5ChasComBrdBayStack5510_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_48T = _S5ChasComBrdBayStack5510_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 733)
)
_S5ChasComBrdBayStack5510_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_48TStore = _S5ChasComBrdBayStack5510_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 733, 0)
)
_S5ChasComBrdBayStack5510_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_48TStoreFlash = _S5ChasComBrdBayStack5510_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 733, 0, 1)
)
_S5ChasComBrdBayStack5510_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_48TStoreBootFW = _S5ChasComBrdBayStack5510_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 733, 0, 2)
)
_S5ChasComBrdBayStack5510_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5510_48TStoreDram = _S5ChasComBrdBayStack5510_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 733, 0, 3)
)
_S5ChasComBrdBayStack470_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T = _S5ChasComBrdBayStack470_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 734)
)
_S5ChasComBrdBayStack470_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24TStore = _S5ChasComBrdBayStack470_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 734, 0)
)
_S5ChasComBrdBayStack470_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24TStoreFlash = _S5ChasComBrdBayStack470_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 734, 0, 1)
)
_S5ChasComBrdBayStack470_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24TStoreBootFW = _S5ChasComBrdBayStack470_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 734, 0, 2)
)
_S5ChasComBrdBayStack470_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24TStoreDram = _S5ChasComBrdBayStack470_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 734, 0, 3)
)
_S5ChasComBrdWLANAccessPoint2220_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2220 = _S5ChasComBrdWLANAccessPoint2220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 735)
)
_S5ChasComBrdWLANAccessPoint2220Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2220Store = _S5ChasComBrdWLANAccessPoint2220Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 735, 0)
)
_S5ChasComBrdWLANAccessPoint2220StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2220StoreFlash = _S5ChasComBrdWLANAccessPoint2220StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 735, 0, 1)
)
_S5ChasComBrdWLANAccessPoint2220StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2220StoreBootFW = _S5ChasComBrdWLANAccessPoint2220StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 735, 0, 2)
)
_S5ChasComBrdWLANAccessPoint2220StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2220StoreDram = _S5ChasComBrdWLANAccessPoint2220StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 735, 0, 3)
)
_S5ChasComBrdWLANSecuritySwitch2250_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2250 = _S5ChasComBrdWLANSecuritySwitch2250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 736)
)
_S5ChasComBrdWLANSecuritySwitch2250Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2250Store = _S5ChasComBrdWLANSecuritySwitch2250Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 736, 0)
)
_S5ChasComBrdWLANSecuritySwitch2250StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2250StoreFlash = _S5ChasComBrdWLANSecuritySwitch2250StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 736, 0, 1)
)
_S5ChasComBrdWLANSecuritySwitch2250StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2250StoreBootFW = _S5ChasComBrdWLANSecuritySwitch2250StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 736, 0, 2)
)
_S5ChasComBrdWLANSecuritySwitch2250StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2250StoreDram = _S5ChasComBrdWLANSecuritySwitch2250StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 736, 0, 3)
)
_S5ChasComBrdBayStack425_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425 = _S5ChasComBrdBayStack425_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 737)
)
_S5ChasComBrdBayStack425Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425Store = _S5ChasComBrdBayStack425Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 737, 0)
)
_S5ChasComBrdBayStack425StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425StoreFlash = _S5ChasComBrdBayStack425StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 737, 0, 1)
)
_S5ChasComBrdBayStack425StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425StoreBootFW = _S5ChasComBrdBayStack425StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 737, 0, 2)
)
_S5ChasComBrdBayStack425StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425StoreDram = _S5ChasComBrdBayStack425StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 737, 0, 3)
)
_S5ChasComBrdWLANAccessPoint2221_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2221 = _S5ChasComBrdWLANAccessPoint2221_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 738)
)
_S5ChasComBrdWLANAccessPoint2221Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2221Store = _S5ChasComBrdWLANAccessPoint2221Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 738, 0)
)
_S5ChasComBrdWLANAccessPoint2221StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2221StoreFlash = _S5ChasComBrdWLANAccessPoint2221StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 738, 0, 1)
)
_S5ChasComBrdWLANAccessPoint2221StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2221StoreBootFW = _S5ChasComBrdWLANAccessPoint2221StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 738, 0, 2)
)
_S5ChasComBrdWLANAccessPoint2221StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2221StoreDram = _S5ChasComBrdWLANAccessPoint2221StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 738, 0, 3)
)
_S5ChasComBrdBayStack5520_24T_PWR_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24T = _S5ChasComBrdBayStack5520_24T_PWR_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739)
)
_S5ChasComBrdBayStack5520_24T_PWR_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24TStore = _S5ChasComBrdBayStack5520_24T_PWR_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739, 0)
)
_S5ChasComBrdBayStack5520_24T_PWR_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24TStoreFlash = _S5ChasComBrdBayStack5520_24T_PWR_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739, 0, 1)
)
_S5ChasComBrdBayStack5520_24T_PWR_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24TStoreBootFW = _S5ChasComBrdBayStack5520_24T_PWR_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739, 0, 2)
)
_S5ChasComBrdBayStack5520_24T_PWR_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24TStoreDram = _S5ChasComBrdBayStack5520_24T_PWR_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739, 0, 3)
)
_S5ChasComBrdBayStack5520_24T_PWR_24TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_24T_PWR_24TStorePoLFlash = _S5ChasComBrdBayStack5520_24T_PWR_24TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 739, 0, 4)
)
_S5ChasComBrdBayStack5520_48T_PWR_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48T = _S5ChasComBrdBayStack5520_48T_PWR_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740)
)
_S5ChasComBrdBayStack5520_48T_PWR_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48TStore = _S5ChasComBrdBayStack5520_48T_PWR_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740, 0)
)
_S5ChasComBrdBayStack5520_48T_PWR_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48TStoreFlash = _S5ChasComBrdBayStack5520_48T_PWR_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740, 0, 1)
)
_S5ChasComBrdBayStack5520_48T_PWR_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48TStoreBootFW = _S5ChasComBrdBayStack5520_48T_PWR_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740, 0, 2)
)
_S5ChasComBrdBayStack5520_48T_PWR_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48TStoreDram = _S5ChasComBrdBayStack5520_48T_PWR_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740, 0, 3)
)
_S5ChasComBrdBayStack5520_48T_PWR_48TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack5520_48T_PWR_48TStorePoLFlash = _S5ChasComBrdBayStack5520_48T_PWR_48TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 740, 0, 4)
)
_S5ChasComBrdBayStack425_48_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425_48 = _S5ChasComBrdBayStack425_48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 741)
)
_S5ChasComBrdBayStack425_48Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425_48Store = _S5ChasComBrdBayStack425_48Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 741, 0)
)
_S5ChasComBrdBayStack425_48StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425_48StoreFlash = _S5ChasComBrdBayStack425_48StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 741, 0, 1)
)
_S5ChasComBrdBayStack425_48StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425_48StoreBootFW = _S5ChasComBrdBayStack425_48StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 741, 0, 2)
)
_S5ChasComBrdBayStack425_48StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack425_48StoreDram = _S5ChasComBrdBayStack425_48StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 741, 0, 3)
)
_S5ChasComBrdBayStack325_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325 = _S5ChasComBrdBayStack325_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742)
)
_S5ChasComBrdBayStack325Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325Store = _S5ChasComBrdBayStack325Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 0)
)
_S5ChasComBrdBayStack325StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325StoreFlash = _S5ChasComBrdBayStack325StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 0, 1)
)
_S5ChasComBrdBayStack325StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325StoreBootFW = _S5ChasComBrdBayStack325StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 0, 2)
)
_S5ChasComBrdBayStack325StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325StoreDram = _S5ChasComBrdBayStack325StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 0, 3)
)
_S5ChasComBrdBayStack325_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325_24T = _S5ChasComBrdBayStack325_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 1)
)
_S5ChasComBrdBayStack325_24G_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack325_24G = _S5ChasComBrdBayStack325_24G_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 742, 2)
)
_S5ChasComBrdWLANAccessPoint2225_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2225 = _S5ChasComBrdWLANAccessPoint2225_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 743)
)
_S5ChasComBrdWLANAccessPoint2225Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2225Store = _S5ChasComBrdWLANAccessPoint2225Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 743, 0)
)
_S5ChasComBrdWLANAccessPoint2225StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2225StoreFlash = _S5ChasComBrdWLANAccessPoint2225StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 743, 0, 1)
)
_S5ChasComBrdWLANAccessPoint2225StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2225StoreBootFW = _S5ChasComBrdWLANAccessPoint2225StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 743, 0, 2)
)
_S5ChasComBrdWLANAccessPoint2225StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANAccessPoint2225StoreDram = _S5ChasComBrdWLANAccessPoint2225StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 743, 0, 3)
)
_S5ChasComBrdBayStack470_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T_PWR = _S5ChasComBrdBayStack470_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 744)
)
_S5ChasComBrdBayStack470_24T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T_PWRStore = _S5ChasComBrdBayStack470_24T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 744, 0)
)
_S5ChasComBrdBayStack470_24T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T_PWRStoreFlash = _S5ChasComBrdBayStack470_24T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 744, 0, 1)
)
_S5ChasComBrdBayStack470_24T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T_PWRStoreBootFW = _S5ChasComBrdBayStack470_24T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 744, 0, 2)
)
_S5ChasComBrdBayStack470_24T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_24T_PWRStoreDram = _S5ChasComBrdBayStack470_24T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 744, 0, 3)
)
_S5ChasComBrdBayStack470_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T_PWR = _S5ChasComBrdBayStack470_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 745)
)
_S5ChasComBrdBayStack470_48T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T_PWRStore = _S5ChasComBrdBayStack470_48T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 745, 0)
)
_S5ChasComBrdBayStack470_48T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T_PWRStoreFlash = _S5ChasComBrdBayStack470_48T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 745, 0, 1)
)
_S5ChasComBrdBayStack470_48T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T_PWRStoreBootFW = _S5ChasComBrdBayStack470_48T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 745, 0, 2)
)
_S5ChasComBrdBayStack470_48T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBayStack470_48T_PWRStoreDram = _S5ChasComBrdBayStack470_48T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 745, 0, 3)
)
_S5ChasComBrdWLANSecuritySwitch2270_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270 = _S5ChasComBrdWLANSecuritySwitch2270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 746)
)
_S5ChasComBrdWLANSecuritySwitch2270Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270Store = _S5ChasComBrdWLANSecuritySwitch2270Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 746, 0)
)
_S5ChasComBrdWLANSecuritySwitch2270StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270StoreFlash = _S5ChasComBrdWLANSecuritySwitch2270StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 746, 0, 1)
)
_S5ChasComBrdWLANSecuritySwitch2270StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270StoreBootFW = _S5ChasComBrdWLANSecuritySwitch2270StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 746, 0, 2)
)
_S5ChasComBrdWLANSecuritySwitch2270StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270StoreDram = _S5ChasComBrdWLANSecuritySwitch2270StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 746, 0, 3)
)
_S5ChasComBrdEthernetRoutingSwitch5530_24TFD_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetRoutingSwitch5530_24TFD = _S5ChasComBrdEthernetRoutingSwitch5530_24TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 747)
)
_S5ChasComBrdEthernetRoutingSwitch5530_24TFDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetRoutingSwitch5530_24TFDStore = _S5ChasComBrdEthernetRoutingSwitch5530_24TFDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 747, 0)
)
_S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreFlash = _S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 747, 0, 1)
)
_S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreBootFW = _S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 747, 0, 2)
)
_S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreDram = _S5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 747, 0, 3)
)
_S5ChasComBrdEthernetSwitch3510_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetSwitch3510_24T = _S5ChasComBrdEthernetSwitch3510_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 748)
)
_S5ChasComBrdEthernetSwitch3510_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetSwitch3510_24TStore = _S5ChasComBrdEthernetSwitch3510_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 748, 0)
)
_S5ChasComBrdEthernetSwitch3510_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetSwitch3510_24TStoreFlash = _S5ChasComBrdEthernetSwitch3510_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 748, 0, 1)
)
_S5ChasComBrdEthernetSwitch3510_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetSwitch3510_24TStoreBootFW = _S5ChasComBrdEthernetSwitch3510_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 748, 0, 2)
)
_S5ChasComBrdEthernetSwitch3510_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdEthernetSwitch3510_24TStoreDram = _S5ChasComBrdEthernetSwitch3510_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 748, 0, 3)
)
_S5ChasComBrdWLANSecurityCryptographyModules_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecurityCryptographyModules = _S5ChasComBrdWLANSecurityCryptographyModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 749)
)
_S5ChasComBrdWLANSecuritySwitch2270CryptoAccelerator_ObjectIdentity = ObjectIdentity
s5ChasComBrdWLANSecuritySwitch2270CryptoAccelerator = _S5ChasComBrdWLANSecuritySwitch2270CryptoAccelerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 749, 1)
)
_S5ChasComBrdBES1010_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_24T = _S5ChasComBrdBES1010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 750)
)
_S5ChasComBrdBES1010_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_24TStore = _S5ChasComBrdBES1010_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 750, 0)
)
_S5ChasComBrdBES1010_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_24TStoreFlash = _S5ChasComBrdBES1010_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 750, 0, 1)
)
_S5ChasComBrdBES1010_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_24TStoreBootFW = _S5ChasComBrdBES1010_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 750, 0, 2)
)
_S5ChasComBrdBES1010_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_24TStoreDram = _S5ChasComBrdBES1010_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 750, 0, 3)
)
_S5ChasComBrdBES1010_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_48T = _S5ChasComBrdBES1010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 751)
)
_S5ChasComBrdBES1010_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_48TStore = _S5ChasComBrdBES1010_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 751, 0)
)
_S5ChasComBrdBES1010_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_48TStoreFlash = _S5ChasComBrdBES1010_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 751, 0, 1)
)
_S5ChasComBrdBES1010_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_48TStoreBootFW = _S5ChasComBrdBES1010_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 751, 0, 2)
)
_S5ChasComBrdBES1010_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1010_48TStoreDram = _S5ChasComBrdBES1010_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 751, 0, 3)
)
_S5ChasComBrdBES1020_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWR = _S5ChasComBrdBES1020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752)
)
_S5ChasComBrdBES1020_24T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWRStore = _S5ChasComBrdBES1020_24T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752, 0)
)
_S5ChasComBrdBES1020_24T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWRStoreFlash = _S5ChasComBrdBES1020_24T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752, 0, 1)
)
_S5ChasComBrdBES1020_24T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWRStoreBootFW = _S5ChasComBrdBES1020_24T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752, 0, 2)
)
_S5ChasComBrdBES1020_24T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWRStoreDram = _S5ChasComBrdBES1020_24T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752, 0, 3)
)
_S5ChasComBrdBES1020_24T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_24T_PWRStorePoLFlash = _S5ChasComBrdBES1020_24T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 752, 0, 4)
)
_S5ChasComBrdBES1020_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWR = _S5ChasComBrdBES1020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753)
)
_S5ChasComBrdBES1020_48T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWRStore = _S5ChasComBrdBES1020_48T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753, 0)
)
_S5ChasComBrdBES1020_48T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWRStoreFlash = _S5ChasComBrdBES1020_48T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753, 0, 1)
)
_S5ChasComBrdBES1020_48T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWRStoreBootFW = _S5ChasComBrdBES1020_48T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753, 0, 2)
)
_S5ChasComBrdBES1020_48T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWRStoreDram = _S5ChasComBrdBES1020_48T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753, 0, 3)
)
_S5ChasComBrdBES1020_48T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES1020_48T_PWRStorePoLFlash = _S5ChasComBrdBES1020_48T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 753, 0, 4)
)
_S5ChasComBrdBES2010_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_24T = _S5ChasComBrdBES2010_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 754)
)
_S5ChasComBrdBES2010_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_24TStore = _S5ChasComBrdBES2010_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 754, 0)
)
_S5ChasComBrdBES2010_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_24TStoreFlash = _S5ChasComBrdBES2010_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 754, 0, 1)
)
_S5ChasComBrdBES2010_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_24TStoreBootFW = _S5ChasComBrdBES2010_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 754, 0, 2)
)
_S5ChasComBrdBES2010_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_24TStoreDram = _S5ChasComBrdBES2010_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 754, 0, 3)
)
_S5ChasComBrdBES2010_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_48T = _S5ChasComBrdBES2010_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 755)
)
_S5ChasComBrdBES2010_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_48TStore = _S5ChasComBrdBES2010_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 755, 0)
)
_S5ChasComBrdBES2010_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_48TStoreFlash = _S5ChasComBrdBES2010_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 755, 0, 1)
)
_S5ChasComBrdBES2010_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_48TStoreBootFW = _S5ChasComBrdBES2010_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 755, 0, 2)
)
_S5ChasComBrdBES2010_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2010_48TStoreDram = _S5ChasComBrdBES2010_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 755, 0, 3)
)
_S5ChasComBrdBES2020_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWR = _S5ChasComBrdBES2020_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756)
)
_S5ChasComBrdBES2020_24T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWRStore = _S5ChasComBrdBES2020_24T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756, 0)
)
_S5ChasComBrdBES2020_24T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWRStoreFlash = _S5ChasComBrdBES2020_24T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756, 0, 1)
)
_S5ChasComBrdBES2020_24T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWRStoreBootFW = _S5ChasComBrdBES2020_24T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756, 0, 2)
)
_S5ChasComBrdBES2020_24T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWRStoreDram = _S5ChasComBrdBES2020_24T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756, 0, 3)
)
_S5ChasComBrdBES2020_24T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_24T_PWRStorePoLFlash = _S5ChasComBrdBES2020_24T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 756, 0, 4)
)
_S5ChasComBrdBES2020_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWR = _S5ChasComBrdBES2020_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757)
)
_S5ChasComBrdBES2020_48T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWRStore = _S5ChasComBrdBES2020_48T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757, 0)
)
_S5ChasComBrdBES2020_48T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWRStoreFlash = _S5ChasComBrdBES2020_48T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757, 0, 1)
)
_S5ChasComBrdBES2020_48T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWRStoreBootFW = _S5ChasComBrdBES2020_48T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757, 0, 2)
)
_S5ChasComBrdBES2020_48T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWRStoreDram = _S5ChasComBrdBES2020_48T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757, 0, 3)
)
_S5ChasComBrdBES2020_48T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES2020_48T_PWRStorePoLFlash = _S5ChasComBrdBES2020_48T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 757, 0, 4)
)
_S5ChasComBrdBES110_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_24T = _S5ChasComBrdBES110_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 758)
)
_S5ChasComBrdBES110_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_24TStore = _S5ChasComBrdBES110_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 758, 0)
)
_S5ChasComBrdBES110_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_24TStoreFlash = _S5ChasComBrdBES110_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 758, 0, 1)
)
_S5ChasComBrdBES110_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_24TStoreBootFW = _S5ChasComBrdBES110_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 758, 0, 2)
)
_S5ChasComBrdBES110_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_24TStoreDram = _S5ChasComBrdBES110_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 758, 0, 3)
)
_S5ChasComBrdBES110_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_48T = _S5ChasComBrdBES110_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 759)
)
_S5ChasComBrdBES110_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_48TStore = _S5ChasComBrdBES110_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 759, 0)
)
_S5ChasComBrdBES110_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_48TStoreFlash = _S5ChasComBrdBES110_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 759, 0, 1)
)
_S5ChasComBrdBES110_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_48TStoreBootFW = _S5ChasComBrdBES110_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 759, 0, 2)
)
_S5ChasComBrdBES110_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES110_48TStoreDram = _S5ChasComBrdBES110_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 759, 0, 3)
)
_S5ChasComBrdBES120_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWR = _S5ChasComBrdBES120_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760)
)
_S5ChasComBrdBES120_24T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWRStore = _S5ChasComBrdBES120_24T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760, 0)
)
_S5ChasComBrdBES120_24T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWRStoreFlash = _S5ChasComBrdBES120_24T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760, 0, 1)
)
_S5ChasComBrdBES120_24T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWRStoreBootFW = _S5ChasComBrdBES120_24T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760, 0, 2)
)
_S5ChasComBrdBES120_24T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWRStoreDram = _S5ChasComBrdBES120_24T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760, 0, 3)
)
_S5ChasComBrdBES120_24T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_24T_PWRStorePoLFlash = _S5ChasComBrdBES120_24T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 760, 0, 4)
)
_S5ChasComBrdBES120_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWR = _S5ChasComBrdBES120_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761)
)
_S5ChasComBrdBES120_48T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWRStore = _S5ChasComBrdBES120_48T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761, 0)
)
_S5ChasComBrdBES120_48T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWRStoreFlash = _S5ChasComBrdBES120_48T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761, 0, 1)
)
_S5ChasComBrdBES120_48T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWRStoreBootFW = _S5ChasComBrdBES120_48T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761, 0, 2)
)
_S5ChasComBrdBES120_48T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWRStoreDram = _S5ChasComBrdBES120_48T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761, 0, 3)
)
_S5ChasComBrdBES120_48T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES120_48T_PWRStorePoLFlash = _S5ChasComBrdBES120_48T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 761, 0, 4)
)
_S5ChasComBrdBES210_24T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_24T = _S5ChasComBrdBES210_24T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 762)
)
_S5ChasComBrdBES210_24TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_24TStore = _S5ChasComBrdBES210_24TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 762, 0)
)
_S5ChasComBrdBES210_24TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_24TStoreFlash = _S5ChasComBrdBES210_24TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 762, 0, 1)
)
_S5ChasComBrdBES210_24TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_24TStoreBootFW = _S5ChasComBrdBES210_24TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 762, 0, 2)
)
_S5ChasComBrdBES210_24TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_24TStoreDram = _S5ChasComBrdBES210_24TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 762, 0, 3)
)
_S5ChasComBrdBES210_48T_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_48T = _S5ChasComBrdBES210_48T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 763)
)
_S5ChasComBrdBES210_48TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_48TStore = _S5ChasComBrdBES210_48TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 763, 0)
)
_S5ChasComBrdBES210_48TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_48TStoreFlash = _S5ChasComBrdBES210_48TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 763, 0, 1)
)
_S5ChasComBrdBES210_48TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_48TStoreBootFW = _S5ChasComBrdBES210_48TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 763, 0, 2)
)
_S5ChasComBrdBES210_48TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES210_48TStoreDram = _S5ChasComBrdBES210_48TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 763, 0, 3)
)
_S5ChasComBrdBES220_24T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWR = _S5ChasComBrdBES220_24T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764)
)
_S5ChasComBrdBES220_24T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWRStore = _S5ChasComBrdBES220_24T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764, 0)
)
_S5ChasComBrdBES220_24T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWRStoreFlash = _S5ChasComBrdBES220_24T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764, 0, 1)
)
_S5ChasComBrdBES220_24T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWRStoreBootFW = _S5ChasComBrdBES220_24T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764, 0, 2)
)
_S5ChasComBrdBES220_24T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWRStoreDram = _S5ChasComBrdBES220_24T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764, 0, 3)
)
_S5ChasComBrdBES220_24T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_24T_PWRStorePoLFlash = _S5ChasComBrdBES220_24T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 764, 0, 4)
)
_S5ChasComBrdBES220_48T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWR = _S5ChasComBrdBES220_48T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765)
)
_S5ChasComBrdBES220_48T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWRStore = _S5ChasComBrdBES220_48T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765, 0)
)
_S5ChasComBrdBES220_48T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWRStoreFlash = _S5ChasComBrdBES220_48T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765, 0, 1)
)
_S5ChasComBrdBES220_48T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWRStoreBootFW = _S5ChasComBrdBES220_48T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765, 0, 2)
)
_S5ChasComBrdBES220_48T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWRStoreDram = _S5ChasComBrdBES220_48T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765, 0, 3)
)
_S5ChasComBrdBES220_48T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdBES220_48T_PWRStorePoLFlash = _S5ChasComBrdBES220_48T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 765, 0, 4)
)
_S5ChasComBrdERS4548GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT = _S5ChasComBrdERS4548GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766)
)
_S5ChasComBrdERS4548GTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStore = _S5ChasComBrdERS4548GTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0)
)
_S5ChasComBrdERS4548GTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreFlash = _S5ChasComBrdERS4548GTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 1)
)
_S5ChasComBrdERS4548GTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreBootFW = _S5ChasComBrdERS4548GTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 2)
)
_S5ChasComBrdERS4548GTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreDram = _S5ChasComBrdERS4548GTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 3)
)
_S5ChasComBrdERS4548GTStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreSecondaryFlash = _S5ChasComBrdERS4548GTStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 5)
)
_S5ChasComBrdERS4548GTStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreCPLD = _S5ChasComBrdERS4548GTStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 6)
)
_S5ChasComBrdERS4548GTStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreInstalledFW = _S5ChasComBrdERS4548GTStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 7)
)
_S5ChasComBrdERS4548GTStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreOperSW = _S5ChasComBrdERS4548GTStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 8)
)
_S5ChasComBrdERS4548GTStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreTotal = _S5ChasComBrdERS4548GTStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 9)
)
_S5ChasComBrdERS4548GTStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreBootLoader = _S5ChasComBrdERS4548GTStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 10)
)
_S5ChasComBrdERS4548GTStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreConfig = _S5ChasComBrdERS4548GTStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 11)
)
_S5ChasComBrdERS4548GTStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreSecondaryConfig = _S5ChasComBrdERS4548GTStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 12)
)
_S5ChasComBrdERS4548GTStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreAutoBakupConfig = _S5ChasComBrdERS4548GTStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 13)
)
_S5ChasComBrdERS4548GTStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GTStoreReserved = _S5ChasComBrdERS4548GTStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 766, 0, 14)
)
_S5ChasComBrdERS4548GT_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWR = _S5ChasComBrdERS4548GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767)
)
_S5ChasComBrdERS4548GT_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStore = _S5ChasComBrdERS4548GT_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0)
)
_S5ChasComBrdERS4548GT_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreFlash = _S5ChasComBrdERS4548GT_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 1)
)
_S5ChasComBrdERS4548GT_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreBootFW = _S5ChasComBrdERS4548GT_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 2)
)
_S5ChasComBrdERS4548GT_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreDram = _S5ChasComBrdERS4548GT_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 3)
)
_S5ChasComBrdERS4548GT_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStorePoLFlash = _S5ChasComBrdERS4548GT_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 4)
)
_S5ChasComBrdERS4548GT_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreSecondaryFlash = _S5ChasComBrdERS4548GT_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 5)
)
_S5ChasComBrdERS4548GT_PWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreCPLD = _S5ChasComBrdERS4548GT_PWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 6)
)
_S5ChasComBrdERS4548GT_PWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreInstalledFW = _S5ChasComBrdERS4548GT_PWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 7)
)
_S5ChasComBrdERS4548GT_PWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreOperSW = _S5ChasComBrdERS4548GT_PWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 8)
)
_S5ChasComBrdERS4548GT_PWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreTotal = _S5ChasComBrdERS4548GT_PWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 9)
)
_S5ChasComBrdERS4548GT_PWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreBootLoader = _S5ChasComBrdERS4548GT_PWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 10)
)
_S5ChasComBrdERS4548GT_PWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreConfig = _S5ChasComBrdERS4548GT_PWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 11)
)
_S5ChasComBrdERS4548GT_PWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreSecondaryConfig = _S5ChasComBrdERS4548GT_PWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 12)
)
_S5ChasComBrdERS4548GT_PWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreAutoBakupConfig = _S5ChasComBrdERS4548GT_PWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 13)
)
_S5ChasComBrdERS4548GT_PWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4548GT_PWRStoreReserved = _S5ChasComBrdERS4548GT_PWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 767, 0, 14)
)
_S5ChasComBrdERS4550T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T = _S5ChasComBrdERS4550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768)
)
_S5ChasComBrdERS4550TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStore = _S5ChasComBrdERS4550TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0)
)
_S5ChasComBrdERS4550TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreFlash = _S5ChasComBrdERS4550TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 1)
)
_S5ChasComBrdERS4550TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreBootFW = _S5ChasComBrdERS4550TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 2)
)
_S5ChasComBrdERS4550TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreDram = _S5ChasComBrdERS4550TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 3)
)
_S5ChasComBrdERS4550TStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreSecondaryFlash = _S5ChasComBrdERS4550TStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 5)
)
_S5ChasComBrdERS4550TStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreCPLD = _S5ChasComBrdERS4550TStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 6)
)
_S5ChasComBrdERS4550TStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreInstalledFW = _S5ChasComBrdERS4550TStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 7)
)
_S5ChasComBrdERS4550TStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreOperSW = _S5ChasComBrdERS4550TStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 8)
)
_S5ChasComBrdERS4550TStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreTotal = _S5ChasComBrdERS4550TStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 9)
)
_S5ChasComBrdERS4550TStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreBootLoader = _S5ChasComBrdERS4550TStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 10)
)
_S5ChasComBrdERS4550TStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreConfig = _S5ChasComBrdERS4550TStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 11)
)
_S5ChasComBrdERS4550TStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreSecondaryConfig = _S5ChasComBrdERS4550TStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 12)
)
_S5ChasComBrdERS4550TStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreAutoBakupConfig = _S5ChasComBrdERS4550TStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 13)
)
_S5ChasComBrdERS4550TStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550TStoreReserved = _S5ChasComBrdERS4550TStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 768, 0, 14)
)
_S5ChasComBrdERS4550T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR = _S5ChasComBrdERS4550T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769)
)
_S5ChasComBrdERS4550T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStore = _S5ChasComBrdERS4550T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0)
)
_S5ChasComBrdERS4550T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreFlash = _S5ChasComBrdERS4550T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 1)
)
_S5ChasComBrdERS4550T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreBootFW = _S5ChasComBrdERS4550T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 2)
)
_S5ChasComBrdERS4550T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreDram = _S5ChasComBrdERS4550T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 3)
)
_S5ChasComBrdERS4550T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStorePoLFlash = _S5ChasComBrdERS4550T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 4)
)
_S5ChasComBrdERS4550T_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreSecondaryFlash = _S5ChasComBrdERS4550T_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 5)
)
_S5ChasComBrdERS4550T_PWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreCPLD = _S5ChasComBrdERS4550T_PWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 6)
)
_S5ChasComBrdERS4550T_PWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreInstalledFW = _S5ChasComBrdERS4550T_PWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 7)
)
_S5ChasComBrdERS4550T_PWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreOperSW = _S5ChasComBrdERS4550T_PWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 8)
)
_S5ChasComBrdERS4550T_PWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreTotal = _S5ChasComBrdERS4550T_PWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 9)
)
_S5ChasComBrdERS4550T_PWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreBootLoader = _S5ChasComBrdERS4550T_PWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 10)
)
_S5ChasComBrdERS4550T_PWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreConfig = _S5ChasComBrdERS4550T_PWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 11)
)
_S5ChasComBrdERS4550T_PWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreSecondaryConfig = _S5ChasComBrdERS4550T_PWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 12)
)
_S5ChasComBrdERS4550T_PWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreAutoBakupConfig = _S5ChasComBrdERS4550T_PWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 13)
)
_S5ChasComBrdERS4550T_PWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWRStoreReserved = _S5ChasComBrdERS4550T_PWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 769, 0, 14)
)
_S5ChasComBrdERS4526FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FX = _S5ChasComBrdERS4526FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770)
)
_S5ChasComBrdERS4526FXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStore = _S5ChasComBrdERS4526FXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0)
)
_S5ChasComBrdERS4526FXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreFlash = _S5ChasComBrdERS4526FXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 1)
)
_S5ChasComBrdERS4526FXStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreBootFW = _S5ChasComBrdERS4526FXStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 2)
)
_S5ChasComBrdERS4526FXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreDram = _S5ChasComBrdERS4526FXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 3)
)
_S5ChasComBrdERS4526FXStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreSecondaryFlash = _S5ChasComBrdERS4526FXStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 5)
)
_S5ChasComBrdERS4526FXStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreCPLD = _S5ChasComBrdERS4526FXStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 6)
)
_S5ChasComBrdERS4526FXStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreInstalledFW = _S5ChasComBrdERS4526FXStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 7)
)
_S5ChasComBrdERS4526FXStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreOperSW = _S5ChasComBrdERS4526FXStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 8)
)
_S5ChasComBrdERS4526FXStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreTotal = _S5ChasComBrdERS4526FXStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 9)
)
_S5ChasComBrdERS4526FXStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreBootLoader = _S5ChasComBrdERS4526FXStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 10)
)
_S5ChasComBrdERS4526FXStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreConfig = _S5ChasComBrdERS4526FXStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 11)
)
_S5ChasComBrdERS4526FXStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreSecondaryConfig = _S5ChasComBrdERS4526FXStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 12)
)
_S5ChasComBrdERS4526FXStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreAutoBakupConfig = _S5ChasComBrdERS4526FXStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 13)
)
_S5ChasComBrdERS4526FXStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526FXStoreReserved = _S5ChasComBrdERS4526FXStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 770, 0, 14)
)
_S5ChasComBrdERS2500_26T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T = _S5ChasComBrdERS2500_26T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771)
)
_S5ChasComBrdERS2500_26TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26TStore = _S5ChasComBrdERS2500_26TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771, 0)
)
_S5ChasComBrdERS2500_26TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26TStoreFlash = _S5ChasComBrdERS2500_26TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771, 0, 1)
)
_S5ChasComBrdERS2500_26TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26TStoreBootFW = _S5ChasComBrdERS2500_26TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771, 0, 2)
)
_S5ChasComBrdERS2500_26TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26TStoreDram = _S5ChasComBrdERS2500_26TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771, 0, 3)
)
_S5ChasComBrdERS2500_26TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26TStorePoLFlash = _S5ChasComBrdERS2500_26TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 771, 0, 4)
)
_S5ChasComBrdERS2500_26T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWR = _S5ChasComBrdERS2500_26T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772)
)
_S5ChasComBrdERS2500_26T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWRStore = _S5ChasComBrdERS2500_26T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772, 0)
)
_S5ChasComBrdERS2500_26T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWRStoreFlash = _S5ChasComBrdERS2500_26T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772, 0, 1)
)
_S5ChasComBrdERS2500_26T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWRStoreBootFW = _S5ChasComBrdERS2500_26T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772, 0, 2)
)
_S5ChasComBrdERS2500_26T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWRStoreDram = _S5ChasComBrdERS2500_26T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772, 0, 3)
)
_S5ChasComBrdERS2500_26T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_26T_PWRStorePoLFlash = _S5ChasComBrdERS2500_26T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 772, 0, 4)
)
_S5ChasComBrdERS2500_50T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T = _S5ChasComBrdERS2500_50T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773)
)
_S5ChasComBrdERS2500_50TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50TStore = _S5ChasComBrdERS2500_50TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773, 0)
)
_S5ChasComBrdERS2500_50TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50TStoreFlash = _S5ChasComBrdERS2500_50TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773, 0, 1)
)
_S5ChasComBrdERS2500_50TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50TStoreBootFW = _S5ChasComBrdERS2500_50TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773, 0, 2)
)
_S5ChasComBrdERS2500_50TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50TStoreDram = _S5ChasComBrdERS2500_50TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773, 0, 3)
)
_S5ChasComBrdERS2500_50TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50TStorePoLFlash = _S5ChasComBrdERS2500_50TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 773, 0, 4)
)
_S5ChasComBrdERS2500_50T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWR = _S5ChasComBrdERS2500_50T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774)
)
_S5ChasComBrdERS2500_50T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWRStore = _S5ChasComBrdERS2500_50T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774, 0)
)
_S5ChasComBrdERS2500_50T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWRStoreFlash = _S5ChasComBrdERS2500_50T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774, 0, 1)
)
_S5ChasComBrdERS2500_50T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWRStoreBootFW = _S5ChasComBrdERS2500_50T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774, 0, 2)
)
_S5ChasComBrdERS2500_50T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWRStoreDram = _S5ChasComBrdERS2500_50T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774, 0, 3)
)
_S5ChasComBrdERS2500_50T_PWRStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS2500_50T_PWRStorePoLFlash = _S5ChasComBrdERS2500_50T_PWRStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 774, 0, 4)
)
_S5ChasComBrdERS4526GTX_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWR = _S5ChasComBrdERS4526GTX_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775)
)
_S5ChasComBrdERS4526GTX_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStore = _S5ChasComBrdERS4526GTX_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0)
)
_S5ChasComBrdERS4526GTX_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreFlash = _S5ChasComBrdERS4526GTX_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 1)
)
_S5ChasComBrdERS4526GTX_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreBootFW = _S5ChasComBrdERS4526GTX_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 2)
)
_S5ChasComBrdERS4526GTX_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreDram = _S5ChasComBrdERS4526GTX_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 3)
)
_S5ChasComBrdERS4526GTX_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreSecondaryFlash = _S5ChasComBrdERS4526GTX_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 5)
)
_S5ChasComBrdERS4526GTX_PWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreCPLD = _S5ChasComBrdERS4526GTX_PWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 6)
)
_S5ChasComBrdERS4526GTX_PWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreInstalledFW = _S5ChasComBrdERS4526GTX_PWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 7)
)
_S5ChasComBrdERS4526GTX_PWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreOperSW = _S5ChasComBrdERS4526GTX_PWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 8)
)
_S5ChasComBrdERS4526GTX_PWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreTotal = _S5ChasComBrdERS4526GTX_PWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 9)
)
_S5ChasComBrdERS4526GTX_PWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreBootLoader = _S5ChasComBrdERS4526GTX_PWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 10)
)
_S5ChasComBrdERS4526GTX_PWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreConfig = _S5ChasComBrdERS4526GTX_PWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 11)
)
_S5ChasComBrdERS4526GTX_PWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreSecondaryConfig = _S5ChasComBrdERS4526GTX_PWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 12)
)
_S5ChasComBrdERS4526GTX_PWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreAutoBakupConfig = _S5ChasComBrdERS4526GTX_PWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 13)
)
_S5ChasComBrdERS4526GTX_PWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX_PWRStoreReserved = _S5ChasComBrdERS4526GTX_PWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 775, 0, 14)
)
_S5ChasComBrdERS4526GTX_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTX = _S5ChasComBrdERS4526GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776)
)
_S5ChasComBrdERS4526GTXStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStore = _S5ChasComBrdERS4526GTXStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0)
)
_S5ChasComBrdERS4526GTXStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreFlash = _S5ChasComBrdERS4526GTXStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 1)
)
_S5ChasComBrdERS4526GTXStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreBootFW = _S5ChasComBrdERS4526GTXStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 2)
)
_S5ChasComBrdERS4526GTXStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreDram = _S5ChasComBrdERS4526GTXStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 3)
)
_S5ChasComBrdERS4526GTXStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreSecondaryFlash = _S5ChasComBrdERS4526GTXStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 5)
)
_S5ChasComBrdERS4526GTXStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreCPLD = _S5ChasComBrdERS4526GTXStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 6)
)
_S5ChasComBrdERS4526GTXStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreInstalledFW = _S5ChasComBrdERS4526GTXStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 7)
)
_S5ChasComBrdERS4526GTXStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreOperSW = _S5ChasComBrdERS4526GTXStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 8)
)
_S5ChasComBrdERS4526GTXStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreTotal = _S5ChasComBrdERS4526GTXStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 9)
)
_S5ChasComBrdERS4526GTXStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreBootLoader = _S5ChasComBrdERS4526GTXStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 10)
)
_S5ChasComBrdERS4526GTXStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreConfig = _S5ChasComBrdERS4526GTXStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 11)
)
_S5ChasComBrdERS4526GTXStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreSecondaryConfig = _S5ChasComBrdERS4526GTXStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 12)
)
_S5ChasComBrdERS4526GTXStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreAutoBakupConfig = _S5ChasComBrdERS4526GTXStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 13)
)
_S5ChasComBrdERS4526GTXStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526GTXStoreReserved = _S5ChasComBrdERS4526GTXStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 776, 0, 14)
)
_S5ChasComBrdERS4524GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT = _S5ChasComBrdERS4524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777)
)
_S5ChasComBrdERS4524GTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStore = _S5ChasComBrdERS4524GTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0)
)
_S5ChasComBrdERS4524GTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreFlash = _S5ChasComBrdERS4524GTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 1)
)
_S5ChasComBrdERS4524GTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreBootFW = _S5ChasComBrdERS4524GTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 2)
)
_S5ChasComBrdERS4524GTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreDram = _S5ChasComBrdERS4524GTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 3)
)
_S5ChasComBrdERS4524GTStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreSecondaryFlash = _S5ChasComBrdERS4524GTStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 5)
)
_S5ChasComBrdERS4524GTStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreCPLD = _S5ChasComBrdERS4524GTStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 6)
)
_S5ChasComBrdERS4524GTStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreInstalledFW = _S5ChasComBrdERS4524GTStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 7)
)
_S5ChasComBrdERS4524GTStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreOperSW = _S5ChasComBrdERS4524GTStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 8)
)
_S5ChasComBrdERS4524GTStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreTotal = _S5ChasComBrdERS4524GTStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 9)
)
_S5ChasComBrdERS4524GTStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreBootLoader = _S5ChasComBrdERS4524GTStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 10)
)
_S5ChasComBrdERS4524GTStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreConfig = _S5ChasComBrdERS4524GTStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 11)
)
_S5ChasComBrdERS4524GTStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreSecondaryConfig = _S5ChasComBrdERS4524GTStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 12)
)
_S5ChasComBrdERS4524GTStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreAutoBakupConfig = _S5ChasComBrdERS4524GTStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 13)
)
_S5ChasComBrdERS4524GTStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GTStoreReserved = _S5ChasComBrdERS4524GTStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 777, 0, 14)
)
_S5ChasComBrdERS4526T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T = _S5ChasComBrdERS4526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778)
)
_S5ChasComBrdERS4526TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStore = _S5ChasComBrdERS4526TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0)
)
_S5ChasComBrdERS4526TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreFlash = _S5ChasComBrdERS4526TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 1)
)
_S5ChasComBrdERS4526TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreBootFW = _S5ChasComBrdERS4526TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 2)
)
_S5ChasComBrdERS4526TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreDram = _S5ChasComBrdERS4526TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 3)
)
_S5ChasComBrdERS4526TStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreSecondaryFlash = _S5ChasComBrdERS4526TStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 5)
)
_S5ChasComBrdERS4526TStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreCPLD = _S5ChasComBrdERS4526TStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 6)
)
_S5ChasComBrdERS4526TStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreInstalledFW = _S5ChasComBrdERS4526TStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 7)
)
_S5ChasComBrdERS4526TStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreOperSW = _S5ChasComBrdERS4526TStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 8)
)
_S5ChasComBrdERS4526TStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreTotal = _S5ChasComBrdERS4526TStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 9)
)
_S5ChasComBrdERS4526TStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreBootLoader = _S5ChasComBrdERS4526TStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 10)
)
_S5ChasComBrdERS4526TStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreConfig = _S5ChasComBrdERS4526TStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 11)
)
_S5ChasComBrdERS4526TStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreSecondaryConfig = _S5ChasComBrdERS4526TStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 12)
)
_S5ChasComBrdERS4526TStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreAutoBakupConfig = _S5ChasComBrdERS4526TStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 13)
)
_S5ChasComBrdERS4526TStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526TStoreReserved = _S5ChasComBrdERS4526TStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 778, 0, 14)
)
_S5ChasComBrdERS4526T_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR = _S5ChasComBrdERS4526T_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779)
)
_S5ChasComBrdERS4526T_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStore = _S5ChasComBrdERS4526T_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0)
)
_S5ChasComBrdERS4526T_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreFlash = _S5ChasComBrdERS4526T_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 1)
)
_S5ChasComBrdERS4526T_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreBootFW = _S5ChasComBrdERS4526T_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 2)
)
_S5ChasComBrdERS4526T_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreDram = _S5ChasComBrdERS4526T_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 3)
)
_S5ChasComBrdERS4526T_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreSecondaryFlash = _S5ChasComBrdERS4526T_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 5)
)
_S5ChasComBrdERS4526T_PWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreCPLD = _S5ChasComBrdERS4526T_PWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 6)
)
_S5ChasComBrdERS4526T_PWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreInstalledFW = _S5ChasComBrdERS4526T_PWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 7)
)
_S5ChasComBrdERS4526T_PWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreOperSW = _S5ChasComBrdERS4526T_PWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 8)
)
_S5ChasComBrdERS4526T_PWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreTotal = _S5ChasComBrdERS4526T_PWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 9)
)
_S5ChasComBrdERS4526T_PWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreBootLoader = _S5ChasComBrdERS4526T_PWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 10)
)
_S5ChasComBrdERS4526T_PWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreConfig = _S5ChasComBrdERS4526T_PWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 11)
)
_S5ChasComBrdERS4526T_PWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreSecondaryConfig = _S5ChasComBrdERS4526T_PWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 12)
)
_S5ChasComBrdERS4526T_PWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreAutoBakupConfig = _S5ChasComBrdERS4526T_PWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 13)
)
_S5ChasComBrdERS4526T_PWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWRStoreReserved = _S5ChasComBrdERS4526T_PWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 779, 0, 14)
)
_S5ChasComBrdUsb_ObjectIdentity = ObjectIdentity
s5ChasComBrdUsb = _S5ChasComBrdUsb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 780)
)
_S5ChasComBrdUsb_None_ObjectIdentity = ObjectIdentity
s5ChasComBrdUsb_None = _S5ChasComBrdUsb_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 780, 1)
)
_S5ChasComBrdUsb_Flash_ObjectIdentity = ObjectIdentity
s5ChasComBrdUsb_Flash = _S5ChasComBrdUsb_Flash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 780, 2)
)
_S5ChasComBrdERS5698_TFD_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWR = _S5ChasComBrdERS5698_TFD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781)
)
_S5ChasComBrdERS5698_TFD_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStore = _S5ChasComBrdERS5698_TFD_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0)
)
_S5ChasComBrdERS5698_TFD_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStoreFlash = _S5ChasComBrdERS5698_TFD_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0, 1)
)
_S5ChasComBrdERS5698_TFD_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStoreBootFW = _S5ChasComBrdERS5698_TFD_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0, 2)
)
_S5ChasComBrdERS5698_TFD_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStoreDram = _S5ChasComBrdERS5698_TFD_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0, 3)
)
_S5ChasComBrdERS5698_TFD_PWRStorePol_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStorePol = _S5ChasComBrdERS5698_TFD_PWRStorePol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0, 4)
)
_S5ChasComBrdERS5698_TFD_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD_PWRStoreSecondaryFlash = _S5ChasComBrdERS5698_TFD_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 781, 0, 5)
)
_S5ChasComBrdERS5698_TFD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFD = _S5ChasComBrdERS5698_TFD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782)
)
_S5ChasComBrdERS5698_TFDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFDStore = _S5ChasComBrdERS5698_TFDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782, 0)
)
_S5ChasComBrdERS5698_TFDStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFDStoreFlash = _S5ChasComBrdERS5698_TFDStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782, 0, 1)
)
_S5ChasComBrdERS5698_TFDStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFDStoreBootFW = _S5ChasComBrdERS5698_TFDStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782, 0, 2)
)
_S5ChasComBrdERS5698_TFDStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFDStoreDram = _S5ChasComBrdERS5698_TFDStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782, 0, 3)
)
_S5ChasComBrdERS5698_TFDStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5698_TFDStoreSecondaryFlash = _S5ChasComBrdERS5698_TFDStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 782, 0, 5)
)
_S5ChasComBrdERS5650_TD_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWR = _S5ChasComBrdERS5650_TD_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783)
)
_S5ChasComBrdERS5650_TD_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStore = _S5ChasComBrdERS5650_TD_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0)
)
_S5ChasComBrdERS5650_TD_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStoreFlash = _S5ChasComBrdERS5650_TD_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0, 1)
)
_S5ChasComBrdERS5650_TD_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStoreBootFW = _S5ChasComBrdERS5650_TD_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0, 2)
)
_S5ChasComBrdERS5650_TD_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStoreDram = _S5ChasComBrdERS5650_TD_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0, 3)
)
_S5ChasComBrdERS5650_TD_PWRStorePol_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStorePol = _S5ChasComBrdERS5650_TD_PWRStorePol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0, 4)
)
_S5ChasComBrdERS5650_TD_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD_PWRStoreSecondaryFlash = _S5ChasComBrdERS5650_TD_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 783, 0, 5)
)
_S5ChasComBrdERS5650_TD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TD = _S5ChasComBrdERS5650_TD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784)
)
_S5ChasComBrdERS5650_TDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TDStore = _S5ChasComBrdERS5650_TDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784, 0)
)
_S5ChasComBrdERS5650_TDStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TDStoreFlash = _S5ChasComBrdERS5650_TDStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784, 0, 1)
)
_S5ChasComBrdERS5650_TDStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TDStoreBootFW = _S5ChasComBrdERS5650_TDStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784, 0, 2)
)
_S5ChasComBrdERS5650_TDStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TDStoreDram = _S5ChasComBrdERS5650_TDStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784, 0, 3)
)
_S5ChasComBrdERS5650_TDStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5650_TDStoreSecondaryFlash = _S5ChasComBrdERS5650_TDStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 784, 0, 5)
)
_S5ChasComBrdERS5632_FD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FD = _S5ChasComBrdERS5632_FD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785)
)
_S5ChasComBrdERS5632_FDStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FDStore = _S5ChasComBrdERS5632_FDStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785, 0)
)
_S5ChasComBrdERS5632_FDStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FDStoreFlash = _S5ChasComBrdERS5632_FDStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785, 0, 1)
)
_S5ChasComBrdERS5632_FDStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FDStoreBootFW = _S5ChasComBrdERS5632_FDStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785, 0, 2)
)
_S5ChasComBrdERS5632_FDStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FDStoreDram = _S5ChasComBrdERS5632_FDStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785, 0, 3)
)
_S5ChasComBrdERS5632_FDStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5632_FDStoreSecondaryFlash = _S5ChasComBrdERS5632_FDStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 785, 0, 5)
)
_S5ChasComBrdESU1860S_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860S = _S5ChasComBrdESU1860S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786)
)
_S5ChasComBrdESU1860SStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStore = _S5ChasComBrdESU1860SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0)
)
_S5ChasComBrdESU1860SStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStoreFlash = _S5ChasComBrdESU1860SStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0, 1)
)
_S5ChasComBrdESU1860SStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStoreBootFW = _S5ChasComBrdESU1860SStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0, 2)
)
_S5ChasComBrdESU1860SStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStoreDram = _S5ChasComBrdESU1860SStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0, 3)
)
_S5ChasComBrdESU1860SStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStoreSecondaryFlash = _S5ChasComBrdESU1860SStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0, 5)
)
_S5ChasComBrdESU1860SStoreCpld_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860SStoreCpld = _S5ChasComBrdESU1860SStoreCpld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 786, 0, 6)
)
_S5ChasComBrdESU1860B_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860B = _S5ChasComBrdESU1860B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787)
)
_S5ChasComBrdESU1860BStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStore = _S5ChasComBrdESU1860BStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0)
)
_S5ChasComBrdESU1860BStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStoreFlash = _S5ChasComBrdESU1860BStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0, 1)
)
_S5ChasComBrdESU1860BStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStoreBootFW = _S5ChasComBrdESU1860BStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0, 2)
)
_S5ChasComBrdESU1860BStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStoreDram = _S5ChasComBrdESU1860BStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0, 3)
)
_S5ChasComBrdESU1860BStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStoreSecondaryFlash = _S5ChasComBrdESU1860BStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0, 5)
)
_S5ChasComBrdESU1860BStoreCpld_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860BStoreCpld = _S5ChasComBrdESU1860BStoreCpld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 787, 0, 6)
)
_S5ChasComBrdESU1860T_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860T = _S5ChasComBrdESU1860T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788)
)
_S5ChasComBrdESU1860TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStore = _S5ChasComBrdESU1860TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0)
)
_S5ChasComBrdESU1860TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStoreFlash = _S5ChasComBrdESU1860TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0, 1)
)
_S5ChasComBrdESU1860TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStoreBootFW = _S5ChasComBrdESU1860TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0, 2)
)
_S5ChasComBrdESU1860TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStoreDram = _S5ChasComBrdESU1860TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0, 3)
)
_S5ChasComBrdESU1860TStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStoreSecondaryFlash = _S5ChasComBrdESU1860TStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0, 5)
)
_S5ChasComBrdESU1860TStoreCpld_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860TStoreCpld = _S5ChasComBrdESU1860TStoreCpld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 788, 0, 6)
)
_S5ChasComBrdESU1860V_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860V = _S5ChasComBrdESU1860V_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789)
)
_S5ChasComBrdESU1860VStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStore = _S5ChasComBrdESU1860VStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0)
)
_S5ChasComBrdESU1860VStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStoreFlash = _S5ChasComBrdESU1860VStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0, 1)
)
_S5ChasComBrdESU1860VStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStoreBootFW = _S5ChasComBrdESU1860VStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0, 2)
)
_S5ChasComBrdESU1860VStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStoreDram = _S5ChasComBrdESU1860VStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0, 3)
)
_S5ChasComBrdESU1860VStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStoreSecondaryFlash = _S5ChasComBrdESU1860VStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0, 5)
)
_S5ChasComBrdESU1860VStoreCpld_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860VStoreCpld = _S5ChasComBrdESU1860VStoreCpld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 789, 0, 6)
)
_S5ChasComBrdESU1880S_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880S = _S5ChasComBrdESU1880S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790)
)
_S5ChasComBrdESU1880SStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStore = _S5ChasComBrdESU1880SStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0)
)
_S5ChasComBrdESU1880SStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStoreFlash = _S5ChasComBrdESU1880SStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0, 1)
)
_S5ChasComBrdESU1880SStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStoreBootFW = _S5ChasComBrdESU1880SStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0, 2)
)
_S5ChasComBrdESU1880SStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStoreDram = _S5ChasComBrdESU1880SStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0, 3)
)
_S5ChasComBrdESU1880SStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStoreSecondaryFlash = _S5ChasComBrdESU1880SStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0, 5)
)
_S5ChasComBrdESU1880SStoreCpld_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880SStoreCpld = _S5ChasComBrdESU1880SStoreCpld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 790, 0, 6)
)
_S5ChasComBrdESU1860_2TX_FX_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1860_2TX_FX = _S5ChasComBrdESU1860_2TX_FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 791)
)
_S5ChasComBrdESU1880_2ST_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880_2ST = _S5ChasComBrdESU1880_2ST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 792)
)
_S5ChasComBrdESU1880_2DC_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880_2DC = _S5ChasComBrdESU1880_2DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 793)
)
_S5ChasComBrdESU1880_2XFP_ObjectIdentity = ObjectIdentity
s5ChasComBrdESU1880_2XFP = _S5ChasComBrdESU1880_2XFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 794)
)
_S5ChasComBrdERS4524GT_PWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWR = _S5ChasComBrdERS4524GT_PWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795)
)
_S5ChasComBrdERS4524GT_PWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStore = _S5ChasComBrdERS4524GT_PWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0)
)
_S5ChasComBrdERS4524GT_PWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreFlash = _S5ChasComBrdERS4524GT_PWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 1)
)
_S5ChasComBrdERS4524GT_PWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreBootFW = _S5ChasComBrdERS4524GT_PWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 2)
)
_S5ChasComBrdERS4524GT_PWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreDram = _S5ChasComBrdERS4524GT_PWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 3)
)
_S5ChasComBrdERS4524GT_PWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreSecondaryFlash = _S5ChasComBrdERS4524GT_PWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 5)
)
_S5ChasComBrdERS4524GT_PWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreCPLD = _S5ChasComBrdERS4524GT_PWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 6)
)
_S5ChasComBrdERS4524GT_PWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreInstalledFW = _S5ChasComBrdERS4524GT_PWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 7)
)
_S5ChasComBrdERS4524GT_PWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreOperSW = _S5ChasComBrdERS4524GT_PWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 8)
)
_S5ChasComBrdERS4524GT_PWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreTotal = _S5ChasComBrdERS4524GT_PWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 9)
)
_S5ChasComBrdERS4524GT_PWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreBootLoader = _S5ChasComBrdERS4524GT_PWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 10)
)
_S5ChasComBrdERS4524GT_PWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreConfig = _S5ChasComBrdERS4524GT_PWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 11)
)
_S5ChasComBrdERS4524GT_PWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreSecondaryConfig = _S5ChasComBrdERS4524GT_PWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 12)
)
_S5ChasComBrdERS4524GT_PWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreAutoBakupConfig = _S5ChasComBrdERS4524GT_PWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 13)
)
_S5ChasComBrdERS4524GT_PWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4524GT_PWRStoreReserved = _S5ChasComBrdERS4524GT_PWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 795, 0, 14)
)
_S5ChasComBrdERS6628XSGT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGT = _S5ChasComBrdERS6628XSGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796)
)
_S5ChasComBrdERS6628XSGTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGTStore = _S5ChasComBrdERS6628XSGTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796, 0)
)
_S5ChasComBrdERS6628XSGTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGTStoreFlash = _S5ChasComBrdERS6628XSGTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796, 0, 1)
)
_S5ChasComBrdERS6628XSGTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGTStoreBootFW = _S5ChasComBrdERS6628XSGTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796, 0, 2)
)
_S5ChasComBrdERS6628XSGTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGTStoreDram = _S5ChasComBrdERS6628XSGTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796, 0, 3)
)
_S5ChasComBrdERS6628XSGTStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6628XSGTStoreSecondaryFlash = _S5ChasComBrdERS6628XSGTStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 796, 0, 5)
)
_S5ChasComBrdERS6632XTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTS = _S5ChasComBrdERS6632XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797)
)
_S5ChasComBrdERS6632XTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTSStore = _S5ChasComBrdERS6632XTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797, 0)
)
_S5ChasComBrdERS6632XTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTSStoreFlash = _S5ChasComBrdERS6632XTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797, 0, 1)
)
_S5ChasComBrdERS6632XTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTSStoreBootFW = _S5ChasComBrdERS6632XTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797, 0, 2)
)
_S5ChasComBrdERS6632XTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTSStoreDram = _S5ChasComBrdERS6632XTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797, 0, 3)
)
_S5ChasComBrdERS6632XTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS6632XTSStoreSecondaryFlash = _S5ChasComBrdERS6632XTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 797, 0, 5)
)
_S5ChasComBrdWC8180_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180 = _S5ChasComBrdWC8180_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798)
)
_S5ChasComBrdWC8180Store_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180Store = _S5ChasComBrdWC8180Store_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798, 0)
)
_S5ChasComBrdWC8180StoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180StoreFlash = _S5ChasComBrdWC8180StoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798, 0, 1)
)
_S5ChasComBrdWC8180StoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180StoreBootFW = _S5ChasComBrdWC8180StoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798, 0, 2)
)
_S5ChasComBrdWC8180StoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180StoreDram = _S5ChasComBrdWC8180StoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798, 0, 3)
)
_S5ChasComBrdWC8180StoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdWC8180StoreSecondaryFlash = _S5ChasComBrdWC8180StoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 798, 0, 5)
)
_S5ChasComBrdERS4526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUS = _S5ChasComBrdERS4526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799)
)
_S5ChasComBrdERS4526T_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStore = _S5ChasComBrdERS4526T_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreFlash = _S5ChasComBrdERS4526T_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 1)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4526T_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 2)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreDram = _S5ChasComBrdERS4526T_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 3)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 5)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4526T_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 6)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4526T_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 7)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4526T_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 8)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreTotal = _S5ChasComBrdERS4526T_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 9)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4526T_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 10)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreConfig = _S5ChasComBrdERS4526T_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 11)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 12)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4526T_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 13)
)
_S5ChasComBrdERS4526T_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4526T_PWR_PLUSStoreReserved = _S5ChasComBrdERS4526T_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 799, 0, 14)
)
_S5ChasComBrdERS4550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUS = _S5ChasComBrdERS4550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800)
)
_S5ChasComBrdERS4550T_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStore = _S5ChasComBrdERS4550T_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreFlash = _S5ChasComBrdERS4550T_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 1)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4550T_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 2)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreDram = _S5ChasComBrdERS4550T_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 3)
)
_S5ChasComBrdERS4550T_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS4550T_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 4)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 5)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4550T_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 6)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4550T_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 7)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4550T_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 8)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreTotal = _S5ChasComBrdERS4550T_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 9)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4550T_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 10)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreConfig = _S5ChasComBrdERS4550T_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 11)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 12)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4550T_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 13)
)
_S5ChasComBrdERS4550T_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4550T_PWR_PLUSStoreReserved = _S5ChasComBrdERS4550T_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 800, 0, 14)
)
_S5ChasComBrdERS4826GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUS = _S5ChasComBrdERS4826GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStore = _S5ChasComBrdERS4826GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 1)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 2)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 3)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 5)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 6)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 7)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 8)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 9)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 10)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 11)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 12)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 13)
)
_S5ChasComBrdERS4826GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS4826GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 801, 0, 14)
)
_S5ChasComBrdERS4850GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUS = _S5ChasComBrdERS4850GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStore = _S5ChasComBrdERS4850GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 1)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 2)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 3)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS4850GTS_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 4)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 5)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 6)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 7)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 8)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 9)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 10)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 11)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 12)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 13)
)
_S5ChasComBrdERS4850GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS4850GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 802, 0, 14)
)
_S5ChasComBrdERS4826GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTS = _S5ChasComBrdERS4826GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803)
)
_S5ChasComBrdERS4826GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStore = _S5ChasComBrdERS4826GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0)
)
_S5ChasComBrdERS4826GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreFlash = _S5ChasComBrdERS4826GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 1)
)
_S5ChasComBrdERS4826GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreBootFW = _S5ChasComBrdERS4826GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 2)
)
_S5ChasComBrdERS4826GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreDram = _S5ChasComBrdERS4826GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 3)
)
_S5ChasComBrdERS4826GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreSecondaryFlash = _S5ChasComBrdERS4826GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 5)
)
_S5ChasComBrdERS4826GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreCPLD = _S5ChasComBrdERS4826GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 6)
)
_S5ChasComBrdERS4826GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreInstalledFW = _S5ChasComBrdERS4826GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 7)
)
_S5ChasComBrdERS4826GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreOperSW = _S5ChasComBrdERS4826GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 8)
)
_S5ChasComBrdERS4826GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreTotal = _S5ChasComBrdERS4826GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 9)
)
_S5ChasComBrdERS4826GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreBootLoader = _S5ChasComBrdERS4826GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 10)
)
_S5ChasComBrdERS4826GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreConfig = _S5ChasComBrdERS4826GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 11)
)
_S5ChasComBrdERS4826GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreSecondaryConfig = _S5ChasComBrdERS4826GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 12)
)
_S5ChasComBrdERS4826GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreAutoBakupConfig = _S5ChasComBrdERS4826GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 13)
)
_S5ChasComBrdERS4826GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4826GTSStoreReserved = _S5ChasComBrdERS4826GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 803, 0, 14)
)
_S5ChasComBrdERS4850GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTS = _S5ChasComBrdERS4850GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804)
)
_S5ChasComBrdERS4850GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStore = _S5ChasComBrdERS4850GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0)
)
_S5ChasComBrdERS4850GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreFlash = _S5ChasComBrdERS4850GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 1)
)
_S5ChasComBrdERS4850GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreBootFW = _S5ChasComBrdERS4850GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 2)
)
_S5ChasComBrdERS4850GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreDram = _S5ChasComBrdERS4850GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 3)
)
_S5ChasComBrdERS4850GTSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStorePoLFlash = _S5ChasComBrdERS4850GTSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 4)
)
_S5ChasComBrdERS4850GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreSecondaryFlash = _S5ChasComBrdERS4850GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 5)
)
_S5ChasComBrdERS4850GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreCPLD = _S5ChasComBrdERS4850GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 6)
)
_S5ChasComBrdERS4850GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreInstalledFW = _S5ChasComBrdERS4850GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 7)
)
_S5ChasComBrdERS4850GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreOperSW = _S5ChasComBrdERS4850GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 8)
)
_S5ChasComBrdERS4850GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreTotal = _S5ChasComBrdERS4850GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 9)
)
_S5ChasComBrdERS4850GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreBootLoader = _S5ChasComBrdERS4850GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 10)
)
_S5ChasComBrdERS4850GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreConfig = _S5ChasComBrdERS4850GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 11)
)
_S5ChasComBrdERS4850GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreSecondaryConfig = _S5ChasComBrdERS4850GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 12)
)
_S5ChasComBrdERS4850GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreAutoBakupConfig = _S5ChasComBrdERS4850GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 13)
)
_S5ChasComBrdERS4850GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4850GTSStoreReserved = _S5ChasComBrdERS4850GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 804, 0, 14)
)
_S5ChasComBrdVSP7024XLS_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLS = _S5ChasComBrdVSP7024XLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805)
)
_S5ChasComBrdVSP7024XLSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStore = _S5ChasComBrdVSP7024XLSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0)
)
_S5ChasComBrdVSP7024XLSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreFlash = _S5ChasComBrdVSP7024XLSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 1)
)
_S5ChasComBrdVSP7024XLSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreBootFW = _S5ChasComBrdVSP7024XLSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 2)
)
_S5ChasComBrdVSP7024XLSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreDram = _S5ChasComBrdVSP7024XLSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 3)
)
_S5ChasComBrdVSP7024XLSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStorePoLFlash = _S5ChasComBrdVSP7024XLSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 4)
)
_S5ChasComBrdVSP7024XLSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreSecondaryFlash = _S5ChasComBrdVSP7024XLSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 5)
)
_S5ChasComBrdVSP7024XLSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreCPLD = _S5ChasComBrdVSP7024XLSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 6)
)
_S5ChasComBrdVSP7024XLSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreInstalledFW = _S5ChasComBrdVSP7024XLSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 7)
)
_S5ChasComBrdVSP7024XLSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreOperSW = _S5ChasComBrdVSP7024XLSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 8)
)
_S5ChasComBrdVSP7024XLSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreTotal = _S5ChasComBrdVSP7024XLSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 9)
)
_S5ChasComBrdVSP7024XLSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreBootLoader = _S5ChasComBrdVSP7024XLSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 10)
)
_S5ChasComBrdVSP7024XLSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreConfig = _S5ChasComBrdVSP7024XLSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 11)
)
_S5ChasComBrdVSP7024XLSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreSecondaryConfig = _S5ChasComBrdVSP7024XLSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 12)
)
_S5ChasComBrdVSP7024XLSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreAutoBakupConfig = _S5ChasComBrdVSP7024XLSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 13)
)
_S5ChasComBrdVSP7024XLSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLSStoreReserved = _S5ChasComBrdVSP7024XLSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 805, 0, 14)
)
_S5ChasComBrdVSP7024XLS_7008XLS_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLS_7008XLS = _S5ChasComBrdVSP7024XLS_7008XLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 806)
)
_S5ChasComBrdVSP7024XLS_7008XLT_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XLS_7008XLT = _S5ChasComBrdVSP7024XLS_7008XLT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 807)
)
_S5ChasComBrdERS3510GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT = _S5ChasComBrdERS3510GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808)
)
_S5ChasComBrdERS3510GTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GTStore = _S5ChasComBrdERS3510GTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808, 0)
)
_S5ChasComBrdERS3510GTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GTStoreFlash = _S5ChasComBrdERS3510GTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808, 0, 1)
)
_S5ChasComBrdERS3510GTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GTStoreBootFW = _S5ChasComBrdERS3510GTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808, 0, 2)
)
_S5ChasComBrdERS3510GTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GTStoreDram = _S5ChasComBrdERS3510GTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808, 0, 3)
)
_S5ChasComBrdERS3510GTStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GTStorePoLFlash = _S5ChasComBrdERS3510GTStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 808, 0, 4)
)
_S5ChasComBrdERS3510GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUS = _S5ChasComBrdERS3510GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809)
)
_S5ChasComBrdERS3510GT_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUSStore = _S5ChasComBrdERS3510GT_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809, 0)
)
_S5ChasComBrdERS3510GT_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUSStoreFlash = _S5ChasComBrdERS3510GT_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809, 0, 1)
)
_S5ChasComBrdERS3510GT_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3510GT_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809, 0, 2)
)
_S5ChasComBrdERS3510GT_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUSStoreDram = _S5ChasComBrdERS3510GT_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809, 0, 3)
)
_S5ChasComBrdERS3510GT_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3510GT_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3510GT_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 809, 0, 4)
)
_S5ChasComBrdERS3524GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT = _S5ChasComBrdERS3524GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810)
)
_S5ChasComBrdERS3524GTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GTStore = _S5ChasComBrdERS3524GTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810, 0)
)
_S5ChasComBrdERS3524GTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GTStoreFlash = _S5ChasComBrdERS3524GTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810, 0, 1)
)
_S5ChasComBrdERS3524GTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GTStoreBootFW = _S5ChasComBrdERS3524GTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810, 0, 2)
)
_S5ChasComBrdERS3524GTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GTStoreDram = _S5ChasComBrdERS3524GTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810, 0, 3)
)
_S5ChasComBrdERS3524GTStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GTStorePoLFlash = _S5ChasComBrdERS3524GTStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 810, 0, 4)
)
_S5ChasComBrdERS3524GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUS = _S5ChasComBrdERS3524GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811)
)
_S5ChasComBrdERS3524GT_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUSStore = _S5ChasComBrdERS3524GT_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811, 0)
)
_S5ChasComBrdERS3524GT_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUSStoreFlash = _S5ChasComBrdERS3524GT_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811, 0, 1)
)
_S5ChasComBrdERS3524GT_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3524GT_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811, 0, 2)
)
_S5ChasComBrdERS3524GT_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUSStoreDram = _S5ChasComBrdERS3524GT_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811, 0, 3)
)
_S5ChasComBrdERS3524GT_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3524GT_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3524GT_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 811, 0, 4)
)
_S5ChasComBrdERS3526GT_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT = _S5ChasComBrdERS3526GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812)
)
_S5ChasComBrdERS3526GTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GTStore = _S5ChasComBrdERS3526GTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812, 0)
)
_S5ChasComBrdERS3526GTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GTStoreFlash = _S5ChasComBrdERS3526GTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812, 0, 1)
)
_S5ChasComBrdERS3526GTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GTStoreBootFW = _S5ChasComBrdERS3526GTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812, 0, 2)
)
_S5ChasComBrdERS3526GTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GTStoreDram = _S5ChasComBrdERS3526GTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812, 0, 3)
)
_S5ChasComBrdERS3526GTStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GTStorePoLFlash = _S5ChasComBrdERS3526GTStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 812, 0, 4)
)
_S5ChasComBrdERS3526GT_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUS = _S5ChasComBrdERS3526GT_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813)
)
_S5ChasComBrdERS3526GT_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUSStore = _S5ChasComBrdERS3526GT_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813, 0)
)
_S5ChasComBrdERS3526GT_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUSStoreFlash = _S5ChasComBrdERS3526GT_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813, 0, 1)
)
_S5ChasComBrdERS3526GT_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3526GT_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813, 0, 2)
)
_S5ChasComBrdERS3526GT_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUSStoreDram = _S5ChasComBrdERS3526GT_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813, 0, 3)
)
_S5ChasComBrdERS3526GT_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526GT_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3526GT_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 813, 0, 4)
)
_S5ChasComBrdERS3526T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T = _S5ChasComBrdERS3526T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814)
)
_S5ChasComBrdERS3526TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526TStore = _S5ChasComBrdERS3526TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814, 0)
)
_S5ChasComBrdERS3526TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526TStoreFlash = _S5ChasComBrdERS3526TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814, 0, 1)
)
_S5ChasComBrdERS3526TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526TStoreBootFW = _S5ChasComBrdERS3526TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814, 0, 2)
)
_S5ChasComBrdERS3526TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526TStoreDram = _S5ChasComBrdERS3526TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814, 0, 3)
)
_S5ChasComBrdERS3526TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526TStorePoLFlash = _S5ChasComBrdERS3526TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 814, 0, 4)
)
_S5ChasComBrdERS3526T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUS = _S5ChasComBrdERS3526T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815)
)
_S5ChasComBrdERS3526T_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUSStore = _S5ChasComBrdERS3526T_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815, 0)
)
_S5ChasComBrdERS3526T_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUSStoreFlash = _S5ChasComBrdERS3526T_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815, 0, 1)
)
_S5ChasComBrdERS3526T_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3526T_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815, 0, 2)
)
_S5ChasComBrdERS3526T_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUSStoreDram = _S5ChasComBrdERS3526T_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815, 0, 3)
)
_S5ChasComBrdERS3526T_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3526T_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3526T_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 815, 0, 4)
)
_S5ChasComBrdERS3549GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS = _S5ChasComBrdERS3549GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816)
)
_S5ChasComBrdERS3549GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTSStore = _S5ChasComBrdERS3549GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816, 0)
)
_S5ChasComBrdERS3549GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTSStoreFlash = _S5ChasComBrdERS3549GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816, 0, 1)
)
_S5ChasComBrdERS3549GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTSStoreBootFW = _S5ChasComBrdERS3549GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816, 0, 2)
)
_S5ChasComBrdERS3549GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTSStoreDram = _S5ChasComBrdERS3549GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816, 0, 3)
)
_S5ChasComBrdERS3549GTSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTSStorePoLFlash = _S5ChasComBrdERS3549GTSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 816, 0, 4)
)
_S5ChasComBrdERS3549GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUS = _S5ChasComBrdERS3549GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817)
)
_S5ChasComBrdERS3549GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUSStore = _S5ChasComBrdERS3549GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817, 0)
)
_S5ChasComBrdERS3549GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS3549GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817, 0, 1)
)
_S5ChasComBrdERS3549GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3549GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817, 0, 2)
)
_S5ChasComBrdERS3549GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS3549GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817, 0, 3)
)
_S5ChasComBrdERS3549GTS_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3549GTS_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3549GTS_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 817, 0, 4)
)
_S5ChasComBrdVSP7000MDA_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7000MDA = _S5ChasComBrdVSP7000MDA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 818)
)
_S5ChasComBrdVSP7000MDA_7008XLS_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7000MDA_7008XLS = _S5ChasComBrdVSP7000MDA_7008XLS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 818, 1)
)
_S5ChasComBrdVSP7000MDA_7008XT_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7000MDA_7008XT = _S5ChasComBrdVSP7000MDA_7008XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 818, 2)
)
_S5ChasComBrdVSP7000MDA_7002QQ_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7000MDA_7002QQ = _S5ChasComBrdVSP7000MDA_7002QQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 818, 3)
)
_S5ChasComBrdVSP7024XT_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XT = _S5ChasComBrdVSP7024XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819)
)
_S5ChasComBrdVSP7024XTStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStore = _S5ChasComBrdVSP7024XTStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0)
)
_S5ChasComBrdVSP7024XTStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreFlash = _S5ChasComBrdVSP7024XTStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 1)
)
_S5ChasComBrdVSP7024XTStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreBootFW = _S5ChasComBrdVSP7024XTStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 2)
)
_S5ChasComBrdVSP7024XTStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreDram = _S5ChasComBrdVSP7024XTStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 3)
)
_S5ChasComBrdVSP7024XTStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStorePoLFlash = _S5ChasComBrdVSP7024XTStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 4)
)
_S5ChasComBrdVSP7024XTStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreSecondaryFlash = _S5ChasComBrdVSP7024XTStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 5)
)
_S5ChasComBrdVSP7024XTStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreCPLD = _S5ChasComBrdVSP7024XTStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 6)
)
_S5ChasComBrdVSP7024XTStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreInstalledFW = _S5ChasComBrdVSP7024XTStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 7)
)
_S5ChasComBrdVSP7024XTStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreOperSW = _S5ChasComBrdVSP7024XTStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 8)
)
_S5ChasComBrdVSP7024XTStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreTotal = _S5ChasComBrdVSP7024XTStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 9)
)
_S5ChasComBrdVSP7024XTStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreBootLoader = _S5ChasComBrdVSP7024XTStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 10)
)
_S5ChasComBrdVSP7024XTStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreConfig = _S5ChasComBrdVSP7024XTStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 11)
)
_S5ChasComBrdVSP7024XTStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreSecondaryConfig = _S5ChasComBrdVSP7024XTStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 12)
)
_S5ChasComBrdVSP7024XTStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreAutoBakupConfig = _S5ChasComBrdVSP7024XTStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 13)
)
_S5ChasComBrdVSP7024XTStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdVSP7024XTStoreReserved = _S5ChasComBrdVSP7024XTStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 819, 0, 14)
)
_S5ChasComBrdERS5928GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS = _S5ChasComBrdERS5928GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820)
)
_S5ChasComBrdERS5928GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStore = _S5ChasComBrdERS5928GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0)
)
_S5ChasComBrdERS5928GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreFlash = _S5ChasComBrdERS5928GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 1)
)
_S5ChasComBrdERS5928GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreBootFW = _S5ChasComBrdERS5928GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 2)
)
_S5ChasComBrdERS5928GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreDram = _S5ChasComBrdERS5928GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 3)
)
_S5ChasComBrdERS5928GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreSecondaryFlash = _S5ChasComBrdERS5928GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 5)
)
_S5ChasComBrdERS5928GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreCPLD = _S5ChasComBrdERS5928GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 6)
)
_S5ChasComBrdERS5928GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreInstalledFW = _S5ChasComBrdERS5928GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 7)
)
_S5ChasComBrdERS5928GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreOperSW = _S5ChasComBrdERS5928GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 8)
)
_S5ChasComBrdERS5928GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreTotal = _S5ChasComBrdERS5928GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 9)
)
_S5ChasComBrdERS5928GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreBootLoader = _S5ChasComBrdERS5928GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 10)
)
_S5ChasComBrdERS5928GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreConfig = _S5ChasComBrdERS5928GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 11)
)
_S5ChasComBrdERS5928GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreSecondaryConfig = _S5ChasComBrdERS5928GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 12)
)
_S5ChasComBrdERS5928GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreAutoBakupConfig = _S5ChasComBrdERS5928GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 13)
)
_S5ChasComBrdERS5928GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTSStoreReserved = _S5ChasComBrdERS5928GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 820, 0, 14)
)
_S5ChasComBrdERS5928GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUS = _S5ChasComBrdERS5928GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStore = _S5ChasComBrdERS5928GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 1)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 2)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 3)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 5)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 6)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 7)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 8)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 9)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 10)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 11)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 12)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 13)
)
_S5ChasComBrdERS5928GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS5928GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 821, 0, 14)
)
_S5ChasComBrdERS5952GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS = _S5ChasComBrdERS5952GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822)
)
_S5ChasComBrdERS5952GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStore = _S5ChasComBrdERS5952GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0)
)
_S5ChasComBrdERS5952GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreFlash = _S5ChasComBrdERS5952GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 1)
)
_S5ChasComBrdERS5952GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreBootFW = _S5ChasComBrdERS5952GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 2)
)
_S5ChasComBrdERS5952GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreDram = _S5ChasComBrdERS5952GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 3)
)
_S5ChasComBrdERS5952GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreSecondaryFlash = _S5ChasComBrdERS5952GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 5)
)
_S5ChasComBrdERS5952GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreCPLD = _S5ChasComBrdERS5952GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 6)
)
_S5ChasComBrdERS5952GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreInstalledFW = _S5ChasComBrdERS5952GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 7)
)
_S5ChasComBrdERS5952GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreOperSW = _S5ChasComBrdERS5952GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 8)
)
_S5ChasComBrdERS5952GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreTotal = _S5ChasComBrdERS5952GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 9)
)
_S5ChasComBrdERS5952GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreBootLoader = _S5ChasComBrdERS5952GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 10)
)
_S5ChasComBrdERS5952GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreConfig = _S5ChasComBrdERS5952GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 11)
)
_S5ChasComBrdERS5952GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreSecondaryConfig = _S5ChasComBrdERS5952GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 12)
)
_S5ChasComBrdERS5952GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreAutoBakupConfig = _S5ChasComBrdERS5952GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 13)
)
_S5ChasComBrdERS5952GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTSStoreReserved = _S5ChasComBrdERS5952GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 822, 0, 14)
)
_S5ChasComBrdERS5952GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUS = _S5ChasComBrdERS5952GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStore = _S5ChasComBrdERS5952GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 1)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 2)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 3)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 5)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 6)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 7)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 8)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 9)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 10)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 11)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 12)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 13)
)
_S5ChasComBrdERS5952GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5952GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS5952GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 823, 0, 14)
)
_S5ChasComBrdERS5928GTS_UPWR_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWR = _S5ChasComBrdERS5928GTS_UPWR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824)
)
_S5ChasComBrdERS5928GTS_UPWRStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStore = _S5ChasComBrdERS5928GTS_UPWRStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0)
)
_S5ChasComBrdERS5928GTS_UPWRStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreFlash = _S5ChasComBrdERS5928GTS_UPWRStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 1)
)
_S5ChasComBrdERS5928GTS_UPWRStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreBootFW = _S5ChasComBrdERS5928GTS_UPWRStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 2)
)
_S5ChasComBrdERS5928GTS_UPWRStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreDram = _S5ChasComBrdERS5928GTS_UPWRStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 3)
)
_S5ChasComBrdERS5928GTS_UPWRStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreSecondaryFlash = _S5ChasComBrdERS5928GTS_UPWRStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 5)
)
_S5ChasComBrdERS5928GTS_UPWRStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreCPLD = _S5ChasComBrdERS5928GTS_UPWRStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 6)
)
_S5ChasComBrdERS5928GTS_UPWRStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreInstalledFW = _S5ChasComBrdERS5928GTS_UPWRStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 7)
)
_S5ChasComBrdERS5928GTS_UPWRStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreOperSW = _S5ChasComBrdERS5928GTS_UPWRStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 8)
)
_S5ChasComBrdERS5928GTS_UPWRStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreTotal = _S5ChasComBrdERS5928GTS_UPWRStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 9)
)
_S5ChasComBrdERS5928GTS_UPWRStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreBootLoader = _S5ChasComBrdERS5928GTS_UPWRStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 10)
)
_S5ChasComBrdERS5928GTS_UPWRStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreConfig = _S5ChasComBrdERS5928GTS_UPWRStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 11)
)
_S5ChasComBrdERS5928GTS_UPWRStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreSecondaryConfig = _S5ChasComBrdERS5928GTS_UPWRStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 12)
)
_S5ChasComBrdERS5928GTS_UPWRStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreAutoBakupConfig = _S5ChasComBrdERS5928GTS_UPWRStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 13)
)
_S5ChasComBrdERS5928GTS_UPWRStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS5928GTS_UPWRStoreReserved = _S5ChasComBrdERS5928GTS_UPWRStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 824, 0, 14)
)
_S5ChasComBrdERS59100GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS = _S5ChasComBrdERS59100GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825)
)
_S5ChasComBrdERS59100GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStore = _S5ChasComBrdERS59100GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0)
)
_S5ChasComBrdERS59100GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreFlash = _S5ChasComBrdERS59100GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 1)
)
_S5ChasComBrdERS59100GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreBootFW = _S5ChasComBrdERS59100GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 2)
)
_S5ChasComBrdERS59100GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreDram = _S5ChasComBrdERS59100GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 3)
)
_S5ChasComBrdERS59100GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreSecondaryFlash = _S5ChasComBrdERS59100GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 5)
)
_S5ChasComBrdERS59100GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreCPLD = _S5ChasComBrdERS59100GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 6)
)
_S5ChasComBrdERS59100GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreInstalledFW = _S5ChasComBrdERS59100GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 7)
)
_S5ChasComBrdERS59100GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreOperSW = _S5ChasComBrdERS59100GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 8)
)
_S5ChasComBrdERS59100GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreTotal = _S5ChasComBrdERS59100GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 9)
)
_S5ChasComBrdERS59100GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreBootLoader = _S5ChasComBrdERS59100GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 10)
)
_S5ChasComBrdERS59100GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreConfig = _S5ChasComBrdERS59100GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 11)
)
_S5ChasComBrdERS59100GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreSecondaryConfig = _S5ChasComBrdERS59100GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 12)
)
_S5ChasComBrdERS59100GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreAutoBakupConfig = _S5ChasComBrdERS59100GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 13)
)
_S5ChasComBrdERS59100GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTSStoreReserved = _S5ChasComBrdERS59100GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 825, 0, 14)
)
_S5ChasComBrdERS59100GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUS = _S5ChasComBrdERS59100GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStore = _S5ChasComBrdERS59100GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 1)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 2)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 3)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 5)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 6)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 7)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 8)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 9)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 10)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 11)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 12)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 13)
)
_S5ChasComBrdERS59100GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS59100GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS59100GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 826, 0, 14)
)
_S5ChasComBrdERS4926GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS = _S5ChasComBrdERS4926GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827)
)
_S5ChasComBrdERS4926GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStore = _S5ChasComBrdERS4926GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0)
)
_S5ChasComBrdERS4926GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreFlash = _S5ChasComBrdERS4926GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 1)
)
_S5ChasComBrdERS4926GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreBootFW = _S5ChasComBrdERS4926GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 2)
)
_S5ChasComBrdERS4926GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreDram = _S5ChasComBrdERS4926GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 3)
)
_S5ChasComBrdERS4926GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreSecondaryFlash = _S5ChasComBrdERS4926GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 5)
)
_S5ChasComBrdERS4926GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreCPLD = _S5ChasComBrdERS4926GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 6)
)
_S5ChasComBrdERS4926GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreInstalledFW = _S5ChasComBrdERS4926GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 7)
)
_S5ChasComBrdERS4926GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreOperSW = _S5ChasComBrdERS4926GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 8)
)
_S5ChasComBrdERS4926GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreTotal = _S5ChasComBrdERS4926GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 9)
)
_S5ChasComBrdERS4926GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreBootLoader = _S5ChasComBrdERS4926GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 10)
)
_S5ChasComBrdERS4926GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreConfig = _S5ChasComBrdERS4926GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 11)
)
_S5ChasComBrdERS4926GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreSecondaryConfig = _S5ChasComBrdERS4926GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 12)
)
_S5ChasComBrdERS4926GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreAutoBakupConfig = _S5ChasComBrdERS4926GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 13)
)
_S5ChasComBrdERS4926GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTSStoreReserved = _S5ChasComBrdERS4926GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 827, 0, 14)
)
_S5ChasComBrdERS4926GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUS = _S5ChasComBrdERS4926GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStore = _S5ChasComBrdERS4926GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 1)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 2)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 3)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 5)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 6)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 7)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 8)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 9)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 10)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 11)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 12)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 13)
)
_S5ChasComBrdERS4926GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4926GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS4926GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 828, 0, 14)
)
_S5ChasComBrdERS4950GTS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS = _S5ChasComBrdERS4950GTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829)
)
_S5ChasComBrdERS4950GTSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStore = _S5ChasComBrdERS4950GTSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0)
)
_S5ChasComBrdERS4950GTSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreFlash = _S5ChasComBrdERS4950GTSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 1)
)
_S5ChasComBrdERS4950GTSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreBootFW = _S5ChasComBrdERS4950GTSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 2)
)
_S5ChasComBrdERS4950GTSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreDram = _S5ChasComBrdERS4950GTSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 3)
)
_S5ChasComBrdERS4950GTSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStorePoLFlash = _S5ChasComBrdERS4950GTSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 4)
)
_S5ChasComBrdERS4950GTSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreSecondaryFlash = _S5ChasComBrdERS4950GTSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 5)
)
_S5ChasComBrdERS4950GTSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreCPLD = _S5ChasComBrdERS4950GTSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 6)
)
_S5ChasComBrdERS4950GTSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreInstalledFW = _S5ChasComBrdERS4950GTSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 7)
)
_S5ChasComBrdERS4950GTSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreOperSW = _S5ChasComBrdERS4950GTSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 8)
)
_S5ChasComBrdERS4950GTSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreTotal = _S5ChasComBrdERS4950GTSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 9)
)
_S5ChasComBrdERS4950GTSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreBootLoader = _S5ChasComBrdERS4950GTSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 10)
)
_S5ChasComBrdERS4950GTSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreConfig = _S5ChasComBrdERS4950GTSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 11)
)
_S5ChasComBrdERS4950GTSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreSecondaryConfig = _S5ChasComBrdERS4950GTSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 12)
)
_S5ChasComBrdERS4950GTSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreAutoBakupConfig = _S5ChasComBrdERS4950GTSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 13)
)
_S5ChasComBrdERS4950GTSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTSStoreReserved = _S5ChasComBrdERS4950GTSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 829, 0, 14)
)
_S5ChasComBrdERS4950GTS_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUS = _S5ChasComBrdERS4950GTS_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStore = _S5ChasComBrdERS4950GTS_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreFlash = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 1)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreBootFW = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 2)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreDram = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 3)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS4950GTS_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 4)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryFlash = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 5)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreCPLD_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreCPLD = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreCPLD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 6)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreInstalledFW = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreInstalledFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 7)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreOperSW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreOperSW = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreOperSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 8)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreTotal_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreTotal = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 9)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreBootLoader_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreBootLoader = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreBootLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 10)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreConfig = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 11)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryConfig = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 12)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreAutoBakupConfig = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreAutoBakupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 13)
)
_S5ChasComBrdERS4950GTS_PWR_PLUSStoreReserved_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS4950GTS_PWR_PLUSStoreReserved = _S5ChasComBrdERS4950GTS_PWR_PLUSStoreReserved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 830, 0, 14)
)
_S5ChasComBrdERS3550T_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T = _S5ChasComBrdERS3550T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831)
)
_S5ChasComBrdERS3550TStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550TStore = _S5ChasComBrdERS3550TStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831, 0)
)
_S5ChasComBrdERS3550TStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550TStoreFlash = _S5ChasComBrdERS3550TStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831, 0, 1)
)
_S5ChasComBrdERS3550TStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550TStoreBootFW = _S5ChasComBrdERS3550TStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831, 0, 2)
)
_S5ChasComBrdERS3550TStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550TStoreDram = _S5ChasComBrdERS3550TStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831, 0, 3)
)
_S5ChasComBrdERS3550TStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550TStorePoLFlash = _S5ChasComBrdERS3550TStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 831, 0, 4)
)
_S5ChasComBrdERS3550T_PWR_PLUS_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUS = _S5ChasComBrdERS3550T_PWR_PLUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832)
)
_S5ChasComBrdERS3550T_PWR_PLUSStore_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUSStore = _S5ChasComBrdERS3550T_PWR_PLUSStore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832, 0)
)
_S5ChasComBrdERS3550T_PWR_PLUSStoreFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUSStoreFlash = _S5ChasComBrdERS3550T_PWR_PLUSStoreFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832, 0, 1)
)
_S5ChasComBrdERS3550T_PWR_PLUSStoreBootFW_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUSStoreBootFW = _S5ChasComBrdERS3550T_PWR_PLUSStoreBootFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832, 0, 2)
)
_S5ChasComBrdERS3550T_PWR_PLUSStoreDram_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUSStoreDram = _S5ChasComBrdERS3550T_PWR_PLUSStoreDram_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832, 0, 3)
)
_S5ChasComBrdERS3550T_PWR_PLUSStorePoLFlash_ObjectIdentity = ObjectIdentity
s5ChasComBrdERS3550T_PWR_PLUSStorePoLFlash = _S5ChasComBrdERS3550T_PWR_PLUSStorePoLFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 6, 832, 0, 4)
)
_S5ChasComMBkpl_ObjectIdentity = ObjectIdentity
s5ChasComMBkpl = _S5ChasComMBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7)
)
_S5ChasComM5000Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM5000Bkpl = _S5ChasComM5000Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12)
)
_S5ChasComM5000BkplLow_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplLow = _S5ChasComM5000BkplLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 1)
)
_S5ChasComM5000BkplLowCmbEthTok_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplLowCmbEthTok = _S5ChasComM5000BkplLowCmbEthTok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 1, 4)
)
_S5ChasComM5000BkplLowCmbEth_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplLowCmbEth = _S5ChasComM5000BkplLowCmbEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 1, 5)
)
_S5ChasComM5000BkplMidLeft_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplMidLeft = _S5ChasComM5000BkplMidLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 2)
)
_S5ChasComM5000BkplMidLeftFddiFull_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplMidLeftFddiFull = _S5ChasComM5000BkplMidLeftFddiFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 2, 0)
)
_S5ChasComM5000BkplMidLeftEth100MbsFull_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplMidLeftEth100MbsFull = _S5ChasComM5000BkplMidLeftEth100MbsFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 2, 4)
)
_S5ChasComM5000BkplMidLeftEth100Mbs_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplMidLeftEth100Mbs = _S5ChasComM5000BkplMidLeftEth100Mbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 2, 7)
)
_S5ChasComM5000BkplMidRight_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplMidRight = _S5ChasComM5000BkplMidRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 3)
)
_S5ChasComM5000BkplHighLeft_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighLeft = _S5ChasComM5000BkplHighLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 4)
)
_S5ChasComM5000BkplHighLeftEth100Mbs_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighLeftEth100Mbs = _S5ChasComM5000BkplHighLeftEth100Mbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 4, 4)
)
_S5ChasComM5000BkplHighLeftSwitchedPktBusFull_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighLeftSwitchedPktBusFull = _S5ChasComM5000BkplHighLeftSwitchedPktBusFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 4, 5)
)
_S5ChasComM5000BkplHighLeftAtm16_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighLeftAtm16 = _S5ChasComM5000BkplHighLeftAtm16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 4, 8)
)
_S5ChasComM5000BkplHighLeftAtm64_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighLeftAtm64 = _S5ChasComM5000BkplHighLeftAtm64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 4, 9)
)
_S5ChasComM5000BkplHighRight_ObjectIdentity = ObjectIdentity
s5ChasComM5000BkplHighRight = _S5ChasComM5000BkplHighRight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 12, 5)
)
_S5ChasComM5005Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM5005Bkpl = _S5ChasComM5005Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17)
)
_S5ChasComM5005BkplLow_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplLow = _S5ChasComM5005BkplLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 1)
)
_S5ChasComM5005BkplLowCmbEthTok_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplLowCmbEthTok = _S5ChasComM5005BkplLowCmbEthTok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 1, 4)
)
_S5ChasComM5005BkplLowCmbEth_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplLowCmbEth = _S5ChasComM5005BkplLowCmbEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 1, 5)
)
_S5ChasComM5005BkplMidLeft_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplMidLeft = _S5ChasComM5005BkplMidLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 2)
)
_S5ChasComM5005BkplMidLeftFddi_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplMidLeftFddi = _S5ChasComM5005BkplMidLeftFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 2, 1)
)
_S5ChasComM5005BkplMidLeftEth100Mbs_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplMidLeftEth100Mbs = _S5ChasComM5005BkplMidLeftEth100Mbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 2, 5)
)
_S5ChasComM5005BkplHighLeft_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplHighLeft = _S5ChasComM5005BkplHighLeft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 4)
)
_S5ChasComM5005BkplHighLeftSwitchedPktBus_ObjectIdentity = ObjectIdentity
s5ChasComM5005BkplHighLeftSwitchedPktBus = _S5ChasComM5005BkplHighLeftSwitchedPktBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 17, 4, 6)
)
_S5ChasComM5Dx000Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM5Dx000Bkpl = _S5ChasComM5Dx000Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 24)
)
_S5ChasComM5DN000BkplEth3_ObjectIdentity = ObjectIdentity
s5ChasComM5DN000BkplEth3 = _S5ChasComM5DN000BkplEth3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 24, 1)
)
_S5ChasComMNBayStackBkpl_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackBkpl = _S5ChasComMNBayStackBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 25)
)
_S5ChasComMNBayStackBkplEth3_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackBkplEth3 = _S5ChasComMNBayStackBkplEth3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 25, 1)
)
_S5ChasComBayStack100Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComBayStack100Bkpl = _S5ChasComBayStack100Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 27)
)
_S5ChasComM3000Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000Bkpl = _S5ChasComM3000Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28)
)
_S5ChasComM3000EthBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthBkpl = _S5ChasComM3000EthBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 2)
)
_S5ChasComM3000_1Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000_1Bkpl = _S5ChasComM3000_1Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 2, 0)
)
_S5ChasComM3000NBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000NBkpl = _S5ChasComM3000NBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 2, 7)
)
_S5ChasComM3000EthTokBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthTokBkpl = _S5ChasComM3000EthTokBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 3)
)
_S5ChasComM3000_4Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000_4Bkpl = _S5ChasComM3000_4Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 3, 4)
)
_S5ChasComM3000NTBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000NTBkpl = _S5ChasComM3000NTBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 3, 5)
)
_S5ChasComM3000EthFddiBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthFddiBkpl = _S5ChasComM3000EthFddiBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 4)
)
_S5ChasComM3000EthTokFddiBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthTokFddiBkpl = _S5ChasComM3000EthTokFddiBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 5)
)
_S5ChasComM3000_5Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000_5Bkpl = _S5ChasComM3000_5Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 5, 2)
)
_S5ChasComM3000SBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000SBkpl = _S5ChasComM3000SBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 5, 6)
)
_S5ChasComM3000EthTokRedBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthTokRedBkpl = _S5ChasComM3000EthTokRedBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 6)
)
_S5ChasComM3000_4RBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000_4RBkpl = _S5ChasComM3000_4RBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 6, 1)
)
_S5ChasComM3000NTRBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000NTRBkpl = _S5ChasComM3000NTRBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 6, 9)
)
_S5ChasComM3000EthTokFddiRedBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000EthTokFddiRedBkpl = _S5ChasComM3000EthTokFddiRedBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 7)
)
_S5ChasComM3000_5RBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000_5RBkpl = _S5ChasComM3000_5RBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 7, 3)
)
_S5ChasComM3000SRBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000SRBkpl = _S5ChasComM3000SRBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 7, 8)
)
_S5ChasComM3000TokBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000TokBkpl = _S5ChasComM3000TokBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 8)
)
_S5ChasComM3000CTBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000CTBkpl = _S5ChasComM3000CTBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 9)
)
_S5ChasComM3000CBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000CBkpl = _S5ChasComM3000CBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 10)
)
_S5ChasComM3000CTRBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3000CTRBkpl = _S5ChasComM3000CTRBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 28, 11)
)
_S5ChasCom28200Bkpl_ObjectIdentity = ObjectIdentity
s5ChasCom28200Bkpl = _S5ChasCom28200Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 30)
)
_S5ChasComMBayStackTrBkpl_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrBkpl = _S5ChasComMBayStackTrBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 36)
)
_S5ChasComMBayStackTrBkplTr1_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrBkplTr1 = _S5ChasComMBayStackTrBkplTr1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 36, 1)
)
_S5ChasComM3030Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3030Bkpl = _S5ChasComM3030Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 39)
)
_S5ChasComM3030EthBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3030EthBkpl = _S5ChasComM3030EthBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 39, 1)
)
_S5ChasComM3030EthTrBkpl_ObjectIdentity = ObjectIdentity
s5ChasComM3030EthTrBkpl = _S5ChasComM3030EthTrBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 39, 5)
)
_S5ChasComSwitchNodeBkpl_ObjectIdentity = ObjectIdentity
s5ChasComSwitchNodeBkpl = _S5ChasComSwitchNodeBkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 40)
)
_S5ChasComBayStack150Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150Bkpl = _S5ChasComBayStack150Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 41)
)
_S5ChasComBayStack150BkplEth_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150BkplEth = _S5ChasComBayStack150BkplEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 41, 1)
)
_S5ChasComMBayStack303_304Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_304Bkpl = _S5ChasComMBayStack303_304Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 42)
)
_S5ChasComBayStack200Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200Bkpl = _S5ChasComBayStack200Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 43)
)
_S5ChasComBayStack200BkplEth_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200BkplEth = _S5ChasComBayStack200BkplEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 43, 1)
)
_S5ChasComBayStack250Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250Bkpl = _S5ChasComBayStack250Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 44)
)
_S5ChasComBayStack250BkplEth10_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250BkplEth10 = _S5ChasComBayStack250BkplEth10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 44, 1)
)
_S5ChasComBayStack250BkplEth100_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250BkplEth100 = _S5ChasComBayStack250BkplEth100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 44, 2)
)
_S5ChasComMAccelar8010Bkpl_ObjectIdentity = ObjectIdentity
s5ChasComMAccelar8010Bkpl = _S5ChasComMAccelar8010Bkpl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 7, 45)
)
_S5ChasComMPwr_ObjectIdentity = ObjectIdentity
s5ChasComMPwr = _S5ChasComMPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8)
)
_S5ChasComM5000Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM5000Pwr = _S5ChasComM5000Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 12)
)
_S5ChasComM5000Pwr_950A_ObjectIdentity = ObjectIdentity
s5ChasComM5000Pwr_950A = _S5ChasComM5000Pwr_950A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 12, 0)
)
_S5ChasComM5000Pwr_950_ObjectIdentity = ObjectIdentity
s5ChasComM5000Pwr_950 = _S5ChasComM5000Pwr_950_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 12, 1)
)
_S5ChasComM5000Pwr_1400WDC_ObjectIdentity = ObjectIdentity
s5ChasComM5000Pwr_1400WDC = _S5ChasComM5000Pwr_1400WDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 12, 3)
)
_S5ChasComM1032xPwr_ObjectIdentity = ObjectIdentity
s5ChasComM1032xPwr = _S5ChasComM1032xPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 16)
)
_S5ChasComM1032xPwr_A_ObjectIdentity = ObjectIdentity
s5ChasComM1032xPwr_A = _S5ChasComM1032xPwr_A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 16, 1)
)
_S5ChasComM5005Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM5005Pwr = _S5ChasComM5005Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 17)
)
_S5ChasComM5005Pwr_600_ObjectIdentity = ObjectIdentity
s5ChasComM5005Pwr_600 = _S5ChasComM5005Pwr_600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 17, 1)
)
_S5ChasComM5005Pwr_900WAC_ObjectIdentity = ObjectIdentity
s5ChasComM5005Pwr_900WAC = _S5ChasComM5005Pwr_900WAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 17, 2)
)
_S5ChasComM5005Pwr_900WDC_ObjectIdentity = ObjectIdentity
s5ChasComM5005Pwr_900WDC = _S5ChasComM5005Pwr_900WDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 17, 3)
)
_S5ChasComM5DN000Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM5DN000Pwr = _S5ChasComM5DN000Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 24)
)
_S5ChasCom5DN000Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasCom5DN000Pwr_RedundFeed = _S5ChasCom5DN000Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 24, 1)
)
_S5ChasComM5DN002Pwr_50W_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002Pwr_50W = _S5ChasComM5DN002Pwr_50W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 24, 2)
)
_S5ChasComM5DN003Pwr_110W_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003Pwr_110W = _S5ChasComM5DN003Pwr_110W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 24, 3)
)
_S5ChasComMNBayStackPwr_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackPwr = _S5ChasComMNBayStackPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 25)
)
_S5ChasComMNBayStackPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackPwr_RedundFeed = _S5ChasComMNBayStackPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 25, 1)
)
_S5ChasComMNBayStackPwr_50W_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackPwr_50W = _S5ChasComMNBayStackPwr_50W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 25, 2)
)
_S5ChasComMBayStack100Pwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100Pwr = _S5ChasComMBayStack100Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 27)
)
_S5ChasComMBayStack100Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100Pwr_RedundFeed = _S5ChasComMBayStack100Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 27, 1)
)
_S5ChasComMBayStack100Pwr_110W_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100Pwr_110W = _S5ChasComMBayStack100Pwr_110W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 27, 2)
)
_S5ChasComM3000Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM3000Pwr = _S5ChasComM3000Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 28)
)
_S5ChasComM3000360Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM3000360Pwr = _S5ChasComM3000360Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 28, 1)
)
_S5ChasComM3000460Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM3000460Pwr = _S5ChasComM3000460Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 28, 2)
)
_S5ChasComM3003_460Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM3003_460Pwr = _S5ChasComM3003_460Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 28, 3)
)
_S5ChasComM28200Pwr_ObjectIdentity = ObjectIdentity
s5ChasComM28200Pwr = _S5ChasComM28200Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 30)
)
_S5ChasComM28200Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComM28200Pwr_RedundFeed = _S5ChasComM28200Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 30, 1)
)
_S5ChasComM28200Pwr_182W_ObjectIdentity = ObjectIdentity
s5ChasComM28200Pwr_182W = _S5ChasComM28200Pwr_182W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 30, 2)
)
_S5ChasComMBayStack301Pwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301Pwr = _S5ChasComMBayStack301Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 31)
)
_S5ChasComMBayStack301IntPwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301IntPwr = _S5ChasComMBayStack301IntPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 31, 1)
)
_S5ChasComMBayStack301ExtPwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301ExtPwr = _S5ChasComMBayStack301ExtPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 31, 2)
)
_S5ChasComSwitchNodePwr_ObjectIdentity = ObjectIdentity
s5ChasComSwitchNodePwr = _S5ChasComSwitchNodePwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 32)
)
_S5ChasComMBayStackTrPwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrPwr = _S5ChasComMBayStackTrPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 36)
)
_S5ChasComMBayStackTrPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrPwr_RedundFeed = _S5ChasComMBayStackTrPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 36, 1)
)
_S5ChasComMBayStackTrPwr_150W_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrPwr_150W = _S5ChasComMBayStackTrPwr_150W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 36, 2)
)
_S5ChasComBayStack150Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150Pwr = _S5ChasComBayStack150Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 41)
)
_S5ChasComBayStack150MasterPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150MasterPwr = _S5ChasComBayStack150MasterPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 41, 1)
)
_S5ChasComBayStack150SlavePwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150SlavePwr = _S5ChasComBayStack150SlavePwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 41, 2)
)
_S5ChasComMBayStack303_304Pwr_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_304Pwr = _S5ChasComMBayStack303_304Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 42)
)
_S5ChasComBayStack200Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200Pwr = _S5ChasComBayStack200Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 43)
)
_S5ChasComBayStack200MasterPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200MasterPwr = _S5ChasComBayStack200MasterPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 43, 1)
)
_S5ChasComBayStack250Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250Pwr = _S5ChasComBayStack250Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 44)
)
_S5ChasComBayStack250MasterPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250MasterPwr = _S5ChasComBayStack250MasterPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 44, 1)
)
_S5ChasComBayStack250SlavePwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250SlavePwr = _S5ChasComBayStack250SlavePwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 44, 2)
)
_S5ChasComMAccelar8001Pwr_ObjectIdentity = ObjectIdentity
s5ChasComMAccelar8001Pwr = _S5ChasComMAccelar8001Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 45)
)
_S5ChasComMAccelar8002Pwr_ObjectIdentity = ObjectIdentity
s5ChasComMAccelar8002Pwr = _S5ChasComMAccelar8002Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 46)
)
_S5ChasComBPS2000Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBPS2000Pwr = _S5ChasComBPS2000Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 47)
)
_S5ChasComBPS2000Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBPS2000Pwr_Main = _S5ChasComBPS2000Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 47, 1)
)
_S5ChasComBPS2000Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBPS2000Pwr_RedundFeed = _S5ChasComBPS2000Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 47, 2)
)
_S5ChasComBayStack450Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450Pwr = _S5ChasComBayStack450Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 48)
)
_S5ChasComBayStack450Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450Pwr_Main = _S5ChasComBayStack450Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 48, 1)
)
_S5ChasComBayStack450Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450Pwr_RedundFeed = _S5ChasComBayStack450Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 48, 2)
)
_S5ChasComBayStack3580Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack3580Pwr = _S5ChasComBayStack3580Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 49)
)
_S5ChasComBayStack3580Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack3580Pwr_Main = _S5ChasComBayStack3580Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 49, 1)
)
_S5ChasComBayStack3580Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack3580Pwr_RedundFeed = _S5ChasComBayStack3580Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 49, 2)
)
_S5ChasComBayStack420Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack420Pwr = _S5ChasComBayStack420Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 50)
)
_S5ChasComMetro1200ESMPwr_ObjectIdentity = ObjectIdentity
s5ChasComMetro1200ESMPwr = _S5ChasComMetro1200ESMPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 51)
)
_S5ChasComMetro1200ESMPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComMetro1200ESMPwr_Main = _S5ChasComMetro1200ESMPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 51, 1)
)
_S5ChasComMetro1200ESMPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMetro1200ESMPwr_RedundFeed = _S5ChasComMetro1200ESMPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 51, 2)
)
_S5ChasComBayStack380Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380Pwr = _S5ChasComBayStack380Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 52)
)
_S5ChasComBayStack380Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380Pwr_Main = _S5ChasComBayStack380Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 52, 1)
)
_S5ChasComBayStack380Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380Pwr_RedundFeed = _S5ChasComBayStack380Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 52, 2)
)
_S5ChasComBayStack470Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470Pwr = _S5ChasComBayStack470Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 53)
)
_S5ChasComBayStack470Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470Pwr_Main = _S5ChasComBayStack470Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 53, 1)
)
_S5ChasComBayStack470Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470Pwr_RedundFeed = _S5ChasComBayStack470Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 53, 2)
)
_S5ChasComMetro1450ESMPwr_ObjectIdentity = ObjectIdentity
s5ChasComMetro1450ESMPwr = _S5ChasComMetro1450ESMPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 54)
)
_S5ChasComMetro1450ESMPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComMetro1450ESMPwr_Main = _S5ChasComMetro1450ESMPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 54, 1)
)
_S5ChasComMetro1450ESMPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMetro1450ESMPwr_RedundFeed = _S5ChasComMetro1450ESMPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 54, 2)
)
_S5ChasComMetro1400ESMPwr_ObjectIdentity = ObjectIdentity
s5ChasComMetro1400ESMPwr = _S5ChasComMetro1400ESMPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 55)
)
_S5ChasComMetro1400ESMPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComMetro1400ESMPwr_Main = _S5ChasComMetro1400ESMPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 55, 1)
)
_S5ChasComMetro1400ESMPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComMetro1400ESMPwr_RedundFeed = _S5ChasComMetro1400ESMPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 55, 2)
)
_S5ChasComBayStack460_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack460_24T_PWRPwr = _S5ChasComBayStack460_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 56)
)
_S5ChasComBayStack460_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack460_24T_PWRPwr_Main = _S5ChasComBayStack460_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 56, 1)
)
_S5ChasComBayStack460_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack460_24T_PWRPwr_RedundFeed = _S5ChasComBayStack460_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 56, 2)
)
_S5ChasComBayStack380_24FPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380_24FPwr = _S5ChasComBayStack380_24FPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 57)
)
_S5ChasComBayStack380_24FPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380_24FPwr_Main = _S5ChasComBayStack380_24FPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 57, 1)
)
_S5ChasComBayStack380_24FPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380_24FPwr_RedundFeed = _S5ChasComBayStack380_24FPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 57, 2)
)
_S5ChasComBayStack5510_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_24TPwr = _S5ChasComBayStack5510_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 58)
)
_S5ChasComBayStack5510_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_24TPwr_Main = _S5ChasComBayStack5510_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 58, 1)
)
_S5ChasComBayStack5510_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_24TPwr_RedundFeed = _S5ChasComBayStack5510_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 58, 2)
)
_S5ChasComBayStack5510_48TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_48TPwr = _S5ChasComBayStack5510_48TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 59)
)
_S5ChasComBayStack5510_48TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_48TPwr_Main = _S5ChasComBayStack5510_48TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 59, 1)
)
_S5ChasComBayStack5510_48TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_48TPwr_RedundFeed = _S5ChasComBayStack5510_48TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 59, 2)
)
_S5ChasComBayStack470_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24TPwr = _S5ChasComBayStack470_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 60)
)
_S5ChasComBayStack470_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24TPwr_Main = _S5ChasComBayStack470_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 60, 1)
)
_S5ChasComBayStack470_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24TPwr_RedundFeed = _S5ChasComBayStack470_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 60, 2)
)
_S5ChasComWLANAccessPoint2220Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2220Pwr = _S5ChasComWLANAccessPoint2220Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 61)
)
_S5ChasComWLANAccessPoint2220Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2220Pwr_Main = _S5ChasComWLANAccessPoint2220Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 61, 1)
)
_S5ChasComWLANSecuritySwitch2250Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2250Pwr = _S5ChasComWLANSecuritySwitch2250Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 62)
)
_S5ChasComWLANSecuritySwitch2250Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2250Pwr_Main = _S5ChasComWLANSecuritySwitch2250Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 62, 1)
)
_S5ChasComBayStack425Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack425Pwr = _S5ChasComBayStack425Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 63)
)
_S5ChasComBayStack425PwrMain_ObjectIdentity = ObjectIdentity
s5ChasComBayStack425PwrMain = _S5ChasComBayStack425PwrMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 63, 1)
)
_S5ChasComBayStack425PwrRedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack425PwrRedundFeed = _S5ChasComBayStack425PwrRedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 63, 2)
)
_S5ChasComWLANAccessPoint2221Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2221Pwr = _S5ChasComWLANAccessPoint2221Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 64)
)
_S5ChasComWLANAccessPoint2221Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2221Pwr_Main = _S5ChasComWLANAccessPoint2221Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 64, 1)
)
_S5ChasComBayStack5520_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_24T_PWRPwr = _S5ChasComBayStack5520_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 65)
)
_S5ChasComBayStack5520_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_24T_PWRPwr_Main = _S5ChasComBayStack5520_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 65, 1)
)
_S5ChasComBayStack5520_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_24T_PWRPwr_RedundFeed = _S5ChasComBayStack5520_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 65, 2)
)
_S5ChasComBayStack5520_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_48T_PWRPwr = _S5ChasComBayStack5520_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 66)
)
_S5ChasComBayStack5520_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_48T_PWRPwr_Main = _S5ChasComBayStack5520_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 66, 1)
)
_S5ChasComBayStack5520_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_48T_PWRPwr_RedundFeed = _S5ChasComBayStack5520_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 66, 2)
)
_S5ChasComBayStack325Pwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack325Pwr = _S5ChasComBayStack325Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 67)
)
_S5ChasComBayStack325PwrMain_ObjectIdentity = ObjectIdentity
s5ChasComBayStack325PwrMain = _S5ChasComBayStack325PwrMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 67, 1)
)
_S5ChasComBayStack325PwrRedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack325PwrRedundFeed = _S5ChasComBayStack325PwrRedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 67, 2)
)
_S5ChasComWLANAccessPoint2225Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2225Pwr = _S5ChasComWLANAccessPoint2225Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 68)
)
_S5ChasComWLANAccessPoint2225Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2225Pwr_Main = _S5ChasComWLANAccessPoint2225Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 68, 1)
)
_S5ChasComBayStack470_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24T_PWRPwr = _S5ChasComBayStack470_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 69)
)
_S5ChasComBayStack470_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24T_PWRPwr_Main = _S5ChasComBayStack470_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 69, 1)
)
_S5ChasComBayStack470_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24T_PWRPwr_RedundFeed = _S5ChasComBayStack470_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 69, 2)
)
_S5ChasComBayStack470_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_48T_PWRPwr = _S5ChasComBayStack470_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 70)
)
_S5ChasComBayStack470_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_48T_PWRPwr_Main = _S5ChasComBayStack470_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 70, 1)
)
_S5ChasComBayStack470_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_48T_PWRPwr_RedundFeed = _S5ChasComBayStack470_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 70, 2)
)
_S5ChasComWLANSecuritySwitch2270Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2270Pwr = _S5ChasComWLANSecuritySwitch2270Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 71)
)
_S5ChasComWLANSecuritySwitch2270Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2270Pwr_Main = _S5ChasComWLANSecuritySwitch2270Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 71, 1)
)
_S5ChasComEthernetRoutingSwitch5530_24TFDPwr_ObjectIdentity = ObjectIdentity
s5ChasComEthernetRoutingSwitch5530_24TFDPwr = _S5ChasComEthernetRoutingSwitch5530_24TFDPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 72)
)
_S5ChasComEthernetRoutingSwitch5530_24TFDPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComEthernetRoutingSwitch5530_24TFDPwr_Main = _S5ChasComEthernetRoutingSwitch5530_24TFDPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 72, 1)
)
_S5ChasComEthernetRoutingSwitch5530_24TFDPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComEthernetRoutingSwitch5530_24TFDPwr_RedundFeed = _S5ChasComEthernetRoutingSwitch5530_24TFDPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 72, 2)
)
_S5ChasComEthernetSwitch3510_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComEthernetSwitch3510_24TPwr = _S5ChasComEthernetSwitch3510_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 73)
)
_S5ChasComEthernetSwitch3510_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComEthernetSwitch3510_24TPwr_Main = _S5ChasComEthernetSwitch3510_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 73, 1)
)
_S5ChasComEthernetSwitch3510_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComEthernetSwitch3510_24TPwr_RedundFeed = _S5ChasComEthernetSwitch3510_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 73, 2)
)
_S5ChasComBES1010_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_24TPwr = _S5ChasComBES1010_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 74)
)
_S5ChasComBES1010_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_24TPwr_Main = _S5ChasComBES1010_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 74, 1)
)
_S5ChasComBES1010_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_24TPwr_RedundFeed = _S5ChasComBES1010_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 74, 2)
)
_S5ChasComBES1010_48TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_48TPwr = _S5ChasComBES1010_48TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 75)
)
_S5ChasComBES1010_48TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_48TPwr_Main = _S5ChasComBES1010_48TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 75, 1)
)
_S5ChasComBES1010_48TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_48TPwr_RedundFeed = _S5ChasComBES1010_48TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 75, 2)
)
_S5ChasComBES1020_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_24T_PWRPwr = _S5ChasComBES1020_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 76)
)
_S5ChasComBES1020_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_24T_PWRPwr_Main = _S5ChasComBES1020_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 76, 1)
)
_S5ChasComBES1020_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_24T_PWRPwr_RedundFeed = _S5ChasComBES1020_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 76, 2)
)
_S5ChasComBES1020_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_48T_PWRPwr = _S5ChasComBES1020_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 77)
)
_S5ChasComBES1020_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_48T_PWRPwr_Main = _S5ChasComBES1020_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 77, 1)
)
_S5ChasComBES1020_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_48T_PWRPwr_RedundFeed = _S5ChasComBES1020_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 77, 2)
)
_S5ChasComBES2010_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_24TPwr = _S5ChasComBES2010_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 78)
)
_S5ChasComBES2010_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_24TPwr_Main = _S5ChasComBES2010_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 78, 1)
)
_S5ChasComBES2010_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_24TPwr_RedundFeed = _S5ChasComBES2010_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 78, 2)
)
_S5ChasComBES2010_48TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_48TPwr = _S5ChasComBES2010_48TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 79)
)
_S5ChasComBES2010_48TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_48TPwr_Main = _S5ChasComBES2010_48TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 79, 1)
)
_S5ChasComBES2010_48TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_48TPwr_RedundFeed = _S5ChasComBES2010_48TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 79, 2)
)
_S5ChasComBES2020_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_24T_PWRPwr = _S5ChasComBES2020_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 80)
)
_S5ChasComBES2020_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_24T_PWRPwr_Main = _S5ChasComBES2020_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 80, 1)
)
_S5ChasComBES2020_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_24T_PWRPwr_RedundFeed = _S5ChasComBES2020_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 80, 2)
)
_S5ChasComBES2020_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_48T_PWRPwr = _S5ChasComBES2020_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 81)
)
_S5ChasComBES2020_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_48T_PWRPwr_Main = _S5ChasComBES2020_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 81, 1)
)
_S5ChasComBES2020_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_48T_PWRPwr_RedundFeed = _S5ChasComBES2020_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 81, 2)
)
_S5ChasComBES110_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES110_24TPwr = _S5ChasComBES110_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 82)
)
_S5ChasComBES110_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES110_24TPwr_Main = _S5ChasComBES110_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 82, 1)
)
_S5ChasComBES110_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES110_24TPwr_RedundFeed = _S5ChasComBES110_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 82, 2)
)
_S5ChasComBES110_48TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES110_48TPwr = _S5ChasComBES110_48TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 83)
)
_S5ChasComBES110_48TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES110_48TPwr_Main = _S5ChasComBES110_48TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 83, 1)
)
_S5ChasComBES110_48TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES110_48TPwr_RedundFeed = _S5ChasComBES110_48TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 83, 2)
)
_S5ChasComBES120_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES120_24T_PWRPwr = _S5ChasComBES120_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 84)
)
_S5ChasComBES120_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES120_24T_PWRPwr_Main = _S5ChasComBES120_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 84, 1)
)
_S5ChasComBES120_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES120_24T_PWRPwr_RedundFeed = _S5ChasComBES120_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 84, 2)
)
_S5ChasComBES120_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES120_48T_PWRPwr = _S5ChasComBES120_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 85)
)
_S5ChasComBES120_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES120_48T_PWRPwr_Main = _S5ChasComBES120_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 85, 1)
)
_S5ChasComBES120_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES120_48T_PWRPwr_RedundFeed = _S5ChasComBES120_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 85, 2)
)
_S5ChasComBES210_24TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES210_24TPwr = _S5ChasComBES210_24TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 86)
)
_S5ChasComBES210_24TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES210_24TPwr_Main = _S5ChasComBES210_24TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 86, 1)
)
_S5ChasComBES210_24TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES210_24TPwr_RedundFeed = _S5ChasComBES210_24TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 86, 2)
)
_S5ChasComBES210_48TPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES210_48TPwr = _S5ChasComBES210_48TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 87)
)
_S5ChasComBES210_48TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES210_48TPwr_Main = _S5ChasComBES210_48TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 87, 1)
)
_S5ChasComBES210_48TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES210_48TPwr_RedundFeed = _S5ChasComBES210_48TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 87, 2)
)
_S5ChasComBES220_24T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES220_24T_PWRPwr = _S5ChasComBES220_24T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 88)
)
_S5ChasComBES220_24T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES220_24T_PWRPwr_Main = _S5ChasComBES220_24T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 88, 1)
)
_S5ChasComBES220_24T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES220_24T_PWRPwr_RedundFeed = _S5ChasComBES220_24T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 88, 2)
)
_S5ChasComBES220_48T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComBES220_48T_PWRPwr = _S5ChasComBES220_48T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 89)
)
_S5ChasComBES220_48T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComBES220_48T_PWRPwr_Main = _S5ChasComBES220_48T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 89, 1)
)
_S5ChasComBES220_48T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComBES220_48T_PWRPwr_RedundFeed = _S5ChasComBES220_48T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 89, 2)
)
_S5ChasComERS4548GTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GTPwr = _S5ChasComERS4548GTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 90)
)
_S5ChasComERS4548GTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GTPwr_Main = _S5ChasComERS4548GTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 90, 1)
)
_S5ChasComERS4548GTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GTPwr_RedundFeed = _S5ChasComERS4548GTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 90, 2)
)
_S5ChasComERS4548GT_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GT_PWRPwr = _S5ChasComERS4548GT_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 91)
)
_S5ChasComERS4548GT_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GT_PWRPwr_Main = _S5ChasComERS4548GT_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 91, 1)
)
_S5ChasComERS4548GT_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GT_PWRPwr_RedundFeed = _S5ChasComERS4548GT_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 91, 2)
)
_S5ChasComERS4550TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4550TPwr = _S5ChasComERS4550TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 92)
)
_S5ChasComERS4550TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4550TPwr_Main = _S5ChasComERS4550TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 92, 1)
)
_S5ChasComERS4550TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4550TPwr_RedundFeed = _S5ChasComERS4550TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 92, 2)
)
_S5ChasComERS4550T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWRPwr = _S5ChasComERS4550T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 93)
)
_S5ChasComERS4550T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWRPwr_Main = _S5ChasComERS4550T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 93, 1)
)
_S5ChasComERS4550T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWRPwr_RedundFeed = _S5ChasComERS4550T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 93, 2)
)
_S5ChasComERS4526FXPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526FXPwr = _S5ChasComERS4526FXPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 94)
)
_S5ChasComERS4526FXPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526FXPwr_Main = _S5ChasComERS4526FXPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 94, 1)
)
_S5ChasComERS4526FXPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526FXPwr_RedundFeed = _S5ChasComERS4526FXPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 94, 2)
)
_S5ChasComERS2500_26TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26TPwr = _S5ChasComERS2500_26TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 95)
)
_S5ChasComERS2500_26TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26TPwr_Main = _S5ChasComERS2500_26TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 95, 1)
)
_S5ChasComERS2500_26TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26TPwr_RedundFeed = _S5ChasComERS2500_26TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 95, 2)
)
_S5ChasComERS2500_26T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26T_PWRPwr = _S5ChasComERS2500_26T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 96)
)
_S5ChasComERS2500_26T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26T_PWRPwr_Main = _S5ChasComERS2500_26T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 96, 1)
)
_S5ChasComERS2500_26T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26T_PWRPwr_RedundFeed = _S5ChasComERS2500_26T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 96, 2)
)
_S5ChasComERS2500_50TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50TPwr = _S5ChasComERS2500_50TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 97)
)
_S5ChasComERS2500_50TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50TPwr_Main = _S5ChasComERS2500_50TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 97, 1)
)
_S5ChasComERS2500_50TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50TPwr_RedundFeed = _S5ChasComERS2500_50TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 97, 2)
)
_S5ChasComERS2500_50T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50T_PWRPwr = _S5ChasComERS2500_50T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 98)
)
_S5ChasComERS2500_50T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50T_PWRPwr_Main = _S5ChasComERS2500_50T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 98, 1)
)
_S5ChasComERS2500_50T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50T_PWRPwr_RedundFeed = _S5ChasComERS2500_50T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 98, 2)
)
_S5ChasComERS4526GTX_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTX_PWRPwr = _S5ChasComERS4526GTX_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 99)
)
_S5ChasComERS4526GTX_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTX_PWRPwr_Main = _S5ChasComERS4526GTX_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 99, 1)
)
_S5ChasComERS4526GTX_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTX_PWRPwr_RedundFeed = _S5ChasComERS4526GTX_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 99, 2)
)
_S5ChasComERS4526GTXPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTXPwr = _S5ChasComERS4526GTXPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 100)
)
_S5ChasComERS4526GTXPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTXPwr_Main = _S5ChasComERS4526GTXPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 100, 1)
)
_S5ChasComERS4526GTXPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTXPwr_RedundFeed = _S5ChasComERS4526GTXPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 100, 2)
)
_S5ChasComERS4524GTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GTPwr = _S5ChasComERS4524GTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 101)
)
_S5ChasComERS4524GTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GTPwr_Main = _S5ChasComERS4524GTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 101, 1)
)
_S5ChasComERS4524GTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GTPwr_RedundFeed = _S5ChasComERS4524GTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 101, 2)
)
_S5ChasComERS4526TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526TPwr = _S5ChasComERS4526TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 102)
)
_S5ChasComERS4526TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526TPwr_Main = _S5ChasComERS4526TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 102, 1)
)
_S5ChasComERS4526TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526TPwr_RedundFeed = _S5ChasComERS4526TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 102, 2)
)
_S5ChasComERS4526T_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWRPwr = _S5ChasComERS4526T_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 103)
)
_S5ChasComERS4526T_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWRPwr_Main = _S5ChasComERS4526T_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 103, 1)
)
_S5ChasComERS4526T_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWRPwr_RedundFeed = _S5ChasComERS4526T_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 103, 2)
)
_S5ChasComERS5698_TFD_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr = _S5ChasComERS5698_TFD_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104)
)
_S5ChasComERS5698_TFD_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_Main = _S5ChasComERS5698_TFD_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 1)
)
_S5ChasComERS5698_TFD_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_RedundFeed = _S5ChasComERS5698_TFD_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 2)
)
_S5ChasComERS5698_TFD_PWRPwr_None_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_None = _S5ChasComERS5698_TFD_PWRPwr_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 3)
)
_S5ChasComERS5698_TFD_PWRPwr_AC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_AC_DC_12V_300W = _S5ChasComERS5698_TFD_PWRPwr_AC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 4)
)
_S5ChasComERS5698_TFD_PWRPwr_DC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_DC_DC_12V_300W = _S5ChasComERS5698_TFD_PWRPwr_DC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 5)
)
_S5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_600W = _S5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 6)
)
_S5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_600W = _S5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 7)
)
_S5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_1000W = _S5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 8)
)
_S5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_1000W = _S5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 104, 9)
)
_S5ChasComERS5698_TFDPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr = _S5ChasComERS5698_TFDPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105)
)
_S5ChasComERS5698_TFDPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_Main = _S5ChasComERS5698_TFDPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 1)
)
_S5ChasComERS5698_TFDPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_RedundFeed = _S5ChasComERS5698_TFDPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 2)
)
_S5ChasComERS5698_TFDPwr_None_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_None = _S5ChasComERS5698_TFDPwr_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 3)
)
_S5ChasComERS5698_TFDPwr_AC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_AC_DC_12V_300W = _S5ChasComERS5698_TFDPwr_AC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 4)
)
_S5ChasComERS5698_TFDPwr_DC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_DC_DC_12V_300W = _S5ChasComERS5698_TFDPwr_DC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 5)
)
_S5ChasComERS5698_TFDPwr_AC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_AC_DC_48V_600W = _S5ChasComERS5698_TFDPwr_AC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 6)
)
_S5ChasComERS5698_TFDPwr_DC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_DC_DC_48V_600W = _S5ChasComERS5698_TFDPwr_DC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 7)
)
_S5ChasComERS5698_TFDPwr_AC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_AC_DC_48V_1000W = _S5ChasComERS5698_TFDPwr_AC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 8)
)
_S5ChasComERS5698_TFDPwr_DC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDPwr_DC_DC_48V_1000W = _S5ChasComERS5698_TFDPwr_DC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 105, 9)
)
_S5ChasComERS5650_TD_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr = _S5ChasComERS5650_TD_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106)
)
_S5ChasComERS5650_TD_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_Main = _S5ChasComERS5650_TD_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 1)
)
_S5ChasComERS5650_TD_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_RedundFeed = _S5ChasComERS5650_TD_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 2)
)
_S5ChasComERS5650_TD_PWRPwr_None_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_None = _S5ChasComERS5650_TD_PWRPwr_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 3)
)
_S5ChasComERS5650_TD_PWRPwr_AC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_AC_DC_12V_300W = _S5ChasComERS5650_TD_PWRPwr_AC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 4)
)
_S5ChasComERS5650_TD_PWRPwr_DC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_DC_DC_12V_300W = _S5ChasComERS5650_TD_PWRPwr_DC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 5)
)
_S5ChasComERS5650_TD_PWRPwr_AC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_AC_DC_48V_600W = _S5ChasComERS5650_TD_PWRPwr_AC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 6)
)
_S5ChasComERS5650_TD_PWRPwr_DC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_DC_DC_48V_600W = _S5ChasComERS5650_TD_PWRPwr_DC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 7)
)
_S5ChasComERS5650_TD_PWRPwr_AC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_AC_DC_48V_1000W = _S5ChasComERS5650_TD_PWRPwr_AC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 8)
)
_S5ChasComERS5650_TD_PWRPwr_DC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRPwr_DC_DC_48V_1000W = _S5ChasComERS5650_TD_PWRPwr_DC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 106, 9)
)
_S5ChasComERS5650_TDPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr = _S5ChasComERS5650_TDPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107)
)
_S5ChasComERS5650_TDPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_Main = _S5ChasComERS5650_TDPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 1)
)
_S5ChasComERS5650_TDPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_RedundFeed = _S5ChasComERS5650_TDPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 2)
)
_S5ChasComERS5650_TDPwr_None_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_None = _S5ChasComERS5650_TDPwr_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 3)
)
_S5ChasComERS5650_TDPwr_AC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_AC_DC_12V_300W = _S5ChasComERS5650_TDPwr_AC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 4)
)
_S5ChasComERS5650_TDPwr_DC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_DC_DC_12V_300W = _S5ChasComERS5650_TDPwr_DC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 5)
)
_S5ChasComERS5650_TDPwr_AC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_AC_DC_48V_600W = _S5ChasComERS5650_TDPwr_AC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 6)
)
_S5ChasComERS5650_TDPwr_DC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_DC_DC_48V_600W = _S5ChasComERS5650_TDPwr_DC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 7)
)
_S5ChasComERS5650_TDPwr_AC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_AC_DC_48V_1000W = _S5ChasComERS5650_TDPwr_AC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 8)
)
_S5ChasComERS5650_TDPwr_DC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDPwr_DC_DC_48V_1000W = _S5ChasComERS5650_TDPwr_DC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 107, 9)
)
_S5ChasComERS5632_FDPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr = _S5ChasComERS5632_FDPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108)
)
_S5ChasComERS5632_FDPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_Main = _S5ChasComERS5632_FDPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 1)
)
_S5ChasComERS5632_FDPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_RedundFeed = _S5ChasComERS5632_FDPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 2)
)
_S5ChasComERS5632_FDPwr_None_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_None = _S5ChasComERS5632_FDPwr_None_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 3)
)
_S5ChasComERS5632_FDPwr_AC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_AC_DC_12V_300W = _S5ChasComERS5632_FDPwr_AC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 4)
)
_S5ChasComERS5632_FDPwr_DC_DC_12V_300W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_DC_DC_12V_300W = _S5ChasComERS5632_FDPwr_DC_DC_12V_300W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 5)
)
_S5ChasComERS5632_FDPwr_AC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_AC_DC_48V_600W = _S5ChasComERS5632_FDPwr_AC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 6)
)
_S5ChasComERS5632_FDPwr_DC_DC_48V_600W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_DC_DC_48V_600W = _S5ChasComERS5632_FDPwr_DC_DC_48V_600W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 7)
)
_S5ChasComERS5632_FDPwr_AC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_AC_DC_48V_1000W = _S5ChasComERS5632_FDPwr_AC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 8)
)
_S5ChasComERS5632_FDPwr_DC_DC_48V_1000W_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDPwr_DC_DC_48V_1000W = _S5ChasComERS5632_FDPwr_DC_DC_48V_1000W_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 108, 9)
)
_S5ChasComESU1860SPwr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SPwr = _S5ChasComESU1860SPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 109)
)
_S5ChasComESU1860SPwr_Main_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SPwr_Main_DC = _S5ChasComESU1860SPwr_Main_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 109, 1)
)
_S5ChasComESU1860SPwr_Main_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SPwr_Main_AC = _S5ChasComESU1860SPwr_Main_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 109, 2)
)
_S5ChasComESU1860SPwr_RedundFeed_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SPwr_RedundFeed_DC = _S5ChasComESU1860SPwr_RedundFeed_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 109, 3)
)
_S5ChasComESU1860SPwr_RedundFeed_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SPwr_RedundFeed_AC = _S5ChasComESU1860SPwr_RedundFeed_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 109, 4)
)
_S5ChasComESU1860BPwr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BPwr = _S5ChasComESU1860BPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 110)
)
_S5ChasComESU1860BPwr_Main_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BPwr_Main_DC = _S5ChasComESU1860BPwr_Main_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 110, 1)
)
_S5ChasComESU1860BPwr_Main_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BPwr_Main_AC = _S5ChasComESU1860BPwr_Main_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 110, 2)
)
_S5ChasComESU1860BPwr_RedundFeed_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BPwr_RedundFeed_DC = _S5ChasComESU1860BPwr_RedundFeed_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 110, 3)
)
_S5ChasComESU1860BPwr_RedundFeed_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BPwr_RedundFeed_AC = _S5ChasComESU1860BPwr_RedundFeed_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 110, 4)
)
_S5ChasComESU1860TPwr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TPwr = _S5ChasComESU1860TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 111)
)
_S5ChasComESU1860TPwr_Main_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TPwr_Main_DC = _S5ChasComESU1860TPwr_Main_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 111, 1)
)
_S5ChasComESU1860TPwr_Main_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TPwr_Main_AC = _S5ChasComESU1860TPwr_Main_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 111, 2)
)
_S5ChasComESU1860TPwr_RedundFeed_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TPwr_RedundFeed_DC = _S5ChasComESU1860TPwr_RedundFeed_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 111, 3)
)
_S5ChasComESU1860TPwr_RedundFeed_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TPwr_RedundFeed_AC = _S5ChasComESU1860TPwr_RedundFeed_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 111, 4)
)
_S5ChasComESU1860VPwr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VPwr = _S5ChasComESU1860VPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 112)
)
_S5ChasComESU1860VPwr_Main_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VPwr_Main_DC = _S5ChasComESU1860VPwr_Main_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 112, 1)
)
_S5ChasComESU1860VPwr_Main_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VPwr_Main_AC = _S5ChasComESU1860VPwr_Main_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 112, 2)
)
_S5ChasComESU1860VPwr_RedundFeed_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VPwr_RedundFeed_DC = _S5ChasComESU1860VPwr_RedundFeed_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 112, 3)
)
_S5ChasComESU1860VPwr_RedundFeed_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VPwr_RedundFeed_AC = _S5ChasComESU1860VPwr_RedundFeed_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 112, 4)
)
_S5ChasComESU1880SPwr_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SPwr = _S5ChasComESU1880SPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 113)
)
_S5ChasComESU1880SPwr_Main_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SPwr_Main_DC = _S5ChasComESU1880SPwr_Main_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 113, 1)
)
_S5ChasComESU1880SPwr_Main_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SPwr_Main_AC = _S5ChasComESU1880SPwr_Main_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 113, 2)
)
_S5ChasComESU1880SPwr_RedundFeed_DC_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SPwr_RedundFeed_DC = _S5ChasComESU1880SPwr_RedundFeed_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 113, 3)
)
_S5ChasComESU1880SPwr_RedundFeed_AC_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SPwr_RedundFeed_AC = _S5ChasComESU1880SPwr_RedundFeed_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 113, 4)
)
_S5ChasComERS4524GT_PWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GT_PWRPwr = _S5ChasComERS4524GT_PWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 114)
)
_S5ChasComERS4524GT_PWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GT_PWRPwr_Main = _S5ChasComERS4524GT_PWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 114, 1)
)
_S5ChasComERS4524GT_PWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GT_PWRPwr_RedundFeed = _S5ChasComERS4524GT_PWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 114, 2)
)
_S5ChasComERS6628XSGTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS6628XSGTPwr = _S5ChasComERS6628XSGTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 115)
)
_S5ChasComERS6628XSGTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS6628XSGTPwr_Main = _S5ChasComERS6628XSGTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 115, 1)
)
_S5ChasComERS6628XSGTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS6628XSGTPwr_RedundFeed = _S5ChasComERS6628XSGTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 115, 2)
)
_S5ChasComERS6632XTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS6632XTSPwr = _S5ChasComERS6632XTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 116)
)
_S5ChasComERS6632XTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS6632XTSPwr_Main = _S5ChasComERS6632XTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 116, 1)
)
_S5ChasComERS6632XTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS6632XTSPwr_RedundFeed = _S5ChasComERS6632XTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 116, 2)
)
_S5ChasComWC8180Pwr_ObjectIdentity = ObjectIdentity
s5ChasComWC8180Pwr = _S5ChasComWC8180Pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 117)
)
_S5ChasComWC8180Pwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComWC8180Pwr_Main = _S5ChasComWC8180Pwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 117, 1)
)
_S5ChasComWC8180Pwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComWC8180Pwr_RedundFeed = _S5ChasComWC8180Pwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 117, 2)
)
_S5ChasComERS4526T_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWR_PLUSPwr = _S5ChasComERS4526T_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 118)
)
_S5ChasComERS4526T_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWR_PLUSPwr_Main = _S5ChasComERS4526T_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 118, 1)
)
_S5ChasComERS4526T_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4526T_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 118, 2)
)
_S5ChasComERS4550T_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWR_PLUSPwr = _S5ChasComERS4550T_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 119)
)
_S5ChasComERS4550T_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWR_PLUSPwr_Main = _S5ChasComERS4550T_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 119, 1)
)
_S5ChasComERS4550T_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4550T_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 119, 2)
)
_S5ChasComERS4826GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTS_PWR_PLUSPwr = _S5ChasComERS4826GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 120)
)
_S5ChasComERS4826GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTS_PWR_PLUSPwr_Main = _S5ChasComERS4826GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 120, 1)
)
_S5ChasComERS4826GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4826GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 120, 2)
)
_S5ChasComERS4850GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTS_PWR_PLUSPwr = _S5ChasComERS4850GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 121)
)
_S5ChasComERS4850GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTS_PWR_PLUSPwr_Main = _S5ChasComERS4850GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 121, 1)
)
_S5ChasComERS4850GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4850GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 121, 2)
)
_S5ChasComERS4826GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTSPwr = _S5ChasComERS4826GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 122)
)
_S5ChasComERS4826GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTSPwr_Main = _S5ChasComERS4826GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 122, 1)
)
_S5ChasComERS4826GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTSPwr_RedundFeed = _S5ChasComERS4826GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 122, 2)
)
_S5ChasComERS4850GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTSPwr = _S5ChasComERS4850GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 123)
)
_S5ChasComERS4850GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTSPwr_Main = _S5ChasComERS4850GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 123, 1)
)
_S5ChasComERS4850GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTSPwr_RedundFeed = _S5ChasComERS4850GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 123, 2)
)
_S5ChasComVSP7024XLSPwr_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XLSPwr = _S5ChasComVSP7024XLSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 124)
)
_S5ChasComVSP7024XLSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XLSPwr_Main = _S5ChasComVSP7024XLSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 124, 1)
)
_S5ChasComVSP7024XLSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XLSPwr_RedundFeed = _S5ChasComVSP7024XLSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 124, 2)
)
_S5ChasComERS3510GTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GTPwr = _S5ChasComERS3510GTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 125)
)
_S5ChasComERS3510GTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GTPwr_Main = _S5ChasComERS3510GTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 125, 1)
)
_S5ChasComERS3510GTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GTPwr_RedundFeed = _S5ChasComERS3510GTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 125, 2)
)
_S5ChasComERS3510GT_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GT_PWR_PLUSPwr = _S5ChasComERS3510GT_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 126)
)
_S5ChasComERS3510GT_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GT_PWR_PLUSPwr_Main = _S5ChasComERS3510GT_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 126, 1)
)
_S5ChasComERS3510GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GT_PWR_PLUSPwr_RedundFeed = _S5ChasComERS3510GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 126, 2)
)
_S5ChasComERS3524GTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GTPwr = _S5ChasComERS3524GTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 127)
)
_S5ChasComERS3524GTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GTPwr_Main = _S5ChasComERS3524GTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 127, 1)
)
_S5ChasComERS3524GTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GTPwr_RedundFeed = _S5ChasComERS3524GTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 127, 2)
)
_S5ChasComERS3524GT_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GT_PWR_PLUSPwr = _S5ChasComERS3524GT_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 128)
)
_S5ChasComERS3524GT_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GT_PWR_PLUSPwr_Main = _S5ChasComERS3524GT_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 128, 1)
)
_S5ChasComERS3524GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GT_PWR_PLUSPwr_RedundFeed = _S5ChasComERS3524GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 128, 2)
)
_S5ChasComERS3526GTPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GTPwr = _S5ChasComERS3526GTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 129)
)
_S5ChasComERS3526GTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GTPwr_Main = _S5ChasComERS3526GTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 129, 1)
)
_S5ChasComERS3526GTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GTPwr_RedundFeed = _S5ChasComERS3526GTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 129, 2)
)
_S5ChasComERS3526GT_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GT_PWR_PLUSPwr = _S5ChasComERS3526GT_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 130)
)
_S5ChasComERS3526GT_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GT_PWR_PLUSPwr_Main = _S5ChasComERS3526GT_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 130, 1)
)
_S5ChasComERS3526GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GT_PWR_PLUSPwr_RedundFeed = _S5ChasComERS3526GT_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 130, 2)
)
_S5ChasComERS3526TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3526TPwr = _S5ChasComERS3526TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 131)
)
_S5ChasComERS3526TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3526TPwr_Main = _S5ChasComERS3526TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 131, 1)
)
_S5ChasComERS3526TPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3526TPwr_RedundFeed = _S5ChasComERS3526TPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 131, 2)
)
_S5ChasComERS3526T_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3526T_PWR_PLUSPwr = _S5ChasComERS3526T_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 132)
)
_S5ChasComERS3526T_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3526T_PWR_PLUSPwr_Main = _S5ChasComERS3526T_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 132, 1)
)
_S5ChasComERS3526T_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS3526T_PWR_PLUSPwr_RedundFeed = _S5ChasComERS3526T_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 132, 2)
)
_S5ChasComERS3549GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTSPwr = _S5ChasComERS3549GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 133)
)
_S5ChasComERS3549GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTSPwr_Main = _S5ChasComERS3549GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 133, 1)
)
_S5ChasComERS3549GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSPwr = _S5ChasComERS3549GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 134)
)
_S5ChasComERS3549GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSPwr_Main = _S5ChasComERS3549GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 134, 1)
)
_S5ChasComVSP7024XTPwr_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XTPwr = _S5ChasComVSP7024XTPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 135)
)
_S5ChasComVSP7024XTPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XTPwr_Main = _S5ChasComVSP7024XTPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 135, 1)
)
_S5ChasComVSP7024XTPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XTPwr_RedundFeed = _S5ChasComVSP7024XTPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 135, 2)
)
_S5ChasComERS5928GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTSPwr = _S5ChasComERS5928GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 136)
)
_S5ChasComERS5928GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTSPwr_Main = _S5ChasComERS5928GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 136, 1)
)
_S5ChasComERS5928GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTSPwr_RedundFeed = _S5ChasComERS5928GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 136, 2)
)
_S5ChasComERS5928GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_PWR_PLUSPwr = _S5ChasComERS5928GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 137)
)
_S5ChasComERS5928GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_PWR_PLUSPwr_Main = _S5ChasComERS5928GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 137, 1)
)
_S5ChasComERS5928GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS5928GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 137, 2)
)
_S5ChasComERS5952GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTSPwr = _S5ChasComERS5952GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 138)
)
_S5ChasComERS5952GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTSPwr_Main = _S5ChasComERS5952GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 138, 1)
)
_S5ChasComERS5952GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTSPwr_RedundFeed = _S5ChasComERS5952GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 138, 2)
)
_S5ChasComERS5952GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTS_PWR_PLUSPwr = _S5ChasComERS5952GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 139)
)
_S5ChasComERS5952GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTS_PWR_PLUSPwr_Main = _S5ChasComERS5952GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 139, 1)
)
_S5ChasComERS5952GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS5952GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 139, 2)
)
_S5ChasComERS5928GTS_UPWRPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_UPWRPwr = _S5ChasComERS5928GTS_UPWRPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 140)
)
_S5ChasComERS5928GTS_UPWRPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_UPWRPwr_Main = _S5ChasComERS5928GTS_UPWRPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 140, 1)
)
_S5ChasComERS5928GTS_UPWRPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_UPWRPwr_RedundFeed = _S5ChasComERS5928GTS_UPWRPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 140, 2)
)
_S5ChasComERS59100GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTSPwr = _S5ChasComERS59100GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 141)
)
_S5ChasComERS59100GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTSPwr_Main = _S5ChasComERS59100GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 141, 1)
)
_S5ChasComERS59100GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTSPwr_RedundFeed = _S5ChasComERS59100GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 141, 2)
)
_S5ChasComERS59100GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTS_PWR_PLUSPwr = _S5ChasComERS59100GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 142)
)
_S5ChasComERS59100GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTS_PWR_PLUSPwr_Main = _S5ChasComERS59100GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 142, 1)
)
_S5ChasComERS59100GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS59100GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 142, 2)
)
_S5ChasComERS4926GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTSPwr = _S5ChasComERS4926GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 143)
)
_S5ChasComERS4926GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTSPwr_Main = _S5ChasComERS4926GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 143, 1)
)
_S5ChasComERS4926GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTSPwr_RedundFeed = _S5ChasComERS4926GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 143, 2)
)
_S5ChasComERS4926GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTS_PWR_PLUSPwr = _S5ChasComERS4926GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 144)
)
_S5ChasComERS4926GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTS_PWR_PLUSPwr_Main = _S5ChasComERS4926GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 144, 1)
)
_S5ChasComERS4926GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4926GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 144, 2)
)
_S5ChasComERS4950GTSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTSPwr = _S5ChasComERS4950GTSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 145)
)
_S5ChasComERS4950GTSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTSPwr_Main = _S5ChasComERS4950GTSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 145, 1)
)
_S5ChasComERS4950GTSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTSPwr_RedundFeed = _S5ChasComERS4950GTSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 145, 2)
)
_S5ChasComERS4950GTS_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTS_PWR_PLUSPwr = _S5ChasComERS4950GTS_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 146)
)
_S5ChasComERS4950GTS_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTS_PWR_PLUSPwr_Main = _S5ChasComERS4950GTS_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 146, 1)
)
_S5ChasComERS4950GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTS_PWR_PLUSPwr_RedundFeed = _S5ChasComERS4950GTS_PWR_PLUSPwr_RedundFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 146, 2)
)
_S5ChasComERS3550TPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3550TPwr = _S5ChasComERS3550TPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 147)
)
_S5ChasComERS3550TPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3550TPwr_Main = _S5ChasComERS3550TPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 147, 1)
)
_S5ChasComERS3550T_PWR_PLUSPwr_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSPwr = _S5ChasComERS3550T_PWR_PLUSPwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 148)
)
_S5ChasComERS3550T_PWR_PLUSPwr_Main_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSPwr_Main = _S5ChasComERS3550T_PWR_PLUSPwr_Main_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 8, 148, 1)
)
_S5ChasComMTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComMTmpSnr = _S5ChasComMTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9)
)
_S5ChasComM5000TmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComM5000TmpSnr = _S5ChasComM5000TmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 12)
)
_S5ChasComM5000TmpSnrA_ObjectIdentity = ObjectIdentity
s5ChasComM5000TmpSnrA = _S5ChasComM5000TmpSnrA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 12, 1)
)
_S5ChasComM5005TmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComM5005TmpSnr = _S5ChasComM5005TmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 17)
)
_S5ChasComM5005TmpSnrA_ObjectIdentity = ObjectIdentity
s5ChasComM5005TmpSnrA = _S5ChasComM5005TmpSnrA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 17, 1)
)
_S5ChasComESU1860STmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860STmpSnr = _S5ChasComESU1860STmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 18)
)
_S5ChasComESU1860STmpSnrCPU_ObjectIdentity = ObjectIdentity
s5ChasComESU1860STmpSnrCPU = _S5ChasComESU1860STmpSnrCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 18, 1)
)
_S5ChasComESU1860STmpSnrBoard1_ObjectIdentity = ObjectIdentity
s5ChasComESU1860STmpSnrBoard1 = _S5ChasComESU1860STmpSnrBoard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 18, 2)
)
_S5ChasComESU1860STmpSnrBoard2_ObjectIdentity = ObjectIdentity
s5ChasComESU1860STmpSnrBoard2 = _S5ChasComESU1860STmpSnrBoard2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 18, 3)
)
_S5ChasComESU1860BTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BTmpSnr = _S5ChasComESU1860BTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 19)
)
_S5ChasComESU1860BTmpSnrCPU_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BTmpSnrCPU = _S5ChasComESU1860BTmpSnrCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 19, 1)
)
_S5ChasComESU1860BTmpSnrBoard1_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BTmpSnrBoard1 = _S5ChasComESU1860BTmpSnrBoard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 19, 2)
)
_S5ChasComESU1860BTmpSnrBoard2_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BTmpSnrBoard2 = _S5ChasComESU1860BTmpSnrBoard2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 19, 3)
)
_S5ChasComESU1860TTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TTmpSnr = _S5ChasComESU1860TTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 20)
)
_S5ChasComESU1860TTmpSnrCPU_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TTmpSnrCPU = _S5ChasComESU1860TTmpSnrCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 20, 1)
)
_S5ChasComESU1860TTmpSnrBoard1_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TTmpSnrBoard1 = _S5ChasComESU1860TTmpSnrBoard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 20, 2)
)
_S5ChasComESU1860TTmpSnrBoard2_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TTmpSnrBoard2 = _S5ChasComESU1860TTmpSnrBoard2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 20, 3)
)
_S5ChasComESU1860VTmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VTmpSnr = _S5ChasComESU1860VTmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 21)
)
_S5ChasComESU1860VTmpSnrCPU_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VTmpSnrCPU = _S5ChasComESU1860VTmpSnrCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 21, 1)
)
_S5ChasComESU1860VTmpSnrBoard1_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VTmpSnrBoard1 = _S5ChasComESU1860VTmpSnrBoard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 21, 2)
)
_S5ChasComESU1860VTmpSnrBoard2_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VTmpSnrBoard2 = _S5ChasComESU1860VTmpSnrBoard2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 21, 3)
)
_S5ChasComESU1880STmpSnr_ObjectIdentity = ObjectIdentity
s5ChasComESU1880STmpSnr = _S5ChasComESU1880STmpSnr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 22)
)
_S5ChasComESU1880STmpSnrCPU_ObjectIdentity = ObjectIdentity
s5ChasComESU1880STmpSnrCPU = _S5ChasComESU1880STmpSnrCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 22, 1)
)
_S5ChasComESU1880STmpSnrBoard1_ObjectIdentity = ObjectIdentity
s5ChasComESU1880STmpSnrBoard1 = _S5ChasComESU1880STmpSnrBoard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 22, 2)
)
_S5ChasComESU1880STmpSnrBoard2_ObjectIdentity = ObjectIdentity
s5ChasComESU1880STmpSnrBoard2 = _S5ChasComESU1880STmpSnrBoard2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 9, 22, 3)
)
_S5ChasComMFan_ObjectIdentity = ObjectIdentity
s5ChasComMFan = _S5ChasComMFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10)
)
_S5ChasComM5000Fan_ObjectIdentity = ObjectIdentity
s5ChasComM5000Fan = _S5ChasComM5000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 12)
)
_S5ChasComM5000FanA_ObjectIdentity = ObjectIdentity
s5ChasComM5000FanA = _S5ChasComM5000FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 12, 1)
)
_S5ChasComM5000FanAA_ObjectIdentity = ObjectIdentity
s5ChasComM5000FanAA = _S5ChasComM5000FanAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 12, 2)
)
_S5ChasComM1032xFan_ObjectIdentity = ObjectIdentity
s5ChasComM1032xFan = _S5ChasComM1032xFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 16)
)
_S5ChasComM1032xFanA_ObjectIdentity = ObjectIdentity
s5ChasComM1032xFanA = _S5ChasComM1032xFanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 16, 1)
)
_S5ChasComM5005Fan_ObjectIdentity = ObjectIdentity
s5ChasComM5005Fan = _S5ChasComM5005Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 17)
)
_S5ChasComM5005FanA_ObjectIdentity = ObjectIdentity
s5ChasComM5005FanA = _S5ChasComM5005FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 17, 1)
)
_S5ChasComM5DN000Fan_ObjectIdentity = ObjectIdentity
s5ChasComM5DN000Fan = _S5ChasComM5DN000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 24)
)
_S5ChasComM5DN002Fan_1U_ObjectIdentity = ObjectIdentity
s5ChasComM5DN002Fan_1U = _S5ChasComM5DN002Fan_1U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 24, 1)
)
_S5ChasComM5DN003Fan_2U_ObjectIdentity = ObjectIdentity
s5ChasComM5DN003Fan_2U = _S5ChasComM5DN003Fan_2U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 24, 2)
)
_S5ChasComMNBayStackFan_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackFan = _S5ChasComMNBayStackFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 25)
)
_S5ChasComMNBayStackFanA_ObjectIdentity = ObjectIdentity
s5ChasComMNBayStackFanA = _S5ChasComMNBayStackFanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 25, 1)
)
_S5ChasComMBayStack100Fan_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100Fan = _S5ChasComMBayStack100Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 27)
)
_S5ChasComMBayStack100FanA_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack100FanA = _S5ChasComMBayStack100FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 27, 1)
)
_S5ChasComM3000Fan_ObjectIdentity = ObjectIdentity
s5ChasComM3000Fan = _S5ChasComM3000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 28)
)
_S5ChasComM3000FanA_ObjectIdentity = ObjectIdentity
s5ChasComM3000FanA = _S5ChasComM3000FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 28, 1)
)
_S5ChasComM28200Fan_ObjectIdentity = ObjectIdentity
s5ChasComM28200Fan = _S5ChasComM28200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 30)
)
_S5ChasComM28200FanA_ObjectIdentity = ObjectIdentity
s5ChasComM28200FanA = _S5ChasComM28200FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 30, 1)
)
_S5ChasComMBayStack301Fan_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301Fan = _S5ChasComMBayStack301Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 31)
)
_S5ChasComMBayStack301FanA_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack301FanA = _S5ChasComMBayStack301FanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 31, 1)
)
_S5ChasComSwitchNodeFan_ObjectIdentity = ObjectIdentity
s5ChasComSwitchNodeFan = _S5ChasComSwitchNodeFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 32)
)
_S5ChasComMBayStackTrFan_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrFan = _S5ChasComMBayStackTrFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 36)
)
_S5ChasComMBayStackTrFanA_ObjectIdentity = ObjectIdentity
s5ChasComMBayStackTrFanA = _S5ChasComMBayStackTrFanA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 36, 1)
)
_S5ChasComBayStack150Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150Fan = _S5ChasComBayStack150Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 41)
)
_S5ChasComBayStack150MasterFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack150MasterFan = _S5ChasComBayStack150MasterFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 41, 1)
)
_S5ChasComMBayStack303_304Fan_ObjectIdentity = ObjectIdentity
s5ChasComMBayStack303_304Fan = _S5ChasComMBayStack303_304Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 42)
)
_S5ChasComBayStack200Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200Fan = _S5ChasComBayStack200Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 43)
)
_S5ChasComBayStack200MasterFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack200MasterFan = _S5ChasComBayStack200MasterFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 43, 1)
)
_S5ChasComBayStack250Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250Fan = _S5ChasComBayStack250Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 44)
)
_S5ChasComBayStack250MasterFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250MasterFan = _S5ChasComBayStack250MasterFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 44, 1)
)
_S5ChasComBayStack250SlaveFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack250SlaveFan = _S5ChasComBayStack250SlaveFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 44, 2)
)
_S5ChasComMAccelar8010Fan_ObjectIdentity = ObjectIdentity
s5ChasComMAccelar8010Fan = _S5ChasComMAccelar8010Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 45)
)
_S5ChasComBPS2000Fan_ObjectIdentity = ObjectIdentity
s5ChasComBPS2000Fan = _S5ChasComBPS2000Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 47)
)
_S5ChasComBPS2000UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBPS2000UnitFan = _S5ChasComBPS2000UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 47, 1)
)
_S5ChasComBayStack450Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450Fan = _S5ChasComBayStack450Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 48)
)
_S5ChasComBayStack450UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450UnitFan = _S5ChasComBayStack450UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 48, 1)
)
_S5ChasComBayStack450RedundPwrFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack450RedundPwrFan = _S5ChasComBayStack450RedundPwrFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 48, 2)
)
_S5ChasComBayStack3580Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack3580Fan = _S5ChasComBayStack3580Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 49)
)
_S5ChasComBayStack3580UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack3580UnitFan = _S5ChasComBayStack3580UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 49, 1)
)
_S5ChasComBayStack420Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack420Fan = _S5ChasComBayStack420Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 50)
)
_S5ChasComMetro1200ESMFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1200ESMFan = _S5ChasComMetro1200ESMFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 51)
)
_S5ChasComMetro1200ESMUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1200ESMUnitFan = _S5ChasComMetro1200ESMUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 51, 1)
)
_S5ChasComBayStack380Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380Fan = _S5ChasComBayStack380Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 52)
)
_S5ChasComBayStack380UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380UnitFan = _S5ChasComBayStack380UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 52, 1)
)
_S5ChasComBayStack470Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470Fan = _S5ChasComBayStack470Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 53)
)
_S5ChasComBayStack470UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470UnitFan = _S5ChasComBayStack470UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 53, 1)
)
_S5ChasComMetro1450ESMFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1450ESMFan = _S5ChasComMetro1450ESMFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 54)
)
_S5ChasComMetro1450ESMUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1450ESMUnitFan = _S5ChasComMetro1450ESMUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 54, 1)
)
_S5ChasComMetro1400ESMFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1400ESMFan = _S5ChasComMetro1400ESMFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 55)
)
_S5ChasComMetro1400ESMUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComMetro1400ESMUnitFan = _S5ChasComMetro1400ESMUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 55, 1)
)
_S5ChasComBayStack460_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack460_24T_PWRFan = _S5ChasComBayStack460_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 56)
)
_S5ChasComBayStack460_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack460_24T_PWRUnitFan = _S5ChasComBayStack460_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 56, 1)
)
_S5ChasComBayStack380_24F_Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380_24F_Fan = _S5ChasComBayStack380_24F_Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 57)
)
_S5ChasComBayStack380_24FUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack380_24FUnitFan = _S5ChasComBayStack380_24FUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 57, 1)
)
_S5ChasComBayStack5510_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_24TFan = _S5ChasComBayStack5510_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 58)
)
_S5ChasComBayStack5510_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_24TUnitFan = _S5ChasComBayStack5510_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 58, 1)
)
_S5ChasComBayStack5510_48TFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_48TFan = _S5ChasComBayStack5510_48TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 59)
)
_S5ChasComBayStack5510_48TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5510_48TUnitFan = _S5ChasComBayStack5510_48TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 59, 1)
)
_S5ChasComBayStack470_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24TFan = _S5ChasComBayStack470_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 60)
)
_S5ChasComBayStack470_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24TUnitFan = _S5ChasComBayStack470_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 60, 1)
)
_S5ChasComWLANAccessPoint2220Fan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2220Fan = _S5ChasComWLANAccessPoint2220Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 61)
)
_S5ChasComWLANAccessPoint2220UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2220UnitFan = _S5ChasComWLANAccessPoint2220UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 61, 1)
)
_S5ChasComWLANSecuritySwitch2250Fan_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2250Fan = _S5ChasComWLANSecuritySwitch2250Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 62)
)
_S5ChasComWLANSecuritySwitch2250UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2250UnitFan = _S5ChasComWLANSecuritySwitch2250UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 62, 1)
)
_S5ChasComBayStack425Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack425Fan = _S5ChasComBayStack425Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 63)
)
_S5ChasComBayStack425UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack425UnitFan = _S5ChasComBayStack425UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 63, 1)
)
_S5ChasComWLANAccessPoint2221Fan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2221Fan = _S5ChasComWLANAccessPoint2221Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 64)
)
_S5ChasComWLANAccessPoint2221UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2221UnitFan = _S5ChasComWLANAccessPoint2221UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 64, 1)
)
_S5ChasComBayStack5520_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_24T_PWRFan = _S5ChasComBayStack5520_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 65)
)
_S5ChasComBayStack5520_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_24T_PWRUnitFan = _S5ChasComBayStack5520_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 65, 1)
)
_S5ChasComBayStack5520_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_48T_PWRFan = _S5ChasComBayStack5520_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 66)
)
_S5ChasComBayStack5520_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack5520_48T_PWRUnitFan = _S5ChasComBayStack5520_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 66, 1)
)
_S5ChasComBayStack325Fan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack325Fan = _S5ChasComBayStack325Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 67)
)
_S5ChasComBayStack325UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack325UnitFan = _S5ChasComBayStack325UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 67, 1)
)
_S5ChasComWLANAccessPoint2225Fan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2225Fan = _S5ChasComWLANAccessPoint2225Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 68)
)
_S5ChasComWLANAccessPoint2225UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWLANAccessPoint2225UnitFan = _S5ChasComWLANAccessPoint2225UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 68, 1)
)
_S5ChasComBayStack470_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24T_PWRFan = _S5ChasComBayStack470_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 69)
)
_S5ChasComBayStack470_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_24T_PWRUnitFan = _S5ChasComBayStack470_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 69, 1)
)
_S5ChasComBayStack470_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_48T_PWRFan = _S5ChasComBayStack470_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 70)
)
_S5ChasComBayStack470_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBayStack470_48T_PWRUnitFan = _S5ChasComBayStack470_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 70, 1)
)
_S5ChasComWLANSecuritySwitch2270Fan_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2270Fan = _S5ChasComWLANSecuritySwitch2270Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 71)
)
_S5ChasComWLANSecuritySwitch2270UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWLANSecuritySwitch2270UnitFan = _S5ChasComWLANSecuritySwitch2270UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 71, 1)
)
_S5ChasComEthernetRoutingSwitch5530_24TFDFan_ObjectIdentity = ObjectIdentity
s5ChasComEthernetRoutingSwitch5530_24TFDFan = _S5ChasComEthernetRoutingSwitch5530_24TFDFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 72)
)
_S5ChasComEthernetRoutingSwitch5530_24TFDUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComEthernetRoutingSwitch5530_24TFDUnitFan = _S5ChasComEthernetRoutingSwitch5530_24TFDUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 72, 1)
)
_S5ChasComEthernetSwitch3510_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComEthernetSwitch3510_24TFan = _S5ChasComEthernetSwitch3510_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 73)
)
_S5ChasComEthernetSwitch3510_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComEthernetSwitch3510_24TUnitFan = _S5ChasComEthernetSwitch3510_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 73, 1)
)
_S5ChasComBES1010_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_24TFan = _S5ChasComBES1010_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 74)
)
_S5ChasComBES1010_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_24TUnitFan = _S5ChasComBES1010_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 74, 1)
)
_S5ChasComBES1010_48TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_48TFan = _S5ChasComBES1010_48TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 75)
)
_S5ChasComBES1010_48TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1010_48TUnitFan = _S5ChasComBES1010_48TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 75, 1)
)
_S5ChasComBES1020_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_24T_PWRFan = _S5ChasComBES1020_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 76)
)
_S5ChasComBES1020_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_24T_PWRUnitFan = _S5ChasComBES1020_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 76, 1)
)
_S5ChasComBES1020_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_48T_PWRFan = _S5ChasComBES1020_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 77)
)
_S5ChasComBES1020_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES1020_48T_PWRUnitFan = _S5ChasComBES1020_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 77, 1)
)
_S5ChasComBES2010_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_24TFan = _S5ChasComBES2010_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 78)
)
_S5ChasComBES2010_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_24TUnitFan = _S5ChasComBES2010_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 78, 1)
)
_S5ChasComBES2010_48TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_48TFan = _S5ChasComBES2010_48TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 79)
)
_S5ChasComBES2010_48TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2010_48TUnitFan = _S5ChasComBES2010_48TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 79, 1)
)
_S5ChasComBES2020_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_24T_PWRFan = _S5ChasComBES2020_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 80)
)
_S5ChasComBES2020_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_24T_PWRUnitFan = _S5ChasComBES2020_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 80, 1)
)
_S5ChasComBES2020_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_48T_PWRFan = _S5ChasComBES2020_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 81)
)
_S5ChasComBES2020_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES2020_48T_PWRUnitFan = _S5ChasComBES2020_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 81, 1)
)
_S5ChasComBES110_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES110_24TFan = _S5ChasComBES110_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 82)
)
_S5ChasComBES110_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES110_24TUnitFan = _S5ChasComBES110_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 82, 1)
)
_S5ChasComBES110_48TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES110_48TFan = _S5ChasComBES110_48TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 83)
)
_S5ChasComBES110_48TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES110_48TUnitFan = _S5ChasComBES110_48TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 83, 1)
)
_S5ChasComBES120_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES120_24T_PWRFan = _S5ChasComBES120_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 84)
)
_S5ChasComBES120_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES120_24T_PWRUnitFan = _S5ChasComBES120_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 84, 1)
)
_S5ChasComBES120_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES120_48T_PWRFan = _S5ChasComBES120_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 85)
)
_S5ChasComBES120_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES120_48T_PWRUnitFan = _S5ChasComBES120_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 85, 1)
)
_S5ChasComBES210_24TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES210_24TFan = _S5ChasComBES210_24TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 86)
)
_S5ChasComBES210_24TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES210_24TUnitFan = _S5ChasComBES210_24TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 86, 1)
)
_S5ChasComBES210_48TFan_ObjectIdentity = ObjectIdentity
s5ChasComBES210_48TFan = _S5ChasComBES210_48TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 87)
)
_S5ChasComBES210_48TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES210_48TUnitFan = _S5ChasComBES210_48TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 87, 1)
)
_S5ChasComBES220_24T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES220_24T_PWRFan = _S5ChasComBES220_24T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 88)
)
_S5ChasComBES220_24T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES220_24T_PWRUnitFan = _S5ChasComBES220_24T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 88, 1)
)
_S5ChasComBES220_48T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComBES220_48T_PWRFan = _S5ChasComBES220_48T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 89)
)
_S5ChasComBES220_48T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComBES220_48T_PWRUnitFan = _S5ChasComBES220_48T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 89, 1)
)
_S5ChasComERS4548GTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GTFan = _S5ChasComERS4548GTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 90)
)
_S5ChasComERS4548GTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GTUnitFan = _S5ChasComERS4548GTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 90, 1)
)
_S5ChasComERS4548GT_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GT_PWRFan = _S5ChasComERS4548GT_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 91)
)
_S5ChasComERS4548GT_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4548GT_PWRUnitFan = _S5ChasComERS4548GT_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 91, 1)
)
_S5ChasComERS4550TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550TFan = _S5ChasComERS4550TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 92)
)
_S5ChasComERS4550TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550TUnitFan = _S5ChasComERS4550TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 92, 1)
)
_S5ChasComERS4550T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWRFan = _S5ChasComERS4550T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 93)
)
_S5ChasComERS4550T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWRUnitFan = _S5ChasComERS4550T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 93, 1)
)
_S5ChasComERS4526FXFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526FXFan = _S5ChasComERS4526FXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 94)
)
_S5ChasComERS4526FXUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526FXUnitFan = _S5ChasComERS4526FXUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 94, 1)
)
_S5ChasComERS2500_26TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26TFan = _S5ChasComERS2500_26TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 95)
)
_S5ChasComERS2500_26TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26TUnitFan = _S5ChasComERS2500_26TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 95, 1)
)
_S5ChasComERS2500_26T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26T_PWRFan = _S5ChasComERS2500_26T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 96)
)
_S5ChasComERS2500_26T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_26T_PWRUnitFan = _S5ChasComERS2500_26T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 96, 1)
)
_S5ChasComERS2500_50TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50TFan = _S5ChasComERS2500_50TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 97)
)
_S5ChasComERS2500_50TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50TUnitFan = _S5ChasComERS2500_50TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 97, 1)
)
_S5ChasComERS2500_50T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50T_PWRFan = _S5ChasComERS2500_50T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 98)
)
_S5ChasComERS2500_50T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS2500_50T_PWRUnitFan = _S5ChasComERS2500_50T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 98, 1)
)
_S5ChasComERS4526GTX_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTX_PWRFan = _S5ChasComERS4526GTX_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 99)
)
_S5ChasComERS4526GTX_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTX_PWRUnitFan = _S5ChasComERS4526GTX_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 99, 1)
)
_S5ChasComERS4526GTXFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTXFan = _S5ChasComERS4526GTXFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 100)
)
_S5ChasComERS4526GTXUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526GTXUnitFan = _S5ChasComERS4526GTXUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 100, 1)
)
_S5ChasComERS4524GTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GTFan = _S5ChasComERS4524GTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 101)
)
_S5ChasComERS4524GTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GTUnitFan = _S5ChasComERS4524GTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 101, 1)
)
_S5ChasComERS4526TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526TFan = _S5ChasComERS4526TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 102)
)
_S5ChasComERS4526TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526TUnitFan = _S5ChasComERS4526TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 102, 1)
)
_S5ChasComERS4526T_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWRFan = _S5ChasComERS4526T_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 103)
)
_S5ChasComERS4526T_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWRUnitFan = _S5ChasComERS4526T_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 103, 1)
)
_S5ChasComERS5698_TFD_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRFan = _S5ChasComERS5698_TFD_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 104)
)
_S5ChasComERS5698_TFD_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFD_PWRUnitFan = _S5ChasComERS5698_TFD_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 104, 1)
)
_S5ChasComERS5698_TFDFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDFan = _S5ChasComERS5698_TFDFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 105)
)
_S5ChasComERS5698_TFDUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5698_TFDUnitFan = _S5ChasComERS5698_TFDUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 105, 1)
)
_S5ChasComERS5650_TD_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRFan = _S5ChasComERS5650_TD_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 106)
)
_S5ChasComERS5650_TD_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TD_PWRUnitFan = _S5ChasComERS5650_TD_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 106, 1)
)
_S5ChasComERS5650_TDFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDFan = _S5ChasComERS5650_TDFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 107)
)
_S5ChasComERS5650_TDUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5650_TDUnitFan = _S5ChasComERS5650_TDUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 107, 1)
)
_S5ChasComERS5632_FDFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDFan = _S5ChasComERS5632_FDFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 108)
)
_S5ChasComERS5632_FDUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5632_FDUnitFan = _S5ChasComERS5632_FDUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 108, 1)
)
_S5ChasComESU1860SFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SFan = _S5ChasComESU1860SFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 109)
)
_S5ChasComESU1860SUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860SUnitFan = _S5ChasComESU1860SUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 109, 1)
)
_S5ChasComESU1860BFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BFan = _S5ChasComESU1860BFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 110)
)
_S5ChasComESU1860BUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860BUnitFan = _S5ChasComESU1860BUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 110, 1)
)
_S5ChasComESU1860TFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TFan = _S5ChasComESU1860TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 111)
)
_S5ChasComESU1860TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860TUnitFan = _S5ChasComESU1860TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 111, 1)
)
_S5ChasComESU1860VFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VFan = _S5ChasComESU1860VFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 112)
)
_S5ChasComESU1860VUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1860VUnitFan = _S5ChasComESU1860VUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 112, 1)
)
_S5ChasComESU1880SFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SFan = _S5ChasComESU1880SFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 113)
)
_S5ChasComESU1880SUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComESU1880SUnitFan = _S5ChasComESU1880SUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 113, 1)
)
_S5ChasComERS4524GT_PWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GT_PWRFan = _S5ChasComERS4524GT_PWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 114)
)
_S5ChasComERS4524GT_PWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4524GT_PWRUnitFan = _S5ChasComERS4524GT_PWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 114, 1)
)
_S5ChasComERS6628XSGTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS6628XSGTFan = _S5ChasComERS6628XSGTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 115)
)
_S5ChasComERS6628XSGTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS6628XSGTUnitFan = _S5ChasComERS6628XSGTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 115, 1)
)
_S5ChasComERS6632XTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS6632XTSFan = _S5ChasComERS6632XTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 116)
)
_S5ChasComERS6632XTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS6632XTSUnitFan = _S5ChasComERS6632XTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 116, 1)
)
_S5ChasComWC8180Fan_ObjectIdentity = ObjectIdentity
s5ChasComWC8180Fan = _S5ChasComWC8180Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 117)
)
_S5ChasComWC8180UnitFan_ObjectIdentity = ObjectIdentity
s5ChasComWC8180UnitFan = _S5ChasComWC8180UnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 117, 1)
)
_S5ChasComERS4526T_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWR_PLUSFan = _S5ChasComERS4526T_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 118)
)
_S5ChasComERS4526T_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4526T_PWR_PLUSUnitFan = _S5ChasComERS4526T_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 118, 1)
)
_S5ChasComERS4550T_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWR_PLUSFan = _S5ChasComERS4550T_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 119)
)
_S5ChasComERS4550T_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4550T_PWR_PLUSUnitFan = _S5ChasComERS4550T_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 119, 1)
)
_S5ChasComERS4826GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTS_PWR_PLUSFan = _S5ChasComERS4826GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 120)
)
_S5ChasComERS4826GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTS_PWR_PLUSUnitFan = _S5ChasComERS4826GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 120, 1)
)
_S5ChasComERS4850GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTS_PWR_PLUSFan = _S5ChasComERS4850GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 121)
)
_S5ChasComERS4850GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTS_PWR_PLUSUnitFan = _S5ChasComERS4850GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 121, 1)
)
_S5ChasComERS4826GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTSFan = _S5ChasComERS4826GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 122)
)
_S5ChasComERS4826GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4826GTSUnitFan = _S5ChasComERS4826GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 122, 1)
)
_S5ChasComERS4850GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTSFan = _S5ChasComERS4850GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 123)
)
_S5ChasComERS4850GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4850GTSUnitFan = _S5ChasComERS4850GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 123, 1)
)
_S5ChasComVSP7024XLSFan_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XLSFan = _S5ChasComVSP7024XLSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 124)
)
_S5ChasComVSP7024XLSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XLSUnitFan = _S5ChasComVSP7024XLSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 124, 1)
)
_S5ChasComERS3510GTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GTFan = _S5ChasComERS3510GTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 125)
)
_S5ChasComERS3510GTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GTUnitFan = _S5ChasComERS3510GTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 125, 1)
)
_S5ChasComERS3510GT_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GT_PWR_PLUSFan = _S5ChasComERS3510GT_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 126)
)
_S5ChasComERS3510GT_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3510GT_PWR_PLUSUnitFan = _S5ChasComERS3510GT_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 126, 1)
)
_S5ChasComERS3524GTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GTFan = _S5ChasComERS3524GTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 127)
)
_S5ChasComERS3524GTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GTUnitFan = _S5ChasComERS3524GTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 127, 1)
)
_S5ChasComERS3524GT_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GT_PWR_PLUSFan = _S5ChasComERS3524GT_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 128)
)
_S5ChasComERS3524GT_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3524GT_PWR_PLUSUnitFan = _S5ChasComERS3524GT_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 128, 1)
)
_S5ChasComERS3526GTFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GTFan = _S5ChasComERS3526GTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 129)
)
_S5ChasComERS3526GTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GTUnitFan = _S5ChasComERS3526GTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 129, 1)
)
_S5ChasComERS3526GT_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GT_PWR_PLUSFan = _S5ChasComERS3526GT_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 130)
)
_S5ChasComERS3526GT_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526GT_PWR_PLUSUnitFan = _S5ChasComERS3526GT_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 130, 1)
)
_S5ChasComERS3526TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526TFan = _S5ChasComERS3526TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 131)
)
_S5ChasComERS3526TUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526TUnitFan = _S5ChasComERS3526TUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 131, 1)
)
_S5ChasComERS3526T_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526T_PWR_PLUSFan = _S5ChasComERS3526T_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 132)
)
_S5ChasComERS3526T_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3526T_PWR_PLUSUnitFan = _S5ChasComERS3526T_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 132, 1)
)
_S5ChasComERS3549GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTSFan = _S5ChasComERS3549GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 133)
)
_S5ChasComERS3549GTSUnitFan1_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTSUnitFan1 = _S5ChasComERS3549GTSUnitFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 133, 1)
)
_S5ChasComERS3549GTSUnitFan2_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTSUnitFan2 = _S5ChasComERS3549GTSUnitFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 133, 2)
)
_S5ChasComERS3549GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSFan = _S5ChasComERS3549GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 134)
)
_S5ChasComERS3549GTS_PWR_PLUSUnitFan1_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSUnitFan1 = _S5ChasComERS3549GTS_PWR_PLUSUnitFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 134, 1)
)
_S5ChasComERS3549GTS_PWR_PLUSUnitFan2_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSUnitFan2 = _S5ChasComERS3549GTS_PWR_PLUSUnitFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 134, 2)
)
_S5ChasComERS3549GTS_PWR_PLUSUnitFan3_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSUnitFan3 = _S5ChasComERS3549GTS_PWR_PLUSUnitFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 134, 3)
)
_S5ChasComERS3549GTS_PWR_PLUSUnitFan4_ObjectIdentity = ObjectIdentity
s5ChasComERS3549GTS_PWR_PLUSUnitFan4 = _S5ChasComERS3549GTS_PWR_PLUSUnitFan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 134, 4)
)
_S5ChasComVSP7024XTFan_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XTFan = _S5ChasComVSP7024XTFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 135)
)
_S5ChasComVSP7024XTUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComVSP7024XTUnitFan = _S5ChasComVSP7024XTUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 135, 1)
)
_S5ChasComERS5928GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTSFan = _S5ChasComERS5928GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 136)
)
_S5ChasComERS5928GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTSUnitFan = _S5ChasComERS5928GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 136, 1)
)
_S5ChasComERS5928GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_PWR_PLUSFan = _S5ChasComERS5928GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 137)
)
_S5ChasComERS5928GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_PWR_PLUSUnitFan = _S5ChasComERS5928GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 137, 1)
)
_S5ChasComERS5952GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTSFan = _S5ChasComERS5952GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 138)
)
_S5ChasComERS5952GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTSUnitFan = _S5ChasComERS5952GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 138, 1)
)
_S5ChasComERS5952GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTS_PWR_PLUSFan = _S5ChasComERS5952GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 139)
)
_S5ChasComERS5952GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5952GTS_PWR_PLUSUnitFan = _S5ChasComERS5952GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 139, 1)
)
_S5ChasComERS5928GTS_UPWRFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_UPWRFan = _S5ChasComERS5928GTS_UPWRFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 140)
)
_S5ChasComERS5928GTS_UPWRUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS5928GTS_UPWRUnitFan = _S5ChasComERS5928GTS_UPWRUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 140, 1)
)
_S5ChasComERS59100GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTSFan = _S5ChasComERS59100GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 141)
)
_S5ChasComERS59100GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTSUnitFan = _S5ChasComERS59100GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 141, 1)
)
_S5ChasComERS59100GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTS_PWR_PLUSFan = _S5ChasComERS59100GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 142)
)
_S5ChasComERS59100GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS59100GTS_PWR_PLUSUnitFan = _S5ChasComERS59100GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 142, 1)
)
_S5ChasComERS4926GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTSFan = _S5ChasComERS4926GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 143)
)
_S5ChasComERS4926GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTSUnitFan = _S5ChasComERS4926GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 143, 1)
)
_S5ChasComERS4926GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTS_PWR_PLUSFan = _S5ChasComERS4926GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 144)
)
_S5ChasComERS4926GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4926GTS_PWR_PLUSUnitFan = _S5ChasComERS4926GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 144, 1)
)
_S5ChasComERS4950GTSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTSFan = _S5ChasComERS4950GTSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 145)
)
_S5ChasComERS4950GTSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTSUnitFan = _S5ChasComERS4950GTSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 145, 1)
)
_S5ChasComERS4950GTS_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTS_PWR_PLUSFan = _S5ChasComERS4950GTS_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 146)
)
_S5ChasComERS4950GTS_PWR_PLUSUnitFan_ObjectIdentity = ObjectIdentity
s5ChasComERS4950GTS_PWR_PLUSUnitFan = _S5ChasComERS4950GTS_PWR_PLUSUnitFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 146, 1)
)
_S5ChasComERS3550TFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3550TFan = _S5ChasComERS3550TFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 147)
)
_S5ChasComERS3550TUnitFan1_ObjectIdentity = ObjectIdentity
s5ChasComERS3550TUnitFan1 = _S5ChasComERS3550TUnitFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 147, 1)
)
_S5ChasComERS3550TUnitFan2_ObjectIdentity = ObjectIdentity
s5ChasComERS3550TUnitFan2 = _S5ChasComERS3550TUnitFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 147, 2)
)
_S5ChasComERS3550T_PWR_PLUSFan_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSFan = _S5ChasComERS3550T_PWR_PLUSFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 148)
)
_S5ChasComERS3550T_PWR_PLUSUnitFan1_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSUnitFan1 = _S5ChasComERS3550T_PWR_PLUSUnitFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 148, 1)
)
_S5ChasComERS3550T_PWR_PLUSUnitFan2_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSUnitFan2 = _S5ChasComERS3550T_PWR_PLUSUnitFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 148, 2)
)
_S5ChasComERS3550T_PWR_PLUSUnitFan3_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSUnitFan3 = _S5ChasComERS3550T_PWR_PLUSUnitFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 148, 3)
)
_S5ChasComERS3550T_PWR_PLUSUnitFan4_ObjectIdentity = ObjectIdentity
s5ChasComERS3550T_PWR_PLUSUnitFan4 = _S5ChasComERS3550T_PWR_PLUSUnitFan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 10, 148, 4)
)
_S5ChasComMClk_ObjectIdentity = ObjectIdentity
s5ChasComMClk = _S5ChasComMClk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11)
)
_S5ChasComM5000Clk_ObjectIdentity = ObjectIdentity
s5ChasComM5000Clk = _S5ChasComM5000Clk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11, 12)
)
_S5ChasComM5000ClkA_ObjectIdentity = ObjectIdentity
s5ChasComM5000ClkA = _S5ChasComM5000ClkA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11, 12, 1)
)
_S5ChasComM5005Clk_ObjectIdentity = ObjectIdentity
s5ChasComM5005Clk = _S5ChasComM5005Clk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11, 17)
)
_S5ChasComM5005ClkA_ObjectIdentity = ObjectIdentity
s5ChasComM5005ClkA = _S5ChasComM5005ClkA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11, 17, 1)
)
_S5ChasComMAccelar8010Clk_ObjectIdentity = ObjectIdentity
s5ChasComMAccelar8010Clk = _S5ChasComMAccelar8010Clk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 11, 18)
)
_S5ChasStoreTypeReg_ObjectIdentity = ObjectIdentity
s5ChasStoreTypeReg = _S5ChasStoreTypeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 1, 3, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-REG-MIB",
    **{"s5ChasTypeVal": s5ChasTypeVal,
       "s5ChasTypeUnknown": s5ChasTypeUnknown,
       "s5ChasTypeM3000Orig": s5ChasTypeM3000Orig,
       "s5ChasTypeM3030": s5ChasTypeM3030,
       "s5ChasTypeM5000": s5ChasTypeM5000,
       "s5ChasTypeM1032x": s5ChasTypeM1032x,
       "s5ChasTypeM5005": s5ChasTypeM5005,
       "s5ChasType5DN000": s5ChasType5DN000,
       "s5ChasType5DN002Unit-1U2": s5ChasType5DN002Unit_1U2,
       "s5ChasType5DN003Unit-2U3": s5ChasType5DN003Unit_2U3,
       "s5ChasType5DN001-08Unit-2U0": s5ChasType5DN001_08Unit_2U0,
       "s5ChasTypeNBayStack": s5ChasTypeNBayStack,
       "s5ChasTypeNBayStackUnit-12Port": s5ChasTypeNBayStackUnit_12Port,
       "s5ChasTypeNBayStackUnit-24Port": s5ChasTypeNBayStackUnit_24Port,
       "s5ChasTypeBayStack100Hub": s5ChasTypeBayStack100Hub,
       "s5ChasTypeBayStack100Unit-12Port": s5ChasTypeBayStack100Unit_12Port,
       "s5ChasTypeM3000": s5ChasTypeM3000,
       "s5ChasTypeXedia": s5ChasTypeXedia,
       "s5ChasTypeNotUsed": s5ChasTypeNotUsed,
       "s5ChasType28200": s5ChasType28200,
       "s5ChasType28200Unit-4slot": s5ChasType28200Unit_4slot,
       "s5ChasTypeCent-sixSlot": s5ChasTypeCent_sixSlot,
       "s5ChasTypeCent-twelveSlot": s5ChasTypeCent_twelveSlot,
       "s5ChasTypeCent-singleSlot": s5ChasTypeCent_singleSlot,
       "s5ChasTypeBayStack301": s5ChasTypeBayStack301,
       "s5ChasTypeBayStackTr": s5ChasTypeBayStackTr,
       "s5ChasTypeBayStackTrUnit-24-port": s5ChasTypeBayStackTrUnit_24_port,
       "s5ChasTypeFVC10625": s5ChasTypeFVC10625,
       "s5ChasTypeSwitchNode": s5ChasTypeSwitchNode,
       "s5ChasTypeBayStack302": s5ChasTypeBayStack302,
       "s5ChasTypeBayStack302-ethSwitch": s5ChasTypeBayStack302_ethSwitch,
       "s5ChasTypeBayStack350": s5ChasTypeBayStack350,
       "s5ChasTypeBayStack350-ethSwitch": s5ChasTypeBayStack350_ethSwitch,
       "s5ChasTypeBayStack150": s5ChasTypeBayStack150,
       "s5ChasTypeBayStack150MasterUnit-24Port": s5ChasTypeBayStack150MasterUnit_24Port,
       "s5ChasTypeBayStack150MasterUnit-12Port": s5ChasTypeBayStack150MasterUnit_12Port,
       "s5ChasTypeBayStack150SlaveUnit-24Port": s5ChasTypeBayStack150SlaveUnit_24Port,
       "s5ChasTypeBayStack150SlaveUnit-12Port": s5ChasTypeBayStack150SlaveUnit_12Port,
       "s5ChasTypeC50N": s5ChasTypeC50N,
       "s5ChasTypeC50T": s5ChasTypeC50T,
       "s5ChasTypeBayStack303-304": s5ChasTypeBayStack303_304,
       "s5ChasTypeBayStack200": s5ChasTypeBayStack200,
       "s5ChasTypeBayStack200NMMHostUnit-12TxPort": s5ChasTypeBayStack200NMMHostUnit_12TxPort,
       "s5ChasTypeBayStack200NMMHostUnit-12Tx1FxPort": s5ChasTypeBayStack200NMMHostUnit_12Tx1FxPort,
       "s5ChasTypeBayStack200HostUnit-24Port": s5ChasTypeBayStack200HostUnit_24Port,
       "s5ChasTypeBayStack200HostUnit-12Port": s5ChasTypeBayStack200HostUnit_12Port,
       "s5ChasTypeBayStack250": s5ChasTypeBayStack250,
       "s5ChasTypeBayStack250NMMHostUnit-12TxPort": s5ChasTypeBayStack250NMMHostUnit_12TxPort,
       "s5ChasTypeBayStack250HostUnit-24Port": s5ChasTypeBayStack250HostUnit_24Port,
       "s5ChasTypeBayStack250HostUnit-12Port": s5ChasTypeBayStack250HostUnit_12Port,
       "s5ChasTypeBayStack250NMMHostUnit-24Port": s5ChasTypeBayStack250NMMHostUnit_24Port,
       "s5ChasTypeBayStack254HostUnit-12Port": s5ChasTypeBayStack254HostUnit_12Port,
       "s5ChasTypeBayStack255HostUnit-24Port": s5ChasTypeBayStack255HostUnit_24Port,
       "s5ChasTypeStackProbe": s5ChasTypeStackProbe,
       "s5ChasTypeStackProbeOgp": s5ChasTypeStackProbeOgp,
       "s5ChasTypeStackProbeOgpEth": s5ChasTypeStackProbeOgpEth,
       "s5ChasTypeStackProbeOgpEth-1Port": s5ChasTypeStackProbeOgpEth_1Port,
       "s5ChasTypeStackProbeOgpEth-2Port": s5ChasTypeStackProbeOgpEth_2Port,
       "s5ChasTypeStackProbeOgpEth-4Port": s5ChasTypeStackProbeOgpEth_4Port,
       "s5ChasTypeStackProbeOgpTr": s5ChasTypeStackProbeOgpTr,
       "s5ChasTypeStackProbeOgpTr-1Port": s5ChasTypeStackProbeOgpTr_1Port,
       "s5ChasTypeStackProbeOgpTr-2Port": s5ChasTypeStackProbeOgpTr_2Port,
       "s5ChasTypeStackProbeOgpFddi": s5ChasTypeStackProbeOgpFddi,
       "s5ChasTypeStackProbeOgpFddiSas": s5ChasTypeStackProbeOgpFddiSas,
       "s5ChasTypeStackProbeOgpFddiDas": s5ChasTypeStackProbeOgpFddiDas,
       "s5ChasTypeStackProbeOgpFeth": s5ChasTypeStackProbeOgpFeth,
       "s5ChasTypeStackProbeOgpFeth-1Port": s5ChasTypeStackProbeOgpFeth_1Port,
       "s5ChasTypeStackProbeOgpFeth-2Port": s5ChasTypeStackProbeOgpFeth_2Port,
       "s5ChasTypeStackProbe1000": s5ChasTypeStackProbe1000,
       "s5ChasTypeStackProbe1000Eth": s5ChasTypeStackProbe1000Eth,
       "s5ChasTypeStackProbe1000Eth-1Port": s5ChasTypeStackProbe1000Eth_1Port,
       "s5ChasTypeStackProbe1000Feth": s5ChasTypeStackProbe1000Feth,
       "s5ChasTypeStackProbe1000Feth-1Port": s5ChasTypeStackProbe1000Feth_1Port,
       "s5ChasTypeStackProbe2000": s5ChasTypeStackProbe2000,
       "s5ChasTypeStackProbe2000Eth": s5ChasTypeStackProbe2000Eth,
       "s5ChasTypeStackProbe2000Eth-1Port": s5ChasTypeStackProbe2000Eth_1Port,
       "s5ChasTypeStackProbe2000Eth-2Port": s5ChasTypeStackProbe2000Eth_2Port,
       "s5ChasTypeStackProbe2000Eth-4Port": s5ChasTypeStackProbe2000Eth_4Port,
       "s5ChasTypeStackProbe2000Fddi": s5ChasTypeStackProbe2000Fddi,
       "s5ChasTypeStackProbe2000FddiSas": s5ChasTypeStackProbe2000FddiSas,
       "s5ChasTypeStackProbe2000FddiDas": s5ChasTypeStackProbe2000FddiDas,
       "s5ChasTypeStackProbe3000": s5ChasTypeStackProbe3000,
       "s5ChasTypeStackProbe3000Geth": s5ChasTypeStackProbe3000Geth,
       "s5ChasTypeStackProbe3000Geth-1Port": s5ChasTypeStackProbe3000Geth_1Port,
       "s5ChasTypeBayStack450": s5ChasTypeBayStack450,
       "s5ChasTypeBayStack450-12TxPort": s5ChasTypeBayStack450_12TxPort,
       "s5ChasTypeBayStack450-24TxPort": s5ChasTypeBayStack450_24TxPort,
       "s5ChasTypeBayStack303-24T": s5ChasTypeBayStack303_24T,
       "s5ChasTypeAccelar8010": s5ChasTypeAccelar8010,
       "s5ChasTypeAccelar8006": s5ChasTypeAccelar8006,
       "s5ChasTypeBayStack670": s5ChasTypeBayStack670,
       "s5ChasTypeBPS2000": s5ChasTypeBPS2000,
       "s5ChasTypeBPS2000-24TxPort": s5ChasTypeBPS2000_24TxPort,
       "s5ChasTypeBayStack3580": s5ChasTypeBayStack3580,
       "s5ChasTypeBayStack3580-16F": s5ChasTypeBayStack3580_16F,
       "s5ChasTypeBayStack420": s5ChasTypeBayStack420,
       "s5ChasTypeBayStack420-24TxPort": s5ChasTypeBayStack420_24TxPort,
       "s5ChasTypeMetro1200ESM": s5ChasTypeMetro1200ESM,
       "s5ChasTypeMetro1200ESM-12TxPort": s5ChasTypeMetro1200ESM_12TxPort,
       "s5ChasTypeBayStack380": s5ChasTypeBayStack380,
       "s5ChasTypeBayStack380-24TxPort": s5ChasTypeBayStack380_24TxPort,
       "s5ChasTypeBayStack470": s5ChasTypeBayStack470,
       "s5ChasTypeBayStack470-48TxPort": s5ChasTypeBayStack470_48TxPort,
       "s5ChasTypeMetro1450ESM": s5ChasTypeMetro1450ESM,
       "s5ChasTypeMetro1450ESM-12TxPort2Gbic": s5ChasTypeMetro1450ESM_12TxPort2Gbic,
       "s5ChasTypeMetro1400ESM": s5ChasTypeMetro1400ESM,
       "s5ChasTypeMetro1400ESM-12TxPort2Gbic": s5ChasTypeMetro1400ESM_12TxPort2Gbic,
       "s5ChasTypeBayStack460-24T-PWR": s5ChasTypeBayStack460_24T_PWR,
       "s5ChasTypeBayStack460-24T-PWR-24TxPort": s5ChasTypeBayStack460_24T_PWR_24TxPort,
       "s5ChasTypeBayStack10": s5ChasTypeBayStack10,
       "s5ChasTypeBayStack10-powerSupplyUnit": s5ChasTypeBayStack10_powerSupplyUnit,
       "s5ChasTypeBayStack380-24F": s5ChasTypeBayStack380_24F,
       "s5ChasTypeBayStack380-24F-20MiniGbic4Gbic": s5ChasTypeBayStack380_24F_20MiniGbic4Gbic,
       "s5ChasTypeBayStack5510-24T": s5ChasTypeBayStack5510_24T,
       "s5ChasTypeBayStack5510-24T-24TxPort": s5ChasTypeBayStack5510_24T_24TxPort,
       "s5ChasTypeBayStack5510-48T": s5ChasTypeBayStack5510_48T,
       "s5ChasTypeBayStack5510-48T-48TxPort": s5ChasTypeBayStack5510_48T_48TxPort,
       "s5ChasTypeBayStack470-24T": s5ChasTypeBayStack470_24T,
       "s5ChasTypeBayStack470-24TxPort": s5ChasTypeBayStack470_24TxPort,
       "s5ChasTypeWLANAccessPoint2220": s5ChasTypeWLANAccessPoint2220,
       "s5ChasTypeWLANAccessPoint2220-wirelessAP": s5ChasTypeWLANAccessPoint2220_wirelessAP,
       "s5ChasTypeWLANSecuritySwitch2250": s5ChasTypeWLANSecuritySwitch2250,
       "s5ChasTypeWLANSecuritySwitch2250-securitySwitch": s5ChasTypeWLANSecuritySwitch2250_securitySwitch,
       "s5ChasTypeBayStack425": s5ChasTypeBayStack425,
       "s5ChasTypeBayStack425-24": s5ChasTypeBayStack425_24,
       "s5ChasTypeBayStack425-48": s5ChasTypeBayStack425_48,
       "s5ChasTypeWLANAccessPoint2221": s5ChasTypeWLANAccessPoint2221,
       "s5ChasTypeWLANAccessPoint2221-wirelessAP": s5ChasTypeWLANAccessPoint2221_wirelessAP,
       "s5ChasTypeBayStack5520": s5ChasTypeBayStack5520,
       "s5ChasTypeBayStack5520-24T-PWR-24TxPort": s5ChasTypeBayStack5520_24T_PWR_24TxPort,
       "s5ChasTypeBayStack5520-48T-PWR-48TxPort": s5ChasTypeBayStack5520_48T_PWR_48TxPort,
       "s5ChasTypeBayStack325": s5ChasTypeBayStack325,
       "s5ChasTypeBayStack325-24T": s5ChasTypeBayStack325_24T,
       "s5ChasTypeBayStack325-24G": s5ChasTypeBayStack325_24G,
       "s5ChasTypeWLANAccessPoint2225": s5ChasTypeWLANAccessPoint2225,
       "s5ChasTypeWLANAccessPoint2225-wirelessAP": s5ChasTypeWLANAccessPoint2225_wirelessAP,
       "s5ChasTypeBayStack470-24T-PWR": s5ChasTypeBayStack470_24T_PWR,
       "s5ChasTypeBayStack470-24TxPort-PWR": s5ChasTypeBayStack470_24TxPort_PWR,
       "s5ChasTypeBayStack470-48T-PWR": s5ChasTypeBayStack470_48T_PWR,
       "s5ChasTypeBayStack470-48TxPort-PWR": s5ChasTypeBayStack470_48TxPort_PWR,
       "s5ChasTypeWLANSecuritySwitch2270": s5ChasTypeWLANSecuritySwitch2270,
       "s5ChasTypeWLANSecuritySwitch2270-securitySwitch": s5ChasTypeWLANSecuritySwitch2270_securitySwitch,
       "s5ChasTypeEthernetRoutingSwitch5530": s5ChasTypeEthernetRoutingSwitch5530,
       "s5ChasTypeEthernetRoutingSwitch5530-24TFD": s5ChasTypeEthernetRoutingSwitch5530_24TFD,
       "s5ChasTypeEthernetSwitch3510": s5ChasTypeEthernetSwitch3510,
       "s5ChasTypeEthernetSwitch3510-24T": s5ChasTypeEthernetSwitch3510_24T,
       "s5ChasTypeBES1010": s5ChasTypeBES1010,
       "s5ChasTypeBES1010-24T": s5ChasTypeBES1010_24T,
       "s5ChasTypeBES1010-48T": s5ChasTypeBES1010_48T,
       "s5ChasTypeBES1020": s5ChasTypeBES1020,
       "s5ChasTypeBES1020-24T-PWR": s5ChasTypeBES1020_24T_PWR,
       "s5ChasTypeBES1020-48T-PWR": s5ChasTypeBES1020_48T_PWR,
       "s5ChasTypeBES2010": s5ChasTypeBES2010,
       "s5ChasTypeBES2010-24T": s5ChasTypeBES2010_24T,
       "s5ChasTypeBES2010-48T": s5ChasTypeBES2010_48T,
       "s5ChasTypeBES2020": s5ChasTypeBES2020,
       "s5ChasTypeBES2020-24T-PWR": s5ChasTypeBES2020_24T_PWR,
       "s5ChasTypeBES2020-48T-PWR": s5ChasTypeBES2020_48T_PWR,
       "s5ChasTypeBES110": s5ChasTypeBES110,
       "s5ChasTypeBES110-24T": s5ChasTypeBES110_24T,
       "s5ChasTypeBES110-48T": s5ChasTypeBES110_48T,
       "s5ChasTypeBES120": s5ChasTypeBES120,
       "s5ChasTypeBES120-24T-PWR": s5ChasTypeBES120_24T_PWR,
       "s5ChasTypeBES120-48T-PWR": s5ChasTypeBES120_48T_PWR,
       "s5ChasTypeBES210": s5ChasTypeBES210,
       "s5ChasTypeBES210-24T": s5ChasTypeBES210_24T,
       "s5ChasTypeBES210-48T": s5ChasTypeBES210_48T,
       "s5ChasTypeBES220": s5ChasTypeBES220,
       "s5ChasTypeBES220-24T-PWR": s5ChasTypeBES220_24T_PWR,
       "s5ChasTypeBES220-48T-PWR": s5ChasTypeBES220_48T_PWR,
       "s5ChasTypeERS45xx": s5ChasTypeERS45xx,
       "s5ChasTypeERS4548GT": s5ChasTypeERS4548GT,
       "s5ChasTypeERS4548GT-PWR": s5ChasTypeERS4548GT_PWR,
       "s5ChasTypeERS4550T": s5ChasTypeERS4550T,
       "s5ChasTypeERS4550T-PWR": s5ChasTypeERS4550T_PWR,
       "s5ChasTypeERS4526FX": s5ChasTypeERS4526FX,
       "s5ChasTypeERS4526GTX-PWR": s5ChasTypeERS4526GTX_PWR,
       "s5ChasTypeERS4526GTX": s5ChasTypeERS4526GTX,
       "s5ChasTypeERS4524GT": s5ChasTypeERS4524GT,
       "s5ChasTypeERS4526T-PWR": s5ChasTypeERS4526T_PWR,
       "s5ChasTypeERS4526T": s5ChasTypeERS4526T,
       "s5ChasTypeERS4524GT-PWR": s5ChasTypeERS4524GT_PWR,
       "s5ChasTypeERS4526T-PWR-PLUS": s5ChasTypeERS4526T_PWR_PLUS,
       "s5ChasTypeERS4550T-PWR-PLUS": s5ChasTypeERS4550T_PWR_PLUS,
       "s5ChasTypeERS25xx": s5ChasTypeERS25xx,
       "s5ChasTypeERS2500-26T": s5ChasTypeERS2500_26T,
       "s5ChasTypeERS2500-26T-PWR": s5ChasTypeERS2500_26T_PWR,
       "s5ChasTypeERS2500-50T": s5ChasTypeERS2500_50T,
       "s5ChasTypeERS2500-50T-PWR": s5ChasTypeERS2500_50T_PWR,
       "s5ChasTypeERS56xx": s5ChasTypeERS56xx,
       "s5ChasTypeERS5698-TFD-PWR": s5ChasTypeERS5698_TFD_PWR,
       "s5ChasTypeERS5698-TFD": s5ChasTypeERS5698_TFD,
       "s5ChasTypeERS5650-TD-PWR": s5ChasTypeERS5650_TD_PWR,
       "s5ChasTypeERS5650-TD": s5ChasTypeERS5650_TD,
       "s5ChasTypeERS5632-FD": s5ChasTypeERS5632_FD,
       "s5ChasTypeESU1860": s5ChasTypeESU1860,
       "s5ChasTypeESU1860S": s5ChasTypeESU1860S,
       "s5ChasTypeESU1860B": s5ChasTypeESU1860B,
       "s5ChasTypeESU1860T": s5ChasTypeESU1860T,
       "s5ChasTypeESU1860V": s5ChasTypeESU1860V,
       "s5ChasTypeESU1880": s5ChasTypeESU1880,
       "s5ChasTypeESU1880S": s5ChasTypeESU1880S,
       "s5ChasTypeERS66xx": s5ChasTypeERS66xx,
       "s5ChasTypeERS642-XSGT": s5ChasTypeERS642_XSGT,
       "s5ChasTypeERS6632-XTS": s5ChasTypeERS6632_XTS,
       "s5ChasTypeWC8xxx": s5ChasTypeWC8xxx,
       "s5ChasTypeWC8180": s5ChasTypeWC8180,
       "s5ChasTypeERS48xx": s5ChasTypeERS48xx,
       "s5ChasTypeERS4826GTS-PWR-PLUS": s5ChasTypeERS4826GTS_PWR_PLUS,
       "s5ChasTypeERS4850GTS-PWR-PLUS": s5ChasTypeERS4850GTS_PWR_PLUS,
       "s5ChasTypeERS4826GTS": s5ChasTypeERS4826GTS,
       "s5ChasTypeERS4850GTS": s5ChasTypeERS4850GTS,
       "s5ChasTypeVSP7xxx": s5ChasTypeVSP7xxx,
       "s5ChasTypeVSP7024XLS": s5ChasTypeVSP7024XLS,
       "s5ChasTypeERS35xx": s5ChasTypeERS35xx,
       "s5ChasTypeERS3510GT": s5ChasTypeERS3510GT,
       "s5ChasTypeERS3510GT-PWR-PLUS": s5ChasTypeERS3510GT_PWR_PLUS,
       "s5ChasTypeERS3524GT": s5ChasTypeERS3524GT,
       "s5ChasTypeERS3524GT-PWR-PLUS": s5ChasTypeERS3524GT_PWR_PLUS,
       "s5ChasTypeERS3526GT": s5ChasTypeERS3526GT,
       "s5ChasTypeERS3526GT-PWR-PLUS": s5ChasTypeERS3526GT_PWR_PLUS,
       "s5ChasTypeERS3526T": s5ChasTypeERS3526T,
       "s5ChasTypeERS3526T-PWR-PLUS": s5ChasTypeERS3526T_PWR_PLUS,
       "s5ChasTypeERS3549GTS": s5ChasTypeERS3549GTS,
       "s5ChasTypeERS3549GTS-PWR-PLUS": s5ChasTypeERS3549GTS_PWR_PLUS,
       "s5ChasTypeERS3550T": s5ChasTypeERS3550T,
       "s5ChasTypeERS3550T-PWR-PLUS": s5ChasTypeERS3550T_PWR_PLUS,
       "s5ChasTypeERS59xx": s5ChasTypeERS59xx,
       "s5ChasTypeERS5928GTS": s5ChasTypeERS5928GTS,
       "s5ChasTypeERS5928GTS-PWR-PLUS": s5ChasTypeERS5928GTS_PWR_PLUS,
       "s5ChasTypeERS5952GTS": s5ChasTypeERS5952GTS,
       "s5ChasTypeERS5952GTS-PWR-PLUS": s5ChasTypeERS5952GTS_PWR_PLUS,
       "s5ChasTypeERS5928GTS-UPWR": s5ChasTypeERS5928GTS_UPWR,
       "s5ChasTypeERS59100GTS": s5ChasTypeERS59100GTS,
       "s5ChasTypeERS59100GTS-PWR-PLUS": s5ChasTypeERS59100GTS_PWR_PLUS,
       "s5ChasTypeERS49xx": s5ChasTypeERS49xx,
       "s5ChasTypeERS4926GTS": s5ChasTypeERS4926GTS,
       "s5ChasTypeERS4926GTS-PWR-PLUS": s5ChasTypeERS4926GTS_PWR_PLUS,
       "s5ChasTypeERS4950GTS": s5ChasTypeERS4950GTS,
       "s5ChasTypeERS4950GTS-PWR-PLUS": s5ChasTypeERS4950GTS_PWR_PLUS,
       "s5ChasGrpTypeVal": s5ChasGrpTypeVal,
       "s5ChasGrpSup": s5ChasGrpSup,
       "s5ChasGrpBkpl": s5ChasGrpBkpl,
       "s5ChasGrpBrd": s5ChasGrpBrd,
       "s5ChasGrpPwr": s5ChasGrpPwr,
       "s5ChasGrpTmpSnr": s5ChasGrpTmpSnr,
       "s5ChasGrpFan": s5ChasGrpFan,
       "s5ChasGrpClk": s5ChasGrpClk,
       "s5ChasGrpUnit": s5ChasGrpUnit,
       "s5ChasComTypeVal": s5ChasComTypeVal,
       "s5ChasComBkpl": s5ChasComBkpl,
       "s5ChasComBkplM5000low": s5ChasComBkplM5000low,
       "s5ChasComBkplM5000lowCmbEthTok": s5ChasComBkplM5000lowCmbEthTok,
       "s5ChasComBkplM5000lowCmbEth": s5ChasComBkplM5000lowCmbEth,
       "s5ChasComBkplM5000midLeft": s5ChasComBkplM5000midLeft,
       "s5ChasComBkplM5000midLeftFddiFull": s5ChasComBkplM5000midLeftFddiFull,
       "s5ChasComBkplM5000midRight": s5ChasComBkplM5000midRight,
       "s5ChasComBkplM5000midRightFddi": s5ChasComBkplM5000midRightFddi,
       "s5ChasComBkplM5000highLeft": s5ChasComBkplM5000highLeft,
       "s5ChasComBkplM5000highRight": s5ChasComBkplM5000highRight,
       "s5ChasComBkplCentATM": s5ChasComBkplCentATM,
       "s5ChasComBkpl2x65000BH": s5ChasComBkpl2x65000BH,
       "s5ChasComBkpl1x125000BH": s5ChasComBkpl1x125000BH,
       "s5ChasComBkplC50": s5ChasComBkplC50,
       "s5ChasComPwr": s5ChasComPwr,
       "s5ChasComPwrM5000-950A": s5ChasComPwrM5000_950A,
       "s5ChasComPwrM5000-950AFan": s5ChasComPwrM5000_950AFan,
       "s5ChasComPwrM5000-950ATmpSnr": s5ChasComPwrM5000_950ATmpSnr,
       "s5ChasComPwrM5000-950": s5ChasComPwrM5000_950,
       "s5ChasComPwrM5000-950Fan": s5ChasComPwrM5000_950Fan,
       "s5ChasComPwrM5000-950TmpSnr": s5ChasComPwrM5000_950TmpSnr,
       "s5ChasComPwrCent": s5ChasComPwrCent,
       "s5ChasComPwrCent50N": s5ChasComPwrCent50N,
       "s5ChasComPwrCent50T": s5ChasComPwrCent50T,
       "s5ChasComTmpSnr": s5ChasComTmpSnr,
       "s5ChasComTmpSnrM5000": s5ChasComTmpSnrM5000,
       "s5ChasComTmpSnrMetro1200ESM": s5ChasComTmpSnrMetro1200ESM,
       "s5ChasComTmpSnrMetro1450ESM": s5ChasComTmpSnrMetro1450ESM,
       "s5ChasComTmpSnrMetro1400ESM": s5ChasComTmpSnrMetro1400ESM,
       "s5ChasComTmpSnrBayStack460-24T-PWR": s5ChasComTmpSnrBayStack460_24T_PWR,
       "s5ChasComTmpSnrBayStack5510-24T": s5ChasComTmpSnrBayStack5510_24T,
       "s5ChasComTmpSnrBayStack5510-48T": s5ChasComTmpSnrBayStack5510_48T,
       "s5ChasComTmpSnrBayStack425": s5ChasComTmpSnrBayStack425,
       "s5ChasComTmpSnrBayStack5520-24T-PWR": s5ChasComTmpSnrBayStack5520_24T_PWR,
       "s5ChasComTmpSnrBayStack5520-48T-PWR": s5ChasComTmpSnrBayStack5520_48T_PWR,
       "s5ChasComTmpSnrBayStack325": s5ChasComTmpSnrBayStack325,
       "s5ChasComFan": s5ChasComFan,
       "s5ChasComFanM5000": s5ChasComFanM5000,
       "s5ChasComFanCent": s5ChasComFanCent,
       "s5ChasComCent50NFan": s5ChasComCent50NFan,
       "s5ChasComCent50TFan": s5ChasComCent50TFan,
       "s5ChasComClk": s5ChasComClk,
       "s5ChasComClkM5000": s5ChasComClkM5000,
       "s5ChasComMod": s5ChasComMod,
       "s5ChasComM331X": s5ChasComM331X,
       "s5ChasComMDA331X": s5ChasComMDA331X,
       "s5ChasComM3302": s5ChasComM3302,
       "s5ChasComMDA3302": s5ChasComMDA3302,
       "s5ChasComM33XX": s5ChasComM33XX,
       "s5ChasComMDA3324-ST": s5ChasComMDA3324_ST,
       "s5ChasComMDA3323": s5ChasComMDA3323,
       "s5ChasComM3304": s5ChasComM3304,
       "s5ChasComMDA3304": s5ChasComMDA3304,
       "s5ChasComM3305": s5ChasComM3305,
       "s5ChasComMDA3305": s5ChasComMDA3305,
       "s5ChasComM333X": s5ChasComM333X,
       "s5ChasComMDA3334-ST": s5ChasComMDA3334_ST,
       "s5ChasComMDA3333": s5ChasComMDA3333,
       "s5ChasComM3307": s5ChasComM3307,
       "s5ChasComMDA3307": s5ChasComMDA3307,
       "s5ChasComM3308": s5ChasComM3308,
       "s5ChasComMDA3308": s5ChasComMDA3308,
       "s5ChasComM3301": s5ChasComM3301,
       "s5ChasComMDA3301": s5ChasComMDA3301,
       "s5ChasComM3904": s5ChasComM3904,
       "s5ChasComMDA3904": s5ChasComMDA3904,
       "s5ChasComMDA3904-2SM": s5ChasComMDA3904_2SM,
       "s5ChasComMDA3904-4SM": s5ChasComMDA3904_4SM,
       "s5ChasComM3902": s5ChasComM3902,
       "s5ChasComMDA3902": s5ChasComMDA3902,
       "s5ChasComM3910S": s5ChasComM3910S,
       "s5ChasComMDA3910S": s5ChasComMDA3910S,
       "s5ChasComMDA3910S-SM": s5ChasComMDA3910S_SM,
       "s5ChasComM331XS": s5ChasComM331XS,
       "s5ChasComMDA3314S": s5ChasComMDA3314S,
       "s5ChasComMDA3313S": s5ChasComMDA3313S,
       "s5ChasComM3100R": s5ChasComM3100R,
       "s5ChasComMDA3100R": s5ChasComMDA3100R,
       "s5ChasComM3502": s5ChasComM3502,
       "s5ChasComMDA3502": s5ChasComMDA3502,
       "s5ChasComM3502A": s5ChasComM3502A,
       "s5ChasComMDA3502A": s5ChasComMDA3502A,
       "s5ChasComM353X": s5ChasComM353X,
       "s5ChasComMDA3532": s5ChasComMDA3532,
       "s5ChasComMDA3534": s5ChasComMDA3534,
       "s5ChasComM3040": s5ChasComM3040,
       "s5ChasComMDA3040": s5ChasComMDA3040,
       "s5ChasComM3505": s5ChasComM3505,
       "s5ChasComMDA3505": s5ChasComMDA3505,
       "s5ChasComM3505A": s5ChasComM3505A,
       "s5ChasComMDA3505A": s5ChasComMDA3505A,
       "s5ChasComM355X": s5ChasComM355X,
       "s5ChasComMDA3552": s5ChasComMDA3552,
       "s5ChasComMDA3554": s5ChasComMDA3554,
       "s5ChasComM3040S": s5ChasComM3040S,
       "s5ChasComMDA3040S": s5ChasComMDA3040S,
       "s5ChasComM351X": s5ChasComM351X,
       "s5ChasComMDA3512": s5ChasComMDA3512,
       "s5ChasComMDA3513": s5ChasComMDA3513,
       "s5ChasComMDA3514": s5ChasComMDA3514,
       "s5ChasComM33XXS": s5ChasComM33XXS,
       "s5ChasComMDA3324S": s5ChasComMDA3324S,
       "s5ChasComMDA3323S": s5ChasComMDA3323S,
       "s5ChasComM338X": s5ChasComM338X,
       "s5ChasComMDA3384": s5ChasComMDA3384,
       "s5ChasComMDA3383": s5ChasComMDA3383,
       "s5ChasComMDA3386": s5ChasComMDA3386,
       "s5ChasComM3328": s5ChasComM3328,
       "s5ChasComMDA3328": s5ChasComMDA3328,
       "s5ChasComM3395": s5ChasComM3395,
       "s5ChasComMDA3395": s5ChasComMDA3395,
       "s5ChasComM3394": s5ChasComM3394,
       "s5ChasComMDA3394": s5ChasComMDA3394,
       "s5ChasComM3522": s5ChasComM3522,
       "s5ChasComMDA3522": s5ChasComMDA3522,
       "s5ChasComM3395A": s5ChasComM3395A,
       "s5ChasComMDA3395A": s5ChasComMDA3395A,
       "s5ChasComM3800": s5ChasComM3800,
       "s5ChasComMDA3803": s5ChasComMDA3803,
       "s5ChasComMDA3805": s5ChasComMDA3805,
       "s5ChasComMDA3809": s5ChasComMDA3809,
       "s5ChasComMDA3806": s5ChasComMDA3806,
       "s5ChasComMDA3800": s5ChasComMDA3800,
       "s5ChasComM3368": s5ChasComM3368,
       "s5ChasComMDA3368": s5ChasComMDA3368,
       "s5ChasComM3307A": s5ChasComM3307A,
       "s5ChasComMDA3307A": s5ChasComMDA3307A,
       "s5ChasComM3308A": s5ChasComM3308A,
       "s5ChasComMDA3308A": s5ChasComMDA3308A,
       "s5ChasComM3301-75": s5ChasComM3301_75,
       "s5ChasComMDA3301-75": s5ChasComMDA3301_75,
       "s5ChasComM3301-93": s5ChasComM3301_93,
       "s5ChasComMDA3301-93": s5ChasComMDA3301_93,
       "s5ChasComM3502B": s5ChasComM3502B,
       "s5ChasComMDA3502B": s5ChasComMDA3502B,
       "s5ChasComM3505B": s5ChasComM3505B,
       "s5ChasComMDA3505B": s5ChasComMDA3505B,
       "s5ChasComM3307HD": s5ChasComM3307HD,
       "s5ChasComMDA3307HD": s5ChasComMDA3307HD,
       "s5ChasComM3356": s5ChasComM3356,
       "s5ChasSubComMDA3356X21": s5ChasSubComMDA3356X21,
       "s5ChasSubComMDA3356X21U": s5ChasSubComMDA3356X21U,
       "s5ChasSubComMDA3356RS232": s5ChasSubComMDA3356RS232,
       "s5ChasSubComMDA3356RS449": s5ChasSubComMDA3356RS449,
       "s5ChasSubComMDA3356V35": s5ChasSubComMDA3356V35,
       "s5ChasSubComMDA3356G703": s5ChasSubComMDA3356G703,
       "s5ChasSubComMDA3356T1": s5ChasSubComMDA3356T1,
       "s5ChasSubComMDA3356": s5ChasSubComMDA3356,
       "s5ChasComM3902A": s5ChasComM3902A,
       "s5ChasComMDA3902A": s5ChasComMDA3902A,
       "s5ChasComM3910S-SD": s5ChasComM3910S_SD,
       "s5ChasComMDA3910S-SD": s5ChasComMDA3910S_SD,
       "s5ChasComM3313A": s5ChasComM3313A,
       "s5ChasComMDA3313A": s5ChasComMDA3313A,
       "s5ChasComM3314A": s5ChasComM3314A,
       "s5ChasComMDA3314A": s5ChasComMDA3314A,
       "s5ChasComM3304A": s5ChasComM3304A,
       "s5ChasComMDA3304A": s5ChasComMDA3304A,
       "s5ChasComM3910SA": s5ChasComM3910SA,
       "s5ChasComMDA3910SA": s5ChasComMDA3910SA,
       "s5ChasComMDA3910SA-SM": s5ChasComMDA3910SA_SM,
       "s5ChasComM3905": s5ChasComM3905,
       "s5ChasComMDA3905": s5ChasComMDA3905,
       "s5ChasComM3486": s5ChasComM3486,
       "s5ChasComMDA3486": s5ChasComMDA3486,
       "s5ChasComM3504-ST": s5ChasComM3504_ST,
       "s5ChasComMDA3504-ST": s5ChasComMDA3504_ST,
       "s5ChasComM3517SA": s5ChasComM3517SA,
       "s5ChasComMDA3517SA": s5ChasComMDA3517SA,
       "s5ChasComM3308B": s5ChasComM3308B,
       "s5ChasComMDA3308B": s5ChasComMDA3308B,
       "s5ChasComM3313SA": s5ChasComM3313SA,
       "s5ChasComMDA3313SA": s5ChasComMDA3313SA,
       "s5ChasComM3314SA": s5ChasComM3314SA,
       "s5ChasComMDA3314SA": s5ChasComMDA3314SA,
       "s5ChasComM3174": s5ChasComM3174,
       "s5ChasComMDA3174": s5ChasComMDA3174,
       "s5ChasComM3522A": s5ChasComM3522A,
       "s5ChasComMDA3522A": s5ChasComMDA3522A,
       "s5ChasComM3299-C": s5ChasComM3299_C,
       "s5ChasComMDA3299-C": s5ChasComMDA3299_C,
       "s5ChasComM3299-U": s5ChasComM3299_U,
       "s5ChasComMDA3299-U": s5ChasComMDA3299_U,
       "s5ChasComM3299-F": s5ChasComM3299_F,
       "s5ChasComMDA3299-F": s5ChasComMDA3299_F,
       "s5ChasComM3410": s5ChasComM3410,
       "s5ChasComM3410Store": s5ChasComM3410Store,
       "s5ChasComM3410StoreBoot": s5ChasComM3410StoreBoot,
       "s5ChasComM3410StoreFlash": s5ChasComM3410StoreFlash,
       "s5ChasComM3410StoreDram": s5ChasComM3410StoreDram,
       "s5ChasComM3405Tx12": s5ChasComM3405Tx12,
       "s5ChasComM3405Tx12Store": s5ChasComM3405Tx12Store,
       "s5ChasComM3405Tx12StoreRom": s5ChasComM3405Tx12StoreRom,
       "s5ChasComM3475FxTx11": s5ChasComM3475FxTx11,
       "s5ChasComM3475FxTx11Store": s5ChasComM3475FxTx11Store,
       "s5ChasComM3475FxTx11StoreRom": s5ChasComM3475FxTx11StoreRom,
       "s5ChasComM3308S": s5ChasComM3308S,
       "s5ChasComM3308SStore": s5ChasComM3308SStore,
       "s5ChasComM3308SStoreDram": s5ChasComM3308SStoreDram,
       "s5ChasComM3308SStoreFlash1": s5ChasComM3308SStoreFlash1,
       "s5ChasComM3308SStoreFlash2": s5ChasComM3308SStoreFlash2,
       "s5ChasComM3308SStoreFlash3": s5ChasComM3308SStoreFlash3,
       "s5ChasComM3308SStoreFlash4": s5ChasComM3308SStoreFlash4,
       "s5ChasComM3000ASM": s5ChasComM3000ASM,
       "s5ChasComMDA3000ASM": s5ChasComMDA3000ASM,
       "s5ChasComSupM5110": s5ChasComSupM5110,
       "s5ChasComSupM5110Store": s5ChasComSupM5110Store,
       "s5ChasComSupM5110StoreDram": s5ChasComSupM5110StoreDram,
       "s5ChasComSupM5110StoreFlash": s5ChasComSupM5110StoreFlash,
       "s5ChasComSupM5110StoreNvram": s5ChasComSupM5110StoreNvram,
       "s5ChasComSupM5110StoreChaEeProm": s5ChasComSupM5110StoreChaEeProm,
       "s5ChasComBrdM5304P": s5ChasComBrdM5304P,
       "s5ChasComBrdM5304PStore": s5ChasComBrdM5304PStore,
       "s5ChasComBrdM5304PStore8051Rom": s5ChasComBrdM5304PStore8051Rom,
       "s5ChasComBrdM5304PStoreDspRom": s5ChasComBrdM5304PStoreDspRom,
       "s5ChasComBrdM5308": s5ChasComBrdM5308,
       "s5ChasComBrdM5308Store": s5ChasComBrdM5308Store,
       "s5ChasComBrdM5308Store8051Rom": s5ChasComBrdM5308Store8051Rom,
       "s5ChasComBrdM5308StoreDspRom": s5ChasComBrdM5308StoreDspRom,
       "s5ChasComBrdM5308AF": s5ChasComBrdM5308AF,
       "s5ChasComBrdM5308AFStore": s5ChasComBrdM5308AFStore,
       "s5ChasComBrdM5308AFStore8051Rom": s5ChasComBrdM5308AFStore8051Rom,
       "s5ChasComBrdM5308AFStoreDspRom": s5ChasComBrdM5308AFStoreDspRom,
       "s5ChasComBrdM5378F": s5ChasComBrdM5378F,
       "s5ChasComBrdM5378FStore": s5ChasComBrdM5378FStore,
       "s5ChasComBrdM5378FStore8051Rom": s5ChasComBrdM5378FStore8051Rom,
       "s5ChasComBrdM5378FStoreDspRom": s5ChasComBrdM5378FStoreDspRom,
       "s5ChasComBrdM5502": s5ChasComBrdM5502,
       "s5ChasComBrdM5502Store": s5ChasComBrdM5502Store,
       "s5ChasComBrdM5502Store8051Rom": s5ChasComBrdM5502Store8051Rom,
       "s5ChasComBrdM5505P": s5ChasComBrdM5505P,
       "s5ChasComBrdM5505PStore": s5ChasComBrdM5505PStore,
       "s5ChasComBrdM5505PStore8051Rom": s5ChasComBrdM5505PStore8051Rom,
       "s5ChasComBrdM5575F": s5ChasComBrdM5575F,
       "s5ChasComBrdM5575FStore": s5ChasComBrdM5575FStore,
       "s5ChasComBrdM5575FStore8051Rom": s5ChasComBrdM5575FStore8051Rom,
       "s5ChasComBrdM5902": s5ChasComBrdM5902,
       "s5ChasComBrdM5902Store": s5ChasComBrdM5902Store,
       "s5ChasComBrdM5902StoreDram": s5ChasComBrdM5902StoreDram,
       "s5ChasComBrdM5902StoreFlash": s5ChasComBrdM5902StoreFlash,
       "s5ChasComBrdM5902StoreNvram": s5ChasComBrdM5902StoreNvram,
       "s5ChasComBrdM5904": s5ChasComBrdM5904,
       "s5ChasComBrdM5904Store": s5ChasComBrdM5904Store,
       "s5ChasComBrdM5904StoreDram": s5ChasComBrdM5904StoreDram,
       "s5ChasComBrdM5904StoreFlash": s5ChasComBrdM5904StoreFlash,
       "s5ChasComBrdM5904StoreNvram": s5ChasComBrdM5904StoreNvram,
       "s5ChasComBrdM59042SM": s5ChasComBrdM59042SM,
       "s5ChasComBrdM59042SMStore": s5ChasComBrdM59042SMStore,
       "s5ChasComBrdM59042SMStoreDram": s5ChasComBrdM59042SMStoreDram,
       "s5ChasComBrdM59042SMStoreFlash": s5ChasComBrdM59042SMStoreFlash,
       "s5ChasComBrdM59042SMStoreNvram": s5ChasComBrdM59042SMStoreNvram,
       "s5ChasComBrdM5310": s5ChasComBrdM5310,
       "s5ChasComBrdM5310Store": s5ChasComBrdM5310Store,
       "s5ChasComBrdM5310StoreFlash": s5ChasComBrdM5310StoreFlash,
       "s5ChasComBrdM5310StoreDram": s5ChasComBrdM5310StoreDram,
       "s5ChasComBrdM5310StoreBoot": s5ChasComBrdM5310StoreBoot,
       "s5ChasComBrdM5510": s5ChasComBrdM5510,
       "s5ChasComBrdM5510Store": s5ChasComBrdM5510Store,
       "s5ChasComBrdM5510StoreBoot": s5ChasComBrdM5510StoreBoot,
       "s5ChasComBrdM5510StoreFlash": s5ChasComBrdM5510StoreFlash,
       "s5ChasComBrdM5510StoreDram": s5ChasComBrdM5510StoreDram,
       "s5ChasComBrdM5910S": s5ChasComBrdM5910S,
       "s5ChasComBrdM5910SStore": s5ChasComBrdM5910SStore,
       "s5ChasComBrdM5910SStoreDram": s5ChasComBrdM5910SStoreDram,
       "s5ChasComBrdM5910SStoreFlash": s5ChasComBrdM5910SStoreFlash,
       "s5ChasComBrdM5910SStoreNvram": s5ChasComBrdM5910SStoreNvram,
       "s5ChasComBrdM5910SSM": s5ChasComBrdM5910SSM,
       "s5ChasComBrdM5910SSMStore": s5ChasComBrdM5910SSMStore,
       "s5ChasComBrdM5910SSMStoreDram": s5ChasComBrdM5910SSMStoreDram,
       "s5ChasComBrdM5910SSMStoreFlash": s5ChasComBrdM5910SSMStoreFlash,
       "s5ChasComBrdM5910SSMStoreNvram": s5ChasComBrdM5910SSMStoreNvram,
       "s5ChasComBrdSubM5311": s5ChasComBrdSubM5311,
       "s5ChasComBrdSubM5511": s5ChasComBrdSubM5511,
       "s5ChasComBrdM5905": s5ChasComBrdM5905,
       "s5ChasComBrdM5905Store": s5ChasComBrdM5905Store,
       "s5ChasComBrdM5905StoreDram": s5ChasComBrdM5905StoreDram,
       "s5ChasComBrdM5905StoreFlash": s5ChasComBrdM5905StoreFlash,
       "s5ChasComBrdM5905StoreNvram": s5ChasComBrdM5905StoreNvram,
       "s5ChasComBrdM5575C": s5ChasComBrdM5575C,
       "s5ChasComBrdM5575CStore": s5ChasComBrdM5575CStore,
       "s5ChasComBrdM5575CStore8051Rom": s5ChasComBrdM5575CStore8051Rom,
       "s5ChasComBrdM559": s5ChasComBrdM559,
       "s5ChasComBrdM5390": s5ChasComBrdM5390,
       "s5ChasComBrdM5390Store": s5ChasComBrdM5390Store,
       "s5ChasComBrdM5390StoreDram": s5ChasComBrdM5390StoreDram,
       "s5ChasComBrdM5390StoreFlash": s5ChasComBrdM5390StoreFlash,
       "s5ChasComBrdM5390StoreNvram": s5ChasComBrdM5390StoreNvram,
       "s5ChasComBrdM5307": s5ChasComBrdM5307,
       "s5ChasComBrdM5307Store": s5ChasComBrdM5307Store,
       "s5ChasComBrdM5307Store8051Rom": s5ChasComBrdM5307Store8051Rom,
       "s5ChasComBrdM5307StoreDspRom": s5ChasComBrdM5307StoreDspRom,
       "s5ChasComBrdMCR5308": s5ChasComBrdMCR5308,
       "s5ChasComBrdMCR5308Store": s5ChasComBrdMCR5308Store,
       "s5ChasComBrdMCR5308Store8051Rom": s5ChasComBrdMCR5308Store8051Rom,
       "s5ChasComBrdMCR5308StoreDspRom": s5ChasComBrdMCR5308StoreDspRom,
       "s5ChasComBrdMCR5378F": s5ChasComBrdMCR5378F,
       "s5ChasComBrdMCR5378FStore": s5ChasComBrdMCR5378FStore,
       "s5ChasComBrdMCR5378FStore8051Rom": s5ChasComBrdMCR5378FStore8051Rom,
       "s5ChasComBrdMCR5378FStoreDspRom": s5ChasComBrdMCR5378FStoreDspRom,
       "s5ChasComBrdM5505": s5ChasComBrdM5505,
       "s5ChasComBrdM5505Store": s5ChasComBrdM5505Store,
       "s5ChasComBrdM5505Store8051Rom": s5ChasComBrdM5505Store8051Rom,
       "s5ChasComSupM5115": s5ChasComSupM5115,
       "s5ChasComSupM5115Store": s5ChasComSupM5115Store,
       "s5ChasComSupM5115StoreDram": s5ChasComSupM5115StoreDram,
       "s5ChasComSupM5115StoreFlash": s5ChasComSupM5115StoreFlash,
       "s5ChasComSupM5115StoreNvram": s5ChasComSupM5115StoreNvram,
       "s5ChasComSupM5115StoreChaEeProm": s5ChasComSupM5115StoreChaEeProm,
       "s5ChasComBrdM5740": s5ChasComBrdM5740,
       "s5ChasComBrdM5740Store": s5ChasComBrdM5740Store,
       "s5ChasComBrdM5740Store8051Rom": s5ChasComBrdM5740Store8051Rom,
       "s5ChasComBrdM5740StoreBoot": s5ChasComBrdM5740StoreBoot,
       "s5ChasComBrdM5740StoreDram": s5ChasComBrdM5740StoreDram,
       "s5ChasComBrdM5740StoreNvram": s5ChasComBrdM5740StoreNvram,
       "s5ChasComBrdM5740StoreDisk1": s5ChasComBrdM5740StoreDisk1,
       "s5ChasComBrdM5740StoreDisk2": s5ChasComBrdM5740StoreDisk2,
       "s5ChasComBrdM5720": s5ChasComBrdM5720,
       "s5ChasComBrdM5720Store": s5ChasComBrdM5720Store,
       "s5ChasComBrdM5720Store8051Rom": s5ChasComBrdM5720Store8051Rom,
       "s5ChasComBrdM5720StoreEprom": s5ChasComBrdM5720StoreEprom,
       "s5ChasComBrdM5720StoreSram": s5ChasComBrdM5720StoreSram,
       "s5ChasComBrdM5700": s5ChasComBrdM5700,
       "s5ChasComBrdM5700Store": s5ChasComBrdM5700Store,
       "s5ChasComBrdM5700Store8051Rom": s5ChasComBrdM5700Store8051Rom,
       "s5ChasComBrdM5700StoreEprom": s5ChasComBrdM5700StoreEprom,
       "s5ChasComBrdM5700StoreSram": s5ChasComBrdM5700StoreSram,
       "s5ChasComBrdSubM5700-17": s5ChasComBrdSubM5700_17,
       "s5ChasComBrdSubM5700-24": s5ChasComBrdSubM5700_24,
       "s5ChasComBrdSubM5700-14": s5ChasComBrdSubM5700_14,
       "s5ChasComBrdSubM5700-31": s5ChasComBrdSubM5700_31,
       "s5ChasComBrdSubM5700-15": s5ChasComBrdSubM5700_15,
       "s5ChasComBrdM5715": s5ChasComBrdM5715,
       "s5ChasComBrdM5715Store": s5ChasComBrdM5715Store,
       "s5ChasComBrdM5715Store8051Rom": s5ChasComBrdM5715Store8051Rom,
       "s5ChasComBrdM5715StoreEprom": s5ChasComBrdM5715StoreEprom,
       "s5ChasComBrdM5715StoreSram": s5ChasComBrdM5715StoreSram,
       "s5ChasComBrdM5714": s5ChasComBrdM5714,
       "s5ChasComBrdM5714Store": s5ChasComBrdM5714Store,
       "s5ChasComBrdM5714Store8051Rom": s5ChasComBrdM5714Store8051Rom,
       "s5ChasComBrdM5714StoreEprom": s5ChasComBrdM5714StoreEprom,
       "s5ChasComBrdM5714StoreSram": s5ChasComBrdM5714StoreSram,
       "s5ChasComBrdM5328": s5ChasComBrdM5328,
       "s5ChasComBrdM5328Store": s5ChasComBrdM5328Store,
       "s5ChasComBrdM5328Store8051Rom": s5ChasComBrdM5328Store8051Rom,
       "s5ChasComBrdM5328StoreEprom": s5ChasComBrdM5328StoreEprom,
       "s5ChasComBrdM5328StoreSram": s5ChasComBrdM5328StoreSram,
       "s5ChasComBrdM5324": s5ChasComBrdM5324,
       "s5ChasComBrdM5324Store": s5ChasComBrdM5324Store,
       "s5ChasComBrdM5324Store8051Rom": s5ChasComBrdM5324Store8051Rom,
       "s5ChasComBrdM5324StoreEprom": s5ChasComBrdM5324StoreEprom,
       "s5ChasComBrdM5324StoreSram": s5ChasComBrdM5324StoreSram,
       "s5ChasComBrdM10328F": s5ChasComBrdM10328F,
       "s5ChasComBrdM10328FStore": s5ChasComBrdM10328FStore,
       "s5ChasComBrdM10328FStoreSram": s5ChasComBrdM10328FStoreSram,
       "s5ChasComBrdM10328FStoreDram": s5ChasComBrdM10328FStoreDram,
       "s5ChasComBrdM10328FStoreNvram": s5ChasComBrdM10328FStoreNvram,
       "s5ChasComBrdM10328FStoreEprom": s5ChasComBrdM10328FStoreEprom,
       "s5ChasComBrdM10328FStoreFlash": s5ChasComBrdM10328FStoreFlash,
       "s5ChasComBrdM10328SM": s5ChasComBrdM10328SM,
       "s5ChasComBrdM10328SMStore": s5ChasComBrdM10328SMStore,
       "s5ChasComBrdM10328SMStoreSram": s5ChasComBrdM10328SMStoreSram,
       "s5ChasComBrdM10328SMStoreDram": s5ChasComBrdM10328SMStoreDram,
       "s5ChasComBrdM10328SMStoreNvram": s5ChasComBrdM10328SMStoreNvram,
       "s5ChasComBrdM10328SMStoreEprom": s5ChasComBrdM10328SMStoreEprom,
       "s5ChasComBrdM10328SMStoreFlash": s5ChasComBrdM10328SMStoreFlash,
       "s5ChasComBrdM10324F": s5ChasComBrdM10324F,
       "s5ChasComBrdM10324FStore": s5ChasComBrdM10324FStore,
       "s5ChasComBrdM10324FStoreSram": s5ChasComBrdM10324FStoreSram,
       "s5ChasComBrdM10324FStoreDram": s5ChasComBrdM10324FStoreDram,
       "s5ChasComBrdM10324FStoreNvram": s5ChasComBrdM10324FStoreNvram,
       "s5ChasComBrdM10324FStoreEprom": s5ChasComBrdM10324FStoreEprom,
       "s5ChasComBrdM10324FStoreFlash": s5ChasComBrdM10324FStoreFlash,
       "s5ChasComBrdM5308P": s5ChasComBrdM5308P,
       "s5ChasComBrdM5308PStore": s5ChasComBrdM5308PStore,
       "s5ChasComBrdM5308PStore8051Rom": s5ChasComBrdM5308PStore8051Rom,
       "s5ChasComBrdM5310ASA": s5ChasComBrdM5310ASA,
       "s5ChasComBrdM5310ASAStore": s5ChasComBrdM5310ASAStore,
       "s5ChasComBrdM5310ASAStoreBoot": s5ChasComBrdM5310ASAStoreBoot,
       "s5ChasComBrdM5310ASAStoreFlash": s5ChasComBrdM5310ASAStoreFlash,
       "s5ChasComBrdM5310ASAStoreDram": s5ChasComBrdM5310ASAStoreDram,
       "s5ChasComBrdSubMMCE": s5ChasComBrdSubMMCE,
       "s5ChasComBrdSubM5740AtmBkplIntf": s5ChasComBrdSubM5740AtmBkplIntf,
       "s5ChasComM5DN002m": s5ChasComM5DN002m,
       "s5ChasComM5DN002mStore": s5ChasComM5DN002mStore,
       "s5ChasComM5DN002mStoreFlash": s5ChasComM5DN002mStoreFlash,
       "s5ChasComM5DN002mStoreBoot": s5ChasComM5DN002mStoreBoot,
       "s5ChasComM5DN003m": s5ChasComM5DN003m,
       "s5ChasComM5DN003mStore": s5ChasComM5DN003mStore,
       "s5ChasComM5DN003mStoreFlash": s5ChasComM5DN003mStoreFlash,
       "s5ChasComM5DN003mStoreBoot": s5ChasComM5DN003mStoreBoot,
       "s5ChasComM5DN308P": s5ChasComM5DN308P,
       "s5ChasComM5DN304P": s5ChasComM5DN304P,
       "s5ChasComM5DN378P-F": s5ChasComM5DN378P_F,
       "s5ChasComM5DN307P": s5ChasComM5DN307P,
       "s5ChasComM5DN310": s5ChasComM5DN310,
       "s5ChasComM5DN310Store": s5ChasComM5DN310Store,
       "s5ChasComM5DN310StoreBoot": s5ChasComM5DN310StoreBoot,
       "s5ChasComM5DN310StoreFlash": s5ChasComM5DN310StoreFlash,
       "s5ChasComM5DN310StoreDram": s5ChasComM5DN310StoreDram,
       "s5ChasComMN11": s5ChasComMN11,
       "s5ChasComMN11Store": s5ChasComMN11Store,
       "s5ChasComMN11StoreFlash": s5ChasComMN11StoreFlash,
       "s5ChasComMN11StoreDram": s5ChasComMN11StoreDram,
       "s5ChasComMNBayStackm1": s5ChasComMNBayStackm1,
       "s5ChasComMNBayStackm1Store": s5ChasComMNBayStackm1Store,
       "s5ChasComMNBayStackm1StoreRom": s5ChasComMNBayStackm1StoreRom,
       "s5ChasComMNBayStackm2": s5ChasComMNBayStackm2,
       "s5ChasComMNBayStackm2Store": s5ChasComMNBayStackm2Store,
       "s5ChasComMNBayStackm2StoreRom": s5ChasComMNBayStackm2StoreRom,
       "s5ChasComMNBayStackAui": s5ChasComMNBayStackAui,
       "s5ChasComMNBayStackThin": s5ChasComMNBayStackThin,
       "s5ChasComMNBayStackFL": s5ChasComMNBayStackFL,
       "s5ChasComMNBayStackStdNmm": s5ChasComMNBayStackStdNmm,
       "s5ChasComMNBayStackStdNmmStore": s5ChasComMNBayStackStdNmmStore,
       "s5ChasComMNBayStackStdnmmStoreBoot": s5ChasComMNBayStackStdnmmStoreBoot,
       "s5ChasComMNBayStackStdNmmStoreFlash": s5ChasComMNBayStackStdNmmStoreFlash,
       "s5ChasComMNBayStackStdNmmStoreDram": s5ChasComMNBayStackStdNmmStoreDram,
       "s5ChasComMNBayStackAdvNmm": s5ChasComMNBayStackAdvNmm,
       "s5ChasComMNBayStackAdvNmmStore": s5ChasComMNBayStackAdvNmmStore,
       "s5ChasComMNBayStackAdvNmmStoreBoot": s5ChasComMNBayStackAdvNmmStoreBoot,
       "s5ChasComMNBayStackAdvNmmStoreFlash": s5ChasComMNBayStackAdvNmmStoreFlash,
       "s5ChasComMNBayStackAdvNmmStoreDram": s5ChasComMNBayStackAdvNmmStoreDram,
       "s5ChasComMF-10BaseT": s5ChasComMF_10BaseT,
       "s5ChasComBrdM58000": s5ChasComBrdM58000,
       "s5ChasComBrdM58000Store": s5ChasComBrdM58000Store,
       "s5ChasComBrdM58000StoreBoot": s5ChasComBrdM58000StoreBoot,
       "s5ChasComBrdM58000StoreFlash": s5ChasComBrdM58000StoreFlash,
       "s5ChasComBrdSubM5800014": s5ChasComBrdSubM5800014,
       "s5ChasComBrdSubM5800015": s5ChasComBrdSubM5800015,
       "s5ChasComBrdSubM5800016": s5ChasComBrdSubM5800016,
       "s5ChasComBrdSubM58000MdaExp": s5ChasComBrdSubM58000MdaExp,
       "s5ChasComM5DN378P-A": s5ChasComM5DN378P_A,
       "s5ChasComMBayStack100m1": s5ChasComMBayStack100m1,
       "s5ChasComMBayStack100m1Store": s5ChasComMBayStack100m1Store,
       "s5ChasComMBayStack100m1StoreRom": s5ChasComMBayStack100m1StoreRom,
       "s5ChasComMBayStack100Nmm": s5ChasComMBayStack100Nmm,
       "s5ChasComMBayStack100NmmStore": s5ChasComMBayStack100NmmStore,
       "s5ChasComMBayStack100NmmStoreBoot": s5ChasComMBayStack100NmmStoreBoot,
       "s5ChasComMBayStack100NmmStoreFlash": s5ChasComMBayStack100NmmStoreFlash,
       "s5ChasComMBayStack100NmmStoreDram": s5ChasComMBayStack100NmmStoreDram,
       "s5ChasComMBayStack100-FxMda": s5ChasComMBayStack100_FxMda,
       "s5ChasComMBayStack100-TxMda": s5ChasComMBayStack100_TxMda,
       "s5ChasComMBayStack100-Tx12": s5ChasComMBayStack100_Tx12,
       "s5ChasComM5DN301P": s5ChasComM5DN301P,
       "s5ChasComBrdM5307PS-HD": s5ChasComBrdM5307PS_HD,
       "s5ChasComBrdM5307PS-HDStore": s5ChasComBrdM5307PS_HDStore,
       "s5ChasComBrdM5307PS-HDStore8051Rom": s5ChasComBrdM5307PS_HDStore8051Rom,
       "s5ChasComBrdM5300P": s5ChasComBrdM5300P,
       "s5ChasComBrdM5300PStore": s5ChasComBrdM5300PStore,
       "s5ChasComBrdM5300PStore8051Rom": s5ChasComBrdM5300PStore8051Rom,
       "s5ChasComMod-5328mEther16PC10BT": s5ChasComMod_5328mEther16PC10BT,
       "s5ChasComMod-5724mATM4PMMFiber": s5ChasComMod_5724mATM4PMMFiber,
       "s5ChasComMod-5724MmATMMCP4PMMFiber": s5ChasComMod_5724MmATMMCP4PMMFiber,
       "s5ChasComMod-5328MmEtherMCP8PC10BT": s5ChasComMod_5328MmEtherMCP8PC10BT,
       "s5ChasComMod-5328FXmEther12P2FXP": s5ChasComMod_5328FXmEther12P2FXP,
       "s5ChasComMod-5324mEther12PFL": s5ChasComMod_5324mEther12PFL,
       "s5ChasComMod-5525mTR8PCopper": s5ChasComMod_5525mTR8PCopper,
       "s5ChasComMod-5525MmTRMCP4PCopper": s5ChasComMod_5525MmTRMCP4PCopper,
       "s5ChasComMod-5524mTR8PFiber": s5ChasComMod_5524mTR8PFiber,
       "s5ChasComMod-5524MmTR4PFiber": s5ChasComMod_5524MmTR4PFiber,
       "s5ChasComMod-5924mFDDI1P": s5ChasComMod_5924mFDDI1P,
       "s5ChasComMod-5824mEther4PFX": s5ChasComMod_5824mEther4PFX,
       "s5ChasComMod-5828FmEther2PTX2PFX": s5ChasComMod_5828FmEther2PTX2PFX,
       "s5ChasComMod-5824MmEtherMCP2PFX": s5ChasComMod_5824MmEtherMCP2PFX,
       "s5ChasComMod-5724SMmATM4PSMFiber": s5ChasComMod_5724SMmATM4PSMFiber,
       "s5ChasComMod-5725mATM4PCopper": s5ChasComMod_5725mATM4PCopper,
       "s5ChasComMod-5721DS3mATM2P": s5ChasComMod_5721DS3mATM2P,
       "s5ChasComMod-5721E3mATM2P": s5ChasComMod_5721E3mATM2P,
       "s5ChasComMod-5380E4Bkp2N": s5ChasComMod_5380E4Bkp2N,
       "s5ChasComMod-5380TR4Bkp2N": s5ChasComMod_5380TR4Bkp2N,
       "s5ChasComMod-5000ENetD10-T": s5ChasComMod_5000ENetD10_T,
       "s5ChasComMod-5000ENetS100-T": s5ChasComMod_5000ENetS100_T,
       "s5ChasComMod-5000TRNetD-DB9": s5ChasComMod_5000TRNetD_DB9,
       "s5ChasComMod-5000MMFibNetD-DASMIC": s5ChasComMod_5000MMFibNetD_DASMIC,
       "s5ChasComMod-5000SMFibNetS-DASMIC": s5ChasComMod_5000SMFibNetS_DASMIC,
       "s5ChasComMod-5000SMMMFibNetS-DASMIC": s5ChasComMod_5000SMMMFibNetS_DASMIC,
       "s5ChasComMod-5000MMSMFibNetS-DASMIC": s5ChasComMod_5000MMSMFibNetS_DASMIC,
       "s5ChasComMod-5000SynNetD-WAN44": s5ChasComMod_5000SynNetD_WAN44,
       "s5ChasComMod-5000SynNetQ-ISDNBRI8": s5ChasComMod_5000SynNetQ_ISDNBRI8,
       "s5ChasComMod-5000MCE1NetQ-75120": s5ChasComMod_5000MCE1NetQ_75120,
       "s5ChasComMod-5000MCT1NetQ-RJ48C": s5ChasComMod_5000MCT1NetQ_RJ48C,
       "s5ChasComMod-5000SynNet4-50Pin": s5ChasComMod_5000SynNet4_50Pin,
       "s5ChasComMod-5000Co-Processor": s5ChasComMod_5000Co_Processor,
       "s5ChasComMod-5000ATMNet1-MMOC3": s5ChasComMod_5000ATMNet1_MMOC3,
       "s5ChasComMod-5000ATMNet1-SMOC3": s5ChasComMod_5000ATMNet1_SMOC3,
       "s5ChasComMod-5000ATMNet1-DS3": s5ChasComMod_5000ATMNet1_DS3,
       "s5ChasComMod-5000ATMNet1-E3": s5ChasComMod_5000ATMNet1_E3,
       "s5ChasComBrdSubM58000Fddi": s5ChasComBrdSubM58000Fddi,
       "s5ChasComBrdM28200": s5ChasComBrdM28200,
       "s5ChasComBrdM28200Store": s5ChasComBrdM28200Store,
       "s5ChasComBrdM28200StoreBoot": s5ChasComBrdM28200StoreBoot,
       "s5ChasComBrdM28200StoreFlash": s5ChasComBrdM28200StoreFlash,
       "s5ChasComBrdM28200StoreDram": s5ChasComBrdM28200StoreDram,
       "s5ChasComBrdSubM2820015": s5ChasComBrdSubM2820015,
       "s5ChasComBrdSubM2820014": s5ChasComBrdSubM2820014,
       "s5ChasComBrdSubM28200105": s5ChasComBrdSubM28200105,
       "s5ChasComBrdSubM28200104": s5ChasComBrdSubM28200104,
       "s5ChasComBrdSubM28200106": s5ChasComBrdSubM28200106,
       "s5ChasComBrdSubM28200Exp": s5ChasComBrdSubM28200Exp,
       "s5ChasComBrdSubM28200Atm": s5ChasComBrdSubM28200Atm,
       "s5ChasComBrdSubM28200Fddi": s5ChasComBrdSubM28200Fddi,
       "s5ChasComBrdSubM28200N11": s5ChasComBrdSubM28200N11,
       "s5ChasComBrdSubM28200N111": s5ChasComBrdSubM28200N111,
       "s5ChasComMod-c100mTR4PC": s5ChasComMod_c100mTR4PC,
       "s5ChasComMod-c100mTRMCP4PC": s5ChasComMod_c100mTRMCP4PC,
       "s5ChasComMod-c100mATM": s5ChasComMod_c100mATM,
       "s5ChasComMod-c100mTRFiber": s5ChasComMod_c100mTRFiber,
       "s5ChasComMod-c100mTRMCPFiber": s5ChasComMod_c100mTRMCPFiber,
       "s5ChasComMod-c100mEther16PC10BT": s5ChasComMod_c100mEther16PC10BT,
       "s5ChasComMod-c100mEtherMCP8PC10BT": s5ChasComMod_c100mEtherMCP8PC10BT,
       "s5ChasComMod-c100mATM2PSMFiber": s5ChasComMod_c100mATM2PSMFiber,
       "s5ChasComMod-c100mATM2PCopper": s5ChasComMod_c100mATM2PCopper,
       "s5ChasComMod-c100mATM4PMMFiber": s5ChasComMod_c100mATM4PMMFiber,
       "s5ChasComMod-c100mATM4PSMFiber": s5ChasComMod_c100mATM4PSMFiber,
       "s5ChasComMod-c100mATM4PCopper": s5ChasComMod_c100mATM4PCopper,
       "s5ChasComMod-c100mATMMCP2PSMFiber": s5ChasComMod_c100mATMMCP2PSMFiber,
       "s5ChasComMod-c100mATMMCP2PMMFiber": s5ChasComMod_c100mATMMCP2PMMFiber,
       "s5ChasComMod-c100mATMMCP2PCopper": s5ChasComMod_c100mATMMCP2PCopper,
       "s5ChasComMod-c100mATMMCP4PSMFiber": s5ChasComMod_c100mATMMCP4PSMFiber,
       "s5ChasComMod-c100mATMMCP4PMMFiber": s5ChasComMod_c100mATMMCP4PMMFiber,
       "s5ChasComMod-c100mATMMCP4PCopper": s5ChasComMod_c100mATMMCP4PCopper,
       "s5ChasComMod-c100mATM2PC": s5ChasComMod_c100mATM2PC,
       "s5ChasComMod-c100mATM4PC": s5ChasComMod_c100mATM4PC,
       "s5ChasComMod-c100mATMMCP2PC": s5ChasComMod_c100mATMMCP2PC,
       "s5ChasComMod-c100mATMMCP4PC": s5ChasComMod_c100mATMMCP4PC,
       "s5ChasComBrdSubDummy": s5ChasComBrdSubDummy,
       "s5ChasComBrdSub5300-T": s5ChasComBrdSub5300_T,
       "s5ChasComBrdSub5300-A": s5ChasComBrdSub5300_A,
       "s5ChasComBrdSub5300-D": s5ChasComBrdSub5300_D,
       "s5ChasComBrdSub5300-F": s5ChasComBrdSub5300_F,
       "s5ChasComBrdSub5300-S": s5ChasComBrdSub5300_S,
       "s5ChasComBrdSub5300-2": s5ChasComBrdSub5300_2,
       "s5ChasComMBayStackTrm1": s5ChasComMBayStackTrm1,
       "s5ChasComMBayStackTrm1Store": s5ChasComMBayStackTrm1Store,
       "s5ChasComMBayStackTrm1StoreFlash": s5ChasComMBayStackTrm1StoreFlash,
       "s5ChasComMBayStackTrm1StoreBoot": s5ChasComMBayStackTrm1StoreBoot,
       "s5ChasComMBayStackTrNmm": s5ChasComMBayStackTrNmm,
       "s5ChasComMBayStackTrNmmStore": s5ChasComMBayStackTrNmmStore,
       "s5ChasComMBayStackTrNmmStoreBoot": s5ChasComMBayStackTrNmmStoreBoot,
       "s5ChasComMBayStackTrNmmStoreFlash": s5ChasComMBayStackTrNmmStoreFlash,
       "s5ChasComMBayStackTrNmmStoreDram": s5ChasComMBayStackTrNmmStoreDram,
       "s5ChasComMBayStackTrMDAFiber": s5ChasComMBayStackTrMDAFiber,
       "s5ChasComMBayStackTrMDACopper": s5ChasComMBayStackTrMDACopper,
       "s5ChasComMBayStackTrDCM": s5ChasComMBayStackTrDCM,
       "s5ChasComMBayStackTrMRM": s5ChasComMBayStackTrMRM,
       "s5ChasComMNBayStackm3": s5ChasComMNBayStackm3,
       "s5ChasComMNBayStackm3Store": s5ChasComMNBayStackm3Store,
       "s5ChasComMNBayStackm3StoreRom": s5ChasComMNBayStackm3StoreRom,
       "s5ChasComMNBayStackm4": s5ChasComMNBayStackm4,
       "s5ChasComMNBayStackm4Store": s5ChasComMNBayStackm4Store,
       "s5ChasComMNBayStackm4StoreRom": s5ChasComMNBayStackm4StoreRom,
       "s5ChasComMNBayStackRedFL": s5ChasComMNBayStackRedFL,
       "s5ChasComMNBayStackSMFL": s5ChasComMNBayStackSMFL,
       "s5ChasComMNBayStackSMRedFL": s5ChasComMNBayStackSMRedFL,
       "s5ChasComBrdM5308S": s5ChasComBrdM5308S,
       "s5ChasComBrdM5308SStore": s5ChasComBrdM5308SStore,
       "s5ChasComBrdM5308SStore8051Rom": s5ChasComBrdM5308SStore8051Rom,
       "s5ChasComBrdM5307S": s5ChasComBrdM5307S,
       "s5ChasComBrdM5307SStore": s5ChasComBrdM5307SStore,
       "s5ChasComBrdM5307SStore8051Rom": s5ChasComBrdM5307SStore8051Rom,
       "s5ChasComBrdM5308PS": s5ChasComBrdM5308PS,
       "s5ChasComBrdM5308PSStore": s5ChasComBrdM5308PSStore,
       "s5ChasComBrdM5308PSStore8051Rom": s5ChasComBrdM5308PSStore8051Rom,
       "s5ChasComBrdM5307PS": s5ChasComBrdM5307PS,
       "s5ChasComBrdM5307PSStore": s5ChasComBrdM5307PSStore,
       "s5ChasComBrdM5307PSStore8051Rom": s5ChasComBrdM5307PSStore8051Rom,
       "s5ChasComM5DN308PS": s5ChasComM5DN308PS,
       "s5ChasComM5DN307PS": s5ChasComM5DN307PS,
       "s5ChasComM5DN378P-SM": s5ChasComM5DN378P_SM,
       "s5ChasComMNBayStackm5": s5ChasComMNBayStackm5,
       "s5ChasComMNBayStackm5Store": s5ChasComMNBayStackm5Store,
       "s5ChasComMNBayStackm5StoreRom": s5ChasComMNBayStackm5StoreRom,
       "s5ChasComMBayStack301": s5ChasComMBayStack301,
       "s5ChasComMBayStack301Store": s5ChasComMBayStack301Store,
       "s5ChasComMBayStack301MaxRAM": s5ChasComMBayStack301MaxRAM,
       "s5ChasComMBayStack301InstalledRAM": s5ChasComMBayStack301InstalledRAM,
       "s5ChasComMBayStack301Flash": s5ChasComMBayStack301Flash,
       "s5ChasComM5DN003Am": s5ChasComM5DN003Am,
       "s5ChasComM5DN003AmStore": s5ChasComM5DN003AmStore,
       "s5ChasComM5DN003AmStoreFlash": s5ChasComM5DN003AmStoreFlash,
       "s5ChasComM5DN003AmStoreBoot": s5ChasComM5DN003AmStoreBoot,
       "s5ChasComM5DN002Am": s5ChasComM5DN002Am,
       "s5ChasComM5DN002AmStore": s5ChasComM5DN002AmStore,
       "s5ChasComM5DN002AmStoreFlash": s5ChasComM5DN002AmStoreFlash,
       "s5ChasComM5DN002AmStoreBoot": s5ChasComM5DN002AmStoreBoot,
       "s5ChasComBrdM5405": s5ChasComBrdM5405,
       "s5ChasComBrdM5405Store": s5ChasComBrdM5405Store,
       "s5ChasComBrdM5405StoreBoot": s5ChasComBrdM5405StoreBoot,
       "s5ChasComBrdM5405StoreFlash": s5ChasComBrdM5405StoreFlash,
       "s5ChasComBrdM5405StoreDram": s5ChasComBrdM5405StoreDram,
       "s5ChasComBrdM5475FX": s5ChasComBrdM5475FX,
       "s5ChasComBrdM5475FXStore": s5ChasComBrdM5475FXStore,
       "s5ChasComBrdM5475FXStoreBoot": s5ChasComBrdM5475FXStoreBoot,
       "s5ChasComBrdM5475FXStoreFlash": s5ChasComBrdM5475FXStoreFlash,
       "s5ChasComBrdM5475FXStoreDram": s5ChasComBrdM5475FXStoreDram,
       "s5ChasComMod-c100mEther12P2FXP": s5ChasComMod_c100mEther12P2FXP,
       "s5ChasComMod-c100mEther14P2TXP": s5ChasComMod_c100mEther14P2TXP,
       "s5ChasComBrdM5605P": s5ChasComBrdM5605P,
       "s5ChasComBrdM5605PStore": s5ChasComBrdM5605PStore,
       "s5ChasComBrdM5605PStoreBoot": s5ChasComBrdM5605PStoreBoot,
       "s5ChasComBrdM5605PStoreFlash": s5ChasComBrdM5605PStoreFlash,
       "s5ChasComBrdM5605PStoreDram": s5ChasComBrdM5605PStoreDram,
       "s5ChasComBrdM5675PFX": s5ChasComBrdM5675PFX,
       "s5ChasComBrdM5675PFXStore": s5ChasComBrdM5675PFXStore,
       "s5ChasComBrdM5675PFXStoreBoot": s5ChasComBrdM5675PFXStoreBoot,
       "s5ChasComBrdM5675PFXStoreFlash": s5ChasComBrdM5675PFXStoreFlash,
       "s5ChasComBrdM5675PFXStoreDram": s5ChasComBrdM5675PFXStoreDram,
       "s5ChasComBrdM5616": s5ChasComBrdM5616,
       "s5ChasComBrdM5616Store": s5ChasComBrdM5616Store,
       "s5ChasComBrdM5616StoreFlash": s5ChasComBrdM5616StoreFlash,
       "s5ChasComBrdM5616StoreDram": s5ChasComBrdM5616StoreDram,
       "s5ChasComBrdM5616StoreBoot": s5ChasComBrdM5616StoreBoot,
       "s5ChasComBrdM5316": s5ChasComBrdM5316,
       "s5ChasComBrdM5316Store": s5ChasComBrdM5316Store,
       "s5ChasComBrdM5316StoreFlash": s5ChasComBrdM5316StoreFlash,
       "s5ChasComBrdM5316StoreDram": s5ChasComBrdM5316StoreDram,
       "s5ChasComBrdM5316StoreBoot": s5ChasComBrdM5316StoreBoot,
       "s5ChasComM3308S-FxMda": s5ChasComM3308S_FxMda,
       "s5ChasComBrdBayStack302T": s5ChasComBrdBayStack302T,
       "s5ChasComBrdBayStack302TStore": s5ChasComBrdBayStack302TStore,
       "s5ChasComBrdBayStack302TFlash": s5ChasComBrdBayStack302TFlash,
       "s5ChasComBrdBayStack302TDram": s5ChasComBrdBayStack302TDram,
       "s5ChasComBrdBayStack302F": s5ChasComBrdBayStack302F,
       "s5ChasComBrdBayStack302FStore": s5ChasComBrdBayStack302FStore,
       "s5ChasComBrdBayStack302FFlash": s5ChasComBrdBayStack302FFlash,
       "s5ChasComBrdBayStack302FDram": s5ChasComBrdBayStack302FDram,
       "s5ChasComMod-c100mEther8P10FL": s5ChasComMod_c100mEther8P10FL,
       "s5ChasComMod-c100mEther12P2BTP": s5ChasComMod_c100mEther12P2BTP,
       "s5ChasComMod-c100mEther4P100BT": s5ChasComMod_c100mEther4P100BT,
       "s5ChasComMod-5425mEther4PC100BT": s5ChasComMod_5425mEther4PC100BT,
       "s5ChasComMod-c100mEther8P2TXP": s5ChasComMod_c100mEther8P2TXP,
       "s5ChasComBrdBayStack350T": s5ChasComBrdBayStack350T,
       "s5ChasComBrdBayStack350TStore": s5ChasComBrdBayStack350TStore,
       "s5ChasComBrdBayStack350TFlash": s5ChasComBrdBayStack350TFlash,
       "s5ChasComBrdBayStack350TBootFW": s5ChasComBrdBayStack350TBootFW,
       "s5ChasComBrdBayStack350TDram": s5ChasComBrdBayStack350TDram,
       "s5ChasComBrdBayStack350F": s5ChasComBrdBayStack350F,
       "s5ChasComBrdBayStack350FStore": s5ChasComBrdBayStack350FStore,
       "s5ChasComBrdBayStack350FFlash": s5ChasComBrdBayStack350FFlash,
       "s5ChasComBrdBayStack350FBootFW": s5ChasComBrdBayStack350FBootFW,
       "s5ChasComBrdBayStack350FDram": s5ChasComBrdBayStack350FDram,
       "s5ChasComBrdBayStack350FHD": s5ChasComBrdBayStack350FHD,
       "s5ChasComBrdBayStack350FHDStore": s5ChasComBrdBayStack350FHDStore,
       "s5ChasComBrdBayStack350FHDFlash": s5ChasComBrdBayStack350FHDFlash,
       "s5ChasComBrdBayStack350FHDBootFW": s5ChasComBrdBayStack350FHDBootFW,
       "s5ChasComBrdBayStack350FHDDram": s5ChasComBrdBayStack350FHDDram,
       "s5ChasComBrdBayStack350THD": s5ChasComBrdBayStack350THD,
       "s5ChasComBrdBayStack350THDStore": s5ChasComBrdBayStack350THDStore,
       "s5ChasComBrdBayStack350THDFlash": s5ChasComBrdBayStack350THDFlash,
       "s5ChasComBrdBayStack350THDBootFW": s5ChasComBrdBayStack350THDBootFW,
       "s5ChasComBrdBayStack350THDDram": s5ChasComBrdBayStack350THDDram,
       "s5ChasComMod-5724M-SMmATMMCP4PSMFiber": s5ChasComMod_5724M_SMmATMMCP4PSMFiber,
       "s5ChasComMod-SwNode10t16": s5ChasComMod_SwNode10t16,
       "s5ChasComMod-SwNode100tx2": s5ChasComMod_SwNode100tx2,
       "s5ChasComMod-SwNode10f8": s5ChasComMod_SwNode10f8,
       "s5ChasComMod-SwNode100tx16": s5ChasComMod_SwNode100tx16,
       "s5ChasComMod-SwNode100fx3": s5ChasComMod_SwNode100fx3,
       "s5ChasComDCMX220SwNode": s5ChasComDCMX220SwNode,
       "s5ChasComMod-c100mEther4x4P100BT": s5ChasComMod_c100mEther4x4P100BT,
       "s5ChasComMod-c100mEther4P100FX": s5ChasComMod_c100mEther4P100FX,
       "s5ChasComBrdBayStack150": s5ChasComBrdBayStack150,
       "s5ChasComBrdBayStack152": s5ChasComBrdBayStack152,
       "s5ChasComBrdBayStack151": s5ChasComBrdBayStack151,
       "s5ChasComBrdBayStack153": s5ChasComBrdBayStack153,
       "s5ChasComBrdBayStack150NMM": s5ChasComBrdBayStack150NMM,
       "s5ChasComBrdBayStack150NMMStore": s5ChasComBrdBayStack150NMMStore,
       "s5ChasComBrdBayStack150NMMStoreBoot": s5ChasComBrdBayStack150NMMStoreBoot,
       "s5ChasComBrdBayStack150NMMStoreFlash": s5ChasComBrdBayStack150NMMStoreFlash,
       "s5ChasComBrdBayStack150NMMStoreDram": s5ChasComBrdBayStack150NMMStoreDram,
       "s5ChasComBrdBayStack150NMMExpMod": s5ChasComBrdBayStack150NMMExpMod,
       "s5ChasComMod-C100ATMMDAhost": s5ChasComMod_C100ATMMDAhost,
       "s5ChasComMod-C100ATMMDAMcp": s5ChasComMod_C100ATMMDAMcp,
       "s5ChasComMod-5720ATMMDAhost": s5ChasComMod_5720ATMMDAhost,
       "s5ChasComMod-5720MATMMDAMcp": s5ChasComMod_5720MATMMDAMcp,
       "s5ChasComMod-5720-14MultiModeMda": s5ChasComMod_5720_14MultiModeMda,
       "s5ChasComMod-5720-15UTPMda": s5ChasComMod_5720_15UTPMda,
       "s5ChasComMod-5720-17SingleModeMda": s5ChasComMod_5720_17SingleModeMda,
       "s5ChasComMod-5720-31DS3Mda": s5ChasComMod_5720_31DS3Mda,
       "s5ChasComMod-5720-41E3Mda": s5ChasComMod_5720_41E3Mda,
       "s5ChasComMod-SwNodeCPU": s5ChasComMod_SwNodeCPU,
       "s5ChasComMod-c1008PUTPTRMcp": s5ChasComMod_c1008PUTPTRMcp,
       "s5ChasComMod-c1008PUTPTR": s5ChasComMod_c1008PUTPTR,
       "s5ChasComBrdM5328-HD": s5ChasComBrdM5328_HD,
       "s5ChasComBrdM5328-HDStore": s5ChasComBrdM5328_HDStore,
       "s5ChasComBrdM5328-HDStoreFlash": s5ChasComBrdM5328_HDStoreFlash,
       "s5ChasComBrdM5328-HDStoreDram": s5ChasComBrdM5328_HDStoreDram,
       "s5ChasComBrdM5625": s5ChasComBrdM5625,
       "s5ChasComBrdM5455": s5ChasComBrdM5455,
       "s5ChasComBrdM5455Store": s5ChasComBrdM5455Store,
       "s5ChasComBrdM5455StoreFlash": s5ChasComBrdM5455StoreFlash,
       "s5ChasComBrdM5455StoreDram": s5ChasComBrdM5455StoreDram,
       "s5ChasComM5611-DCM": s5ChasComM5611_DCM,
       "s5ChasComM5611-DCMStore": s5ChasComM5611_DCMStore,
       "s5ChasComM5611-DCMStoreFlash": s5ChasComM5611_DCMStoreFlash,
       "s5ChasComM5611-DCMStoreDram": s5ChasComM5611_DCMStoreDram,
       "s5ChasComBrdBayStack202": s5ChasComBrdBayStack202,
       "s5ChasComBrdBayStack203": s5ChasComBrdBayStack203,
       "s5ChasComBrdBayStack204": s5ChasComBrdBayStack204,
       "s5ChasComBrdBayStack205": s5ChasComBrdBayStack205,
       "s5ChasComBrdBayStack200NMM": s5ChasComBrdBayStack200NMM,
       "s5ChasComBrdBayStack200NMMStore": s5ChasComBrdBayStack200NMMStore,
       "s5ChasComBrdBayStack200NMMStoreFlash": s5ChasComBrdBayStack200NMMStoreFlash,
       "s5ChasComBrdBayStack200NMMStoreDram": s5ChasComBrdBayStack200NMMStoreDram,
       "s5ChasComMBayStack303": s5ChasComMBayStack303,
       "s5ChasComMBayStack304": s5ChasComMBayStack304,
       "s5ChasComMBayStack303A": s5ChasComMBayStack303A,
       "s5ChasComMBayStack304A": s5ChasComMBayStack304A,
       "s5ChasComMBayStack303-304FxMda": s5ChasComMBayStack303_304FxMda,
       "s5ChasComMBayStack303-304TxMda": s5ChasComMBayStack303_304TxMda,
       "s5ChasComBrdM5665": s5ChasComBrdM5665,
       "s5ChasComBrdM5665Store": s5ChasComBrdM5665Store,
       "s5ChasComBrdM5665StoreFlash": s5ChasComBrdM5665StoreFlash,
       "s5ChasComBrdM5665StoreDram": s5ChasComBrdM5665StoreDram,
       "s5ChasComBrdM5660FX": s5ChasComBrdM5660FX,
       "s5ChasComBrdM5660FXStore": s5ChasComBrdM5660FXStore,
       "s5ChasComBrdM5660FXStoreFlash": s5ChasComBrdM5660FXStoreFlash,
       "s5ChasComBrdM5660FXStoreDram": s5ChasComBrdM5660FXStoreDram,
       "s5ChasComBrdM5620FX": s5ChasComBrdM5620FX,
       "s5ChasComBrdM5620FXStore": s5ChasComBrdM5620FXStore,
       "s5ChasComBrdM5620FXStoreFlash": s5ChasComBrdM5620FXStoreFlash,
       "s5ChasComBrdM5620FXStoreDram": s5ChasComBrdM5620FXStoreDram,
       "s5ChasComBrdBayStack250": s5ChasComBrdBayStack250,
       "s5ChasComBrdBayStack251": s5ChasComBrdBayStack251,
       "s5ChasComBrdBayStack252": s5ChasComBrdBayStack252,
       "s5ChasComBrdBayStack250NMM": s5ChasComBrdBayStack250NMM,
       "s5ChasComBrdBayStack250NMMStore": s5ChasComBrdBayStack250NMMStore,
       "s5ChasComBrdBayStack250NMMStoreFlash": s5ChasComBrdBayStack250NMMStoreFlash,
       "s5ChasComBrdBayStack250NMMStoreDram": s5ChasComBrdBayStack250NMMStoreDram,
       "s5ChasComBrdBayStack250NMMStoreBoot": s5ChasComBrdBayStack250NMMStoreBoot,
       "s5ChasComMod-c100mEther24P10BT": s5ChasComMod_c100mEther24P10BT,
       "s5ChasComMod-C100ATMMultiModeMda": s5ChasComMod_C100ATMMultiModeMda,
       "s5ChasComMod-C100ATMUTPMda": s5ChasComMod_C100ATMUTPMda,
       "s5ChasComMod-C100ATMSingleModeMda": s5ChasComMod_C100ATMSingleModeMda,
       "s5ChasComMod-C100ATMDS3Mda": s5ChasComMod_C100ATMDS3Mda,
       "s5ChasComMod-C100ATME3Mda": s5ChasComMod_C100ATME3Mda,
       "s5ChasComBrdTR24PC": s5ChasComBrdTR24PC,
       "s5ChasComBrd-C100TR16PC": s5ChasComBrd_C100TR16PC,
       "s5ChasComBrd57622M-SM": s5ChasComBrd57622M_SM,
       "s5ChasComBrd57622M-MM": s5ChasComBrd57622M_MM,
       "s5ChasComBrd57622-MM": s5ChasComBrd57622_MM,
       "s5ChasComBrd-C100ATMMCP1PSM": s5ChasComBrd_C100ATMMCP1PSM,
       "s5ChasComBrd-C100ATMMCP1PMM": s5ChasComBrd_C100ATMMCP1PMM,
       "s5ChasComBrd-C100ATM1PMM": s5ChasComBrd_C100ATM1PMM,
       "s5ChasComBrdBayStack450-24T": s5ChasComBrdBayStack450_24T,
       "s5ChasComBrdBayStack450-24TStore": s5ChasComBrdBayStack450_24TStore,
       "s5ChasComBrdBayStack450-24TStoreFlash": s5ChasComBrdBayStack450_24TStoreFlash,
       "s5ChasComBrdBayStack450-24TStoreBootFW": s5ChasComBrdBayStack450_24TStoreBootFW,
       "s5ChasComBrdBayStack450-24TStoreDram": s5ChasComBrdBayStack450_24TStoreDram,
       "s5ChasComBrdBayStack450-12T": s5ChasComBrdBayStack450_12T,
       "s5ChasComBrdBayStack450-12TStore": s5ChasComBrdBayStack450_12TStore,
       "s5ChasComBrdBayStack450-12TStoreFlash": s5ChasComBrdBayStack450_12TStoreFlash,
       "s5ChasComBrdBayStack450-12TStoreBootFW": s5ChasComBrdBayStack450_12TStoreBootFW,
       "s5ChasComBrdBayStack450-12TStoreDram": s5ChasComBrdBayStack450_12TStoreDram,
       "s5ChasComBrdBayStack410-24T": s5ChasComBrdBayStack410_24T,
       "s5ChasComBrdBayStack450-1SX": s5ChasComBrdBayStack450_1SX,
       "s5ChasComBrdBayStack450-1SR": s5ChasComBrdBayStack450_1SR,
       "s5ChasComBrdBayStack400-4TX": s5ChasComBrdBayStack400_4TX,
       "s5ChasComBrdBayStack400-2FX": s5ChasComBrdBayStack400_2FX,
       "s5ChasComBrdBayStack400-ST1": s5ChasComBrdBayStack400_ST1,
       "s5ChasComBrdBayStack400-ST2": s5ChasComBrdBayStack400_ST2,
       "s5ChasComBrdBayStack450-1LX": s5ChasComBrdBayStack450_1LX,
       "s5ChasComBrdBayStack450-1LR": s5ChasComBrdBayStack450_1LR,
       "s5ChasComBrdBayStack450-2SX": s5ChasComBrdBayStack450_2SX,
       "s5ChasComBrdBayStack450-2LX": s5ChasComBrdBayStack450_2LX,
       "s5ChasComBrdBayStack450-OC3": s5ChasComBrdBayStack450_OC3,
       "s5ChasComBrdBayStack450-24TQP": s5ChasComBrdBayStack450_24TQP,
       "s5ChasComBrdBPS2000-24T": s5ChasComBrdBPS2000_24T,
       "s5ChasComBrdBPS2000-24TStore": s5ChasComBrdBPS2000_24TStore,
       "s5ChasComBrdBPS2000-24TStoreFlash": s5ChasComBrdBPS2000_24TStoreFlash,
       "s5ChasComBrdBPS2000-24TStoreBootFW": s5ChasComBrdBPS2000_24TStoreBootFW,
       "s5ChasComBrdBPS2000-24TStoreDram": s5ChasComBrdBPS2000_24TStoreDram,
       "s5ChasComBrd5424": s5ChasComBrd5424,
       "s5ChasComBrdBayStack525": s5ChasComBrdBayStack525,
       "s5ChasComBrdBayStack350-24T": s5ChasComBrdBayStack350_24T,
       "s5ChasComBrdBayStack350-24TStore": s5ChasComBrdBayStack350_24TStore,
       "s5ChasComBrdBayStack350-24TStoreFlash": s5ChasComBrdBayStack350_24TStoreFlash,
       "s5ChasComBrdBayStack350-24TStoreBootFW": s5ChasComBrdBayStack350_24TStoreBootFW,
       "s5ChasComBrdBayStack350-24TStoreDram": s5ChasComBrdBayStack350_24TStoreDram,
       "s5ChasComBrdBayStack350-12T": s5ChasComBrdBayStack350_12T,
       "s5ChasComBrdBayStack350-12TStore": s5ChasComBrdBayStack350_12TStore,
       "s5ChasComBrdBayStack350-12TStoreFlash": s5ChasComBrdBayStack350_12TStoreFlash,
       "s5ChasComBrdBayStack350-12TStoreBootFW": s5ChasComBrdBayStack350_12TStoreBootFW,
       "s5ChasComBrdBayStack350-12TStoreDram": s5ChasComBrdBayStack350_12TStoreDram,
       "s5ChasComBrdBayStack253": s5ChasComBrdBayStack253,
       "s5ChasComBrdBayStack450-12TQP": s5ChasComBrdBayStack450_12TQP,
       "s5ChasComBrdBayStack350-24TQP": s5ChasComBrdBayStack350_24TQP,
       "s5ChasComBrdBayStack350-24TQPStore": s5ChasComBrdBayStack350_24TQPStore,
       "s5ChasComBrdBayStack350-24TQPStoreFlash": s5ChasComBrdBayStack350_24TQPStoreFlash,
       "s5ChasComBrdBayStack350-24TQPStoreBootFW": s5ChasComBrdBayStack350_24TQPStoreBootFW,
       "s5ChasComBrdBayStack350-24TQPStoreDram": s5ChasComBrdBayStack350_24TQPStoreDram,
       "s5ChasComBrdBayStack350-12TQP": s5ChasComBrdBayStack350_12TQP,
       "s5ChasComBrdBayStack350-12TQPStore": s5ChasComBrdBayStack350_12TQPStore,
       "s5ChasComBrdBayStack350-12TQPStoreFlash": s5ChasComBrdBayStack350_12TQPStoreFlash,
       "s5ChasComBrdBayStack350-12TQPStoreBootFW": s5ChasComBrdBayStack350_12TQPStoreBootFW,
       "s5ChasComBrdBayStack350-12TQPStoreDram": s5ChasComBrdBayStack350_12TQPStoreDram,
       "s5ChasComBrdBayStack450-12F": s5ChasComBrdBayStack450_12F,
       "s5ChasComBrdBayStack450-12FStore": s5ChasComBrdBayStack450_12FStore,
       "s5ChasComBrdBayStack450-12FStoreFlash": s5ChasComBrdBayStack450_12FStoreFlash,
       "s5ChasComBrdBayStack450-12FStoreBootFW": s5ChasComBrdBayStack450_12FStoreBootFW,
       "s5ChasComBrdBayStack450-12FStoreDram": s5ChasComBrdBayStack450_12FStoreDram,
       "s5ChasComBrdBayStack400-4FX": s5ChasComBrdBayStack400_4FX,
       "s5ChasComMBayStack303-24T": s5ChasComMBayStack303_24T,
       "s5ChasComBrdBayStack-100FxMda": s5ChasComBrdBayStack_100FxMda,
       "s5ChasComBrdAccelar8132TX": s5ChasComBrdAccelar8132TX,
       "s5ChasComBrdAccelar8148TX": s5ChasComBrdAccelar8148TX,
       "s5ChasComBrdBayStack254": s5ChasComBrdBayStack254,
       "s5ChasComBrdBayStack255": s5ChasComBrdBayStack255,
       "s5ChasComBrdBayStack25x-100FxMda": s5ChasComBrdBayStack25x_100FxMda,
       "s5ChasComBrdM5625HD": s5ChasComBrdM5625HD,
       "s5ChasComBrdM5424HD": s5ChasComBrdM5424HD,
       "s5ChasComMod-C100mEther20PC": s5ChasComMod_C100mEther20PC,
       "s5ChasComMod-C100mEther16P100FX": s5ChasComMod_C100mEther16P100FX,
       "s5ChasComBrdBayStack670": s5ChasComBrdBayStack670,
       "s5ChasComBrdBayStack670Store": s5ChasComBrdBayStack670Store,
       "s5ChasComBrdBayStack670StoreFlash": s5ChasComBrdBayStack670StoreFlash,
       "s5ChasComBrdM5420": s5ChasComBrdM5420,
       "s5ChasComMod-C100mEther3PGBIC": s5ChasComMod_C100mEther3PGBIC,
       "s5ChasComBrdBPS2000-4TX": s5ChasComBrdBPS2000_4TX,
       "s5ChasComBrdBPS2000-4FX": s5ChasComBrdBPS2000_4FX,
       "s5ChasComBrdBPS2000-2FX": s5ChasComBrdBPS2000_2FX,
       "s5ChasComBrdBayStack3580-16F": s5ChasComBrdBayStack3580_16F,
       "s5ChasComBrdBayStack3580-16FStore": s5ChasComBrdBayStack3580_16FStore,
       "s5ChasComBrdBayStack3580-16FStoreFlash": s5ChasComBrdBayStack3580_16FStoreFlash,
       "s5ChasComBrdBayStack3580-16FStoreBootFW": s5ChasComBrdBayStack3580_16FStoreBootFW,
       "s5ChasComBrdBayStack3580-16FStoreDram": s5ChasComBrdBayStack3580_16FStoreDram,
       "s5ChasComBrdBayStack450-OC3S": s5ChasComBrdBayStack450_OC3S,
       "s5ChasComBrdBayStack450-OC12": s5ChasComBrdBayStack450_OC12,
       "s5ChasComBrdBayStack450-OC12S": s5ChasComBrdBayStack450_OC12S,
       "s5ChasComBrdBayStack420-24T": s5ChasComBrdBayStack420_24T,
       "s5ChasComBrdBayStack420-24TStore": s5ChasComBrdBayStack420_24TStore,
       "s5ChasComBrdBayStack420-24TStoreFlash": s5ChasComBrdBayStack420_24TStoreFlash,
       "s5ChasComBrdBayStack420-24TStoreBootFW": s5ChasComBrdBayStack420_24TStoreBootFW,
       "s5ChasComBrdBayStack420-24TStoreDram": s5ChasComBrdBayStack420_24TStoreDram,
       "s5ChasComBrdBayStack450-GBIC": s5ChasComBrdBayStack450_GBIC,
       "s5ChasComBrdBayStack450-GBICno": s5ChasComBrdBayStack450_GBICno,
       "s5ChasComBrdBayStack450-GBICun": s5ChasComBrdBayStack450_GBICun,
       "s5ChasComBrdBayStack450-GBICsx": s5ChasComBrdBayStack450_GBICsx,
       "s5ChasComBrdBayStack450-GBIClx": s5ChasComBrdBayStack450_GBIClx,
       "s5ChasComBrdBayStack450-GBICzx": s5ChasComBrdBayStack450_GBICzx,
       "s5ChasComBrdBayStack450-GBICxd": s5ChasComBrdBayStack450_GBICxd,
       "s5ChasComBrdBayStack450-GBICbt": s5ChasComBrdBayStack450_GBICbt,
       "s5ChasComBrdMetro1200ESM-12T": s5ChasComBrdMetro1200ESM_12T,
       "s5ChasComBrdMetro1200ESM-12TStore": s5ChasComBrdMetro1200ESM_12TStore,
       "s5ChasComBrdMetro1200ESM-12TStoreFlash": s5ChasComBrdMetro1200ESM_12TStoreFlash,
       "s5ChasComBrdMetro1200ESM-12TStoreBootFW": s5ChasComBrdMetro1200ESM_12TStoreBootFW,
       "s5ChasComBrdMetro1200ESM-12TStoreDram": s5ChasComBrdMetro1200ESM_12TStoreDram,
       "s5ChasComBrdBayStack380-24T": s5ChasComBrdBayStack380_24T,
       "s5ChasComBrdBayStack380-24TStore": s5ChasComBrdBayStack380_24TStore,
       "s5ChasComBrdBayStack380-24TStoreFlash": s5ChasComBrdBayStack380_24TStoreFlash,
       "s5ChasComBrdBayStack380-24TStoreBootFW": s5ChasComBrdBayStack380_24TStoreBootFW,
       "s5ChasComBrdBayStack380-24TStoreDram": s5ChasComBrdBayStack380_24TStoreDram,
       "s5ChasComBrdTalonMDA": s5ChasComBrdTalonMDA,
       "s5ChasComBrdTalonMDA-1GT": s5ChasComBrdTalonMDA_1GT,
       "s5ChasComBrdTalonMDA-2GT": s5ChasComBrdTalonMDA_2GT,
       "s5ChasComBrdTalonMDA-2GE": s5ChasComBrdTalonMDA_2GE,
       "s5ChasComBrdTalonMDA-2GE-NO-NO": s5ChasComBrdTalonMDA_2GE_NO_NO,
       "s5ChasComBrdTalonMDA-2GE-NO-UN": s5ChasComBrdTalonMDA_2GE_NO_UN,
       "s5ChasComBrdTalonMDA-2GE-NO-SX": s5ChasComBrdTalonMDA_2GE_NO_SX,
       "s5ChasComBrdTalonMDA-2GE-NO-LX": s5ChasComBrdTalonMDA_2GE_NO_LX,
       "s5ChasComBrdTalonMDA-2GE-NO-ZX": s5ChasComBrdTalonMDA_2GE_NO_ZX,
       "s5ChasComBrdTalonMDA-2GE-NO-XD": s5ChasComBrdTalonMDA_2GE_NO_XD,
       "s5ChasComBrdTalonMDA-2GE-UN-NO": s5ChasComBrdTalonMDA_2GE_UN_NO,
       "s5ChasComBrdTalonMDA-2GE-UN-UN": s5ChasComBrdTalonMDA_2GE_UN_UN,
       "s5ChasComBrdTalonMDA-2GE-UN-SX": s5ChasComBrdTalonMDA_2GE_UN_SX,
       "s5ChasComBrdTalonMDA-2GE-UN-LX": s5ChasComBrdTalonMDA_2GE_UN_LX,
       "s5ChasComBrdTalonMDA-2GE-UN-ZX": s5ChasComBrdTalonMDA_2GE_UN_ZX,
       "s5ChasComBrdTalonMDA-2GE-UN-XD": s5ChasComBrdTalonMDA_2GE_UN_XD,
       "s5ChasComBrdTalonMDA-2GE-SX-NO": s5ChasComBrdTalonMDA_2GE_SX_NO,
       "s5ChasComBrdTalonMDA-2GE-SX-UN": s5ChasComBrdTalonMDA_2GE_SX_UN,
       "s5ChasComBrdTalonMDA-2GE-SX-SX": s5ChasComBrdTalonMDA_2GE_SX_SX,
       "s5ChasComBrdTalonMDA-2GE-SX-LX": s5ChasComBrdTalonMDA_2GE_SX_LX,
       "s5ChasComBrdTalonMDA-2GE-SX-ZX": s5ChasComBrdTalonMDA_2GE_SX_ZX,
       "s5ChasComBrdTalonMDA-2GE-SX-XD": s5ChasComBrdTalonMDA_2GE_SX_XD,
       "s5ChasComBrdTalonMDA-2GE-LX-NO": s5ChasComBrdTalonMDA_2GE_LX_NO,
       "s5ChasComBrdTalonMDA-2GE-LX-UN": s5ChasComBrdTalonMDA_2GE_LX_UN,
       "s5ChasComBrdTalonMDA-2GE-LX-SX": s5ChasComBrdTalonMDA_2GE_LX_SX,
       "s5ChasComBrdTalonMDA-2GE-LX-LX": s5ChasComBrdTalonMDA_2GE_LX_LX,
       "s5ChasComBrdTalonMDA-2GE-LX-ZX": s5ChasComBrdTalonMDA_2GE_LX_ZX,
       "s5ChasComBrdTalonMDA-2GE-LX-XD": s5ChasComBrdTalonMDA_2GE_LX_XD,
       "s5ChasComBrdTalonMDA-2GE-ZX-NO": s5ChasComBrdTalonMDA_2GE_ZX_NO,
       "s5ChasComBrdTalonMDA-2GE-ZX-UN": s5ChasComBrdTalonMDA_2GE_ZX_UN,
       "s5ChasComBrdTalonMDA-2GE-ZX-SX": s5ChasComBrdTalonMDA_2GE_ZX_SX,
       "s5ChasComBrdTalonMDA-2GE-ZX-LX": s5ChasComBrdTalonMDA_2GE_ZX_LX,
       "s5ChasComBrdTalonMDA-2GE-ZX-ZX": s5ChasComBrdTalonMDA_2GE_ZX_ZX,
       "s5ChasComBrdTalonMDA-2GE-ZX-XD": s5ChasComBrdTalonMDA_2GE_ZX_XD,
       "s5ChasComBrdTalonMDA-2GE-XD-NO": s5ChasComBrdTalonMDA_2GE_XD_NO,
       "s5ChasComBrdTalonMDA-2GE-XD-UN": s5ChasComBrdTalonMDA_2GE_XD_UN,
       "s5ChasComBrdTalonMDA-2GE-XD-SX": s5ChasComBrdTalonMDA_2GE_XD_SX,
       "s5ChasComBrdTalonMDA-2GE-XD-LX": s5ChasComBrdTalonMDA_2GE_XD_LX,
       "s5ChasComBrdTalonMDA-2GE-XD-ZX": s5ChasComBrdTalonMDA_2GE_XD_ZX,
       "s5ChasComBrdTalonMDA-2GE-XD-XD": s5ChasComBrdTalonMDA_2GE_XD_XD,
       "s5ChasComBrdBPS2000-4FX-SM": s5ChasComBrdBPS2000_4FX_SM,
       "s5ChasComBrdBayStack470-48T": s5ChasComBrdBayStack470_48T,
       "s5ChasComBrdBayStack470-48TStore": s5ChasComBrdBayStack470_48TStore,
       "s5ChasComBrdBayStack470-48TStoreFlash": s5ChasComBrdBayStack470_48TStoreFlash,
       "s5ChasComBrdBayStack470-48TStoreBootFW": s5ChasComBrdBayStack470_48TStoreBootFW,
       "s5ChasComBrdBayStack470-48TStoreDram": s5ChasComBrdBayStack470_48TStoreDram,
       "s5ChasComBrdGbic": s5ChasComBrdGbic,
       "s5ChasComBrdGbic-None": s5ChasComBrdGbic_None,
       "s5ChasComBrdGbic-Unsupported": s5ChasComBrdGbic_Unsupported,
       "s5ChasComBrdGbic-SX": s5ChasComBrdGbic_SX,
       "s5ChasComBrdGbic-LX": s5ChasComBrdGbic_LX,
       "s5ChasComBrdGbic-ZX": s5ChasComBrdGbic_ZX,
       "s5ChasComBrdGbic-XD": s5ChasComBrdGbic_XD,
       "s5ChasComBrdGbic-TX": s5ChasComBrdGbic_TX,
       "s5ChasComBrdGbic-CWDM": s5ChasComBrdGbic_CWDM,
       "s5ChasComBrdGbic-DWDM": s5ChasComBrdGbic_DWDM,
       "s5ChasComBrdGbic-10G-SR": s5ChasComBrdGbic_10G_SR,
       "s5ChasComBrdGbic-10G-LR": s5ChasComBrdGbic_10G_LR,
       "s5ChasComBrdGbic-10G-ER": s5ChasComBrdGbic_10G_ER,
       "s5ChasComBrdGbic-10G-LX4": s5ChasComBrdGbic_10G_LX4,
       "s5ChasComBrdGbic-10G-ZR": s5ChasComBrdGbic_10G_ZR,
       "s5ChasComBrdGbic-10G-LRM": s5ChasComBrdGbic_10G_LRM,
       "s5ChasComBrdGbic-T1": s5ChasComBrdGbic_T1,
       "s5ChasComBrdGbic-EX": s5ChasComBrdGbic_EX,
       "s5ChasComBrdGbic-DIRECT": s5ChasComBrdGbic_DIRECT,
       "s5ChasComBrdGbic-40G-SR4": s5ChasComBrdGbic_40G_SR4,
       "s5ChasComBrdGbic-40G-LR": s5ChasComBrdGbic_40G_LR,
       "s5ChasComBrdGbic-40G-ER": s5ChasComBrdGbic_40G_ER,
       "s5ChasComBrdMetro1450ESM-12T2GBIC": s5ChasComBrdMetro1450ESM_12T2GBIC,
       "s5ChasComBrdMetro1450ESM-12T2GBICStore": s5ChasComBrdMetro1450ESM_12T2GBICStore,
       "s5ChasComBrdMetro1450ESM-12T2GBICStoreFlash": s5ChasComBrdMetro1450ESM_12T2GBICStoreFlash,
       "s5ChasComBrdMetro1450ESM-12T2GBICStoreBootFW": s5ChasComBrdMetro1450ESM_12T2GBICStoreBootFW,
       "s5ChasComBrdMetro1450ESM-12T2GBICStoreDram": s5ChasComBrdMetro1450ESM_12T2GBICStoreDram,
       "s5ChasComBrdMetro1400ESM-12T2GBIC": s5ChasComBrdMetro1400ESM_12T2GBIC,
       "s5ChasComBrdMetro1400ESM-12T2GBICStore": s5ChasComBrdMetro1400ESM_12T2GBICStore,
       "s5ChasComBrdMetro1400ESM-12T2GBICStoreFlash": s5ChasComBrdMetro1400ESM_12T2GBICStoreFlash,
       "s5ChasComBrdMetro1400ESM-12T2GBICStoreBootFW": s5ChasComBrdMetro1400ESM_12T2GBICStoreBootFW,
       "s5ChasComBrdMetro1400ESM-12T2GBICStoreDram": s5ChasComBrdMetro1400ESM_12T2GBICStoreDram,
       "s5ChasComBrdBayStack460-24T-PWR-24T": s5ChasComBrdBayStack460_24T_PWR_24T,
       "s5ChasComBrdBayStack460-24T-PWR-24TStore": s5ChasComBrdBayStack460_24T_PWR_24TStore,
       "s5ChasComBrdBayStack460-24T-PWR-24TStoreFlash": s5ChasComBrdBayStack460_24T_PWR_24TStoreFlash,
       "s5ChasComBrdBayStack460-24T-PWR-24TStoreBootFW": s5ChasComBrdBayStack460_24T_PWR_24TStoreBootFW,
       "s5ChasComBrdBayStack460-24T-PWR-24TStoreDram": s5ChasComBrdBayStack460_24T_PWR_24TStoreDram,
       "s5ChasComBrdBayStack460-24T-PWR-24TStorePoLFlash": s5ChasComBrdBayStack460_24T_PWR_24TStorePoLFlash,
       "s5ChasComBrdBayStack380-24F": s5ChasComBrdBayStack380_24F,
       "s5ChasComBrdBayStack380-24FStore": s5ChasComBrdBayStack380_24FStore,
       "s5ChasComBrdBayStack380-24FStoreFlash": s5ChasComBrdBayStack380_24FStoreFlash,
       "s5ChasComBrdBayStack380-24FStoreBootFW": s5ChasComBrdBayStack380_24FStoreBootFW,
       "s5ChasComBrdBayStack380-24FStoreDram": s5ChasComBrdBayStack380_24FStoreDram,
       "s5ChasComBrdBayStack5510-24T": s5ChasComBrdBayStack5510_24T,
       "s5ChasComBrdBayStack5510-24TStore": s5ChasComBrdBayStack5510_24TStore,
       "s5ChasComBrdBayStack5510-24TStoreFlash": s5ChasComBrdBayStack5510_24TStoreFlash,
       "s5ChasComBrdBayStack5510-24TStoreBootFW": s5ChasComBrdBayStack5510_24TStoreBootFW,
       "s5ChasComBrdBayStack5510-24TStoreDram": s5ChasComBrdBayStack5510_24TStoreDram,
       "s5ChasComBrdBayStack5510-48T": s5ChasComBrdBayStack5510_48T,
       "s5ChasComBrdBayStack5510-48TStore": s5ChasComBrdBayStack5510_48TStore,
       "s5ChasComBrdBayStack5510-48TStoreFlash": s5ChasComBrdBayStack5510_48TStoreFlash,
       "s5ChasComBrdBayStack5510-48TStoreBootFW": s5ChasComBrdBayStack5510_48TStoreBootFW,
       "s5ChasComBrdBayStack5510-48TStoreDram": s5ChasComBrdBayStack5510_48TStoreDram,
       "s5ChasComBrdBayStack470-24T": s5ChasComBrdBayStack470_24T,
       "s5ChasComBrdBayStack470-24TStore": s5ChasComBrdBayStack470_24TStore,
       "s5ChasComBrdBayStack470-24TStoreFlash": s5ChasComBrdBayStack470_24TStoreFlash,
       "s5ChasComBrdBayStack470-24TStoreBootFW": s5ChasComBrdBayStack470_24TStoreBootFW,
       "s5ChasComBrdBayStack470-24TStoreDram": s5ChasComBrdBayStack470_24TStoreDram,
       "s5ChasComBrdWLANAccessPoint2220": s5ChasComBrdWLANAccessPoint2220,
       "s5ChasComBrdWLANAccessPoint2220Store": s5ChasComBrdWLANAccessPoint2220Store,
       "s5ChasComBrdWLANAccessPoint2220StoreFlash": s5ChasComBrdWLANAccessPoint2220StoreFlash,
       "s5ChasComBrdWLANAccessPoint2220StoreBootFW": s5ChasComBrdWLANAccessPoint2220StoreBootFW,
       "s5ChasComBrdWLANAccessPoint2220StoreDram": s5ChasComBrdWLANAccessPoint2220StoreDram,
       "s5ChasComBrdWLANSecuritySwitch2250": s5ChasComBrdWLANSecuritySwitch2250,
       "s5ChasComBrdWLANSecuritySwitch2250Store": s5ChasComBrdWLANSecuritySwitch2250Store,
       "s5ChasComBrdWLANSecuritySwitch2250StoreFlash": s5ChasComBrdWLANSecuritySwitch2250StoreFlash,
       "s5ChasComBrdWLANSecuritySwitch2250StoreBootFW": s5ChasComBrdWLANSecuritySwitch2250StoreBootFW,
       "s5ChasComBrdWLANSecuritySwitch2250StoreDram": s5ChasComBrdWLANSecuritySwitch2250StoreDram,
       "s5ChasComBrdBayStack425": s5ChasComBrdBayStack425,
       "s5ChasComBrdBayStack425Store": s5ChasComBrdBayStack425Store,
       "s5ChasComBrdBayStack425StoreFlash": s5ChasComBrdBayStack425StoreFlash,
       "s5ChasComBrdBayStack425StoreBootFW": s5ChasComBrdBayStack425StoreBootFW,
       "s5ChasComBrdBayStack425StoreDram": s5ChasComBrdBayStack425StoreDram,
       "s5ChasComBrdWLANAccessPoint2221": s5ChasComBrdWLANAccessPoint2221,
       "s5ChasComBrdWLANAccessPoint2221Store": s5ChasComBrdWLANAccessPoint2221Store,
       "s5ChasComBrdWLANAccessPoint2221StoreFlash": s5ChasComBrdWLANAccessPoint2221StoreFlash,
       "s5ChasComBrdWLANAccessPoint2221StoreBootFW": s5ChasComBrdWLANAccessPoint2221StoreBootFW,
       "s5ChasComBrdWLANAccessPoint2221StoreDram": s5ChasComBrdWLANAccessPoint2221StoreDram,
       "s5ChasComBrdBayStack5520-24T-PWR-24T": s5ChasComBrdBayStack5520_24T_PWR_24T,
       "s5ChasComBrdBayStack5520-24T-PWR-24TStore": s5ChasComBrdBayStack5520_24T_PWR_24TStore,
       "s5ChasComBrdBayStack5520-24T-PWR-24TStoreFlash": s5ChasComBrdBayStack5520_24T_PWR_24TStoreFlash,
       "s5ChasComBrdBayStack5520-24T-PWR-24TStoreBootFW": s5ChasComBrdBayStack5520_24T_PWR_24TStoreBootFW,
       "s5ChasComBrdBayStack5520-24T-PWR-24TStoreDram": s5ChasComBrdBayStack5520_24T_PWR_24TStoreDram,
       "s5ChasComBrdBayStack5520-24T-PWR-24TStorePoLFlash": s5ChasComBrdBayStack5520_24T_PWR_24TStorePoLFlash,
       "s5ChasComBrdBayStack5520-48T-PWR-48T": s5ChasComBrdBayStack5520_48T_PWR_48T,
       "s5ChasComBrdBayStack5520-48T-PWR-48TStore": s5ChasComBrdBayStack5520_48T_PWR_48TStore,
       "s5ChasComBrdBayStack5520-48T-PWR-48TStoreFlash": s5ChasComBrdBayStack5520_48T_PWR_48TStoreFlash,
       "s5ChasComBrdBayStack5520-48T-PWR-48TStoreBootFW": s5ChasComBrdBayStack5520_48T_PWR_48TStoreBootFW,
       "s5ChasComBrdBayStack5520-48T-PWR-48TStoreDram": s5ChasComBrdBayStack5520_48T_PWR_48TStoreDram,
       "s5ChasComBrdBayStack5520-48T-PWR-48TStorePoLFlash": s5ChasComBrdBayStack5520_48T_PWR_48TStorePoLFlash,
       "s5ChasComBrdBayStack425-48": s5ChasComBrdBayStack425_48,
       "s5ChasComBrdBayStack425-48Store": s5ChasComBrdBayStack425_48Store,
       "s5ChasComBrdBayStack425-48StoreFlash": s5ChasComBrdBayStack425_48StoreFlash,
       "s5ChasComBrdBayStack425-48StoreBootFW": s5ChasComBrdBayStack425_48StoreBootFW,
       "s5ChasComBrdBayStack425-48StoreDram": s5ChasComBrdBayStack425_48StoreDram,
       "s5ChasComBrdBayStack325": s5ChasComBrdBayStack325,
       "s5ChasComBrdBayStack325Store": s5ChasComBrdBayStack325Store,
       "s5ChasComBrdBayStack325StoreFlash": s5ChasComBrdBayStack325StoreFlash,
       "s5ChasComBrdBayStack325StoreBootFW": s5ChasComBrdBayStack325StoreBootFW,
       "s5ChasComBrdBayStack325StoreDram": s5ChasComBrdBayStack325StoreDram,
       "s5ChasComBrdBayStack325-24T": s5ChasComBrdBayStack325_24T,
       "s5ChasComBrdBayStack325-24G": s5ChasComBrdBayStack325_24G,
       "s5ChasComBrdWLANAccessPoint2225": s5ChasComBrdWLANAccessPoint2225,
       "s5ChasComBrdWLANAccessPoint2225Store": s5ChasComBrdWLANAccessPoint2225Store,
       "s5ChasComBrdWLANAccessPoint2225StoreFlash": s5ChasComBrdWLANAccessPoint2225StoreFlash,
       "s5ChasComBrdWLANAccessPoint2225StoreBootFW": s5ChasComBrdWLANAccessPoint2225StoreBootFW,
       "s5ChasComBrdWLANAccessPoint2225StoreDram": s5ChasComBrdWLANAccessPoint2225StoreDram,
       "s5ChasComBrdBayStack470-24T-PWR": s5ChasComBrdBayStack470_24T_PWR,
       "s5ChasComBrdBayStack470-24T-PWRStore": s5ChasComBrdBayStack470_24T_PWRStore,
       "s5ChasComBrdBayStack470-24T-PWRStoreFlash": s5ChasComBrdBayStack470_24T_PWRStoreFlash,
       "s5ChasComBrdBayStack470-24T-PWRStoreBootFW": s5ChasComBrdBayStack470_24T_PWRStoreBootFW,
       "s5ChasComBrdBayStack470-24T-PWRStoreDram": s5ChasComBrdBayStack470_24T_PWRStoreDram,
       "s5ChasComBrdBayStack470-48T-PWR": s5ChasComBrdBayStack470_48T_PWR,
       "s5ChasComBrdBayStack470-48T-PWRStore": s5ChasComBrdBayStack470_48T_PWRStore,
       "s5ChasComBrdBayStack470-48T-PWRStoreFlash": s5ChasComBrdBayStack470_48T_PWRStoreFlash,
       "s5ChasComBrdBayStack470-48T-PWRStoreBootFW": s5ChasComBrdBayStack470_48T_PWRStoreBootFW,
       "s5ChasComBrdBayStack470-48T-PWRStoreDram": s5ChasComBrdBayStack470_48T_PWRStoreDram,
       "s5ChasComBrdWLANSecuritySwitch2270": s5ChasComBrdWLANSecuritySwitch2270,
       "s5ChasComBrdWLANSecuritySwitch2270Store": s5ChasComBrdWLANSecuritySwitch2270Store,
       "s5ChasComBrdWLANSecuritySwitch2270StoreFlash": s5ChasComBrdWLANSecuritySwitch2270StoreFlash,
       "s5ChasComBrdWLANSecuritySwitch2270StoreBootFW": s5ChasComBrdWLANSecuritySwitch2270StoreBootFW,
       "s5ChasComBrdWLANSecuritySwitch2270StoreDram": s5ChasComBrdWLANSecuritySwitch2270StoreDram,
       "s5ChasComBrdEthernetRoutingSwitch5530-24TFD": s5ChasComBrdEthernetRoutingSwitch5530_24TFD,
       "s5ChasComBrdEthernetRoutingSwitch5530-24TFDStore": s5ChasComBrdEthernetRoutingSwitch5530_24TFDStore,
       "s5ChasComBrdEthernetRoutingSwitch5530-24TFDStoreFlash": s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreFlash,
       "s5ChasComBrdEthernetRoutingSwitch5530-24TFDStoreBootFW": s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreBootFW,
       "s5ChasComBrdEthernetRoutingSwitch5530-24TFDStoreDram": s5ChasComBrdEthernetRoutingSwitch5530_24TFDStoreDram,
       "s5ChasComBrdEthernetSwitch3510-24T": s5ChasComBrdEthernetSwitch3510_24T,
       "s5ChasComBrdEthernetSwitch3510-24TStore": s5ChasComBrdEthernetSwitch3510_24TStore,
       "s5ChasComBrdEthernetSwitch3510-24TStoreFlash": s5ChasComBrdEthernetSwitch3510_24TStoreFlash,
       "s5ChasComBrdEthernetSwitch3510-24TStoreBootFW": s5ChasComBrdEthernetSwitch3510_24TStoreBootFW,
       "s5ChasComBrdEthernetSwitch3510-24TStoreDram": s5ChasComBrdEthernetSwitch3510_24TStoreDram,
       "s5ChasComBrdWLANSecurityCryptographyModules": s5ChasComBrdWLANSecurityCryptographyModules,
       "s5ChasComBrdWLANSecuritySwitch2270CryptoAccelerator": s5ChasComBrdWLANSecuritySwitch2270CryptoAccelerator,
       "s5ChasComBrdBES1010-24T": s5ChasComBrdBES1010_24T,
       "s5ChasComBrdBES1010-24TStore": s5ChasComBrdBES1010_24TStore,
       "s5ChasComBrdBES1010-24TStoreFlash": s5ChasComBrdBES1010_24TStoreFlash,
       "s5ChasComBrdBES1010-24TStoreBootFW": s5ChasComBrdBES1010_24TStoreBootFW,
       "s5ChasComBrdBES1010-24TStoreDram": s5ChasComBrdBES1010_24TStoreDram,
       "s5ChasComBrdBES1010-48T": s5ChasComBrdBES1010_48T,
       "s5ChasComBrdBES1010-48TStore": s5ChasComBrdBES1010_48TStore,
       "s5ChasComBrdBES1010-48TStoreFlash": s5ChasComBrdBES1010_48TStoreFlash,
       "s5ChasComBrdBES1010-48TStoreBootFW": s5ChasComBrdBES1010_48TStoreBootFW,
       "s5ChasComBrdBES1010-48TStoreDram": s5ChasComBrdBES1010_48TStoreDram,
       "s5ChasComBrdBES1020-24T-PWR": s5ChasComBrdBES1020_24T_PWR,
       "s5ChasComBrdBES1020-24T-PWRStore": s5ChasComBrdBES1020_24T_PWRStore,
       "s5ChasComBrdBES1020-24T-PWRStoreFlash": s5ChasComBrdBES1020_24T_PWRStoreFlash,
       "s5ChasComBrdBES1020-24T-PWRStoreBootFW": s5ChasComBrdBES1020_24T_PWRStoreBootFW,
       "s5ChasComBrdBES1020-24T-PWRStoreDram": s5ChasComBrdBES1020_24T_PWRStoreDram,
       "s5ChasComBrdBES1020-24T-PWRStorePoLFlash": s5ChasComBrdBES1020_24T_PWRStorePoLFlash,
       "s5ChasComBrdBES1020-48T-PWR": s5ChasComBrdBES1020_48T_PWR,
       "s5ChasComBrdBES1020-48T-PWRStore": s5ChasComBrdBES1020_48T_PWRStore,
       "s5ChasComBrdBES1020-48T-PWRStoreFlash": s5ChasComBrdBES1020_48T_PWRStoreFlash,
       "s5ChasComBrdBES1020-48T-PWRStoreBootFW": s5ChasComBrdBES1020_48T_PWRStoreBootFW,
       "s5ChasComBrdBES1020-48T-PWRStoreDram": s5ChasComBrdBES1020_48T_PWRStoreDram,
       "s5ChasComBrdBES1020-48T-PWRStorePoLFlash": s5ChasComBrdBES1020_48T_PWRStorePoLFlash,
       "s5ChasComBrdBES2010-24T": s5ChasComBrdBES2010_24T,
       "s5ChasComBrdBES2010-24TStore": s5ChasComBrdBES2010_24TStore,
       "s5ChasComBrdBES2010-24TStoreFlash": s5ChasComBrdBES2010_24TStoreFlash,
       "s5ChasComBrdBES2010-24TStoreBootFW": s5ChasComBrdBES2010_24TStoreBootFW,
       "s5ChasComBrdBES2010-24TStoreDram": s5ChasComBrdBES2010_24TStoreDram,
       "s5ChasComBrdBES2010-48T": s5ChasComBrdBES2010_48T,
       "s5ChasComBrdBES2010-48TStore": s5ChasComBrdBES2010_48TStore,
       "s5ChasComBrdBES2010-48TStoreFlash": s5ChasComBrdBES2010_48TStoreFlash,
       "s5ChasComBrdBES2010-48TStoreBootFW": s5ChasComBrdBES2010_48TStoreBootFW,
       "s5ChasComBrdBES2010-48TStoreDram": s5ChasComBrdBES2010_48TStoreDram,
       "s5ChasComBrdBES2020-24T-PWR": s5ChasComBrdBES2020_24T_PWR,
       "s5ChasComBrdBES2020-24T-PWRStore": s5ChasComBrdBES2020_24T_PWRStore,
       "s5ChasComBrdBES2020-24T-PWRStoreFlash": s5ChasComBrdBES2020_24T_PWRStoreFlash,
       "s5ChasComBrdBES2020-24T-PWRStoreBootFW": s5ChasComBrdBES2020_24T_PWRStoreBootFW,
       "s5ChasComBrdBES2020-24T-PWRStoreDram": s5ChasComBrdBES2020_24T_PWRStoreDram,
       "s5ChasComBrdBES2020-24T-PWRStorePoLFlash": s5ChasComBrdBES2020_24T_PWRStorePoLFlash,
       "s5ChasComBrdBES2020-48T-PWR": s5ChasComBrdBES2020_48T_PWR,
       "s5ChasComBrdBES2020-48T-PWRStore": s5ChasComBrdBES2020_48T_PWRStore,
       "s5ChasComBrdBES2020-48T-PWRStoreFlash": s5ChasComBrdBES2020_48T_PWRStoreFlash,
       "s5ChasComBrdBES2020-48T-PWRStoreBootFW": s5ChasComBrdBES2020_48T_PWRStoreBootFW,
       "s5ChasComBrdBES2020-48T-PWRStoreDram": s5ChasComBrdBES2020_48T_PWRStoreDram,
       "s5ChasComBrdBES2020-48T-PWRStorePoLFlash": s5ChasComBrdBES2020_48T_PWRStorePoLFlash,
       "s5ChasComBrdBES110-24T": s5ChasComBrdBES110_24T,
       "s5ChasComBrdBES110-24TStore": s5ChasComBrdBES110_24TStore,
       "s5ChasComBrdBES110-24TStoreFlash": s5ChasComBrdBES110_24TStoreFlash,
       "s5ChasComBrdBES110-24TStoreBootFW": s5ChasComBrdBES110_24TStoreBootFW,
       "s5ChasComBrdBES110-24TStoreDram": s5ChasComBrdBES110_24TStoreDram,
       "s5ChasComBrdBES110-48T": s5ChasComBrdBES110_48T,
       "s5ChasComBrdBES110-48TStore": s5ChasComBrdBES110_48TStore,
       "s5ChasComBrdBES110-48TStoreFlash": s5ChasComBrdBES110_48TStoreFlash,
       "s5ChasComBrdBES110-48TStoreBootFW": s5ChasComBrdBES110_48TStoreBootFW,
       "s5ChasComBrdBES110-48TStoreDram": s5ChasComBrdBES110_48TStoreDram,
       "s5ChasComBrdBES120-24T-PWR": s5ChasComBrdBES120_24T_PWR,
       "s5ChasComBrdBES120-24T-PWRStore": s5ChasComBrdBES120_24T_PWRStore,
       "s5ChasComBrdBES120-24T-PWRStoreFlash": s5ChasComBrdBES120_24T_PWRStoreFlash,
       "s5ChasComBrdBES120-24T-PWRStoreBootFW": s5ChasComBrdBES120_24T_PWRStoreBootFW,
       "s5ChasComBrdBES120-24T-PWRStoreDram": s5ChasComBrdBES120_24T_PWRStoreDram,
       "s5ChasComBrdBES120-24T-PWRStorePoLFlash": s5ChasComBrdBES120_24T_PWRStorePoLFlash,
       "s5ChasComBrdBES120-48T-PWR": s5ChasComBrdBES120_48T_PWR,
       "s5ChasComBrdBES120-48T-PWRStore": s5ChasComBrdBES120_48T_PWRStore,
       "s5ChasComBrdBES120-48T-PWRStoreFlash": s5ChasComBrdBES120_48T_PWRStoreFlash,
       "s5ChasComBrdBES120-48T-PWRStoreBootFW": s5ChasComBrdBES120_48T_PWRStoreBootFW,
       "s5ChasComBrdBES120-48T-PWRStoreDram": s5ChasComBrdBES120_48T_PWRStoreDram,
       "s5ChasComBrdBES120-48T-PWRStorePoLFlash": s5ChasComBrdBES120_48T_PWRStorePoLFlash,
       "s5ChasComBrdBES210-24T": s5ChasComBrdBES210_24T,
       "s5ChasComBrdBES210-24TStore": s5ChasComBrdBES210_24TStore,
       "s5ChasComBrdBES210-24TStoreFlash": s5ChasComBrdBES210_24TStoreFlash,
       "s5ChasComBrdBES210-24TStoreBootFW": s5ChasComBrdBES210_24TStoreBootFW,
       "s5ChasComBrdBES210-24TStoreDram": s5ChasComBrdBES210_24TStoreDram,
       "s5ChasComBrdBES210-48T": s5ChasComBrdBES210_48T,
       "s5ChasComBrdBES210-48TStore": s5ChasComBrdBES210_48TStore,
       "s5ChasComBrdBES210-48TStoreFlash": s5ChasComBrdBES210_48TStoreFlash,
       "s5ChasComBrdBES210-48TStoreBootFW": s5ChasComBrdBES210_48TStoreBootFW,
       "s5ChasComBrdBES210-48TStoreDram": s5ChasComBrdBES210_48TStoreDram,
       "s5ChasComBrdBES220-24T-PWR": s5ChasComBrdBES220_24T_PWR,
       "s5ChasComBrdBES220-24T-PWRStore": s5ChasComBrdBES220_24T_PWRStore,
       "s5ChasComBrdBES220-24T-PWRStoreFlash": s5ChasComBrdBES220_24T_PWRStoreFlash,
       "s5ChasComBrdBES220-24T-PWRStoreBootFW": s5ChasComBrdBES220_24T_PWRStoreBootFW,
       "s5ChasComBrdBES220-24T-PWRStoreDram": s5ChasComBrdBES220_24T_PWRStoreDram,
       "s5ChasComBrdBES220-24T-PWRStorePoLFlash": s5ChasComBrdBES220_24T_PWRStorePoLFlash,
       "s5ChasComBrdBES220-48T-PWR": s5ChasComBrdBES220_48T_PWR,
       "s5ChasComBrdBES220-48T-PWRStore": s5ChasComBrdBES220_48T_PWRStore,
       "s5ChasComBrdBES220-48T-PWRStoreFlash": s5ChasComBrdBES220_48T_PWRStoreFlash,
       "s5ChasComBrdBES220-48T-PWRStoreBootFW": s5ChasComBrdBES220_48T_PWRStoreBootFW,
       "s5ChasComBrdBES220-48T-PWRStoreDram": s5ChasComBrdBES220_48T_PWRStoreDram,
       "s5ChasComBrdBES220-48T-PWRStorePoLFlash": s5ChasComBrdBES220_48T_PWRStorePoLFlash,
       "s5ChasComBrdERS4548GT": s5ChasComBrdERS4548GT,
       "s5ChasComBrdERS4548GTStore": s5ChasComBrdERS4548GTStore,
       "s5ChasComBrdERS4548GTStoreFlash": s5ChasComBrdERS4548GTStoreFlash,
       "s5ChasComBrdERS4548GTStoreBootFW": s5ChasComBrdERS4548GTStoreBootFW,
       "s5ChasComBrdERS4548GTStoreDram": s5ChasComBrdERS4548GTStoreDram,
       "s5ChasComBrdERS4548GTStoreSecondaryFlash": s5ChasComBrdERS4548GTStoreSecondaryFlash,
       "s5ChasComBrdERS4548GTStoreCPLD": s5ChasComBrdERS4548GTStoreCPLD,
       "s5ChasComBrdERS4548GTStoreInstalledFW": s5ChasComBrdERS4548GTStoreInstalledFW,
       "s5ChasComBrdERS4548GTStoreOperSW": s5ChasComBrdERS4548GTStoreOperSW,
       "s5ChasComBrdERS4548GTStoreTotal": s5ChasComBrdERS4548GTStoreTotal,
       "s5ChasComBrdERS4548GTStoreBootLoader": s5ChasComBrdERS4548GTStoreBootLoader,
       "s5ChasComBrdERS4548GTStoreConfig": s5ChasComBrdERS4548GTStoreConfig,
       "s5ChasComBrdERS4548GTStoreSecondaryConfig": s5ChasComBrdERS4548GTStoreSecondaryConfig,
       "s5ChasComBrdERS4548GTStoreAutoBakupConfig": s5ChasComBrdERS4548GTStoreAutoBakupConfig,
       "s5ChasComBrdERS4548GTStoreReserved": s5ChasComBrdERS4548GTStoreReserved,
       "s5ChasComBrdERS4548GT-PWR": s5ChasComBrdERS4548GT_PWR,
       "s5ChasComBrdERS4548GT-PWRStore": s5ChasComBrdERS4548GT_PWRStore,
       "s5ChasComBrdERS4548GT-PWRStoreFlash": s5ChasComBrdERS4548GT_PWRStoreFlash,
       "s5ChasComBrdERS4548GT-PWRStoreBootFW": s5ChasComBrdERS4548GT_PWRStoreBootFW,
       "s5ChasComBrdERS4548GT-PWRStoreDram": s5ChasComBrdERS4548GT_PWRStoreDram,
       "s5ChasComBrdERS4548GT-PWRStorePoLFlash": s5ChasComBrdERS4548GT_PWRStorePoLFlash,
       "s5ChasComBrdERS4548GT-PWRStoreSecondaryFlash": s5ChasComBrdERS4548GT_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS4548GT-PWRStoreCPLD": s5ChasComBrdERS4548GT_PWRStoreCPLD,
       "s5ChasComBrdERS4548GT-PWRStoreInstalledFW": s5ChasComBrdERS4548GT_PWRStoreInstalledFW,
       "s5ChasComBrdERS4548GT-PWRStoreOperSW": s5ChasComBrdERS4548GT_PWRStoreOperSW,
       "s5ChasComBrdERS4548GT-PWRStoreTotal": s5ChasComBrdERS4548GT_PWRStoreTotal,
       "s5ChasComBrdERS4548GT-PWRStoreBootLoader": s5ChasComBrdERS4548GT_PWRStoreBootLoader,
       "s5ChasComBrdERS4548GT-PWRStoreConfig": s5ChasComBrdERS4548GT_PWRStoreConfig,
       "s5ChasComBrdERS4548GT-PWRStoreSecondaryConfig": s5ChasComBrdERS4548GT_PWRStoreSecondaryConfig,
       "s5ChasComBrdERS4548GT-PWRStoreAutoBakupConfig": s5ChasComBrdERS4548GT_PWRStoreAutoBakupConfig,
       "s5ChasComBrdERS4548GT-PWRStoreReserved": s5ChasComBrdERS4548GT_PWRStoreReserved,
       "s5ChasComBrdERS4550T": s5ChasComBrdERS4550T,
       "s5ChasComBrdERS4550TStore": s5ChasComBrdERS4550TStore,
       "s5ChasComBrdERS4550TStoreFlash": s5ChasComBrdERS4550TStoreFlash,
       "s5ChasComBrdERS4550TStoreBootFW": s5ChasComBrdERS4550TStoreBootFW,
       "s5ChasComBrdERS4550TStoreDram": s5ChasComBrdERS4550TStoreDram,
       "s5ChasComBrdERS4550TStoreSecondaryFlash": s5ChasComBrdERS4550TStoreSecondaryFlash,
       "s5ChasComBrdERS4550TStoreCPLD": s5ChasComBrdERS4550TStoreCPLD,
       "s5ChasComBrdERS4550TStoreInstalledFW": s5ChasComBrdERS4550TStoreInstalledFW,
       "s5ChasComBrdERS4550TStoreOperSW": s5ChasComBrdERS4550TStoreOperSW,
       "s5ChasComBrdERS4550TStoreTotal": s5ChasComBrdERS4550TStoreTotal,
       "s5ChasComBrdERS4550TStoreBootLoader": s5ChasComBrdERS4550TStoreBootLoader,
       "s5ChasComBrdERS4550TStoreConfig": s5ChasComBrdERS4550TStoreConfig,
       "s5ChasComBrdERS4550TStoreSecondaryConfig": s5ChasComBrdERS4550TStoreSecondaryConfig,
       "s5ChasComBrdERS4550TStoreAutoBakupConfig": s5ChasComBrdERS4550TStoreAutoBakupConfig,
       "s5ChasComBrdERS4550TStoreReserved": s5ChasComBrdERS4550TStoreReserved,
       "s5ChasComBrdERS4550T-PWR": s5ChasComBrdERS4550T_PWR,
       "s5ChasComBrdERS4550T-PWRStore": s5ChasComBrdERS4550T_PWRStore,
       "s5ChasComBrdERS4550T-PWRStoreFlash": s5ChasComBrdERS4550T_PWRStoreFlash,
       "s5ChasComBrdERS4550T-PWRStoreBootFW": s5ChasComBrdERS4550T_PWRStoreBootFW,
       "s5ChasComBrdERS4550T-PWRStoreDram": s5ChasComBrdERS4550T_PWRStoreDram,
       "s5ChasComBrdERS4550T-PWRStorePoLFlash": s5ChasComBrdERS4550T_PWRStorePoLFlash,
       "s5ChasComBrdERS4550T-PWRStoreSecondaryFlash": s5ChasComBrdERS4550T_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS4550T-PWRStoreCPLD": s5ChasComBrdERS4550T_PWRStoreCPLD,
       "s5ChasComBrdERS4550T-PWRStoreInstalledFW": s5ChasComBrdERS4550T_PWRStoreInstalledFW,
       "s5ChasComBrdERS4550T-PWRStoreOperSW": s5ChasComBrdERS4550T_PWRStoreOperSW,
       "s5ChasComBrdERS4550T-PWRStoreTotal": s5ChasComBrdERS4550T_PWRStoreTotal,
       "s5ChasComBrdERS4550T-PWRStoreBootLoader": s5ChasComBrdERS4550T_PWRStoreBootLoader,
       "s5ChasComBrdERS4550T-PWRStoreConfig": s5ChasComBrdERS4550T_PWRStoreConfig,
       "s5ChasComBrdERS4550T-PWRStoreSecondaryConfig": s5ChasComBrdERS4550T_PWRStoreSecondaryConfig,
       "s5ChasComBrdERS4550T-PWRStoreAutoBakupConfig": s5ChasComBrdERS4550T_PWRStoreAutoBakupConfig,
       "s5ChasComBrdERS4550T-PWRStoreReserved": s5ChasComBrdERS4550T_PWRStoreReserved,
       "s5ChasComBrdERS4526FX": s5ChasComBrdERS4526FX,
       "s5ChasComBrdERS4526FXStore": s5ChasComBrdERS4526FXStore,
       "s5ChasComBrdERS4526FXStoreFlash": s5ChasComBrdERS4526FXStoreFlash,
       "s5ChasComBrdERS4526FXStoreBootFW": s5ChasComBrdERS4526FXStoreBootFW,
       "s5ChasComBrdERS4526FXStoreDram": s5ChasComBrdERS4526FXStoreDram,
       "s5ChasComBrdERS4526FXStoreSecondaryFlash": s5ChasComBrdERS4526FXStoreSecondaryFlash,
       "s5ChasComBrdERS4526FXStoreCPLD": s5ChasComBrdERS4526FXStoreCPLD,
       "s5ChasComBrdERS4526FXStoreInstalledFW": s5ChasComBrdERS4526FXStoreInstalledFW,
       "s5ChasComBrdERS4526FXStoreOperSW": s5ChasComBrdERS4526FXStoreOperSW,
       "s5ChasComBrdERS4526FXStoreTotal": s5ChasComBrdERS4526FXStoreTotal,
       "s5ChasComBrdERS4526FXStoreBootLoader": s5ChasComBrdERS4526FXStoreBootLoader,
       "s5ChasComBrdERS4526FXStoreConfig": s5ChasComBrdERS4526FXStoreConfig,
       "s5ChasComBrdERS4526FXStoreSecondaryConfig": s5ChasComBrdERS4526FXStoreSecondaryConfig,
       "s5ChasComBrdERS4526FXStoreAutoBakupConfig": s5ChasComBrdERS4526FXStoreAutoBakupConfig,
       "s5ChasComBrdERS4526FXStoreReserved": s5ChasComBrdERS4526FXStoreReserved,
       "s5ChasComBrdERS2500-26T": s5ChasComBrdERS2500_26T,
       "s5ChasComBrdERS2500-26TStore": s5ChasComBrdERS2500_26TStore,
       "s5ChasComBrdERS2500-26TStoreFlash": s5ChasComBrdERS2500_26TStoreFlash,
       "s5ChasComBrdERS2500-26TStoreBootFW": s5ChasComBrdERS2500_26TStoreBootFW,
       "s5ChasComBrdERS2500-26TStoreDram": s5ChasComBrdERS2500_26TStoreDram,
       "s5ChasComBrdERS2500-26TStorePoLFlash": s5ChasComBrdERS2500_26TStorePoLFlash,
       "s5ChasComBrdERS2500-26T-PWR": s5ChasComBrdERS2500_26T_PWR,
       "s5ChasComBrdERS2500-26T-PWRStore": s5ChasComBrdERS2500_26T_PWRStore,
       "s5ChasComBrdERS2500-26T-PWRStoreFlash": s5ChasComBrdERS2500_26T_PWRStoreFlash,
       "s5ChasComBrdERS2500-26T-PWRStoreBootFW": s5ChasComBrdERS2500_26T_PWRStoreBootFW,
       "s5ChasComBrdERS2500-26T-PWRStoreDram": s5ChasComBrdERS2500_26T_PWRStoreDram,
       "s5ChasComBrdERS2500-26T-PWRStorePoLFlash": s5ChasComBrdERS2500_26T_PWRStorePoLFlash,
       "s5ChasComBrdERS2500-50T": s5ChasComBrdERS2500_50T,
       "s5ChasComBrdERS2500-50TStore": s5ChasComBrdERS2500_50TStore,
       "s5ChasComBrdERS2500-50TStoreFlash": s5ChasComBrdERS2500_50TStoreFlash,
       "s5ChasComBrdERS2500-50TStoreBootFW": s5ChasComBrdERS2500_50TStoreBootFW,
       "s5ChasComBrdERS2500-50TStoreDram": s5ChasComBrdERS2500_50TStoreDram,
       "s5ChasComBrdERS2500-50TStorePoLFlash": s5ChasComBrdERS2500_50TStorePoLFlash,
       "s5ChasComBrdERS2500-50T-PWR": s5ChasComBrdERS2500_50T_PWR,
       "s5ChasComBrdERS2500-50T-PWRStore": s5ChasComBrdERS2500_50T_PWRStore,
       "s5ChasComBrdERS2500-50T-PWRStoreFlash": s5ChasComBrdERS2500_50T_PWRStoreFlash,
       "s5ChasComBrdERS2500-50T-PWRStoreBootFW": s5ChasComBrdERS2500_50T_PWRStoreBootFW,
       "s5ChasComBrdERS2500-50T-PWRStoreDram": s5ChasComBrdERS2500_50T_PWRStoreDram,
       "s5ChasComBrdERS2500-50T-PWRStorePoLFlash": s5ChasComBrdERS2500_50T_PWRStorePoLFlash,
       "s5ChasComBrdERS4526GTX-PWR": s5ChasComBrdERS4526GTX_PWR,
       "s5ChasComBrdERS4526GTX-PWRStore": s5ChasComBrdERS4526GTX_PWRStore,
       "s5ChasComBrdERS4526GTX-PWRStoreFlash": s5ChasComBrdERS4526GTX_PWRStoreFlash,
       "s5ChasComBrdERS4526GTX-PWRStoreBootFW": s5ChasComBrdERS4526GTX_PWRStoreBootFW,
       "s5ChasComBrdERS4526GTX-PWRStoreDram": s5ChasComBrdERS4526GTX_PWRStoreDram,
       "s5ChasComBrdERS4526GTX-PWRStoreSecondaryFlash": s5ChasComBrdERS4526GTX_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS4526GTX-PWRStoreCPLD": s5ChasComBrdERS4526GTX_PWRStoreCPLD,
       "s5ChasComBrdERS4526GTX-PWRStoreInstalledFW": s5ChasComBrdERS4526GTX_PWRStoreInstalledFW,
       "s5ChasComBrdERS4526GTX-PWRStoreOperSW": s5ChasComBrdERS4526GTX_PWRStoreOperSW,
       "s5ChasComBrdERS4526GTX-PWRStoreTotal": s5ChasComBrdERS4526GTX_PWRStoreTotal,
       "s5ChasComBrdERS4526GTX-PWRStoreBootLoader": s5ChasComBrdERS4526GTX_PWRStoreBootLoader,
       "s5ChasComBrdERS4526GTX-PWRStoreConfig": s5ChasComBrdERS4526GTX_PWRStoreConfig,
       "s5ChasComBrdERS4526GTX-PWRStoreSecondaryConfig": s5ChasComBrdERS4526GTX_PWRStoreSecondaryConfig,
       "s5ChasComBrdERS4526GTX-PWRStoreAutoBakupConfig": s5ChasComBrdERS4526GTX_PWRStoreAutoBakupConfig,
       "s5ChasComBrdERS4526GTX-PWRStoreReserved": s5ChasComBrdERS4526GTX_PWRStoreReserved,
       "s5ChasComBrdERS4526GTX": s5ChasComBrdERS4526GTX,
       "s5ChasComBrdERS4526GTXStore": s5ChasComBrdERS4526GTXStore,
       "s5ChasComBrdERS4526GTXStoreFlash": s5ChasComBrdERS4526GTXStoreFlash,
       "s5ChasComBrdERS4526GTXStoreBootFW": s5ChasComBrdERS4526GTXStoreBootFW,
       "s5ChasComBrdERS4526GTXStoreDram": s5ChasComBrdERS4526GTXStoreDram,
       "s5ChasComBrdERS4526GTXStoreSecondaryFlash": s5ChasComBrdERS4526GTXStoreSecondaryFlash,
       "s5ChasComBrdERS4526GTXStoreCPLD": s5ChasComBrdERS4526GTXStoreCPLD,
       "s5ChasComBrdERS4526GTXStoreInstalledFW": s5ChasComBrdERS4526GTXStoreInstalledFW,
       "s5ChasComBrdERS4526GTXStoreOperSW": s5ChasComBrdERS4526GTXStoreOperSW,
       "s5ChasComBrdERS4526GTXStoreTotal": s5ChasComBrdERS4526GTXStoreTotal,
       "s5ChasComBrdERS4526GTXStoreBootLoader": s5ChasComBrdERS4526GTXStoreBootLoader,
       "s5ChasComBrdERS4526GTXStoreConfig": s5ChasComBrdERS4526GTXStoreConfig,
       "s5ChasComBrdERS4526GTXStoreSecondaryConfig": s5ChasComBrdERS4526GTXStoreSecondaryConfig,
       "s5ChasComBrdERS4526GTXStoreAutoBakupConfig": s5ChasComBrdERS4526GTXStoreAutoBakupConfig,
       "s5ChasComBrdERS4526GTXStoreReserved": s5ChasComBrdERS4526GTXStoreReserved,
       "s5ChasComBrdERS4524GT": s5ChasComBrdERS4524GT,
       "s5ChasComBrdERS4524GTStore": s5ChasComBrdERS4524GTStore,
       "s5ChasComBrdERS4524GTStoreFlash": s5ChasComBrdERS4524GTStoreFlash,
       "s5ChasComBrdERS4524GTStoreBootFW": s5ChasComBrdERS4524GTStoreBootFW,
       "s5ChasComBrdERS4524GTStoreDram": s5ChasComBrdERS4524GTStoreDram,
       "s5ChasComBrdERS4524GTStoreSecondaryFlash": s5ChasComBrdERS4524GTStoreSecondaryFlash,
       "s5ChasComBrdERS4524GTStoreCPLD": s5ChasComBrdERS4524GTStoreCPLD,
       "s5ChasComBrdERS4524GTStoreInstalledFW": s5ChasComBrdERS4524GTStoreInstalledFW,
       "s5ChasComBrdERS4524GTStoreOperSW": s5ChasComBrdERS4524GTStoreOperSW,
       "s5ChasComBrdERS4524GTStoreTotal": s5ChasComBrdERS4524GTStoreTotal,
       "s5ChasComBrdERS4524GTStoreBootLoader": s5ChasComBrdERS4524GTStoreBootLoader,
       "s5ChasComBrdERS4524GTStoreConfig": s5ChasComBrdERS4524GTStoreConfig,
       "s5ChasComBrdERS4524GTStoreSecondaryConfig": s5ChasComBrdERS4524GTStoreSecondaryConfig,
       "s5ChasComBrdERS4524GTStoreAutoBakupConfig": s5ChasComBrdERS4524GTStoreAutoBakupConfig,
       "s5ChasComBrdERS4524GTStoreReserved": s5ChasComBrdERS4524GTStoreReserved,
       "s5ChasComBrdERS4526T": s5ChasComBrdERS4526T,
       "s5ChasComBrdERS4526TStore": s5ChasComBrdERS4526TStore,
       "s5ChasComBrdERS4526TStoreFlash": s5ChasComBrdERS4526TStoreFlash,
       "s5ChasComBrdERS4526TStoreBootFW": s5ChasComBrdERS4526TStoreBootFW,
       "s5ChasComBrdERS4526TStoreDram": s5ChasComBrdERS4526TStoreDram,
       "s5ChasComBrdERS4526TStoreSecondaryFlash": s5ChasComBrdERS4526TStoreSecondaryFlash,
       "s5ChasComBrdERS4526TStoreCPLD": s5ChasComBrdERS4526TStoreCPLD,
       "s5ChasComBrdERS4526TStoreInstalledFW": s5ChasComBrdERS4526TStoreInstalledFW,
       "s5ChasComBrdERS4526TStoreOperSW": s5ChasComBrdERS4526TStoreOperSW,
       "s5ChasComBrdERS4526TStoreTotal": s5ChasComBrdERS4526TStoreTotal,
       "s5ChasComBrdERS4526TStoreBootLoader": s5ChasComBrdERS4526TStoreBootLoader,
       "s5ChasComBrdERS4526TStoreConfig": s5ChasComBrdERS4526TStoreConfig,
       "s5ChasComBrdERS4526TStoreSecondaryConfig": s5ChasComBrdERS4526TStoreSecondaryConfig,
       "s5ChasComBrdERS4526TStoreAutoBakupConfig": s5ChasComBrdERS4526TStoreAutoBakupConfig,
       "s5ChasComBrdERS4526TStoreReserved": s5ChasComBrdERS4526TStoreReserved,
       "s5ChasComBrdERS4526T-PWR": s5ChasComBrdERS4526T_PWR,
       "s5ChasComBrdERS4526T-PWRStore": s5ChasComBrdERS4526T_PWRStore,
       "s5ChasComBrdERS4526T-PWRStoreFlash": s5ChasComBrdERS4526T_PWRStoreFlash,
       "s5ChasComBrdERS4526T-PWRStoreBootFW": s5ChasComBrdERS4526T_PWRStoreBootFW,
       "s5ChasComBrdERS4526T-PWRStoreDram": s5ChasComBrdERS4526T_PWRStoreDram,
       "s5ChasComBrdERS4526T-PWRStoreSecondaryFlash": s5ChasComBrdERS4526T_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS4526T-PWRStoreCPLD": s5ChasComBrdERS4526T_PWRStoreCPLD,
       "s5ChasComBrdERS4526T-PWRStoreInstalledFW": s5ChasComBrdERS4526T_PWRStoreInstalledFW,
       "s5ChasComBrdERS4526T-PWRStoreOperSW": s5ChasComBrdERS4526T_PWRStoreOperSW,
       "s5ChasComBrdERS4526T-PWRStoreTotal": s5ChasComBrdERS4526T_PWRStoreTotal,
       "s5ChasComBrdERS4526T-PWRStoreBootLoader": s5ChasComBrdERS4526T_PWRStoreBootLoader,
       "s5ChasComBrdERS4526T-PWRStoreConfig": s5ChasComBrdERS4526T_PWRStoreConfig,
       "s5ChasComBrdERS4526T-PWRStoreSecondaryConfig": s5ChasComBrdERS4526T_PWRStoreSecondaryConfig,
       "s5ChasComBrdERS4526T-PWRStoreAutoBakupConfig": s5ChasComBrdERS4526T_PWRStoreAutoBakupConfig,
       "s5ChasComBrdERS4526T-PWRStoreReserved": s5ChasComBrdERS4526T_PWRStoreReserved,
       "s5ChasComBrdUsb": s5ChasComBrdUsb,
       "s5ChasComBrdUsb-None": s5ChasComBrdUsb_None,
       "s5ChasComBrdUsb-Flash": s5ChasComBrdUsb_Flash,
       "s5ChasComBrdERS5698-TFD-PWR": s5ChasComBrdERS5698_TFD_PWR,
       "s5ChasComBrdERS5698-TFD-PWRStore": s5ChasComBrdERS5698_TFD_PWRStore,
       "s5ChasComBrdERS5698-TFD-PWRStoreFlash": s5ChasComBrdERS5698_TFD_PWRStoreFlash,
       "s5ChasComBrdERS5698-TFD-PWRStoreBootFW": s5ChasComBrdERS5698_TFD_PWRStoreBootFW,
       "s5ChasComBrdERS5698-TFD-PWRStoreDram": s5ChasComBrdERS5698_TFD_PWRStoreDram,
       "s5ChasComBrdERS5698-TFD-PWRStorePol": s5ChasComBrdERS5698_TFD_PWRStorePol,
       "s5ChasComBrdERS5698-TFD-PWRStoreSecondaryFlash": s5ChasComBrdERS5698_TFD_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS5698-TFD": s5ChasComBrdERS5698_TFD,
       "s5ChasComBrdERS5698-TFDStore": s5ChasComBrdERS5698_TFDStore,
       "s5ChasComBrdERS5698-TFDStoreFlash": s5ChasComBrdERS5698_TFDStoreFlash,
       "s5ChasComBrdERS5698-TFDStoreBootFW": s5ChasComBrdERS5698_TFDStoreBootFW,
       "s5ChasComBrdERS5698-TFDStoreDram": s5ChasComBrdERS5698_TFDStoreDram,
       "s5ChasComBrdERS5698-TFDStoreSecondaryFlash": s5ChasComBrdERS5698_TFDStoreSecondaryFlash,
       "s5ChasComBrdERS5650-TD-PWR": s5ChasComBrdERS5650_TD_PWR,
       "s5ChasComBrdERS5650-TD-PWRStore": s5ChasComBrdERS5650_TD_PWRStore,
       "s5ChasComBrdERS5650-TD-PWRStoreFlash": s5ChasComBrdERS5650_TD_PWRStoreFlash,
       "s5ChasComBrdERS5650-TD-PWRStoreBootFW": s5ChasComBrdERS5650_TD_PWRStoreBootFW,
       "s5ChasComBrdERS5650-TD-PWRStoreDram": s5ChasComBrdERS5650_TD_PWRStoreDram,
       "s5ChasComBrdERS5650-TD-PWRStorePol": s5ChasComBrdERS5650_TD_PWRStorePol,
       "s5ChasComBrdERS5650-TD-PWRStoreSecondaryFlash": s5ChasComBrdERS5650_TD_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS5650-TD": s5ChasComBrdERS5650_TD,
       "s5ChasComBrdERS5650-TDStore": s5ChasComBrdERS5650_TDStore,
       "s5ChasComBrdERS5650-TDStoreFlash": s5ChasComBrdERS5650_TDStoreFlash,
       "s5ChasComBrdERS5650-TDStoreBootFW": s5ChasComBrdERS5650_TDStoreBootFW,
       "s5ChasComBrdERS5650-TDStoreDram": s5ChasComBrdERS5650_TDStoreDram,
       "s5ChasComBrdERS5650-TDStoreSecondaryFlash": s5ChasComBrdERS5650_TDStoreSecondaryFlash,
       "s5ChasComBrdERS5632-FD": s5ChasComBrdERS5632_FD,
       "s5ChasComBrdERS5632-FDStore": s5ChasComBrdERS5632_FDStore,
       "s5ChasComBrdERS5632-FDStoreFlash": s5ChasComBrdERS5632_FDStoreFlash,
       "s5ChasComBrdERS5632-FDStoreBootFW": s5ChasComBrdERS5632_FDStoreBootFW,
       "s5ChasComBrdERS5632-FDStoreDram": s5ChasComBrdERS5632_FDStoreDram,
       "s5ChasComBrdERS5632-FDStoreSecondaryFlash": s5ChasComBrdERS5632_FDStoreSecondaryFlash,
       "s5ChasComBrdESU1860S": s5ChasComBrdESU1860S,
       "s5ChasComBrdESU1860SStore": s5ChasComBrdESU1860SStore,
       "s5ChasComBrdESU1860SStoreFlash": s5ChasComBrdESU1860SStoreFlash,
       "s5ChasComBrdESU1860SStoreBootFW": s5ChasComBrdESU1860SStoreBootFW,
       "s5ChasComBrdESU1860SStoreDram": s5ChasComBrdESU1860SStoreDram,
       "s5ChasComBrdESU1860SStoreSecondaryFlash": s5ChasComBrdESU1860SStoreSecondaryFlash,
       "s5ChasComBrdESU1860SStoreCpld": s5ChasComBrdESU1860SStoreCpld,
       "s5ChasComBrdESU1860B": s5ChasComBrdESU1860B,
       "s5ChasComBrdESU1860BStore": s5ChasComBrdESU1860BStore,
       "s5ChasComBrdESU1860BStoreFlash": s5ChasComBrdESU1860BStoreFlash,
       "s5ChasComBrdESU1860BStoreBootFW": s5ChasComBrdESU1860BStoreBootFW,
       "s5ChasComBrdESU1860BStoreDram": s5ChasComBrdESU1860BStoreDram,
       "s5ChasComBrdESU1860BStoreSecondaryFlash": s5ChasComBrdESU1860BStoreSecondaryFlash,
       "s5ChasComBrdESU1860BStoreCpld": s5ChasComBrdESU1860BStoreCpld,
       "s5ChasComBrdESU1860T": s5ChasComBrdESU1860T,
       "s5ChasComBrdESU1860TStore": s5ChasComBrdESU1860TStore,
       "s5ChasComBrdESU1860TStoreFlash": s5ChasComBrdESU1860TStoreFlash,
       "s5ChasComBrdESU1860TStoreBootFW": s5ChasComBrdESU1860TStoreBootFW,
       "s5ChasComBrdESU1860TStoreDram": s5ChasComBrdESU1860TStoreDram,
       "s5ChasComBrdESU1860TStoreSecondaryFlash": s5ChasComBrdESU1860TStoreSecondaryFlash,
       "s5ChasComBrdESU1860TStoreCpld": s5ChasComBrdESU1860TStoreCpld,
       "s5ChasComBrdESU1860V": s5ChasComBrdESU1860V,
       "s5ChasComBrdESU1860VStore": s5ChasComBrdESU1860VStore,
       "s5ChasComBrdESU1860VStoreFlash": s5ChasComBrdESU1860VStoreFlash,
       "s5ChasComBrdESU1860VStoreBootFW": s5ChasComBrdESU1860VStoreBootFW,
       "s5ChasComBrdESU1860VStoreDram": s5ChasComBrdESU1860VStoreDram,
       "s5ChasComBrdESU1860VStoreSecondaryFlash": s5ChasComBrdESU1860VStoreSecondaryFlash,
       "s5ChasComBrdESU1860VStoreCpld": s5ChasComBrdESU1860VStoreCpld,
       "s5ChasComBrdESU1880S": s5ChasComBrdESU1880S,
       "s5ChasComBrdESU1880SStore": s5ChasComBrdESU1880SStore,
       "s5ChasComBrdESU1880SStoreFlash": s5ChasComBrdESU1880SStoreFlash,
       "s5ChasComBrdESU1880SStoreBootFW": s5ChasComBrdESU1880SStoreBootFW,
       "s5ChasComBrdESU1880SStoreDram": s5ChasComBrdESU1880SStoreDram,
       "s5ChasComBrdESU1880SStoreSecondaryFlash": s5ChasComBrdESU1880SStoreSecondaryFlash,
       "s5ChasComBrdESU1880SStoreCpld": s5ChasComBrdESU1880SStoreCpld,
       "s5ChasComBrdESU1860-2TX-FX": s5ChasComBrdESU1860_2TX_FX,
       "s5ChasComBrdESU1880-2ST": s5ChasComBrdESU1880_2ST,
       "s5ChasComBrdESU1880-2DC": s5ChasComBrdESU1880_2DC,
       "s5ChasComBrdESU1880-2XFP": s5ChasComBrdESU1880_2XFP,
       "s5ChasComBrdERS4524GT-PWR": s5ChasComBrdERS4524GT_PWR,
       "s5ChasComBrdERS4524GT-PWRStore": s5ChasComBrdERS4524GT_PWRStore,
       "s5ChasComBrdERS4524GT-PWRStoreFlash": s5ChasComBrdERS4524GT_PWRStoreFlash,
       "s5ChasComBrdERS4524GT-PWRStoreBootFW": s5ChasComBrdERS4524GT_PWRStoreBootFW,
       "s5ChasComBrdERS4524GT-PWRStoreDram": s5ChasComBrdERS4524GT_PWRStoreDram,
       "s5ChasComBrdERS4524GT-PWRStoreSecondaryFlash": s5ChasComBrdERS4524GT_PWRStoreSecondaryFlash,
       "s5ChasComBrdERS4524GT-PWRStoreCPLD": s5ChasComBrdERS4524GT_PWRStoreCPLD,
       "s5ChasComBrdERS4524GT-PWRStoreInstalledFW": s5ChasComBrdERS4524GT_PWRStoreInstalledFW,
       "s5ChasComBrdERS4524GT-PWRStoreOperSW": s5ChasComBrdERS4524GT_PWRStoreOperSW,
       "s5ChasComBrdERS4524GT-PWRStoreTotal": s5ChasComBrdERS4524GT_PWRStoreTotal,
       "s5ChasComBrdERS4524GT-PWRStoreBootLoader": s5ChasComBrdERS4524GT_PWRStoreBootLoader,
       "s5ChasComBrdERS4524GT-PWRStoreConfig": s5ChasComBrdERS4524GT_PWRStoreConfig,
       "s5ChasComBrdERS4524GT-PWRStoreSecondaryConfig": s5ChasComBrdERS4524GT_PWRStoreSecondaryConfig,
       "s5ChasComBrdERS4524GT-PWRStoreAutoBakupConfig": s5ChasComBrdERS4524GT_PWRStoreAutoBakupConfig,
       "s5ChasComBrdERS4524GT-PWRStoreReserved": s5ChasComBrdERS4524GT_PWRStoreReserved,
       "s5ChasComBrdERS6628XSGT": s5ChasComBrdERS6628XSGT,
       "s5ChasComBrdERS6628XSGTStore": s5ChasComBrdERS6628XSGTStore,
       "s5ChasComBrdERS6628XSGTStoreFlash": s5ChasComBrdERS6628XSGTStoreFlash,
       "s5ChasComBrdERS6628XSGTStoreBootFW": s5ChasComBrdERS6628XSGTStoreBootFW,
       "s5ChasComBrdERS6628XSGTStoreDram": s5ChasComBrdERS6628XSGTStoreDram,
       "s5ChasComBrdERS6628XSGTStoreSecondaryFlash": s5ChasComBrdERS6628XSGTStoreSecondaryFlash,
       "s5ChasComBrdERS6632XTS": s5ChasComBrdERS6632XTS,
       "s5ChasComBrdERS6632XTSStore": s5ChasComBrdERS6632XTSStore,
       "s5ChasComBrdERS6632XTSStoreFlash": s5ChasComBrdERS6632XTSStoreFlash,
       "s5ChasComBrdERS6632XTSStoreBootFW": s5ChasComBrdERS6632XTSStoreBootFW,
       "s5ChasComBrdERS6632XTSStoreDram": s5ChasComBrdERS6632XTSStoreDram,
       "s5ChasComBrdERS6632XTSStoreSecondaryFlash": s5ChasComBrdERS6632XTSStoreSecondaryFlash,
       "s5ChasComBrdWC8180": s5ChasComBrdWC8180,
       "s5ChasComBrdWC8180Store": s5ChasComBrdWC8180Store,
       "s5ChasComBrdWC8180StoreFlash": s5ChasComBrdWC8180StoreFlash,
       "s5ChasComBrdWC8180StoreBootFW": s5ChasComBrdWC8180StoreBootFW,
       "s5ChasComBrdWC8180StoreDram": s5ChasComBrdWC8180StoreDram,
       "s5ChasComBrdWC8180StoreSecondaryFlash": s5ChasComBrdWC8180StoreSecondaryFlash,
       "s5ChasComBrdERS4526T-PWR-PLUS": s5ChasComBrdERS4526T_PWR_PLUS,
       "s5ChasComBrdERS4526T-PWR-PLUSStore": s5ChasComBrdERS4526T_PWR_PLUSStore,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreFlash": s5ChasComBrdERS4526T_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreBootFW": s5ChasComBrdERS4526T_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreDram": s5ChasComBrdERS4526T_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreCPLD": s5ChasComBrdERS4526T_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4526T_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreOperSW": s5ChasComBrdERS4526T_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreTotal": s5ChasComBrdERS4526T_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4526T_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreConfig": s5ChasComBrdERS4526T_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4526T_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4526T_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4526T-PWR-PLUSStoreReserved": s5ChasComBrdERS4526T_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4550T-PWR-PLUS": s5ChasComBrdERS4550T_PWR_PLUS,
       "s5ChasComBrdERS4550T-PWR-PLUSStore": s5ChasComBrdERS4550T_PWR_PLUSStore,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreFlash": s5ChasComBrdERS4550T_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreBootFW": s5ChasComBrdERS4550T_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreDram": s5ChasComBrdERS4550T_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4550T-PWR-PLUSStorePoLFlash": s5ChasComBrdERS4550T_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreCPLD": s5ChasComBrdERS4550T_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4550T_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreOperSW": s5ChasComBrdERS4550T_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreTotal": s5ChasComBrdERS4550T_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4550T_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreConfig": s5ChasComBrdERS4550T_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4550T_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4550T_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4550T-PWR-PLUSStoreReserved": s5ChasComBrdERS4550T_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4826GTS-PWR-PLUS": s5ChasComBrdERS4826GTS_PWR_PLUS,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStore": s5ChasComBrdERS4826GTS_PWR_PLUSStore,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS4826GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS4826GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreDram": s5ChasComBrdERS4826GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS4826GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4826GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS4826GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS4826GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4826GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS4826GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4826GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4826GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4826GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS4826GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4850GTS-PWR-PLUS": s5ChasComBrdERS4850GTS_PWR_PLUS,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStore": s5ChasComBrdERS4850GTS_PWR_PLUSStore,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS4850GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS4850GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreDram": s5ChasComBrdERS4850GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStorePoLFlash": s5ChasComBrdERS4850GTS_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS4850GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4850GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS4850GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS4850GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4850GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS4850GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4850GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4850GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4850GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS4850GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4826GTS": s5ChasComBrdERS4826GTS,
       "s5ChasComBrdERS4826GTSStore": s5ChasComBrdERS4826GTSStore,
       "s5ChasComBrdERS4826GTSStoreFlash": s5ChasComBrdERS4826GTSStoreFlash,
       "s5ChasComBrdERS4826GTSStoreBootFW": s5ChasComBrdERS4826GTSStoreBootFW,
       "s5ChasComBrdERS4826GTSStoreDram": s5ChasComBrdERS4826GTSStoreDram,
       "s5ChasComBrdERS4826GTSStoreSecondaryFlash": s5ChasComBrdERS4826GTSStoreSecondaryFlash,
       "s5ChasComBrdERS4826GTSStoreCPLD": s5ChasComBrdERS4826GTSStoreCPLD,
       "s5ChasComBrdERS4826GTSStoreInstalledFW": s5ChasComBrdERS4826GTSStoreInstalledFW,
       "s5ChasComBrdERS4826GTSStoreOperSW": s5ChasComBrdERS4826GTSStoreOperSW,
       "s5ChasComBrdERS4826GTSStoreTotal": s5ChasComBrdERS4826GTSStoreTotal,
       "s5ChasComBrdERS4826GTSStoreBootLoader": s5ChasComBrdERS4826GTSStoreBootLoader,
       "s5ChasComBrdERS4826GTSStoreConfig": s5ChasComBrdERS4826GTSStoreConfig,
       "s5ChasComBrdERS4826GTSStoreSecondaryConfig": s5ChasComBrdERS4826GTSStoreSecondaryConfig,
       "s5ChasComBrdERS4826GTSStoreAutoBakupConfig": s5ChasComBrdERS4826GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS4826GTSStoreReserved": s5ChasComBrdERS4826GTSStoreReserved,
       "s5ChasComBrdERS4850GTS": s5ChasComBrdERS4850GTS,
       "s5ChasComBrdERS4850GTSStore": s5ChasComBrdERS4850GTSStore,
       "s5ChasComBrdERS4850GTSStoreFlash": s5ChasComBrdERS4850GTSStoreFlash,
       "s5ChasComBrdERS4850GTSStoreBootFW": s5ChasComBrdERS4850GTSStoreBootFW,
       "s5ChasComBrdERS4850GTSStoreDram": s5ChasComBrdERS4850GTSStoreDram,
       "s5ChasComBrdERS4850GTSStorePoLFlash": s5ChasComBrdERS4850GTSStorePoLFlash,
       "s5ChasComBrdERS4850GTSStoreSecondaryFlash": s5ChasComBrdERS4850GTSStoreSecondaryFlash,
       "s5ChasComBrdERS4850GTSStoreCPLD": s5ChasComBrdERS4850GTSStoreCPLD,
       "s5ChasComBrdERS4850GTSStoreInstalledFW": s5ChasComBrdERS4850GTSStoreInstalledFW,
       "s5ChasComBrdERS4850GTSStoreOperSW": s5ChasComBrdERS4850GTSStoreOperSW,
       "s5ChasComBrdERS4850GTSStoreTotal": s5ChasComBrdERS4850GTSStoreTotal,
       "s5ChasComBrdERS4850GTSStoreBootLoader": s5ChasComBrdERS4850GTSStoreBootLoader,
       "s5ChasComBrdERS4850GTSStoreConfig": s5ChasComBrdERS4850GTSStoreConfig,
       "s5ChasComBrdERS4850GTSStoreSecondaryConfig": s5ChasComBrdERS4850GTSStoreSecondaryConfig,
       "s5ChasComBrdERS4850GTSStoreAutoBakupConfig": s5ChasComBrdERS4850GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS4850GTSStoreReserved": s5ChasComBrdERS4850GTSStoreReserved,
       "s5ChasComBrdVSP7024XLS": s5ChasComBrdVSP7024XLS,
       "s5ChasComBrdVSP7024XLSStore": s5ChasComBrdVSP7024XLSStore,
       "s5ChasComBrdVSP7024XLSStoreFlash": s5ChasComBrdVSP7024XLSStoreFlash,
       "s5ChasComBrdVSP7024XLSStoreBootFW": s5ChasComBrdVSP7024XLSStoreBootFW,
       "s5ChasComBrdVSP7024XLSStoreDram": s5ChasComBrdVSP7024XLSStoreDram,
       "s5ChasComBrdVSP7024XLSStorePoLFlash": s5ChasComBrdVSP7024XLSStorePoLFlash,
       "s5ChasComBrdVSP7024XLSStoreSecondaryFlash": s5ChasComBrdVSP7024XLSStoreSecondaryFlash,
       "s5ChasComBrdVSP7024XLSStoreCPLD": s5ChasComBrdVSP7024XLSStoreCPLD,
       "s5ChasComBrdVSP7024XLSStoreInstalledFW": s5ChasComBrdVSP7024XLSStoreInstalledFW,
       "s5ChasComBrdVSP7024XLSStoreOperSW": s5ChasComBrdVSP7024XLSStoreOperSW,
       "s5ChasComBrdVSP7024XLSStoreTotal": s5ChasComBrdVSP7024XLSStoreTotal,
       "s5ChasComBrdVSP7024XLSStoreBootLoader": s5ChasComBrdVSP7024XLSStoreBootLoader,
       "s5ChasComBrdVSP7024XLSStoreConfig": s5ChasComBrdVSP7024XLSStoreConfig,
       "s5ChasComBrdVSP7024XLSStoreSecondaryConfig": s5ChasComBrdVSP7024XLSStoreSecondaryConfig,
       "s5ChasComBrdVSP7024XLSStoreAutoBakupConfig": s5ChasComBrdVSP7024XLSStoreAutoBakupConfig,
       "s5ChasComBrdVSP7024XLSStoreReserved": s5ChasComBrdVSP7024XLSStoreReserved,
       "s5ChasComBrdVSP7024XLS-7008XLS": s5ChasComBrdVSP7024XLS_7008XLS,
       "s5ChasComBrdVSP7024XLS-7008XLT": s5ChasComBrdVSP7024XLS_7008XLT,
       "s5ChasComBrdERS3510GT": s5ChasComBrdERS3510GT,
       "s5ChasComBrdERS3510GTStore": s5ChasComBrdERS3510GTStore,
       "s5ChasComBrdERS3510GTStoreFlash": s5ChasComBrdERS3510GTStoreFlash,
       "s5ChasComBrdERS3510GTStoreBootFW": s5ChasComBrdERS3510GTStoreBootFW,
       "s5ChasComBrdERS3510GTStoreDram": s5ChasComBrdERS3510GTStoreDram,
       "s5ChasComBrdERS3510GTStorePoLFlash": s5ChasComBrdERS3510GTStorePoLFlash,
       "s5ChasComBrdERS3510GT-PWR-PLUS": s5ChasComBrdERS3510GT_PWR_PLUS,
       "s5ChasComBrdERS3510GT-PWR-PLUSStore": s5ChasComBrdERS3510GT_PWR_PLUSStore,
       "s5ChasComBrdERS3510GT-PWR-PLUSStoreFlash": s5ChasComBrdERS3510GT_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3510GT-PWR-PLUSStoreBootFW": s5ChasComBrdERS3510GT_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3510GT-PWR-PLUSStoreDram": s5ChasComBrdERS3510GT_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3510GT-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3510GT_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS3524GT": s5ChasComBrdERS3524GT,
       "s5ChasComBrdERS3524GTStore": s5ChasComBrdERS3524GTStore,
       "s5ChasComBrdERS3524GTStoreFlash": s5ChasComBrdERS3524GTStoreFlash,
       "s5ChasComBrdERS3524GTStoreBootFW": s5ChasComBrdERS3524GTStoreBootFW,
       "s5ChasComBrdERS3524GTStoreDram": s5ChasComBrdERS3524GTStoreDram,
       "s5ChasComBrdERS3524GTStorePoLFlash": s5ChasComBrdERS3524GTStorePoLFlash,
       "s5ChasComBrdERS3524GT-PWR-PLUS": s5ChasComBrdERS3524GT_PWR_PLUS,
       "s5ChasComBrdERS3524GT-PWR-PLUSStore": s5ChasComBrdERS3524GT_PWR_PLUSStore,
       "s5ChasComBrdERS3524GT-PWR-PLUSStoreFlash": s5ChasComBrdERS3524GT_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3524GT-PWR-PLUSStoreBootFW": s5ChasComBrdERS3524GT_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3524GT-PWR-PLUSStoreDram": s5ChasComBrdERS3524GT_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3524GT-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3524GT_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS3526GT": s5ChasComBrdERS3526GT,
       "s5ChasComBrdERS3526GTStore": s5ChasComBrdERS3526GTStore,
       "s5ChasComBrdERS3526GTStoreFlash": s5ChasComBrdERS3526GTStoreFlash,
       "s5ChasComBrdERS3526GTStoreBootFW": s5ChasComBrdERS3526GTStoreBootFW,
       "s5ChasComBrdERS3526GTStoreDram": s5ChasComBrdERS3526GTStoreDram,
       "s5ChasComBrdERS3526GTStorePoLFlash": s5ChasComBrdERS3526GTStorePoLFlash,
       "s5ChasComBrdERS3526GT-PWR-PLUS": s5ChasComBrdERS3526GT_PWR_PLUS,
       "s5ChasComBrdERS3526GT-PWR-PLUSStore": s5ChasComBrdERS3526GT_PWR_PLUSStore,
       "s5ChasComBrdERS3526GT-PWR-PLUSStoreFlash": s5ChasComBrdERS3526GT_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3526GT-PWR-PLUSStoreBootFW": s5ChasComBrdERS3526GT_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3526GT-PWR-PLUSStoreDram": s5ChasComBrdERS3526GT_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3526GT-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3526GT_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS3526T": s5ChasComBrdERS3526T,
       "s5ChasComBrdERS3526TStore": s5ChasComBrdERS3526TStore,
       "s5ChasComBrdERS3526TStoreFlash": s5ChasComBrdERS3526TStoreFlash,
       "s5ChasComBrdERS3526TStoreBootFW": s5ChasComBrdERS3526TStoreBootFW,
       "s5ChasComBrdERS3526TStoreDram": s5ChasComBrdERS3526TStoreDram,
       "s5ChasComBrdERS3526TStorePoLFlash": s5ChasComBrdERS3526TStorePoLFlash,
       "s5ChasComBrdERS3526T-PWR-PLUS": s5ChasComBrdERS3526T_PWR_PLUS,
       "s5ChasComBrdERS3526T-PWR-PLUSStore": s5ChasComBrdERS3526T_PWR_PLUSStore,
       "s5ChasComBrdERS3526T-PWR-PLUSStoreFlash": s5ChasComBrdERS3526T_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3526T-PWR-PLUSStoreBootFW": s5ChasComBrdERS3526T_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3526T-PWR-PLUSStoreDram": s5ChasComBrdERS3526T_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3526T-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3526T_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS3549GTS": s5ChasComBrdERS3549GTS,
       "s5ChasComBrdERS3549GTSStore": s5ChasComBrdERS3549GTSStore,
       "s5ChasComBrdERS3549GTSStoreFlash": s5ChasComBrdERS3549GTSStoreFlash,
       "s5ChasComBrdERS3549GTSStoreBootFW": s5ChasComBrdERS3549GTSStoreBootFW,
       "s5ChasComBrdERS3549GTSStoreDram": s5ChasComBrdERS3549GTSStoreDram,
       "s5ChasComBrdERS3549GTSStorePoLFlash": s5ChasComBrdERS3549GTSStorePoLFlash,
       "s5ChasComBrdERS3549GTS-PWR-PLUS": s5ChasComBrdERS3549GTS_PWR_PLUS,
       "s5ChasComBrdERS3549GTS-PWR-PLUSStore": s5ChasComBrdERS3549GTS_PWR_PLUSStore,
       "s5ChasComBrdERS3549GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS3549GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3549GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS3549GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3549GTS-PWR-PLUSStoreDram": s5ChasComBrdERS3549GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3549GTS-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3549GTS_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdVSP7000MDA": s5ChasComBrdVSP7000MDA,
       "s5ChasComBrdVSP7000MDA-7008XLS": s5ChasComBrdVSP7000MDA_7008XLS,
       "s5ChasComBrdVSP7000MDA-7008XT": s5ChasComBrdVSP7000MDA_7008XT,
       "s5ChasComBrdVSP7000MDA-7002QQ": s5ChasComBrdVSP7000MDA_7002QQ,
       "s5ChasComBrdVSP7024XT": s5ChasComBrdVSP7024XT,
       "s5ChasComBrdVSP7024XTStore": s5ChasComBrdVSP7024XTStore,
       "s5ChasComBrdVSP7024XTStoreFlash": s5ChasComBrdVSP7024XTStoreFlash,
       "s5ChasComBrdVSP7024XTStoreBootFW": s5ChasComBrdVSP7024XTStoreBootFW,
       "s5ChasComBrdVSP7024XTStoreDram": s5ChasComBrdVSP7024XTStoreDram,
       "s5ChasComBrdVSP7024XTStorePoLFlash": s5ChasComBrdVSP7024XTStorePoLFlash,
       "s5ChasComBrdVSP7024XTStoreSecondaryFlash": s5ChasComBrdVSP7024XTStoreSecondaryFlash,
       "s5ChasComBrdVSP7024XTStoreCPLD": s5ChasComBrdVSP7024XTStoreCPLD,
       "s5ChasComBrdVSP7024XTStoreInstalledFW": s5ChasComBrdVSP7024XTStoreInstalledFW,
       "s5ChasComBrdVSP7024XTStoreOperSW": s5ChasComBrdVSP7024XTStoreOperSW,
       "s5ChasComBrdVSP7024XTStoreTotal": s5ChasComBrdVSP7024XTStoreTotal,
       "s5ChasComBrdVSP7024XTStoreBootLoader": s5ChasComBrdVSP7024XTStoreBootLoader,
       "s5ChasComBrdVSP7024XTStoreConfig": s5ChasComBrdVSP7024XTStoreConfig,
       "s5ChasComBrdVSP7024XTStoreSecondaryConfig": s5ChasComBrdVSP7024XTStoreSecondaryConfig,
       "s5ChasComBrdVSP7024XTStoreAutoBakupConfig": s5ChasComBrdVSP7024XTStoreAutoBakupConfig,
       "s5ChasComBrdVSP7024XTStoreReserved": s5ChasComBrdVSP7024XTStoreReserved,
       "s5ChasComBrdERS5928GTS": s5ChasComBrdERS5928GTS,
       "s5ChasComBrdERS5928GTSStore": s5ChasComBrdERS5928GTSStore,
       "s5ChasComBrdERS5928GTSStoreFlash": s5ChasComBrdERS5928GTSStoreFlash,
       "s5ChasComBrdERS5928GTSStoreBootFW": s5ChasComBrdERS5928GTSStoreBootFW,
       "s5ChasComBrdERS5928GTSStoreDram": s5ChasComBrdERS5928GTSStoreDram,
       "s5ChasComBrdERS5928GTSStoreSecondaryFlash": s5ChasComBrdERS5928GTSStoreSecondaryFlash,
       "s5ChasComBrdERS5928GTSStoreCPLD": s5ChasComBrdERS5928GTSStoreCPLD,
       "s5ChasComBrdERS5928GTSStoreInstalledFW": s5ChasComBrdERS5928GTSStoreInstalledFW,
       "s5ChasComBrdERS5928GTSStoreOperSW": s5ChasComBrdERS5928GTSStoreOperSW,
       "s5ChasComBrdERS5928GTSStoreTotal": s5ChasComBrdERS5928GTSStoreTotal,
       "s5ChasComBrdERS5928GTSStoreBootLoader": s5ChasComBrdERS5928GTSStoreBootLoader,
       "s5ChasComBrdERS5928GTSStoreConfig": s5ChasComBrdERS5928GTSStoreConfig,
       "s5ChasComBrdERS5928GTSStoreSecondaryConfig": s5ChasComBrdERS5928GTSStoreSecondaryConfig,
       "s5ChasComBrdERS5928GTSStoreAutoBakupConfig": s5ChasComBrdERS5928GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS5928GTSStoreReserved": s5ChasComBrdERS5928GTSStoreReserved,
       "s5ChasComBrdERS5928GTS-PWR-PLUS": s5ChasComBrdERS5928GTS_PWR_PLUS,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStore": s5ChasComBrdERS5928GTS_PWR_PLUSStore,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS5928GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS5928GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreDram": s5ChasComBrdERS5928GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS5928GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS5928GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS5928GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS5928GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS5928GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS5928GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS5928GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS5928GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS5928GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS5928GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS5952GTS": s5ChasComBrdERS5952GTS,
       "s5ChasComBrdERS5952GTSStore": s5ChasComBrdERS5952GTSStore,
       "s5ChasComBrdERS5952GTSStoreFlash": s5ChasComBrdERS5952GTSStoreFlash,
       "s5ChasComBrdERS5952GTSStoreBootFW": s5ChasComBrdERS5952GTSStoreBootFW,
       "s5ChasComBrdERS5952GTSStoreDram": s5ChasComBrdERS5952GTSStoreDram,
       "s5ChasComBrdERS5952GTSStoreSecondaryFlash": s5ChasComBrdERS5952GTSStoreSecondaryFlash,
       "s5ChasComBrdERS5952GTSStoreCPLD": s5ChasComBrdERS5952GTSStoreCPLD,
       "s5ChasComBrdERS5952GTSStoreInstalledFW": s5ChasComBrdERS5952GTSStoreInstalledFW,
       "s5ChasComBrdERS5952GTSStoreOperSW": s5ChasComBrdERS5952GTSStoreOperSW,
       "s5ChasComBrdERS5952GTSStoreTotal": s5ChasComBrdERS5952GTSStoreTotal,
       "s5ChasComBrdERS5952GTSStoreBootLoader": s5ChasComBrdERS5952GTSStoreBootLoader,
       "s5ChasComBrdERS5952GTSStoreConfig": s5ChasComBrdERS5952GTSStoreConfig,
       "s5ChasComBrdERS5952GTSStoreSecondaryConfig": s5ChasComBrdERS5952GTSStoreSecondaryConfig,
       "s5ChasComBrdERS5952GTSStoreAutoBakupConfig": s5ChasComBrdERS5952GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS5952GTSStoreReserved": s5ChasComBrdERS5952GTSStoreReserved,
       "s5ChasComBrdERS5952GTS-PWR-PLUS": s5ChasComBrdERS5952GTS_PWR_PLUS,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStore": s5ChasComBrdERS5952GTS_PWR_PLUSStore,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS5952GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS5952GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreDram": s5ChasComBrdERS5952GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS5952GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS5952GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS5952GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS5952GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS5952GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS5952GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS5952GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS5952GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS5952GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS5952GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS5928GTS-UPWR": s5ChasComBrdERS5928GTS_UPWR,
       "s5ChasComBrdERS5928GTS-UPWRStore": s5ChasComBrdERS5928GTS_UPWRStore,
       "s5ChasComBrdERS5928GTS-UPWRStoreFlash": s5ChasComBrdERS5928GTS_UPWRStoreFlash,
       "s5ChasComBrdERS5928GTS-UPWRStoreBootFW": s5ChasComBrdERS5928GTS_UPWRStoreBootFW,
       "s5ChasComBrdERS5928GTS-UPWRStoreDram": s5ChasComBrdERS5928GTS_UPWRStoreDram,
       "s5ChasComBrdERS5928GTS-UPWRStoreSecondaryFlash": s5ChasComBrdERS5928GTS_UPWRStoreSecondaryFlash,
       "s5ChasComBrdERS5928GTS-UPWRStoreCPLD": s5ChasComBrdERS5928GTS_UPWRStoreCPLD,
       "s5ChasComBrdERS5928GTS-UPWRStoreInstalledFW": s5ChasComBrdERS5928GTS_UPWRStoreInstalledFW,
       "s5ChasComBrdERS5928GTS-UPWRStoreOperSW": s5ChasComBrdERS5928GTS_UPWRStoreOperSW,
       "s5ChasComBrdERS5928GTS-UPWRStoreTotal": s5ChasComBrdERS5928GTS_UPWRStoreTotal,
       "s5ChasComBrdERS5928GTS-UPWRStoreBootLoader": s5ChasComBrdERS5928GTS_UPWRStoreBootLoader,
       "s5ChasComBrdERS5928GTS-UPWRStoreConfig": s5ChasComBrdERS5928GTS_UPWRStoreConfig,
       "s5ChasComBrdERS5928GTS-UPWRStoreSecondaryConfig": s5ChasComBrdERS5928GTS_UPWRStoreSecondaryConfig,
       "s5ChasComBrdERS5928GTS-UPWRStoreAutoBakupConfig": s5ChasComBrdERS5928GTS_UPWRStoreAutoBakupConfig,
       "s5ChasComBrdERS5928GTS-UPWRStoreReserved": s5ChasComBrdERS5928GTS_UPWRStoreReserved,
       "s5ChasComBrdERS59100GTS": s5ChasComBrdERS59100GTS,
       "s5ChasComBrdERS59100GTSStore": s5ChasComBrdERS59100GTSStore,
       "s5ChasComBrdERS59100GTSStoreFlash": s5ChasComBrdERS59100GTSStoreFlash,
       "s5ChasComBrdERS59100GTSStoreBootFW": s5ChasComBrdERS59100GTSStoreBootFW,
       "s5ChasComBrdERS59100GTSStoreDram": s5ChasComBrdERS59100GTSStoreDram,
       "s5ChasComBrdERS59100GTSStoreSecondaryFlash": s5ChasComBrdERS59100GTSStoreSecondaryFlash,
       "s5ChasComBrdERS59100GTSStoreCPLD": s5ChasComBrdERS59100GTSStoreCPLD,
       "s5ChasComBrdERS59100GTSStoreInstalledFW": s5ChasComBrdERS59100GTSStoreInstalledFW,
       "s5ChasComBrdERS59100GTSStoreOperSW": s5ChasComBrdERS59100GTSStoreOperSW,
       "s5ChasComBrdERS59100GTSStoreTotal": s5ChasComBrdERS59100GTSStoreTotal,
       "s5ChasComBrdERS59100GTSStoreBootLoader": s5ChasComBrdERS59100GTSStoreBootLoader,
       "s5ChasComBrdERS59100GTSStoreConfig": s5ChasComBrdERS59100GTSStoreConfig,
       "s5ChasComBrdERS59100GTSStoreSecondaryConfig": s5ChasComBrdERS59100GTSStoreSecondaryConfig,
       "s5ChasComBrdERS59100GTSStoreAutoBakupConfig": s5ChasComBrdERS59100GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS59100GTSStoreReserved": s5ChasComBrdERS59100GTSStoreReserved,
       "s5ChasComBrdERS59100GTS-PWR-PLUS": s5ChasComBrdERS59100GTS_PWR_PLUS,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStore": s5ChasComBrdERS59100GTS_PWR_PLUSStore,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS59100GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS59100GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreDram": s5ChasComBrdERS59100GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS59100GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS59100GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS59100GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS59100GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS59100GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS59100GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS59100GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS59100GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS59100GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS59100GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4926GTS": s5ChasComBrdERS4926GTS,
       "s5ChasComBrdERS4926GTSStore": s5ChasComBrdERS4926GTSStore,
       "s5ChasComBrdERS4926GTSStoreFlash": s5ChasComBrdERS4926GTSStoreFlash,
       "s5ChasComBrdERS4926GTSStoreBootFW": s5ChasComBrdERS4926GTSStoreBootFW,
       "s5ChasComBrdERS4926GTSStoreDram": s5ChasComBrdERS4926GTSStoreDram,
       "s5ChasComBrdERS4926GTSStoreSecondaryFlash": s5ChasComBrdERS4926GTSStoreSecondaryFlash,
       "s5ChasComBrdERS4926GTSStoreCPLD": s5ChasComBrdERS4926GTSStoreCPLD,
       "s5ChasComBrdERS4926GTSStoreInstalledFW": s5ChasComBrdERS4926GTSStoreInstalledFW,
       "s5ChasComBrdERS4926GTSStoreOperSW": s5ChasComBrdERS4926GTSStoreOperSW,
       "s5ChasComBrdERS4926GTSStoreTotal": s5ChasComBrdERS4926GTSStoreTotal,
       "s5ChasComBrdERS4926GTSStoreBootLoader": s5ChasComBrdERS4926GTSStoreBootLoader,
       "s5ChasComBrdERS4926GTSStoreConfig": s5ChasComBrdERS4926GTSStoreConfig,
       "s5ChasComBrdERS4926GTSStoreSecondaryConfig": s5ChasComBrdERS4926GTSStoreSecondaryConfig,
       "s5ChasComBrdERS4926GTSStoreAutoBakupConfig": s5ChasComBrdERS4926GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS4926GTSStoreReserved": s5ChasComBrdERS4926GTSStoreReserved,
       "s5ChasComBrdERS4926GTS-PWR-PLUS": s5ChasComBrdERS4926GTS_PWR_PLUS,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStore": s5ChasComBrdERS4926GTS_PWR_PLUSStore,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS4926GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS4926GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreDram": s5ChasComBrdERS4926GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS4926GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4926GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS4926GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS4926GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4926GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS4926GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4926GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4926GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4926GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS4926GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS4950GTS": s5ChasComBrdERS4950GTS,
       "s5ChasComBrdERS4950GTSStore": s5ChasComBrdERS4950GTSStore,
       "s5ChasComBrdERS4950GTSStoreFlash": s5ChasComBrdERS4950GTSStoreFlash,
       "s5ChasComBrdERS4950GTSStoreBootFW": s5ChasComBrdERS4950GTSStoreBootFW,
       "s5ChasComBrdERS4950GTSStoreDram": s5ChasComBrdERS4950GTSStoreDram,
       "s5ChasComBrdERS4950GTSStorePoLFlash": s5ChasComBrdERS4950GTSStorePoLFlash,
       "s5ChasComBrdERS4950GTSStoreSecondaryFlash": s5ChasComBrdERS4950GTSStoreSecondaryFlash,
       "s5ChasComBrdERS4950GTSStoreCPLD": s5ChasComBrdERS4950GTSStoreCPLD,
       "s5ChasComBrdERS4950GTSStoreInstalledFW": s5ChasComBrdERS4950GTSStoreInstalledFW,
       "s5ChasComBrdERS4950GTSStoreOperSW": s5ChasComBrdERS4950GTSStoreOperSW,
       "s5ChasComBrdERS4950GTSStoreTotal": s5ChasComBrdERS4950GTSStoreTotal,
       "s5ChasComBrdERS4950GTSStoreBootLoader": s5ChasComBrdERS4950GTSStoreBootLoader,
       "s5ChasComBrdERS4950GTSStoreConfig": s5ChasComBrdERS4950GTSStoreConfig,
       "s5ChasComBrdERS4950GTSStoreSecondaryConfig": s5ChasComBrdERS4950GTSStoreSecondaryConfig,
       "s5ChasComBrdERS4950GTSStoreAutoBakupConfig": s5ChasComBrdERS4950GTSStoreAutoBakupConfig,
       "s5ChasComBrdERS4950GTSStoreReserved": s5ChasComBrdERS4950GTSStoreReserved,
       "s5ChasComBrdERS4950GTS-PWR-PLUS": s5ChasComBrdERS4950GTS_PWR_PLUS,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStore": s5ChasComBrdERS4950GTS_PWR_PLUSStore,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreFlash": s5ChasComBrdERS4950GTS_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreBootFW": s5ChasComBrdERS4950GTS_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreDram": s5ChasComBrdERS4950GTS_PWR_PLUSStoreDram,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStorePoLFlash": s5ChasComBrdERS4950GTS_PWR_PLUSStorePoLFlash,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreSecondaryFlash": s5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryFlash,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreCPLD": s5ChasComBrdERS4950GTS_PWR_PLUSStoreCPLD,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreInstalledFW": s5ChasComBrdERS4950GTS_PWR_PLUSStoreInstalledFW,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreOperSW": s5ChasComBrdERS4950GTS_PWR_PLUSStoreOperSW,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreTotal": s5ChasComBrdERS4950GTS_PWR_PLUSStoreTotal,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreBootLoader": s5ChasComBrdERS4950GTS_PWR_PLUSStoreBootLoader,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreConfig": s5ChasComBrdERS4950GTS_PWR_PLUSStoreConfig,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreSecondaryConfig": s5ChasComBrdERS4950GTS_PWR_PLUSStoreSecondaryConfig,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreAutoBakupConfig": s5ChasComBrdERS4950GTS_PWR_PLUSStoreAutoBakupConfig,
       "s5ChasComBrdERS4950GTS-PWR-PLUSStoreReserved": s5ChasComBrdERS4950GTS_PWR_PLUSStoreReserved,
       "s5ChasComBrdERS3550T": s5ChasComBrdERS3550T,
       "s5ChasComBrdERS3550TStore": s5ChasComBrdERS3550TStore,
       "s5ChasComBrdERS3550TStoreFlash": s5ChasComBrdERS3550TStoreFlash,
       "s5ChasComBrdERS3550TStoreBootFW": s5ChasComBrdERS3550TStoreBootFW,
       "s5ChasComBrdERS3550TStoreDram": s5ChasComBrdERS3550TStoreDram,
       "s5ChasComBrdERS3550TStorePoLFlash": s5ChasComBrdERS3550TStorePoLFlash,
       "s5ChasComBrdERS3550T-PWR-PLUS": s5ChasComBrdERS3550T_PWR_PLUS,
       "s5ChasComBrdERS3550T-PWR-PLUSStore": s5ChasComBrdERS3550T_PWR_PLUSStore,
       "s5ChasComBrdERS3550T-PWR-PLUSStoreFlash": s5ChasComBrdERS3550T_PWR_PLUSStoreFlash,
       "s5ChasComBrdERS3550T-PWR-PLUSStoreBootFW": s5ChasComBrdERS3550T_PWR_PLUSStoreBootFW,
       "s5ChasComBrdERS3550T-PWR-PLUSStoreDram": s5ChasComBrdERS3550T_PWR_PLUSStoreDram,
       "s5ChasComBrdERS3550T-PWR-PLUSStorePoLFlash": s5ChasComBrdERS3550T_PWR_PLUSStorePoLFlash,
       "s5ChasComMBkpl": s5ChasComMBkpl,
       "s5ChasComM5000Bkpl": s5ChasComM5000Bkpl,
       "s5ChasComM5000BkplLow": s5ChasComM5000BkplLow,
       "s5ChasComM5000BkplLowCmbEthTok": s5ChasComM5000BkplLowCmbEthTok,
       "s5ChasComM5000BkplLowCmbEth": s5ChasComM5000BkplLowCmbEth,
       "s5ChasComM5000BkplMidLeft": s5ChasComM5000BkplMidLeft,
       "s5ChasComM5000BkplMidLeftFddiFull": s5ChasComM5000BkplMidLeftFddiFull,
       "s5ChasComM5000BkplMidLeftEth100MbsFull": s5ChasComM5000BkplMidLeftEth100MbsFull,
       "s5ChasComM5000BkplMidLeftEth100Mbs": s5ChasComM5000BkplMidLeftEth100Mbs,
       "s5ChasComM5000BkplMidRight": s5ChasComM5000BkplMidRight,
       "s5ChasComM5000BkplHighLeft": s5ChasComM5000BkplHighLeft,
       "s5ChasComM5000BkplHighLeftEth100Mbs": s5ChasComM5000BkplHighLeftEth100Mbs,
       "s5ChasComM5000BkplHighLeftSwitchedPktBusFull": s5ChasComM5000BkplHighLeftSwitchedPktBusFull,
       "s5ChasComM5000BkplHighLeftAtm16": s5ChasComM5000BkplHighLeftAtm16,
       "s5ChasComM5000BkplHighLeftAtm64": s5ChasComM5000BkplHighLeftAtm64,
       "s5ChasComM5000BkplHighRight": s5ChasComM5000BkplHighRight,
       "s5ChasComM5005Bkpl": s5ChasComM5005Bkpl,
       "s5ChasComM5005BkplLow": s5ChasComM5005BkplLow,
       "s5ChasComM5005BkplLowCmbEthTok": s5ChasComM5005BkplLowCmbEthTok,
       "s5ChasComM5005BkplLowCmbEth": s5ChasComM5005BkplLowCmbEth,
       "s5ChasComM5005BkplMidLeft": s5ChasComM5005BkplMidLeft,
       "s5ChasComM5005BkplMidLeftFddi": s5ChasComM5005BkplMidLeftFddi,
       "s5ChasComM5005BkplMidLeftEth100Mbs": s5ChasComM5005BkplMidLeftEth100Mbs,
       "s5ChasComM5005BkplHighLeft": s5ChasComM5005BkplHighLeft,
       "s5ChasComM5005BkplHighLeftSwitchedPktBus": s5ChasComM5005BkplHighLeftSwitchedPktBus,
       "s5ChasComM5Dx000Bkpl": s5ChasComM5Dx000Bkpl,
       "s5ChasComM5DN000BkplEth3": s5ChasComM5DN000BkplEth3,
       "s5ChasComMNBayStackBkpl": s5ChasComMNBayStackBkpl,
       "s5ChasComMNBayStackBkplEth3": s5ChasComMNBayStackBkplEth3,
       "s5ChasComBayStack100Bkpl": s5ChasComBayStack100Bkpl,
       "s5ChasComM3000Bkpl": s5ChasComM3000Bkpl,
       "s5ChasComM3000EthBkpl": s5ChasComM3000EthBkpl,
       "s5ChasComM3000-1Bkpl": s5ChasComM3000_1Bkpl,
       "s5ChasComM3000NBkpl": s5ChasComM3000NBkpl,
       "s5ChasComM3000EthTokBkpl": s5ChasComM3000EthTokBkpl,
       "s5ChasComM3000-4Bkpl": s5ChasComM3000_4Bkpl,
       "s5ChasComM3000NTBkpl": s5ChasComM3000NTBkpl,
       "s5ChasComM3000EthFddiBkpl": s5ChasComM3000EthFddiBkpl,
       "s5ChasComM3000EthTokFddiBkpl": s5ChasComM3000EthTokFddiBkpl,
       "s5ChasComM3000-5Bkpl": s5ChasComM3000_5Bkpl,
       "s5ChasComM3000SBkpl": s5ChasComM3000SBkpl,
       "s5ChasComM3000EthTokRedBkpl": s5ChasComM3000EthTokRedBkpl,
       "s5ChasComM3000-4RBkpl": s5ChasComM3000_4RBkpl,
       "s5ChasComM3000NTRBkpl": s5ChasComM3000NTRBkpl,
       "s5ChasComM3000EthTokFddiRedBkpl": s5ChasComM3000EthTokFddiRedBkpl,
       "s5ChasComM3000-5RBkpl": s5ChasComM3000_5RBkpl,
       "s5ChasComM3000SRBkpl": s5ChasComM3000SRBkpl,
       "s5ChasComM3000TokBkpl": s5ChasComM3000TokBkpl,
       "s5ChasComM3000CTBkpl": s5ChasComM3000CTBkpl,
       "s5ChasComM3000CBkpl": s5ChasComM3000CBkpl,
       "s5ChasComM3000CTRBkpl": s5ChasComM3000CTRBkpl,
       "s5ChasCom28200Bkpl": s5ChasCom28200Bkpl,
       "s5ChasComMBayStackTrBkpl": s5ChasComMBayStackTrBkpl,
       "s5ChasComMBayStackTrBkplTr1": s5ChasComMBayStackTrBkplTr1,
       "s5ChasComM3030Bkpl": s5ChasComM3030Bkpl,
       "s5ChasComM3030EthBkpl": s5ChasComM3030EthBkpl,
       "s5ChasComM3030EthTrBkpl": s5ChasComM3030EthTrBkpl,
       "s5ChasComSwitchNodeBkpl": s5ChasComSwitchNodeBkpl,
       "s5ChasComBayStack150Bkpl": s5ChasComBayStack150Bkpl,
       "s5ChasComBayStack150BkplEth": s5ChasComBayStack150BkplEth,
       "s5ChasComMBayStack303-304Bkpl": s5ChasComMBayStack303_304Bkpl,
       "s5ChasComBayStack200Bkpl": s5ChasComBayStack200Bkpl,
       "s5ChasComBayStack200BkplEth": s5ChasComBayStack200BkplEth,
       "s5ChasComBayStack250Bkpl": s5ChasComBayStack250Bkpl,
       "s5ChasComBayStack250BkplEth10": s5ChasComBayStack250BkplEth10,
       "s5ChasComBayStack250BkplEth100": s5ChasComBayStack250BkplEth100,
       "s5ChasComMAccelar8010Bkpl": s5ChasComMAccelar8010Bkpl,
       "s5ChasComMPwr": s5ChasComMPwr,
       "s5ChasComM5000Pwr": s5ChasComM5000Pwr,
       "s5ChasComM5000Pwr-950A": s5ChasComM5000Pwr_950A,
       "s5ChasComM5000Pwr-950": s5ChasComM5000Pwr_950,
       "s5ChasComM5000Pwr-1400WDC": s5ChasComM5000Pwr_1400WDC,
       "s5ChasComM1032xPwr": s5ChasComM1032xPwr,
       "s5ChasComM1032xPwr-A": s5ChasComM1032xPwr_A,
       "s5ChasComM5005Pwr": s5ChasComM5005Pwr,
       "s5ChasComM5005Pwr-600": s5ChasComM5005Pwr_600,
       "s5ChasComM5005Pwr-900WAC": s5ChasComM5005Pwr_900WAC,
       "s5ChasComM5005Pwr-900WDC": s5ChasComM5005Pwr_900WDC,
       "s5ChasComM5DN000Pwr": s5ChasComM5DN000Pwr,
       "s5ChasCom5DN000Pwr-RedundFeed": s5ChasCom5DN000Pwr_RedundFeed,
       "s5ChasComM5DN002Pwr-50W": s5ChasComM5DN002Pwr_50W,
       "s5ChasComM5DN003Pwr-110W": s5ChasComM5DN003Pwr_110W,
       "s5ChasComMNBayStackPwr": s5ChasComMNBayStackPwr,
       "s5ChasComMNBayStackPwr-RedundFeed": s5ChasComMNBayStackPwr_RedundFeed,
       "s5ChasComMNBayStackPwr-50W": s5ChasComMNBayStackPwr_50W,
       "s5ChasComMBayStack100Pwr": s5ChasComMBayStack100Pwr,
       "s5ChasComMBayStack100Pwr-RedundFeed": s5ChasComMBayStack100Pwr_RedundFeed,
       "s5ChasComMBayStack100Pwr-110W": s5ChasComMBayStack100Pwr_110W,
       "s5ChasComM3000Pwr": s5ChasComM3000Pwr,
       "s5ChasComM3000360Pwr": s5ChasComM3000360Pwr,
       "s5ChasComM3000460Pwr": s5ChasComM3000460Pwr,
       "s5ChasComM3003-460Pwr": s5ChasComM3003_460Pwr,
       "s5ChasComM28200Pwr": s5ChasComM28200Pwr,
       "s5ChasComM28200Pwr-RedundFeed": s5ChasComM28200Pwr_RedundFeed,
       "s5ChasComM28200Pwr-182W": s5ChasComM28200Pwr_182W,
       "s5ChasComMBayStack301Pwr": s5ChasComMBayStack301Pwr,
       "s5ChasComMBayStack301IntPwr": s5ChasComMBayStack301IntPwr,
       "s5ChasComMBayStack301ExtPwr": s5ChasComMBayStack301ExtPwr,
       "s5ChasComSwitchNodePwr": s5ChasComSwitchNodePwr,
       "s5ChasComMBayStackTrPwr": s5ChasComMBayStackTrPwr,
       "s5ChasComMBayStackTrPwr-RedundFeed": s5ChasComMBayStackTrPwr_RedundFeed,
       "s5ChasComMBayStackTrPwr-150W": s5ChasComMBayStackTrPwr_150W,
       "s5ChasComBayStack150Pwr": s5ChasComBayStack150Pwr,
       "s5ChasComBayStack150MasterPwr": s5ChasComBayStack150MasterPwr,
       "s5ChasComBayStack150SlavePwr": s5ChasComBayStack150SlavePwr,
       "s5ChasComMBayStack303-304Pwr": s5ChasComMBayStack303_304Pwr,
       "s5ChasComBayStack200Pwr": s5ChasComBayStack200Pwr,
       "s5ChasComBayStack200MasterPwr": s5ChasComBayStack200MasterPwr,
       "s5ChasComBayStack250Pwr": s5ChasComBayStack250Pwr,
       "s5ChasComBayStack250MasterPwr": s5ChasComBayStack250MasterPwr,
       "s5ChasComBayStack250SlavePwr": s5ChasComBayStack250SlavePwr,
       "s5ChasComMAccelar8001Pwr": s5ChasComMAccelar8001Pwr,
       "s5ChasComMAccelar8002Pwr": s5ChasComMAccelar8002Pwr,
       "s5ChasComBPS2000Pwr": s5ChasComBPS2000Pwr,
       "s5ChasComBPS2000Pwr-Main": s5ChasComBPS2000Pwr_Main,
       "s5ChasComBPS2000Pwr-RedundFeed": s5ChasComBPS2000Pwr_RedundFeed,
       "s5ChasComBayStack450Pwr": s5ChasComBayStack450Pwr,
       "s5ChasComBayStack450Pwr-Main": s5ChasComBayStack450Pwr_Main,
       "s5ChasComBayStack450Pwr-RedundFeed": s5ChasComBayStack450Pwr_RedundFeed,
       "s5ChasComBayStack3580Pwr": s5ChasComBayStack3580Pwr,
       "s5ChasComBayStack3580Pwr-Main": s5ChasComBayStack3580Pwr_Main,
       "s5ChasComBayStack3580Pwr-RedundFeed": s5ChasComBayStack3580Pwr_RedundFeed,
       "s5ChasComBayStack420Pwr": s5ChasComBayStack420Pwr,
       "s5ChasComMetro1200ESMPwr": s5ChasComMetro1200ESMPwr,
       "s5ChasComMetro1200ESMPwr-Main": s5ChasComMetro1200ESMPwr_Main,
       "s5ChasComMetro1200ESMPwr-RedundFeed": s5ChasComMetro1200ESMPwr_RedundFeed,
       "s5ChasComBayStack380Pwr": s5ChasComBayStack380Pwr,
       "s5ChasComBayStack380Pwr-Main": s5ChasComBayStack380Pwr_Main,
       "s5ChasComBayStack380Pwr-RedundFeed": s5ChasComBayStack380Pwr_RedundFeed,
       "s5ChasComBayStack470Pwr": s5ChasComBayStack470Pwr,
       "s5ChasComBayStack470Pwr-Main": s5ChasComBayStack470Pwr_Main,
       "s5ChasComBayStack470Pwr-RedundFeed": s5ChasComBayStack470Pwr_RedundFeed,
       "s5ChasComMetro1450ESMPwr": s5ChasComMetro1450ESMPwr,
       "s5ChasComMetro1450ESMPwr-Main": s5ChasComMetro1450ESMPwr_Main,
       "s5ChasComMetro1450ESMPwr-RedundFeed": s5ChasComMetro1450ESMPwr_RedundFeed,
       "s5ChasComMetro1400ESMPwr": s5ChasComMetro1400ESMPwr,
       "s5ChasComMetro1400ESMPwr-Main": s5ChasComMetro1400ESMPwr_Main,
       "s5ChasComMetro1400ESMPwr-RedundFeed": s5ChasComMetro1400ESMPwr_RedundFeed,
       "s5ChasComBayStack460-24T-PWRPwr": s5ChasComBayStack460_24T_PWRPwr,
       "s5ChasComBayStack460-24T-PWRPwr-Main": s5ChasComBayStack460_24T_PWRPwr_Main,
       "s5ChasComBayStack460-24T-PWRPwr-RedundFeed": s5ChasComBayStack460_24T_PWRPwr_RedundFeed,
       "s5ChasComBayStack380-24FPwr": s5ChasComBayStack380_24FPwr,
       "s5ChasComBayStack380-24FPwr-Main": s5ChasComBayStack380_24FPwr_Main,
       "s5ChasComBayStack380-24FPwr-RedundFeed": s5ChasComBayStack380_24FPwr_RedundFeed,
       "s5ChasComBayStack5510-24TPwr": s5ChasComBayStack5510_24TPwr,
       "s5ChasComBayStack5510-24TPwr-Main": s5ChasComBayStack5510_24TPwr_Main,
       "s5ChasComBayStack5510-24TPwr-RedundFeed": s5ChasComBayStack5510_24TPwr_RedundFeed,
       "s5ChasComBayStack5510-48TPwr": s5ChasComBayStack5510_48TPwr,
       "s5ChasComBayStack5510-48TPwr-Main": s5ChasComBayStack5510_48TPwr_Main,
       "s5ChasComBayStack5510-48TPwr-RedundFeed": s5ChasComBayStack5510_48TPwr_RedundFeed,
       "s5ChasComBayStack470-24TPwr": s5ChasComBayStack470_24TPwr,
       "s5ChasComBayStack470-24TPwr-Main": s5ChasComBayStack470_24TPwr_Main,
       "s5ChasComBayStack470-24TPwr-RedundFeed": s5ChasComBayStack470_24TPwr_RedundFeed,
       "s5ChasComWLANAccessPoint2220Pwr": s5ChasComWLANAccessPoint2220Pwr,
       "s5ChasComWLANAccessPoint2220Pwr-Main": s5ChasComWLANAccessPoint2220Pwr_Main,
       "s5ChasComWLANSecuritySwitch2250Pwr": s5ChasComWLANSecuritySwitch2250Pwr,
       "s5ChasComWLANSecuritySwitch2250Pwr-Main": s5ChasComWLANSecuritySwitch2250Pwr_Main,
       "s5ChasComBayStack425Pwr": s5ChasComBayStack425Pwr,
       "s5ChasComBayStack425PwrMain": s5ChasComBayStack425PwrMain,
       "s5ChasComBayStack425PwrRedundFeed": s5ChasComBayStack425PwrRedundFeed,
       "s5ChasComWLANAccessPoint2221Pwr": s5ChasComWLANAccessPoint2221Pwr,
       "s5ChasComWLANAccessPoint2221Pwr-Main": s5ChasComWLANAccessPoint2221Pwr_Main,
       "s5ChasComBayStack5520-24T-PWRPwr": s5ChasComBayStack5520_24T_PWRPwr,
       "s5ChasComBayStack5520-24T-PWRPwr-Main": s5ChasComBayStack5520_24T_PWRPwr_Main,
       "s5ChasComBayStack5520-24T-PWRPwr-RedundFeed": s5ChasComBayStack5520_24T_PWRPwr_RedundFeed,
       "s5ChasComBayStack5520-48T-PWRPwr": s5ChasComBayStack5520_48T_PWRPwr,
       "s5ChasComBayStack5520-48T-PWRPwr-Main": s5ChasComBayStack5520_48T_PWRPwr_Main,
       "s5ChasComBayStack5520-48T-PWRPwr-RedundFeed": s5ChasComBayStack5520_48T_PWRPwr_RedundFeed,
       "s5ChasComBayStack325Pwr": s5ChasComBayStack325Pwr,
       "s5ChasComBayStack325PwrMain": s5ChasComBayStack325PwrMain,
       "s5ChasComBayStack325PwrRedundFeed": s5ChasComBayStack325PwrRedundFeed,
       "s5ChasComWLANAccessPoint2225Pwr": s5ChasComWLANAccessPoint2225Pwr,
       "s5ChasComWLANAccessPoint2225Pwr-Main": s5ChasComWLANAccessPoint2225Pwr_Main,
       "s5ChasComBayStack470-24T-PWRPwr": s5ChasComBayStack470_24T_PWRPwr,
       "s5ChasComBayStack470-24T-PWRPwr-Main": s5ChasComBayStack470_24T_PWRPwr_Main,
       "s5ChasComBayStack470-24T-PWRPwr-RedundFeed": s5ChasComBayStack470_24T_PWRPwr_RedundFeed,
       "s5ChasComBayStack470-48T-PWRPwr": s5ChasComBayStack470_48T_PWRPwr,
       "s5ChasComBayStack470-48T-PWRPwr-Main": s5ChasComBayStack470_48T_PWRPwr_Main,
       "s5ChasComBayStack470-48T-PWRPwr-RedundFeed": s5ChasComBayStack470_48T_PWRPwr_RedundFeed,
       "s5ChasComWLANSecuritySwitch2270Pwr": s5ChasComWLANSecuritySwitch2270Pwr,
       "s5ChasComWLANSecuritySwitch2270Pwr-Main": s5ChasComWLANSecuritySwitch2270Pwr_Main,
       "s5ChasComEthernetRoutingSwitch5530-24TFDPwr": s5ChasComEthernetRoutingSwitch5530_24TFDPwr,
       "s5ChasComEthernetRoutingSwitch5530-24TFDPwr-Main": s5ChasComEthernetRoutingSwitch5530_24TFDPwr_Main,
       "s5ChasComEthernetRoutingSwitch5530-24TFDPwr-RedundFeed": s5ChasComEthernetRoutingSwitch5530_24TFDPwr_RedundFeed,
       "s5ChasComEthernetSwitch3510-24TPwr": s5ChasComEthernetSwitch3510_24TPwr,
       "s5ChasComEthernetSwitch3510-24TPwr-Main": s5ChasComEthernetSwitch3510_24TPwr_Main,
       "s5ChasComEthernetSwitch3510-24TPwr-RedundFeed": s5ChasComEthernetSwitch3510_24TPwr_RedundFeed,
       "s5ChasComBES1010-24TPwr": s5ChasComBES1010_24TPwr,
       "s5ChasComBES1010-24TPwr-Main": s5ChasComBES1010_24TPwr_Main,
       "s5ChasComBES1010-24TPwr-RedundFeed": s5ChasComBES1010_24TPwr_RedundFeed,
       "s5ChasComBES1010-48TPwr": s5ChasComBES1010_48TPwr,
       "s5ChasComBES1010-48TPwr-Main": s5ChasComBES1010_48TPwr_Main,
       "s5ChasComBES1010-48TPwr-RedundFeed": s5ChasComBES1010_48TPwr_RedundFeed,
       "s5ChasComBES1020-24T-PWRPwr": s5ChasComBES1020_24T_PWRPwr,
       "s5ChasComBES1020-24T-PWRPwr-Main": s5ChasComBES1020_24T_PWRPwr_Main,
       "s5ChasComBES1020-24T-PWRPwr-RedundFeed": s5ChasComBES1020_24T_PWRPwr_RedundFeed,
       "s5ChasComBES1020-48T-PWRPwr": s5ChasComBES1020_48T_PWRPwr,
       "s5ChasComBES1020-48T-PWRPwr-Main": s5ChasComBES1020_48T_PWRPwr_Main,
       "s5ChasComBES1020-48T-PWRPwr-RedundFeed": s5ChasComBES1020_48T_PWRPwr_RedundFeed,
       "s5ChasComBES2010-24TPwr": s5ChasComBES2010_24TPwr,
       "s5ChasComBES2010-24TPwr-Main": s5ChasComBES2010_24TPwr_Main,
       "s5ChasComBES2010-24TPwr-RedundFeed": s5ChasComBES2010_24TPwr_RedundFeed,
       "s5ChasComBES2010-48TPwr": s5ChasComBES2010_48TPwr,
       "s5ChasComBES2010-48TPwr-Main": s5ChasComBES2010_48TPwr_Main,
       "s5ChasComBES2010-48TPwr-RedundFeed": s5ChasComBES2010_48TPwr_RedundFeed,
       "s5ChasComBES2020-24T-PWRPwr": s5ChasComBES2020_24T_PWRPwr,
       "s5ChasComBES2020-24T-PWRPwr-Main": s5ChasComBES2020_24T_PWRPwr_Main,
       "s5ChasComBES2020-24T-PWRPwr-RedundFeed": s5ChasComBES2020_24T_PWRPwr_RedundFeed,
       "s5ChasComBES2020-48T-PWRPwr": s5ChasComBES2020_48T_PWRPwr,
       "s5ChasComBES2020-48T-PWRPwr-Main": s5ChasComBES2020_48T_PWRPwr_Main,
       "s5ChasComBES2020-48T-PWRPwr-RedundFeed": s5ChasComBES2020_48T_PWRPwr_RedundFeed,
       "s5ChasComBES110-24TPwr": s5ChasComBES110_24TPwr,
       "s5ChasComBES110-24TPwr-Main": s5ChasComBES110_24TPwr_Main,
       "s5ChasComBES110-24TPwr-RedundFeed": s5ChasComBES110_24TPwr_RedundFeed,
       "s5ChasComBES110-48TPwr": s5ChasComBES110_48TPwr,
       "s5ChasComBES110-48TPwr-Main": s5ChasComBES110_48TPwr_Main,
       "s5ChasComBES110-48TPwr-RedundFeed": s5ChasComBES110_48TPwr_RedundFeed,
       "s5ChasComBES120-24T-PWRPwr": s5ChasComBES120_24T_PWRPwr,
       "s5ChasComBES120-24T-PWRPwr-Main": s5ChasComBES120_24T_PWRPwr_Main,
       "s5ChasComBES120-24T-PWRPwr-RedundFeed": s5ChasComBES120_24T_PWRPwr_RedundFeed,
       "s5ChasComBES120-48T-PWRPwr": s5ChasComBES120_48T_PWRPwr,
       "s5ChasComBES120-48T-PWRPwr-Main": s5ChasComBES120_48T_PWRPwr_Main,
       "s5ChasComBES120-48T-PWRPwr-RedundFeed": s5ChasComBES120_48T_PWRPwr_RedundFeed,
       "s5ChasComBES210-24TPwr": s5ChasComBES210_24TPwr,
       "s5ChasComBES210-24TPwr-Main": s5ChasComBES210_24TPwr_Main,
       "s5ChasComBES210-24TPwr-RedundFeed": s5ChasComBES210_24TPwr_RedundFeed,
       "s5ChasComBES210-48TPwr": s5ChasComBES210_48TPwr,
       "s5ChasComBES210-48TPwr-Main": s5ChasComBES210_48TPwr_Main,
       "s5ChasComBES210-48TPwr-RedundFeed": s5ChasComBES210_48TPwr_RedundFeed,
       "s5ChasComBES220-24T-PWRPwr": s5ChasComBES220_24T_PWRPwr,
       "s5ChasComBES220-24T-PWRPwr-Main": s5ChasComBES220_24T_PWRPwr_Main,
       "s5ChasComBES220-24T-PWRPwr-RedundFeed": s5ChasComBES220_24T_PWRPwr_RedundFeed,
       "s5ChasComBES220-48T-PWRPwr": s5ChasComBES220_48T_PWRPwr,
       "s5ChasComBES220-48T-PWRPwr-Main": s5ChasComBES220_48T_PWRPwr_Main,
       "s5ChasComBES220-48T-PWRPwr-RedundFeed": s5ChasComBES220_48T_PWRPwr_RedundFeed,
       "s5ChasComERS4548GTPwr": s5ChasComERS4548GTPwr,
       "s5ChasComERS4548GTPwr-Main": s5ChasComERS4548GTPwr_Main,
       "s5ChasComERS4548GTPwr-RedundFeed": s5ChasComERS4548GTPwr_RedundFeed,
       "s5ChasComERS4548GT-PWRPwr": s5ChasComERS4548GT_PWRPwr,
       "s5ChasComERS4548GT-PWRPwr-Main": s5ChasComERS4548GT_PWRPwr_Main,
       "s5ChasComERS4548GT-PWRPwr-RedundFeed": s5ChasComERS4548GT_PWRPwr_RedundFeed,
       "s5ChasComERS4550TPwr": s5ChasComERS4550TPwr,
       "s5ChasComERS4550TPwr-Main": s5ChasComERS4550TPwr_Main,
       "s5ChasComERS4550TPwr-RedundFeed": s5ChasComERS4550TPwr_RedundFeed,
       "s5ChasComERS4550T-PWRPwr": s5ChasComERS4550T_PWRPwr,
       "s5ChasComERS4550T-PWRPwr-Main": s5ChasComERS4550T_PWRPwr_Main,
       "s5ChasComERS4550T-PWRPwr-RedundFeed": s5ChasComERS4550T_PWRPwr_RedundFeed,
       "s5ChasComERS4526FXPwr": s5ChasComERS4526FXPwr,
       "s5ChasComERS4526FXPwr-Main": s5ChasComERS4526FXPwr_Main,
       "s5ChasComERS4526FXPwr-RedundFeed": s5ChasComERS4526FXPwr_RedundFeed,
       "s5ChasComERS2500-26TPwr": s5ChasComERS2500_26TPwr,
       "s5ChasComERS2500-26TPwr-Main": s5ChasComERS2500_26TPwr_Main,
       "s5ChasComERS2500-26TPwr-RedundFeed": s5ChasComERS2500_26TPwr_RedundFeed,
       "s5ChasComERS2500-26T-PWRPwr": s5ChasComERS2500_26T_PWRPwr,
       "s5ChasComERS2500-26T-PWRPwr-Main": s5ChasComERS2500_26T_PWRPwr_Main,
       "s5ChasComERS2500-26T-PWRPwr-RedundFeed": s5ChasComERS2500_26T_PWRPwr_RedundFeed,
       "s5ChasComERS2500-50TPwr": s5ChasComERS2500_50TPwr,
       "s5ChasComERS2500-50TPwr-Main": s5ChasComERS2500_50TPwr_Main,
       "s5ChasComERS2500-50TPwr-RedundFeed": s5ChasComERS2500_50TPwr_RedundFeed,
       "s5ChasComERS2500-50T-PWRPwr": s5ChasComERS2500_50T_PWRPwr,
       "s5ChasComERS2500-50T-PWRPwr-Main": s5ChasComERS2500_50T_PWRPwr_Main,
       "s5ChasComERS2500-50T-PWRPwr-RedundFeed": s5ChasComERS2500_50T_PWRPwr_RedundFeed,
       "s5ChasComERS4526GTX-PWRPwr": s5ChasComERS4526GTX_PWRPwr,
       "s5ChasComERS4526GTX-PWRPwr-Main": s5ChasComERS4526GTX_PWRPwr_Main,
       "s5ChasComERS4526GTX-PWRPwr-RedundFeed": s5ChasComERS4526GTX_PWRPwr_RedundFeed,
       "s5ChasComERS4526GTXPwr": s5ChasComERS4526GTXPwr,
       "s5ChasComERS4526GTXPwr-Main": s5ChasComERS4526GTXPwr_Main,
       "s5ChasComERS4526GTXPwr-RedundFeed": s5ChasComERS4526GTXPwr_RedundFeed,
       "s5ChasComERS4524GTPwr": s5ChasComERS4524GTPwr,
       "s5ChasComERS4524GTPwr-Main": s5ChasComERS4524GTPwr_Main,
       "s5ChasComERS4524GTPwr-RedundFeed": s5ChasComERS4524GTPwr_RedundFeed,
       "s5ChasComERS4526TPwr": s5ChasComERS4526TPwr,
       "s5ChasComERS4526TPwr-Main": s5ChasComERS4526TPwr_Main,
       "s5ChasComERS4526TPwr-RedundFeed": s5ChasComERS4526TPwr_RedundFeed,
       "s5ChasComERS4526T-PWRPwr": s5ChasComERS4526T_PWRPwr,
       "s5ChasComERS4526T-PWRPwr-Main": s5ChasComERS4526T_PWRPwr_Main,
       "s5ChasComERS4526T-PWRPwr-RedundFeed": s5ChasComERS4526T_PWRPwr_RedundFeed,
       "s5ChasComERS5698-TFD-PWRPwr": s5ChasComERS5698_TFD_PWRPwr,
       "s5ChasComERS5698-TFD-PWRPwr-Main": s5ChasComERS5698_TFD_PWRPwr_Main,
       "s5ChasComERS5698-TFD-PWRPwr-RedundFeed": s5ChasComERS5698_TFD_PWRPwr_RedundFeed,
       "s5ChasComERS5698-TFD-PWRPwr-None": s5ChasComERS5698_TFD_PWRPwr_None,
       "s5ChasComERS5698-TFD-PWRPwr-AC-DC-12V-300W": s5ChasComERS5698_TFD_PWRPwr_AC_DC_12V_300W,
       "s5ChasComERS5698-TFD-PWRPwr-DC-DC-12V-300W": s5ChasComERS5698_TFD_PWRPwr_DC_DC_12V_300W,
       "s5ChasComERS5698-TFD-PWRPwr-AC-DC-48V-600W": s5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_600W,
       "s5ChasComERS5698-TFD-PWRPwr-DC-DC-48V-600W": s5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_600W,
       "s5ChasComERS5698-TFD-PWRPwr-AC-DC-48V-1000W": s5ChasComERS5698_TFD_PWRPwr_AC_DC_48V_1000W,
       "s5ChasComERS5698-TFD-PWRPwr-DC-DC-48V-1000W": s5ChasComERS5698_TFD_PWRPwr_DC_DC_48V_1000W,
       "s5ChasComERS5698-TFDPwr": s5ChasComERS5698_TFDPwr,
       "s5ChasComERS5698-TFDPwr-Main": s5ChasComERS5698_TFDPwr_Main,
       "s5ChasComERS5698-TFDPwr-RedundFeed": s5ChasComERS5698_TFDPwr_RedundFeed,
       "s5ChasComERS5698-TFDPwr-None": s5ChasComERS5698_TFDPwr_None,
       "s5ChasComERS5698-TFDPwr-AC-DC-12V-300W": s5ChasComERS5698_TFDPwr_AC_DC_12V_300W,
       "s5ChasComERS5698-TFDPwr-DC-DC-12V-300W": s5ChasComERS5698_TFDPwr_DC_DC_12V_300W,
       "s5ChasComERS5698-TFDPwr-AC-DC-48V-600W": s5ChasComERS5698_TFDPwr_AC_DC_48V_600W,
       "s5ChasComERS5698-TFDPwr-DC-DC-48V-600W": s5ChasComERS5698_TFDPwr_DC_DC_48V_600W,
       "s5ChasComERS5698-TFDPwr-AC-DC-48V-1000W": s5ChasComERS5698_TFDPwr_AC_DC_48V_1000W,
       "s5ChasComERS5698-TFDPwr-DC-DC-48V-1000W": s5ChasComERS5698_TFDPwr_DC_DC_48V_1000W,
       "s5ChasComERS5650-TD-PWRPwr": s5ChasComERS5650_TD_PWRPwr,
       "s5ChasComERS5650-TD-PWRPwr-Main": s5ChasComERS5650_TD_PWRPwr_Main,
       "s5ChasComERS5650-TD-PWRPwr-RedundFeed": s5ChasComERS5650_TD_PWRPwr_RedundFeed,
       "s5ChasComERS5650-TD-PWRPwr-None": s5ChasComERS5650_TD_PWRPwr_None,
       "s5ChasComERS5650-TD-PWRPwr-AC-DC-12V-300W": s5ChasComERS5650_TD_PWRPwr_AC_DC_12V_300W,
       "s5ChasComERS5650-TD-PWRPwr-DC-DC-12V-300W": s5ChasComERS5650_TD_PWRPwr_DC_DC_12V_300W,
       "s5ChasComERS5650-TD-PWRPwr-AC-DC-48V-600W": s5ChasComERS5650_TD_PWRPwr_AC_DC_48V_600W,
       "s5ChasComERS5650-TD-PWRPwr-DC-DC-48V-600W": s5ChasComERS5650_TD_PWRPwr_DC_DC_48V_600W,
       "s5ChasComERS5650-TD-PWRPwr-AC-DC-48V-1000W": s5ChasComERS5650_TD_PWRPwr_AC_DC_48V_1000W,
       "s5ChasComERS5650-TD-PWRPwr-DC-DC-48V-1000W": s5ChasComERS5650_TD_PWRPwr_DC_DC_48V_1000W,
       "s5ChasComERS5650-TDPwr": s5ChasComERS5650_TDPwr,
       "s5ChasComERS5650-TDPwr-Main": s5ChasComERS5650_TDPwr_Main,
       "s5ChasComERS5650-TDPwr-RedundFeed": s5ChasComERS5650_TDPwr_RedundFeed,
       "s5ChasComERS5650-TDPwr-None": s5ChasComERS5650_TDPwr_None,
       "s5ChasComERS5650-TDPwr-AC-DC-12V-300W": s5ChasComERS5650_TDPwr_AC_DC_12V_300W,
       "s5ChasComERS5650-TDPwr-DC-DC-12V-300W": s5ChasComERS5650_TDPwr_DC_DC_12V_300W,
       "s5ChasComERS5650-TDPwr-AC-DC-48V-600W": s5ChasComERS5650_TDPwr_AC_DC_48V_600W,
       "s5ChasComERS5650-TDPwr-DC-DC-48V-600W": s5ChasComERS5650_TDPwr_DC_DC_48V_600W,
       "s5ChasComERS5650-TDPwr-AC-DC-48V-1000W": s5ChasComERS5650_TDPwr_AC_DC_48V_1000W,
       "s5ChasComERS5650-TDPwr-DC-DC-48V-1000W": s5ChasComERS5650_TDPwr_DC_DC_48V_1000W,
       "s5ChasComERS5632-FDPwr": s5ChasComERS5632_FDPwr,
       "s5ChasComERS5632-FDPwr-Main": s5ChasComERS5632_FDPwr_Main,
       "s5ChasComERS5632-FDPwr-RedundFeed": s5ChasComERS5632_FDPwr_RedundFeed,
       "s5ChasComERS5632-FDPwr-None": s5ChasComERS5632_FDPwr_None,
       "s5ChasComERS5632-FDPwr-AC-DC-12V-300W": s5ChasComERS5632_FDPwr_AC_DC_12V_300W,
       "s5ChasComERS5632-FDPwr-DC-DC-12V-300W": s5ChasComERS5632_FDPwr_DC_DC_12V_300W,
       "s5ChasComERS5632-FDPwr-AC-DC-48V-600W": s5ChasComERS5632_FDPwr_AC_DC_48V_600W,
       "s5ChasComERS5632-FDPwr-DC-DC-48V-600W": s5ChasComERS5632_FDPwr_DC_DC_48V_600W,
       "s5ChasComERS5632-FDPwr-AC-DC-48V-1000W": s5ChasComERS5632_FDPwr_AC_DC_48V_1000W,
       "s5ChasComERS5632-FDPwr-DC-DC-48V-1000W": s5ChasComERS5632_FDPwr_DC_DC_48V_1000W,
       "s5ChasComESU1860SPwr": s5ChasComESU1860SPwr,
       "s5ChasComESU1860SPwr-Main-DC": s5ChasComESU1860SPwr_Main_DC,
       "s5ChasComESU1860SPwr-Main-AC": s5ChasComESU1860SPwr_Main_AC,
       "s5ChasComESU1860SPwr-RedundFeed-DC": s5ChasComESU1860SPwr_RedundFeed_DC,
       "s5ChasComESU1860SPwr-RedundFeed-AC": s5ChasComESU1860SPwr_RedundFeed_AC,
       "s5ChasComESU1860BPwr": s5ChasComESU1860BPwr,
       "s5ChasComESU1860BPwr-Main-DC": s5ChasComESU1860BPwr_Main_DC,
       "s5ChasComESU1860BPwr-Main-AC": s5ChasComESU1860BPwr_Main_AC,
       "s5ChasComESU1860BPwr-RedundFeed-DC": s5ChasComESU1860BPwr_RedundFeed_DC,
       "s5ChasComESU1860BPwr-RedundFeed-AC": s5ChasComESU1860BPwr_RedundFeed_AC,
       "s5ChasComESU1860TPwr": s5ChasComESU1860TPwr,
       "s5ChasComESU1860TPwr-Main-DC": s5ChasComESU1860TPwr_Main_DC,
       "s5ChasComESU1860TPwr-Main-AC": s5ChasComESU1860TPwr_Main_AC,
       "s5ChasComESU1860TPwr-RedundFeed-DC": s5ChasComESU1860TPwr_RedundFeed_DC,
       "s5ChasComESU1860TPwr-RedundFeed-AC": s5ChasComESU1860TPwr_RedundFeed_AC,
       "s5ChasComESU1860VPwr": s5ChasComESU1860VPwr,
       "s5ChasComESU1860VPwr-Main-DC": s5ChasComESU1860VPwr_Main_DC,
       "s5ChasComESU1860VPwr-Main-AC": s5ChasComESU1860VPwr_Main_AC,
       "s5ChasComESU1860VPwr-RedundFeed-DC": s5ChasComESU1860VPwr_RedundFeed_DC,
       "s5ChasComESU1860VPwr-RedundFeed-AC": s5ChasComESU1860VPwr_RedundFeed_AC,
       "s5ChasComESU1880SPwr": s5ChasComESU1880SPwr,
       "s5ChasComESU1880SPwr-Main-DC": s5ChasComESU1880SPwr_Main_DC,
       "s5ChasComESU1880SPwr-Main-AC": s5ChasComESU1880SPwr_Main_AC,
       "s5ChasComESU1880SPwr-RedundFeed-DC": s5ChasComESU1880SPwr_RedundFeed_DC,
       "s5ChasComESU1880SPwr-RedundFeed-AC": s5ChasComESU1880SPwr_RedundFeed_AC,
       "s5ChasComERS4524GT-PWRPwr": s5ChasComERS4524GT_PWRPwr,
       "s5ChasComERS4524GT-PWRPwr-Main": s5ChasComERS4524GT_PWRPwr_Main,
       "s5ChasComERS4524GT-PWRPwr-RedundFeed": s5ChasComERS4524GT_PWRPwr_RedundFeed,
       "s5ChasComERS6628XSGTPwr": s5ChasComERS6628XSGTPwr,
       "s5ChasComERS6628XSGTPwr-Main": s5ChasComERS6628XSGTPwr_Main,
       "s5ChasComERS6628XSGTPwr-RedundFeed": s5ChasComERS6628XSGTPwr_RedundFeed,
       "s5ChasComERS6632XTSPwr": s5ChasComERS6632XTSPwr,
       "s5ChasComERS6632XTSPwr-Main": s5ChasComERS6632XTSPwr_Main,
       "s5ChasComERS6632XTSPwr-RedundFeed": s5ChasComERS6632XTSPwr_RedundFeed,
       "s5ChasComWC8180Pwr": s5ChasComWC8180Pwr,
       "s5ChasComWC8180Pwr-Main": s5ChasComWC8180Pwr_Main,
       "s5ChasComWC8180Pwr-RedundFeed": s5ChasComWC8180Pwr_RedundFeed,
       "s5ChasComERS4526T-PWR-PLUSPwr": s5ChasComERS4526T_PWR_PLUSPwr,
       "s5ChasComERS4526T-PWR-PLUSPwr-Main": s5ChasComERS4526T_PWR_PLUSPwr_Main,
       "s5ChasComERS4526T-PWR-PLUSPwr-RedundFeed": s5ChasComERS4526T_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4550T-PWR-PLUSPwr": s5ChasComERS4550T_PWR_PLUSPwr,
       "s5ChasComERS4550T-PWR-PLUSPwr-Main": s5ChasComERS4550T_PWR_PLUSPwr_Main,
       "s5ChasComERS4550T-PWR-PLUSPwr-RedundFeed": s5ChasComERS4550T_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4826GTS-PWR-PLUSPwr": s5ChasComERS4826GTS_PWR_PLUSPwr,
       "s5ChasComERS4826GTS-PWR-PLUSPwr-Main": s5ChasComERS4826GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS4826GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS4826GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4850GTS-PWR-PLUSPwr": s5ChasComERS4850GTS_PWR_PLUSPwr,
       "s5ChasComERS4850GTS-PWR-PLUSPwr-Main": s5ChasComERS4850GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS4850GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS4850GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4826GTSPwr": s5ChasComERS4826GTSPwr,
       "s5ChasComERS4826GTSPwr-Main": s5ChasComERS4826GTSPwr_Main,
       "s5ChasComERS4826GTSPwr-RedundFeed": s5ChasComERS4826GTSPwr_RedundFeed,
       "s5ChasComERS4850GTSPwr": s5ChasComERS4850GTSPwr,
       "s5ChasComERS4850GTSPwr-Main": s5ChasComERS4850GTSPwr_Main,
       "s5ChasComERS4850GTSPwr-RedundFeed": s5ChasComERS4850GTSPwr_RedundFeed,
       "s5ChasComVSP7024XLSPwr": s5ChasComVSP7024XLSPwr,
       "s5ChasComVSP7024XLSPwr-Main": s5ChasComVSP7024XLSPwr_Main,
       "s5ChasComVSP7024XLSPwr-RedundFeed": s5ChasComVSP7024XLSPwr_RedundFeed,
       "s5ChasComERS3510GTPwr": s5ChasComERS3510GTPwr,
       "s5ChasComERS3510GTPwr-Main": s5ChasComERS3510GTPwr_Main,
       "s5ChasComERS3510GTPwr-RedundFeed": s5ChasComERS3510GTPwr_RedundFeed,
       "s5ChasComERS3510GT-PWR-PLUSPwr": s5ChasComERS3510GT_PWR_PLUSPwr,
       "s5ChasComERS3510GT-PWR-PLUSPwr-Main": s5ChasComERS3510GT_PWR_PLUSPwr_Main,
       "s5ChasComERS3510GT-PWR-PLUSPwr-RedundFeed": s5ChasComERS3510GT_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS3524GTPwr": s5ChasComERS3524GTPwr,
       "s5ChasComERS3524GTPwr-Main": s5ChasComERS3524GTPwr_Main,
       "s5ChasComERS3524GTPwr-RedundFeed": s5ChasComERS3524GTPwr_RedundFeed,
       "s5ChasComERS3524GT-PWR-PLUSPwr": s5ChasComERS3524GT_PWR_PLUSPwr,
       "s5ChasComERS3524GT-PWR-PLUSPwr-Main": s5ChasComERS3524GT_PWR_PLUSPwr_Main,
       "s5ChasComERS3524GT-PWR-PLUSPwr-RedundFeed": s5ChasComERS3524GT_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS3526GTPwr": s5ChasComERS3526GTPwr,
       "s5ChasComERS3526GTPwr-Main": s5ChasComERS3526GTPwr_Main,
       "s5ChasComERS3526GTPwr-RedundFeed": s5ChasComERS3526GTPwr_RedundFeed,
       "s5ChasComERS3526GT-PWR-PLUSPwr": s5ChasComERS3526GT_PWR_PLUSPwr,
       "s5ChasComERS3526GT-PWR-PLUSPwr-Main": s5ChasComERS3526GT_PWR_PLUSPwr_Main,
       "s5ChasComERS3526GT-PWR-PLUSPwr-RedundFeed": s5ChasComERS3526GT_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS3526TPwr": s5ChasComERS3526TPwr,
       "s5ChasComERS3526TPwr-Main": s5ChasComERS3526TPwr_Main,
       "s5ChasComERS3526TPwr-RedundFeed": s5ChasComERS3526TPwr_RedundFeed,
       "s5ChasComERS3526T-PWR-PLUSPwr": s5ChasComERS3526T_PWR_PLUSPwr,
       "s5ChasComERS3526T-PWR-PLUSPwr-Main": s5ChasComERS3526T_PWR_PLUSPwr_Main,
       "s5ChasComERS3526T-PWR-PLUSPwr-RedundFeed": s5ChasComERS3526T_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS3549GTSPwr": s5ChasComERS3549GTSPwr,
       "s5ChasComERS3549GTSPwr-Main": s5ChasComERS3549GTSPwr_Main,
       "s5ChasComERS3549GTS-PWR-PLUSPwr": s5ChasComERS3549GTS_PWR_PLUSPwr,
       "s5ChasComERS3549GTS-PWR-PLUSPwr-Main": s5ChasComERS3549GTS_PWR_PLUSPwr_Main,
       "s5ChasComVSP7024XTPwr": s5ChasComVSP7024XTPwr,
       "s5ChasComVSP7024XTPwr-Main": s5ChasComVSP7024XTPwr_Main,
       "s5ChasComVSP7024XTPwr-RedundFeed": s5ChasComVSP7024XTPwr_RedundFeed,
       "s5ChasComERS5928GTSPwr": s5ChasComERS5928GTSPwr,
       "s5ChasComERS5928GTSPwr-Main": s5ChasComERS5928GTSPwr_Main,
       "s5ChasComERS5928GTSPwr-RedundFeed": s5ChasComERS5928GTSPwr_RedundFeed,
       "s5ChasComERS5928GTS-PWR-PLUSPwr": s5ChasComERS5928GTS_PWR_PLUSPwr,
       "s5ChasComERS5928GTS-PWR-PLUSPwr-Main": s5ChasComERS5928GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS5928GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS5928GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS5952GTSPwr": s5ChasComERS5952GTSPwr,
       "s5ChasComERS5952GTSPwr-Main": s5ChasComERS5952GTSPwr_Main,
       "s5ChasComERS5952GTSPwr-RedundFeed": s5ChasComERS5952GTSPwr_RedundFeed,
       "s5ChasComERS5952GTS-PWR-PLUSPwr": s5ChasComERS5952GTS_PWR_PLUSPwr,
       "s5ChasComERS5952GTS-PWR-PLUSPwr-Main": s5ChasComERS5952GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS5952GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS5952GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS5928GTS-UPWRPwr": s5ChasComERS5928GTS_UPWRPwr,
       "s5ChasComERS5928GTS-UPWRPwr-Main": s5ChasComERS5928GTS_UPWRPwr_Main,
       "s5ChasComERS5928GTS-UPWRPwr-RedundFeed": s5ChasComERS5928GTS_UPWRPwr_RedundFeed,
       "s5ChasComERS59100GTSPwr": s5ChasComERS59100GTSPwr,
       "s5ChasComERS59100GTSPwr-Main": s5ChasComERS59100GTSPwr_Main,
       "s5ChasComERS59100GTSPwr-RedundFeed": s5ChasComERS59100GTSPwr_RedundFeed,
       "s5ChasComERS59100GTS-PWR-PLUSPwr": s5ChasComERS59100GTS_PWR_PLUSPwr,
       "s5ChasComERS59100GTS-PWR-PLUSPwr-Main": s5ChasComERS59100GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS59100GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS59100GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4926GTSPwr": s5ChasComERS4926GTSPwr,
       "s5ChasComERS4926GTSPwr-Main": s5ChasComERS4926GTSPwr_Main,
       "s5ChasComERS4926GTSPwr-RedundFeed": s5ChasComERS4926GTSPwr_RedundFeed,
       "s5ChasComERS4926GTS-PWR-PLUSPwr": s5ChasComERS4926GTS_PWR_PLUSPwr,
       "s5ChasComERS4926GTS-PWR-PLUSPwr-Main": s5ChasComERS4926GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS4926GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS4926GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS4950GTSPwr": s5ChasComERS4950GTSPwr,
       "s5ChasComERS4950GTSPwr-Main": s5ChasComERS4950GTSPwr_Main,
       "s5ChasComERS4950GTSPwr-RedundFeed": s5ChasComERS4950GTSPwr_RedundFeed,
       "s5ChasComERS4950GTS-PWR-PLUSPwr": s5ChasComERS4950GTS_PWR_PLUSPwr,
       "s5ChasComERS4950GTS-PWR-PLUSPwr-Main": s5ChasComERS4950GTS_PWR_PLUSPwr_Main,
       "s5ChasComERS4950GTS-PWR-PLUSPwr-RedundFeed": s5ChasComERS4950GTS_PWR_PLUSPwr_RedundFeed,
       "s5ChasComERS3550TPwr": s5ChasComERS3550TPwr,
       "s5ChasComERS3550TPwr-Main": s5ChasComERS3550TPwr_Main,
       "s5ChasComERS3550T-PWR-PLUSPwr": s5ChasComERS3550T_PWR_PLUSPwr,
       "s5ChasComERS3550T-PWR-PLUSPwr-Main": s5ChasComERS3550T_PWR_PLUSPwr_Main,
       "s5ChasComMTmpSnr": s5ChasComMTmpSnr,
       "s5ChasComM5000TmpSnr": s5ChasComM5000TmpSnr,
       "s5ChasComM5000TmpSnrA": s5ChasComM5000TmpSnrA,
       "s5ChasComM5005TmpSnr": s5ChasComM5005TmpSnr,
       "s5ChasComM5005TmpSnrA": s5ChasComM5005TmpSnrA,
       "s5ChasComESU1860STmpSnr": s5ChasComESU1860STmpSnr,
       "s5ChasComESU1860STmpSnrCPU": s5ChasComESU1860STmpSnrCPU,
       "s5ChasComESU1860STmpSnrBoard1": s5ChasComESU1860STmpSnrBoard1,
       "s5ChasComESU1860STmpSnrBoard2": s5ChasComESU1860STmpSnrBoard2,
       "s5ChasComESU1860BTmpSnr": s5ChasComESU1860BTmpSnr,
       "s5ChasComESU1860BTmpSnrCPU": s5ChasComESU1860BTmpSnrCPU,
       "s5ChasComESU1860BTmpSnrBoard1": s5ChasComESU1860BTmpSnrBoard1,
       "s5ChasComESU1860BTmpSnrBoard2": s5ChasComESU1860BTmpSnrBoard2,
       "s5ChasComESU1860TTmpSnr": s5ChasComESU1860TTmpSnr,
       "s5ChasComESU1860TTmpSnrCPU": s5ChasComESU1860TTmpSnrCPU,
       "s5ChasComESU1860TTmpSnrBoard1": s5ChasComESU1860TTmpSnrBoard1,
       "s5ChasComESU1860TTmpSnrBoard2": s5ChasComESU1860TTmpSnrBoard2,
       "s5ChasComESU1860VTmpSnr": s5ChasComESU1860VTmpSnr,
       "s5ChasComESU1860VTmpSnrCPU": s5ChasComESU1860VTmpSnrCPU,
       "s5ChasComESU1860VTmpSnrBoard1": s5ChasComESU1860VTmpSnrBoard1,
       "s5ChasComESU1860VTmpSnrBoard2": s5ChasComESU1860VTmpSnrBoard2,
       "s5ChasComESU1880STmpSnr": s5ChasComESU1880STmpSnr,
       "s5ChasComESU1880STmpSnrCPU": s5ChasComESU1880STmpSnrCPU,
       "s5ChasComESU1880STmpSnrBoard1": s5ChasComESU1880STmpSnrBoard1,
       "s5ChasComESU1880STmpSnrBoard2": s5ChasComESU1880STmpSnrBoard2,
       "s5ChasComMFan": s5ChasComMFan,
       "s5ChasComM5000Fan": s5ChasComM5000Fan,
       "s5ChasComM5000FanA": s5ChasComM5000FanA,
       "s5ChasComM5000FanAA": s5ChasComM5000FanAA,
       "s5ChasComM1032xFan": s5ChasComM1032xFan,
       "s5ChasComM1032xFanA": s5ChasComM1032xFanA,
       "s5ChasComM5005Fan": s5ChasComM5005Fan,
       "s5ChasComM5005FanA": s5ChasComM5005FanA,
       "s5ChasComM5DN000Fan": s5ChasComM5DN000Fan,
       "s5ChasComM5DN002Fan-1U": s5ChasComM5DN002Fan_1U,
       "s5ChasComM5DN003Fan-2U": s5ChasComM5DN003Fan_2U,
       "s5ChasComMNBayStackFan": s5ChasComMNBayStackFan,
       "s5ChasComMNBayStackFanA": s5ChasComMNBayStackFanA,
       "s5ChasComMBayStack100Fan": s5ChasComMBayStack100Fan,
       "s5ChasComMBayStack100FanA": s5ChasComMBayStack100FanA,
       "s5ChasComM3000Fan": s5ChasComM3000Fan,
       "s5ChasComM3000FanA": s5ChasComM3000FanA,
       "s5ChasComM28200Fan": s5ChasComM28200Fan,
       "s5ChasComM28200FanA": s5ChasComM28200FanA,
       "s5ChasComMBayStack301Fan": s5ChasComMBayStack301Fan,
       "s5ChasComMBayStack301FanA": s5ChasComMBayStack301FanA,
       "s5ChasComSwitchNodeFan": s5ChasComSwitchNodeFan,
       "s5ChasComMBayStackTrFan": s5ChasComMBayStackTrFan,
       "s5ChasComMBayStackTrFanA": s5ChasComMBayStackTrFanA,
       "s5ChasComBayStack150Fan": s5ChasComBayStack150Fan,
       "s5ChasComBayStack150MasterFan": s5ChasComBayStack150MasterFan,
       "s5ChasComMBayStack303-304Fan": s5ChasComMBayStack303_304Fan,
       "s5ChasComBayStack200Fan": s5ChasComBayStack200Fan,
       "s5ChasComBayStack200MasterFan": s5ChasComBayStack200MasterFan,
       "s5ChasComBayStack250Fan": s5ChasComBayStack250Fan,
       "s5ChasComBayStack250MasterFan": s5ChasComBayStack250MasterFan,
       "s5ChasComBayStack250SlaveFan": s5ChasComBayStack250SlaveFan,
       "s5ChasComMAccelar8010Fan": s5ChasComMAccelar8010Fan,
       "s5ChasComBPS2000Fan": s5ChasComBPS2000Fan,
       "s5ChasComBPS2000UnitFan": s5ChasComBPS2000UnitFan,
       "s5ChasComBayStack450Fan": s5ChasComBayStack450Fan,
       "s5ChasComBayStack450UnitFan": s5ChasComBayStack450UnitFan,
       "s5ChasComBayStack450RedundPwrFan": s5ChasComBayStack450RedundPwrFan,
       "s5ChasComBayStack3580Fan": s5ChasComBayStack3580Fan,
       "s5ChasComBayStack3580UnitFan": s5ChasComBayStack3580UnitFan,
       "s5ChasComBayStack420Fan": s5ChasComBayStack420Fan,
       "s5ChasComMetro1200ESMFan": s5ChasComMetro1200ESMFan,
       "s5ChasComMetro1200ESMUnitFan": s5ChasComMetro1200ESMUnitFan,
       "s5ChasComBayStack380Fan": s5ChasComBayStack380Fan,
       "s5ChasComBayStack380UnitFan": s5ChasComBayStack380UnitFan,
       "s5ChasComBayStack470Fan": s5ChasComBayStack470Fan,
       "s5ChasComBayStack470UnitFan": s5ChasComBayStack470UnitFan,
       "s5ChasComMetro1450ESMFan": s5ChasComMetro1450ESMFan,
       "s5ChasComMetro1450ESMUnitFan": s5ChasComMetro1450ESMUnitFan,
       "s5ChasComMetro1400ESMFan": s5ChasComMetro1400ESMFan,
       "s5ChasComMetro1400ESMUnitFan": s5ChasComMetro1400ESMUnitFan,
       "s5ChasComBayStack460-24T-PWRFan": s5ChasComBayStack460_24T_PWRFan,
       "s5ChasComBayStack460-24T-PWRUnitFan": s5ChasComBayStack460_24T_PWRUnitFan,
       "s5ChasComBayStack380-24F-Fan": s5ChasComBayStack380_24F_Fan,
       "s5ChasComBayStack380-24FUnitFan": s5ChasComBayStack380_24FUnitFan,
       "s5ChasComBayStack5510-24TFan": s5ChasComBayStack5510_24TFan,
       "s5ChasComBayStack5510-24TUnitFan": s5ChasComBayStack5510_24TUnitFan,
       "s5ChasComBayStack5510-48TFan": s5ChasComBayStack5510_48TFan,
       "s5ChasComBayStack5510-48TUnitFan": s5ChasComBayStack5510_48TUnitFan,
       "s5ChasComBayStack470-24TFan": s5ChasComBayStack470_24TFan,
       "s5ChasComBayStack470-24TUnitFan": s5ChasComBayStack470_24TUnitFan,
       "s5ChasComWLANAccessPoint2220Fan": s5ChasComWLANAccessPoint2220Fan,
       "s5ChasComWLANAccessPoint2220UnitFan": s5ChasComWLANAccessPoint2220UnitFan,
       "s5ChasComWLANSecuritySwitch2250Fan": s5ChasComWLANSecuritySwitch2250Fan,
       "s5ChasComWLANSecuritySwitch2250UnitFan": s5ChasComWLANSecuritySwitch2250UnitFan,
       "s5ChasComBayStack425Fan": s5ChasComBayStack425Fan,
       "s5ChasComBayStack425UnitFan": s5ChasComBayStack425UnitFan,
       "s5ChasComWLANAccessPoint2221Fan": s5ChasComWLANAccessPoint2221Fan,
       "s5ChasComWLANAccessPoint2221UnitFan": s5ChasComWLANAccessPoint2221UnitFan,
       "s5ChasComBayStack5520-24T-PWRFan": s5ChasComBayStack5520_24T_PWRFan,
       "s5ChasComBayStack5520-24T-PWRUnitFan": s5ChasComBayStack5520_24T_PWRUnitFan,
       "s5ChasComBayStack5520-48T-PWRFan": s5ChasComBayStack5520_48T_PWRFan,
       "s5ChasComBayStack5520-48T-PWRUnitFan": s5ChasComBayStack5520_48T_PWRUnitFan,
       "s5ChasComBayStack325Fan": s5ChasComBayStack325Fan,
       "s5ChasComBayStack325UnitFan": s5ChasComBayStack325UnitFan,
       "s5ChasComWLANAccessPoint2225Fan": s5ChasComWLANAccessPoint2225Fan,
       "s5ChasComWLANAccessPoint2225UnitFan": s5ChasComWLANAccessPoint2225UnitFan,
       "s5ChasComBayStack470-24T-PWRFan": s5ChasComBayStack470_24T_PWRFan,
       "s5ChasComBayStack470-24T-PWRUnitFan": s5ChasComBayStack470_24T_PWRUnitFan,
       "s5ChasComBayStack470-48T-PWRFan": s5ChasComBayStack470_48T_PWRFan,
       "s5ChasComBayStack470-48T-PWRUnitFan": s5ChasComBayStack470_48T_PWRUnitFan,
       "s5ChasComWLANSecuritySwitch2270Fan": s5ChasComWLANSecuritySwitch2270Fan,
       "s5ChasComWLANSecuritySwitch2270UnitFan": s5ChasComWLANSecuritySwitch2270UnitFan,
       "s5ChasComEthernetRoutingSwitch5530-24TFDFan": s5ChasComEthernetRoutingSwitch5530_24TFDFan,
       "s5ChasComEthernetRoutingSwitch5530-24TFDUnitFan": s5ChasComEthernetRoutingSwitch5530_24TFDUnitFan,
       "s5ChasComEthernetSwitch3510-24TFan": s5ChasComEthernetSwitch3510_24TFan,
       "s5ChasComEthernetSwitch3510-24TUnitFan": s5ChasComEthernetSwitch3510_24TUnitFan,
       "s5ChasComBES1010-24TFan": s5ChasComBES1010_24TFan,
       "s5ChasComBES1010-24TUnitFan": s5ChasComBES1010_24TUnitFan,
       "s5ChasComBES1010-48TFan": s5ChasComBES1010_48TFan,
       "s5ChasComBES1010-48TUnitFan": s5ChasComBES1010_48TUnitFan,
       "s5ChasComBES1020-24T-PWRFan": s5ChasComBES1020_24T_PWRFan,
       "s5ChasComBES1020-24T-PWRUnitFan": s5ChasComBES1020_24T_PWRUnitFan,
       "s5ChasComBES1020-48T-PWRFan": s5ChasComBES1020_48T_PWRFan,
       "s5ChasComBES1020-48T-PWRUnitFan": s5ChasComBES1020_48T_PWRUnitFan,
       "s5ChasComBES2010-24TFan": s5ChasComBES2010_24TFan,
       "s5ChasComBES2010-24TUnitFan": s5ChasComBES2010_24TUnitFan,
       "s5ChasComBES2010-48TFan": s5ChasComBES2010_48TFan,
       "s5ChasComBES2010-48TUnitFan": s5ChasComBES2010_48TUnitFan,
       "s5ChasComBES2020-24T-PWRFan": s5ChasComBES2020_24T_PWRFan,
       "s5ChasComBES2020-24T-PWRUnitFan": s5ChasComBES2020_24T_PWRUnitFan,
       "s5ChasComBES2020-48T-PWRFan": s5ChasComBES2020_48T_PWRFan,
       "s5ChasComBES2020-48T-PWRUnitFan": s5ChasComBES2020_48T_PWRUnitFan,
       "s5ChasComBES110-24TFan": s5ChasComBES110_24TFan,
       "s5ChasComBES110-24TUnitFan": s5ChasComBES110_24TUnitFan,
       "s5ChasComBES110-48TFan": s5ChasComBES110_48TFan,
       "s5ChasComBES110-48TUnitFan": s5ChasComBES110_48TUnitFan,
       "s5ChasComBES120-24T-PWRFan": s5ChasComBES120_24T_PWRFan,
       "s5ChasComBES120-24T-PWRUnitFan": s5ChasComBES120_24T_PWRUnitFan,
       "s5ChasComBES120-48T-PWRFan": s5ChasComBES120_48T_PWRFan,
       "s5ChasComBES120-48T-PWRUnitFan": s5ChasComBES120_48T_PWRUnitFan,
       "s5ChasComBES210-24TFan": s5ChasComBES210_24TFan,
       "s5ChasComBES210-24TUnitFan": s5ChasComBES210_24TUnitFan,
       "s5ChasComBES210-48TFan": s5ChasComBES210_48TFan,
       "s5ChasComBES210-48TUnitFan": s5ChasComBES210_48TUnitFan,
       "s5ChasComBES220-24T-PWRFan": s5ChasComBES220_24T_PWRFan,
       "s5ChasComBES220-24T-PWRUnitFan": s5ChasComBES220_24T_PWRUnitFan,
       "s5ChasComBES220-48T-PWRFan": s5ChasComBES220_48T_PWRFan,
       "s5ChasComBES220-48T-PWRUnitFan": s5ChasComBES220_48T_PWRUnitFan,
       "s5ChasComERS4548GTFan": s5ChasComERS4548GTFan,
       "s5ChasComERS4548GTUnitFan": s5ChasComERS4548GTUnitFan,
       "s5ChasComERS4548GT-PWRFan": s5ChasComERS4548GT_PWRFan,
       "s5ChasComERS4548GT-PWRUnitFan": s5ChasComERS4548GT_PWRUnitFan,
       "s5ChasComERS4550TFan": s5ChasComERS4550TFan,
       "s5ChasComERS4550TUnitFan": s5ChasComERS4550TUnitFan,
       "s5ChasComERS4550T-PWRFan": s5ChasComERS4550T_PWRFan,
       "s5ChasComERS4550T-PWRUnitFan": s5ChasComERS4550T_PWRUnitFan,
       "s5ChasComERS4526FXFan": s5ChasComERS4526FXFan,
       "s5ChasComERS4526FXUnitFan": s5ChasComERS4526FXUnitFan,
       "s5ChasComERS2500-26TFan": s5ChasComERS2500_26TFan,
       "s5ChasComERS2500-26TUnitFan": s5ChasComERS2500_26TUnitFan,
       "s5ChasComERS2500-26T-PWRFan": s5ChasComERS2500_26T_PWRFan,
       "s5ChasComERS2500-26T-PWRUnitFan": s5ChasComERS2500_26T_PWRUnitFan,
       "s5ChasComERS2500-50TFan": s5ChasComERS2500_50TFan,
       "s5ChasComERS2500-50TUnitFan": s5ChasComERS2500_50TUnitFan,
       "s5ChasComERS2500-50T-PWRFan": s5ChasComERS2500_50T_PWRFan,
       "s5ChasComERS2500-50T-PWRUnitFan": s5ChasComERS2500_50T_PWRUnitFan,
       "s5ChasComERS4526GTX-PWRFan": s5ChasComERS4526GTX_PWRFan,
       "s5ChasComERS4526GTX-PWRUnitFan": s5ChasComERS4526GTX_PWRUnitFan,
       "s5ChasComERS4526GTXFan": s5ChasComERS4526GTXFan,
       "s5ChasComERS4526GTXUnitFan": s5ChasComERS4526GTXUnitFan,
       "s5ChasComERS4524GTFan": s5ChasComERS4524GTFan,
       "s5ChasComERS4524GTUnitFan": s5ChasComERS4524GTUnitFan,
       "s5ChasComERS4526TFan": s5ChasComERS4526TFan,
       "s5ChasComERS4526TUnitFan": s5ChasComERS4526TUnitFan,
       "s5ChasComERS4526T-PWRFan": s5ChasComERS4526T_PWRFan,
       "s5ChasComERS4526T-PWRUnitFan": s5ChasComERS4526T_PWRUnitFan,
       "s5ChasComERS5698-TFD-PWRFan": s5ChasComERS5698_TFD_PWRFan,
       "s5ChasComERS5698-TFD-PWRUnitFan": s5ChasComERS5698_TFD_PWRUnitFan,
       "s5ChasComERS5698-TFDFan": s5ChasComERS5698_TFDFan,
       "s5ChasComERS5698-TFDUnitFan": s5ChasComERS5698_TFDUnitFan,
       "s5ChasComERS5650-TD-PWRFan": s5ChasComERS5650_TD_PWRFan,
       "s5ChasComERS5650-TD-PWRUnitFan": s5ChasComERS5650_TD_PWRUnitFan,
       "s5ChasComERS5650-TDFan": s5ChasComERS5650_TDFan,
       "s5ChasComERS5650-TDUnitFan": s5ChasComERS5650_TDUnitFan,
       "s5ChasComERS5632-FDFan": s5ChasComERS5632_FDFan,
       "s5ChasComERS5632-FDUnitFan": s5ChasComERS5632_FDUnitFan,
       "s5ChasComESU1860SFan": s5ChasComESU1860SFan,
       "s5ChasComESU1860SUnitFan": s5ChasComESU1860SUnitFan,
       "s5ChasComESU1860BFan": s5ChasComESU1860BFan,
       "s5ChasComESU1860BUnitFan": s5ChasComESU1860BUnitFan,
       "s5ChasComESU1860TFan": s5ChasComESU1860TFan,
       "s5ChasComESU1860TUnitFan": s5ChasComESU1860TUnitFan,
       "s5ChasComESU1860VFan": s5ChasComESU1860VFan,
       "s5ChasComESU1860VUnitFan": s5ChasComESU1860VUnitFan,
       "s5ChasComESU1880SFan": s5ChasComESU1880SFan,
       "s5ChasComESU1880SUnitFan": s5ChasComESU1880SUnitFan,
       "s5ChasComERS4524GT-PWRFan": s5ChasComERS4524GT_PWRFan,
       "s5ChasComERS4524GT-PWRUnitFan": s5ChasComERS4524GT_PWRUnitFan,
       "s5ChasComERS6628XSGTFan": s5ChasComERS6628XSGTFan,
       "s5ChasComERS6628XSGTUnitFan": s5ChasComERS6628XSGTUnitFan,
       "s5ChasComERS6632XTSFan": s5ChasComERS6632XTSFan,
       "s5ChasComERS6632XTSUnitFan": s5ChasComERS6632XTSUnitFan,
       "s5ChasComWC8180Fan": s5ChasComWC8180Fan,
       "s5ChasComWC8180UnitFan": s5ChasComWC8180UnitFan,
       "s5ChasComERS4526T-PWR-PLUSFan": s5ChasComERS4526T_PWR_PLUSFan,
       "s5ChasComERS4526T-PWR-PLUSUnitFan": s5ChasComERS4526T_PWR_PLUSUnitFan,
       "s5ChasComERS4550T-PWR-PLUSFan": s5ChasComERS4550T_PWR_PLUSFan,
       "s5ChasComERS4550T-PWR-PLUSUnitFan": s5ChasComERS4550T_PWR_PLUSUnitFan,
       "s5ChasComERS4826GTS-PWR-PLUSFan": s5ChasComERS4826GTS_PWR_PLUSFan,
       "s5ChasComERS4826GTS-PWR-PLUSUnitFan": s5ChasComERS4826GTS_PWR_PLUSUnitFan,
       "s5ChasComERS4850GTS-PWR-PLUSFan": s5ChasComERS4850GTS_PWR_PLUSFan,
       "s5ChasComERS4850GTS-PWR-PLUSUnitFan": s5ChasComERS4850GTS_PWR_PLUSUnitFan,
       "s5ChasComERS4826GTSFan": s5ChasComERS4826GTSFan,
       "s5ChasComERS4826GTSUnitFan": s5ChasComERS4826GTSUnitFan,
       "s5ChasComERS4850GTSFan": s5ChasComERS4850GTSFan,
       "s5ChasComERS4850GTSUnitFan": s5ChasComERS4850GTSUnitFan,
       "s5ChasComVSP7024XLSFan": s5ChasComVSP7024XLSFan,
       "s5ChasComVSP7024XLSUnitFan": s5ChasComVSP7024XLSUnitFan,
       "s5ChasComERS3510GTFan": s5ChasComERS3510GTFan,
       "s5ChasComERS3510GTUnitFan": s5ChasComERS3510GTUnitFan,
       "s5ChasComERS3510GT-PWR-PLUSFan": s5ChasComERS3510GT_PWR_PLUSFan,
       "s5ChasComERS3510GT-PWR-PLUSUnitFan": s5ChasComERS3510GT_PWR_PLUSUnitFan,
       "s5ChasComERS3524GTFan": s5ChasComERS3524GTFan,
       "s5ChasComERS3524GTUnitFan": s5ChasComERS3524GTUnitFan,
       "s5ChasComERS3524GT-PWR-PLUSFan": s5ChasComERS3524GT_PWR_PLUSFan,
       "s5ChasComERS3524GT-PWR-PLUSUnitFan": s5ChasComERS3524GT_PWR_PLUSUnitFan,
       "s5ChasComERS3526GTFan": s5ChasComERS3526GTFan,
       "s5ChasComERS3526GTUnitFan": s5ChasComERS3526GTUnitFan,
       "s5ChasComERS3526GT-PWR-PLUSFan": s5ChasComERS3526GT_PWR_PLUSFan,
       "s5ChasComERS3526GT-PWR-PLUSUnitFan": s5ChasComERS3526GT_PWR_PLUSUnitFan,
       "s5ChasComERS3526TFan": s5ChasComERS3526TFan,
       "s5ChasComERS3526TUnitFan": s5ChasComERS3526TUnitFan,
       "s5ChasComERS3526T-PWR-PLUSFan": s5ChasComERS3526T_PWR_PLUSFan,
       "s5ChasComERS3526T-PWR-PLUSUnitFan": s5ChasComERS3526T_PWR_PLUSUnitFan,
       "s5ChasComERS3549GTSFan": s5ChasComERS3549GTSFan,
       "s5ChasComERS3549GTSUnitFan1": s5ChasComERS3549GTSUnitFan1,
       "s5ChasComERS3549GTSUnitFan2": s5ChasComERS3549GTSUnitFan2,
       "s5ChasComERS3549GTS-PWR-PLUSFan": s5ChasComERS3549GTS_PWR_PLUSFan,
       "s5ChasComERS3549GTS-PWR-PLUSUnitFan1": s5ChasComERS3549GTS_PWR_PLUSUnitFan1,
       "s5ChasComERS3549GTS-PWR-PLUSUnitFan2": s5ChasComERS3549GTS_PWR_PLUSUnitFan2,
       "s5ChasComERS3549GTS-PWR-PLUSUnitFan3": s5ChasComERS3549GTS_PWR_PLUSUnitFan3,
       "s5ChasComERS3549GTS-PWR-PLUSUnitFan4": s5ChasComERS3549GTS_PWR_PLUSUnitFan4,
       "s5ChasComVSP7024XTFan": s5ChasComVSP7024XTFan,
       "s5ChasComVSP7024XTUnitFan": s5ChasComVSP7024XTUnitFan,
       "s5ChasComERS5928GTSFan": s5ChasComERS5928GTSFan,
       "s5ChasComERS5928GTSUnitFan": s5ChasComERS5928GTSUnitFan,
       "s5ChasComERS5928GTS-PWR-PLUSFan": s5ChasComERS5928GTS_PWR_PLUSFan,
       "s5ChasComERS5928GTS-PWR-PLUSUnitFan": s5ChasComERS5928GTS_PWR_PLUSUnitFan,
       "s5ChasComERS5952GTSFan": s5ChasComERS5952GTSFan,
       "s5ChasComERS5952GTSUnitFan": s5ChasComERS5952GTSUnitFan,
       "s5ChasComERS5952GTS-PWR-PLUSFan": s5ChasComERS5952GTS_PWR_PLUSFan,
       "s5ChasComERS5952GTS-PWR-PLUSUnitFan": s5ChasComERS5952GTS_PWR_PLUSUnitFan,
       "s5ChasComERS5928GTS-UPWRFan": s5ChasComERS5928GTS_UPWRFan,
       "s5ChasComERS5928GTS-UPWRUnitFan": s5ChasComERS5928GTS_UPWRUnitFan,
       "s5ChasComERS59100GTSFan": s5ChasComERS59100GTSFan,
       "s5ChasComERS59100GTSUnitFan": s5ChasComERS59100GTSUnitFan,
       "s5ChasComERS59100GTS-PWR-PLUSFan": s5ChasComERS59100GTS_PWR_PLUSFan,
       "s5ChasComERS59100GTS-PWR-PLUSUnitFan": s5ChasComERS59100GTS_PWR_PLUSUnitFan,
       "s5ChasComERS4926GTSFan": s5ChasComERS4926GTSFan,
       "s5ChasComERS4926GTSUnitFan": s5ChasComERS4926GTSUnitFan,
       "s5ChasComERS4926GTS-PWR-PLUSFan": s5ChasComERS4926GTS_PWR_PLUSFan,
       "s5ChasComERS4926GTS-PWR-PLUSUnitFan": s5ChasComERS4926GTS_PWR_PLUSUnitFan,
       "s5ChasComERS4950GTSFan": s5ChasComERS4950GTSFan,
       "s5ChasComERS4950GTSUnitFan": s5ChasComERS4950GTSUnitFan,
       "s5ChasComERS4950GTS-PWR-PLUSFan": s5ChasComERS4950GTS_PWR_PLUSFan,
       "s5ChasComERS4950GTS-PWR-PLUSUnitFan": s5ChasComERS4950GTS_PWR_PLUSUnitFan,
       "s5ChasComERS3550TFan": s5ChasComERS3550TFan,
       "s5ChasComERS3550TUnitFan1": s5ChasComERS3550TUnitFan1,
       "s5ChasComERS3550TUnitFan2": s5ChasComERS3550TUnitFan2,
       "s5ChasComERS3550T-PWR-PLUSFan": s5ChasComERS3550T_PWR_PLUSFan,
       "s5ChasComERS3550T-PWR-PLUSUnitFan1": s5ChasComERS3550T_PWR_PLUSUnitFan1,
       "s5ChasComERS3550T-PWR-PLUSUnitFan2": s5ChasComERS3550T_PWR_PLUSUnitFan2,
       "s5ChasComERS3550T-PWR-PLUSUnitFan3": s5ChasComERS3550T_PWR_PLUSUnitFan3,
       "s5ChasComERS3550T-PWR-PLUSUnitFan4": s5ChasComERS3550T_PWR_PLUSUnitFan4,
       "s5ChasComMClk": s5ChasComMClk,
       "s5ChasComM5000Clk": s5ChasComM5000Clk,
       "s5ChasComM5000ClkA": s5ChasComM5000ClkA,
       "s5ChasComM5005Clk": s5ChasComM5005Clk,
       "s5ChasComM5005ClkA": s5ChasComM5005ClkA,
       "s5ChasComMAccelar8010Clk": s5ChasComMAccelar8010Clk,
       "s5ChasStoreTypeReg": s5ChasStoreTypeReg,
       "s5RegMib": s5RegMib}
)
