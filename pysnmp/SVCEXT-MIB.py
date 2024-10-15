# SNMP MIB module (SVCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SVCEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:43 2024
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

(svcExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "svcExt")

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
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apSvcExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSvcTable_Object = MibTable
apSvcTable = _ApSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2)
)
if mibBuilder.loadTexts:
    apSvcTable.setStatus("current")
_ApSvcEntry_Object = MibTableRow
apSvcEntry = _ApSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1)
)
apSvcEntry.setIndexNames(
    (0, "SVCEXT-MIB", "apSvcName"),
)
if mibBuilder.loadTexts:
    apSvcEntry.setStatus("current")


class _ApSvcName_Type(DisplayString):
    """Custom type apSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApSvcName_Type.__name__ = "DisplayString"
_ApSvcName_Object = MibTableColumn
apSvcName = _ApSvcName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 1),
    _ApSvcName_Type()
)
apSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcName.setStatus("current")
_ApSvcIndex_Type = Integer32
_ApSvcIndex_Object = MibTableColumn
apSvcIndex = _ApSvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 2),
    _ApSvcIndex_Type()
)
apSvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcIndex.setStatus("current")
_ApSvcIPAddress_Type = IpAddress
_ApSvcIPAddress_Object = MibTableColumn
apSvcIPAddress = _ApSvcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 3),
    _ApSvcIPAddress_Type()
)
apSvcIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcIPAddress.setStatus("current")


class _ApSvcIPProtocol_Type(Integer32):
    """Custom type apSvcIPProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("tcp", 6),
          ("udp", 17))
    )


_ApSvcIPProtocol_Type.__name__ = "Integer32"
_ApSvcIPProtocol_Object = MibTableColumn
apSvcIPProtocol = _ApSvcIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 4),
    _ApSvcIPProtocol_Type()
)
apSvcIPProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcIPProtocol.setStatus("current")


class _ApSvcPort_Type(Integer32):
    """Custom type apSvcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcPort_Type.__name__ = "Integer32"
_ApSvcPort_Object = MibTableColumn
apSvcPort = _ApSvcPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 5),
    _ApSvcPort_Type()
)
apSvcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPort.setStatus("current")


class _ApSvcKALType_Type(Integer32):
    """Custom type apSvcKALType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("http", 2),
          ("icmp", 1),
          ("named", 5),
          ("none", 0),
          ("script", 6),
          ("tcp", 4))
    )


_ApSvcKALType_Type.__name__ = "Integer32"
_ApSvcKALType_Object = MibTableColumn
apSvcKALType = _ApSvcKALType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 6),
    _ApSvcKALType_Type()
)
apSvcKALType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALType.setStatus("current")


class _ApSvcKALFrequency_Type(Integer32):
    """Custom type apSvcKALFrequency based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcKALFrequency_Type.__name__ = "Integer32"
_ApSvcKALFrequency_Object = MibTableColumn
apSvcKALFrequency = _ApSvcKALFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 7),
    _ApSvcKALFrequency_Type()
)
apSvcKALFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALFrequency.setStatus("current")


class _ApSvcKALMaxFailure_Type(Integer32):
    """Custom type apSvcKALMaxFailure based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApSvcKALMaxFailure_Type.__name__ = "Integer32"
_ApSvcKALMaxFailure_Object = MibTableColumn
apSvcKALMaxFailure = _ApSvcKALMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 8),
    _ApSvcKALMaxFailure_Type()
)
apSvcKALMaxFailure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALMaxFailure.setStatus("current")


class _ApSvcKALRetryPeriod_Type(Integer32):
    """Custom type apSvcKALRetryPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcKALRetryPeriod_Type.__name__ = "Integer32"
_ApSvcKALRetryPeriod_Object = MibTableColumn
apSvcKALRetryPeriod = _ApSvcKALRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 9),
    _ApSvcKALRetryPeriod_Type()
)
apSvcKALRetryPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALRetryPeriod.setStatus("current")


class _ApSvcKALUri_Type(DisplayString):
    """Custom type apSvcKALUri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcKALUri_Type.__name__ = "DisplayString"
_ApSvcKALUri_Object = MibTableColumn
apSvcKALUri = _ApSvcKALUri_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 10),
    _ApSvcKALUri_Type()
)
apSvcKALUri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALUri.setStatus("current")


class _ApSvcKALMethod_Type(Integer32):
    """Custom type apSvcKALMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("head", 0),
          ("post", 2))
    )


_ApSvcKALMethod_Type.__name__ = "Integer32"
_ApSvcKALMethod_Object = MibTableColumn
apSvcKALMethod = _ApSvcKALMethod_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 11),
    _ApSvcKALMethod_Type()
)
apSvcKALMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALMethod.setStatus("current")


class _ApSvcEnable_Type(Integer32):
    """Custom type apSvcEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcEnable_Type.__name__ = "Integer32"
_ApSvcEnable_Object = MibTableColumn
apSvcEnable = _ApSvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 12),
    _ApSvcEnable_Type()
)
apSvcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcEnable.setStatus("current")


class _ApSvcType_Type(Integer32):
    """Custom type apSvcType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("automaticRedirect", 16),
          ("local", 1),
          ("nciDirectReturn", 1024),
          ("nciInfoOnly", 512),
          ("proxyCache", 4),
          ("redirect", 2),
          ("redundancyUp", 256),
          ("replicationCache", 64),
          ("replicationCacheRedirect", 4096),
          ("replicationStore", 32),
          ("replicationStoreRedirect", 2048),
          ("smashCache", 128),
          ("transparentCache", 8))
    )


_ApSvcType_Type.__name__ = "Integer32"
_ApSvcType_Object = MibTableColumn
apSvcType = _ApSvcType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 13),
    _ApSvcType_Type()
)
apSvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcType.setStatus("current")


class _ApSvcQOSMinRate_Type(Integer32):
    """Custom type apSvcQOSMinRate based on Integer32"""
    defaultValue = 14400


_ApSvcQOSMinRate_Object = MibTableColumn
apSvcQOSMinRate = _ApSvcQOSMinRate_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 14),
    _ApSvcQOSMinRate_Type()
)
apSvcQOSMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcQOSMinRate.setStatus("current")


class _ApSvcQOSMinBW_Type(Integer32):
    """Custom type apSvcQOSMinBW based on Integer32"""
    defaultValue = 100000000


_ApSvcQOSMinBW_Object = MibTableColumn
apSvcQOSMinBW = _ApSvcQOSMinBW_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 15),
    _ApSvcQOSMinBW_Type()
)
apSvcQOSMinBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcQOSMinBW.setStatus("current")


class _ApSvcWeight_Type(Integer32):
    """Custom type apSvcWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApSvcWeight_Type.__name__ = "Integer32"
_ApSvcWeight_Object = MibTableColumn
apSvcWeight = _ApSvcWeight_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 16),
    _ApSvcWeight_Type()
)
apSvcWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcWeight.setStatus("current")


class _ApSvcState_Type(Integer32):
    """Custom type apSvcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alive", 4),
          ("down", 2),
          ("dying", 5),
          ("suspended", 1))
    )


_ApSvcState_Type.__name__ = "Integer32"
_ApSvcState_Object = MibTableColumn
apSvcState = _ApSvcState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 17),
    _ApSvcState_Type()
)
apSvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcState.setStatus("current")


class _ApSvcShortLoad_Type(Integer32):
    """Custom type apSvcShortLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcShortLoad_Type.__name__ = "Integer32"
_ApSvcShortLoad_Object = MibTableColumn
apSvcShortLoad = _ApSvcShortLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 18),
    _ApSvcShortLoad_Type()
)
apSvcShortLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcShortLoad.setStatus("current")


class _ApSvcMaxConnections_Type(Integer32):
    """Custom type apSvcMaxConnections based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcMaxConnections_Type.__name__ = "Integer32"
_ApSvcMaxConnections_Object = MibTableColumn
apSvcMaxConnections = _ApSvcMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 19),
    _ApSvcMaxConnections_Type()
)
apSvcMaxConnections.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcMaxConnections.setStatus("current")


class _ApSvcConnections_Type(Integer32):
    """Custom type apSvcConnections based on Integer32"""
    defaultValue = 0


_ApSvcConnections_Object = MibTableColumn
apSvcConnections = _ApSvcConnections_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 20),
    _ApSvcConnections_Type()
)
apSvcConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcConnections.setStatus("current")


class _ApSvcTransitions_Type(Integer32):
    """Custom type apSvcTransitions based on Integer32"""
    defaultValue = 0


_ApSvcTransitions_Object = MibTableColumn
apSvcTransitions = _ApSvcTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 21),
    _ApSvcTransitions_Type()
)
apSvcTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcTransitions.setStatus("current")


class _ApSvcMaxContent_Type(Integer32):
    """Custom type apSvcMaxContent based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcMaxContent_Type.__name__ = "Integer32"
_ApSvcMaxContent_Object = MibTableColumn
apSvcMaxContent = _ApSvcMaxContent_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 22),
    _ApSvcMaxContent_Type()
)
apSvcMaxContent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcMaxContent.setStatus("current")


class _ApSvcMaxUsage_Type(Integer32):
    """Custom type apSvcMaxUsage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_ApSvcMaxUsage_Type.__name__ = "Integer32"
_ApSvcMaxUsage_Object = MibTableColumn
apSvcMaxUsage = _ApSvcMaxUsage_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 23),
    _ApSvcMaxUsage_Type()
)
apSvcMaxUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcMaxUsage.setStatus("current")


class _ApSvcMaxAge_Type(Integer32):
    """Custom type apSvcMaxAge based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_ApSvcMaxAge_Type.__name__ = "Integer32"
_ApSvcMaxAge_Object = MibTableColumn
apSvcMaxAge = _ApSvcMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 24),
    _ApSvcMaxAge_Type()
)
apSvcMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcMaxAge.setStatus("current")


class _ApSvcAccessRecordName_Type(DisplayString):
    """Custom type apSvcAccessRecordName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApSvcAccessRecordName_Type.__name__ = "DisplayString"
_ApSvcAccessRecordName_Object = MibTableColumn
apSvcAccessRecordName = _ApSvcAccessRecordName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 25),
    _ApSvcAccessRecordName_Type()
)
apSvcAccessRecordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcAccessRecordName.setStatus("current")
_ApSvcStatus_Type = RowStatus
_ApSvcStatus_Object = MibTableColumn
apSvcStatus = _ApSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 26),
    _ApSvcStatus_Type()
)
apSvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcStatus.setStatus("current")


class _ApSvcCookie_Type(DisplayString):
    """Custom type apSvcCookie based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ApSvcCookie_Type.__name__ = "DisplayString"
_ApSvcCookie_Object = MibTableColumn
apSvcCookie = _ApSvcCookie_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 27),
    _ApSvcCookie_Type()
)
apSvcCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcCookie.setStatus("current")


class _ApSvcKALPersistence_Type(Integer32):
    """Custom type apSvcKALPersistence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-persistent", 0),
          ("persistent", 1))
    )


_ApSvcKALPersistence_Type.__name__ = "Integer32"
_ApSvcKALPersistence_Object = MibTableColumn
apSvcKALPersistence = _ApSvcKALPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 28),
    _ApSvcKALPersistence_Type()
)
apSvcKALPersistence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALPersistence.setStatus("current")


class _ApSvcKALName_Type(DisplayString):
    """Custom type apSvcKALName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ApSvcKALName_Type.__name__ = "DisplayString"
_ApSvcKALName_Object = MibTableColumn
apSvcKALName = _ApSvcKALName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 29),
    _ApSvcKALName_Type()
)
apSvcKALName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALName.setStatus("current")


class _ApSvcLongLoad_Type(Integer32):
    """Custom type apSvcLongLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcLongLoad_Type.__name__ = "Integer32"
_ApSvcLongLoad_Object = MibTableColumn
apSvcLongLoad = _ApSvcLongLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 30),
    _ApSvcLongLoad_Type()
)
apSvcLongLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcLongLoad.setStatus("current")


class _ApSvcKALPort_Type(Integer32):
    """Custom type apSvcKALPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSvcKALPort_Type.__name__ = "Integer32"
_ApSvcKALPort_Object = MibTableColumn
apSvcKALPort = _ApSvcKALPort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 31),
    _ApSvcKALPort_Type()
)
apSvcKALPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALPort.setStatus("current")


class _ApSvcPublishName_Type(DisplayString):
    """Custom type apSvcPublishName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcPublishName_Type.__name__ = "DisplayString"
_ApSvcPublishName_Object = MibTableColumn
apSvcPublishName = _ApSvcPublishName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 32),
    _ApSvcPublishName_Type()
)
apSvcPublishName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPublishName.setStatus("current")


class _ApSvcPublishState_Type(Integer32):
    """Custom type apSvcPublishState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("publisher", 1),
          ("subscriber", 2))
    )


_ApSvcPublishState_Type.__name__ = "Integer32"
_ApSvcPublishState_Object = MibTableColumn
apSvcPublishState = _ApSvcPublishState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 33),
    _ApSvcPublishState_Type()
)
apSvcPublishState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPublishState.setStatus("current")


class _ApSvcPublishInterval_Type(Integer32):
    """Custom type apSvcPublishInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ApSvcPublishInterval_Type.__name__ = "Integer32"
_ApSvcPublishInterval_Object = MibTableColumn
apSvcPublishInterval = _ApSvcPublishInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 34),
    _ApSvcPublishInterval_Type()
)
apSvcPublishInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPublishInterval.setStatus("current")


class _ApSvcAccessType_Type(Integer32):
    """Custom type apSvcAccessType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp-access", 0),
          ("http-access", 1),
          ("no-access", 2))
    )


_ApSvcAccessType_Type.__name__ = "Integer32"
_ApSvcAccessType_Object = MibTableColumn
apSvcAccessType = _ApSvcAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 35),
    _ApSvcAccessType_Type()
)
apSvcAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcAccessType.setStatus("current")


class _ApSvcKALHash_Type(DisplayString):
    """Custom type apSvcKALHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALHash_Type.__name__ = "DisplayString"
_ApSvcKALHash_Object = MibTableColumn
apSvcKALHash = _ApSvcKALHash_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 36),
    _ApSvcKALHash_Type()
)
apSvcKALHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALHash.setStatus("current")


class _ApSvcKALFTPRecord_Type(DisplayString):
    """Custom type apSvcKALFTPRecord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApSvcKALFTPRecord_Type.__name__ = "DisplayString"
_ApSvcKALFTPRecord_Object = MibTableColumn
apSvcKALFTPRecord = _ApSvcKALFTPRecord_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 37),
    _ApSvcKALFTPRecord_Type()
)
apSvcKALFTPRecord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALFTPRecord.setStatus("current")


class _ApSvcPublishFile_Type(DisplayString):
    """Custom type apSvcPublishFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcPublishFile_Type.__name__ = "DisplayString"
_ApSvcPublishFile_Object = MibTableColumn
apSvcPublishFile = _ApSvcPublishFile_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 38),
    _ApSvcPublishFile_Type()
)
apSvcPublishFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPublishFile.setStatus("current")


class _ApSvcRedirectDomain_Type(DisplayString):
    """Custom type apSvcRedirectDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApSvcRedirectDomain_Type.__name__ = "DisplayString"
_ApSvcRedirectDomain_Object = MibTableColumn
apSvcRedirectDomain = _ApSvcRedirectDomain_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 39),
    _ApSvcRedirectDomain_Type()
)
apSvcRedirectDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcRedirectDomain.setStatus("current")


class _ApSvcAvgLoad_Type(Integer32):
    """Custom type apSvcAvgLoad based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_ApSvcAvgLoad_Type.__name__ = "Integer32"
_ApSvcAvgLoad_Object = MibTableColumn
apSvcAvgLoad = _ApSvcAvgLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 40),
    _ApSvcAvgLoad_Type()
)
apSvcAvgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apSvcAvgLoad.setStatus("current")


class _ApSvcIPAddressRange_Type(Integer32):
    """Custom type apSvcIPAddressRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcIPAddressRange_Type.__name__ = "Integer32"
_ApSvcIPAddressRange_Object = MibTableColumn
apSvcIPAddressRange = _ApSvcIPAddressRange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 41),
    _ApSvcIPAddressRange_Type()
)
apSvcIPAddressRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcIPAddressRange.setStatus("current")


class _ApSvcPortRange_Type(Integer32):
    """Custom type apSvcPortRange based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApSvcPortRange_Type.__name__ = "Integer32"
_ApSvcPortRange_Object = MibTableColumn
apSvcPortRange = _ApSvcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 42),
    _ApSvcPortRange_Type()
)
apSvcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcPortRange.setStatus("current")


class _ApSvcKALScriptName_Type(DisplayString):
    """Custom type apSvcKALScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALScriptName_Type.__name__ = "DisplayString"
_ApSvcKALScriptName_Object = MibTableColumn
apSvcKALScriptName = _ApSvcKALScriptName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 43),
    _ApSvcKALScriptName_Type()
)
apSvcKALScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALScriptName.setStatus("current")


class _ApSvcKALScriptArgs_Type(DisplayString):
    """Custom type apSvcKALScriptArgs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ApSvcKALScriptArgs_Type.__name__ = "DisplayString"
_ApSvcKALScriptArgs_Object = MibTableColumn
apSvcKALScriptArgs = _ApSvcKALScriptArgs_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 44),
    _ApSvcKALScriptArgs_Type()
)
apSvcKALScriptArgs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALScriptArgs.setStatus("current")


class _ApSvcKALScriptLog_Type(DisplayString):
    """Custom type apSvcKALScriptLog based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSvcKALScriptLog_Type.__name__ = "DisplayString"
_ApSvcKALScriptLog_Object = MibTableColumn
apSvcKALScriptLog = _ApSvcKALScriptLog_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 45),
    _ApSvcKALScriptLog_Type()
)
apSvcKALScriptLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcKALScriptLog.setStatus("current")


class _ApSvcCacheByPass_Type(Integer32):
    """Custom type apSvcCacheByPass based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcCacheByPass_Type.__name__ = "Integer32"
_ApSvcCacheByPass_Object = MibTableColumn
apSvcCacheByPass = _ApSvcCacheByPass_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 2, 1, 46),
    _ApSvcCacheByPass_Type()
)
apSvcCacheByPass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apSvcCacheByPass.setStatus("current")


class _ApSvcLoadThreshold_Type(Integer32):
    """Custom type apSvcLoadThreshold based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_ApSvcLoadThreshold_Type.__name__ = "Integer32"
_ApSvcLoadThreshold_Object = MibScalar
apSvcLoadThreshold = _ApSvcLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 3),
    _ApSvcLoadThreshold_Type()
)
apSvcLoadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadThreshold.setStatus("current")


class _ApSvcLoadStepSize_Type(Integer32):
    """Custom type apSvcLoadStepSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ApSvcLoadStepSize_Type.__name__ = "Integer32"
_ApSvcLoadStepSize_Object = MibScalar
apSvcLoadStepSize = _ApSvcLoadStepSize_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 4),
    _ApSvcLoadStepSize_Type()
)
apSvcLoadStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadStepSize.setStatus("current")


class _ApSvcLoadStepStatic_Type(Integer32):
    """Custom type apSvcLoadStepStatic based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcLoadStepStatic_Type.__name__ = "Integer32"
_ApSvcLoadStepStatic_Object = MibScalar
apSvcLoadStepStatic = _ApSvcLoadStepStatic_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 5),
    _ApSvcLoadStepStatic_Type()
)
apSvcLoadStepStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadStepStatic.setStatus("current")


class _ApSvcLoadDecayInterval_Type(Integer32):
    """Custom type apSvcLoadDecayInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000000),
    )


_ApSvcLoadDecayInterval_Type.__name__ = "Integer32"
_ApSvcLoadDecayInterval_Object = MibScalar
apSvcLoadDecayInterval = _ApSvcLoadDecayInterval_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 6),
    _ApSvcLoadDecayInterval_Type()
)
apSvcLoadDecayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadDecayInterval.setStatus("current")


class _ApSvcLoadEnable_Type(Integer32):
    """Custom type apSvcLoadEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ApSvcLoadEnable_Type.__name__ = "Integer32"
_ApSvcLoadEnable_Object = MibScalar
apSvcLoadEnable = _ApSvcLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 7),
    _ApSvcLoadEnable_Type()
)
apSvcLoadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadEnable.setStatus("current")


class _ApSvcLoadSvcStatRptTimeout_Type(Integer32):
    """Custom type apSvcLoadSvcStatRptTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_ApSvcLoadSvcStatRptTimeout_Type.__name__ = "Integer32"
_ApSvcLoadSvcStatRptTimeout_Object = MibScalar
apSvcLoadSvcStatRptTimeout = _ApSvcLoadSvcStatRptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 8),
    _ApSvcLoadSvcStatRptTimeout_Type()
)
apSvcLoadSvcStatRptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadSvcStatRptTimeout.setStatus("current")


class _ApSvcLoadInfoTimeout_Type(Integer32):
    """Custom type apSvcLoadInfoTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_ApSvcLoadInfoTimeout_Type.__name__ = "Integer32"
_ApSvcLoadInfoTimeout_Object = MibScalar
apSvcLoadInfoTimeout = _ApSvcLoadInfoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 9),
    _ApSvcLoadInfoTimeout_Type()
)
apSvcLoadInfoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSvcLoadInfoTimeout.setStatus("current")

# Managed Objects groups


# Notification objects

apSvcTransitionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 15, 0, 1)
)
apSvcTransitionTrap.setObjects(
      *(("SVCEXT-MIB", "apSvcName"),
        ("SVCEXT-MIB", "apSvcState"))
)
if mibBuilder.loadTexts:
    apSvcTransitionTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SVCEXT-MIB",
    **{"apSvcTransitionTrap": apSvcTransitionTrap,
       "apSvcExtMib": apSvcExtMib,
       "apSvcTable": apSvcTable,
       "apSvcEntry": apSvcEntry,
       "apSvcName": apSvcName,
       "apSvcIndex": apSvcIndex,
       "apSvcIPAddress": apSvcIPAddress,
       "apSvcIPProtocol": apSvcIPProtocol,
       "apSvcPort": apSvcPort,
       "apSvcKALType": apSvcKALType,
       "apSvcKALFrequency": apSvcKALFrequency,
       "apSvcKALMaxFailure": apSvcKALMaxFailure,
       "apSvcKALRetryPeriod": apSvcKALRetryPeriod,
       "apSvcKALUri": apSvcKALUri,
       "apSvcKALMethod": apSvcKALMethod,
       "apSvcEnable": apSvcEnable,
       "apSvcType": apSvcType,
       "apSvcQOSMinRate": apSvcQOSMinRate,
       "apSvcQOSMinBW": apSvcQOSMinBW,
       "apSvcWeight": apSvcWeight,
       "apSvcState": apSvcState,
       "apSvcShortLoad": apSvcShortLoad,
       "apSvcMaxConnections": apSvcMaxConnections,
       "apSvcConnections": apSvcConnections,
       "apSvcTransitions": apSvcTransitions,
       "apSvcMaxContent": apSvcMaxContent,
       "apSvcMaxUsage": apSvcMaxUsage,
       "apSvcMaxAge": apSvcMaxAge,
       "apSvcAccessRecordName": apSvcAccessRecordName,
       "apSvcStatus": apSvcStatus,
       "apSvcCookie": apSvcCookie,
       "apSvcKALPersistence": apSvcKALPersistence,
       "apSvcKALName": apSvcKALName,
       "apSvcLongLoad": apSvcLongLoad,
       "apSvcKALPort": apSvcKALPort,
       "apSvcPublishName": apSvcPublishName,
       "apSvcPublishState": apSvcPublishState,
       "apSvcPublishInterval": apSvcPublishInterval,
       "apSvcAccessType": apSvcAccessType,
       "apSvcKALHash": apSvcKALHash,
       "apSvcKALFTPRecord": apSvcKALFTPRecord,
       "apSvcPublishFile": apSvcPublishFile,
       "apSvcRedirectDomain": apSvcRedirectDomain,
       "apSvcAvgLoad": apSvcAvgLoad,
       "apSvcIPAddressRange": apSvcIPAddressRange,
       "apSvcPortRange": apSvcPortRange,
       "apSvcKALScriptName": apSvcKALScriptName,
       "apSvcKALScriptArgs": apSvcKALScriptArgs,
       "apSvcKALScriptLog": apSvcKALScriptLog,
       "apSvcCacheByPass": apSvcCacheByPass,
       "apSvcLoadThreshold": apSvcLoadThreshold,
       "apSvcLoadStepSize": apSvcLoadStepSize,
       "apSvcLoadStepStatic": apSvcLoadStepStatic,
       "apSvcLoadDecayInterval": apSvcLoadDecayInterval,
       "apSvcLoadEnable": apSvcLoadEnable,
       "apSvcLoadSvcStatRptTimeout": apSvcLoadSvcStatRptTimeout,
       "apSvcLoadInfoTimeout": apSvcLoadInfoTimeout}
)
