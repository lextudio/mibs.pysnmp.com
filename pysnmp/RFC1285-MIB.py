# SNMP MIB module (RFC1285-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1285-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:18 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class FddiTime(Integer32):
    """Custom type FddiTime based on Integer32"""
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
    (1, 3, 6, 1, 2, 1, 10, 15)
)
_SnmpFddiSMT_ObjectIdentity = ObjectIdentity
snmpFddiSMT = _SnmpFddiSMT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 1)
)


class _SnmpFddiSMTNumber_Type(Integer32):
    """Custom type snmpFddiSMTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpFddiSMTNumber_Type.__name__ = "Integer32"
_SnmpFddiSMTNumber_Object = MibScalar
snmpFddiSMTNumber = _SnmpFddiSMTNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 1),
    _SnmpFddiSMTNumber_Type()
)
snmpFddiSMTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTNumber.setStatus("mandatory")
_SnmpFddiSMTTable_Object = MibTable
snmpFddiSMTTable = _SnmpFddiSMTTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2)
)
if mibBuilder.loadTexts:
    snmpFddiSMTTable.setStatus("mandatory")
_SnmpFddiSMTEntry_Object = MibTableRow
snmpFddiSMTEntry = _SnmpFddiSMTEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1)
)
snmpFddiSMTEntry.setIndexNames(
    (0, "RFC1285-MIB", "snmpFddiSMTIndex"),
)
if mibBuilder.loadTexts:
    snmpFddiSMTEntry.setStatus("mandatory")


class _SnmpFddiSMTIndex_Type(Integer32):
    """Custom type snmpFddiSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiSMTIndex_Type.__name__ = "Integer32"
_SnmpFddiSMTIndex_Object = MibTableColumn
snmpFddiSMTIndex = _SnmpFddiSMTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 1),
    _SnmpFddiSMTIndex_Type()
)
snmpFddiSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTIndex.setStatus("mandatory")
_SnmpFddiSMTStationId_Type = FddiSMTStationIdType
_SnmpFddiSMTStationId_Object = MibTableColumn
snmpFddiSMTStationId = _SnmpFddiSMTStationId_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 2),
    _SnmpFddiSMTStationId_Type()
)
snmpFddiSMTStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTStationId.setStatus("mandatory")


class _SnmpFddiSMTOpVersionId_Type(Integer32):
    """Custom type snmpFddiSMTOpVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiSMTOpVersionId_Type.__name__ = "Integer32"
_SnmpFddiSMTOpVersionId_Object = MibTableColumn
snmpFddiSMTOpVersionId = _SnmpFddiSMTOpVersionId_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 3),
    _SnmpFddiSMTOpVersionId_Type()
)
snmpFddiSMTOpVersionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiSMTOpVersionId.setStatus("mandatory")


class _SnmpFddiSMTHiVersionId_Type(Integer32):
    """Custom type snmpFddiSMTHiVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiSMTHiVersionId_Type.__name__ = "Integer32"
_SnmpFddiSMTHiVersionId_Object = MibTableColumn
snmpFddiSMTHiVersionId = _SnmpFddiSMTHiVersionId_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 4),
    _SnmpFddiSMTHiVersionId_Type()
)
snmpFddiSMTHiVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTHiVersionId.setStatus("mandatory")


class _SnmpFddiSMTLoVersionId_Type(Integer32):
    """Custom type snmpFddiSMTLoVersionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiSMTLoVersionId_Type.__name__ = "Integer32"
_SnmpFddiSMTLoVersionId_Object = MibTableColumn
snmpFddiSMTLoVersionId = _SnmpFddiSMTLoVersionId_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 5),
    _SnmpFddiSMTLoVersionId_Type()
)
snmpFddiSMTLoVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTLoVersionId.setStatus("mandatory")


class _SnmpFddiSMTMACCt_Type(Integer32):
    """Custom type snmpFddiSMTMACCt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpFddiSMTMACCt_Type.__name__ = "Integer32"
_SnmpFddiSMTMACCt_Object = MibTableColumn
snmpFddiSMTMACCt = _SnmpFddiSMTMACCt_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 6),
    _SnmpFddiSMTMACCt_Type()
)
snmpFddiSMTMACCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTMACCt.setStatus("mandatory")


class _SnmpFddiSMTNonMasterCt_Type(Integer32):
    """Custom type snmpFddiSMTNonMasterCt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SnmpFddiSMTNonMasterCt_Type.__name__ = "Integer32"
_SnmpFddiSMTNonMasterCt_Object = MibTableColumn
snmpFddiSMTNonMasterCt = _SnmpFddiSMTNonMasterCt_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 7),
    _SnmpFddiSMTNonMasterCt_Type()
)
snmpFddiSMTNonMasterCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTNonMasterCt.setStatus("mandatory")


class _SnmpFddiSMTMasterCt_Type(Integer32):
    """Custom type snmpFddiSMTMasterCt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpFddiSMTMasterCt_Type.__name__ = "Integer32"
_SnmpFddiSMTMasterCt_Object = MibTableColumn
snmpFddiSMTMasterCt = _SnmpFddiSMTMasterCt_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 8),
    _SnmpFddiSMTMasterCt_Type()
)
snmpFddiSMTMasterCt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTMasterCt.setStatus("mandatory")


class _SnmpFddiSMTPathsAvailable_Type(Integer32):
    """Custom type snmpFddiSMTPathsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpFddiSMTPathsAvailable_Type.__name__ = "Integer32"
_SnmpFddiSMTPathsAvailable_Object = MibTableColumn
snmpFddiSMTPathsAvailable = _SnmpFddiSMTPathsAvailable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 9),
    _SnmpFddiSMTPathsAvailable_Type()
)
snmpFddiSMTPathsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTPathsAvailable.setStatus("mandatory")


class _SnmpFddiSMTConfigCapabilities_Type(Integer32):
    """Custom type snmpFddiSMTConfigCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnmpFddiSMTConfigCapabilities_Type.__name__ = "Integer32"
_SnmpFddiSMTConfigCapabilities_Object = MibTableColumn
snmpFddiSMTConfigCapabilities = _SnmpFddiSMTConfigCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 10),
    _SnmpFddiSMTConfigCapabilities_Type()
)
snmpFddiSMTConfigCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTConfigCapabilities.setStatus("mandatory")


class _SnmpFddiSMTConfigPolicy_Type(Integer32):
    """Custom type snmpFddiSMTConfigPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SnmpFddiSMTConfigPolicy_Type.__name__ = "Integer32"
_SnmpFddiSMTConfigPolicy_Object = MibTableColumn
snmpFddiSMTConfigPolicy = _SnmpFddiSMTConfigPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 11),
    _SnmpFddiSMTConfigPolicy_Type()
)
snmpFddiSMTConfigPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiSMTConfigPolicy.setStatus("mandatory")


class _SnmpFddiSMTConnectionPolicy_Type(Integer32):
    """Custom type snmpFddiSMTConnectionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpFddiSMTConnectionPolicy_Type.__name__ = "Integer32"
_SnmpFddiSMTConnectionPolicy_Object = MibTableColumn
snmpFddiSMTConnectionPolicy = _SnmpFddiSMTConnectionPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 12),
    _SnmpFddiSMTConnectionPolicy_Type()
)
snmpFddiSMTConnectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiSMTConnectionPolicy.setStatus("mandatory")


class _SnmpFddiSMTTNotify_Type(Integer32):
    """Custom type snmpFddiSMTTNotify based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_SnmpFddiSMTTNotify_Type.__name__ = "Integer32"
_SnmpFddiSMTTNotify_Object = MibTableColumn
snmpFddiSMTTNotify = _SnmpFddiSMTTNotify_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 13),
    _SnmpFddiSMTTNotify_Type()
)
snmpFddiSMTTNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiSMTTNotify.setStatus("mandatory")


class _SnmpFddiSMTStatusReporting_Type(Integer32):
    """Custom type snmpFddiSMTStatusReporting based on Integer32"""
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


_SnmpFddiSMTStatusReporting_Type.__name__ = "Integer32"
_SnmpFddiSMTStatusReporting_Object = MibTableColumn
snmpFddiSMTStatusReporting = _SnmpFddiSMTStatusReporting_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 14),
    _SnmpFddiSMTStatusReporting_Type()
)
snmpFddiSMTStatusReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTStatusReporting.setStatus("mandatory")


class _SnmpFddiSMTECMState_Type(Integer32):
    """Custom type snmpFddiSMTECMState based on Integer32"""
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


_SnmpFddiSMTECMState_Type.__name__ = "Integer32"
_SnmpFddiSMTECMState_Object = MibTableColumn
snmpFddiSMTECMState = _SnmpFddiSMTECMState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 15),
    _SnmpFddiSMTECMState_Type()
)
snmpFddiSMTECMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTECMState.setStatus("mandatory")


class _SnmpFddiSMTCFState_Type(Integer32):
    """Custom type snmpFddiSMTCFState based on Integer32"""
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
        *(("cf0", 1),
          ("cf1", 2),
          ("cf2", 3),
          ("cf3", 4),
          ("cf4", 5),
          ("cf5", 6))
    )


_SnmpFddiSMTCFState_Type.__name__ = "Integer32"
_SnmpFddiSMTCFState_Object = MibTableColumn
snmpFddiSMTCFState = _SnmpFddiSMTCFState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 16),
    _SnmpFddiSMTCFState_Type()
)
snmpFddiSMTCFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTCFState.setStatus("mandatory")


class _SnmpFddiSMTHoldState_Type(Integer32):
    """Custom type snmpFddiSMTHoldState based on Integer32"""
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
        *(("holding-prm", 3),
          ("holding-sec", 4),
          ("not-holding", 2),
          ("not-implemented", 1))
    )


_SnmpFddiSMTHoldState_Type.__name__ = "Integer32"
_SnmpFddiSMTHoldState_Object = MibTableColumn
snmpFddiSMTHoldState = _SnmpFddiSMTHoldState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 17),
    _SnmpFddiSMTHoldState_Type()
)
snmpFddiSMTHoldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTHoldState.setStatus("mandatory")


class _SnmpFddiSMTRemoteDisconnectFlag_Type(Integer32):
    """Custom type snmpFddiSMTRemoteDisconnectFlag based on Integer32"""
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


_SnmpFddiSMTRemoteDisconnectFlag_Type.__name__ = "Integer32"
_SnmpFddiSMTRemoteDisconnectFlag_Object = MibTableColumn
snmpFddiSMTRemoteDisconnectFlag = _SnmpFddiSMTRemoteDisconnectFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 18),
    _SnmpFddiSMTRemoteDisconnectFlag_Type()
)
snmpFddiSMTRemoteDisconnectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiSMTRemoteDisconnectFlag.setStatus("mandatory")


class _SnmpFddiSMTStationAction_Type(Integer32):
    """Custom type snmpFddiSMTStationAction based on Integer32"""
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
        *(("connect", 2),
          ("disconnect", 3),
          ("other", 1),
          ("path-Test", 4),
          ("self-Test", 5))
    )


_SnmpFddiSMTStationAction_Type.__name__ = "Integer32"
_SnmpFddiSMTStationAction_Object = MibTableColumn
snmpFddiSMTStationAction = _SnmpFddiSMTStationAction_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 1, 2, 1, 19),
    _SnmpFddiSMTStationAction_Type()
)
snmpFddiSMTStationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiSMTStationAction.setStatus("mandatory")
_SnmpFddiMAC_ObjectIdentity = ObjectIdentity
snmpFddiMAC = _SnmpFddiMAC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 2)
)


class _SnmpFddiMACNumber_Type(Integer32):
    """Custom type snmpFddiMACNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpFddiMACNumber_Type.__name__ = "Integer32"
_SnmpFddiMACNumber_Object = MibScalar
snmpFddiMACNumber = _SnmpFddiMACNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 1),
    _SnmpFddiMACNumber_Type()
)
snmpFddiMACNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACNumber.setStatus("mandatory")
_SnmpFddiMACTable_Object = MibTable
snmpFddiMACTable = _SnmpFddiMACTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2)
)
if mibBuilder.loadTexts:
    snmpFddiMACTable.setStatus("mandatory")
_SnmpFddiMACEntry_Object = MibTableRow
snmpFddiMACEntry = _SnmpFddiMACEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1)
)
snmpFddiMACEntry.setIndexNames(
    (0, "RFC1285-MIB", "snmpFddiMACSMTIndex"),
    (0, "RFC1285-MIB", "snmpFddiMACIndex"),
)
if mibBuilder.loadTexts:
    snmpFddiMACEntry.setStatus("mandatory")


class _SnmpFddiMACSMTIndex_Type(Integer32):
    """Custom type snmpFddiMACSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiMACSMTIndex_Type.__name__ = "Integer32"
_SnmpFddiMACSMTIndex_Object = MibTableColumn
snmpFddiMACSMTIndex = _SnmpFddiMACSMTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 1),
    _SnmpFddiMACSMTIndex_Type()
)
snmpFddiMACSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACSMTIndex.setStatus("mandatory")


class _SnmpFddiMACIndex_Type(Integer32):
    """Custom type snmpFddiMACIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiMACIndex_Type.__name__ = "Integer32"
_SnmpFddiMACIndex_Object = MibTableColumn
snmpFddiMACIndex = _SnmpFddiMACIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 2),
    _SnmpFddiMACIndex_Type()
)
snmpFddiMACIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACIndex.setStatus("mandatory")


class _SnmpFddiMACFrameStatusCapabilities_Type(Integer32):
    """Custom type snmpFddiMACFrameStatusCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1799),
    )


_SnmpFddiMACFrameStatusCapabilities_Type.__name__ = "Integer32"
_SnmpFddiMACFrameStatusCapabilities_Object = MibTableColumn
snmpFddiMACFrameStatusCapabilities = _SnmpFddiMACFrameStatusCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 3),
    _SnmpFddiMACFrameStatusCapabilities_Type()
)
snmpFddiMACFrameStatusCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACFrameStatusCapabilities.setStatus("mandatory")
_SnmpFddiMACTMaxGreatestLowerBound_Type = FddiTime
_SnmpFddiMACTMaxGreatestLowerBound_Object = MibTableColumn
snmpFddiMACTMaxGreatestLowerBound = _SnmpFddiMACTMaxGreatestLowerBound_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 4),
    _SnmpFddiMACTMaxGreatestLowerBound_Type()
)
snmpFddiMACTMaxGreatestLowerBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiMACTMaxGreatestLowerBound.setStatus("mandatory")
_SnmpFddiMACTVXGreatestLowerBound_Type = FddiTime
_SnmpFddiMACTVXGreatestLowerBound_Object = MibTableColumn
snmpFddiMACTVXGreatestLowerBound = _SnmpFddiMACTVXGreatestLowerBound_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 5),
    _SnmpFddiMACTVXGreatestLowerBound_Type()
)
snmpFddiMACTVXGreatestLowerBound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACTVXGreatestLowerBound.setStatus("mandatory")


class _SnmpFddiMACPathsAvailable_Type(Integer32):
    """Custom type snmpFddiMACPathsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpFddiMACPathsAvailable_Type.__name__ = "Integer32"
_SnmpFddiMACPathsAvailable_Object = MibTableColumn
snmpFddiMACPathsAvailable = _SnmpFddiMACPathsAvailable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 6),
    _SnmpFddiMACPathsAvailable_Type()
)
snmpFddiMACPathsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACPathsAvailable.setStatus("mandatory")


class _SnmpFddiMACCurrentPath_Type(Integer32):
    """Custom type snmpFddiMACCurrentPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("isolated", 16),
          ("local", 8),
          ("primary", 2),
          ("secondary", 4),
          ("unknown", 1))
    )


_SnmpFddiMACCurrentPath_Type.__name__ = "Integer32"
_SnmpFddiMACCurrentPath_Object = MibTableColumn
snmpFddiMACCurrentPath = _SnmpFddiMACCurrentPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 7),
    _SnmpFddiMACCurrentPath_Type()
)
snmpFddiMACCurrentPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACCurrentPath.setStatus("mandatory")
_SnmpFddiMACUpstreamNbr_Type = FddiMACLongAddressType
_SnmpFddiMACUpstreamNbr_Object = MibTableColumn
snmpFddiMACUpstreamNbr = _SnmpFddiMACUpstreamNbr_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 8),
    _SnmpFddiMACUpstreamNbr_Type()
)
snmpFddiMACUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACUpstreamNbr.setStatus("mandatory")
_SnmpFddiMACOldUpstreamNbr_Type = FddiMACLongAddressType
_SnmpFddiMACOldUpstreamNbr_Object = MibTableColumn
snmpFddiMACOldUpstreamNbr = _SnmpFddiMACOldUpstreamNbr_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 9),
    _SnmpFddiMACOldUpstreamNbr_Type()
)
snmpFddiMACOldUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACOldUpstreamNbr.setStatus("mandatory")


class _SnmpFddiMACDupAddrTest_Type(Integer32):
    """Custom type snmpFddiMACDupAddrTest based on Integer32"""
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


_SnmpFddiMACDupAddrTest_Type.__name__ = "Integer32"
_SnmpFddiMACDupAddrTest_Object = MibTableColumn
snmpFddiMACDupAddrTest = _SnmpFddiMACDupAddrTest_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 10),
    _SnmpFddiMACDupAddrTest_Type()
)
snmpFddiMACDupAddrTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACDupAddrTest.setStatus("mandatory")
_SnmpFddiMACPathsRequested_Type = Integer32
_SnmpFddiMACPathsRequested_Object = MibTableColumn
snmpFddiMACPathsRequested = _SnmpFddiMACPathsRequested_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 11),
    _SnmpFddiMACPathsRequested_Type()
)
snmpFddiMACPathsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiMACPathsRequested.setStatus("mandatory")


class _SnmpFddiMACDownstreamPORTType_Type(Integer32):
    """Custom type snmpFddiMACDownstreamPORTType based on Integer32"""
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
          ("s", 3),
          ("unknown", 5))
    )


_SnmpFddiMACDownstreamPORTType_Type.__name__ = "Integer32"
_SnmpFddiMACDownstreamPORTType_Object = MibTableColumn
snmpFddiMACDownstreamPORTType = _SnmpFddiMACDownstreamPORTType_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 12),
    _SnmpFddiMACDownstreamPORTType_Type()
)
snmpFddiMACDownstreamPORTType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACDownstreamPORTType.setStatus("mandatory")
_SnmpFddiMACSMTAddress_Type = FddiMACLongAddressType
_SnmpFddiMACSMTAddress_Object = MibTableColumn
snmpFddiMACSMTAddress = _SnmpFddiMACSMTAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 13),
    _SnmpFddiMACSMTAddress_Type()
)
snmpFddiMACSMTAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACSMTAddress.setStatus("mandatory")
_SnmpFddiMACTReq_Type = FddiTime
_SnmpFddiMACTReq_Object = MibTableColumn
snmpFddiMACTReq = _SnmpFddiMACTReq_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 14),
    _SnmpFddiMACTReq_Type()
)
snmpFddiMACTReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiMACTReq.setStatus("mandatory")
_SnmpFddiMACTNeg_Type = FddiTime
_SnmpFddiMACTNeg_Object = MibTableColumn
snmpFddiMACTNeg = _SnmpFddiMACTNeg_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 15),
    _SnmpFddiMACTNeg_Type()
)
snmpFddiMACTNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACTNeg.setStatus("mandatory")
_SnmpFddiMACTMax_Type = FddiTime
_SnmpFddiMACTMax_Object = MibTableColumn
snmpFddiMACTMax = _SnmpFddiMACTMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 16),
    _SnmpFddiMACTMax_Type()
)
snmpFddiMACTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACTMax.setStatus("mandatory")
_SnmpFddiMACTvxValue_Type = FddiTime
_SnmpFddiMACTvxValue_Object = MibTableColumn
snmpFddiMACTvxValue = _SnmpFddiMACTvxValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 17),
    _SnmpFddiMACTvxValue_Type()
)
snmpFddiMACTvxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACTvxValue.setStatus("mandatory")
_SnmpFddiMACTMin_Type = FddiTime
_SnmpFddiMACTMin_Object = MibTableColumn
snmpFddiMACTMin = _SnmpFddiMACTMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 18),
    _SnmpFddiMACTMin_Type()
)
snmpFddiMACTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACTMin.setStatus("mandatory")


class _SnmpFddiMACCurrentFrameStatus_Type(Integer32):
    """Custom type snmpFddiMACCurrentFrameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpFddiMACCurrentFrameStatus_Type.__name__ = "Integer32"
_SnmpFddiMACCurrentFrameStatus_Object = MibTableColumn
snmpFddiMACCurrentFrameStatus = _SnmpFddiMACCurrentFrameStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 19),
    _SnmpFddiMACCurrentFrameStatus_Type()
)
snmpFddiMACCurrentFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiMACCurrentFrameStatus.setStatus("mandatory")
_SnmpFddiMACFrameCts_Type = Counter32
_SnmpFddiMACFrameCts_Object = MibTableColumn
snmpFddiMACFrameCts = _SnmpFddiMACFrameCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 20),
    _SnmpFddiMACFrameCts_Type()
)
snmpFddiMACFrameCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACFrameCts.setStatus("mandatory")
_SnmpFddiMACErrorCts_Type = Counter32
_SnmpFddiMACErrorCts_Object = MibTableColumn
snmpFddiMACErrorCts = _SnmpFddiMACErrorCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 21),
    _SnmpFddiMACErrorCts_Type()
)
snmpFddiMACErrorCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACErrorCts.setStatus("mandatory")
_SnmpFddiMACLostCts_Type = Counter32
_SnmpFddiMACLostCts_Object = MibTableColumn
snmpFddiMACLostCts = _SnmpFddiMACLostCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 22),
    _SnmpFddiMACLostCts_Type()
)
snmpFddiMACLostCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACLostCts.setStatus("mandatory")


class _SnmpFddiMACFrameErrorThreshold_Type(Integer32):
    """Custom type snmpFddiMACFrameErrorThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiMACFrameErrorThreshold_Type.__name__ = "Integer32"
_SnmpFddiMACFrameErrorThreshold_Object = MibTableColumn
snmpFddiMACFrameErrorThreshold = _SnmpFddiMACFrameErrorThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 23),
    _SnmpFddiMACFrameErrorThreshold_Type()
)
snmpFddiMACFrameErrorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACFrameErrorThreshold.setStatus("mandatory")


class _SnmpFddiMACFrameErrorRatio_Type(Integer32):
    """Custom type snmpFddiMACFrameErrorRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiMACFrameErrorRatio_Type.__name__ = "Integer32"
_SnmpFddiMACFrameErrorRatio_Object = MibTableColumn
snmpFddiMACFrameErrorRatio = _SnmpFddiMACFrameErrorRatio_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 24),
    _SnmpFddiMACFrameErrorRatio_Type()
)
snmpFddiMACFrameErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACFrameErrorRatio.setStatus("mandatory")


class _SnmpFddiMACRMTState_Type(Integer32):
    """Custom type snmpFddiMACRMTState based on Integer32"""
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


_SnmpFddiMACRMTState_Type.__name__ = "Integer32"
_SnmpFddiMACRMTState_Object = MibTableColumn
snmpFddiMACRMTState = _SnmpFddiMACRMTState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 25),
    _SnmpFddiMACRMTState_Type()
)
snmpFddiMACRMTState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACRMTState.setStatus("mandatory")


class _SnmpFddiMACDaFlag_Type(Integer32):
    """Custom type snmpFddiMACDaFlag based on Integer32"""
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


_SnmpFddiMACDaFlag_Type.__name__ = "Integer32"
_SnmpFddiMACDaFlag_Object = MibTableColumn
snmpFddiMACDaFlag = _SnmpFddiMACDaFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 26),
    _SnmpFddiMACDaFlag_Type()
)
snmpFddiMACDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACDaFlag.setStatus("mandatory")


class _SnmpFddiMACUnaDaFlag_Type(Integer32):
    """Custom type snmpFddiMACUnaDaFlag based on Integer32"""
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


_SnmpFddiMACUnaDaFlag_Type.__name__ = "Integer32"
_SnmpFddiMACUnaDaFlag_Object = MibTableColumn
snmpFddiMACUnaDaFlag = _SnmpFddiMACUnaDaFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 27),
    _SnmpFddiMACUnaDaFlag_Type()
)
snmpFddiMACUnaDaFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACUnaDaFlag.setStatus("mandatory")


class _SnmpFddiMACFrameCondition_Type(Integer32):
    """Custom type snmpFddiMACFrameCondition based on Integer32"""
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


_SnmpFddiMACFrameCondition_Type.__name__ = "Integer32"
_SnmpFddiMACFrameCondition_Object = MibTableColumn
snmpFddiMACFrameCondition = _SnmpFddiMACFrameCondition_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 28),
    _SnmpFddiMACFrameCondition_Type()
)
snmpFddiMACFrameCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACFrameCondition.setStatus("mandatory")
_SnmpFddiMACChipSet_Type = ObjectIdentifier
_SnmpFddiMACChipSet_Object = MibTableColumn
snmpFddiMACChipSet = _SnmpFddiMACChipSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 29),
    _SnmpFddiMACChipSet_Type()
)
snmpFddiMACChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiMACChipSet.setStatus("mandatory")


class _SnmpFddiMACAction_Type(Integer32):
    """Custom type snmpFddiMACAction based on Integer32"""
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
        *(("connectMAC", 4),
          ("disableLLCService", 3),
          ("disconnectMAC", 5),
          ("enableLLCService", 2),
          ("other", 1))
    )


_SnmpFddiMACAction_Type.__name__ = "Integer32"
_SnmpFddiMACAction_Object = MibTableColumn
snmpFddiMACAction = _SnmpFddiMACAction_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 2, 2, 1, 30),
    _SnmpFddiMACAction_Type()
)
snmpFddiMACAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiMACAction.setStatus("mandatory")
_SnmpFddiPATH_ObjectIdentity = ObjectIdentity
snmpFddiPATH = _SnmpFddiPATH_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 3)
)
_SnmpFddiPORT_ObjectIdentity = ObjectIdentity
snmpFddiPORT = _SnmpFddiPORT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 4)
)


class _SnmpFddiPORTNumber_Type(Integer32):
    """Custom type snmpFddiPORTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpFddiPORTNumber_Type.__name__ = "Integer32"
_SnmpFddiPORTNumber_Object = MibScalar
snmpFddiPORTNumber = _SnmpFddiPORTNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 1),
    _SnmpFddiPORTNumber_Type()
)
snmpFddiPORTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTNumber.setStatus("mandatory")
_SnmpFddiPORTTable_Object = MibTable
snmpFddiPORTTable = _SnmpFddiPORTTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2)
)
if mibBuilder.loadTexts:
    snmpFddiPORTTable.setStatus("mandatory")
_SnmpFddiPORTEntry_Object = MibTableRow
snmpFddiPORTEntry = _SnmpFddiPORTEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1)
)
snmpFddiPORTEntry.setIndexNames(
    (0, "RFC1285-MIB", "snmpFddiPORTSMTIndex"),
    (0, "RFC1285-MIB", "snmpFddiPORTIndex"),
)
if mibBuilder.loadTexts:
    snmpFddiPORTEntry.setStatus("mandatory")


class _SnmpFddiPORTSMTIndex_Type(Integer32):
    """Custom type snmpFddiPORTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiPORTSMTIndex_Type.__name__ = "Integer32"
_SnmpFddiPORTSMTIndex_Object = MibTableColumn
snmpFddiPORTSMTIndex = _SnmpFddiPORTSMTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 1),
    _SnmpFddiPORTSMTIndex_Type()
)
snmpFddiPORTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTSMTIndex.setStatus("mandatory")


class _SnmpFddiPORTIndex_Type(Integer32):
    """Custom type snmpFddiPORTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiPORTIndex_Type.__name__ = "Integer32"
_SnmpFddiPORTIndex_Object = MibTableColumn
snmpFddiPORTIndex = _SnmpFddiPORTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 2),
    _SnmpFddiPORTIndex_Type()
)
snmpFddiPORTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTIndex.setStatus("mandatory")


class _SnmpFddiPORTPCType_Type(Integer32):
    """Custom type snmpFddiPORTPCType based on Integer32"""
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
        *(("a", 1),
          ("b", 2),
          ("m", 4),
          ("s", 3))
    )


_SnmpFddiPORTPCType_Type.__name__ = "Integer32"
_SnmpFddiPORTPCType_Object = MibTableColumn
snmpFddiPORTPCType = _SnmpFddiPORTPCType_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 3),
    _SnmpFddiPORTPCType_Type()
)
snmpFddiPORTPCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTPCType.setStatus("mandatory")


class _SnmpFddiPORTPCNeighbor_Type(Integer32):
    """Custom type snmpFddiPORTPCNeighbor based on Integer32"""
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
          ("s", 3),
          ("unknown", 5))
    )


_SnmpFddiPORTPCNeighbor_Type.__name__ = "Integer32"
_SnmpFddiPORTPCNeighbor_Object = MibTableColumn
snmpFddiPORTPCNeighbor = _SnmpFddiPORTPCNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 4),
    _SnmpFddiPORTPCNeighbor_Type()
)
snmpFddiPORTPCNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTPCNeighbor.setStatus("mandatory")


class _SnmpFddiPORTConnectionPolicies_Type(Integer32):
    """Custom type snmpFddiPORTConnectionPolicies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpFddiPORTConnectionPolicies_Type.__name__ = "Integer32"
_SnmpFddiPORTConnectionPolicies_Object = MibTableColumn
snmpFddiPORTConnectionPolicies = _SnmpFddiPORTConnectionPolicies_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 5),
    _SnmpFddiPORTConnectionPolicies_Type()
)
snmpFddiPORTConnectionPolicies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTConnectionPolicies.setStatus("mandatory")


class _SnmpFddiPORTRemoteMACIndicated_Type(Integer32):
    """Custom type snmpFddiPORTRemoteMACIndicated based on Integer32"""
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


_SnmpFddiPORTRemoteMACIndicated_Type.__name__ = "Integer32"
_SnmpFddiPORTRemoteMACIndicated_Object = MibTableColumn
snmpFddiPORTRemoteMACIndicated = _SnmpFddiPORTRemoteMACIndicated_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 6),
    _SnmpFddiPORTRemoteMACIndicated_Type()
)
snmpFddiPORTRemoteMACIndicated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTRemoteMACIndicated.setStatus("mandatory")


class _SnmpFddiPORTCEState_Type(Integer32):
    """Custom type snmpFddiPORTCEState based on Integer32"""
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
        *(("ce0", 1),
          ("ce1", 2),
          ("ce2", 3),
          ("ce3", 4),
          ("ce4", 5))
    )


_SnmpFddiPORTCEState_Type.__name__ = "Integer32"
_SnmpFddiPORTCEState_Object = MibTableColumn
snmpFddiPORTCEState = _SnmpFddiPORTCEState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 7),
    _SnmpFddiPORTCEState_Type()
)
snmpFddiPORTCEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTCEState.setStatus("mandatory")


class _SnmpFddiPORTPathsRequested_Type(Integer32):
    """Custom type snmpFddiPORTPathsRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_SnmpFddiPORTPathsRequested_Type.__name__ = "Integer32"
_SnmpFddiPORTPathsRequested_Object = MibTableColumn
snmpFddiPORTPathsRequested = _SnmpFddiPORTPathsRequested_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 8),
    _SnmpFddiPORTPathsRequested_Type()
)
snmpFddiPORTPathsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTPathsRequested.setStatus("mandatory")
_SnmpFddiPORTMACPlacement_Type = FddiResourceId
_SnmpFddiPORTMACPlacement_Object = MibTableColumn
snmpFddiPORTMACPlacement = _SnmpFddiPORTMACPlacement_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 9),
    _SnmpFddiPORTMACPlacement_Type()
)
snmpFddiPORTMACPlacement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTMACPlacement.setStatus("mandatory")


class _SnmpFddiPORTAvailablePaths_Type(Integer32):
    """Custom type snmpFddiPORTAvailablePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnmpFddiPORTAvailablePaths_Type.__name__ = "Integer32"
_SnmpFddiPORTAvailablePaths_Object = MibTableColumn
snmpFddiPORTAvailablePaths = _SnmpFddiPORTAvailablePaths_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 10),
    _SnmpFddiPORTAvailablePaths_Type()
)
snmpFddiPORTAvailablePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTAvailablePaths.setStatus("mandatory")
_SnmpFddiPORTMACLoopTime_Type = FddiTime
_SnmpFddiPORTMACLoopTime_Object = MibTableColumn
snmpFddiPORTMACLoopTime = _SnmpFddiPORTMACLoopTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 11),
    _SnmpFddiPORTMACLoopTime_Type()
)
snmpFddiPORTMACLoopTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTMACLoopTime.setStatus("mandatory")
_SnmpFddiPORTTBMax_Type = FddiTime
_SnmpFddiPORTTBMax_Object = MibTableColumn
snmpFddiPORTTBMax = _SnmpFddiPORTTBMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 12),
    _SnmpFddiPORTTBMax_Type()
)
snmpFddiPORTTBMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTTBMax.setStatus("mandatory")


class _SnmpFddiPORTBSFlag_Type(Integer32):
    """Custom type snmpFddiPORTBSFlag based on Integer32"""
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


_SnmpFddiPORTBSFlag_Type.__name__ = "Integer32"
_SnmpFddiPORTBSFlag_Object = MibTableColumn
snmpFddiPORTBSFlag = _SnmpFddiPORTBSFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 13),
    _SnmpFddiPORTBSFlag_Type()
)
snmpFddiPORTBSFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTBSFlag.setStatus("mandatory")
_SnmpFddiPORTLCTFailCts_Type = Counter32
_SnmpFddiPORTLCTFailCts_Object = MibTableColumn
snmpFddiPORTLCTFailCts = _SnmpFddiPORTLCTFailCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 14),
    _SnmpFddiPORTLCTFailCts_Type()
)
snmpFddiPORTLCTFailCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTLCTFailCts.setStatus("mandatory")


class _SnmpFddiPORTLerEstimate_Type(Integer32):
    """Custom type snmpFddiPORTLerEstimate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_SnmpFddiPORTLerEstimate_Type.__name__ = "Integer32"
_SnmpFddiPORTLerEstimate_Object = MibTableColumn
snmpFddiPORTLerEstimate = _SnmpFddiPORTLerEstimate_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 15),
    _SnmpFddiPORTLerEstimate_Type()
)
snmpFddiPORTLerEstimate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTLerEstimate.setStatus("mandatory")
_SnmpFddiPORTLemRejectCts_Type = Counter32
_SnmpFddiPORTLemRejectCts_Object = MibTableColumn
snmpFddiPORTLemRejectCts = _SnmpFddiPORTLemRejectCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 16),
    _SnmpFddiPORTLemRejectCts_Type()
)
snmpFddiPORTLemRejectCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTLemRejectCts.setStatus("mandatory")
_SnmpFddiPORTLemCts_Type = Counter32
_SnmpFddiPORTLemCts_Object = MibTableColumn
snmpFddiPORTLemCts = _SnmpFddiPORTLemCts_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 17),
    _SnmpFddiPORTLemCts_Type()
)
snmpFddiPORTLemCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTLemCts.setStatus("mandatory")


class _SnmpFddiPORTLerCutoff_Type(Integer32):
    """Custom type snmpFddiPORTLerCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_SnmpFddiPORTLerCutoff_Type.__name__ = "Integer32"
_SnmpFddiPORTLerCutoff_Object = MibTableColumn
snmpFddiPORTLerCutoff = _SnmpFddiPORTLerCutoff_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 18),
    _SnmpFddiPORTLerCutoff_Type()
)
snmpFddiPORTLerCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTLerCutoff.setStatus("mandatory")


class _SnmpFddiPORTLerAlarm_Type(Integer32):
    """Custom type snmpFddiPORTLerAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 15),
    )


_SnmpFddiPORTLerAlarm_Type.__name__ = "Integer32"
_SnmpFddiPORTLerAlarm_Object = MibTableColumn
snmpFddiPORTLerAlarm = _SnmpFddiPORTLerAlarm_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 19),
    _SnmpFddiPORTLerAlarm_Type()
)
snmpFddiPORTLerAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTLerAlarm.setStatus("mandatory")


class _SnmpFddiPORTConnectState_Type(Integer32):
    """Custom type snmpFddiPORTConnectState based on Integer32"""
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


_SnmpFddiPORTConnectState_Type.__name__ = "Integer32"
_SnmpFddiPORTConnectState_Object = MibTableColumn
snmpFddiPORTConnectState = _SnmpFddiPORTConnectState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 20),
    _SnmpFddiPORTConnectState_Type()
)
snmpFddiPORTConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTConnectState.setStatus("mandatory")


class _SnmpFddiPORTPCMState_Type(Integer32):
    """Custom type snmpFddiPORTPCMState based on Integer32"""
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


_SnmpFddiPORTPCMState_Type.__name__ = "Integer32"
_SnmpFddiPORTPCMState_Object = MibTableColumn
snmpFddiPORTPCMState = _SnmpFddiPORTPCMState_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 21),
    _SnmpFddiPORTPCMState_Type()
)
snmpFddiPORTPCMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTPCMState.setStatus("mandatory")


class _SnmpFddiPORTPCWithhold_Type(Integer32):
    """Custom type snmpFddiPORTPCWithhold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m-m", 2),
          ("none", 1),
          ("other", 3))
    )


_SnmpFddiPORTPCWithhold_Type.__name__ = "Integer32"
_SnmpFddiPORTPCWithhold_Object = MibTableColumn
snmpFddiPORTPCWithhold = _SnmpFddiPORTPCWithhold_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 22),
    _SnmpFddiPORTPCWithhold_Type()
)
snmpFddiPORTPCWithhold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTPCWithhold.setStatus("mandatory")


class _SnmpFddiPORTLerCondition_Type(Integer32):
    """Custom type snmpFddiPORTLerCondition based on Integer32"""
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


_SnmpFddiPORTLerCondition_Type.__name__ = "Integer32"
_SnmpFddiPORTLerCondition_Object = MibTableColumn
snmpFddiPORTLerCondition = _SnmpFddiPORTLerCondition_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 23),
    _SnmpFddiPORTLerCondition_Type()
)
snmpFddiPORTLerCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTLerCondition.setStatus("mandatory")
_SnmpFddiPORTChipSet_Type = ObjectIdentifier
_SnmpFddiPORTChipSet_Object = MibTableColumn
snmpFddiPORTChipSet = _SnmpFddiPORTChipSet_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 24),
    _SnmpFddiPORTChipSet_Type()
)
snmpFddiPORTChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiPORTChipSet.setStatus("mandatory")


class _SnmpFddiPORTAction_Type(Integer32):
    """Custom type snmpFddiPORTAction based on Integer32"""
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


_SnmpFddiPORTAction_Type.__name__ = "Integer32"
_SnmpFddiPORTAction_Object = MibTableColumn
snmpFddiPORTAction = _SnmpFddiPORTAction_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 4, 2, 1, 25),
    _SnmpFddiPORTAction_Type()
)
snmpFddiPORTAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiPORTAction.setStatus("mandatory")
_SnmpFddiATTACHMENT_ObjectIdentity = ObjectIdentity
snmpFddiATTACHMENT = _SnmpFddiATTACHMENT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 5)
)


class _SnmpFddiATTACHMENTNumber_Type(Integer32):
    """Custom type snmpFddiATTACHMENTNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpFddiATTACHMENTNumber_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTNumber_Object = MibScalar
snmpFddiATTACHMENTNumber = _SnmpFddiATTACHMENTNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 1),
    _SnmpFddiATTACHMENTNumber_Type()
)
snmpFddiATTACHMENTNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTNumber.setStatus("mandatory")
_SnmpFddiATTACHMENTTable_Object = MibTable
snmpFddiATTACHMENTTable = _SnmpFddiATTACHMENTTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2)
)
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTTable.setStatus("mandatory")
_SnmpFddiATTACHMENTEntry_Object = MibTableRow
snmpFddiATTACHMENTEntry = _SnmpFddiATTACHMENTEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1)
)
snmpFddiATTACHMENTEntry.setIndexNames(
    (0, "RFC1285-MIB", "snmpFddiATTACHMENTSMTIndex"),
    (0, "RFC1285-MIB", "snmpFddiATTACHMENTIndex"),
)
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTEntry.setStatus("mandatory")


class _SnmpFddiATTACHMENTSMTIndex_Type(Integer32):
    """Custom type snmpFddiATTACHMENTSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiATTACHMENTSMTIndex_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTSMTIndex_Object = MibTableColumn
snmpFddiATTACHMENTSMTIndex = _SnmpFddiATTACHMENTSMTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 1),
    _SnmpFddiATTACHMENTSMTIndex_Type()
)
snmpFddiATTACHMENTSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTSMTIndex.setStatus("mandatory")


class _SnmpFddiATTACHMENTIndex_Type(Integer32):
    """Custom type snmpFddiATTACHMENTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpFddiATTACHMENTIndex_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTIndex_Object = MibTableColumn
snmpFddiATTACHMENTIndex = _SnmpFddiATTACHMENTIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 2),
    _SnmpFddiATTACHMENTIndex_Type()
)
snmpFddiATTACHMENTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTIndex.setStatus("mandatory")


class _SnmpFddiATTACHMENTClass_Type(Integer32):
    """Custom type snmpFddiATTACHMENTClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("concentrator", 3),
          ("dual-attachment", 2),
          ("single-attachment", 1))
    )


_SnmpFddiATTACHMENTClass_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTClass_Object = MibTableColumn
snmpFddiATTACHMENTClass = _SnmpFddiATTACHMENTClass_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 3),
    _SnmpFddiATTACHMENTClass_Type()
)
snmpFddiATTACHMENTClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTClass.setStatus("mandatory")


class _SnmpFddiATTACHMENTOpticalBypassPresent_Type(Integer32):
    """Custom type snmpFddiATTACHMENTOpticalBypassPresent based on Integer32"""
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


_SnmpFddiATTACHMENTOpticalBypassPresent_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTOpticalBypassPresent_Object = MibTableColumn
snmpFddiATTACHMENTOpticalBypassPresent = _SnmpFddiATTACHMENTOpticalBypassPresent_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 4),
    _SnmpFddiATTACHMENTOpticalBypassPresent_Type()
)
snmpFddiATTACHMENTOpticalBypassPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTOpticalBypassPresent.setStatus("mandatory")
_SnmpFddiATTACHMENTIMaxExpiration_Type = FddiTime
_SnmpFddiATTACHMENTIMaxExpiration_Object = MibTableColumn
snmpFddiATTACHMENTIMaxExpiration = _SnmpFddiATTACHMENTIMaxExpiration_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 5),
    _SnmpFddiATTACHMENTIMaxExpiration_Type()
)
snmpFddiATTACHMENTIMaxExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTIMaxExpiration.setStatus("mandatory")


class _SnmpFddiATTACHMENTInsertedStatus_Type(Integer32):
    """Custom type snmpFddiATTACHMENTInsertedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unimplemented", 3))
    )


_SnmpFddiATTACHMENTInsertedStatus_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTInsertedStatus_Object = MibTableColumn
snmpFddiATTACHMENTInsertedStatus = _SnmpFddiATTACHMENTInsertedStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 6),
    _SnmpFddiATTACHMENTInsertedStatus_Type()
)
snmpFddiATTACHMENTInsertedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTInsertedStatus.setStatus("mandatory")


class _SnmpFddiATTACHMENTInsertPolicy_Type(Integer32):
    """Custom type snmpFddiATTACHMENTInsertPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unimplemented", 3))
    )


_SnmpFddiATTACHMENTInsertPolicy_Type.__name__ = "Integer32"
_SnmpFddiATTACHMENTInsertPolicy_Object = MibTableColumn
snmpFddiATTACHMENTInsertPolicy = _SnmpFddiATTACHMENTInsertPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 15, 5, 2, 1, 7),
    _SnmpFddiATTACHMENTInsertPolicy_Type()
)
snmpFddiATTACHMENTInsertPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpFddiATTACHMENTInsertPolicy.setStatus("mandatory")
_SnmpFddiChipSets_ObjectIdentity = ObjectIdentity
snmpFddiChipSets = _SnmpFddiChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 6)
)
_SnmpFddiPHYChipSets_ObjectIdentity = ObjectIdentity
snmpFddiPHYChipSets = _SnmpFddiPHYChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 6, 1)
)
_SnmpFddiMACChipSets_ObjectIdentity = ObjectIdentity
snmpFddiMACChipSets = _SnmpFddiMACChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 6, 2)
)
_SnmpFddiPHYMACChipSets_ObjectIdentity = ObjectIdentity
snmpFddiPHYMACChipSets = _SnmpFddiPHYMACChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 15, 6, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1285-MIB",
    **{"FddiTime": FddiTime,
       "FddiResourceId": FddiResourceId,
       "FddiSMTStationIdType": FddiSMTStationIdType,
       "FddiMACLongAddressType": FddiMACLongAddressType,
       "fddi": fddi,
       "snmpFddiSMT": snmpFddiSMT,
       "snmpFddiSMTNumber": snmpFddiSMTNumber,
       "snmpFddiSMTTable": snmpFddiSMTTable,
       "snmpFddiSMTEntry": snmpFddiSMTEntry,
       "snmpFddiSMTIndex": snmpFddiSMTIndex,
       "snmpFddiSMTStationId": snmpFddiSMTStationId,
       "snmpFddiSMTOpVersionId": snmpFddiSMTOpVersionId,
       "snmpFddiSMTHiVersionId": snmpFddiSMTHiVersionId,
       "snmpFddiSMTLoVersionId": snmpFddiSMTLoVersionId,
       "snmpFddiSMTMACCt": snmpFddiSMTMACCt,
       "snmpFddiSMTNonMasterCt": snmpFddiSMTNonMasterCt,
       "snmpFddiSMTMasterCt": snmpFddiSMTMasterCt,
       "snmpFddiSMTPathsAvailable": snmpFddiSMTPathsAvailable,
       "snmpFddiSMTConfigCapabilities": snmpFddiSMTConfigCapabilities,
       "snmpFddiSMTConfigPolicy": snmpFddiSMTConfigPolicy,
       "snmpFddiSMTConnectionPolicy": snmpFddiSMTConnectionPolicy,
       "snmpFddiSMTTNotify": snmpFddiSMTTNotify,
       "snmpFddiSMTStatusReporting": snmpFddiSMTStatusReporting,
       "snmpFddiSMTECMState": snmpFddiSMTECMState,
       "snmpFddiSMTCFState": snmpFddiSMTCFState,
       "snmpFddiSMTHoldState": snmpFddiSMTHoldState,
       "snmpFddiSMTRemoteDisconnectFlag": snmpFddiSMTRemoteDisconnectFlag,
       "snmpFddiSMTStationAction": snmpFddiSMTStationAction,
       "snmpFddiMAC": snmpFddiMAC,
       "snmpFddiMACNumber": snmpFddiMACNumber,
       "snmpFddiMACTable": snmpFddiMACTable,
       "snmpFddiMACEntry": snmpFddiMACEntry,
       "snmpFddiMACSMTIndex": snmpFddiMACSMTIndex,
       "snmpFddiMACIndex": snmpFddiMACIndex,
       "snmpFddiMACFrameStatusCapabilities": snmpFddiMACFrameStatusCapabilities,
       "snmpFddiMACTMaxGreatestLowerBound": snmpFddiMACTMaxGreatestLowerBound,
       "snmpFddiMACTVXGreatestLowerBound": snmpFddiMACTVXGreatestLowerBound,
       "snmpFddiMACPathsAvailable": snmpFddiMACPathsAvailable,
       "snmpFddiMACCurrentPath": snmpFddiMACCurrentPath,
       "snmpFddiMACUpstreamNbr": snmpFddiMACUpstreamNbr,
       "snmpFddiMACOldUpstreamNbr": snmpFddiMACOldUpstreamNbr,
       "snmpFddiMACDupAddrTest": snmpFddiMACDupAddrTest,
       "snmpFddiMACPathsRequested": snmpFddiMACPathsRequested,
       "snmpFddiMACDownstreamPORTType": snmpFddiMACDownstreamPORTType,
       "snmpFddiMACSMTAddress": snmpFddiMACSMTAddress,
       "snmpFddiMACTReq": snmpFddiMACTReq,
       "snmpFddiMACTNeg": snmpFddiMACTNeg,
       "snmpFddiMACTMax": snmpFddiMACTMax,
       "snmpFddiMACTvxValue": snmpFddiMACTvxValue,
       "snmpFddiMACTMin": snmpFddiMACTMin,
       "snmpFddiMACCurrentFrameStatus": snmpFddiMACCurrentFrameStatus,
       "snmpFddiMACFrameCts": snmpFddiMACFrameCts,
       "snmpFddiMACErrorCts": snmpFddiMACErrorCts,
       "snmpFddiMACLostCts": snmpFddiMACLostCts,
       "snmpFddiMACFrameErrorThreshold": snmpFddiMACFrameErrorThreshold,
       "snmpFddiMACFrameErrorRatio": snmpFddiMACFrameErrorRatio,
       "snmpFddiMACRMTState": snmpFddiMACRMTState,
       "snmpFddiMACDaFlag": snmpFddiMACDaFlag,
       "snmpFddiMACUnaDaFlag": snmpFddiMACUnaDaFlag,
       "snmpFddiMACFrameCondition": snmpFddiMACFrameCondition,
       "snmpFddiMACChipSet": snmpFddiMACChipSet,
       "snmpFddiMACAction": snmpFddiMACAction,
       "snmpFddiPATH": snmpFddiPATH,
       "snmpFddiPORT": snmpFddiPORT,
       "snmpFddiPORTNumber": snmpFddiPORTNumber,
       "snmpFddiPORTTable": snmpFddiPORTTable,
       "snmpFddiPORTEntry": snmpFddiPORTEntry,
       "snmpFddiPORTSMTIndex": snmpFddiPORTSMTIndex,
       "snmpFddiPORTIndex": snmpFddiPORTIndex,
       "snmpFddiPORTPCType": snmpFddiPORTPCType,
       "snmpFddiPORTPCNeighbor": snmpFddiPORTPCNeighbor,
       "snmpFddiPORTConnectionPolicies": snmpFddiPORTConnectionPolicies,
       "snmpFddiPORTRemoteMACIndicated": snmpFddiPORTRemoteMACIndicated,
       "snmpFddiPORTCEState": snmpFddiPORTCEState,
       "snmpFddiPORTPathsRequested": snmpFddiPORTPathsRequested,
       "snmpFddiPORTMACPlacement": snmpFddiPORTMACPlacement,
       "snmpFddiPORTAvailablePaths": snmpFddiPORTAvailablePaths,
       "snmpFddiPORTMACLoopTime": snmpFddiPORTMACLoopTime,
       "snmpFddiPORTTBMax": snmpFddiPORTTBMax,
       "snmpFddiPORTBSFlag": snmpFddiPORTBSFlag,
       "snmpFddiPORTLCTFailCts": snmpFddiPORTLCTFailCts,
       "snmpFddiPORTLerEstimate": snmpFddiPORTLerEstimate,
       "snmpFddiPORTLemRejectCts": snmpFddiPORTLemRejectCts,
       "snmpFddiPORTLemCts": snmpFddiPORTLemCts,
       "snmpFddiPORTLerCutoff": snmpFddiPORTLerCutoff,
       "snmpFddiPORTLerAlarm": snmpFddiPORTLerAlarm,
       "snmpFddiPORTConnectState": snmpFddiPORTConnectState,
       "snmpFddiPORTPCMState": snmpFddiPORTPCMState,
       "snmpFddiPORTPCWithhold": snmpFddiPORTPCWithhold,
       "snmpFddiPORTLerCondition": snmpFddiPORTLerCondition,
       "snmpFddiPORTChipSet": snmpFddiPORTChipSet,
       "snmpFddiPORTAction": snmpFddiPORTAction,
       "snmpFddiATTACHMENT": snmpFddiATTACHMENT,
       "snmpFddiATTACHMENTNumber": snmpFddiATTACHMENTNumber,
       "snmpFddiATTACHMENTTable": snmpFddiATTACHMENTTable,
       "snmpFddiATTACHMENTEntry": snmpFddiATTACHMENTEntry,
       "snmpFddiATTACHMENTSMTIndex": snmpFddiATTACHMENTSMTIndex,
       "snmpFddiATTACHMENTIndex": snmpFddiATTACHMENTIndex,
       "snmpFddiATTACHMENTClass": snmpFddiATTACHMENTClass,
       "snmpFddiATTACHMENTOpticalBypassPresent": snmpFddiATTACHMENTOpticalBypassPresent,
       "snmpFddiATTACHMENTIMaxExpiration": snmpFddiATTACHMENTIMaxExpiration,
       "snmpFddiATTACHMENTInsertedStatus": snmpFddiATTACHMENTInsertedStatus,
       "snmpFddiATTACHMENTInsertPolicy": snmpFddiATTACHMENTInsertPolicy,
       "snmpFddiChipSets": snmpFddiChipSets,
       "snmpFddiPHYChipSets": snmpFddiPHYChipSets,
       "snmpFddiMACChipSets": snmpFddiMACChipSets,
       "snmpFddiPHYMACChipSets": snmpFddiPHYMACChipSets}
)
