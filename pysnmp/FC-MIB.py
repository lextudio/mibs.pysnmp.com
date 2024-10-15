# SNMP MIB module (FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:20 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fastcomm_ObjectIdentity = ObjectIdentity
fastcomm = _Fastcomm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1)
)
_FrameRelay_ObjectIdentity = ObjectIdentity
frameRelay = _FrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1, 2)
)
_FsFrad_ObjectIdentity = ObjectIdentity
fsFrad = _FsFrad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1, 2, 1)
)
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1, 3)
)


class _SnmpMibVersion_Type(DisplayString):
    """Custom type snmpMibVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnmpMibVersion_Type.__name__ = "DisplayString"
_SnmpMibVersion_Object = MibScalar
snmpMibVersion = _SnmpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 1),
    _SnmpMibVersion_Type()
)
snmpMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpMibVersion.setStatus("mandatory")
_SnmpAgentIpAddr_Type = IpAddress
_SnmpAgentIpAddr_Object = MibScalar
snmpAgentIpAddr = _SnmpAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 2),
    _SnmpAgentIpAddr_Type()
)
snmpAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentIpAddr.setStatus("mandatory")


class _SnmpAgentName_Type(DisplayString):
    """Custom type snmpAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SnmpAgentName_Type.__name__ = "DisplayString"
_SnmpAgentName_Object = MibScalar
snmpAgentName = _SnmpAgentName_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 3),
    _SnmpAgentName_Type()
)
snmpAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentName.setStatus("mandatory")


class _SnmpAgentGetCommunity_Type(DisplayString):
    """Custom type snmpAgentGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnmpAgentGetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentGetCommunity_Object = MibScalar
snmpAgentGetCommunity = _SnmpAgentGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 4),
    _SnmpAgentGetCommunity_Type()
)
snmpAgentGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentGetCommunity.setStatus("mandatory")


class _SnmpAgentSetCommunity_Type(DisplayString):
    """Custom type snmpAgentSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnmpAgentSetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentSetCommunity_Object = MibScalar
snmpAgentSetCommunity = _SnmpAgentSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 5),
    _SnmpAgentSetCommunity_Type()
)
snmpAgentSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentSetCommunity.setStatus("mandatory")
_SnmpAgentDefaultTrapIpAddr_Type = IpAddress
_SnmpAgentDefaultTrapIpAddr_Object = MibScalar
snmpAgentDefaultTrapIpAddr = _SnmpAgentDefaultTrapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 6),
    _SnmpAgentDefaultTrapIpAddr_Type()
)
snmpAgentDefaultTrapIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentDefaultTrapIpAddr.setStatus("mandatory")
_SnmpAgentTrapSendTable_Object = MibTable
snmpAgentTrapSendTable = _SnmpAgentTrapSendTable_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 7)
)
if mibBuilder.loadTexts:
    snmpAgentTrapSendTable.setStatus("mandatory")
_SnmpAgentTrapTableEntry_Object = MibTableRow
snmpAgentTrapTableEntry = _SnmpAgentTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 7, 1)
)
snmpAgentTrapTableEntry.setIndexNames(
    (0, "FC-MIB", "trapTableIndex"),
)
if mibBuilder.loadTexts:
    snmpAgentTrapTableEntry.setStatus("mandatory")
_TrapTableIndex_Type = Integer32
_TrapTableIndex_Object = MibTableColumn
trapTableIndex = _TrapTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 7, 1, 1),
    _TrapTableIndex_Type()
)
trapTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTableIndex.setStatus("mandatory")
_TrapSendIPAddress_Type = IpAddress
_TrapSendIPAddress_Object = MibTableColumn
trapSendIPAddress = _TrapSendIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 7, 1, 2),
    _TrapSendIPAddress_Type()
)
trapSendIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSendIPAddress.setStatus("mandatory")


class _TrapTableStatus_Type(Integer32):
    """Custom type trapTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("view", 1))
    )


_TrapTableStatus_Type.__name__ = "Integer32"
_TrapTableStatus_Object = MibTableColumn
trapTableStatus = _TrapTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 7, 1, 3),
    _TrapTableStatus_Type()
)
trapTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapTableStatus.setStatus("mandatory")
_SnmpAgentTrapMessageDesc_Type = DisplayString
_SnmpAgentTrapMessageDesc_Object = MibScalar
snmpAgentTrapMessageDesc = _SnmpAgentTrapMessageDesc_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 8),
    _SnmpAgentTrapMessageDesc_Type()
)
snmpAgentTrapMessageDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapMessageDesc.setStatus("mandatory")
_SnmpTrapDefineTable_Object = MibTable
snmpTrapDefineTable = _SnmpTrapDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9)
)
if mibBuilder.loadTexts:
    snmpTrapDefineTable.setStatus("mandatory")
_SnmpTrapDefineTableEntry_Object = MibTableRow
snmpTrapDefineTableEntry = _SnmpTrapDefineTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1)
)
snmpTrapDefineTableEntry.setIndexNames(
    (0, "FC-MIB", "trapDefIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapDefineTableEntry.setStatus("mandatory")
_TrapDefIndex_Type = Integer32
_TrapDefIndex_Object = MibTableColumn
trapDefIndex = _TrapDefIndex_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 1),
    _TrapDefIndex_Type()
)
trapDefIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDefIndex.setStatus("mandatory")
_TrapDefDesc_Type = DisplayString
_TrapDefDesc_Object = MibTableColumn
trapDefDesc = _TrapDefDesc_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 2),
    _TrapDefDesc_Type()
)
trapDefDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefDesc.setStatus("mandatory")
_TrapDefOid_Type = DisplayString
_TrapDefOid_Object = MibTableColumn
trapDefOid = _TrapDefOid_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 3),
    _TrapDefOid_Type()
)
trapDefOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefOid.setStatus("mandatory")


class _TrapDefTrapType_Type(Integer32):
    """Custom type trapDefTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200),
    )


_TrapDefTrapType_Type.__name__ = "Integer32"
_TrapDefTrapType_Object = MibTableColumn
trapDefTrapType = _TrapDefTrapType_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 4),
    _TrapDefTrapType_Type()
)
trapDefTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefTrapType.setStatus("mandatory")


class _TrapDefTriggerType_Type(Integer32):
    """Custom type trapDefTriggerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("range", 2),
          ("relative", 4),
          ("simple", 1),
          ("time", 3))
    )


_TrapDefTriggerType_Type.__name__ = "Integer32"
_TrapDefTriggerType_Object = MibTableColumn
trapDefTriggerType = _TrapDefTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 5),
    _TrapDefTriggerType_Type()
)
trapDefTriggerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefTriggerType.setStatus("mandatory")
_TrapDefSimpleTrigValue_Type = Integer32
_TrapDefSimpleTrigValue_Object = MibTableColumn
trapDefSimpleTrigValue = _TrapDefSimpleTrigValue_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 6),
    _TrapDefSimpleTrigValue_Type()
)
trapDefSimpleTrigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefSimpleTrigValue.setStatus("mandatory")


class _TrapDefSimpleTrigCond_Type(Integer32):
    """Custom type trapDefSimpleTrigCond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eQUAL-TO", 2),
          ("gREATER-THAN", 3),
          ("lESS-THAN", 1))
    )


_TrapDefSimpleTrigCond_Type.__name__ = "Integer32"
_TrapDefSimpleTrigCond_Object = MibTableColumn
trapDefSimpleTrigCond = _TrapDefSimpleTrigCond_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 7),
    _TrapDefSimpleTrigCond_Type()
)
trapDefSimpleTrigCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefSimpleTrigCond.setStatus("mandatory")
_TrapDefRangeValueHigh_Type = Integer32
_TrapDefRangeValueHigh_Object = MibTableColumn
trapDefRangeValueHigh = _TrapDefRangeValueHigh_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 8),
    _TrapDefRangeValueHigh_Type()
)
trapDefRangeValueHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefRangeValueHigh.setStatus("mandatory")
_TrapDefRangeValueLow_Type = Integer32
_TrapDefRangeValueLow_Object = MibTableColumn
trapDefRangeValueLow = _TrapDefRangeValueLow_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 9),
    _TrapDefRangeValueLow_Type()
)
trapDefRangeValueLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefRangeValueLow.setStatus("mandatory")
_TrapDefTimeTrigValue_Type = Integer32
_TrapDefTimeTrigValue_Object = MibTableColumn
trapDefTimeTrigValue = _TrapDefTimeTrigValue_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 10),
    _TrapDefTimeTrigValue_Type()
)
trapDefTimeTrigValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefTimeTrigValue.setStatus("mandatory")
_TrapDefTimeDuration_Type = Integer32
_TrapDefTimeDuration_Object = MibTableColumn
trapDefTimeDuration = _TrapDefTimeDuration_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 11),
    _TrapDefTimeDuration_Type()
)
trapDefTimeDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefTimeDuration.setStatus("mandatory")
_TrapDefRelativeOccur_Type = Integer32
_TrapDefRelativeOccur_Object = MibTableColumn
trapDefRelativeOccur = _TrapDefRelativeOccur_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 12),
    _TrapDefRelativeOccur_Type()
)
trapDefRelativeOccur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefRelativeOccur.setStatus("mandatory")
_TrapDefRelativeOID_Type = DisplayString
_TrapDefRelativeOID_Object = MibTableColumn
trapDefRelativeOID = _TrapDefRelativeOID_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 13),
    _TrapDefRelativeOID_Type()
)
trapDefRelativeOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefRelativeOID.setStatus("mandatory")
_TrapDefRelativeRefOccur_Type = Integer32
_TrapDefRelativeRefOccur_Object = MibTableColumn
trapDefRelativeRefOccur = _TrapDefRelativeRefOccur_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 14),
    _TrapDefRelativeRefOccur_Type()
)
trapDefRelativeRefOccur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefRelativeRefOccur.setStatus("mandatory")


class _TrapDefReTrigger_Type(Integer32):
    """Custom type trapDefReTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1))
    )


_TrapDefReTrigger_Type.__name__ = "Integer32"
_TrapDefReTrigger_Object = MibTableColumn
trapDefReTrigger = _TrapDefReTrigger_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 15),
    _TrapDefReTrigger_Type()
)
trapDefReTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefReTrigger.setStatus("mandatory")


class _TrapDefTrigPri_Type(Integer32):
    """Custom type trapDefTrigPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("normal", 1))
    )


_TrapDefTrigPri_Type.__name__ = "Integer32"
_TrapDefTrigPri_Object = MibTableColumn
trapDefTrigPri = _TrapDefTrigPri_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 16),
    _TrapDefTrigPri_Type()
)
trapDefTrigPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefTrigPri.setStatus("mandatory")


class _TrapDefStatus_Type(Integer32):
    """Custom type trapDefStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("modify", 4),
          ("view", 1))
    )


_TrapDefStatus_Type.__name__ = "Integer32"
_TrapDefStatus_Object = MibTableColumn
trapDefStatus = _TrapDefStatus_Object(
    (1, 3, 6, 1, 4, 1, 635, 1, 3, 9, 1, 17),
    _TrapDefStatus_Type()
)
trapDefStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDefStatus.setStatus("mandatory")
_FcQuick_ObjectIdentity = ObjectIdentity
fcQuick = _FcQuick_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1, 4)
)
_Quick2_ObjectIdentity = ObjectIdentity
quick2 = _Quick2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 1, 4, 1)
)
_Registration_ObjectIdentity = ObjectIdentity
registration = _Registration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2)
)
_FcFradReg_ObjectIdentity = ObjectIdentity
fcFradReg = _FcFradReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1)
)
_Fastcomm_F9100_SN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SN_NI = _Fastcomm_F9100_SN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 1)
)
_Fastcomm_F9100_SN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SN_NE = _Fastcomm_F9100_SN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 2)
)
_Fastcomm_F9100_DN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DN_NI = _Fastcomm_F9100_DN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 3)
)
_Fastcomm_F9100_DN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DN_NE = _Fastcomm_F9100_DN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 4)
)
_Fastcomm_F9100_TN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_TN_NE = _Fastcomm_F9100_TN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 5)
)
_Fastcomm_F9100_EN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_EN_NE = _Fastcomm_F9100_EN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 6)
)
_Fastcomm_F9100_SQ_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SQ_NI = _Fastcomm_F9100_SQ_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 11)
)
_Fastcomm_F9100_SQ_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SQ_NL = _Fastcomm_F9100_SQ_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 12)
)
_Fastcomm_F9100_DQ_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DQ_NI = _Fastcomm_F9100_DQ_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 13)
)
_Fastcomm_F9100_DQ_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DQ_NL = _Fastcomm_F9100_DQ_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 14)
)
_Fastcomm_F9100_SM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SM_NI = _Fastcomm_F9100_SM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 15)
)
_Fastcomm_F9100_DM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DM_NI = _Fastcomm_F9100_DM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 16)
)
_Fastcomm_F9200_SR_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SR_NI = _Fastcomm_F9200_SR_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 21)
)
_Fastcomm_F9200_SR_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SR_NL = _Fastcomm_F9200_SR_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 22)
)
_Fastcomm_F9200_DR_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DR_NI = _Fastcomm_F9200_DR_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 23)
)
_Fastcomm_F9200_DR_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DR_NL = _Fastcomm_F9200_DR_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 24)
)
_Fastcomm_F9200_SS_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SS_NI = _Fastcomm_F9200_SS_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 25)
)
_Fastcomm_F9200_SS_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SS_NE = _Fastcomm_F9200_SS_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 26)
)
_Fastcomm_F9200_DS_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DS_NI = _Fastcomm_F9200_DS_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 27)
)
_Fastcomm_F9200_DS_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DS_NE = _Fastcomm_F9200_DS_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 28)
)
_Fastcomm_F9200_SN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SN_NI = _Fastcomm_F9200_SN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 30)
)
_Fastcomm_F9200_SN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SN_NE = _Fastcomm_F9200_SN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 31)
)
_Fastcomm_F9200_DN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DN_NI = _Fastcomm_F9200_DN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 32)
)
_Fastcomm_F9200_DN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DN_NE = _Fastcomm_F9200_DN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 33)
)
_Fastcomm_F9100_SW_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SW_NI = _Fastcomm_F9100_SW_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 41)
)
_Fastcomm_F9100_SW_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SW_NL = _Fastcomm_F9100_SW_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 42)
)
_Fastcomm_F9100_DW_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DW_NI = _Fastcomm_F9100_DW_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 43)
)
_Fastcomm_F9100_DW_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DW_NL = _Fastcomm_F9100_DW_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 44)
)
_Fastcomm_F9100_SV_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SV_NI = _Fastcomm_F9100_SV_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 45)
)
_Fastcomm_F9100_SV_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SV_NE = _Fastcomm_F9100_SV_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 46)
)
_Fastcomm_F9100_DV_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DV_NI = _Fastcomm_F9100_DV_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 47)
)
_Fastcomm_F9100_DV_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DV_NE = _Fastcomm_F9100_DV_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 48)
)
_Fastcomm_F9100_SN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9100_SN_NW = _Fastcomm_F9100_SN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 50)
)
_Fastcomm_F9100_DN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9100_DN_NW = _Fastcomm_F9100_DN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 51)
)
_Fastcomm_F9200_SN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SN_NW = _Fastcomm_F9200_SN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 52)
)
_Fastcomm_F9200_DN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DN_NW = _Fastcomm_F9200_DN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 53)
)
_Fastcomm_F9200_TN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TN_NI = _Fastcomm_F9200_TN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 60)
)
_Fastcomm_F9200_TN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TN_NE = _Fastcomm_F9200_TN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 61)
)
_Fastcomm_F9200_TS_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TS_NI = _Fastcomm_F9200_TS_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 62)
)
_Fastcomm_F9200_TS_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TS_NE = _Fastcomm_F9200_TS_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 63)
)
_Fastcomm_F9200_TR_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TR_NI = _Fastcomm_F9200_TR_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 64)
)
_Fastcomm_F9200_TR_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TR_NL = _Fastcomm_F9200_TR_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 65)
)
_Fastcomm_F9200_TN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TN_NW = _Fastcomm_F9200_TN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 66)
)
_Fastcomm_F9200_TM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TM_NI = _Fastcomm_F9200_TM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 67)
)
_Fastcomm_F9200_TM_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_TM_NL = _Fastcomm_F9200_TM_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 68)
)
_Fastcomm_F9200_EN_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_EN_NI = _Fastcomm_F9200_EN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 70)
)
_Fastcomm_F9200_EN_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_EN_NE = _Fastcomm_F9200_EN_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 71)
)
_Fastcomm_F9200_ES_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ES_NI = _Fastcomm_F9200_ES_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 72)
)
_Fastcomm_F9200_ES_NE_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ES_NE = _Fastcomm_F9200_ES_NE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 73)
)
_Fastcomm_F9200_ER_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ER_NI = _Fastcomm_F9200_ER_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 74)
)
_Fastcomm_F9200_ER_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ER_NL = _Fastcomm_F9200_ER_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 75)
)
_Fastcomm_F9200_EN_NW_ObjectIdentity = ObjectIdentity
fastcomm_F9200_EN_NW = _Fastcomm_F9200_EN_NW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 76)
)
_Fastcomm_F9200_EM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_EM_NI = _Fastcomm_F9200_EM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 77)
)
_Fastcomm_F9200_EM_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_EM_NL = _Fastcomm_F9200_EM_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 78)
)
_Fastcomm_F9200_SM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SM_NI = _Fastcomm_F9200_SM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 80)
)
_Fastcomm_F9200_SM_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_SM_NL = _Fastcomm_F9200_SM_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 81)
)
_Fastcomm_F9200_DM_NI_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DM_NI = _Fastcomm_F9200_DM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 82)
)
_Fastcomm_F9200_DM_NL_ObjectIdentity = ObjectIdentity
fastcomm_F9200_DM_NL = _Fastcomm_F9200_DM_NL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 83)
)
_Fastcomm_F9900_GS_ObjectIdentity = ObjectIdentity
fastcomm_F9900_GS = _Fastcomm_F9900_GS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 1, 84)
)
_CdQuickReg_ObjectIdentity = ObjectIdentity
cdQuickReg = _CdQuickReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2)
)
_Fastcomm_F9500_S1_ObjectIdentity = ObjectIdentity
fastcomm_F9500_S1 = _Fastcomm_F9500_S1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 1)
)
_Fastcomm_F9500_S3_ObjectIdentity = ObjectIdentity
fastcomm_F9500_S3 = _Fastcomm_F9500_S3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 2)
)
_Fastcomm_F9500_S5_ObjectIdentity = ObjectIdentity
fastcomm_F9500_S5 = _Fastcomm_F9500_S5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 3)
)
_Fastcomm_F9500_D1_ObjectIdentity = ObjectIdentity
fastcomm_F9500_D1 = _Fastcomm_F9500_D1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 4)
)
_Fastcomm_F9500_D3_ObjectIdentity = ObjectIdentity
fastcomm_F9500_D3 = _Fastcomm_F9500_D3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 5)
)
_Fastcomm_F9500_D5_ObjectIdentity = ObjectIdentity
fastcomm_F9500_D5 = _Fastcomm_F9500_D5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 2, 6)
)
_FcFrad433Reg_ObjectIdentity = ObjectIdentity
fcFrad433Reg = _FcFrad433Reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3)
)
_Fastcomm_F9100_MO_NN_ObjectIdentity = ObjectIdentity
fastcomm_F9100_MO_NN = _Fastcomm_F9100_MO_NN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 1)
)
_Fastcomm_F9100_MO_NS_ObjectIdentity = ObjectIdentity
fastcomm_F9100_MO_NS = _Fastcomm_F9100_MO_NS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 2)
)
_Fastcomm_F9100_MO_NX_ObjectIdentity = ObjectIdentity
fastcomm_F9100_MO_NX = _Fastcomm_F9100_MO_NX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 3)
)
_Fastcomm_F9100_TO_KN_ObjectIdentity = ObjectIdentity
fastcomm_F9100_TO_KN = _Fastcomm_F9100_TO_KN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 4)
)
_Fastcomm_F9100_TO_KS_ObjectIdentity = ObjectIdentity
fastcomm_F9100_TO_KS = _Fastcomm_F9100_TO_KS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 5)
)
_Fastcomm_F9100_TO_KX_ObjectIdentity = ObjectIdentity
fastcomm_F9100_TO_KX = _Fastcomm_F9100_TO_KX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 6)
)
_Fastcomm_F9200_ET_HN_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ET_HN = _Fastcomm_F9200_ET_HN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 7)
)
_Fastcomm_F9200_ET_HS_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ET_HS = _Fastcomm_F9200_ET_HS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 8)
)
_Fastcomm_F9200_ET_HX_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ET_HX = _Fastcomm_F9200_ET_HX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 9)
)
_Fastcomm_F9200_IS_DS_ObjectIdentity = ObjectIdentity
fastcomm_F9200_IS_DS = _Fastcomm_F9200_IS_DS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 10)
)
_Fastcomm_F9200_IS_DX_ObjectIdentity = ObjectIdentity
fastcomm_F9200_IS_DX = _Fastcomm_F9200_IS_DX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 11)
)
_Fastcomm_F9200_ALC_ObjectIdentity = ObjectIdentity
fastcomm_F9200_ALC = _Fastcomm_F9200_ALC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 12)
)
_Fastcomm_F9200_INET_ObjectIdentity = ObjectIdentity
fastcomm_F9200_INET = _Fastcomm_F9200_INET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 13)
)
_Fastcomm_SY1_DM_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_DM_NI = _Fastcomm_SY1_DM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 14)
)
_Fastcomm_SY1_DN_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_DN_NI = _Fastcomm_SY1_DN_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 15)
)
_Fastcomm_SY1_DQ_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_DQ_NI = _Fastcomm_SY1_DQ_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 16)
)
_Fastcomm_SY1_DV_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_DV_NI = _Fastcomm_SY1_DV_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 17)
)
_Fastcomm_SY1_DW_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_DW_NI = _Fastcomm_SY1_DW_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 18)
)
_Fastcomm_SY1_SM_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_SM_NI = _Fastcomm_SY1_SM_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 19)
)
_Fastcomm_SY1_SV_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_SV_NI = _Fastcomm_SY1_SV_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 20)
)
_Fastcomm_SY1_SW_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY1_SW_NI = _Fastcomm_SY1_SW_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 21)
)
_Fastcomm_SY2_DR_NI_ObjectIdentity = ObjectIdentity
fastcomm_SY2_DR_NI = _Fastcomm_SY2_DR_NI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 22)
)
_Fastcomm_GTEDRNL_ObjectIdentity = ObjectIdentity
fastcomm_GTEDRNL = _Fastcomm_GTEDRNL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 23)
)
_Fastcomm_NETLDR_ObjectIdentity = ObjectIdentity
fastcomm_NETLDR = _Fastcomm_NETLDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 24)
)
_Fastcomm_NNOSNMP_ObjectIdentity = ObjectIdentity
fastcomm_NNOSNMP = _Fastcomm_NNOSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 25)
)
_Fastcomm_NOPPPNA_ObjectIdentity = ObjectIdentity
fastcomm_NOPPPNA = _Fastcomm_NOPPPNA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 26)
)
_Fastcomm_NOPPPNB_ObjectIdentity = ObjectIdentity
fastcomm_NOPPPNB = _Fastcomm_NOPPPNB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 27)
)
_Fastcomm_NOX25NA_ObjectIdentity = ObjectIdentity
fastcomm_NOX25NA = _Fastcomm_NOX25NA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 28)
)
_Fastcomm_NOX25NB_ObjectIdentity = ObjectIdentity
fastcomm_NOX25NB = _Fastcomm_NOX25NB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 29)
)
_Fastcomm_NTNONEA_ObjectIdentity = ObjectIdentity
fastcomm_NTNONEA = _Fastcomm_NTNONEA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 30)
)
_Fastcomm_NTNONEB_ObjectIdentity = ObjectIdentity
fastcomm_NTNONEB = _Fastcomm_NTNONEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 31)
)
_Fastcomm_PRODUCTS_ObjectIdentity = ObjectIdentity
fastcomm_PRODUCTS = _Fastcomm_PRODUCTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 2, 3, 40)
)
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 635, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FC-MIB",
    **{"fastcomm": fastcomm,
       "products": products,
       "frameRelay": frameRelay,
       "fsFrad": fsFrad,
       "snmpAgent": snmpAgent,
       "snmpMibVersion": snmpMibVersion,
       "snmpAgentIpAddr": snmpAgentIpAddr,
       "snmpAgentName": snmpAgentName,
       "snmpAgentGetCommunity": snmpAgentGetCommunity,
       "snmpAgentSetCommunity": snmpAgentSetCommunity,
       "snmpAgentDefaultTrapIpAddr": snmpAgentDefaultTrapIpAddr,
       "snmpAgentTrapSendTable": snmpAgentTrapSendTable,
       "snmpAgentTrapTableEntry": snmpAgentTrapTableEntry,
       "trapTableIndex": trapTableIndex,
       "trapSendIPAddress": trapSendIPAddress,
       "trapTableStatus": trapTableStatus,
       "snmpAgentTrapMessageDesc": snmpAgentTrapMessageDesc,
       "snmpTrapDefineTable": snmpTrapDefineTable,
       "snmpTrapDefineTableEntry": snmpTrapDefineTableEntry,
       "trapDefIndex": trapDefIndex,
       "trapDefDesc": trapDefDesc,
       "trapDefOid": trapDefOid,
       "trapDefTrapType": trapDefTrapType,
       "trapDefTriggerType": trapDefTriggerType,
       "trapDefSimpleTrigValue": trapDefSimpleTrigValue,
       "trapDefSimpleTrigCond": trapDefSimpleTrigCond,
       "trapDefRangeValueHigh": trapDefRangeValueHigh,
       "trapDefRangeValueLow": trapDefRangeValueLow,
       "trapDefTimeTrigValue": trapDefTimeTrigValue,
       "trapDefTimeDuration": trapDefTimeDuration,
       "trapDefRelativeOccur": trapDefRelativeOccur,
       "trapDefRelativeOID": trapDefRelativeOID,
       "trapDefRelativeRefOccur": trapDefRelativeRefOccur,
       "trapDefReTrigger": trapDefReTrigger,
       "trapDefTrigPri": trapDefTrigPri,
       "trapDefStatus": trapDefStatus,
       "fcQuick": fcQuick,
       "quick2": quick2,
       "registration": registration,
       "fcFradReg": fcFradReg,
       "fastcomm-F9100-SN-NI": fastcomm_F9100_SN_NI,
       "fastcomm-F9100-SN-NE": fastcomm_F9100_SN_NE,
       "fastcomm-F9100-DN-NI": fastcomm_F9100_DN_NI,
       "fastcomm-F9100-DN-NE": fastcomm_F9100_DN_NE,
       "fastcomm-F9100-TN-NE": fastcomm_F9100_TN_NE,
       "fastcomm-F9100-EN-NE": fastcomm_F9100_EN_NE,
       "fastcomm-F9100-SQ-NI": fastcomm_F9100_SQ_NI,
       "fastcomm-F9100-SQ-NL": fastcomm_F9100_SQ_NL,
       "fastcomm-F9100-DQ-NI": fastcomm_F9100_DQ_NI,
       "fastcomm-F9100-DQ-NL": fastcomm_F9100_DQ_NL,
       "fastcomm-F9100-SM-NI": fastcomm_F9100_SM_NI,
       "fastcomm-F9100-DM-NI": fastcomm_F9100_DM_NI,
       "fastcomm-F9200-SR-NI": fastcomm_F9200_SR_NI,
       "fastcomm-F9200-SR-NL": fastcomm_F9200_SR_NL,
       "fastcomm-F9200-DR-NI": fastcomm_F9200_DR_NI,
       "fastcomm-F9200-DR-NL": fastcomm_F9200_DR_NL,
       "fastcomm-F9200-SS-NI": fastcomm_F9200_SS_NI,
       "fastcomm-F9200-SS-NE": fastcomm_F9200_SS_NE,
       "fastcomm-F9200-DS-NI": fastcomm_F9200_DS_NI,
       "fastcomm-F9200-DS-NE": fastcomm_F9200_DS_NE,
       "fastcomm-F9200-SN-NI": fastcomm_F9200_SN_NI,
       "fastcomm-F9200-SN-NE": fastcomm_F9200_SN_NE,
       "fastcomm-F9200-DN-NI": fastcomm_F9200_DN_NI,
       "fastcomm-F9200-DN-NE": fastcomm_F9200_DN_NE,
       "fastcomm-F9100-SW-NI": fastcomm_F9100_SW_NI,
       "fastcomm-F9100-SW-NL": fastcomm_F9100_SW_NL,
       "fastcomm-F9100-DW-NI": fastcomm_F9100_DW_NI,
       "fastcomm-F9100-DW-NL": fastcomm_F9100_DW_NL,
       "fastcomm-F9100-SV-NI": fastcomm_F9100_SV_NI,
       "fastcomm-F9100-SV-NE": fastcomm_F9100_SV_NE,
       "fastcomm-F9100-DV-NI": fastcomm_F9100_DV_NI,
       "fastcomm-F9100-DV-NE": fastcomm_F9100_DV_NE,
       "fastcomm-F9100-SN-NW": fastcomm_F9100_SN_NW,
       "fastcomm-F9100-DN-NW": fastcomm_F9100_DN_NW,
       "fastcomm-F9200-SN-NW": fastcomm_F9200_SN_NW,
       "fastcomm-F9200-DN-NW": fastcomm_F9200_DN_NW,
       "fastcomm-F9200-TN-NI": fastcomm_F9200_TN_NI,
       "fastcomm-F9200-TN-NE": fastcomm_F9200_TN_NE,
       "fastcomm-F9200-TS-NI": fastcomm_F9200_TS_NI,
       "fastcomm-F9200-TS-NE": fastcomm_F9200_TS_NE,
       "fastcomm-F9200-TR-NI": fastcomm_F9200_TR_NI,
       "fastcomm-F9200-TR-NL": fastcomm_F9200_TR_NL,
       "fastcomm-F9200-TN-NW": fastcomm_F9200_TN_NW,
       "fastcomm-F9200-TM-NI": fastcomm_F9200_TM_NI,
       "fastcomm-F9200-TM-NL": fastcomm_F9200_TM_NL,
       "fastcomm-F9200-EN-NI": fastcomm_F9200_EN_NI,
       "fastcomm-F9200-EN-NE": fastcomm_F9200_EN_NE,
       "fastcomm-F9200-ES-NI": fastcomm_F9200_ES_NI,
       "fastcomm-F9200-ES-NE": fastcomm_F9200_ES_NE,
       "fastcomm-F9200-ER-NI": fastcomm_F9200_ER_NI,
       "fastcomm-F9200-ER-NL": fastcomm_F9200_ER_NL,
       "fastcomm-F9200-EN-NW": fastcomm_F9200_EN_NW,
       "fastcomm-F9200-EM-NI": fastcomm_F9200_EM_NI,
       "fastcomm-F9200-EM-NL": fastcomm_F9200_EM_NL,
       "fastcomm-F9200-SM-NI": fastcomm_F9200_SM_NI,
       "fastcomm-F9200-SM-NL": fastcomm_F9200_SM_NL,
       "fastcomm-F9200-DM-NI": fastcomm_F9200_DM_NI,
       "fastcomm-F9200-DM-NL": fastcomm_F9200_DM_NL,
       "fastcomm-F9900-GS": fastcomm_F9900_GS,
       "cdQuickReg": cdQuickReg,
       "fastcomm-F9500-S1": fastcomm_F9500_S1,
       "fastcomm-F9500-S3": fastcomm_F9500_S3,
       "fastcomm-F9500-S5": fastcomm_F9500_S5,
       "fastcomm-F9500-D1": fastcomm_F9500_D1,
       "fastcomm-F9500-D3": fastcomm_F9500_D3,
       "fastcomm-F9500-D5": fastcomm_F9500_D5,
       "fcFrad433Reg": fcFrad433Reg,
       "fastcomm-F9100-MO-NN": fastcomm_F9100_MO_NN,
       "fastcomm-F9100-MO-NS": fastcomm_F9100_MO_NS,
       "fastcomm-F9100-MO-NX": fastcomm_F9100_MO_NX,
       "fastcomm-F9100-TO-KN": fastcomm_F9100_TO_KN,
       "fastcomm-F9100-TO-KS": fastcomm_F9100_TO_KS,
       "fastcomm-F9100-TO-KX": fastcomm_F9100_TO_KX,
       "fastcomm-F9200-ET-HN": fastcomm_F9200_ET_HN,
       "fastcomm-F9200-ET-HS": fastcomm_F9200_ET_HS,
       "fastcomm-F9200-ET-HX": fastcomm_F9200_ET_HX,
       "fastcomm-F9200-IS-DS": fastcomm_F9200_IS_DS,
       "fastcomm-F9200-IS-DX": fastcomm_F9200_IS_DX,
       "fastcomm-F9200-ALC": fastcomm_F9200_ALC,
       "fastcomm-F9200-INET": fastcomm_F9200_INET,
       "fastcomm-SY1-DM-NI": fastcomm_SY1_DM_NI,
       "fastcomm-SY1-DN-NI": fastcomm_SY1_DN_NI,
       "fastcomm-SY1-DQ-NI": fastcomm_SY1_DQ_NI,
       "fastcomm-SY1-DV-NI": fastcomm_SY1_DV_NI,
       "fastcomm-SY1-DW-NI": fastcomm_SY1_DW_NI,
       "fastcomm-SY1-SM-NI": fastcomm_SY1_SM_NI,
       "fastcomm-SY1-SV-NI": fastcomm_SY1_SV_NI,
       "fastcomm-SY1-SW-NI": fastcomm_SY1_SW_NI,
       "fastcomm-SY2-DR-NI": fastcomm_SY2_DR_NI,
       "fastcomm-GTEDRNL": fastcomm_GTEDRNL,
       "fastcomm-NETLDR": fastcomm_NETLDR,
       "fastcomm-NNOSNMP": fastcomm_NNOSNMP,
       "fastcomm-NOPPPNA": fastcomm_NOPPPNA,
       "fastcomm-NOPPPNB": fastcomm_NOPPPNB,
       "fastcomm-NOX25NA": fastcomm_NOX25NA,
       "fastcomm-NOX25NB": fastcomm_NOX25NB,
       "fastcomm-NTNONEA": fastcomm_NTNONEA,
       "fastcomm-NTNONEB": fastcomm_NTNONEB,
       "fastcomm-PRODUCTS": fastcomm_PRODUCTS,
       "temporary": temporary}
)
