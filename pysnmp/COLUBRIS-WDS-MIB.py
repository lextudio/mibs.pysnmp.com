# SNMP MIB module (COLUBRIS-WDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-WDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:31 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisWdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisWdsMIBObjects_ObjectIdentity = ObjectIdentity
colubrisWdsMIBObjects = _ColubrisWdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1)
)
_CoWDSInfoGroup_ObjectIdentity = ObjectIdentity
coWDSInfoGroup = _CoWDSInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1)
)


class _CoWDSNumberOfGroup_Type(Unsigned32):
    """Custom type coWDSNumberOfGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoWDSNumberOfGroup_Type.__name__ = "Unsigned32"
_CoWDSNumberOfGroup_Object = MibScalar
coWDSNumberOfGroup = _CoWDSNumberOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1, 1),
    _CoWDSNumberOfGroup_Type()
)
coWDSNumberOfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSNumberOfGroup.setStatus("current")
_CoWDSDynamicModeImplemented_Type = TruthValue
_CoWDSDynamicModeImplemented_Object = MibScalar
coWDSDynamicModeImplemented = _CoWDSDynamicModeImplemented_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1, 2),
    _CoWDSDynamicModeImplemented_Type()
)
coWDSDynamicModeImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSDynamicModeImplemented.setStatus("current")
_CoWDSRadioGroup_ObjectIdentity = ObjectIdentity
coWDSRadioGroup = _CoWDSRadioGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2)
)
_CoWDSRadioTable_Object = MibTable
coWDSRadioTable = _CoWDSRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coWDSRadioTable.setStatus("current")
_CoWDSRadioEntry_Object = MibTableRow
coWDSRadioEntry = _CoWDSRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1)
)
coWDSRadioEntry.setIndexNames(
    (0, "COLUBRIS-WDS-MIB", "coWDSRadioIndex"),
)
if mibBuilder.loadTexts:
    coWDSRadioEntry.setStatus("current")


class _CoWDSRadioIndex_Type(Integer32):
    """Custom type coWDSRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoWDSRadioIndex_Type.__name__ = "Integer32"
_CoWDSRadioIndex_Object = MibTableColumn
coWDSRadioIndex = _CoWDSRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 1),
    _CoWDSRadioIndex_Type()
)
coWDSRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coWDSRadioIndex.setStatus("current")
_CoWDSRadioAckDistance_Type = Unsigned32
_CoWDSRadioAckDistance_Object = MibTableColumn
coWDSRadioAckDistance = _CoWDSRadioAckDistance_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 2),
    _CoWDSRadioAckDistance_Type()
)
coWDSRadioAckDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSRadioAckDistance.setStatus("current")
if mibBuilder.loadTexts:
    coWDSRadioAckDistance.setUnits("km")


class _CoWDSRadioQoS_Type(Integer32):
    """Custom type coWDSRadioQoS based on Integer32"""
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


_CoWDSRadioQoS_Type.__name__ = "Integer32"
_CoWDSRadioQoS_Object = MibTableColumn
coWDSRadioQoS = _CoWDSRadioQoS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 3),
    _CoWDSRadioQoS_Type()
)
coWDSRadioQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSRadioQoS.setStatus("current")
_CoWDSGroupGroup_ObjectIdentity = ObjectIdentity
coWDSGroupGroup = _CoWDSGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3)
)
_CoWDSGroupTable_Object = MibTable
coWDSGroupTable = _CoWDSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coWDSGroupTable.setStatus("current")
_CoWDSGroupEntry_Object = MibTableRow
coWDSGroupEntry = _CoWDSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1)
)
coWDSGroupEntry.setIndexNames(
    (0, "COLUBRIS-WDS-MIB", "coWDSGroupIndex"),
)
if mibBuilder.loadTexts:
    coWDSGroupEntry.setStatus("current")


class _CoWDSGroupIndex_Type(Integer32):
    """Custom type coWDSGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoWDSGroupIndex_Type.__name__ = "Integer32"
_CoWDSGroupIndex_Object = MibTableColumn
coWDSGroupIndex = _CoWDSGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 1),
    _CoWDSGroupIndex_Type()
)
coWDSGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coWDSGroupIndex.setStatus("current")


class _CoWDSGroupName_Type(DisplayString):
    """Custom type coWDSGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoWDSGroupName_Type.__name__ = "DisplayString"
_CoWDSGroupName_Object = MibTableColumn
coWDSGroupName = _CoWDSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 2),
    _CoWDSGroupName_Type()
)
coWDSGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupName.setStatus("current")


class _CoWDSGroupState_Type(Integer32):
    """Custom type coWDSGroupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CoWDSGroupState_Type.__name__ = "Integer32"
_CoWDSGroupState_Object = MibTableColumn
coWDSGroupState = _CoWDSGroupState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 3),
    _CoWDSGroupState_Type()
)
coWDSGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupState.setStatus("current")


class _CoWDSGroupSecurity_Type(Integer32):
    """Custom type coWDSGroupSecurity based on Integer32"""
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


_CoWDSGroupSecurity_Type.__name__ = "Integer32"
_CoWDSGroupSecurity_Object = MibTableColumn
coWDSGroupSecurity = _CoWDSGroupSecurity_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 4),
    _CoWDSGroupSecurity_Type()
)
coWDSGroupSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupSecurity.setStatus("current")


class _CoWDSGroupAddressing_Type(Integer32):
    """Custom type coWDSGroupAddressing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CoWDSGroupAddressing_Type.__name__ = "Integer32"
_CoWDSGroupAddressing_Object = MibTableColumn
coWDSGroupAddressing = _CoWDSGroupAddressing_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 5),
    _CoWDSGroupAddressing_Type()
)
coWDSGroupAddressing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupAddressing.setStatus("current")
_CoWDSGroupStaticMacAddress_Type = MacAddress
_CoWDSGroupStaticMacAddress_Object = MibTableColumn
coWDSGroupStaticMacAddress = _CoWDSGroupStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 6),
    _CoWDSGroupStaticMacAddress_Type()
)
coWDSGroupStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupStaticMacAddress.setStatus("current")


class _CoWDSGroupDynamicMode_Type(Integer32):
    """Custom type coWDSGroupDynamicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alternateMaster", 3),
          ("master", 1),
          ("none", 0),
          ("slave", 2))
    )


_CoWDSGroupDynamicMode_Type.__name__ = "Integer32"
_CoWDSGroupDynamicMode_Object = MibTableColumn
coWDSGroupDynamicMode = _CoWDSGroupDynamicMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 7),
    _CoWDSGroupDynamicMode_Type()
)
coWDSGroupDynamicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupDynamicMode.setStatus("current")
_CoWDSGroupDynamicGroupId_Type = Unsigned32
_CoWDSGroupDynamicGroupId_Object = MibTableColumn
coWDSGroupDynamicGroupId = _CoWDSGroupDynamicGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 8),
    _CoWDSGroupDynamicGroupId_Type()
)
coWDSGroupDynamicGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSGroupDynamicGroupId.setStatus("current")
_CoWDSLinkGroup_ObjectIdentity = ObjectIdentity
coWDSLinkGroup = _CoWDSLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4)
)
_CoWDSLinkTable_Object = MibTable
coWDSLinkTable = _CoWDSLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coWDSLinkTable.setStatus("current")
_CoWDSLinkEntry_Object = MibTableRow
coWDSLinkEntry = _CoWDSLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1)
)
coWDSLinkEntry.setIndexNames(
    (0, "COLUBRIS-WDS-MIB", "coWDSGroupIndex"),
    (0, "COLUBRIS-WDS-MIB", "coWDSLinkIndex"),
)
if mibBuilder.loadTexts:
    coWDSLinkEntry.setStatus("current")


class _CoWDSLinkIndex_Type(Integer32):
    """Custom type coWDSLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_CoWDSLinkIndex_Type.__name__ = "Integer32"
_CoWDSLinkIndex_Object = MibTableColumn
coWDSLinkIndex = _CoWDSLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 1),
    _CoWDSLinkIndex_Type()
)
coWDSLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coWDSLinkIndex.setStatus("current")


class _CoWDSLinkState_Type(Integer32):
    """Custom type coWDSLinkState based on Integer32"""
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


_CoWDSLinkState_Type.__name__ = "Integer32"
_CoWDSLinkState_Object = MibTableColumn
coWDSLinkState = _CoWDSLinkState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 2),
    _CoWDSLinkState_Type()
)
coWDSLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkState.setStatus("current")


class _CoWDSLinkRadio_Type(Integer32):
    """Custom type coWDSLinkRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoWDSLinkRadio_Type.__name__ = "Integer32"
_CoWDSLinkRadio_Object = MibTableColumn
coWDSLinkRadio = _CoWDSLinkRadio_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 3),
    _CoWDSLinkRadio_Type()
)
coWDSLinkRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkRadio.setStatus("current")
_CoWDSLinkPeerMacAddress_Type = MacAddress
_CoWDSLinkPeerMacAddress_Object = MibTableColumn
coWDSLinkPeerMacAddress = _CoWDSLinkPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 4),
    _CoWDSLinkPeerMacAddress_Type()
)
coWDSLinkPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkPeerMacAddress.setStatus("current")
_CoWDSLinkMaster_Type = TruthValue
_CoWDSLinkMaster_Object = MibTableColumn
coWDSLinkMaster = _CoWDSLinkMaster_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 5),
    _CoWDSLinkMaster_Type()
)
coWDSLinkMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkMaster.setStatus("current")
_CoWDSLinkAuthorized_Type = TruthValue
_CoWDSLinkAuthorized_Object = MibTableColumn
coWDSLinkAuthorized = _CoWDSLinkAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 6),
    _CoWDSLinkAuthorized_Type()
)
coWDSLinkAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkAuthorized.setStatus("current")


class _CoWDSLinkEncryption_Type(Integer32):
    """Custom type coWDSLinkEncryption based on Integer32"""
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


_CoWDSLinkEncryption_Type.__name__ = "Integer32"
_CoWDSLinkEncryption_Object = MibTableColumn
coWDSLinkEncryption = _CoWDSLinkEncryption_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 7),
    _CoWDSLinkEncryption_Type()
)
coWDSLinkEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkEncryption.setStatus("current")
_CoWDSLinkIdleTime_Type = Unsigned32
_CoWDSLinkIdleTime_Object = MibTableColumn
coWDSLinkIdleTime = _CoWDSLinkIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 8),
    _CoWDSLinkIdleTime_Type()
)
coWDSLinkIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkIdleTime.setUnits("seconds")


class _CoWDSLinkSNR_Type(Integer32):
    """Custom type coWDSLinkSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoWDSLinkSNR_Type.__name__ = "Integer32"
_CoWDSLinkSNR_Object = MibTableColumn
coWDSLinkSNR = _CoWDSLinkSNR_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 9),
    _CoWDSLinkSNR_Type()
)
coWDSLinkSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkSNR.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkSNR.setUnits("dBm")
_CoWDSLinkTxRate_Type = Unsigned32
_CoWDSLinkTxRate_Object = MibTableColumn
coWDSLinkTxRate = _CoWDSLinkTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 10),
    _CoWDSLinkTxRate_Type()
)
coWDSLinkTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkTxRate.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkTxRate.setUnits("500Kb/s")
_CoWDSLinkRxRate_Type = Unsigned32
_CoWDSLinkRxRate_Object = MibTableColumn
coWDSLinkRxRate = _CoWDSLinkRxRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 11),
    _CoWDSLinkRxRate_Type()
)
coWDSLinkRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkRxRate.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkRxRate.setUnits("500Kb/s")


class _CoWDSLinkIfIndex_Type(Integer32):
    """Custom type coWDSLinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoWDSLinkIfIndex_Type.__name__ = "Integer32"
_CoWDSLinkIfIndex_Object = MibTableColumn
coWDSLinkIfIndex = _CoWDSLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 12),
    _CoWDSLinkIfIndex_Type()
)
coWDSLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkIfIndex.setStatus("current")
_CoWDSLinkHT_Type = TruthValue
_CoWDSLinkHT_Object = MibTableColumn
coWDSLinkHT = _CoWDSLinkHT_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 13),
    _CoWDSLinkHT_Type()
)
coWDSLinkHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkHT.setStatus("current")
_CoWDSLinkTxMCS_Type = Unsigned32
_CoWDSLinkTxMCS_Object = MibTableColumn
coWDSLinkTxMCS = _CoWDSLinkTxMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 14),
    _CoWDSLinkTxMCS_Type()
)
coWDSLinkTxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkTxMCS.setStatus("current")
_CoWDSLinkRxMCS_Type = Unsigned32
_CoWDSLinkRxMCS_Object = MibTableColumn
coWDSLinkRxMCS = _CoWDSLinkRxMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 15),
    _CoWDSLinkRxMCS_Type()
)
coWDSLinkRxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkRxMCS.setStatus("current")
_CoWDSLinkSignal_Type = Integer32
_CoWDSLinkSignal_Object = MibTableColumn
coWDSLinkSignal = _CoWDSLinkSignal_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 16),
    _CoWDSLinkSignal_Type()
)
coWDSLinkSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkSignal.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkSignal.setUnits("dBm")
_CoWDSLinkNoise_Type = Integer32
_CoWDSLinkNoise_Object = MibTableColumn
coWDSLinkNoise = _CoWDSLinkNoise_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 17),
    _CoWDSLinkNoise_Type()
)
coWDSLinkNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSLinkNoise.setStatus("current")
if mibBuilder.loadTexts:
    coWDSLinkNoise.setUnits("dBm")
_CoWDSNetworkScanGroup_ObjectIdentity = ObjectIdentity
coWDSNetworkScanGroup = _CoWDSNetworkScanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5)
)
_CoWDSNetworkScanTable_Object = MibTable
coWDSNetworkScanTable = _CoWDSNetworkScanTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coWDSNetworkScanTable.setStatus("current")
_CoWDSNetworkScanEntry_Object = MibTableRow
coWDSNetworkScanEntry = _CoWDSNetworkScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1)
)
coWDSNetworkScanEntry.setIndexNames(
    (0, "COLUBRIS-WDS-MIB", "coWDSScanRadioIndex"),
    (0, "COLUBRIS-WDS-MIB", "coWDSScanPeerIndex"),
)
if mibBuilder.loadTexts:
    coWDSNetworkScanEntry.setStatus("current")


class _CoWDSScanRadioIndex_Type(Integer32):
    """Custom type coWDSScanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoWDSScanRadioIndex_Type.__name__ = "Integer32"
_CoWDSScanRadioIndex_Object = MibTableColumn
coWDSScanRadioIndex = _CoWDSScanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 1),
    _CoWDSScanRadioIndex_Type()
)
coWDSScanRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coWDSScanRadioIndex.setStatus("current")


class _CoWDSScanPeerIndex_Type(Integer32):
    """Custom type coWDSScanPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CoWDSScanPeerIndex_Type.__name__ = "Integer32"
_CoWDSScanPeerIndex_Object = MibTableColumn
coWDSScanPeerIndex = _CoWDSScanPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 2),
    _CoWDSScanPeerIndex_Type()
)
coWDSScanPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coWDSScanPeerIndex.setStatus("current")
_CoWDSScanGroupId_Type = Unsigned32
_CoWDSScanGroupId_Object = MibTableColumn
coWDSScanGroupId = _CoWDSScanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 3),
    _CoWDSScanGroupId_Type()
)
coWDSScanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanGroupId.setStatus("current")
_CoWDSScanPeerMacAddress_Type = MacAddress
_CoWDSScanPeerMacAddress_Object = MibTableColumn
coWDSScanPeerMacAddress = _CoWDSScanPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 4),
    _CoWDSScanPeerMacAddress_Type()
)
coWDSScanPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanPeerMacAddress.setStatus("current")


class _CoWDSScanChannel_Type(Unsigned32):
    """Custom type coWDSScanChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_CoWDSScanChannel_Type.__name__ = "Unsigned32"
_CoWDSScanChannel_Object = MibTableColumn
coWDSScanChannel = _CoWDSScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 5),
    _CoWDSScanChannel_Type()
)
coWDSScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanChannel.setStatus("current")


class _CoWDSScanSNR_Type(Integer32):
    """Custom type coWDSScanSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoWDSScanSNR_Type.__name__ = "Integer32"
_CoWDSScanSNR_Object = MibTableColumn
coWDSScanSNR = _CoWDSScanSNR_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 6),
    _CoWDSScanSNR_Type()
)
coWDSScanSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanSNR.setStatus("current")
if mibBuilder.loadTexts:
    coWDSScanSNR.setUnits("dBm")


class _CoWDSScanMode_Type(Integer32):
    """Custom type coWDSScanMode based on Integer32"""
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


_CoWDSScanMode_Type.__name__ = "Integer32"
_CoWDSScanMode_Object = MibTableColumn
coWDSScanMode = _CoWDSScanMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 7),
    _CoWDSScanMode_Type()
)
coWDSScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanMode.setStatus("current")
_CoWDSScanAvailable_Type = TruthValue
_CoWDSScanAvailable_Object = MibTableColumn
coWDSScanAvailable = _CoWDSScanAvailable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 8),
    _CoWDSScanAvailable_Type()
)
coWDSScanAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coWDSScanAvailable.setStatus("current")
_ColubrisWdsMIBConformance_ObjectIdentity = ObjectIdentity
colubrisWdsMIBConformance = _ColubrisWdsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2)
)
_ColubrisWdsMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisWdsMIBCompliances = _ColubrisWdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 1)
)
_ColubrisWdsMIBGroups_ObjectIdentity = ObjectIdentity
colubrisWdsMIBGroups = _ColubrisWdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2)
)

# Managed Objects groups

colubrisWDSInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 1)
)
colubrisWDSInfoMIBGroup.setObjects(
      *(("COLUBRIS-WDS-MIB", "coWDSNumberOfGroup"),
        ("COLUBRIS-WDS-MIB", "coWDSDynamicModeImplemented"))
)
if mibBuilder.loadTexts:
    colubrisWDSInfoMIBGroup.setStatus("current")

colubrisWDSRadioMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 2)
)
colubrisWDSRadioMIBGroup.setObjects(
      *(("COLUBRIS-WDS-MIB", "coWDSRadioAckDistance"),
        ("COLUBRIS-WDS-MIB", "coWDSRadioQoS"))
)
if mibBuilder.loadTexts:
    colubrisWDSRadioMIBGroup.setStatus("current")

colubrisWDSGroupMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 3)
)
colubrisWDSGroupMIBGroup.setObjects(
      *(("COLUBRIS-WDS-MIB", "coWDSGroupName"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupState"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupSecurity"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupAddressing"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupStaticMacAddress"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupDynamicMode"),
        ("COLUBRIS-WDS-MIB", "coWDSGroupDynamicGroupId"))
)
if mibBuilder.loadTexts:
    colubrisWDSGroupMIBGroup.setStatus("current")

colubrisWDSLinkMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 4)
)
colubrisWDSLinkMIBGroup.setObjects(
      *(("COLUBRIS-WDS-MIB", "coWDSLinkState"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkRadio"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkPeerMacAddress"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkMaster"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkAuthorized"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkEncryption"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkIdleTime"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkSNR"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkTxRate"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkRxRate"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkIfIndex"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkHT"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkTxMCS"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkRxMCS"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkSignal"),
        ("COLUBRIS-WDS-MIB", "coWDSLinkNoise"))
)
if mibBuilder.loadTexts:
    colubrisWDSLinkMIBGroup.setStatus("current")

colubrisWDSScanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 5)
)
colubrisWDSScanMIBGroup.setObjects(
      *(("COLUBRIS-WDS-MIB", "coWDSScanGroupId"),
        ("COLUBRIS-WDS-MIB", "coWDSScanPeerMacAddress"),
        ("COLUBRIS-WDS-MIB", "coWDSScanChannel"),
        ("COLUBRIS-WDS-MIB", "coWDSScanSNR"),
        ("COLUBRIS-WDS-MIB", "coWDSScanMode"),
        ("COLUBRIS-WDS-MIB", "coWDSScanAvailable"))
)
if mibBuilder.loadTexts:
    colubrisWDSScanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisWdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisWdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-WDS-MIB",
    **{"colubrisWdsMIB": colubrisWdsMIB,
       "colubrisWdsMIBObjects": colubrisWdsMIBObjects,
       "coWDSInfoGroup": coWDSInfoGroup,
       "coWDSNumberOfGroup": coWDSNumberOfGroup,
       "coWDSDynamicModeImplemented": coWDSDynamicModeImplemented,
       "coWDSRadioGroup": coWDSRadioGroup,
       "coWDSRadioTable": coWDSRadioTable,
       "coWDSRadioEntry": coWDSRadioEntry,
       "coWDSRadioIndex": coWDSRadioIndex,
       "coWDSRadioAckDistance": coWDSRadioAckDistance,
       "coWDSRadioQoS": coWDSRadioQoS,
       "coWDSGroupGroup": coWDSGroupGroup,
       "coWDSGroupTable": coWDSGroupTable,
       "coWDSGroupEntry": coWDSGroupEntry,
       "coWDSGroupIndex": coWDSGroupIndex,
       "coWDSGroupName": coWDSGroupName,
       "coWDSGroupState": coWDSGroupState,
       "coWDSGroupSecurity": coWDSGroupSecurity,
       "coWDSGroupAddressing": coWDSGroupAddressing,
       "coWDSGroupStaticMacAddress": coWDSGroupStaticMacAddress,
       "coWDSGroupDynamicMode": coWDSGroupDynamicMode,
       "coWDSGroupDynamicGroupId": coWDSGroupDynamicGroupId,
       "coWDSLinkGroup": coWDSLinkGroup,
       "coWDSLinkTable": coWDSLinkTable,
       "coWDSLinkEntry": coWDSLinkEntry,
       "coWDSLinkIndex": coWDSLinkIndex,
       "coWDSLinkState": coWDSLinkState,
       "coWDSLinkRadio": coWDSLinkRadio,
       "coWDSLinkPeerMacAddress": coWDSLinkPeerMacAddress,
       "coWDSLinkMaster": coWDSLinkMaster,
       "coWDSLinkAuthorized": coWDSLinkAuthorized,
       "coWDSLinkEncryption": coWDSLinkEncryption,
       "coWDSLinkIdleTime": coWDSLinkIdleTime,
       "coWDSLinkSNR": coWDSLinkSNR,
       "coWDSLinkTxRate": coWDSLinkTxRate,
       "coWDSLinkRxRate": coWDSLinkRxRate,
       "coWDSLinkIfIndex": coWDSLinkIfIndex,
       "coWDSLinkHT": coWDSLinkHT,
       "coWDSLinkTxMCS": coWDSLinkTxMCS,
       "coWDSLinkRxMCS": coWDSLinkRxMCS,
       "coWDSLinkSignal": coWDSLinkSignal,
       "coWDSLinkNoise": coWDSLinkNoise,
       "coWDSNetworkScanGroup": coWDSNetworkScanGroup,
       "coWDSNetworkScanTable": coWDSNetworkScanTable,
       "coWDSNetworkScanEntry": coWDSNetworkScanEntry,
       "coWDSScanRadioIndex": coWDSScanRadioIndex,
       "coWDSScanPeerIndex": coWDSScanPeerIndex,
       "coWDSScanGroupId": coWDSScanGroupId,
       "coWDSScanPeerMacAddress": coWDSScanPeerMacAddress,
       "coWDSScanChannel": coWDSScanChannel,
       "coWDSScanSNR": coWDSScanSNR,
       "coWDSScanMode": coWDSScanMode,
       "coWDSScanAvailable": coWDSScanAvailable,
       "colubrisWdsMIBConformance": colubrisWdsMIBConformance,
       "colubrisWdsMIBCompliances": colubrisWdsMIBCompliances,
       "colubrisWdsMIBCompliance": colubrisWdsMIBCompliance,
       "colubrisWdsMIBGroups": colubrisWdsMIBGroups,
       "colubrisWDSInfoMIBGroup": colubrisWDSInfoMIBGroup,
       "colubrisWDSRadioMIBGroup": colubrisWDSRadioMIBGroup,
       "colubrisWDSGroupMIBGroup": colubrisWDSGroupMIBGroup,
       "colubrisWDSLinkMIBGroup": colubrisWDSLinkMIBGroup,
       "colubrisWDSScanMIBGroup": colubrisWDSScanMIBGroup}
)
