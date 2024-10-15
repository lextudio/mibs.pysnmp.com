# SNMP MIB module (ALVARION-DEVICE-WDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-DEVICE-WDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:35 2024
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "ALVARION-DEVICE-MIB",
    "coDevDisIndex")

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alvarionDeviceWdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionDeviceWdsMIBObjects_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBObjects = _AlvarionDeviceWdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1)
)
_CoDeviceWDSInfoGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSInfoGroup = _CoDeviceWDSInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 2)
)
_CoDeviceWdsInfoTable_Object = MibTable
coDeviceWdsInfoTable = _CoDeviceWdsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWdsInfoTable.setStatus("current")
_CoDeviceWdsInfoEntry_Object = MibTableRow
coDeviceWdsInfoEntry = _CoDeviceWdsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 2, 1, 1)
)
coDeviceWdsInfoEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWdsInfoEntry.setStatus("current")


class _CoDevWDSInfoMaxNumberOfGroup_Type(Unsigned32):
    """Custom type coDevWDSInfoMaxNumberOfGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoDevWDSInfoMaxNumberOfGroup_Type.__name__ = "Unsigned32"
_CoDevWDSInfoMaxNumberOfGroup_Object = MibTableColumn
coDevWDSInfoMaxNumberOfGroup = _CoDevWDSInfoMaxNumberOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 2, 1, 1, 1),
    _CoDevWDSInfoMaxNumberOfGroup_Type()
)
coDevWDSInfoMaxNumberOfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSInfoMaxNumberOfGroup.setStatus("current")
_CoDeviceWDSRadioGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSRadioGroup = _CoDeviceWDSRadioGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3)
)
_CoDeviceWDSRadioTable_Object = MibTable
coDeviceWDSRadioTable = _CoDeviceWDSRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSRadioTable.setStatus("current")
_CoDeviceWDSRadioEntry_Object = MibTableRow
coDeviceWDSRadioEntry = _CoDeviceWDSRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3, 1, 1)
)
coDeviceWDSRadioEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSRadioIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSRadioEntry.setStatus("current")


class _CoDevWDSRadioIndex_Type(Integer32):
    """Custom type coDevWDSRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSRadioIndex_Type.__name__ = "Integer32"
_CoDevWDSRadioIndex_Object = MibTableColumn
coDevWDSRadioIndex = _CoDevWDSRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3, 1, 1, 1),
    _CoDevWDSRadioIndex_Type()
)
coDevWDSRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSRadioIndex.setStatus("current")
_CoDevWDSRadioAckDistance_Type = Unsigned32
_CoDevWDSRadioAckDistance_Object = MibTableColumn
coDevWDSRadioAckDistance = _CoDevWDSRadioAckDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3, 1, 1, 2),
    _CoDevWDSRadioAckDistance_Type()
)
coDevWDSRadioAckDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSRadioAckDistance.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSRadioAckDistance.setUnits("km")


class _CoDevWDSRadioQoS_Type(Integer32):
    """Custom type coDevWDSRadioQoS based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("diffSrv", 7),
          ("disabled", 1),
          ("high", 4),
          ("ipQos", 9),
          ("low", 6),
          ("normal", 5),
          ("tos", 8),
          ("veryHigh", 3),
          ("vlan", 2))
    )


_CoDevWDSRadioQoS_Type.__name__ = "Integer32"
_CoDevWDSRadioQoS_Object = MibTableColumn
coDevWDSRadioQoS = _CoDevWDSRadioQoS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 3, 1, 1, 3),
    _CoDevWDSRadioQoS_Type()
)
coDevWDSRadioQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSRadioQoS.setStatus("current")
_CoDeviceWDSGroupGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSGroupGroup = _CoDeviceWDSGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4)
)
_CoDeviceWDSGroupTable_Object = MibTable
coDeviceWDSGroupTable = _CoDeviceWDSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSGroupTable.setStatus("current")
_CoDeviceWDSGroupEntry_Object = MibTableRow
coDeviceWDSGroupEntry = _CoDeviceWDSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1)
)
coDeviceWDSGroupEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSGroupEntry.setStatus("current")


class _CoDevWDSGroupIndex_Type(Integer32):
    """Custom type coDevWDSGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoDevWDSGroupIndex_Type.__name__ = "Integer32"
_CoDevWDSGroupIndex_Object = MibTableColumn
coDevWDSGroupIndex = _CoDevWDSGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 1),
    _CoDevWDSGroupIndex_Type()
)
coDevWDSGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSGroupIndex.setStatus("current")


class _CoDevWDSGroupName_Type(DisplayString):
    """Custom type coDevWDSGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoDevWDSGroupName_Type.__name__ = "DisplayString"
_CoDevWDSGroupName_Object = MibTableColumn
coDevWDSGroupName = _CoDevWDSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 2),
    _CoDevWDSGroupName_Type()
)
coDevWDSGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupName.setStatus("current")


class _CoDevWDSGroupState_Type(Integer32):
    """Custom type coDevWDSGroupState based on Integer32"""
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
        *(("acquisition", 3),
          ("discovery", 1),
          ("locked", 4),
          ("negotiation", 2),
          ("shutdown", 5))
    )


_CoDevWDSGroupState_Type.__name__ = "Integer32"
_CoDevWDSGroupState_Object = MibTableColumn
coDevWDSGroupState = _CoDevWDSGroupState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 3),
    _CoDevWDSGroupState_Type()
)
coDevWDSGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupState.setStatus("current")


class _CoDevWDSGroupSecurity_Type(Integer32):
    """Custom type coDevWDSGroupSecurity based on Integer32"""
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
        *(("aes", 4),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_CoDevWDSGroupSecurity_Type.__name__ = "Integer32"
_CoDevWDSGroupSecurity_Object = MibTableColumn
coDevWDSGroupSecurity = _CoDevWDSGroupSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 4),
    _CoDevWDSGroupSecurity_Type()
)
coDevWDSGroupSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupSecurity.setStatus("current")


class _CoDevWDSGroupDynamicMode_Type(Integer32):
    """Custom type coDevWDSGroupDynamicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternateMaster", 3),
          ("master", 1),
          ("slave", 2))
    )


_CoDevWDSGroupDynamicMode_Type.__name__ = "Integer32"
_CoDevWDSGroupDynamicMode_Object = MibTableColumn
coDevWDSGroupDynamicMode = _CoDevWDSGroupDynamicMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 5),
    _CoDevWDSGroupDynamicMode_Type()
)
coDevWDSGroupDynamicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupDynamicMode.setStatus("current")
_CoDevWDSGroupDynamicGroupId_Type = Unsigned32
_CoDevWDSGroupDynamicGroupId_Object = MibTableColumn
coDevWDSGroupDynamicGroupId = _CoDevWDSGroupDynamicGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 4, 1, 1, 6),
    _CoDevWDSGroupDynamicGroupId_Type()
)
coDevWDSGroupDynamicGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupDynamicGroupId.setStatus("current")
_CoDeviceWDSLinkGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSLinkGroup = _CoDeviceWDSLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5)
)
_CoDeviceWDSLinkStatusTable_Object = MibTable
coDeviceWDSLinkStatusTable = _CoDeviceWDSLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatusTable.setStatus("current")
_CoDeviceWDSLinkStatusEntry_Object = MibTableRow
coDeviceWDSLinkStatusEntry = _CoDeviceWDSLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1)
)
coDeviceWDSLinkStatusEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatusEntry.setStatus("current")


class _CoDevWDSLinkStaIndex_Type(Integer32):
    """Custom type coDevWDSLinkStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_CoDevWDSLinkStaIndex_Type.__name__ = "Integer32"
_CoDevWDSLinkStaIndex_Object = MibTableColumn
coDevWDSLinkStaIndex = _CoDevWDSLinkStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 1),
    _CoDevWDSLinkStaIndex_Type()
)
coDevWDSLinkStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIndex.setStatus("current")


class _CoDevWDSLinkStaState_Type(Integer32):
    """Custom type coDevWDSLinkStaState based on Integer32"""
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
        *(("acquiring", 2),
          ("active", 4),
          ("down", 1),
          ("inactive", 3))
    )


_CoDevWDSLinkStaState_Type.__name__ = "Integer32"
_CoDevWDSLinkStaState_Object = MibTableColumn
coDevWDSLinkStaState = _CoDevWDSLinkStaState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 2),
    _CoDevWDSLinkStaState_Type()
)
coDevWDSLinkStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaState.setStatus("current")


class _CoDevWDSLinkStaRadio_Type(Integer32):
    """Custom type coDevWDSLinkStaRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSLinkStaRadio_Type.__name__ = "Integer32"
_CoDevWDSLinkStaRadio_Object = MibTableColumn
coDevWDSLinkStaRadio = _CoDevWDSLinkStaRadio_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 3),
    _CoDevWDSLinkStaRadio_Type()
)
coDevWDSLinkStaRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRadio.setStatus("current")
_CoDevWDSLinkStaPeerMacAddress_Type = MacAddress
_CoDevWDSLinkStaPeerMacAddress_Object = MibTableColumn
coDevWDSLinkStaPeerMacAddress = _CoDevWDSLinkStaPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 4),
    _CoDevWDSLinkStaPeerMacAddress_Type()
)
coDevWDSLinkStaPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaPeerMacAddress.setStatus("current")
_CoDevWDSLinkStaMaster_Type = TruthValue
_CoDevWDSLinkStaMaster_Object = MibTableColumn
coDevWDSLinkStaMaster = _CoDevWDSLinkStaMaster_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 5),
    _CoDevWDSLinkStaMaster_Type()
)
coDevWDSLinkStaMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaMaster.setStatus("current")
_CoDevWDSLinkStaAuthorized_Type = TruthValue
_CoDevWDSLinkStaAuthorized_Object = MibTableColumn
coDevWDSLinkStaAuthorized = _CoDevWDSLinkStaAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 6),
    _CoDevWDSLinkStaAuthorized_Type()
)
coDevWDSLinkStaAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaAuthorized.setStatus("current")


class _CoDevWDSLinkStaEncryption_Type(Integer32):
    """Custom type coDevWDSLinkStaEncryption based on Integer32"""
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
        *(("aes", 4),
          ("none", 1),
          ("tkip", 3),
          ("wep", 2))
    )


_CoDevWDSLinkStaEncryption_Type.__name__ = "Integer32"
_CoDevWDSLinkStaEncryption_Object = MibTableColumn
coDevWDSLinkStaEncryption = _CoDevWDSLinkStaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 7),
    _CoDevWDSLinkStaEncryption_Type()
)
coDevWDSLinkStaEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaEncryption.setStatus("current")
_CoDevWDSLinkStaIdleTime_Type = Unsigned32
_CoDevWDSLinkStaIdleTime_Object = MibTableColumn
coDevWDSLinkStaIdleTime = _CoDevWDSLinkStaIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 8),
    _CoDevWDSLinkStaIdleTime_Type()
)
coDevWDSLinkStaIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIdleTime.setUnits("seconds")


class _CoDevWDSLinkStaSNR_Type(Integer32):
    """Custom type coDevWDSLinkStaSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWDSLinkStaSNR_Type.__name__ = "Integer32"
_CoDevWDSLinkStaSNR_Object = MibTableColumn
coDevWDSLinkStaSNR = _CoDevWDSLinkStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 9),
    _CoDevWDSLinkStaSNR_Type()
)
coDevWDSLinkStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSNR.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSNR.setUnits("dBm")
_CoDevWDSLinkStaTxRate_Type = Unsigned32
_CoDevWDSLinkStaTxRate_Object = MibTableColumn
coDevWDSLinkStaTxRate = _CoDevWDSLinkStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 10),
    _CoDevWDSLinkStaTxRate_Type()
)
coDevWDSLinkStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaTxRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaTxRate.setUnits("500Kb/s")
_CoDevWDSLinkStaRxRate_Type = Unsigned32
_CoDevWDSLinkStaRxRate_Object = MibTableColumn
coDevWDSLinkStaRxRate = _CoDevWDSLinkStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 11),
    _CoDevWDSLinkStaRxRate_Type()
)
coDevWDSLinkStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRxRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRxRate.setUnits("500Kb/s")


class _CoDevWDSLinkStaIfIndex_Type(Integer32):
    """Custom type coDevWDSLinkStaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWDSLinkStaIfIndex_Type.__name__ = "Integer32"
_CoDevWDSLinkStaIfIndex_Object = MibTableColumn
coDevWDSLinkStaIfIndex = _CoDevWDSLinkStaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 1, 1, 12),
    _CoDevWDSLinkStaIfIndex_Type()
)
coDevWDSLinkStaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIfIndex.setStatus("current")
_CoDeviceWDSLinkStatsRatesTable_Object = MibTable
coDeviceWDSLinkStatsRatesTable = _CoDeviceWDSLinkStatsRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsRatesTable.setStatus("current")
_CoDeviceWDSLinkStatsRatesEntry_Object = MibTableRow
coDeviceWDSLinkStatsRatesEntry = _CoDeviceWDSLinkStatsRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsRatesEntry.setStatus("current")
_CoDevWDSLinkStsPktsTxRate1_Type = Counter32
_CoDevWDSLinkStsPktsTxRate1_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate1 = _CoDevWDSLinkStsPktsTxRate1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 1),
    _CoDevWDSLinkStsPktsTxRate1_Type()
)
coDevWDSLinkStsPktsTxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate1.setStatus("current")
_CoDevWDSLinkStsPktsTxRate2_Type = Counter32
_CoDevWDSLinkStsPktsTxRate2_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate2 = _CoDevWDSLinkStsPktsTxRate2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 2),
    _CoDevWDSLinkStsPktsTxRate2_Type()
)
coDevWDSLinkStsPktsTxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate2.setStatus("current")
_CoDevWDSLinkStsPktsTxRate5dot5_Type = Counter32
_CoDevWDSLinkStsPktsTxRate5dot5_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate5dot5 = _CoDevWDSLinkStsPktsTxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 3),
    _CoDevWDSLinkStsPktsTxRate5dot5_Type()
)
coDevWDSLinkStsPktsTxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate5dot5.setStatus("current")
_CoDevWDSLinkStsPktsTxRate11_Type = Counter32
_CoDevWDSLinkStsPktsTxRate11_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate11 = _CoDevWDSLinkStsPktsTxRate11_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 4),
    _CoDevWDSLinkStsPktsTxRate11_Type()
)
coDevWDSLinkStsPktsTxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate11.setStatus("current")
_CoDevWDSLinkStsPktsTxRate6_Type = Counter32
_CoDevWDSLinkStsPktsTxRate6_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate6 = _CoDevWDSLinkStsPktsTxRate6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 5),
    _CoDevWDSLinkStsPktsTxRate6_Type()
)
coDevWDSLinkStsPktsTxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate6.setStatus("current")
_CoDevWDSLinkStsPktsTxRate9_Type = Counter32
_CoDevWDSLinkStsPktsTxRate9_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate9 = _CoDevWDSLinkStsPktsTxRate9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 6),
    _CoDevWDSLinkStsPktsTxRate9_Type()
)
coDevWDSLinkStsPktsTxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate9.setStatus("current")
_CoDevWDSLinkStsPktsTxRate12_Type = Counter32
_CoDevWDSLinkStsPktsTxRate12_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate12 = _CoDevWDSLinkStsPktsTxRate12_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 7),
    _CoDevWDSLinkStsPktsTxRate12_Type()
)
coDevWDSLinkStsPktsTxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate12.setStatus("current")
_CoDevWDSLinkStsPktsTxRate18_Type = Counter32
_CoDevWDSLinkStsPktsTxRate18_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate18 = _CoDevWDSLinkStsPktsTxRate18_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 8),
    _CoDevWDSLinkStsPktsTxRate18_Type()
)
coDevWDSLinkStsPktsTxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate18.setStatus("current")
_CoDevWDSLinkStsPktsTxRate24_Type = Counter32
_CoDevWDSLinkStsPktsTxRate24_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate24 = _CoDevWDSLinkStsPktsTxRate24_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 9),
    _CoDevWDSLinkStsPktsTxRate24_Type()
)
coDevWDSLinkStsPktsTxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate24.setStatus("current")
_CoDevWDSLinkStsPktsTxRate36_Type = Counter32
_CoDevWDSLinkStsPktsTxRate36_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate36 = _CoDevWDSLinkStsPktsTxRate36_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 10),
    _CoDevWDSLinkStsPktsTxRate36_Type()
)
coDevWDSLinkStsPktsTxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate36.setStatus("current")
_CoDevWDSLinkStsPktsTxRate48_Type = Counter32
_CoDevWDSLinkStsPktsTxRate48_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate48 = _CoDevWDSLinkStsPktsTxRate48_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 11),
    _CoDevWDSLinkStsPktsTxRate48_Type()
)
coDevWDSLinkStsPktsTxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate48.setStatus("current")
_CoDevWDSLinkStsPktsTxRate54_Type = Counter32
_CoDevWDSLinkStsPktsTxRate54_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate54 = _CoDevWDSLinkStsPktsTxRate54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 12),
    _CoDevWDSLinkStsPktsTxRate54_Type()
)
coDevWDSLinkStsPktsTxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate54.setStatus("current")
_CoDevWDSLinkStsPktsRxRate1_Type = Counter32
_CoDevWDSLinkStsPktsRxRate1_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate1 = _CoDevWDSLinkStsPktsRxRate1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 13),
    _CoDevWDSLinkStsPktsRxRate1_Type()
)
coDevWDSLinkStsPktsRxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate1.setStatus("current")
_CoDevWDSLinkStsPktsRxRate2_Type = Counter32
_CoDevWDSLinkStsPktsRxRate2_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate2 = _CoDevWDSLinkStsPktsRxRate2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 14),
    _CoDevWDSLinkStsPktsRxRate2_Type()
)
coDevWDSLinkStsPktsRxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate2.setStatus("current")
_CoDevWDSLinkStsPktsRxRate5dot5_Type = Counter32
_CoDevWDSLinkStsPktsRxRate5dot5_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate5dot5 = _CoDevWDSLinkStsPktsRxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 15),
    _CoDevWDSLinkStsPktsRxRate5dot5_Type()
)
coDevWDSLinkStsPktsRxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate5dot5.setStatus("current")
_CoDevWDSLinkStsPktsRxRate11_Type = Counter32
_CoDevWDSLinkStsPktsRxRate11_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate11 = _CoDevWDSLinkStsPktsRxRate11_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 16),
    _CoDevWDSLinkStsPktsRxRate11_Type()
)
coDevWDSLinkStsPktsRxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate11.setStatus("current")
_CoDevWDSLinkStsPktsRxRate6_Type = Counter32
_CoDevWDSLinkStsPktsRxRate6_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate6 = _CoDevWDSLinkStsPktsRxRate6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 17),
    _CoDevWDSLinkStsPktsRxRate6_Type()
)
coDevWDSLinkStsPktsRxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate6.setStatus("current")
_CoDevWDSLinkStsPktsRxRate9_Type = Counter32
_CoDevWDSLinkStsPktsRxRate9_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate9 = _CoDevWDSLinkStsPktsRxRate9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 18),
    _CoDevWDSLinkStsPktsRxRate9_Type()
)
coDevWDSLinkStsPktsRxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate9.setStatus("current")
_CoDevWDSLinkStsPktsRxRate12_Type = Counter32
_CoDevWDSLinkStsPktsRxRate12_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate12 = _CoDevWDSLinkStsPktsRxRate12_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 19),
    _CoDevWDSLinkStsPktsRxRate12_Type()
)
coDevWDSLinkStsPktsRxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate12.setStatus("current")
_CoDevWDSLinkStsPktsRxRate18_Type = Counter32
_CoDevWDSLinkStsPktsRxRate18_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate18 = _CoDevWDSLinkStsPktsRxRate18_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 20),
    _CoDevWDSLinkStsPktsRxRate18_Type()
)
coDevWDSLinkStsPktsRxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate18.setStatus("current")
_CoDevWDSLinkStsPktsRxRate24_Type = Counter32
_CoDevWDSLinkStsPktsRxRate24_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate24 = _CoDevWDSLinkStsPktsRxRate24_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 21),
    _CoDevWDSLinkStsPktsRxRate24_Type()
)
coDevWDSLinkStsPktsRxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate24.setStatus("current")
_CoDevWDSLinkStsPktsRxRate36_Type = Counter32
_CoDevWDSLinkStsPktsRxRate36_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate36 = _CoDevWDSLinkStsPktsRxRate36_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 22),
    _CoDevWDSLinkStsPktsRxRate36_Type()
)
coDevWDSLinkStsPktsRxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate36.setStatus("current")
_CoDevWDSLinkStsPktsRxRate48_Type = Counter32
_CoDevWDSLinkStsPktsRxRate48_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate48 = _CoDevWDSLinkStsPktsRxRate48_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 23),
    _CoDevWDSLinkStsPktsRxRate48_Type()
)
coDevWDSLinkStsPktsRxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate48.setStatus("current")
_CoDevWDSLinkStsPktsRxRate54_Type = Counter32
_CoDevWDSLinkStsPktsRxRate54_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate54 = _CoDevWDSLinkStsPktsRxRate54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 5, 2, 1, 24),
    _CoDevWDSLinkStsPktsRxRate54_Type()
)
coDevWDSLinkStsPktsRxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate54.setStatus("current")
_CoDeviceWDSNetworkScanGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSNetworkScanGroup = _CoDeviceWDSNetworkScanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6)
)
_CoDeviceWDSNetworkScanTable_Object = MibTable
coDeviceWDSNetworkScanTable = _CoDeviceWDSNetworkScanTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSNetworkScanTable.setStatus("current")
_CoDeviceWDSNetworkScanEntry_Object = MibTableRow
coDeviceWDSNetworkScanEntry = _CoDeviceWDSNetworkScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1)
)
coDeviceWDSNetworkScanEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSScanRadioIndex"),
    (0, "ALVARION-DEVICE-WDS-MIB", "coDevWDSScanPeerIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSNetworkScanEntry.setStatus("current")


class _CoDevWDSScanRadioIndex_Type(Integer32):
    """Custom type coDevWDSScanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSScanRadioIndex_Type.__name__ = "Integer32"
_CoDevWDSScanRadioIndex_Object = MibTableColumn
coDevWDSScanRadioIndex = _CoDevWDSScanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 1),
    _CoDevWDSScanRadioIndex_Type()
)
coDevWDSScanRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSScanRadioIndex.setStatus("current")


class _CoDevWDSScanPeerIndex_Type(Integer32):
    """Custom type coDevWDSScanPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CoDevWDSScanPeerIndex_Type.__name__ = "Integer32"
_CoDevWDSScanPeerIndex_Object = MibTableColumn
coDevWDSScanPeerIndex = _CoDevWDSScanPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 2),
    _CoDevWDSScanPeerIndex_Type()
)
coDevWDSScanPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSScanPeerIndex.setStatus("current")
_CoDevWDSScanGroupId_Type = Unsigned32
_CoDevWDSScanGroupId_Object = MibTableColumn
coDevWDSScanGroupId = _CoDevWDSScanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 3),
    _CoDevWDSScanGroupId_Type()
)
coDevWDSScanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanGroupId.setStatus("current")
_CoDevWDSScanPeerMacAddress_Type = MacAddress
_CoDevWDSScanPeerMacAddress_Object = MibTableColumn
coDevWDSScanPeerMacAddress = _CoDevWDSScanPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 4),
    _CoDevWDSScanPeerMacAddress_Type()
)
coDevWDSScanPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanPeerMacAddress.setStatus("current")


class _CoDevWDSScanChannel_Type(Unsigned32):
    """Custom type coDevWDSScanChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_CoDevWDSScanChannel_Type.__name__ = "Unsigned32"
_CoDevWDSScanChannel_Object = MibTableColumn
coDevWDSScanChannel = _CoDevWDSScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 5),
    _CoDevWDSScanChannel_Type()
)
coDevWDSScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanChannel.setStatus("current")


class _CoDevWDSScanSNR_Type(Integer32):
    """Custom type coDevWDSScanSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWDSScanSNR_Type.__name__ = "Integer32"
_CoDevWDSScanSNR_Object = MibTableColumn
coDevWDSScanSNR = _CoDevWDSScanSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 6),
    _CoDevWDSScanSNR_Type()
)
coDevWDSScanSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanSNR.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSScanSNR.setUnits("dBm")


class _CoDevWDSScanMode_Type(Integer32):
    """Custom type coDevWDSScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternateMaster", 3),
          ("master", 1),
          ("slave", 2))
    )


_CoDevWDSScanMode_Type.__name__ = "Integer32"
_CoDevWDSScanMode_Object = MibTableColumn
coDevWDSScanMode = _CoDevWDSScanMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 7),
    _CoDevWDSScanMode_Type()
)
coDevWDSScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanMode.setStatus("current")
_CoDevWDSScanAvailable_Type = TruthValue
_CoDevWDSScanAvailable_Object = MibTableColumn
coDevWDSScanAvailable = _CoDevWDSScanAvailable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 1, 6, 1, 1, 8),
    _CoDevWDSScanAvailable_Type()
)
coDevWDSScanAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanAvailable.setStatus("current")
_AlvarionDeviceWdsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBNotificationPrefix = _AlvarionDeviceWdsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 2)
)
_AlvarionDeviceWdsMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBNotifications = _AlvarionDeviceWdsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 2, 0)
)
_AlvarionDeviceWdsMIBConformance_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBConformance = _AlvarionDeviceWdsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3)
)
_AlvarionDeviceWdsMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBCompliances = _AlvarionDeviceWdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 1)
)
_AlvarionDeviceWdsMIBGroups_ObjectIdentity = ObjectIdentity
alvarionDeviceWdsMIBGroups = _AlvarionDeviceWdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2)
)
coDeviceWDSLinkStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-WDS-MIB",
     "coDeviceWDSLinkStatsRatesEntry")
)
coDeviceWDSLinkStatsRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())

# Managed Objects groups

alvarionDeviceWdsInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2, 1)
)
alvarionDeviceWdsInfoMIBGroup.setObjects(
    ("ALVARION-DEVICE-WDS-MIB", "coDevWDSInfoMaxNumberOfGroup")
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsInfoMIBGroup.setStatus("current")

alvarionDeviceWdsRadioMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2, 2)
)
alvarionDeviceWdsRadioMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WDS-MIB", "coDevWDSRadioAckDistance"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSRadioQoS"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsRadioMIBGroup.setStatus("current")

alvarionDeviceWdsGroupMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2, 3)
)
alvarionDeviceWdsGroupMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupName"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupState"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupSecurity"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupDynamicMode"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSGroupDynamicGroupId"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsGroupMIBGroup.setStatus("current")

alvarionDeviceWdsLinkMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2, 4)
)
alvarionDeviceWdsLinkMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaState"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaRadio"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaPeerMacAddress"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaMaster"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaAuthorized"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaEncryption"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaIdleTime"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaSNR"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaTxRate"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaRxRate"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStaIfIndex"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate1"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate2"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate5dot5"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate11"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate6"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate9"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate12"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate18"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate24"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate36"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate48"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate54"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate1"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate2"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate5dot5"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate11"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate6"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate9"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate12"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate18"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate24"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate36"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate48"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate54"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsLinkMIBGroup.setStatus("current")

alvarionDeviceWdsNetworkScanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 2, 5)
)
alvarionDeviceWdsNetworkScanMIBGroup.setObjects(
      *(("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanGroupId"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanPeerMacAddress"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanChannel"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanSNR"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanMode"),
        ("ALVARION-DEVICE-WDS-MIB", "coDevWDSScanAvailable"))
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsNetworkScanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionDeviceWdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 34, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionDeviceWdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-DEVICE-WDS-MIB",
    **{"alvarionDeviceWdsMIB": alvarionDeviceWdsMIB,
       "alvarionDeviceWdsMIBObjects": alvarionDeviceWdsMIBObjects,
       "coDeviceWDSInfoGroup": coDeviceWDSInfoGroup,
       "coDeviceWdsInfoTable": coDeviceWdsInfoTable,
       "coDeviceWdsInfoEntry": coDeviceWdsInfoEntry,
       "coDevWDSInfoMaxNumberOfGroup": coDevWDSInfoMaxNumberOfGroup,
       "coDeviceWDSRadioGroup": coDeviceWDSRadioGroup,
       "coDeviceWDSRadioTable": coDeviceWDSRadioTable,
       "coDeviceWDSRadioEntry": coDeviceWDSRadioEntry,
       "coDevWDSRadioIndex": coDevWDSRadioIndex,
       "coDevWDSRadioAckDistance": coDevWDSRadioAckDistance,
       "coDevWDSRadioQoS": coDevWDSRadioQoS,
       "coDeviceWDSGroupGroup": coDeviceWDSGroupGroup,
       "coDeviceWDSGroupTable": coDeviceWDSGroupTable,
       "coDeviceWDSGroupEntry": coDeviceWDSGroupEntry,
       "coDevWDSGroupIndex": coDevWDSGroupIndex,
       "coDevWDSGroupName": coDevWDSGroupName,
       "coDevWDSGroupState": coDevWDSGroupState,
       "coDevWDSGroupSecurity": coDevWDSGroupSecurity,
       "coDevWDSGroupDynamicMode": coDevWDSGroupDynamicMode,
       "coDevWDSGroupDynamicGroupId": coDevWDSGroupDynamicGroupId,
       "coDeviceWDSLinkGroup": coDeviceWDSLinkGroup,
       "coDeviceWDSLinkStatusTable": coDeviceWDSLinkStatusTable,
       "coDeviceWDSLinkStatusEntry": coDeviceWDSLinkStatusEntry,
       "coDevWDSLinkStaIndex": coDevWDSLinkStaIndex,
       "coDevWDSLinkStaState": coDevWDSLinkStaState,
       "coDevWDSLinkStaRadio": coDevWDSLinkStaRadio,
       "coDevWDSLinkStaPeerMacAddress": coDevWDSLinkStaPeerMacAddress,
       "coDevWDSLinkStaMaster": coDevWDSLinkStaMaster,
       "coDevWDSLinkStaAuthorized": coDevWDSLinkStaAuthorized,
       "coDevWDSLinkStaEncryption": coDevWDSLinkStaEncryption,
       "coDevWDSLinkStaIdleTime": coDevWDSLinkStaIdleTime,
       "coDevWDSLinkStaSNR": coDevWDSLinkStaSNR,
       "coDevWDSLinkStaTxRate": coDevWDSLinkStaTxRate,
       "coDevWDSLinkStaRxRate": coDevWDSLinkStaRxRate,
       "coDevWDSLinkStaIfIndex": coDevWDSLinkStaIfIndex,
       "coDeviceWDSLinkStatsRatesTable": coDeviceWDSLinkStatsRatesTable,
       "coDeviceWDSLinkStatsRatesEntry": coDeviceWDSLinkStatsRatesEntry,
       "coDevWDSLinkStsPktsTxRate1": coDevWDSLinkStsPktsTxRate1,
       "coDevWDSLinkStsPktsTxRate2": coDevWDSLinkStsPktsTxRate2,
       "coDevWDSLinkStsPktsTxRate5dot5": coDevWDSLinkStsPktsTxRate5dot5,
       "coDevWDSLinkStsPktsTxRate11": coDevWDSLinkStsPktsTxRate11,
       "coDevWDSLinkStsPktsTxRate6": coDevWDSLinkStsPktsTxRate6,
       "coDevWDSLinkStsPktsTxRate9": coDevWDSLinkStsPktsTxRate9,
       "coDevWDSLinkStsPktsTxRate12": coDevWDSLinkStsPktsTxRate12,
       "coDevWDSLinkStsPktsTxRate18": coDevWDSLinkStsPktsTxRate18,
       "coDevWDSLinkStsPktsTxRate24": coDevWDSLinkStsPktsTxRate24,
       "coDevWDSLinkStsPktsTxRate36": coDevWDSLinkStsPktsTxRate36,
       "coDevWDSLinkStsPktsTxRate48": coDevWDSLinkStsPktsTxRate48,
       "coDevWDSLinkStsPktsTxRate54": coDevWDSLinkStsPktsTxRate54,
       "coDevWDSLinkStsPktsRxRate1": coDevWDSLinkStsPktsRxRate1,
       "coDevWDSLinkStsPktsRxRate2": coDevWDSLinkStsPktsRxRate2,
       "coDevWDSLinkStsPktsRxRate5dot5": coDevWDSLinkStsPktsRxRate5dot5,
       "coDevWDSLinkStsPktsRxRate11": coDevWDSLinkStsPktsRxRate11,
       "coDevWDSLinkStsPktsRxRate6": coDevWDSLinkStsPktsRxRate6,
       "coDevWDSLinkStsPktsRxRate9": coDevWDSLinkStsPktsRxRate9,
       "coDevWDSLinkStsPktsRxRate12": coDevWDSLinkStsPktsRxRate12,
       "coDevWDSLinkStsPktsRxRate18": coDevWDSLinkStsPktsRxRate18,
       "coDevWDSLinkStsPktsRxRate24": coDevWDSLinkStsPktsRxRate24,
       "coDevWDSLinkStsPktsRxRate36": coDevWDSLinkStsPktsRxRate36,
       "coDevWDSLinkStsPktsRxRate48": coDevWDSLinkStsPktsRxRate48,
       "coDevWDSLinkStsPktsRxRate54": coDevWDSLinkStsPktsRxRate54,
       "coDeviceWDSNetworkScanGroup": coDeviceWDSNetworkScanGroup,
       "coDeviceWDSNetworkScanTable": coDeviceWDSNetworkScanTable,
       "coDeviceWDSNetworkScanEntry": coDeviceWDSNetworkScanEntry,
       "coDevWDSScanRadioIndex": coDevWDSScanRadioIndex,
       "coDevWDSScanPeerIndex": coDevWDSScanPeerIndex,
       "coDevWDSScanGroupId": coDevWDSScanGroupId,
       "coDevWDSScanPeerMacAddress": coDevWDSScanPeerMacAddress,
       "coDevWDSScanChannel": coDevWDSScanChannel,
       "coDevWDSScanSNR": coDevWDSScanSNR,
       "coDevWDSScanMode": coDevWDSScanMode,
       "coDevWDSScanAvailable": coDevWDSScanAvailable,
       "alvarionDeviceWdsMIBNotificationPrefix": alvarionDeviceWdsMIBNotificationPrefix,
       "alvarionDeviceWdsMIBNotifications": alvarionDeviceWdsMIBNotifications,
       "alvarionDeviceWdsMIBConformance": alvarionDeviceWdsMIBConformance,
       "alvarionDeviceWdsMIBCompliances": alvarionDeviceWdsMIBCompliances,
       "alvarionDeviceWdsMIBCompliance": alvarionDeviceWdsMIBCompliance,
       "alvarionDeviceWdsMIBGroups": alvarionDeviceWdsMIBGroups,
       "alvarionDeviceWdsInfoMIBGroup": alvarionDeviceWdsInfoMIBGroup,
       "alvarionDeviceWdsRadioMIBGroup": alvarionDeviceWdsRadioMIBGroup,
       "alvarionDeviceWdsGroupMIBGroup": alvarionDeviceWdsGroupMIBGroup,
       "alvarionDeviceWdsLinkMIBGroup": alvarionDeviceWdsLinkMIBGroup,
       "alvarionDeviceWdsNetworkScanMIBGroup": alvarionDeviceWdsNetworkScanMIBGroup}
)
