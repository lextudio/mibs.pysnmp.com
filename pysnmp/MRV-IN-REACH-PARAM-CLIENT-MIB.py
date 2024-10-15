# SNMP MIB module (MRV-IN-REACH-PARAM-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-PARAM-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:44 2024
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

(AddressType,
 DateTime,
 mrvInReachProductDivision) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "AddressType",
    "DateTime",
    "mrvInReachProductDivision")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XParamClient_ObjectIdentity = ObjectIdentity
xParamClient = _XParamClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 7)
)
_ParamClientLoaderName_Type = DisplayString
_ParamClientLoaderName_Object = MibScalar
paramClientLoaderName = _ParamClientLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 1),
    _ParamClientLoaderName_Type()
)
paramClientLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderName.setStatus("mandatory")
_ParamClientLoaderAddressType_Type = AddressType
_ParamClientLoaderAddressType_Object = MibScalar
paramClientLoaderAddressType = _ParamClientLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 2),
    _ParamClientLoaderAddressType_Type()
)
paramClientLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderAddressType.setStatus("mandatory")
_ParamClientLoaderAddress_Type = OctetString
_ParamClientLoaderAddress_Object = MibScalar
paramClientLoaderAddress = _ParamClientLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 3),
    _ParamClientLoaderAddress_Type()
)
paramClientLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderAddress.setStatus("mandatory")
_ParamClientParameterVersion_Type = Integer32
_ParamClientParameterVersion_Object = MibScalar
paramClientParameterVersion = _ParamClientParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 4),
    _ParamClientParameterVersion_Type()
)
paramClientParameterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientParameterVersion.setStatus("mandatory")
_ParamClientUpdateTime_Type = DateTime
_ParamClientUpdateTime_Object = MibScalar
paramClientUpdateTime = _ParamClientUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 5),
    _ParamClientUpdateTime_Type()
)
paramClientUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientUpdateTime.setStatus("mandatory")


class _ParamClientServerCheck_Type(Integer32):
    """Custom type paramClientServerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamClientServerCheck_Type.__name__ = "Integer32"
_ParamClientServerCheck_Object = MibScalar
paramClientServerCheck = _ParamClientServerCheck_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 6),
    _ParamClientServerCheck_Type()
)
paramClientServerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientServerCheck.setStatus("mandatory")


class _ParamClientCheckInterval_Type(Integer32):
    """Custom type paramClientCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_ParamClientCheckInterval_Type.__name__ = "Integer32"
_ParamClientCheckInterval_Object = MibScalar
paramClientCheckInterval = _ParamClientCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 7),
    _ParamClientCheckInterval_Type()
)
paramClientCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientCheckInterval.setStatus("mandatory")


class _ParamClientCheckNow_Type(Integer32):
    """Custom type paramClientCheckNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_ParamClientCheckNow_Type.__name__ = "Integer32"
_ParamClientCheckNow_Object = MibScalar
paramClientCheckNow = _ParamClientCheckNow_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 8),
    _ParamClientCheckNow_Type()
)
paramClientCheckNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientCheckNow.setStatus("mandatory")


class _ParamClientServerLimit_Type(Integer32):
    """Custom type paramClientServerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ParamClientServerLimit_Type.__name__ = "Integer32"
_ParamClientServerLimit_Object = MibScalar
paramClientServerLimit = _ParamClientServerLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 9),
    _ParamClientServerLimit_Type()
)
paramClientServerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientServerLimit.setStatus("mandatory")


class _ParamClientRetransmitInterval_Type(Integer32):
    """Custom type paramClientRetransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ParamClientRetransmitInterval_Type.__name__ = "Integer32"
_ParamClientRetransmitInterval_Object = MibScalar
paramClientRetransmitInterval = _ParamClientRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 10),
    _ParamClientRetransmitInterval_Type()
)
paramClientRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientRetransmitInterval.setStatus("mandatory")


class _ParamClientRetransmitLimit_Type(Integer32):
    """Custom type paramClientRetransmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ParamClientRetransmitLimit_Type.__name__ = "Integer32"
_ParamClientRetransmitLimit_Object = MibScalar
paramClientRetransmitLimit = _ParamClientRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 11),
    _ParamClientRetransmitLimit_Type()
)
paramClientRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientRetransmitLimit.setStatus("mandatory")


class _ParamClientState_Type(Integer32):
    """Custom type paramClientState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("hold", 11),
          ("idle", 2),
          ("internal1", 3),
          ("internal2", 4),
          ("internal3", 5),
          ("internal4", 6),
          ("internal5", 7),
          ("internal6", 8),
          ("internal7", 9),
          ("internal8", 10),
          ("other", 1),
          ("retry", 12))
    )


_ParamClientState_Type.__name__ = "Integer32"
_ParamClientState_Object = MibScalar
paramClientState = _ParamClientState_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 12),
    _ParamClientState_Type()
)
paramClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientState.setStatus("mandatory")
_ParamClientProtocolErrors_Type = Counter32
_ParamClientProtocolErrors_Object = MibScalar
paramClientProtocolErrors = _ParamClientProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 13),
    _ParamClientProtocolErrors_Type()
)
paramClientProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientProtocolErrors.setStatus("mandatory")
_ParamClientServerRejects_Type = Counter32
_ParamClientServerRejects_Object = MibScalar
paramClientServerRejects = _ParamClientServerRejects_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 14),
    _ParamClientServerRejects_Type()
)
paramClientServerRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientServerRejects.setStatus("mandatory")
_ParamClientServerNumber_Type = Integer32
_ParamClientServerNumber_Object = MibScalar
paramClientServerNumber = _ParamClientServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 15),
    _ParamClientServerNumber_Type()
)
paramClientServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientServerNumber.setStatus("mandatory")
_ParamServerTable_Object = MibTable
paramServerTable = _ParamServerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16)
)
if mibBuilder.loadTexts:
    paramServerTable.setStatus("mandatory")
_ParamServerEntry_Object = MibTableRow
paramServerEntry = _ParamServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1)
)
paramServerEntry.setIndexNames(
    (0, "MRV-IN-REACH-PARAM-CLIENT-MIB", "paramServerName"),
)
if mibBuilder.loadTexts:
    paramServerEntry.setStatus("mandatory")


class _ParamServerName_Type(DisplayString):
    """Custom type paramServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ParamServerName_Type.__name__ = "DisplayString"
_ParamServerName_Object = MibTableColumn
paramServerName = _ParamServerName_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 1),
    _ParamServerName_Type()
)
paramServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerName.setStatus("mandatory")


class _ParamServerEntryStatus_Type(Integer32):
    """Custom type paramServerEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ParamServerEntryStatus_Type.__name__ = "Integer32"
_ParamServerEntryStatus_Object = MibTableColumn
paramServerEntryStatus = _ParamServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 2),
    _ParamServerEntryStatus_Type()
)
paramServerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerEntryStatus.setStatus("mandatory")


class _ParamServerAddressType_Type(AddressType):
    """Custom type paramServerAddressType based on AddressType"""


_ParamServerAddressType_Object = MibTableColumn
paramServerAddressType = _ParamServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 3),
    _ParamServerAddressType_Type()
)
paramServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerAddressType.setStatus("mandatory")
_ParamServerAddress_Type = OctetString
_ParamServerAddress_Object = MibTableColumn
paramServerAddress = _ParamServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 4),
    _ParamServerAddress_Type()
)
paramServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerAddress.setStatus("mandatory")


class _ParamServerStoredVersion_Type(Integer32):
    """Custom type paramServerStoredVersion based on Integer32"""
    defaultValue = 0


_ParamServerStoredVersion_Object = MibTableColumn
paramServerStoredVersion = _ParamServerStoredVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 5),
    _ParamServerStoredVersion_Type()
)
paramServerStoredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredVersion.setStatus("mandatory")


class _ParamServerStoredTime_Type(DateTime):
    """Custom type paramServerStoredTime based on DateTime"""
    defaultHexValue = "00"


_ParamServerStoredTime_Object = MibTableColumn
paramServerStoredTime = _ParamServerStoredTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 6),
    _ParamServerStoredTime_Type()
)
paramServerStoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredTime.setStatus("mandatory")


class _ParamServerStoredStatus_Type(Integer32):
    """Custom type paramServerStoredStatus based on Integer32"""
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
        *(("ahead", 3),
          ("behind", 4),
          ("current", 2),
          ("failed", 6),
          ("failing", 5),
          ("noMemCard", 8),
          ("query", 7),
          ("unknown", 1))
    )


_ParamServerStoredStatus_Type.__name__ = "Integer32"
_ParamServerStoredStatus_Object = MibTableColumn
paramServerStoredStatus = _ParamServerStoredStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 7),
    _ParamServerStoredStatus_Type()
)
paramServerStoredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredStatus.setStatus("mandatory")


class _ParamServerStoredFailure_Type(Integer32):
    """Custom type paramServerStoredFailure based on Integer32"""
    defaultValue = 2

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("close", 10),
          ("delete", 11),
          ("fileData", 13),
          ("none", 2),
          ("open", 4),
          ("other", 1),
          ("protocolIn", 8),
          ("protocolOut", 3),
          ("read", 5),
          ("rename", 12),
          ("resource", 7),
          ("response", 9),
          ("write", 6))
    )


_ParamServerStoredFailure_Type.__name__ = "Integer32"
_ParamServerStoredFailure_Object = MibTableColumn
paramServerStoredFailure = _ParamServerStoredFailure_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 8),
    _ParamServerStoredFailure_Type()
)
paramServerStoredFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredFailure.setStatus("mandatory")


class _ParamClientPath_Type(DisplayString):
    """Custom type paramClientPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ParamClientPath_Type.__name__ = "DisplayString"
_ParamClientPath_Object = MibScalar
paramClientPath = _ParamClientPath_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 17),
    _ParamClientPath_Type()
)
paramClientPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientPath.setStatus("mandatory")


class _ParamClientChassisStorageState_Type(Integer32):
    """Custom type paramClientChassisStorageState based on Integer32"""
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
        *(("behind", 8),
          ("busBusy", 5),
          ("current", 3),
          ("failing", 7),
          ("notApplicable", 1),
          ("retrying", 6),
          ("unknown", 2),
          ("verifying", 4))
    )


_ParamClientChassisStorageState_Type.__name__ = "Integer32"
_ParamClientChassisStorageState_Object = MibScalar
paramClientChassisStorageState = _ParamClientChassisStorageState_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 18),
    _ParamClientChassisStorageState_Type()
)
paramClientChassisStorageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientChassisStorageState.setStatus("mandatory")


class _ParamClientTftpBroadcast_Type(Integer32):
    """Custom type paramClientTftpBroadcast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamClientTftpBroadcast_Type.__name__ = "Integer32"
_ParamClientTftpBroadcast_Object = MibScalar
paramClientTftpBroadcast = _ParamClientTftpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 20),
    _ParamClientTftpBroadcast_Type()
)
paramClientTftpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientTftpBroadcast.setStatus("mandatory")


class _ParamClientWriteNow_Type(Integer32):
    """Custom type paramClientWriteNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_ParamClientWriteNow_Type.__name__ = "Integer32"
_ParamClientWriteNow_Object = MibScalar
paramClientWriteNow = _ParamClientWriteNow_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 21),
    _ParamClientWriteNow_Type()
)
paramClientWriteNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientWriteNow.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-PARAM-CLIENT-MIB",
    **{"xParamClient": xParamClient,
       "paramClientLoaderName": paramClientLoaderName,
       "paramClientLoaderAddressType": paramClientLoaderAddressType,
       "paramClientLoaderAddress": paramClientLoaderAddress,
       "paramClientParameterVersion": paramClientParameterVersion,
       "paramClientUpdateTime": paramClientUpdateTime,
       "paramClientServerCheck": paramClientServerCheck,
       "paramClientCheckInterval": paramClientCheckInterval,
       "paramClientCheckNow": paramClientCheckNow,
       "paramClientServerLimit": paramClientServerLimit,
       "paramClientRetransmitInterval": paramClientRetransmitInterval,
       "paramClientRetransmitLimit": paramClientRetransmitLimit,
       "paramClientState": paramClientState,
       "paramClientProtocolErrors": paramClientProtocolErrors,
       "paramClientServerRejects": paramClientServerRejects,
       "paramClientServerNumber": paramClientServerNumber,
       "paramServerTable": paramServerTable,
       "paramServerEntry": paramServerEntry,
       "paramServerName": paramServerName,
       "paramServerEntryStatus": paramServerEntryStatus,
       "paramServerAddressType": paramServerAddressType,
       "paramServerAddress": paramServerAddress,
       "paramServerStoredVersion": paramServerStoredVersion,
       "paramServerStoredTime": paramServerStoredTime,
       "paramServerStoredStatus": paramServerStoredStatus,
       "paramServerStoredFailure": paramServerStoredFailure,
       "paramClientPath": paramClientPath,
       "paramClientChassisStorageState": paramClientChassisStorageState,
       "paramClientTftpBroadcast": paramClientTftpBroadcast,
       "paramClientWriteNow": paramClientWriteNow}
)
