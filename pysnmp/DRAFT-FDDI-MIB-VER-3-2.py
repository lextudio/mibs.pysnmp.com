# SNMP MIB module (DRAFT-FDDI-MIB-VER-3-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DRAFT-FDDI-MIB-VER-3-2
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:26 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FddiTimeNano(Integer32):
    """Custom type FddiTimeNano based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FddiTimeMilli(Integer32):
    """Custom type FddiTimeMilli based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class FddiResourceId(Integer32):
    """Custom type FddiResourceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class FddiSMTStationIdType(OctetString):
    """Custom type FddiSMTStationIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class FddiMACLongAddressType(OctetString):
    """Custom type FddiMACLongAddressType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fddi_ObjectIdentity = ObjectIdentity
fddi = _Fddi_ObjectIdentity(
    (1, 3, 6, 1, 3, 8)
)
_Fddimib_ObjectIdentity = ObjectIdentity
fddimib = _Fddimib_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73)
)
_FddimibSMT_ObjectIdentity = ObjectIdentity
fddimibSMT = _FddimibSMT_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73, 1)
)


class _FddimibSMTNumber_Type(Integer32):
    """Custom type fddimibSMTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibSMTNumber_Type.__name__ = "Integer32"
_FddimibSMTNumber_Object = MibScalar
fddimibSMTNumber = _FddimibSMTNumber_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 1),
    _FddimibSMTNumber_Type()
)
fddimibSMTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTNumber.setStatus("mandatory")
_FddimibSMTTable_Object = MibTable
fddimibSMTTable = _FddimibSMTTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2)
)
if mibBuilder.loadTexts:
    fddimibSMTTable.setStatus("mandatory")
_FddimibSMTEntry_Object = MibTableRow
fddimibSMTEntry = _FddimibSMTEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1)
)
fddimibSMTEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibSMTIndex"),
)
if mibBuilder.loadTexts:
    fddimibSMTEntry.setStatus("mandatory")


class _FddimibSMTIndex_Type(Integer32):
    """Custom type fddimibSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibSMTIndex_Type.__name__ = "Integer32"
_FddimibSMTIndex_Object = MibTableColumn
fddimibSMTIndex = _FddimibSMTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 1),
    _FddimibSMTIndex_Type()
)
fddimibSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTIndex.setStatus("mandatory")
_FddimibSMTStationId_Type = FddiSMTStationIdType
_FddimibSMTStationId_Object = MibTableColumn
fddimibSMTStationId = _FddimibSMTStationId_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 2),
    _FddimibSMTStationId_Type()
)
fddimibSMTStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTStationId.setStatus("mandatory")


class _FddimibSMTOpVersionId_Type(Integer32):
    """Custom type fddimibSMTOpVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibSMTOpVersionId_Type.__name__ = "Integer32"
_FddimibSMTOpVersionId_Object = MibTableColumn
fddimibSMTOpVersionId = _FddimibSMTOpVersionId_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 3),
    _FddimibSMTOpVersionId_Type()
)
fddimibSMTOpVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTOpVersionId.setStatus("mandatory")


class _FddimibSMTHiVersionId_Type(Integer32):
    """Custom type fddimibSMTHiVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibSMTHiVersionId_Type.__name__ = "Integer32"
_FddimibSMTHiVersionId_Object = MibTableColumn
fddimibSMTHiVersionId = _FddimibSMTHiVersionId_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 4),
    _FddimibSMTHiVersionId_Type()
)
fddimibSMTHiVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTHiVersionId.setStatus("mandatory")


class _FddimibSMTLoVersionId_Type(Integer32):
    """Custom type fddimibSMTLoVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibSMTLoVersionId_Type.__name__ = "Integer32"
_FddimibSMTLoVersionId_Object = MibTableColumn
fddimibSMTLoVersionId = _FddimibSMTLoVersionId_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 5),
    _FddimibSMTLoVersionId_Type()
)
fddimibSMTLoVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTLoVersionId.setStatus("mandatory")


class _FddimibSMTUserData_Type(OctetString):
    """Custom type fddimibSMTUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_FddimibSMTUserData_Type.__name__ = "OctetString"
_FddimibSMTUserData_Object = MibTableColumn
fddimibSMTUserData = _FddimibSMTUserData_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 6),
    _FddimibSMTUserData_Type()
)
fddimibSMTUserData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTUserData.setStatus("mandatory")


class _FddimibSMTMIBVersionId_Type(Integer32):
    """Custom type fddimibSMTMIBVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibSMTMIBVersionId_Type.__name__ = "Integer32"
_FddimibSMTMIBVersionId_Object = MibTableColumn
fddimibSMTMIBVersionId = _FddimibSMTMIBVersionId_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 7),
    _FddimibSMTMIBVersionId_Type()
)
fddimibSMTMIBVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTMIBVersionId.setStatus("mandatory")


class _FddimibSMTMACCts_Type(Integer32):
    """Custom type fddimibSMTMACCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FddimibSMTMACCts_Type.__name__ = "Integer32"
_FddimibSMTMACCts_Object = MibTableColumn
fddimibSMTMACCts = _FddimibSMTMACCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 8),
    _FddimibSMTMACCts_Type()
)
fddimibSMTMACCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTMACCts.setStatus("mandatory")


class _FddimibSMTNonMasterCts_Type(Integer32):
    """Custom type fddimibSMTNonMasterCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_FddimibSMTNonMasterCts_Type.__name__ = "Integer32"
_FddimibSMTNonMasterCts_Object = MibTableColumn
fddimibSMTNonMasterCts = _FddimibSMTNonMasterCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 9),
    _FddimibSMTNonMasterCts_Type()
)
fddimibSMTNonMasterCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTNonMasterCts.setStatus("mandatory")


class _FddimibSMTMasterCts_Type(Integer32):
    """Custom type fddimibSMTMasterCts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FddimibSMTMasterCts_Type.__name__ = "Integer32"
_FddimibSMTMasterCts_Object = MibTableColumn
fddimibSMTMasterCts = _FddimibSMTMasterCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 10),
    _FddimibSMTMasterCts_Type()
)
fddimibSMTMasterCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTMasterCts.setStatus("mandatory")


class _FddimibSMTAvailablePaths_Type(Integer32):
    """Custom type fddimibSMTAvailablePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FddimibSMTAvailablePaths_Type.__name__ = "Integer32"
_FddimibSMTAvailablePaths_Object = MibTableColumn
fddimibSMTAvailablePaths = _FddimibSMTAvailablePaths_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 11),
    _FddimibSMTAvailablePaths_Type()
)
fddimibSMTAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTAvailablePaths.setStatus("mandatory")


class _FddimibSMTConfigCapabilities_Type(Integer32):
    """Custom type fddimibSMTConfigCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FddimibSMTConfigCapabilities_Type.__name__ = "Integer32"
_FddimibSMTConfigCapabilities_Object = MibTableColumn
fddimibSMTConfigCapabilities = _FddimibSMTConfigCapabilities_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 12),
    _FddimibSMTConfigCapabilities_Type()
)
fddimibSMTConfigCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTConfigCapabilities.setStatus("mandatory")


class _FddimibSMTConfigPolicy_Type(Integer32):
    """Custom type fddimibSMTConfigPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FddimibSMTConfigPolicy_Type.__name__ = "Integer32"
_FddimibSMTConfigPolicy_Object = MibTableColumn
fddimibSMTConfigPolicy = _FddimibSMTConfigPolicy_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 13),
    _FddimibSMTConfigPolicy_Type()
)
fddimibSMTConfigPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTConfigPolicy.setStatus("mandatory")


class _FddimibSMTConnectionPolicy_Type(Integer32):
    """Custom type fddimibSMTConnectionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32768, 65535),
    )


_FddimibSMTConnectionPolicy_Type.__name__ = "Integer32"
_FddimibSMTConnectionPolicy_Object = MibTableColumn
fddimibSMTConnectionPolicy = _FddimibSMTConnectionPolicy_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 14),
    _FddimibSMTConnectionPolicy_Type()
)
fddimibSMTConnectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTConnectionPolicy.setStatus("mandatory")


class _FddimibSMTTNotify_Type(Integer32):
    """Custom type fddimibSMTTNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_FddimibSMTTNotify_Type.__name__ = "Integer32"
_FddimibSMTTNotify_Object = MibTableColumn
fddimibSMTTNotify = _FddimibSMTTNotify_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 15),
    _FddimibSMTTNotify_Type()
)
fddimibSMTTNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTTNotify.setStatus("mandatory")


class _FddimibSMTStatRptPolicy_Type(Integer32):
    """Custom type fddimibSMTStatRptPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibSMTStatRptPolicy_Type.__name__ = "Integer32"
_FddimibSMTStatRptPolicy_Object = MibTableColumn
fddimibSMTStatRptPolicy = _FddimibSMTStatRptPolicy_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 16),
    _FddimibSMTStatRptPolicy_Type()
)
fddimibSMTStatRptPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTStatRptPolicy.setStatus("mandatory")
_FddimibSMTTraceMaxExpiration_Type = FddiTimeMilli
_FddimibSMTTraceMaxExpiration_Object = MibTableColumn
fddimibSMTTraceMaxExpiration = _FddimibSMTTraceMaxExpiration_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 17),
    _FddimibSMTTraceMaxExpiration_Type()
)
fddimibSMTTraceMaxExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTTraceMaxExpiration.setStatus("mandatory")


class _FddimibSMTBypassPresent_Type(Integer32):
    """Custom type fddimibSMTBypassPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibSMTBypassPresent_Type.__name__ = "Integer32"
_FddimibSMTBypassPresent_Object = MibTableColumn
fddimibSMTBypassPresent = _FddimibSMTBypassPresent_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 18),
    _FddimibSMTBypassPresent_Type()
)
fddimibSMTBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTBypassPresent.setStatus("mandatory")


class _FddimibSMTECMState_Type(Integer32):
    """Custom type fddimibSMTECMState based on Integer32"""
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
        *(("ec0", 1),
          ("ec1", 2),
          ("ec2", 3),
          ("ec3", 4),
          ("ec4", 5),
          ("ec5", 6),
          ("ec6", 7),
          ("ec7", 8))
    )


_FddimibSMTECMState_Type.__name__ = "Integer32"
_FddimibSMTECMState_Object = MibTableColumn
fddimibSMTECMState = _FddimibSMTECMState_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 19),
    _FddimibSMTECMState_Type()
)
fddimibSMTECMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTECMState.setStatus("mandatory")


class _FddimibSMTCFState_Type(Integer32):
    """Custom type fddimibSMTCFState based on Integer32"""
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
        *(("cf0", 1),
          ("cf1", 2),
          ("cf10", 11),
          ("cf11", 12),
          ("cf12", 13),
          ("cf2", 3),
          ("cf3", 4),
          ("cf4", 5),
          ("cf5", 6),
          ("cf6", 7),
          ("cf7", 8),
          ("cf8", 9),
          ("cf9", 10))
    )


_FddimibSMTCFState_Type.__name__ = "Integer32"
_FddimibSMTCFState_Object = MibTableColumn
fddimibSMTCFState = _FddimibSMTCFState_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 20),
    _FddimibSMTCFState_Type()
)
fddimibSMTCFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTCFState.setStatus("mandatory")


class _FddimibSMTRemoteDisconnectFlag_Type(Integer32):
    """Custom type fddimibSMTRemoteDisconnectFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibSMTRemoteDisconnectFlag_Type.__name__ = "Integer32"
_FddimibSMTRemoteDisconnectFlag_Object = MibTableColumn
fddimibSMTRemoteDisconnectFlag = _FddimibSMTRemoteDisconnectFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 21),
    _FddimibSMTRemoteDisconnectFlag_Type()
)
fddimibSMTRemoteDisconnectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTRemoteDisconnectFlag.setStatus("mandatory")


class _FddimibSMTStationStatus_Type(Integer32):
    """Custom type fddimibSMTStationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concatenated", 1),
          ("separated", 2),
          ("thru", 3))
    )


_FddimibSMTStationStatus_Type.__name__ = "Integer32"
_FddimibSMTStationStatus_Object = MibTableColumn
fddimibSMTStationStatus = _FddimibSMTStationStatus_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 22),
    _FddimibSMTStationStatus_Type()
)
fddimibSMTStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTStationStatus.setStatus("mandatory")


class _FddimibSMTPeerWrapFlag_Type(Integer32):
    """Custom type fddimibSMTPeerWrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibSMTPeerWrapFlag_Type.__name__ = "Integer32"
_FddimibSMTPeerWrapFlag_Object = MibTableColumn
fddimibSMTPeerWrapFlag = _FddimibSMTPeerWrapFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 23),
    _FddimibSMTPeerWrapFlag_Type()
)
fddimibSMTPeerWrapFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTPeerWrapFlag.setStatus("mandatory")
_FddimibSMTTimeStamp_Type = FddiTimeMilli
_FddimibSMTTimeStamp_Object = MibTableColumn
fddimibSMTTimeStamp = _FddimibSMTTimeStamp_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 24),
    _FddimibSMTTimeStamp_Type()
)
fddimibSMTTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTTimeStamp.setStatus("mandatory")
_FddimibSMTTransitionTimeStamp_Type = FddiTimeMilli
_FddimibSMTTransitionTimeStamp_Object = MibTableColumn
fddimibSMTTransitionTimeStamp = _FddimibSMTTransitionTimeStamp_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 25),
    _FddimibSMTTransitionTimeStamp_Type()
)
fddimibSMTTransitionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibSMTTransitionTimeStamp.setStatus("mandatory")


class _FddimibSMTStationAction_Type(Integer32):
    """Custom type fddimibSMTStationAction based on Integer32"""
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
        *(("connect", 2),
          ("disable-a", 6),
          ("disable-b", 7),
          ("disable-m", 8),
          ("disconnect", 3),
          ("other", 1),
          ("path-Test", 4),
          ("self-Test", 5))
    )


_FddimibSMTStationAction_Type.__name__ = "Integer32"
_FddimibSMTStationAction_Object = MibTableColumn
fddimibSMTStationAction = _FddimibSMTStationAction_Object(
    (1, 3, 6, 1, 3, 8, 73, 1, 2, 1, 26),
    _FddimibSMTStationAction_Type()
)
fddimibSMTStationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibSMTStationAction.setStatus("mandatory")
_FddimibMAC_ObjectIdentity = ObjectIdentity
fddimibMAC = _FddimibMAC_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73, 2)
)


class _FddimibMACNumber_Type(Integer32):
    """Custom type fddimibMACNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibMACNumber_Type.__name__ = "Integer32"
_FddimibMACNumber_Object = MibScalar
fddimibMACNumber = _FddimibMACNumber_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 1),
    _FddimibMACNumber_Type()
)
fddimibMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACNumber.setStatus("mandatory")
_FddimibMACTable_Object = MibTable
fddimibMACTable = _FddimibMACTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2)
)
if mibBuilder.loadTexts:
    fddimibMACTable.setStatus("mandatory")
_FddimibMACEntry_Object = MibTableRow
fddimibMACEntry = _FddimibMACEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1)
)
fddimibMACEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibMACIndex"),
)
if mibBuilder.loadTexts:
    fddimibMACEntry.setStatus("mandatory")


class _FddimibMACSMTIndex_Type(Integer32):
    """Custom type fddimibMACSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibMACSMTIndex_Type.__name__ = "Integer32"
_FddimibMACSMTIndex_Object = MibTableColumn
fddimibMACSMTIndex = _FddimibMACSMTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 1),
    _FddimibMACSMTIndex_Type()
)
fddimibMACSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACSMTIndex.setStatus("mandatory")


class _FddimibMACIndex_Type(Integer32):
    """Custom type fddimibMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibMACIndex_Type.__name__ = "Integer32"
_FddimibMACIndex_Object = MibTableColumn
fddimibMACIndex = _FddimibMACIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 2),
    _FddimibMACIndex_Type()
)
fddimibMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACIndex.setStatus("mandatory")


class _FddimibMACIfIndex_Type(Integer32):
    """Custom type fddimibMACIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibMACIfIndex_Type.__name__ = "Integer32"
_FddimibMACIfIndex_Object = MibTableColumn
fddimibMACIfIndex = _FddimibMACIfIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 3),
    _FddimibMACIfIndex_Type()
)
fddimibMACIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACIfIndex.setStatus("mandatory")


class _FddimibMACFrameStatusFunctions_Type(Integer32):
    """Custom type fddimibMACFrameStatusFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FddimibMACFrameStatusFunctions_Type.__name__ = "Integer32"
_FddimibMACFrameStatusFunctions_Object = MibTableColumn
fddimibMACFrameStatusFunctions = _FddimibMACFrameStatusFunctions_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 4),
    _FddimibMACFrameStatusFunctions_Type()
)
fddimibMACFrameStatusFunctions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACFrameStatusFunctions.setStatus("mandatory")
_FddimibMACTMaxCapability_Type = FddiTimeNano
_FddimibMACTMaxCapability_Object = MibTableColumn
fddimibMACTMaxCapability = _FddimibMACTMaxCapability_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 5),
    _FddimibMACTMaxCapability_Type()
)
fddimibMACTMaxCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTMaxCapability.setStatus("mandatory")
_FddimibMACTVXCapability_Type = FddiTimeNano
_FddimibMACTVXCapability_Object = MibTableColumn
fddimibMACTVXCapability = _FddimibMACTVXCapability_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 6),
    _FddimibMACTVXCapability_Type()
)
fddimibMACTVXCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTVXCapability.setStatus("mandatory")


class _FddimibMACAvailablePaths_Type(Integer32):
    """Custom type fddimibMACAvailablePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FddimibMACAvailablePaths_Type.__name__ = "Integer32"
_FddimibMACAvailablePaths_Object = MibTableColumn
fddimibMACAvailablePaths = _FddimibMACAvailablePaths_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 7),
    _FddimibMACAvailablePaths_Type()
)
fddimibMACAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACAvailablePaths.setStatus("mandatory")


class _FddimibMACCurrentPath_Type(Integer32):
    """Custom type fddimibMACCurrentPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("concatenated", 5),
          ("isolated", 1),
          ("local", 2),
          ("primary", 4),
          ("secondary", 3),
          ("thru", 6))
    )


_FddimibMACCurrentPath_Type.__name__ = "Integer32"
_FddimibMACCurrentPath_Object = MibTableColumn
fddimibMACCurrentPath = _FddimibMACCurrentPath_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 8),
    _FddimibMACCurrentPath_Type()
)
fddimibMACCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACCurrentPath.setStatus("mandatory")
_FddimibMACUpstreamNbr_Type = FddiMACLongAddressType
_FddimibMACUpstreamNbr_Object = MibTableColumn
fddimibMACUpstreamNbr = _FddimibMACUpstreamNbr_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 9),
    _FddimibMACUpstreamNbr_Type()
)
fddimibMACUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACUpstreamNbr.setStatus("mandatory")
_FddimibMACDownstreamNbr_Type = FddiMACLongAddressType
_FddimibMACDownstreamNbr_Object = MibTableColumn
fddimibMACDownstreamNbr = _FddimibMACDownstreamNbr_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 10),
    _FddimibMACDownstreamNbr_Type()
)
fddimibMACDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACDownstreamNbr.setStatus("mandatory")
_FddimibMACOldUpstreamNbr_Type = FddiMACLongAddressType
_FddimibMACOldUpstreamNbr_Object = MibTableColumn
fddimibMACOldUpstreamNbr = _FddimibMACOldUpstreamNbr_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 11),
    _FddimibMACOldUpstreamNbr_Type()
)
fddimibMACOldUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACOldUpstreamNbr.setStatus("mandatory")
_FddimibMACOldDownstreamNbr_Type = FddiMACLongAddressType
_FddimibMACOldDownstreamNbr_Object = MibTableColumn
fddimibMACOldDownstreamNbr = _FddimibMACOldDownstreamNbr_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 12),
    _FddimibMACOldDownstreamNbr_Type()
)
fddimibMACOldDownstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACOldDownstreamNbr.setStatus("mandatory")


class _FddimibMACDupAddressTest_Type(Integer32):
    """Custom type fddimibMACDupAddressTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("none", 1),
          ("pass", 2))
    )


_FddimibMACDupAddressTest_Type.__name__ = "Integer32"
_FddimibMACDupAddressTest_Object = MibTableColumn
fddimibMACDupAddressTest = _FddimibMACDupAddressTest_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 13),
    _FddimibMACDupAddressTest_Type()
)
fddimibMACDupAddressTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACDupAddressTest.setStatus("mandatory")


class _FddimibMACRequestedPaths_Type(Integer32):
    """Custom type fddimibMACRequestedPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FddimibMACRequestedPaths_Type.__name__ = "Integer32"
_FddimibMACRequestedPaths_Object = MibTableColumn
fddimibMACRequestedPaths = _FddimibMACRequestedPaths_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 14),
    _FddimibMACRequestedPaths_Type()
)
fddimibMACRequestedPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibMACRequestedPaths.setStatus("mandatory")


class _FddimibMACDownstreamPORTType_Type(Integer32):
    """Custom type fddimibMACDownstreamPORTType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("none", 5),
          ("s", 3))
    )


_FddimibMACDownstreamPORTType_Type.__name__ = "Integer32"
_FddimibMACDownstreamPORTType_Object = MibTableColumn
fddimibMACDownstreamPORTType = _FddimibMACDownstreamPORTType_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 15),
    _FddimibMACDownstreamPORTType_Type()
)
fddimibMACDownstreamPORTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACDownstreamPORTType.setStatus("mandatory")
_FddimibMACSMTAddress_Type = FddiMACLongAddressType
_FddimibMACSMTAddress_Object = MibTableColumn
fddimibMACSMTAddress = _FddimibMACSMTAddress_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 16),
    _FddimibMACSMTAddress_Type()
)
fddimibMACSMTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACSMTAddress.setStatus("mandatory")
_FddimibMACTReq_Type = FddiTimeNano
_FddimibMACTReq_Object = MibTableColumn
fddimibMACTReq = _FddimibMACTReq_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 17),
    _FddimibMACTReq_Type()
)
fddimibMACTReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTReq.setStatus("mandatory")
_FddimibMACTNeg_Type = FddiTimeNano
_FddimibMACTNeg_Object = MibTableColumn
fddimibMACTNeg = _FddimibMACTNeg_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 18),
    _FddimibMACTNeg_Type()
)
fddimibMACTNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTNeg.setStatus("mandatory")
_FddimibMACTMax_Type = FddiTimeNano
_FddimibMACTMax_Object = MibTableColumn
fddimibMACTMax = _FddimibMACTMax_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 19),
    _FddimibMACTMax_Type()
)
fddimibMACTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTMax.setStatus("mandatory")
_FddimibMACTvxValue_Type = FddiTimeNano
_FddimibMACTvxValue_Object = MibTableColumn
fddimibMACTvxValue = _FddimibMACTvxValue_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 20),
    _FddimibMACTvxValue_Type()
)
fddimibMACTvxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTvxValue.setStatus("mandatory")
_FddimibMACFrameCts_Type = Counter32
_FddimibMACFrameCts_Object = MibTableColumn
fddimibMACFrameCts = _FddimibMACFrameCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 21),
    _FddimibMACFrameCts_Type()
)
fddimibMACFrameCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACFrameCts.setStatus("mandatory")
_FddimibMACCopiedCts_Type = Counter32
_FddimibMACCopiedCts_Object = MibTableColumn
fddimibMACCopiedCts = _FddimibMACCopiedCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 22),
    _FddimibMACCopiedCts_Type()
)
fddimibMACCopiedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACCopiedCts.setStatus("mandatory")
_FddimibMACTransmitCts_Type = Counter32
_FddimibMACTransmitCts_Object = MibTableColumn
fddimibMACTransmitCts = _FddimibMACTransmitCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 23),
    _FddimibMACTransmitCts_Type()
)
fddimibMACTransmitCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTransmitCts.setStatus("mandatory")
_FddimibMACErrorCts_Type = Counter32
_FddimibMACErrorCts_Object = MibTableColumn
fddimibMACErrorCts = _FddimibMACErrorCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 24),
    _FddimibMACErrorCts_Type()
)
fddimibMACErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACErrorCts.setStatus("mandatory")
_FddimibMACLostCts_Type = Counter32
_FddimibMACLostCts_Object = MibTableColumn
fddimibMACLostCts = _FddimibMACLostCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 25),
    _FddimibMACLostCts_Type()
)
fddimibMACLostCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACLostCts.setStatus("mandatory")


class _FddimibMACFrameErrorThreshold_Type(Integer32):
    """Custom type fddimibMACFrameErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibMACFrameErrorThreshold_Type.__name__ = "Integer32"
_FddimibMACFrameErrorThreshold_Object = MibTableColumn
fddimibMACFrameErrorThreshold = _FddimibMACFrameErrorThreshold_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 26),
    _FddimibMACFrameErrorThreshold_Type()
)
fddimibMACFrameErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibMACFrameErrorThreshold.setStatus("mandatory")


class _FddimibMACFrameErrorRatio_Type(Integer32):
    """Custom type fddimibMACFrameErrorRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibMACFrameErrorRatio_Type.__name__ = "Integer32"
_FddimibMACFrameErrorRatio_Object = MibTableColumn
fddimibMACFrameErrorRatio = _FddimibMACFrameErrorRatio_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 27),
    _FddimibMACFrameErrorRatio_Type()
)
fddimibMACFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACFrameErrorRatio.setStatus("mandatory")


class _FddimibMACRMTState_Type(Integer32):
    """Custom type fddimibMACRMTState based on Integer32"""
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
        *(("rm0", 1),
          ("rm1", 2),
          ("rm2", 3),
          ("rm3", 4),
          ("rm4", 5),
          ("rm5", 6),
          ("rm6", 7),
          ("rm7", 8))
    )


_FddimibMACRMTState_Type.__name__ = "Integer32"
_FddimibMACRMTState_Object = MibTableColumn
fddimibMACRMTState = _FddimibMACRMTState_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 28),
    _FddimibMACRMTState_Type()
)
fddimibMACRMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACRMTState.setStatus("mandatory")


class _FddimibMACDaFlag_Type(Integer32):
    """Custom type fddimibMACDaFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACDaFlag_Type.__name__ = "Integer32"
_FddimibMACDaFlag_Object = MibTableColumn
fddimibMACDaFlag = _FddimibMACDaFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 29),
    _FddimibMACDaFlag_Type()
)
fddimibMACDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACDaFlag.setStatus("mandatory")


class _FddimibMACUnaDaFlag_Type(Integer32):
    """Custom type fddimibMACUnaDaFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACUnaDaFlag_Type.__name__ = "Integer32"
_FddimibMACUnaDaFlag_Object = MibTableColumn
fddimibMACUnaDaFlag = _FddimibMACUnaDaFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 30),
    _FddimibMACUnaDaFlag_Type()
)
fddimibMACUnaDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACUnaDaFlag.setStatus("mandatory")


class _FddimibMACFrameErrorFlag_Type(Integer32):
    """Custom type fddimibMACFrameErrorFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACFrameErrorFlag_Type.__name__ = "Integer32"
_FddimibMACFrameErrorFlag_Object = MibTableColumn
fddimibMACFrameErrorFlag = _FddimibMACFrameErrorFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 31),
    _FddimibMACFrameErrorFlag_Type()
)
fddimibMACFrameErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACFrameErrorFlag.setStatus("mandatory")


class _FddimibMACMAUnitdataAvailable_Type(Integer32):
    """Custom type fddimibMACMAUnitdataAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACMAUnitdataAvailable_Type.__name__ = "Integer32"
_FddimibMACMAUnitdataAvailable_Object = MibTableColumn
fddimibMACMAUnitdataAvailable = _FddimibMACMAUnitdataAvailable_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 32),
    _FddimibMACMAUnitdataAvailable_Type()
)
fddimibMACMAUnitdataAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACMAUnitdataAvailable.setStatus("mandatory")


class _FddimibMACHardwarePresent_Type(Integer32):
    """Custom type fddimibMACHardwarePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACHardwarePresent_Type.__name__ = "Integer32"
_FddimibMACHardwarePresent_Object = MibTableColumn
fddimibMACHardwarePresent = _FddimibMACHardwarePresent_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 33),
    _FddimibMACHardwarePresent_Type()
)
fddimibMACHardwarePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACHardwarePresent.setStatus("mandatory")


class _FddimibMACMAUnitdataEnable_Type(Integer32):
    """Custom type fddimibMACMAUnitdataEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACMAUnitdataEnable_Type.__name__ = "Integer32"
_FddimibMACMAUnitdataEnable_Object = MibTableColumn
fddimibMACMAUnitdataEnable = _FddimibMACMAUnitdataEnable_Object(
    (1, 3, 6, 1, 3, 8, 73, 2, 2, 1, 34),
    _FddimibMACMAUnitdataEnable_Type()
)
fddimibMACMAUnitdataEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibMACMAUnitdataEnable.setStatus("mandatory")
_FddimibMACCounters_ObjectIdentity = ObjectIdentity
fddimibMACCounters = _FddimibMACCounters_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73, 3)
)
_FddimibMACCountersTable_Object = MibTable
fddimibMACCountersTable = _FddimibMACCountersTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1)
)
if mibBuilder.loadTexts:
    fddimibMACCountersTable.setStatus("mandatory")
_FddimibMACCountersEntry_Object = MibTableRow
fddimibMACCountersEntry = _FddimibMACCountersEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1)
)
fddimibMACCountersEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibMACSMTIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibMACIndex"),
)
if mibBuilder.loadTexts:
    fddimibMACCountersEntry.setStatus("mandatory")
_FddimibMACTokenCts_Type = Counter32
_FddimibMACTokenCts_Object = MibTableColumn
fddimibMACTokenCts = _FddimibMACTokenCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 1),
    _FddimibMACTokenCts_Type()
)
fddimibMACTokenCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTokenCts.setStatus("mandatory")
_FddimibMACTvxExpiredCts_Type = Counter32
_FddimibMACTvxExpiredCts_Object = MibTableColumn
fddimibMACTvxExpiredCts = _FddimibMACTvxExpiredCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 2),
    _FddimibMACTvxExpiredCts_Type()
)
fddimibMACTvxExpiredCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACTvxExpiredCts.setStatus("mandatory")
_FddimibMACNotCopiedCts_Type = Counter32
_FddimibMACNotCopiedCts_Object = MibTableColumn
fddimibMACNotCopiedCts = _FddimibMACNotCopiedCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 3),
    _FddimibMACNotCopiedCts_Type()
)
fddimibMACNotCopiedCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACNotCopiedCts.setStatus("mandatory")
_FddimibMACLateCts_Type = Counter32
_FddimibMACLateCts_Object = MibTableColumn
fddimibMACLateCts = _FddimibMACLateCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 4),
    _FddimibMACLateCts_Type()
)
fddimibMACLateCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACLateCts.setStatus("mandatory")
_FddimibMACRingOpCts_Type = Counter32
_FddimibMACRingOpCts_Object = MibTableColumn
fddimibMACRingOpCts = _FddimibMACRingOpCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 5),
    _FddimibMACRingOpCts_Type()
)
fddimibMACRingOpCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACRingOpCts.setStatus("mandatory")


class _FddimibMACNotCopiedRatio_Type(Integer32):
    """Custom type fddimibMACNotCopiedRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibMACNotCopiedRatio_Type.__name__ = "Integer32"
_FddimibMACNotCopiedRatio_Object = MibTableColumn
fddimibMACNotCopiedRatio = _FddimibMACNotCopiedRatio_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 6),
    _FddimibMACNotCopiedRatio_Type()
)
fddimibMACNotCopiedRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACNotCopiedRatio.setStatus("mandatory")


class _FddimibMACNotCopiedFlag_Type(Integer32):
    """Custom type fddimibMACNotCopiedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibMACNotCopiedFlag_Type.__name__ = "Integer32"
_FddimibMACNotCopiedFlag_Object = MibTableColumn
fddimibMACNotCopiedFlag = _FddimibMACNotCopiedFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 7),
    _FddimibMACNotCopiedFlag_Type()
)
fddimibMACNotCopiedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibMACNotCopiedFlag.setStatus("mandatory")


class _FddimibMACNotCopiedThreshold_Type(Integer32):
    """Custom type fddimibMACNotCopiedThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibMACNotCopiedThreshold_Type.__name__ = "Integer32"
_FddimibMACNotCopiedThreshold_Object = MibTableColumn
fddimibMACNotCopiedThreshold = _FddimibMACNotCopiedThreshold_Object(
    (1, 3, 6, 1, 3, 8, 73, 3, 1, 1, 8),
    _FddimibMACNotCopiedThreshold_Type()
)
fddimibMACNotCopiedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibMACNotCopiedThreshold.setStatus("mandatory")
_FddimibPATH_ObjectIdentity = ObjectIdentity
fddimibPATH = _FddimibPATH_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73, 4)
)


class _FddimibPATHNumber_Type(Integer32):
    """Custom type fddimibPATHNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibPATHNumber_Type.__name__ = "Integer32"
_FddimibPATHNumber_Object = MibScalar
fddimibPATHNumber = _FddimibPATHNumber_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 1),
    _FddimibPATHNumber_Type()
)
fddimibPATHNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHNumber.setStatus("mandatory")
_FddimibPATHTable_Object = MibTable
fddimibPATHTable = _FddimibPATHTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2)
)
if mibBuilder.loadTexts:
    fddimibPATHTable.setStatus("mandatory")
_FddimibPATHEntry_Object = MibTableRow
fddimibPATHEntry = _FddimibPATHEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1)
)
fddimibPATHEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPATHSMTIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPATHIndex"),
)
if mibBuilder.loadTexts:
    fddimibPATHEntry.setStatus("mandatory")


class _FddimibPATHSMTIndex_Type(Integer32):
    """Custom type fddimibPATHSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPATHSMTIndex_Type.__name__ = "Integer32"
_FddimibPATHSMTIndex_Object = MibTableColumn
fddimibPATHSMTIndex = _FddimibPATHSMTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1, 1),
    _FddimibPATHSMTIndex_Type()
)
fddimibPATHSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHSMTIndex.setStatus("mandatory")


class _FddimibPATHIndex_Type(Integer32):
    """Custom type fddimibPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibPATHIndex_Type.__name__ = "Integer32"
_FddimibPATHIndex_Object = MibTableColumn
fddimibPATHIndex = _FddimibPATHIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1, 2),
    _FddimibPATHIndex_Type()
)
fddimibPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHIndex.setStatus("mandatory")
_FddimibPATHTVXLowerBound_Type = FddiTimeNano
_FddimibPATHTVXLowerBound_Object = MibTableColumn
fddimibPATHTVXLowerBound = _FddimibPATHTVXLowerBound_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1, 3),
    _FddimibPATHTVXLowerBound_Type()
)
fddimibPATHTVXLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPATHTVXLowerBound.setStatus("mandatory")
_FddimibPATHTMaxLowerBound_Type = FddiTimeNano
_FddimibPATHTMaxLowerBound_Object = MibTableColumn
fddimibPATHTMaxLowerBound = _FddimibPATHTMaxLowerBound_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1, 4),
    _FddimibPATHTMaxLowerBound_Type()
)
fddimibPATHTMaxLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPATHTMaxLowerBound.setStatus("mandatory")
_FddimibPATHMaxTReq_Type = FddiTimeNano
_FddimibPATHMaxTReq_Object = MibTableColumn
fddimibPATHMaxTReq = _FddimibPATHMaxTReq_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 2, 1, 5),
    _FddimibPATHMaxTReq_Type()
)
fddimibPATHMaxTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPATHMaxTReq.setStatus("mandatory")
_FddimibPATHConfigTable_Object = MibTable
fddimibPATHConfigTable = _FddimibPATHConfigTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3)
)
if mibBuilder.loadTexts:
    fddimibPATHConfigTable.setStatus("mandatory")
_FddimibPATHConfigEntry_Object = MibTableRow
fddimibPATHConfigEntry = _FddimibPATHConfigEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1)
)
fddimibPATHConfigEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPATHConfigSMTIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPATHConfigPATHIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPATHConfigTokenOrder"),
)
if mibBuilder.loadTexts:
    fddimibPATHConfigEntry.setStatus("mandatory")


class _FddimibPATHConfigSMTIndex_Type(Integer32):
    """Custom type fddimibPATHConfigSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPATHConfigSMTIndex_Type.__name__ = "Integer32"
_FddimibPATHConfigSMTIndex_Object = MibTableColumn
fddimibPATHConfigSMTIndex = _FddimibPATHConfigSMTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 1),
    _FddimibPATHConfigSMTIndex_Type()
)
fddimibPATHConfigSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigSMTIndex.setStatus("mandatory")


class _FddimibPATHConfigPATHIndex_Type(Integer32):
    """Custom type fddimibPATHConfigPATHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPATHConfigPATHIndex_Type.__name__ = "Integer32"
_FddimibPATHConfigPATHIndex_Object = MibTableColumn
fddimibPATHConfigPATHIndex = _FddimibPATHConfigPATHIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 2),
    _FddimibPATHConfigPATHIndex_Type()
)
fddimibPATHConfigPATHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigPATHIndex.setStatus("mandatory")


class _FddimibPATHConfigTokenOrder_Type(Integer32):
    """Custom type fddimibPATHConfigTokenOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPATHConfigTokenOrder_Type.__name__ = "Integer32"
_FddimibPATHConfigTokenOrder_Object = MibTableColumn
fddimibPATHConfigTokenOrder = _FddimibPATHConfigTokenOrder_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 3),
    _FddimibPATHConfigTokenOrder_Type()
)
fddimibPATHConfigTokenOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigTokenOrder.setStatus("mandatory")


class _FddimibPATHConfigResourceType_Type(Integer32):
    """Custom type fddimibPATHConfigResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mac", 2),
          ("port", 4))
    )


_FddimibPATHConfigResourceType_Type.__name__ = "Integer32"
_FddimibPATHConfigResourceType_Object = MibTableColumn
fddimibPATHConfigResourceType = _FddimibPATHConfigResourceType_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 4),
    _FddimibPATHConfigResourceType_Type()
)
fddimibPATHConfigResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigResourceType.setStatus("mandatory")


class _FddimibPATHConfigResourceIndex_Type(Integer32):
    """Custom type fddimibPATHConfigResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPATHConfigResourceIndex_Type.__name__ = "Integer32"
_FddimibPATHConfigResourceIndex_Object = MibTableColumn
fddimibPATHConfigResourceIndex = _FddimibPATHConfigResourceIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 5),
    _FddimibPATHConfigResourceIndex_Type()
)
fddimibPATHConfigResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigResourceIndex.setStatus("mandatory")


class _FddimibPATHConfigCurrentPath_Type(Integer32):
    """Custom type fddimibPATHConfigCurrentPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("concatenated", 5),
          ("isolated", 1),
          ("local", 2),
          ("primary", 4),
          ("secondary", 3),
          ("thru", 6))
    )


_FddimibPATHConfigCurrentPath_Type.__name__ = "Integer32"
_FddimibPATHConfigCurrentPath_Object = MibTableColumn
fddimibPATHConfigCurrentPath = _FddimibPATHConfigCurrentPath_Object(
    (1, 3, 6, 1, 3, 8, 73, 4, 3, 1, 6),
    _FddimibPATHConfigCurrentPath_Type()
)
fddimibPATHConfigCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPATHConfigCurrentPath.setStatus("mandatory")
_FddimibPORT_ObjectIdentity = ObjectIdentity
fddimibPORT = _FddimibPORT_ObjectIdentity(
    (1, 3, 6, 1, 3, 8, 73, 5)
)


class _FddimibPORTNumber_Type(Integer32):
    """Custom type fddimibPORTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FddimibPORTNumber_Type.__name__ = "Integer32"
_FddimibPORTNumber_Object = MibScalar
fddimibPORTNumber = _FddimibPORTNumber_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 1),
    _FddimibPORTNumber_Type()
)
fddimibPORTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTNumber.setStatus("mandatory")
_FddimibPORTTable_Object = MibTable
fddimibPORTTable = _FddimibPORTTable_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2)
)
if mibBuilder.loadTexts:
    fddimibPORTTable.setStatus("mandatory")
_FddimibPORTEntry_Object = MibTableRow
fddimibPORTEntry = _FddimibPORTEntry_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1)
)
fddimibPORTEntry.setIndexNames(
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTSMTIndex"),
    (0, "DRAFT-FDDI-MIB-VER-3-2", "fddimibPORTIndex"),
)
if mibBuilder.loadTexts:
    fddimibPORTEntry.setStatus("mandatory")


class _FddimibPORTSMTIndex_Type(Integer32):
    """Custom type fddimibPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPORTSMTIndex_Type.__name__ = "Integer32"
_FddimibPORTSMTIndex_Object = MibTableColumn
fddimibPORTSMTIndex = _FddimibPORTSMTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 1),
    _FddimibPORTSMTIndex_Type()
)
fddimibPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTSMTIndex.setStatus("mandatory")


class _FddimibPORTIndex_Type(Integer32):
    """Custom type fddimibPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FddimibPORTIndex_Type.__name__ = "Integer32"
_FddimibPORTIndex_Object = MibTableColumn
fddimibPORTIndex = _FddimibPORTIndex_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 2),
    _FddimibPORTIndex_Type()
)
fddimibPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTIndex.setStatus("mandatory")


class _FddimibPORTMyType_Type(Integer32):
    """Custom type fddimibPORTMyType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("none", 5),
          ("s", 3))
    )


_FddimibPORTMyType_Type.__name__ = "Integer32"
_FddimibPORTMyType_Object = MibTableColumn
fddimibPORTMyType = _FddimibPORTMyType_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 3),
    _FddimibPORTMyType_Type()
)
fddimibPORTMyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTMyType.setStatus("mandatory")


class _FddimibPORTNeighborType_Type(Integer32):
    """Custom type fddimibPORTNeighborType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("none", 5),
          ("s", 3))
    )


_FddimibPORTNeighborType_Type.__name__ = "Integer32"
_FddimibPORTNeighborType_Object = MibTableColumn
fddimibPORTNeighborType = _FddimibPORTNeighborType_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 4),
    _FddimibPORTNeighborType_Type()
)
fddimibPORTNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTNeighborType.setStatus("mandatory")


class _FddimibPORTConnectionPolicies_Type(Integer32):
    """Custom type fddimibPORTConnectionPolicies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FddimibPORTConnectionPolicies_Type.__name__ = "Integer32"
_FddimibPORTConnectionPolicies_Object = MibTableColumn
fddimibPORTConnectionPolicies = _FddimibPORTConnectionPolicies_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 5),
    _FddimibPORTConnectionPolicies_Type()
)
fddimibPORTConnectionPolicies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPORTConnectionPolicies.setStatus("mandatory")


class _FddimibPORTMACIndicated_Type(Integer32):
    """Custom type fddimibPORTMACIndicated based on Integer32"""
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
        *(("tVal9FalseRVal9False", 1),
          ("tVal9FalseRVal9True", 2),
          ("tVal9TrueRVal9False", 3),
          ("tVal9TrueRVal9True", 4))
    )


_FddimibPORTMACIndicated_Type.__name__ = "Integer32"
_FddimibPORTMACIndicated_Object = MibTableColumn
fddimibPORTMACIndicated = _FddimibPORTMACIndicated_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 6),
    _FddimibPORTMACIndicated_Type()
)
fddimibPORTMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTMACIndicated.setStatus("mandatory")


class _FddimibPORTCurrentPath_Type(Integer32):
    """Custom type fddimibPORTCurrentPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ce0", 1),
          ("ce1", 2),
          ("ce2", 3),
          ("ce3", 4),
          ("ce4", 5),
          ("ce5", 6))
    )


_FddimibPORTCurrentPath_Type.__name__ = "Integer32"
_FddimibPORTCurrentPath_Object = MibTableColumn
fddimibPORTCurrentPath = _FddimibPORTCurrentPath_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 7),
    _FddimibPORTCurrentPath_Type()
)
fddimibPORTCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTCurrentPath.setStatus("mandatory")


class _FddimibPORTRequestedPaths_Type(OctetString):
    """Custom type fddimibPORTRequestedPaths based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_FddimibPORTRequestedPaths_Type.__name__ = "OctetString"
_FddimibPORTRequestedPaths_Object = MibTableColumn
fddimibPORTRequestedPaths = _FddimibPORTRequestedPaths_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 8),
    _FddimibPORTRequestedPaths_Type()
)
fddimibPORTRequestedPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPORTRequestedPaths.setStatus("mandatory")
_FddimibPORTMACPlacement_Type = FddiResourceId
_FddimibPORTMACPlacement_Object = MibTableColumn
fddimibPORTMACPlacement = _FddimibPORTMACPlacement_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 9),
    _FddimibPORTMACPlacement_Type()
)
fddimibPORTMACPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTMACPlacement.setStatus("mandatory")


class _FddimibPORTAvailablePaths_Type(Integer32):
    """Custom type fddimibPORTAvailablePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FddimibPORTAvailablePaths_Type.__name__ = "Integer32"
_FddimibPORTAvailablePaths_Object = MibTableColumn
fddimibPORTAvailablePaths = _FddimibPORTAvailablePaths_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 10),
    _FddimibPORTAvailablePaths_Type()
)
fddimibPORTAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTAvailablePaths.setStatus("mandatory")


class _FddimibPORTPMDClass_Type(Integer32):
    """Custom type fddimibPORTPMDClass based on Integer32"""
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
        *(("low-cost-fiber", 5),
          ("multimode", 1),
          ("single-mode1", 2),
          ("single-mode2", 3),
          ("sonet", 4),
          ("twisted-pair", 6),
          ("unknown", 7),
          ("unspecified", 8))
    )


_FddimibPORTPMDClass_Type.__name__ = "Integer32"
_FddimibPORTPMDClass_Object = MibTableColumn
fddimibPORTPMDClass = _FddimibPORTPMDClass_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 11),
    _FddimibPORTPMDClass_Type()
)
fddimibPORTPMDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTPMDClass.setStatus("mandatory")


class _FddimibPORTConnectionCapabilities_Type(Integer32):
    """Custom type fddimibPORTConnectionCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FddimibPORTConnectionCapabilities_Type.__name__ = "Integer32"
_FddimibPORTConnectionCapabilities_Object = MibTableColumn
fddimibPORTConnectionCapabilities = _FddimibPORTConnectionCapabilities_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 12),
    _FddimibPORTConnectionCapabilities_Type()
)
fddimibPORTConnectionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTConnectionCapabilities.setStatus("mandatory")


class _FddimibPORTBSFlag_Type(Integer32):
    """Custom type fddimibPORTBSFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibPORTBSFlag_Type.__name__ = "Integer32"
_FddimibPORTBSFlag_Object = MibTableColumn
fddimibPORTBSFlag = _FddimibPORTBSFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 13),
    _FddimibPORTBSFlag_Type()
)
fddimibPORTBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTBSFlag.setStatus("mandatory")
_FddimibPORTLCTFailCts_Type = Counter32
_FddimibPORTLCTFailCts_Object = MibTableColumn
fddimibPORTLCTFailCts = _FddimibPORTLCTFailCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 14),
    _FddimibPORTLCTFailCts_Type()
)
fddimibPORTLCTFailCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTLCTFailCts.setStatus("mandatory")


class _FddimibPORTLerEstimate_Type(Integer32):
    """Custom type fddimibPORTLerEstimate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_FddimibPORTLerEstimate_Type.__name__ = "Integer32"
_FddimibPORTLerEstimate_Object = MibTableColumn
fddimibPORTLerEstimate = _FddimibPORTLerEstimate_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 15),
    _FddimibPORTLerEstimate_Type()
)
fddimibPORTLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTLerEstimate.setStatus("mandatory")
_FddimibPORTLemRejectCts_Type = Counter32
_FddimibPORTLemRejectCts_Object = MibTableColumn
fddimibPORTLemRejectCts = _FddimibPORTLemRejectCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 16),
    _FddimibPORTLemRejectCts_Type()
)
fddimibPORTLemRejectCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTLemRejectCts.setStatus("mandatory")
_FddimibPORTLemCts_Type = Counter32
_FddimibPORTLemCts_Object = MibTableColumn
fddimibPORTLemCts = _FddimibPORTLemCts_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 17),
    _FddimibPORTLemCts_Type()
)
fddimibPORTLemCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTLemCts.setStatus("mandatory")


class _FddimibPORTLerCutoff_Type(Integer32):
    """Custom type fddimibPORTLerCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_FddimibPORTLerCutoff_Type.__name__ = "Integer32"
_FddimibPORTLerCutoff_Object = MibTableColumn
fddimibPORTLerCutoff = _FddimibPORTLerCutoff_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 18),
    _FddimibPORTLerCutoff_Type()
)
fddimibPORTLerCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPORTLerCutoff.setStatus("mandatory")


class _FddimibPORTLerAlarm_Type(Integer32):
    """Custom type fddimibPORTLerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_FddimibPORTLerAlarm_Type.__name__ = "Integer32"
_FddimibPORTLerAlarm_Object = MibTableColumn
fddimibPORTLerAlarm = _FddimibPORTLerAlarm_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 19),
    _FddimibPORTLerAlarm_Type()
)
fddimibPORTLerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPORTLerAlarm.setStatus("mandatory")


class _FddimibPORTConnectState_Type(Integer32):
    """Custom type fddimibPORTConnectState based on Integer32"""
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
        *(("active", 4),
          ("connecting", 2),
          ("disabled", 1),
          ("standby", 3))
    )


_FddimibPORTConnectState_Type.__name__ = "Integer32"
_FddimibPORTConnectState_Object = MibTableColumn
fddimibPORTConnectState = _FddimibPORTConnectState_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 20),
    _FddimibPORTConnectState_Type()
)
fddimibPORTConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTConnectState.setStatus("mandatory")


class _FddimibPORTPCMState_Type(Integer32):
    """Custom type fddimibPORTPCMState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("pc0", 1),
          ("pc1", 2),
          ("pc2", 3),
          ("pc3", 4),
          ("pc4", 5),
          ("pc5", 6),
          ("pc6", 7),
          ("pc7", 8),
          ("pc8", 9),
          ("pc9", 10))
    )


_FddimibPORTPCMState_Type.__name__ = "Integer32"
_FddimibPORTPCMState_Object = MibTableColumn
fddimibPORTPCMState = _FddimibPORTPCMState_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 21),
    _FddimibPORTPCMState_Type()
)
fddimibPORTPCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTPCMState.setStatus("mandatory")


class _FddimibPORTPCWithhold_Type(Integer32):
    """Custom type fddimibPORTPCWithhold based on Integer32"""
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
        *(("m-m", 2),
          ("none", 1),
          ("otherincompatible", 3),
          ("pathnotavailable", 4))
    )


_FddimibPORTPCWithhold_Type.__name__ = "Integer32"
_FddimibPORTPCWithhold_Object = MibTableColumn
fddimibPORTPCWithhold = _FddimibPORTPCWithhold_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 22),
    _FddimibPORTPCWithhold_Type()
)
fddimibPORTPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTPCWithhold.setStatus("mandatory")


class _FddimibPORTLerFlag_Type(Integer32):
    """Custom type fddimibPORTLerFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibPORTLerFlag_Type.__name__ = "Integer32"
_FddimibPORTLerFlag_Object = MibTableColumn
fddimibPORTLerFlag = _FddimibPORTLerFlag_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 23),
    _FddimibPORTLerFlag_Type()
)
fddimibPORTLerFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTLerFlag.setStatus("mandatory")


class _FddimibPORTHardwarePresent_Type(Integer32):
    """Custom type fddimibPORTHardwarePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_FddimibPORTHardwarePresent_Type.__name__ = "Integer32"
_FddimibPORTHardwarePresent_Object = MibTableColumn
fddimibPORTHardwarePresent = _FddimibPORTHardwarePresent_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 24),
    _FddimibPORTHardwarePresent_Type()
)
fddimibPORTHardwarePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fddimibPORTHardwarePresent.setStatus("mandatory")


class _FddimibPORTAction_Type(Integer32):
    """Custom type fddimibPORTAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disablePORT", 4),
          ("enablePORT", 3),
          ("maintPORT", 2),
          ("other", 1),
          ("startPORT", 5),
          ("stopPORT", 6))
    )


_FddimibPORTAction_Type.__name__ = "Integer32"
_FddimibPORTAction_Object = MibTableColumn
fddimibPORTAction = _FddimibPORTAction_Object(
    (1, 3, 6, 1, 3, 8, 73, 5, 2, 1, 25),
    _FddimibPORTAction_Type()
)
fddimibPORTAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fddimibPORTAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAFT-FDDI-MIB-VER-3-2",
    **{"FddiTimeNano": FddiTimeNano,
       "FddiTimeMilli": FddiTimeMilli,
       "FddiResourceId": FddiResourceId,
       "FddiSMTStationIdType": FddiSMTStationIdType,
       "FddiMACLongAddressType": FddiMACLongAddressType,
       "fddi": fddi,
       "fddimib": fddimib,
       "fddimibSMT": fddimibSMT,
       "fddimibSMTNumber": fddimibSMTNumber,
       "fddimibSMTTable": fddimibSMTTable,
       "fddimibSMTEntry": fddimibSMTEntry,
       "fddimibSMTIndex": fddimibSMTIndex,
       "fddimibSMTStationId": fddimibSMTStationId,
       "fddimibSMTOpVersionId": fddimibSMTOpVersionId,
       "fddimibSMTHiVersionId": fddimibSMTHiVersionId,
       "fddimibSMTLoVersionId": fddimibSMTLoVersionId,
       "fddimibSMTUserData": fddimibSMTUserData,
       "fddimibSMTMIBVersionId": fddimibSMTMIBVersionId,
       "fddimibSMTMACCts": fddimibSMTMACCts,
       "fddimibSMTNonMasterCts": fddimibSMTNonMasterCts,
       "fddimibSMTMasterCts": fddimibSMTMasterCts,
       "fddimibSMTAvailablePaths": fddimibSMTAvailablePaths,
       "fddimibSMTConfigCapabilities": fddimibSMTConfigCapabilities,
       "fddimibSMTConfigPolicy": fddimibSMTConfigPolicy,
       "fddimibSMTConnectionPolicy": fddimibSMTConnectionPolicy,
       "fddimibSMTTNotify": fddimibSMTTNotify,
       "fddimibSMTStatRptPolicy": fddimibSMTStatRptPolicy,
       "fddimibSMTTraceMaxExpiration": fddimibSMTTraceMaxExpiration,
       "fddimibSMTBypassPresent": fddimibSMTBypassPresent,
       "fddimibSMTECMState": fddimibSMTECMState,
       "fddimibSMTCFState": fddimibSMTCFState,
       "fddimibSMTRemoteDisconnectFlag": fddimibSMTRemoteDisconnectFlag,
       "fddimibSMTStationStatus": fddimibSMTStationStatus,
       "fddimibSMTPeerWrapFlag": fddimibSMTPeerWrapFlag,
       "fddimibSMTTimeStamp": fddimibSMTTimeStamp,
       "fddimibSMTTransitionTimeStamp": fddimibSMTTransitionTimeStamp,
       "fddimibSMTStationAction": fddimibSMTStationAction,
       "fddimibMAC": fddimibMAC,
       "fddimibMACNumber": fddimibMACNumber,
       "fddimibMACTable": fddimibMACTable,
       "fddimibMACEntry": fddimibMACEntry,
       "fddimibMACSMTIndex": fddimibMACSMTIndex,
       "fddimibMACIndex": fddimibMACIndex,
       "fddimibMACIfIndex": fddimibMACIfIndex,
       "fddimibMACFrameStatusFunctions": fddimibMACFrameStatusFunctions,
       "fddimibMACTMaxCapability": fddimibMACTMaxCapability,
       "fddimibMACTVXCapability": fddimibMACTVXCapability,
       "fddimibMACAvailablePaths": fddimibMACAvailablePaths,
       "fddimibMACCurrentPath": fddimibMACCurrentPath,
       "fddimibMACUpstreamNbr": fddimibMACUpstreamNbr,
       "fddimibMACDownstreamNbr": fddimibMACDownstreamNbr,
       "fddimibMACOldUpstreamNbr": fddimibMACOldUpstreamNbr,
       "fddimibMACOldDownstreamNbr": fddimibMACOldDownstreamNbr,
       "fddimibMACDupAddressTest": fddimibMACDupAddressTest,
       "fddimibMACRequestedPaths": fddimibMACRequestedPaths,
       "fddimibMACDownstreamPORTType": fddimibMACDownstreamPORTType,
       "fddimibMACSMTAddress": fddimibMACSMTAddress,
       "fddimibMACTReq": fddimibMACTReq,
       "fddimibMACTNeg": fddimibMACTNeg,
       "fddimibMACTMax": fddimibMACTMax,
       "fddimibMACTvxValue": fddimibMACTvxValue,
       "fddimibMACFrameCts": fddimibMACFrameCts,
       "fddimibMACCopiedCts": fddimibMACCopiedCts,
       "fddimibMACTransmitCts": fddimibMACTransmitCts,
       "fddimibMACErrorCts": fddimibMACErrorCts,
       "fddimibMACLostCts": fddimibMACLostCts,
       "fddimibMACFrameErrorThreshold": fddimibMACFrameErrorThreshold,
       "fddimibMACFrameErrorRatio": fddimibMACFrameErrorRatio,
       "fddimibMACRMTState": fddimibMACRMTState,
       "fddimibMACDaFlag": fddimibMACDaFlag,
       "fddimibMACUnaDaFlag": fddimibMACUnaDaFlag,
       "fddimibMACFrameErrorFlag": fddimibMACFrameErrorFlag,
       "fddimibMACMAUnitdataAvailable": fddimibMACMAUnitdataAvailable,
       "fddimibMACHardwarePresent": fddimibMACHardwarePresent,
       "fddimibMACMAUnitdataEnable": fddimibMACMAUnitdataEnable,
       "fddimibMACCounters": fddimibMACCounters,
       "fddimibMACCountersTable": fddimibMACCountersTable,
       "fddimibMACCountersEntry": fddimibMACCountersEntry,
       "fddimibMACTokenCts": fddimibMACTokenCts,
       "fddimibMACTvxExpiredCts": fddimibMACTvxExpiredCts,
       "fddimibMACNotCopiedCts": fddimibMACNotCopiedCts,
       "fddimibMACLateCts": fddimibMACLateCts,
       "fddimibMACRingOpCts": fddimibMACRingOpCts,
       "fddimibMACNotCopiedRatio": fddimibMACNotCopiedRatio,
       "fddimibMACNotCopiedFlag": fddimibMACNotCopiedFlag,
       "fddimibMACNotCopiedThreshold": fddimibMACNotCopiedThreshold,
       "fddimibPATH": fddimibPATH,
       "fddimibPATHNumber": fddimibPATHNumber,
       "fddimibPATHTable": fddimibPATHTable,
       "fddimibPATHEntry": fddimibPATHEntry,
       "fddimibPATHSMTIndex": fddimibPATHSMTIndex,
       "fddimibPATHIndex": fddimibPATHIndex,
       "fddimibPATHTVXLowerBound": fddimibPATHTVXLowerBound,
       "fddimibPATHTMaxLowerBound": fddimibPATHTMaxLowerBound,
       "fddimibPATHMaxTReq": fddimibPATHMaxTReq,
       "fddimibPATHConfigTable": fddimibPATHConfigTable,
       "fddimibPATHConfigEntry": fddimibPATHConfigEntry,
       "fddimibPATHConfigSMTIndex": fddimibPATHConfigSMTIndex,
       "fddimibPATHConfigPATHIndex": fddimibPATHConfigPATHIndex,
       "fddimibPATHConfigTokenOrder": fddimibPATHConfigTokenOrder,
       "fddimibPATHConfigResourceType": fddimibPATHConfigResourceType,
       "fddimibPATHConfigResourceIndex": fddimibPATHConfigResourceIndex,
       "fddimibPATHConfigCurrentPath": fddimibPATHConfigCurrentPath,
       "fddimibPORT": fddimibPORT,
       "fddimibPORTNumber": fddimibPORTNumber,
       "fddimibPORTTable": fddimibPORTTable,
       "fddimibPORTEntry": fddimibPORTEntry,
       "fddimibPORTSMTIndex": fddimibPORTSMTIndex,
       "fddimibPORTIndex": fddimibPORTIndex,
       "fddimibPORTMyType": fddimibPORTMyType,
       "fddimibPORTNeighborType": fddimibPORTNeighborType,
       "fddimibPORTConnectionPolicies": fddimibPORTConnectionPolicies,
       "fddimibPORTMACIndicated": fddimibPORTMACIndicated,
       "fddimibPORTCurrentPath": fddimibPORTCurrentPath,
       "fddimibPORTRequestedPaths": fddimibPORTRequestedPaths,
       "fddimibPORTMACPlacement": fddimibPORTMACPlacement,
       "fddimibPORTAvailablePaths": fddimibPORTAvailablePaths,
       "fddimibPORTPMDClass": fddimibPORTPMDClass,
       "fddimibPORTConnectionCapabilities": fddimibPORTConnectionCapabilities,
       "fddimibPORTBSFlag": fddimibPORTBSFlag,
       "fddimibPORTLCTFailCts": fddimibPORTLCTFailCts,
       "fddimibPORTLerEstimate": fddimibPORTLerEstimate,
       "fddimibPORTLemRejectCts": fddimibPORTLemRejectCts,
       "fddimibPORTLemCts": fddimibPORTLemCts,
       "fddimibPORTLerCutoff": fddimibPORTLerCutoff,
       "fddimibPORTLerAlarm": fddimibPORTLerAlarm,
       "fddimibPORTConnectState": fddimibPORTConnectState,
       "fddimibPORTPCMState": fddimibPORTPCMState,
       "fddimibPORTPCWithhold": fddimibPORTPCWithhold,
       "fddimibPORTLerFlag": fddimibPORTLerFlag,
       "fddimibPORTHardwarePresent": fddimibPORTHardwarePresent,
       "fddimibPORTAction": fddimibPORTAction}
)
