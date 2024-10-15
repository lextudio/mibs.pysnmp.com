# SNMP MIB module (IPSEC-IKEACTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPSEC-IKEACTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:10 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(IpsaCredentialType,
 IpsaIdentityFilter,
 IpsecDoiIdentType,
 ipsaSharedGroup) = mibBuilder.importSymbols(
    "IPSEC-IPSECACTION-MIB",
    "IpsaCredentialType",
    "IpsaIdentityFilter",
    "IpsecDoiIdentType",
    "ipsaSharedGroup")

(SpdIPPacketLogging,
 spdActions,
 spdEndGroupInterface) = mibBuilder.importSymbols(
    "IPSEC-SPD-MIB",
    "SpdIPPacketLogging",
    "spdActions",
    "spdEndGroupInterface")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ipiaMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2)
)
ipiaMIB.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IkeEncryptionAlgorithm(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IkeAuthMethod(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IkeHashAlgorithm(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IkeGroupDescription(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class IpsecDoiSecProtocolId(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_IpiaConfigObjects_ObjectIdentity = ObjectIdentity
ipiaConfigObjects = _IpiaConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1)
)
_IpiaLocalConfigObjects_ObjectIdentity = ObjectIdentity
ipiaLocalConfigObjects = _IpiaLocalConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 1)
)
_IpiaStaticFilters_ObjectIdentity = ObjectIdentity
ipiaStaticFilters = _IpiaStaticFilters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 2)
)
_IpiaIkePhase1Filter_Type = Integer32
_IpiaIkePhase1Filter_Object = MibScalar
ipiaIkePhase1Filter = _IpiaIkePhase1Filter_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 2, 1),
    _IpiaIkePhase1Filter_Type()
)
ipiaIkePhase1Filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkePhase1Filter.setStatus("current")
_IpiaIkePhase2Filter_Type = Integer32
_IpiaIkePhase2Filter_Object = MibScalar
ipiaIkePhase2Filter = _IpiaIkePhase2Filter_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 2, 2),
    _IpiaIkePhase2Filter_Type()
)
ipiaIkePhase2Filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkePhase2Filter.setStatus("current")
_IpiaCredentialFilterTable_Object = MibTable
ipiaCredentialFilterTable = _IpiaCredentialFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ipiaCredentialFilterTable.setStatus("current")
_IpiaCredentialFilterEntry_Object = MibTableRow
ipiaCredentialFilterEntry = _IpiaCredentialFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1)
)
ipiaCredentialFilterEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaCredFiltName"),
)
if mibBuilder.loadTexts:
    ipiaCredentialFilterEntry.setStatus("current")


class _IpiaCredFiltName_Type(SnmpAdminString):
    """Custom type ipiaCredFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaCredFiltName_Type.__name__ = "SnmpAdminString"
_IpiaCredFiltName_Object = MibTableColumn
ipiaCredFiltName = _IpiaCredFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 1),
    _IpiaCredFiltName_Type()
)
ipiaCredFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaCredFiltName.setStatus("current")


class _IpiaCredFiltCredentialType_Type(IpsaCredentialType):
    """Custom type ipiaCredFiltCredentialType based on IpsaCredentialType"""


_IpiaCredFiltCredentialType_Object = MibTableColumn
ipiaCredFiltCredentialType = _IpiaCredFiltCredentialType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 2),
    _IpiaCredFiltCredentialType_Type()
)
ipiaCredFiltCredentialType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltCredentialType.setStatus("current")


class _IpiaCredFiltMatchFieldName_Type(OctetString):
    """Custom type ipiaCredFiltMatchFieldName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpiaCredFiltMatchFieldName_Type.__name__ = "OctetString"
_IpiaCredFiltMatchFieldName_Object = MibTableColumn
ipiaCredFiltMatchFieldName = _IpiaCredFiltMatchFieldName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 3),
    _IpiaCredFiltMatchFieldName_Type()
)
ipiaCredFiltMatchFieldName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltMatchFieldName.setStatus("current")


class _IpiaCredFiltMatchFieldValue_Type(OctetString):
    """Custom type ipiaCredFiltMatchFieldValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4096),
    )


_IpiaCredFiltMatchFieldValue_Type.__name__ = "OctetString"
_IpiaCredFiltMatchFieldValue_Object = MibTableColumn
ipiaCredFiltMatchFieldValue = _IpiaCredFiltMatchFieldValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 4),
    _IpiaCredFiltMatchFieldValue_Type()
)
ipiaCredFiltMatchFieldValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltMatchFieldValue.setStatus("current")


class _IpiaCredFiltAcceptCredFrom_Type(OctetString):
    """Custom type ipiaCredFiltAcceptCredFrom based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 117),
    )


_IpiaCredFiltAcceptCredFrom_Type.__name__ = "OctetString"
_IpiaCredFiltAcceptCredFrom_Object = MibTableColumn
ipiaCredFiltAcceptCredFrom = _IpiaCredFiltAcceptCredFrom_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 5),
    _IpiaCredFiltAcceptCredFrom_Type()
)
ipiaCredFiltAcceptCredFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltAcceptCredFrom.setStatus("current")
_IpiaCredFiltLastChanged_Type = TimeStamp
_IpiaCredFiltLastChanged_Object = MibTableColumn
ipiaCredFiltLastChanged = _IpiaCredFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 6),
    _IpiaCredFiltLastChanged_Type()
)
ipiaCredFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaCredFiltLastChanged.setStatus("current")


class _IpiaCredFiltStorageType_Type(StorageType):
    """Custom type ipiaCredFiltStorageType based on StorageType"""


_IpiaCredFiltStorageType_Object = MibTableColumn
ipiaCredFiltStorageType = _IpiaCredFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 7),
    _IpiaCredFiltStorageType_Type()
)
ipiaCredFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltStorageType.setStatus("current")
_IpiaCredFiltRowStatus_Type = RowStatus
_IpiaCredFiltRowStatus_Object = MibTableColumn
ipiaCredFiltRowStatus = _IpiaCredFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 3, 1, 8),
    _IpiaCredFiltRowStatus_Type()
)
ipiaCredFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCredFiltRowStatus.setStatus("current")
_IpiaPeerIdentityFilterTable_Object = MibTable
ipiaPeerIdentityFilterTable = _IpiaPeerIdentityFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ipiaPeerIdentityFilterTable.setStatus("current")
_IpiaPeerIdentityFilterEntry_Object = MibTableRow
ipiaPeerIdentityFilterEntry = _IpiaPeerIdentityFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1)
)
ipiaPeerIdentityFilterEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltName"),
)
if mibBuilder.loadTexts:
    ipiaPeerIdentityFilterEntry.setStatus("current")


class _IpiaPeerIdFiltName_Type(SnmpAdminString):
    """Custom type ipiaPeerIdFiltName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaPeerIdFiltName_Type.__name__ = "SnmpAdminString"
_IpiaPeerIdFiltName_Object = MibTableColumn
ipiaPeerIdFiltName = _IpiaPeerIdFiltName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 1),
    _IpiaPeerIdFiltName_Type()
)
ipiaPeerIdFiltName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltName.setStatus("current")
_IpiaPeerIdFiltIdentityType_Type = IpsecDoiIdentType
_IpiaPeerIdFiltIdentityType_Object = MibTableColumn
ipiaPeerIdFiltIdentityType = _IpiaPeerIdFiltIdentityType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 2),
    _IpiaPeerIdFiltIdentityType_Type()
)
ipiaPeerIdFiltIdentityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltIdentityType.setStatus("current")
_IpiaPeerIdFiltIdentityValue_Type = IpsaIdentityFilter
_IpiaPeerIdFiltIdentityValue_Object = MibTableColumn
ipiaPeerIdFiltIdentityValue = _IpiaPeerIdFiltIdentityValue_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 3),
    _IpiaPeerIdFiltIdentityValue_Type()
)
ipiaPeerIdFiltIdentityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltIdentityValue.setStatus("current")
_IpiaPeerIdFiltLastChanged_Type = TimeStamp
_IpiaPeerIdFiltLastChanged_Object = MibTableColumn
ipiaPeerIdFiltLastChanged = _IpiaPeerIdFiltLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 4),
    _IpiaPeerIdFiltLastChanged_Type()
)
ipiaPeerIdFiltLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltLastChanged.setStatus("current")


class _IpiaPeerIdFiltStorageType_Type(StorageType):
    """Custom type ipiaPeerIdFiltStorageType based on StorageType"""


_IpiaPeerIdFiltStorageType_Object = MibTableColumn
ipiaPeerIdFiltStorageType = _IpiaPeerIdFiltStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 5),
    _IpiaPeerIdFiltStorageType_Type()
)
ipiaPeerIdFiltStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltStorageType.setStatus("current")
_IpiaPeerIdFiltRowStatus_Type = RowStatus
_IpiaPeerIdFiltRowStatus_Object = MibTableColumn
ipiaPeerIdFiltRowStatus = _IpiaPeerIdFiltRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 4, 1, 6),
    _IpiaPeerIdFiltRowStatus_Type()
)
ipiaPeerIdFiltRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaPeerIdFiltRowStatus.setStatus("current")
_IpiaStaticActions_ObjectIdentity = ObjectIdentity
ipiaStaticActions = _IpiaStaticActions_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 5)
)
_IpiaRejectIKEAction_Type = Integer32
_IpiaRejectIKEAction_Object = MibScalar
ipiaRejectIKEAction = _IpiaRejectIKEAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 5, 1),
    _IpiaRejectIKEAction_Type()
)
ipiaRejectIKEAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaRejectIKEAction.setStatus("current")
_IpiaRejectIKEActionLog_Type = Integer32
_IpiaRejectIKEActionLog_Object = MibScalar
ipiaRejectIKEActionLog = _IpiaRejectIKEActionLog_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 5, 2),
    _IpiaRejectIKEActionLog_Type()
)
ipiaRejectIKEActionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaRejectIKEActionLog.setStatus("current")
_IpiaIkeActionTable_Object = MibTable
ipiaIkeActionTable = _IpiaIkeActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ipiaIkeActionTable.setStatus("current")
_IpiaIkeActionEntry_Object = MibTableRow
ipiaIkeActionEntry = _IpiaIkeActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1)
)
ipiaIkeActionEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActName"),
)
if mibBuilder.loadTexts:
    ipiaIkeActionEntry.setStatus("current")


class _IpiaIkeActName_Type(SnmpAdminString):
    """Custom type ipiaIkeActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIkeActName_Type.__name__ = "SnmpAdminString"
_IpiaIkeActName_Object = MibTableColumn
ipiaIkeActName = _IpiaIkeActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 1),
    _IpiaIkeActName_Type()
)
ipiaIkeActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIkeActName.setStatus("current")


class _IpiaIkeActParametersName_Type(SnmpAdminString):
    """Custom type ipiaIkeActParametersName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIkeActParametersName_Type.__name__ = "SnmpAdminString"
_IpiaIkeActParametersName_Object = MibTableColumn
ipiaIkeActParametersName = _IpiaIkeActParametersName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 2),
    _IpiaIkeActParametersName_Type()
)
ipiaIkeActParametersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActParametersName.setStatus("current")


class _IpiaIkeActThresholdDerivedKeys_Type(Integer32):
    """Custom type ipiaIkeActThresholdDerivedKeys based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IpiaIkeActThresholdDerivedKeys_Type.__name__ = "Integer32"
_IpiaIkeActThresholdDerivedKeys_Object = MibTableColumn
ipiaIkeActThresholdDerivedKeys = _IpiaIkeActThresholdDerivedKeys_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 3),
    _IpiaIkeActThresholdDerivedKeys_Type()
)
ipiaIkeActThresholdDerivedKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActThresholdDerivedKeys.setStatus("current")


class _IpiaIkeActExchangeMode_Type(Integer32):
    """Custom type ipiaIkeActExchangeMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("agressive", 2),
          ("main", 1))
    )


_IpiaIkeActExchangeMode_Type.__name__ = "Integer32"
_IpiaIkeActExchangeMode_Object = MibTableColumn
ipiaIkeActExchangeMode = _IpiaIkeActExchangeMode_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 4),
    _IpiaIkeActExchangeMode_Type()
)
ipiaIkeActExchangeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActExchangeMode.setStatus("current")
_IpiaIkeActAgressiveModeGroupId_Type = IkeGroupDescription
_IpiaIkeActAgressiveModeGroupId_Object = MibTableColumn
ipiaIkeActAgressiveModeGroupId = _IpiaIkeActAgressiveModeGroupId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 5),
    _IpiaIkeActAgressiveModeGroupId_Type()
)
ipiaIkeActAgressiveModeGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActAgressiveModeGroupId.setStatus("current")
_IpiaIkeActIdentityType_Type = IpsecDoiIdentType
_IpiaIkeActIdentityType_Object = MibTableColumn
ipiaIkeActIdentityType = _IpiaIkeActIdentityType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 6),
    _IpiaIkeActIdentityType_Type()
)
ipiaIkeActIdentityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActIdentityType.setStatus("current")


class _IpiaIkeActIdentityContext_Type(SnmpAdminString):
    """Custom type ipiaIkeActIdentityContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIkeActIdentityContext_Type.__name__ = "SnmpAdminString"
_IpiaIkeActIdentityContext_Object = MibTableColumn
ipiaIkeActIdentityContext = _IpiaIkeActIdentityContext_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 7),
    _IpiaIkeActIdentityContext_Type()
)
ipiaIkeActIdentityContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActIdentityContext.setStatus("current")


class _IpiaIkeActPeerName_Type(SnmpAdminString):
    """Custom type ipiaIkeActPeerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaIkeActPeerName_Type.__name__ = "SnmpAdminString"
_IpiaIkeActPeerName_Object = MibTableColumn
ipiaIkeActPeerName = _IpiaIkeActPeerName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 8),
    _IpiaIkeActPeerName_Type()
)
ipiaIkeActPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActPeerName.setStatus("current")


class _IpiaIkeActDoActionLogging_Type(TruthValue):
    """Custom type ipiaIkeActDoActionLogging based on TruthValue"""


_IpiaIkeActDoActionLogging_Object = MibTableColumn
ipiaIkeActDoActionLogging = _IpiaIkeActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 9),
    _IpiaIkeActDoActionLogging_Type()
)
ipiaIkeActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActDoActionLogging.setStatus("current")


class _IpiaIkeActDoPacketLogging_Type(SpdIPPacketLogging):
    """Custom type ipiaIkeActDoPacketLogging based on SpdIPPacketLogging"""
    defaultValue = -1


_IpiaIkeActDoPacketLogging_Object = MibTableColumn
ipiaIkeActDoPacketLogging = _IpiaIkeActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 10),
    _IpiaIkeActDoPacketLogging_Type()
)
ipiaIkeActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActDoPacketLogging.setStatus("current")


class _IpiaIkeActVendorId_Type(OctetString):
    """Custom type ipiaIkeActVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_IpiaIkeActVendorId_Type.__name__ = "OctetString"
_IpiaIkeActVendorId_Object = MibTableColumn
ipiaIkeActVendorId = _IpiaIkeActVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 11),
    _IpiaIkeActVendorId_Type()
)
ipiaIkeActVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActVendorId.setStatus("current")
_IpiaIkeActLastChanged_Type = TimeStamp
_IpiaIkeActLastChanged_Object = MibTableColumn
ipiaIkeActLastChanged = _IpiaIkeActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 12),
    _IpiaIkeActLastChanged_Type()
)
ipiaIkeActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkeActLastChanged.setStatus("current")


class _IpiaIkeActStorageType_Type(StorageType):
    """Custom type ipiaIkeActStorageType based on StorageType"""


_IpiaIkeActStorageType_Object = MibTableColumn
ipiaIkeActStorageType = _IpiaIkeActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 13),
    _IpiaIkeActStorageType_Type()
)
ipiaIkeActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActStorageType.setStatus("current")
_IpiaIkeActRowStatus_Type = RowStatus
_IpiaIkeActRowStatus_Object = MibTableColumn
ipiaIkeActRowStatus = _IpiaIkeActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 6, 1, 14),
    _IpiaIkeActRowStatus_Type()
)
ipiaIkeActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActRowStatus.setStatus("current")
_IpiaIpsecActionTable_Object = MibTable
ipiaIpsecActionTable = _IpiaIpsecActionTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ipiaIpsecActionTable.setStatus("current")
_IpiaIpsecActionEntry_Object = MibTableRow
ipiaIpsecActionEntry = _IpiaIpsecActionEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1)
)
ipiaIpsecActionEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecActName"),
)
if mibBuilder.loadTexts:
    ipiaIpsecActionEntry.setStatus("current")


class _IpiaIpsecActName_Type(SnmpAdminString):
    """Custom type ipiaIpsecActName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecActName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecActName_Object = MibTableColumn
ipiaIpsecActName = _IpiaIpsecActName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 1),
    _IpiaIpsecActName_Type()
)
ipiaIpsecActName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecActName.setStatus("current")


class _IpiaIpsecActParametersName_Type(SnmpAdminString):
    """Custom type ipiaIpsecActParametersName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecActParametersName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecActParametersName_Object = MibTableColumn
ipiaIpsecActParametersName = _IpiaIpsecActParametersName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 2),
    _IpiaIpsecActParametersName_Type()
)
ipiaIpsecActParametersName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActParametersName.setStatus("current")


class _IpiaIpsecActProposalsName_Type(SnmpAdminString):
    """Custom type ipiaIpsecActProposalsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecActProposalsName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecActProposalsName_Object = MibTableColumn
ipiaIpsecActProposalsName = _IpiaIpsecActProposalsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 3),
    _IpiaIpsecActProposalsName_Type()
)
ipiaIpsecActProposalsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActProposalsName.setStatus("current")
_IpiaIpsecActUsePfs_Type = TruthValue
_IpiaIpsecActUsePfs_Object = MibTableColumn
ipiaIpsecActUsePfs = _IpiaIpsecActUsePfs_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 4),
    _IpiaIpsecActUsePfs_Type()
)
ipiaIpsecActUsePfs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActUsePfs.setStatus("current")


class _IpiaIpsecActVendorId_Type(OctetString):
    """Custom type ipiaIpsecActVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpiaIpsecActVendorId_Type.__name__ = "OctetString"
_IpiaIpsecActVendorId_Object = MibTableColumn
ipiaIpsecActVendorId = _IpiaIpsecActVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 5),
    _IpiaIpsecActVendorId_Type()
)
ipiaIpsecActVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActVendorId.setStatus("current")
_IpiaIpsecActGroupId_Type = IkeGroupDescription
_IpiaIpsecActGroupId_Object = MibTableColumn
ipiaIpsecActGroupId = _IpiaIpsecActGroupId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 6),
    _IpiaIpsecActGroupId_Type()
)
ipiaIpsecActGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActGroupId.setStatus("current")


class _IpiaIpsecActPeerGatewayIdName_Type(OctetString):
    """Custom type ipiaIpsecActPeerGatewayIdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 116),
    )


_IpiaIpsecActPeerGatewayIdName_Type.__name__ = "OctetString"
_IpiaIpsecActPeerGatewayIdName_Object = MibTableColumn
ipiaIpsecActPeerGatewayIdName = _IpiaIpsecActPeerGatewayIdName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 7),
    _IpiaIpsecActPeerGatewayIdName_Type()
)
ipiaIpsecActPeerGatewayIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActPeerGatewayIdName.setStatus("current")
_IpiaIpsecActUseIkeGroup_Type = TruthValue
_IpiaIpsecActUseIkeGroup_Object = MibTableColumn
ipiaIpsecActUseIkeGroup = _IpiaIpsecActUseIkeGroup_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 8),
    _IpiaIpsecActUseIkeGroup_Type()
)
ipiaIpsecActUseIkeGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActUseIkeGroup.setStatus("current")


class _IpiaIpsecActGranularity_Type(Integer32):
    """Custom type ipiaIpsecActGranularity based on Integer32"""
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
        *(("address", 2),
          ("port", 4),
          ("protocol", 3),
          ("subnet", 1))
    )


_IpiaIpsecActGranularity_Type.__name__ = "Integer32"
_IpiaIpsecActGranularity_Object = MibTableColumn
ipiaIpsecActGranularity = _IpiaIpsecActGranularity_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 9),
    _IpiaIpsecActGranularity_Type()
)
ipiaIpsecActGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActGranularity.setStatus("current")


class _IpiaIpsecActMode_Type(Integer32):
    """Custom type ipiaIpsecActMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transport", 2),
          ("tunnel", 1))
    )


_IpiaIpsecActMode_Type.__name__ = "Integer32"
_IpiaIpsecActMode_Object = MibTableColumn
ipiaIpsecActMode = _IpiaIpsecActMode_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 10),
    _IpiaIpsecActMode_Type()
)
ipiaIpsecActMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActMode.setStatus("current")


class _IpiaIpsecActDFHandling_Type(Integer32):
    """Custom type ipiaIpsecActDFHandling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("copy", 1),
          ("set", 2))
    )


_IpiaIpsecActDFHandling_Type.__name__ = "Integer32"
_IpiaIpsecActDFHandling_Object = MibTableColumn
ipiaIpsecActDFHandling = _IpiaIpsecActDFHandling_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 11),
    _IpiaIpsecActDFHandling_Type()
)
ipiaIpsecActDFHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActDFHandling.setStatus("current")


class _IpiaIpsecActDoActionLogging_Type(TruthValue):
    """Custom type ipiaIpsecActDoActionLogging based on TruthValue"""


_IpiaIpsecActDoActionLogging_Object = MibTableColumn
ipiaIpsecActDoActionLogging = _IpiaIpsecActDoActionLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 12),
    _IpiaIpsecActDoActionLogging_Type()
)
ipiaIpsecActDoActionLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActDoActionLogging.setStatus("current")


class _IpiaIpsecActDoPacketLogging_Type(SpdIPPacketLogging):
    """Custom type ipiaIpsecActDoPacketLogging based on SpdIPPacketLogging"""
    defaultValue = -1


_IpiaIpsecActDoPacketLogging_Object = MibTableColumn
ipiaIpsecActDoPacketLogging = _IpiaIpsecActDoPacketLogging_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 13),
    _IpiaIpsecActDoPacketLogging_Type()
)
ipiaIpsecActDoPacketLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActDoPacketLogging.setStatus("current")
_IpiaIpsecActLastChanged_Type = TimeStamp
_IpiaIpsecActLastChanged_Object = MibTableColumn
ipiaIpsecActLastChanged = _IpiaIpsecActLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 14),
    _IpiaIpsecActLastChanged_Type()
)
ipiaIpsecActLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIpsecActLastChanged.setStatus("current")


class _IpiaIpsecActStorageType_Type(StorageType):
    """Custom type ipiaIpsecActStorageType based on StorageType"""


_IpiaIpsecActStorageType_Object = MibTableColumn
ipiaIpsecActStorageType = _IpiaIpsecActStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 15),
    _IpiaIpsecActStorageType_Type()
)
ipiaIpsecActStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActStorageType.setStatus("current")
_IpiaIpsecActRowStatus_Type = RowStatus
_IpiaIpsecActRowStatus_Object = MibTableColumn
ipiaIpsecActRowStatus = _IpiaIpsecActRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 7, 1, 16),
    _IpiaIpsecActRowStatus_Type()
)
ipiaIpsecActRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecActRowStatus.setStatus("current")
_IpiaSaNegotiationParametersTable_Object = MibTable
ipiaSaNegotiationParametersTable = _IpiaSaNegotiationParametersTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ipiaSaNegotiationParametersTable.setStatus("current")
_IpiaSaNegotiationParametersEntry_Object = MibTableRow
ipiaSaNegotiationParametersEntry = _IpiaSaNegotiationParametersEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1)
)
ipiaSaNegotiationParametersEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaSaNegParamName"),
)
if mibBuilder.loadTexts:
    ipiaSaNegotiationParametersEntry.setStatus("current")


class _IpiaSaNegParamName_Type(SnmpAdminString):
    """Custom type ipiaSaNegParamName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaSaNegParamName_Type.__name__ = "SnmpAdminString"
_IpiaSaNegParamName_Object = MibTableColumn
ipiaSaNegParamName = _IpiaSaNegParamName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 1),
    _IpiaSaNegParamName_Type()
)
ipiaSaNegParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaSaNegParamName.setStatus("current")
_IpiaSaNegParamMinLifetimeSecs_Type = Unsigned32
_IpiaSaNegParamMinLifetimeSecs_Object = MibTableColumn
ipiaSaNegParamMinLifetimeSecs = _IpiaSaNegParamMinLifetimeSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 2),
    _IpiaSaNegParamMinLifetimeSecs_Type()
)
ipiaSaNegParamMinLifetimeSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamMinLifetimeSecs.setStatus("current")
if mibBuilder.loadTexts:
    ipiaSaNegParamMinLifetimeSecs.setUnits("seconds")
_IpiaSaNegParamMinLifetimeKB_Type = Unsigned32
_IpiaSaNegParamMinLifetimeKB_Object = MibTableColumn
ipiaSaNegParamMinLifetimeKB = _IpiaSaNegParamMinLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 3),
    _IpiaSaNegParamMinLifetimeKB_Type()
)
ipiaSaNegParamMinLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamMinLifetimeKB.setStatus("current")


class _IpiaSaNegParamRefreshThreshSecs_Type(Unsigned32):
    """Custom type ipiaSaNegParamRefreshThreshSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IpiaSaNegParamRefreshThreshSecs_Type.__name__ = "Unsigned32"
_IpiaSaNegParamRefreshThreshSecs_Object = MibTableColumn
ipiaSaNegParamRefreshThreshSecs = _IpiaSaNegParamRefreshThreshSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 4),
    _IpiaSaNegParamRefreshThreshSecs_Type()
)
ipiaSaNegParamRefreshThreshSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamRefreshThreshSecs.setStatus("current")
if mibBuilder.loadTexts:
    ipiaSaNegParamRefreshThreshSecs.setUnits("seconds")


class _IpiaSaNegParamRefreshThresholdKB_Type(Unsigned32):
    """Custom type ipiaSaNegParamRefreshThresholdKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IpiaSaNegParamRefreshThresholdKB_Type.__name__ = "Unsigned32"
_IpiaSaNegParamRefreshThresholdKB_Object = MibTableColumn
ipiaSaNegParamRefreshThresholdKB = _IpiaSaNegParamRefreshThresholdKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 5),
    _IpiaSaNegParamRefreshThresholdKB_Type()
)
ipiaSaNegParamRefreshThresholdKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamRefreshThresholdKB.setStatus("current")
_IpiaSaNegParamIdleDurationSecs_Type = Unsigned32
_IpiaSaNegParamIdleDurationSecs_Object = MibTableColumn
ipiaSaNegParamIdleDurationSecs = _IpiaSaNegParamIdleDurationSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 6),
    _IpiaSaNegParamIdleDurationSecs_Type()
)
ipiaSaNegParamIdleDurationSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamIdleDurationSecs.setStatus("current")
if mibBuilder.loadTexts:
    ipiaSaNegParamIdleDurationSecs.setUnits("seconds")
_IpiaSaNegParamLastChanged_Type = TimeStamp
_IpiaSaNegParamLastChanged_Object = MibTableColumn
ipiaSaNegParamLastChanged = _IpiaSaNegParamLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 7),
    _IpiaSaNegParamLastChanged_Type()
)
ipiaSaNegParamLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaSaNegParamLastChanged.setStatus("current")


class _IpiaSaNegParamStorageType_Type(StorageType):
    """Custom type ipiaSaNegParamStorageType based on StorageType"""


_IpiaSaNegParamStorageType_Object = MibTableColumn
ipiaSaNegParamStorageType = _IpiaSaNegParamStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 8),
    _IpiaSaNegParamStorageType_Type()
)
ipiaSaNegParamStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamStorageType.setStatus("current")
_IpiaSaNegParamRowStatus_Type = RowStatus
_IpiaSaNegParamRowStatus_Object = MibTableColumn
ipiaSaNegParamRowStatus = _IpiaSaNegParamRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 8, 1, 9),
    _IpiaSaNegParamRowStatus_Type()
)
ipiaSaNegParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaSaNegParamRowStatus.setStatus("current")
_IpiaIkeActionProposalsTable_Object = MibTable
ipiaIkeActionProposalsTable = _IpiaIkeActionProposalsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9)
)
if mibBuilder.loadTexts:
    ipiaIkeActionProposalsTable.setStatus("current")
_IpiaIkeActionProposalsEntry_Object = MibTableRow
ipiaIkeActionProposalsEntry = _IpiaIkeActionProposalsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1)
)
ipiaIkeActionProposalsEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActName"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActPropPriority"),
)
if mibBuilder.loadTexts:
    ipiaIkeActionProposalsEntry.setStatus("current")


class _IpiaIkeActPropPriority_Type(Integer32):
    """Custom type ipiaIkeActPropPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpiaIkeActPropPriority_Type.__name__ = "Integer32"
_IpiaIkeActPropPriority_Object = MibTableColumn
ipiaIkeActPropPriority = _IpiaIkeActPropPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1, 1),
    _IpiaIkeActPropPriority_Type()
)
ipiaIkeActPropPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIkeActPropPriority.setStatus("current")


class _IpiaIkeActPropName_Type(SnmpAdminString):
    """Custom type ipiaIkeActPropName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIkeActPropName_Type.__name__ = "SnmpAdminString"
_IpiaIkeActPropName_Object = MibTableColumn
ipiaIkeActPropName = _IpiaIkeActPropName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1, 2),
    _IpiaIkeActPropName_Type()
)
ipiaIkeActPropName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActPropName.setStatus("current")
_IpiaIkeActPropLastChanged_Type = TimeStamp
_IpiaIkeActPropLastChanged_Object = MibTableColumn
ipiaIkeActPropLastChanged = _IpiaIkeActPropLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1, 3),
    _IpiaIkeActPropLastChanged_Type()
)
ipiaIkeActPropLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkeActPropLastChanged.setStatus("current")


class _IpiaIkeActPropStorageType_Type(StorageType):
    """Custom type ipiaIkeActPropStorageType based on StorageType"""


_IpiaIkeActPropStorageType_Object = MibTableColumn
ipiaIkeActPropStorageType = _IpiaIkeActPropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1, 4),
    _IpiaIkeActPropStorageType_Type()
)
ipiaIkeActPropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActPropStorageType.setStatus("current")
_IpiaIkeActPropRowStatus_Type = RowStatus
_IpiaIkeActPropRowStatus_Object = MibTableColumn
ipiaIkeActPropRowStatus = _IpiaIkeActPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 9, 1, 5),
    _IpiaIkeActPropRowStatus_Type()
)
ipiaIkeActPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeActPropRowStatus.setStatus("current")
_IpiaIkeProposalTable_Object = MibTable
ipiaIkeProposalTable = _IpiaIkeProposalTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ipiaIkeProposalTable.setStatus("current")
_IpiaIkeProposalEntry_Object = MibTableRow
ipiaIkeProposalEntry = _IpiaIkeProposalEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1)
)
ipiaIkeProposalEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActPropName"),
)
if mibBuilder.loadTexts:
    ipiaIkeProposalEntry.setStatus("current")
_IpiaIkePropLifetimeDerivedKeys_Type = Unsigned32
_IpiaIkePropLifetimeDerivedKeys_Object = MibTableColumn
ipiaIkePropLifetimeDerivedKeys = _IpiaIkePropLifetimeDerivedKeys_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 1),
    _IpiaIkePropLifetimeDerivedKeys_Type()
)
ipiaIkePropLifetimeDerivedKeys.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropLifetimeDerivedKeys.setStatus("current")
_IpiaIkePropCipherAlgorithm_Type = IkeEncryptionAlgorithm
_IpiaIkePropCipherAlgorithm_Object = MibTableColumn
ipiaIkePropCipherAlgorithm = _IpiaIkePropCipherAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 2),
    _IpiaIkePropCipherAlgorithm_Type()
)
ipiaIkePropCipherAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropCipherAlgorithm.setStatus("current")
_IpiaIkePropCipherKeyLength_Type = Unsigned32
_IpiaIkePropCipherKeyLength_Object = MibTableColumn
ipiaIkePropCipherKeyLength = _IpiaIkePropCipherKeyLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 3),
    _IpiaIkePropCipherKeyLength_Type()
)
ipiaIkePropCipherKeyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropCipherKeyLength.setStatus("current")
_IpiaIkePropCipherKeyRounds_Type = Unsigned32
_IpiaIkePropCipherKeyRounds_Object = MibTableColumn
ipiaIkePropCipherKeyRounds = _IpiaIkePropCipherKeyRounds_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 4),
    _IpiaIkePropCipherKeyRounds_Type()
)
ipiaIkePropCipherKeyRounds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropCipherKeyRounds.setStatus("current")
_IpiaIkePropHashAlgorithm_Type = IkeHashAlgorithm
_IpiaIkePropHashAlgorithm_Object = MibTableColumn
ipiaIkePropHashAlgorithm = _IpiaIkePropHashAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 5),
    _IpiaIkePropHashAlgorithm_Type()
)
ipiaIkePropHashAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropHashAlgorithm.setStatus("current")


class _IpiaIkePropPrfAlgorithm_Type(Integer32):
    """Custom type ipiaIkePropPrfAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("reserved", 0)
    )


_IpiaIkePropPrfAlgorithm_Type.__name__ = "Integer32"
_IpiaIkePropPrfAlgorithm_Object = MibTableColumn
ipiaIkePropPrfAlgorithm = _IpiaIkePropPrfAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 6),
    _IpiaIkePropPrfAlgorithm_Type()
)
ipiaIkePropPrfAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropPrfAlgorithm.setStatus("current")


class _IpiaIkePropVendorId_Type(OctetString):
    """Custom type ipiaIkePropVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpiaIkePropVendorId_Type.__name__ = "OctetString"
_IpiaIkePropVendorId_Object = MibTableColumn
ipiaIkePropVendorId = _IpiaIkePropVendorId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 7),
    _IpiaIkePropVendorId_Type()
)
ipiaIkePropVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropVendorId.setStatus("current")
_IpiaIkePropDhGroup_Type = IkeGroupDescription
_IpiaIkePropDhGroup_Object = MibTableColumn
ipiaIkePropDhGroup = _IpiaIkePropDhGroup_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 8),
    _IpiaIkePropDhGroup_Type()
)
ipiaIkePropDhGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropDhGroup.setStatus("current")
_IpiaIkePropAuthenticationMethod_Type = IkeAuthMethod
_IpiaIkePropAuthenticationMethod_Object = MibTableColumn
ipiaIkePropAuthenticationMethod = _IpiaIkePropAuthenticationMethod_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 9),
    _IpiaIkePropAuthenticationMethod_Type()
)
ipiaIkePropAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropAuthenticationMethod.setStatus("current")
_IpiaIkePropMaxLifetimeSecs_Type = Unsigned32
_IpiaIkePropMaxLifetimeSecs_Object = MibTableColumn
ipiaIkePropMaxLifetimeSecs = _IpiaIkePropMaxLifetimeSecs_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 10),
    _IpiaIkePropMaxLifetimeSecs_Type()
)
ipiaIkePropMaxLifetimeSecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropMaxLifetimeSecs.setStatus("current")
_IpiaIkePropMaxLifetimeKB_Type = Unsigned32
_IpiaIkePropMaxLifetimeKB_Object = MibTableColumn
ipiaIkePropMaxLifetimeKB = _IpiaIkePropMaxLifetimeKB_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 11),
    _IpiaIkePropMaxLifetimeKB_Type()
)
ipiaIkePropMaxLifetimeKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropMaxLifetimeKB.setStatus("current")
_IpiaIkePropLastChanged_Type = TimeStamp
_IpiaIkePropLastChanged_Object = MibTableColumn
ipiaIkePropLastChanged = _IpiaIkePropLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 12),
    _IpiaIkePropLastChanged_Type()
)
ipiaIkePropLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkePropLastChanged.setStatus("current")


class _IpiaIkePropStorageType_Type(StorageType):
    """Custom type ipiaIkePropStorageType based on StorageType"""


_IpiaIkePropStorageType_Object = MibTableColumn
ipiaIkePropStorageType = _IpiaIkePropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 13),
    _IpiaIkePropStorageType_Type()
)
ipiaIkePropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropStorageType.setStatus("current")
_IpiaIkePropRowStatus_Type = RowStatus
_IpiaIkePropRowStatus_Object = MibTableColumn
ipiaIkePropRowStatus = _IpiaIkePropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 10, 1, 14),
    _IpiaIkePropRowStatus_Type()
)
ipiaIkePropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkePropRowStatus.setStatus("current")
_IpiaIpsecProposalsTable_Object = MibTable
ipiaIpsecProposalsTable = _IpiaIpsecProposalsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ipiaIpsecProposalsTable.setStatus("current")
_IpiaIpsecProposalsEntry_Object = MibTableRow
ipiaIpsecProposalsEntry = _IpiaIpsecProposalsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1)
)
ipiaIpsecProposalsEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecPropName"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecPropPriority"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecPropProtocolId"),
)
if mibBuilder.loadTexts:
    ipiaIpsecProposalsEntry.setStatus("current")


class _IpiaIpsecPropName_Type(SnmpAdminString):
    """Custom type ipiaIpsecPropName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecPropName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecPropName_Object = MibTableColumn
ipiaIpsecPropName = _IpiaIpsecPropName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 1),
    _IpiaIpsecPropName_Type()
)
ipiaIpsecPropName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecPropName.setStatus("current")


class _IpiaIpsecPropPriority_Type(Integer32):
    """Custom type ipiaIpsecPropPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpiaIpsecPropPriority_Type.__name__ = "Integer32"
_IpiaIpsecPropPriority_Object = MibTableColumn
ipiaIpsecPropPriority = _IpiaIpsecPropPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 2),
    _IpiaIpsecPropPriority_Type()
)
ipiaIpsecPropPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecPropPriority.setStatus("current")
_IpiaIpsecPropProtocolId_Type = IpsecDoiSecProtocolId
_IpiaIpsecPropProtocolId_Object = MibTableColumn
ipiaIpsecPropProtocolId = _IpiaIpsecPropProtocolId_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 3),
    _IpiaIpsecPropProtocolId_Type()
)
ipiaIpsecPropProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecPropProtocolId.setStatus("current")


class _IpiaIpsecPropTransformsName_Type(SnmpAdminString):
    """Custom type ipiaIpsecPropTransformsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecPropTransformsName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecPropTransformsName_Object = MibTableColumn
ipiaIpsecPropTransformsName = _IpiaIpsecPropTransformsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 4),
    _IpiaIpsecPropTransformsName_Type()
)
ipiaIpsecPropTransformsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecPropTransformsName.setStatus("current")
_IpiaIpsecPropLastChanged_Type = TimeStamp
_IpiaIpsecPropLastChanged_Object = MibTableColumn
ipiaIpsecPropLastChanged = _IpiaIpsecPropLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 5),
    _IpiaIpsecPropLastChanged_Type()
)
ipiaIpsecPropLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIpsecPropLastChanged.setStatus("current")


class _IpiaIpsecPropStorageType_Type(StorageType):
    """Custom type ipiaIpsecPropStorageType based on StorageType"""


_IpiaIpsecPropStorageType_Object = MibTableColumn
ipiaIpsecPropStorageType = _IpiaIpsecPropStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 6),
    _IpiaIpsecPropStorageType_Type()
)
ipiaIpsecPropStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecPropStorageType.setStatus("current")
_IpiaIpsecPropRowStatus_Type = RowStatus
_IpiaIpsecPropRowStatus_Object = MibTableColumn
ipiaIpsecPropRowStatus = _IpiaIpsecPropRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 11, 1, 7),
    _IpiaIpsecPropRowStatus_Type()
)
ipiaIpsecPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecPropRowStatus.setStatus("current")
_IpiaIpsecTransformsTable_Object = MibTable
ipiaIpsecTransformsTable = _IpiaIpsecTransformsTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12)
)
if mibBuilder.loadTexts:
    ipiaIpsecTransformsTable.setStatus("current")
_IpiaIpsecTransformsEntry_Object = MibTableRow
ipiaIpsecTransformsEntry = _IpiaIpsecTransformsEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1)
)
ipiaIpsecTransformsEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecTranType"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecTranName"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIpsecTranPriority"),
)
if mibBuilder.loadTexts:
    ipiaIpsecTransformsEntry.setStatus("current")
_IpiaIpsecTranType_Type = IpsecDoiSecProtocolId
_IpiaIpsecTranType_Object = MibTableColumn
ipiaIpsecTranType = _IpiaIpsecTranType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 1),
    _IpiaIpsecTranType_Type()
)
ipiaIpsecTranType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecTranType.setStatus("current")


class _IpiaIpsecTranName_Type(SnmpAdminString):
    """Custom type ipiaIpsecTranName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecTranName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecTranName_Object = MibTableColumn
ipiaIpsecTranName = _IpiaIpsecTranName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 2),
    _IpiaIpsecTranName_Type()
)
ipiaIpsecTranName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecTranName.setStatus("current")


class _IpiaIpsecTranPriority_Type(Integer32):
    """Custom type ipiaIpsecTranPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpiaIpsecTranPriority_Type.__name__ = "Integer32"
_IpiaIpsecTranPriority_Object = MibTableColumn
ipiaIpsecTranPriority = _IpiaIpsecTranPriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 3),
    _IpiaIpsecTranPriority_Type()
)
ipiaIpsecTranPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIpsecTranPriority.setStatus("current")


class _IpiaIpsecTranTransformName_Type(SnmpAdminString):
    """Custom type ipiaIpsecTranTransformName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIpsecTranTransformName_Type.__name__ = "SnmpAdminString"
_IpiaIpsecTranTransformName_Object = MibTableColumn
ipiaIpsecTranTransformName = _IpiaIpsecTranTransformName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 4),
    _IpiaIpsecTranTransformName_Type()
)
ipiaIpsecTranTransformName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecTranTransformName.setStatus("current")
_IpiaIpsecTranLastChanged_Type = TimeStamp
_IpiaIpsecTranLastChanged_Object = MibTableColumn
ipiaIpsecTranLastChanged = _IpiaIpsecTranLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 5),
    _IpiaIpsecTranLastChanged_Type()
)
ipiaIpsecTranLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIpsecTranLastChanged.setStatus("current")


class _IpiaIpsecTranStorageType_Type(StorageType):
    """Custom type ipiaIpsecTranStorageType based on StorageType"""


_IpiaIpsecTranStorageType_Object = MibTableColumn
ipiaIpsecTranStorageType = _IpiaIpsecTranStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 6),
    _IpiaIpsecTranStorageType_Type()
)
ipiaIpsecTranStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecTranStorageType.setStatus("current")
_IpiaIpsecTranRowStatus_Type = RowStatus
_IpiaIpsecTranRowStatus_Object = MibTableColumn
ipiaIpsecTranRowStatus = _IpiaIpsecTranRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 12, 1, 7),
    _IpiaIpsecTranRowStatus_Type()
)
ipiaIpsecTranRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIpsecTranRowStatus.setStatus("current")
_IpiaIkeIdentityTable_Object = MibTable
ipiaIkeIdentityTable = _IpiaIkeIdentityTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13)
)
if mibBuilder.loadTexts:
    ipiaIkeIdentityTable.setStatus("current")
_IpiaIkeIdentityEntry_Object = MibTableRow
ipiaIkeIdentityEntry = _IpiaIkeIdentityEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13, 1)
)
ipiaIkeIdentityEntry.setIndexNames(
    (0, "IPSEC-SPD-MIB", "spdEndGroupInterface"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActIdentityType"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaIkeActIdentityContext"),
)
if mibBuilder.loadTexts:
    ipiaIkeIdentityEntry.setStatus("current")


class _IpiaIkeIdCredentialName_Type(SnmpAdminString):
    """Custom type ipiaIkeIdCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaIkeIdCredentialName_Type.__name__ = "SnmpAdminString"
_IpiaIkeIdCredentialName_Object = MibTableColumn
ipiaIkeIdCredentialName = _IpiaIkeIdCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13, 1, 1),
    _IpiaIkeIdCredentialName_Type()
)
ipiaIkeIdCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeIdCredentialName.setStatus("current")
_IpiaIkeIdLastChanged_Type = TimeStamp
_IpiaIkeIdLastChanged_Object = MibTableColumn
ipiaIkeIdLastChanged = _IpiaIkeIdLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13, 1, 2),
    _IpiaIkeIdLastChanged_Type()
)
ipiaIkeIdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIkeIdLastChanged.setStatus("current")


class _IpiaIkeIdStorageType_Type(StorageType):
    """Custom type ipiaIkeIdStorageType based on StorageType"""


_IpiaIkeIdStorageType_Object = MibTableColumn
ipiaIkeIdStorageType = _IpiaIkeIdStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13, 1, 3),
    _IpiaIkeIdStorageType_Type()
)
ipiaIkeIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeIdStorageType.setStatus("current")
_IpiaIkeIdRowStatus_Type = RowStatus
_IpiaIkeIdRowStatus_Object = MibTableColumn
ipiaIkeIdRowStatus = _IpiaIkeIdRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 13, 1, 4),
    _IpiaIkeIdRowStatus_Type()
)
ipiaIkeIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIkeIdRowStatus.setStatus("current")
_IpiaAutostartIkeTable_Object = MibTable
ipiaAutostartIkeTable = _IpiaAutostartIkeTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14)
)
if mibBuilder.loadTexts:
    ipiaAutostartIkeTable.setStatus("current")
_IpiaAutostartIkeEntry_Object = MibTableRow
ipiaAutostartIkeEntry = _IpiaAutostartIkeEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1)
)
ipiaAutostartIkeEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaAutoIkePriority"),
)
if mibBuilder.loadTexts:
    ipiaAutostartIkeEntry.setStatus("current")


class _IpiaAutoIkePriority_Type(Integer32):
    """Custom type ipiaAutoIkePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpiaAutoIkePriority_Type.__name__ = "Integer32"
_IpiaAutoIkePriority_Object = MibTableColumn
ipiaAutoIkePriority = _IpiaAutoIkePriority_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 1),
    _IpiaAutoIkePriority_Type()
)
ipiaAutoIkePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaAutoIkePriority.setStatus("current")
_IpiaAutoIkeAction_Type = VariablePointer
_IpiaAutoIkeAction_Object = MibTableColumn
ipiaAutoIkeAction = _IpiaAutoIkeAction_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 2),
    _IpiaAutoIkeAction_Type()
)
ipiaAutoIkeAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeAction.setStatus("current")
_IpiaAutoIkeAddressType_Type = InetAddressType
_IpiaAutoIkeAddressType_Object = MibTableColumn
ipiaAutoIkeAddressType = _IpiaAutoIkeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 3),
    _IpiaAutoIkeAddressType_Type()
)
ipiaAutoIkeAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeAddressType.setStatus("current")
_IpiaAutoIkeSourceAddress_Type = InetAddress
_IpiaAutoIkeSourceAddress_Object = MibTableColumn
ipiaAutoIkeSourceAddress = _IpiaAutoIkeSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 4),
    _IpiaAutoIkeSourceAddress_Type()
)
ipiaAutoIkeSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeSourceAddress.setStatus("current")
_IpiaAutoIkeSourcePort_Type = InetPortNumber
_IpiaAutoIkeSourcePort_Object = MibTableColumn
ipiaAutoIkeSourcePort = _IpiaAutoIkeSourcePort_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 5),
    _IpiaAutoIkeSourcePort_Type()
)
ipiaAutoIkeSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeSourcePort.setStatus("current")
_IpiaAutoIkeDestAddress_Type = InetAddress
_IpiaAutoIkeDestAddress_Object = MibTableColumn
ipiaAutoIkeDestAddress = _IpiaAutoIkeDestAddress_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 6),
    _IpiaAutoIkeDestAddress_Type()
)
ipiaAutoIkeDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeDestAddress.setStatus("current")
_IpiaAutoIkeDestPort_Type = InetPortNumber
_IpiaAutoIkeDestPort_Object = MibTableColumn
ipiaAutoIkeDestPort = _IpiaAutoIkeDestPort_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 7),
    _IpiaAutoIkeDestPort_Type()
)
ipiaAutoIkeDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeDestPort.setStatus("current")


class _IpiaAutoIkeProtocol_Type(Unsigned32):
    """Custom type ipiaAutoIkeProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiaAutoIkeProtocol_Type.__name__ = "Unsigned32"
_IpiaAutoIkeProtocol_Object = MibTableColumn
ipiaAutoIkeProtocol = _IpiaAutoIkeProtocol_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 8),
    _IpiaAutoIkeProtocol_Type()
)
ipiaAutoIkeProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeProtocol.setStatus("current")
_IpiaAutoIkeLastChanged_Type = TimeStamp
_IpiaAutoIkeLastChanged_Object = MibTableColumn
ipiaAutoIkeLastChanged = _IpiaAutoIkeLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 9),
    _IpiaAutoIkeLastChanged_Type()
)
ipiaAutoIkeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaAutoIkeLastChanged.setStatus("current")


class _IpiaAutoIkeStorageType_Type(StorageType):
    """Custom type ipiaAutoIkeStorageType based on StorageType"""


_IpiaAutoIkeStorageType_Object = MibTableColumn
ipiaAutoIkeStorageType = _IpiaAutoIkeStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 10),
    _IpiaAutoIkeStorageType_Type()
)
ipiaAutoIkeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeStorageType.setStatus("current")
_IpiaAutoIkeRowStatus_Type = RowStatus
_IpiaAutoIkeRowStatus_Object = MibTableColumn
ipiaAutoIkeRowStatus = _IpiaAutoIkeRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 14, 1, 11),
    _IpiaAutoIkeRowStatus_Type()
)
ipiaAutoIkeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaAutoIkeRowStatus.setStatus("current")
_IpiaIpsecCredMngServiceTable_Object = MibTable
ipiaIpsecCredMngServiceTable = _IpiaIpsecCredMngServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15)
)
if mibBuilder.loadTexts:
    ipiaIpsecCredMngServiceTable.setStatus("current")
_IpiaIpsecCredMngServiceEntry_Object = MibTableRow
ipiaIpsecCredMngServiceEntry = _IpiaIpsecCredMngServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1)
)
ipiaIpsecCredMngServiceEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIcmsName"),
)
if mibBuilder.loadTexts:
    ipiaIpsecCredMngServiceEntry.setStatus("current")


class _IpiaIcmsName_Type(SnmpAdminString):
    """Custom type ipiaIcmsName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaIcmsName_Type.__name__ = "SnmpAdminString"
_IpiaIcmsName_Object = MibTableColumn
ipiaIcmsName = _IpiaIcmsName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 1),
    _IpiaIcmsName_Type()
)
ipiaIcmsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaIcmsName.setStatus("current")


class _IpiaIcmsDistinguishedName_Type(OctetString):
    """Custom type ipiaIcmsDistinguishedName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_IpiaIcmsDistinguishedName_Type.__name__ = "OctetString"
_IpiaIcmsDistinguishedName_Object = MibTableColumn
ipiaIcmsDistinguishedName = _IpiaIcmsDistinguishedName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 2),
    _IpiaIcmsDistinguishedName_Type()
)
ipiaIcmsDistinguishedName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsDistinguishedName.setStatus("current")


class _IpiaIcmsPolicyStatement_Type(OctetString):
    """Custom type ipiaIcmsPolicyStatement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_IpiaIcmsPolicyStatement_Type.__name__ = "OctetString"
_IpiaIcmsPolicyStatement_Object = MibTableColumn
ipiaIcmsPolicyStatement = _IpiaIcmsPolicyStatement_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 3),
    _IpiaIcmsPolicyStatement_Type()
)
ipiaIcmsPolicyStatement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsPolicyStatement.setStatus("current")


class _IpiaIcmsMaxChainLength_Type(Integer32):
    """Custom type ipiaIcmsMaxChainLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpiaIcmsMaxChainLength_Type.__name__ = "Integer32"
_IpiaIcmsMaxChainLength_Object = MibTableColumn
ipiaIcmsMaxChainLength = _IpiaIcmsMaxChainLength_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 4),
    _IpiaIcmsMaxChainLength_Type()
)
ipiaIcmsMaxChainLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsMaxChainLength.setStatus("current")


class _IpiaIcmsCredentialName_Type(SnmpAdminString):
    """Custom type ipiaIcmsCredentialName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaIcmsCredentialName_Type.__name__ = "SnmpAdminString"
_IpiaIcmsCredentialName_Object = MibTableColumn
ipiaIcmsCredentialName = _IpiaIcmsCredentialName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 5),
    _IpiaIcmsCredentialName_Type()
)
ipiaIcmsCredentialName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsCredentialName.setStatus("current")
_IpiaIcmsLastChanged_Type = TimeStamp
_IpiaIcmsLastChanged_Object = MibTableColumn
ipiaIcmsLastChanged = _IpiaIcmsLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 6),
    _IpiaIcmsLastChanged_Type()
)
ipiaIcmsLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaIcmsLastChanged.setStatus("current")


class _IpiaIcmsStorageType_Type(StorageType):
    """Custom type ipiaIcmsStorageType based on StorageType"""


_IpiaIcmsStorageType_Object = MibTableColumn
ipiaIcmsStorageType = _IpiaIcmsStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 7),
    _IpiaIcmsStorageType_Type()
)
ipiaIcmsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsStorageType.setStatus("current")
_IpiaIcmsRowStatus_Type = RowStatus
_IpiaIcmsRowStatus_Object = MibTableColumn
ipiaIcmsRowStatus = _IpiaIcmsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 15, 1, 8),
    _IpiaIcmsRowStatus_Type()
)
ipiaIcmsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaIcmsRowStatus.setStatus("current")
_IpiaCredMngCRLTable_Object = MibTable
ipiaCredMngCRLTable = _IpiaCredMngCRLTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16)
)
if mibBuilder.loadTexts:
    ipiaCredMngCRLTable.setStatus("current")
_IpiaCredMngCRLEntry_Object = MibTableRow
ipiaCredMngCRLEntry = _IpiaCredMngCRLEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1)
)
ipiaCredMngCRLEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaIcmsName"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaCmcCRLName"),
)
if mibBuilder.loadTexts:
    ipiaCredMngCRLEntry.setStatus("current")


class _IpiaCmcCRLName_Type(SnmpAdminString):
    """Custom type ipiaCmcCRLName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IpiaCmcCRLName_Type.__name__ = "SnmpAdminString"
_IpiaCmcCRLName_Object = MibTableColumn
ipiaCmcCRLName = _IpiaCmcCRLName_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 1),
    _IpiaCmcCRLName_Type()
)
ipiaCmcCRLName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaCmcCRLName.setStatus("current")


class _IpiaCmcDistributionPoint_Type(OctetString):
    """Custom type ipiaCmcDistributionPoint based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_IpiaCmcDistributionPoint_Type.__name__ = "OctetString"
_IpiaCmcDistributionPoint_Object = MibTableColumn
ipiaCmcDistributionPoint = _IpiaCmcDistributionPoint_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 2),
    _IpiaCmcDistributionPoint_Type()
)
ipiaCmcDistributionPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCmcDistributionPoint.setStatus("current")


class _IpiaCmcThisUpdate_Type(OctetString):
    """Custom type ipiaCmcThisUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaCmcThisUpdate_Type.__name__ = "OctetString"
_IpiaCmcThisUpdate_Object = MibTableColumn
ipiaCmcThisUpdate = _IpiaCmcThisUpdate_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 3),
    _IpiaCmcThisUpdate_Type()
)
ipiaCmcThisUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCmcThisUpdate.setStatus("current")


class _IpiaCmcNextUpdate_Type(OctetString):
    """Custom type ipiaCmcNextUpdate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaCmcNextUpdate_Type.__name__ = "OctetString"
_IpiaCmcNextUpdate_Object = MibTableColumn
ipiaCmcNextUpdate = _IpiaCmcNextUpdate_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 4),
    _IpiaCmcNextUpdate_Type()
)
ipiaCmcNextUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCmcNextUpdate.setStatus("current")
_IpiaCmcLastChanged_Type = TimeStamp
_IpiaCmcLastChanged_Object = MibTableColumn
ipiaCmcLastChanged = _IpiaCmcLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 5),
    _IpiaCmcLastChanged_Type()
)
ipiaCmcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaCmcLastChanged.setStatus("current")


class _IpiaCmcStorageType_Type(StorageType):
    """Custom type ipiaCmcStorageType based on StorageType"""


_IpiaCmcStorageType_Object = MibTableColumn
ipiaCmcStorageType = _IpiaCmcStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 6),
    _IpiaCmcStorageType_Type()
)
ipiaCmcStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCmcStorageType.setStatus("current")
_IpiaCmcRowStatus_Type = RowStatus
_IpiaCmcRowStatus_Object = MibTableColumn
ipiaCmcRowStatus = _IpiaCmcRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 16, 1, 7),
    _IpiaCmcRowStatus_Type()
)
ipiaCmcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaCmcRowStatus.setStatus("current")
_IpiaRevokedCertificateTable_Object = MibTable
ipiaRevokedCertificateTable = _IpiaRevokedCertificateTable_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17)
)
if mibBuilder.loadTexts:
    ipiaRevokedCertificateTable.setStatus("current")
_IpiaRevokedCertificateEntry_Object = MibTableRow
ipiaRevokedCertificateEntry = _IpiaRevokedCertificateEntry_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1)
)
ipiaRevokedCertificateEntry.setIndexNames(
    (0, "IPSEC-IKEACTION-MIB", "ipiaCmcCRLName"),
    (0, "IPSEC-IKEACTION-MIB", "ipiaRctCertSerialNumber"),
)
if mibBuilder.loadTexts:
    ipiaRevokedCertificateEntry.setStatus("current")


class _IpiaRctCertSerialNumber_Type(Unsigned32):
    """Custom type ipiaRctCertSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IpiaRctCertSerialNumber_Type.__name__ = "Unsigned32"
_IpiaRctCertSerialNumber_Object = MibTableColumn
ipiaRctCertSerialNumber = _IpiaRctCertSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 1),
    _IpiaRctCertSerialNumber_Type()
)
ipiaRctCertSerialNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipiaRctCertSerialNumber.setStatus("current")


class _IpiaRctRevokedDate_Type(OctetString):
    """Custom type ipiaRctRevokedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpiaRctRevokedDate_Type.__name__ = "OctetString"
_IpiaRctRevokedDate_Object = MibTableColumn
ipiaRctRevokedDate = _IpiaRctRevokedDate_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 2),
    _IpiaRctRevokedDate_Type()
)
ipiaRctRevokedDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaRctRevokedDate.setStatus("current")


class _IpiaRctRevokedReason_Type(Integer32):
    """Custom type ipiaRctRevokedReason based on Integer32"""
    defaultValue = 1

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
        *(("affiliationChanged", 4),
          ("cACompromise", 3),
          ("certificateHold", 7),
          ("cessationOfOperation", 6),
          ("keyCompromise", 2),
          ("removeFromCRL", 8),
          ("superseded", 5),
          ("unspecified", 1))
    )


_IpiaRctRevokedReason_Type.__name__ = "Integer32"
_IpiaRctRevokedReason_Object = MibTableColumn
ipiaRctRevokedReason = _IpiaRctRevokedReason_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 3),
    _IpiaRctRevokedReason_Type()
)
ipiaRctRevokedReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaRctRevokedReason.setStatus("current")
_IpiaRctLastChanged_Type = TimeStamp
_IpiaRctLastChanged_Object = MibTableColumn
ipiaRctLastChanged = _IpiaRctLastChanged_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 4),
    _IpiaRctLastChanged_Type()
)
ipiaRctLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipiaRctLastChanged.setStatus("current")


class _IpiaRctStorageType_Type(StorageType):
    """Custom type ipiaRctStorageType based on StorageType"""


_IpiaRctStorageType_Object = MibTableColumn
ipiaRctStorageType = _IpiaRctStorageType_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 5),
    _IpiaRctStorageType_Type()
)
ipiaRctStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaRctStorageType.setStatus("current")
_IpiaRctRowStatus_Type = RowStatus
_IpiaRctRowStatus_Object = MibTableColumn
ipiaRctRowStatus = _IpiaRctRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 1, 17, 1, 6),
    _IpiaRctRowStatus_Type()
)
ipiaRctRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipiaRctRowStatus.setStatus("current")
_IpiaNotificationObjects_ObjectIdentity = ObjectIdentity
ipiaNotificationObjects = _IpiaNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 2)
)
_IpiaNotifications_ObjectIdentity = ObjectIdentity
ipiaNotifications = _IpiaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 2, 0)
)
_IpiaNotificationVariables_ObjectIdentity = ObjectIdentity
ipiaNotificationVariables = _IpiaNotificationVariables_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 2, 1)
)
_IpiaConformanceObjects_ObjectIdentity = ObjectIdentity
ipiaConformanceObjects = _IpiaConformanceObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3)
)
_IpiaCompliances_ObjectIdentity = ObjectIdentity
ipiaCompliances = _IpiaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 1)
)
_IpiaGroups_ObjectIdentity = ObjectIdentity
ipiaGroups = _IpiaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2)
)

# Managed Objects groups

ipiaStaticFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 1)
)
ipiaStaticFilterGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaIkePhase1Filter"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePhase2Filter"))
)
if mibBuilder.loadTexts:
    ipiaStaticFilterGroup.setStatus("current")

ipiaCredentialFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 2)
)
ipiaCredentialFilterGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaCredFiltCredentialType"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltMatchFieldName"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltMatchFieldValue"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltAcceptCredFrom"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaCredFiltRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcDistributionPoint"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcThisUpdate"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcNextUpdate"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRevokedDate"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRevokedReason"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsDistinguishedName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsPolicyStatement"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsMaxChainLength"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsCredentialName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsRowStatus"))
)
if mibBuilder.loadTexts:
    ipiaCredentialFilterGroup.setStatus("current")

ipiaPeerIdFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 3)
)
ipiaPeerIdFilterGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltIdentityType"),
        ("IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltIdentityValue"),
        ("IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaPeerIdFiltRowStatus"))
)
if mibBuilder.loadTexts:
    ipiaPeerIdFilterGroup.setStatus("current")

ipiaStaticActionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 4)
)
ipiaStaticActionGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaRejectIKEAction"),
        ("IPSEC-IKEACTION-MIB", "ipiaRejectIKEActionLog"))
)
if mibBuilder.loadTexts:
    ipiaStaticActionGroup.setStatus("current")

ipiaIkeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 5)
)
ipiaIkeGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaIkeActParametersName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActThresholdDerivedKeys"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActExchangeMode"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActAgressiveModeGroupId"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActIdentityType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActIdentityContext"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActPeerName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActVendorId"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActPropName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActDoActionLogging"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActDoPacketLogging"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActPropLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActPropStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeActPropRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropLifetimeDerivedKeys"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropCipherAlgorithm"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropCipherKeyLength"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropCipherKeyRounds"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropHashAlgorithm"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropPrfAlgorithm"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropVendorId"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropDhGroup"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropAuthenticationMethod"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropMaxLifetimeSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropMaxLifetimeKB"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkePropRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamMinLifetimeSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamMinLifetimeKB"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRefreshThreshSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRefreshThresholdKB"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamIdleDurationSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeIdCredentialName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeIdLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeIdStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIkeIdRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeAction"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeAddressType"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeSourceAddress"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeSourcePort"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeDestAddress"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeDestPort"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeProtocol"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaAutoIkeRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcDistributionPoint"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcThisUpdate"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcNextUpdate"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaCmcRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRevokedDate"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRevokedReason"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaRctRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsDistinguishedName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsPolicyStatement"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsMaxChainLength"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsCredentialName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIcmsRowStatus"))
)
if mibBuilder.loadTexts:
    ipiaIkeGroup.setStatus("current")

ipiaIpsecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 2, 6)
)
ipiaIpsecGroup.setObjects(
      *(("IPSEC-IKEACTION-MIB", "ipiaIpsecActParametersName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActProposalsName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActUsePfs"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActVendorId"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActGroupId"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActPeerGatewayIdName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActUseIkeGroup"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActGranularity"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActMode"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActDFHandling"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActDoActionLogging"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActDoPacketLogging"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecActRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecPropTransformsName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecPropLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecPropStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecPropRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecTranTransformName"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecTranLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecTranStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaIpsecTranRowStatus"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamMinLifetimeSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamMinLifetimeKB"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRefreshThreshSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRefreshThresholdKB"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamIdleDurationSecs"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamLastChanged"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamStorageType"),
        ("IPSEC-IKEACTION-MIB", "ipiaSaNegParamRowStatus"))
)
if mibBuilder.loadTexts:
    ipiaIpsecGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipiaIKECompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipiaIKECompliance.setStatus(
        "current"
    )

ipiaRuleFilterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 153, 4, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ipiaRuleFilterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPSEC-IKEACTION-MIB",
    **{"IkeEncryptionAlgorithm": IkeEncryptionAlgorithm,
       "IkeAuthMethod": IkeAuthMethod,
       "IkeHashAlgorithm": IkeHashAlgorithm,
       "IkeGroupDescription": IkeGroupDescription,
       "IpsecDoiSecProtocolId": IpsecDoiSecProtocolId,
       "ipiaMIB": ipiaMIB,
       "ipiaConfigObjects": ipiaConfigObjects,
       "ipiaLocalConfigObjects": ipiaLocalConfigObjects,
       "ipiaStaticFilters": ipiaStaticFilters,
       "ipiaIkePhase1Filter": ipiaIkePhase1Filter,
       "ipiaIkePhase2Filter": ipiaIkePhase2Filter,
       "ipiaCredentialFilterTable": ipiaCredentialFilterTable,
       "ipiaCredentialFilterEntry": ipiaCredentialFilterEntry,
       "ipiaCredFiltName": ipiaCredFiltName,
       "ipiaCredFiltCredentialType": ipiaCredFiltCredentialType,
       "ipiaCredFiltMatchFieldName": ipiaCredFiltMatchFieldName,
       "ipiaCredFiltMatchFieldValue": ipiaCredFiltMatchFieldValue,
       "ipiaCredFiltAcceptCredFrom": ipiaCredFiltAcceptCredFrom,
       "ipiaCredFiltLastChanged": ipiaCredFiltLastChanged,
       "ipiaCredFiltStorageType": ipiaCredFiltStorageType,
       "ipiaCredFiltRowStatus": ipiaCredFiltRowStatus,
       "ipiaPeerIdentityFilterTable": ipiaPeerIdentityFilterTable,
       "ipiaPeerIdentityFilterEntry": ipiaPeerIdentityFilterEntry,
       "ipiaPeerIdFiltName": ipiaPeerIdFiltName,
       "ipiaPeerIdFiltIdentityType": ipiaPeerIdFiltIdentityType,
       "ipiaPeerIdFiltIdentityValue": ipiaPeerIdFiltIdentityValue,
       "ipiaPeerIdFiltLastChanged": ipiaPeerIdFiltLastChanged,
       "ipiaPeerIdFiltStorageType": ipiaPeerIdFiltStorageType,
       "ipiaPeerIdFiltRowStatus": ipiaPeerIdFiltRowStatus,
       "ipiaStaticActions": ipiaStaticActions,
       "ipiaRejectIKEAction": ipiaRejectIKEAction,
       "ipiaRejectIKEActionLog": ipiaRejectIKEActionLog,
       "ipiaIkeActionTable": ipiaIkeActionTable,
       "ipiaIkeActionEntry": ipiaIkeActionEntry,
       "ipiaIkeActName": ipiaIkeActName,
       "ipiaIkeActParametersName": ipiaIkeActParametersName,
       "ipiaIkeActThresholdDerivedKeys": ipiaIkeActThresholdDerivedKeys,
       "ipiaIkeActExchangeMode": ipiaIkeActExchangeMode,
       "ipiaIkeActAgressiveModeGroupId": ipiaIkeActAgressiveModeGroupId,
       "ipiaIkeActIdentityType": ipiaIkeActIdentityType,
       "ipiaIkeActIdentityContext": ipiaIkeActIdentityContext,
       "ipiaIkeActPeerName": ipiaIkeActPeerName,
       "ipiaIkeActDoActionLogging": ipiaIkeActDoActionLogging,
       "ipiaIkeActDoPacketLogging": ipiaIkeActDoPacketLogging,
       "ipiaIkeActVendorId": ipiaIkeActVendorId,
       "ipiaIkeActLastChanged": ipiaIkeActLastChanged,
       "ipiaIkeActStorageType": ipiaIkeActStorageType,
       "ipiaIkeActRowStatus": ipiaIkeActRowStatus,
       "ipiaIpsecActionTable": ipiaIpsecActionTable,
       "ipiaIpsecActionEntry": ipiaIpsecActionEntry,
       "ipiaIpsecActName": ipiaIpsecActName,
       "ipiaIpsecActParametersName": ipiaIpsecActParametersName,
       "ipiaIpsecActProposalsName": ipiaIpsecActProposalsName,
       "ipiaIpsecActUsePfs": ipiaIpsecActUsePfs,
       "ipiaIpsecActVendorId": ipiaIpsecActVendorId,
       "ipiaIpsecActGroupId": ipiaIpsecActGroupId,
       "ipiaIpsecActPeerGatewayIdName": ipiaIpsecActPeerGatewayIdName,
       "ipiaIpsecActUseIkeGroup": ipiaIpsecActUseIkeGroup,
       "ipiaIpsecActGranularity": ipiaIpsecActGranularity,
       "ipiaIpsecActMode": ipiaIpsecActMode,
       "ipiaIpsecActDFHandling": ipiaIpsecActDFHandling,
       "ipiaIpsecActDoActionLogging": ipiaIpsecActDoActionLogging,
       "ipiaIpsecActDoPacketLogging": ipiaIpsecActDoPacketLogging,
       "ipiaIpsecActLastChanged": ipiaIpsecActLastChanged,
       "ipiaIpsecActStorageType": ipiaIpsecActStorageType,
       "ipiaIpsecActRowStatus": ipiaIpsecActRowStatus,
       "ipiaSaNegotiationParametersTable": ipiaSaNegotiationParametersTable,
       "ipiaSaNegotiationParametersEntry": ipiaSaNegotiationParametersEntry,
       "ipiaSaNegParamName": ipiaSaNegParamName,
       "ipiaSaNegParamMinLifetimeSecs": ipiaSaNegParamMinLifetimeSecs,
       "ipiaSaNegParamMinLifetimeKB": ipiaSaNegParamMinLifetimeKB,
       "ipiaSaNegParamRefreshThreshSecs": ipiaSaNegParamRefreshThreshSecs,
       "ipiaSaNegParamRefreshThresholdKB": ipiaSaNegParamRefreshThresholdKB,
       "ipiaSaNegParamIdleDurationSecs": ipiaSaNegParamIdleDurationSecs,
       "ipiaSaNegParamLastChanged": ipiaSaNegParamLastChanged,
       "ipiaSaNegParamStorageType": ipiaSaNegParamStorageType,
       "ipiaSaNegParamRowStatus": ipiaSaNegParamRowStatus,
       "ipiaIkeActionProposalsTable": ipiaIkeActionProposalsTable,
       "ipiaIkeActionProposalsEntry": ipiaIkeActionProposalsEntry,
       "ipiaIkeActPropPriority": ipiaIkeActPropPriority,
       "ipiaIkeActPropName": ipiaIkeActPropName,
       "ipiaIkeActPropLastChanged": ipiaIkeActPropLastChanged,
       "ipiaIkeActPropStorageType": ipiaIkeActPropStorageType,
       "ipiaIkeActPropRowStatus": ipiaIkeActPropRowStatus,
       "ipiaIkeProposalTable": ipiaIkeProposalTable,
       "ipiaIkeProposalEntry": ipiaIkeProposalEntry,
       "ipiaIkePropLifetimeDerivedKeys": ipiaIkePropLifetimeDerivedKeys,
       "ipiaIkePropCipherAlgorithm": ipiaIkePropCipherAlgorithm,
       "ipiaIkePropCipherKeyLength": ipiaIkePropCipherKeyLength,
       "ipiaIkePropCipherKeyRounds": ipiaIkePropCipherKeyRounds,
       "ipiaIkePropHashAlgorithm": ipiaIkePropHashAlgorithm,
       "ipiaIkePropPrfAlgorithm": ipiaIkePropPrfAlgorithm,
       "ipiaIkePropVendorId": ipiaIkePropVendorId,
       "ipiaIkePropDhGroup": ipiaIkePropDhGroup,
       "ipiaIkePropAuthenticationMethod": ipiaIkePropAuthenticationMethod,
       "ipiaIkePropMaxLifetimeSecs": ipiaIkePropMaxLifetimeSecs,
       "ipiaIkePropMaxLifetimeKB": ipiaIkePropMaxLifetimeKB,
       "ipiaIkePropLastChanged": ipiaIkePropLastChanged,
       "ipiaIkePropStorageType": ipiaIkePropStorageType,
       "ipiaIkePropRowStatus": ipiaIkePropRowStatus,
       "ipiaIpsecProposalsTable": ipiaIpsecProposalsTable,
       "ipiaIpsecProposalsEntry": ipiaIpsecProposalsEntry,
       "ipiaIpsecPropName": ipiaIpsecPropName,
       "ipiaIpsecPropPriority": ipiaIpsecPropPriority,
       "ipiaIpsecPropProtocolId": ipiaIpsecPropProtocolId,
       "ipiaIpsecPropTransformsName": ipiaIpsecPropTransformsName,
       "ipiaIpsecPropLastChanged": ipiaIpsecPropLastChanged,
       "ipiaIpsecPropStorageType": ipiaIpsecPropStorageType,
       "ipiaIpsecPropRowStatus": ipiaIpsecPropRowStatus,
       "ipiaIpsecTransformsTable": ipiaIpsecTransformsTable,
       "ipiaIpsecTransformsEntry": ipiaIpsecTransformsEntry,
       "ipiaIpsecTranType": ipiaIpsecTranType,
       "ipiaIpsecTranName": ipiaIpsecTranName,
       "ipiaIpsecTranPriority": ipiaIpsecTranPriority,
       "ipiaIpsecTranTransformName": ipiaIpsecTranTransformName,
       "ipiaIpsecTranLastChanged": ipiaIpsecTranLastChanged,
       "ipiaIpsecTranStorageType": ipiaIpsecTranStorageType,
       "ipiaIpsecTranRowStatus": ipiaIpsecTranRowStatus,
       "ipiaIkeIdentityTable": ipiaIkeIdentityTable,
       "ipiaIkeIdentityEntry": ipiaIkeIdentityEntry,
       "ipiaIkeIdCredentialName": ipiaIkeIdCredentialName,
       "ipiaIkeIdLastChanged": ipiaIkeIdLastChanged,
       "ipiaIkeIdStorageType": ipiaIkeIdStorageType,
       "ipiaIkeIdRowStatus": ipiaIkeIdRowStatus,
       "ipiaAutostartIkeTable": ipiaAutostartIkeTable,
       "ipiaAutostartIkeEntry": ipiaAutostartIkeEntry,
       "ipiaAutoIkePriority": ipiaAutoIkePriority,
       "ipiaAutoIkeAction": ipiaAutoIkeAction,
       "ipiaAutoIkeAddressType": ipiaAutoIkeAddressType,
       "ipiaAutoIkeSourceAddress": ipiaAutoIkeSourceAddress,
       "ipiaAutoIkeSourcePort": ipiaAutoIkeSourcePort,
       "ipiaAutoIkeDestAddress": ipiaAutoIkeDestAddress,
       "ipiaAutoIkeDestPort": ipiaAutoIkeDestPort,
       "ipiaAutoIkeProtocol": ipiaAutoIkeProtocol,
       "ipiaAutoIkeLastChanged": ipiaAutoIkeLastChanged,
       "ipiaAutoIkeStorageType": ipiaAutoIkeStorageType,
       "ipiaAutoIkeRowStatus": ipiaAutoIkeRowStatus,
       "ipiaIpsecCredMngServiceTable": ipiaIpsecCredMngServiceTable,
       "ipiaIpsecCredMngServiceEntry": ipiaIpsecCredMngServiceEntry,
       "ipiaIcmsName": ipiaIcmsName,
       "ipiaIcmsDistinguishedName": ipiaIcmsDistinguishedName,
       "ipiaIcmsPolicyStatement": ipiaIcmsPolicyStatement,
       "ipiaIcmsMaxChainLength": ipiaIcmsMaxChainLength,
       "ipiaIcmsCredentialName": ipiaIcmsCredentialName,
       "ipiaIcmsLastChanged": ipiaIcmsLastChanged,
       "ipiaIcmsStorageType": ipiaIcmsStorageType,
       "ipiaIcmsRowStatus": ipiaIcmsRowStatus,
       "ipiaCredMngCRLTable": ipiaCredMngCRLTable,
       "ipiaCredMngCRLEntry": ipiaCredMngCRLEntry,
       "ipiaCmcCRLName": ipiaCmcCRLName,
       "ipiaCmcDistributionPoint": ipiaCmcDistributionPoint,
       "ipiaCmcThisUpdate": ipiaCmcThisUpdate,
       "ipiaCmcNextUpdate": ipiaCmcNextUpdate,
       "ipiaCmcLastChanged": ipiaCmcLastChanged,
       "ipiaCmcStorageType": ipiaCmcStorageType,
       "ipiaCmcRowStatus": ipiaCmcRowStatus,
       "ipiaRevokedCertificateTable": ipiaRevokedCertificateTable,
       "ipiaRevokedCertificateEntry": ipiaRevokedCertificateEntry,
       "ipiaRctCertSerialNumber": ipiaRctCertSerialNumber,
       "ipiaRctRevokedDate": ipiaRctRevokedDate,
       "ipiaRctRevokedReason": ipiaRctRevokedReason,
       "ipiaRctLastChanged": ipiaRctLastChanged,
       "ipiaRctStorageType": ipiaRctStorageType,
       "ipiaRctRowStatus": ipiaRctRowStatus,
       "ipiaNotificationObjects": ipiaNotificationObjects,
       "ipiaNotifications": ipiaNotifications,
       "ipiaNotificationVariables": ipiaNotificationVariables,
       "ipiaConformanceObjects": ipiaConformanceObjects,
       "ipiaCompliances": ipiaCompliances,
       "ipiaIKECompliance": ipiaIKECompliance,
       "ipiaRuleFilterCompliance": ipiaRuleFilterCompliance,
       "ipiaGroups": ipiaGroups,
       "ipiaStaticFilterGroup": ipiaStaticFilterGroup,
       "ipiaCredentialFilterGroup": ipiaCredentialFilterGroup,
       "ipiaPeerIdFilterGroup": ipiaPeerIdFilterGroup,
       "ipiaStaticActionGroup": ipiaStaticActionGroup,
       "ipiaIkeGroup": ipiaIkeGroup,
       "ipiaIpsecGroup": ipiaIpsecGroup}
)
