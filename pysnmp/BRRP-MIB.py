# SNMP MIB module (BRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:37 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Brrp_ObjectIdentity = ObjectIdentity
brrp = _Brrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 40)
)
_BiboBrrpOperTable_Object = MibTable
biboBrrpOperTable = _BiboBrrpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1)
)
if mibBuilder.loadTexts:
    biboBrrpOperTable.setStatus("mandatory")
_BiboBrrpOperEntry_Object = MibTableRow
biboBrrpOperEntry = _BiboBrrpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1)
)
biboBrrpOperEntry.setIndexNames(
    (0, "BRRP-MIB", "biboBrrpVirtIfIndex"),
    (0, "BRRP-MIB", "biboBrrpOperVrId"),
)
if mibBuilder.loadTexts:
    biboBrrpOperEntry.setStatus("mandatory")


class _BiboBrrpOperVrId_Type(Integer32):
    """Custom type biboBrrpOperVrId based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BiboBrrpOperVrId_Type.__name__ = "Integer32"
_BiboBrrpOperVrId_Object = MibTableColumn
biboBrrpOperVrId = _BiboBrrpOperVrId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 1),
    _BiboBrrpOperVrId_Type()
)
biboBrrpOperVrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperVrId.setStatus("mandatory")
_BiboBrrpVirtIfIndex_Type = Integer32
_BiboBrrpVirtIfIndex_Object = MibTableColumn
biboBrrpVirtIfIndex = _BiboBrrpVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 2),
    _BiboBrrpVirtIfIndex_Type()
)
biboBrrpVirtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpVirtIfIndex.setStatus("mandatory")
_BiboBrrpOperMasterIpAddr_Type = IpAddress
_BiboBrrpOperMasterIpAddr_Object = MibTableColumn
biboBrrpOperMasterIpAddr = _BiboBrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 3),
    _BiboBrrpOperMasterIpAddr_Type()
)
biboBrrpOperMasterIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperMasterIpAddr.setStatus("mandatory")


class _BiboBrrpOperState_Type(Integer32):
    """Custom type biboBrrpOperState based on Integer32"""
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
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3))
    )


_BiboBrrpOperState_Type.__name__ = "Integer32"
_BiboBrrpOperState_Object = MibTableColumn
biboBrrpOperState = _BiboBrrpOperState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 4),
    _BiboBrrpOperState_Type()
)
biboBrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpOperState.setStatus("mandatory")


class _BiboBrrpOperAdminState_Type(Integer32):
    """Custom type biboBrrpOperAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("down", 2),
          ("up", 1))
    )


_BiboBrrpOperAdminState_Type.__name__ = "Integer32"
_BiboBrrpOperAdminState_Object = MibTableColumn
biboBrrpOperAdminState = _BiboBrrpOperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 5),
    _BiboBrrpOperAdminState_Type()
)
biboBrrpOperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperAdminState.setStatus("mandatory")


class _BiboBrrpOperPriority_Type(Integer32):
    """Custom type biboBrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BiboBrrpOperPriority_Type.__name__ = "Integer32"
_BiboBrrpOperPriority_Object = MibTableColumn
biboBrrpOperPriority = _BiboBrrpOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 6),
    _BiboBrrpOperPriority_Type()
)
biboBrrpOperPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperPriority.setStatus("mandatory")


class _BiboBrrpOperAuthType_Type(Integer32):
    """Custom type biboBrrpOperAuthType based on Integer32"""
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
        *(("ipAuthenticationHeader", 3),
          ("noAuthentication", 1),
          ("simpleTextPassword", 2))
    )


_BiboBrrpOperAuthType_Type.__name__ = "Integer32"
_BiboBrrpOperAuthType_Object = MibTableColumn
biboBrrpOperAuthType = _BiboBrrpOperAuthType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 7),
    _BiboBrrpOperAuthType_Type()
)
biboBrrpOperAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperAuthType.setStatus("mandatory")


class _BiboBrrpOperAuthKey_Type(OctetString):
    """Custom type biboBrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BiboBrrpOperAuthKey_Type.__name__ = "OctetString"
_BiboBrrpOperAuthKey_Object = MibTableColumn
biboBrrpOperAuthKey = _BiboBrrpOperAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 8),
    _BiboBrrpOperAuthKey_Type()
)
biboBrrpOperAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperAuthKey.setStatus("mandatory")


class _BiboBrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type biboBrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BiboBrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_BiboBrrpOperAdvertisementInterval_Object = MibTableColumn
biboBrrpOperAdvertisementInterval = _BiboBrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 9),
    _BiboBrrpOperAdvertisementInterval_Type()
)
biboBrrpOperAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperAdvertisementInterval.setStatus("mandatory")


class _BiboBrrpOperMasterDownRetries_Type(Integer32):
    """Custom type biboBrrpOperMasterDownRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BiboBrrpOperMasterDownRetries_Type.__name__ = "Integer32"
_BiboBrrpOperMasterDownRetries_Object = MibTableColumn
biboBrrpOperMasterDownRetries = _BiboBrrpOperMasterDownRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 10),
    _BiboBrrpOperMasterDownRetries_Type()
)
biboBrrpOperMasterDownRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperMasterDownRetries.setStatus("mandatory")


class _BiboBrrpOperPreemptMode_Type(Integer32):
    """Custom type biboBrrpOperPreemptMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_BiboBrrpOperPreemptMode_Type.__name__ = "Integer32"
_BiboBrrpOperPreemptMode_Object = MibTableColumn
biboBrrpOperPreemptMode = _BiboBrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 11),
    _BiboBrrpOperPreemptMode_Type()
)
biboBrrpOperPreemptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpOperPreemptMode.setStatus("mandatory")
_BiboBrrpOperVirtualRouterUpTime_Type = TimeTicks
_BiboBrrpOperVirtualRouterUpTime_Object = MibTableColumn
biboBrrpOperVirtualRouterUpTime = _BiboBrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 12),
    _BiboBrrpOperVirtualRouterUpTime_Type()
)
biboBrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpOperVirtualRouterUpTime.setStatus("mandatory")
_BiboBrrpMasterIfIndex_Type = Integer32
_BiboBrrpMasterIfIndex_Object = MibTableColumn
biboBrrpMasterIfIndex = _BiboBrrpMasterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 14),
    _BiboBrrpMasterIfIndex_Type()
)
biboBrrpMasterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    biboBrrpMasterIfIndex.setStatus("mandatory")


class _BiboBrrpOperDecrPrio_Type(Integer32):
    """Custom type biboBrrpOperDecrPrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BiboBrrpOperDecrPrio_Type.__name__ = "Integer32"
_BiboBrrpOperDecrPrio_Object = MibTableColumn
biboBrrpOperDecrPrio = _BiboBrrpOperDecrPrio_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 1, 1, 15),
    _BiboBrrpOperDecrPrio_Type()
)
biboBrrpOperDecrPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpOperDecrPrio.setStatus("mandatory")
_BiboBrrpRouterStatsTable_Object = MibTable
biboBrrpRouterStatsTable = _BiboBrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2)
)
if mibBuilder.loadTexts:
    biboBrrpRouterStatsTable.setStatus("mandatory")
_BiboBrrpRouterStatsEntry_Object = MibTableRow
biboBrrpRouterStatsEntry = _BiboBrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1)
)
biboBrrpRouterStatsEntry.setIndexNames(
    (0, "BRRP-MIB", "biboBrrpStatsIfIndex"),
    (0, "BRRP-MIB", "biboBrrpStatsVrId"),
)
if mibBuilder.loadTexts:
    biboBrrpRouterStatsEntry.setStatus("mandatory")


class _BiboBrrpStatsVrId_Type(Integer32):
    """Custom type biboBrrpStatsVrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BiboBrrpStatsVrId_Type.__name__ = "Integer32"
_BiboBrrpStatsVrId_Object = MibTableColumn
biboBrrpStatsVrId = _BiboBrrpStatsVrId_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 1),
    _BiboBrrpStatsVrId_Type()
)
biboBrrpStatsVrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsVrId.setStatus("mandatory")
_BiboBrrpStatsIfIndex_Type = Integer32
_BiboBrrpStatsIfIndex_Object = MibTableColumn
biboBrrpStatsIfIndex = _BiboBrrpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 2),
    _BiboBrrpStatsIfIndex_Type()
)
biboBrrpStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsIfIndex.setStatus("mandatory")
_BiboBrrpStatsBecomeMaster_Type = Counter32
_BiboBrrpStatsBecomeMaster_Object = MibTableColumn
biboBrrpStatsBecomeMaster = _BiboBrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 3),
    _BiboBrrpStatsBecomeMaster_Type()
)
biboBrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsBecomeMaster.setStatus("mandatory")
_BiboBrrpStatsAdvertiseRcvd_Type = Counter32
_BiboBrrpStatsAdvertiseRcvd_Object = MibTableColumn
biboBrrpStatsAdvertiseRcvd = _BiboBrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 4),
    _BiboBrrpStatsAdvertiseRcvd_Type()
)
biboBrrpStatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsAdvertiseRcvd.setStatus("mandatory")
_BiboBrrpStatsAdvertiseIntervalErrors_Type = Counter32
_BiboBrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
biboBrrpStatsAdvertiseIntervalErrors = _BiboBrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 5),
    _BiboBrrpStatsAdvertiseIntervalErrors_Type()
)
biboBrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsAdvertiseIntervalErrors.setStatus("mandatory")
_BiboBrrpStatsAuthFailures_Type = Counter32
_BiboBrrpStatsAuthFailures_Object = MibTableColumn
biboBrrpStatsAuthFailures = _BiboBrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 6),
    _BiboBrrpStatsAuthFailures_Type()
)
biboBrrpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsAuthFailures.setStatus("mandatory")
_BiboBrrpStatsIpTtlErrors_Type = Counter32
_BiboBrrpStatsIpTtlErrors_Object = MibTableColumn
biboBrrpStatsIpTtlErrors = _BiboBrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 7),
    _BiboBrrpStatsIpTtlErrors_Type()
)
biboBrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsIpTtlErrors.setStatus("mandatory")
_BiboBrrpStatsInvalidTypePktsRcvd_Type = Counter32
_BiboBrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
biboBrrpStatsInvalidTypePktsRcvd = _BiboBrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 8),
    _BiboBrrpStatsInvalidTypePktsRcvd_Type()
)
biboBrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsInvalidTypePktsRcvd.setStatus("mandatory")
_BiboBrrpStatsInvalidAuthType_Type = Counter32
_BiboBrrpStatsInvalidAuthType_Object = MibTableColumn
biboBrrpStatsInvalidAuthType = _BiboBrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 9),
    _BiboBrrpStatsInvalidAuthType_Type()
)
biboBrrpStatsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsInvalidAuthType.setStatus("mandatory")
_BiboBrrpStatsAuthTypeMismatch_Type = Counter32
_BiboBrrpStatsAuthTypeMismatch_Object = MibTableColumn
biboBrrpStatsAuthTypeMismatch = _BiboBrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 10),
    _BiboBrrpStatsAuthTypeMismatch_Type()
)
biboBrrpStatsAuthTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsAuthTypeMismatch.setStatus("mandatory")
_BiboBrrpStatsPacketLengthErrors_Type = Counter32
_BiboBrrpStatsPacketLengthErrors_Object = MibTableColumn
biboBrrpStatsPacketLengthErrors = _BiboBrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 11),
    _BiboBrrpStatsPacketLengthErrors_Type()
)
biboBrrpStatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsPacketLengthErrors.setStatus("mandatory")
_BiboBrrpStatsChecksumErrors_Type = Counter32
_BiboBrrpStatsChecksumErrors_Object = MibTableColumn
biboBrrpStatsChecksumErrors = _BiboBrrpStatsChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 12),
    _BiboBrrpStatsChecksumErrors_Type()
)
biboBrrpStatsChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsChecksumErrors.setStatus("mandatory")
_BiboBrrpStatsVersionErrors_Type = Counter32
_BiboBrrpStatsVersionErrors_Object = MibTableColumn
biboBrrpStatsVersionErrors = _BiboBrrpStatsVersionErrors_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 40, 2, 1, 13),
    _BiboBrrpStatsVersionErrors_Type()
)
biboBrrpStatsVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biboBrrpStatsVersionErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRRP-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "brrp": brrp,
       "biboBrrpOperTable": biboBrrpOperTable,
       "biboBrrpOperEntry": biboBrrpOperEntry,
       "biboBrrpOperVrId": biboBrrpOperVrId,
       "biboBrrpVirtIfIndex": biboBrrpVirtIfIndex,
       "biboBrrpOperMasterIpAddr": biboBrrpOperMasterIpAddr,
       "biboBrrpOperState": biboBrrpOperState,
       "biboBrrpOperAdminState": biboBrrpOperAdminState,
       "biboBrrpOperPriority": biboBrrpOperPriority,
       "biboBrrpOperAuthType": biboBrrpOperAuthType,
       "biboBrrpOperAuthKey": biboBrrpOperAuthKey,
       "biboBrrpOperAdvertisementInterval": biboBrrpOperAdvertisementInterval,
       "biboBrrpOperMasterDownRetries": biboBrrpOperMasterDownRetries,
       "biboBrrpOperPreemptMode": biboBrrpOperPreemptMode,
       "biboBrrpOperVirtualRouterUpTime": biboBrrpOperVirtualRouterUpTime,
       "biboBrrpMasterIfIndex": biboBrrpMasterIfIndex,
       "biboBrrpOperDecrPrio": biboBrrpOperDecrPrio,
       "biboBrrpRouterStatsTable": biboBrrpRouterStatsTable,
       "biboBrrpRouterStatsEntry": biboBrrpRouterStatsEntry,
       "biboBrrpStatsVrId": biboBrrpStatsVrId,
       "biboBrrpStatsIfIndex": biboBrrpStatsIfIndex,
       "biboBrrpStatsBecomeMaster": biboBrrpStatsBecomeMaster,
       "biboBrrpStatsAdvertiseRcvd": biboBrrpStatsAdvertiseRcvd,
       "biboBrrpStatsAdvertiseIntervalErrors": biboBrrpStatsAdvertiseIntervalErrors,
       "biboBrrpStatsAuthFailures": biboBrrpStatsAuthFailures,
       "biboBrrpStatsIpTtlErrors": biboBrrpStatsIpTtlErrors,
       "biboBrrpStatsInvalidTypePktsRcvd": biboBrrpStatsInvalidTypePktsRcvd,
       "biboBrrpStatsInvalidAuthType": biboBrrpStatsInvalidAuthType,
       "biboBrrpStatsAuthTypeMismatch": biboBrrpStatsAuthTypeMismatch,
       "biboBrrpStatsPacketLengthErrors": biboBrrpStatsPacketLengthErrors,
       "biboBrrpStatsChecksumErrors": biboBrrpStatsChecksumErrors,
       "biboBrrpStatsVersionErrors": biboBrrpStatsVersionErrors}
)
