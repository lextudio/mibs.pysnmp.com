# SNMP MIB module (SONUS-SIP-SIGNALLING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-SIP-SIGNALLING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:08 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel")

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(SonusAdminState,
 SonusName,
 SonusServiceState) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusAdminState",
    "SonusName",
    "SonusServiceState")


# MODULE-IDENTITY

sonusSipSignallingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusSipSignallingMIBObjects_ObjectIdentity = ObjectIdentity
sonusSipSignallingMIBObjects = _SonusSipSignallingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1)
)
_SonusSipSigTimerObjects_ObjectIdentity = ObjectIdentity
sonusSipSigTimerObjects = _SonusSipSigTimerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1)
)


class _SonusSipSigTimerT1_Type(Integer32):
    """Custom type sonusSipSigTimerT1 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_SonusSipSigTimerT1_Type.__name__ = "Integer32"
_SonusSipSigTimerT1_Object = MibScalar
sonusSipSigTimerT1 = _SonusSipSigTimerT1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 1),
    _SonusSipSigTimerT1_Type()
)
sonusSipSigTimerT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigTimerT1.setStatus("current")


class _SonusSipSigTimerT2_Type(Integer32):
    """Custom type sonusSipSigTimerT2 based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSipSigTimerT2_Type.__name__ = "Integer32"
_SonusSipSigTimerT2_Object = MibScalar
sonusSipSigTimerT2 = _SonusSipSigTimerT2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 2),
    _SonusSipSigTimerT2_Type()
)
sonusSipSigTimerT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigTimerT2.setStatus("current")


class _SonusSipSigTimerSessionKeepalive_Type(Integer32):
    """Custom type sonusSipSigTimerSessionKeepalive based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SonusSipSigTimerSessionKeepalive_Type.__name__ = "Integer32"
_SonusSipSigTimerSessionKeepalive_Object = MibScalar
sonusSipSigTimerSessionKeepalive = _SonusSipSigTimerSessionKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 1, 3),
    _SonusSipSigTimerSessionKeepalive_Type()
)
sonusSipSigTimerSessionKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigTimerSessionKeepalive.setStatus("current")
_SonusSipSigRetryObjects_ObjectIdentity = ObjectIdentity
sonusSipSigRetryObjects = _SonusSipSigRetryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2)
)


class _SonusSipSigNumOfRetry_Type(Integer32):
    """Custom type sonusSipSigNumOfRetry based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 12),
    )


_SonusSipSigNumOfRetry_Type.__name__ = "Integer32"
_SonusSipSigNumOfRetry_Object = MibScalar
sonusSipSigNumOfRetry = _SonusSipSigNumOfRetry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2, 1),
    _SonusSipSigNumOfRetry_Type()
)
sonusSipSigNumOfRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigNumOfRetry.setStatus("current")


class _SonusSipSigInviteRetry_Type(Integer32):
    """Custom type sonusSipSigInviteRetry based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_SonusSipSigInviteRetry_Type.__name__ = "Integer32"
_SonusSipSigInviteRetry_Object = MibScalar
sonusSipSigInviteRetry = _SonusSipSigInviteRetry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 2, 2),
    _SonusSipSigInviteRetry_Type()
)
sonusSipSigInviteRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigInviteRetry.setStatus("current")
_SonusSipSigPortTable_Object = MibTable
sonusSipSigPortTable = _SonusSipSigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3)
)
if mibBuilder.loadTexts:
    sonusSipSigPortTable.setStatus("current")
_SonusSipSigPortEntry_Object = MibTableRow
sonusSipSigPortEntry = _SonusSipSigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1)
)
sonusSipSigPortEntry.setIndexNames(
    (0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIndex"),
)
if mibBuilder.loadTexts:
    sonusSipSigPortEntry.setStatus("current")
_SonusSipSigPortIndex_Type = Integer32
_SonusSipSigPortIndex_Object = MibTableColumn
sonusSipSigPortIndex = _SonusSipSigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 1),
    _SonusSipSigPortIndex_Type()
)
sonusSipSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortIndex.setStatus("current")
_SonusSipSigPortIpAddress_Type = IpAddress
_SonusSipSigPortIpAddress_Object = MibTableColumn
sonusSipSigPortIpAddress = _SonusSipSigPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 2),
    _SonusSipSigPortIpAddress_Type()
)
sonusSipSigPortIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortIpAddress.setStatus("current")


class _SonusSipSigPortNum_Type(Integer32):
    """Custom type sonusSipSigPortNum based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSipSigPortNum_Type.__name__ = "Integer32"
_SonusSipSigPortNum_Object = MibTableColumn
sonusSipSigPortNum = _SonusSipSigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 3),
    _SonusSipSigPortNum_Type()
)
sonusSipSigPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortNum.setStatus("current")


class _SonusSipSigPortInterface_Type(Integer32):
    """Custom type sonusSipSigPortInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgtNif", 1),
          ("nif", 2))
    )


_SonusSipSigPortInterface_Type.__name__ = "Integer32"
_SonusSipSigPortInterface_Object = MibTableColumn
sonusSipSigPortInterface = _SonusSipSigPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 4),
    _SonusSipSigPortInterface_Type()
)
sonusSipSigPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortInterface.setStatus("current")


class _SonusSipSigPortRole_Type(Integer32):
    """Custom type sonusSipSigPortRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SonusSipSigPortRole_Type.__name__ = "Integer32"
_SonusSipSigPortRole_Object = MibTableColumn
sonusSipSigPortRole = _SonusSipSigPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 5),
    _SonusSipSigPortRole_Type()
)
sonusSipSigPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortRole.setStatus("current")


class _SonusSipSigPortMode_Type(SonusServiceState):
    """Custom type sonusSipSigPortMode based on SonusServiceState"""


_SonusSipSigPortMode_Object = MibTableColumn
sonusSipSigPortMode = _SonusSipSigPortMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 6),
    _SonusSipSigPortMode_Type()
)
sonusSipSigPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortMode.setStatus("current")


class _SonusSipSigPortState_Type(SonusAdminState):
    """Custom type sonusSipSigPortState based on SonusAdminState"""


_SonusSipSigPortState_Object = MibTableColumn
sonusSipSigPortState = _SonusSipSigPortState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 7),
    _SonusSipSigPortState_Type()
)
sonusSipSigPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortState.setStatus("current")
_SonusSipSigPortRowStatus_Type = RowStatus
_SonusSipSigPortRowStatus_Object = MibTableColumn
sonusSipSigPortRowStatus = _SonusSipSigPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 8),
    _SonusSipSigPortRowStatus_Type()
)
sonusSipSigPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortRowStatus.setStatus("current")


class _SonusSipSigPortAclState_Type(SonusAdminState):
    """Custom type sonusSipSigPortAclState based on SonusAdminState"""


_SonusSipSigPortAclState_Object = MibTableColumn
sonusSipSigPortAclState = _SonusSipSigPortAclState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 3, 1, 9),
    _SonusSipSigPortAclState_Type()
)
sonusSipSigPortAclState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortAclState.setStatus("current")
_SonusSipSigPortStatusTable_Object = MibTable
sonusSipSigPortStatusTable = _SonusSipSigPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4)
)
if mibBuilder.loadTexts:
    sonusSipSigPortStatusTable.setStatus("current")
_SonusSipSigPortStatusEntry_Object = MibTableRow
sonusSipSigPortStatusEntry = _SonusSipSigPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1)
)
sonusSipSigPortStatusEntry.setIndexNames(
    (0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusSipSigPortStatusEntry.setStatus("current")
_SonusSipSigPortStatusIndex_Type = Integer32
_SonusSipSigPortStatusIndex_Object = MibTableColumn
sonusSipSigPortStatusIndex = _SonusSipSigPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 1),
    _SonusSipSigPortStatusIndex_Type()
)
sonusSipSigPortStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusIndex.setStatus("current")
_SonusSipSigPortStatusIpAddress_Type = IpAddress
_SonusSipSigPortStatusIpAddress_Object = MibTableColumn
sonusSipSigPortStatusIpAddress = _SonusSipSigPortStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 2),
    _SonusSipSigPortStatusIpAddress_Type()
)
sonusSipSigPortStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusIpAddress.setStatus("current")


class _SonusSipSigPortStatusNum_Type(Integer32):
    """Custom type sonusSipSigPortStatusNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSipSigPortStatusNum_Type.__name__ = "Integer32"
_SonusSipSigPortStatusNum_Object = MibTableColumn
sonusSipSigPortStatusNum = _SonusSipSigPortStatusNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 3),
    _SonusSipSigPortStatusNum_Type()
)
sonusSipSigPortStatusNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusNum.setStatus("current")


class _SonusSipSigPortStatusInterface_Type(Integer32):
    """Custom type sonusSipSigPortStatusInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgtNif", 1),
          ("nif", 2))
    )


_SonusSipSigPortStatusInterface_Type.__name__ = "Integer32"
_SonusSipSigPortStatusInterface_Object = MibTableColumn
sonusSipSigPortStatusInterface = _SonusSipSigPortStatusInterface_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 4),
    _SonusSipSigPortStatusInterface_Type()
)
sonusSipSigPortStatusInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusInterface.setStatus("current")


class _SonusSipSigPortStatusRole_Type(Integer32):
    """Custom type sonusSipSigPortStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SonusSipSigPortStatusRole_Type.__name__ = "Integer32"
_SonusSipSigPortStatusRole_Object = MibTableColumn
sonusSipSigPortStatusRole = _SonusSipSigPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 5),
    _SonusSipSigPortStatusRole_Type()
)
sonusSipSigPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusRole.setStatus("current")
_SonusSipSigPortStatusNif_Type = Integer32
_SonusSipSigPortStatusNif_Object = MibTableColumn
sonusSipSigPortStatusNif = _SonusSipSigPortStatusNif_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 6),
    _SonusSipSigPortStatusNif_Type()
)
sonusSipSigPortStatusNif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusNif.setStatus("current")
_SonusSipSigPortStatusState_Type = SonusServiceState
_SonusSipSigPortStatusState_Object = MibTableColumn
sonusSipSigPortStatusState = _SonusSipSigPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 4, 1, 7),
    _SonusSipSigPortStatusState_Type()
)
sonusSipSigPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatusState.setStatus("current")
_SonusSipSigPortStatTable_Object = MibTable
sonusSipSigPortStatTable = _SonusSipSigPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5)
)
if mibBuilder.loadTexts:
    sonusSipSigPortStatTable.setStatus("current")
_SonusSipSigPortStatEntry_Object = MibTableRow
sonusSipSigPortStatEntry = _SonusSipSigPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1)
)
sonusSipSigPortStatEntry.setIndexNames(
    (0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortStatIndex"),
)
if mibBuilder.loadTexts:
    sonusSipSigPortStatEntry.setStatus("current")
_SonusSipSigPortStatIndex_Type = Integer32
_SonusSipSigPortStatIndex_Object = MibTableColumn
sonusSipSigPortStatIndex = _SonusSipSigPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 1),
    _SonusSipSigPortStatIndex_Type()
)
sonusSipSigPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatIndex.setStatus("current")
_SonusSipSigPortStatIpAddress_Type = IpAddress
_SonusSipSigPortStatIpAddress_Object = MibTableColumn
sonusSipSigPortStatIpAddress = _SonusSipSigPortStatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 2),
    _SonusSipSigPortStatIpAddress_Type()
)
sonusSipSigPortStatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatIpAddress.setStatus("current")


class _SonusSipSigPortStatPortNum_Type(Integer32):
    """Custom type sonusSipSigPortStatPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SonusSipSigPortStatPortNum_Type.__name__ = "Integer32"
_SonusSipSigPortStatPortNum_Object = MibTableColumn
sonusSipSigPortStatPortNum = _SonusSipSigPortStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 3),
    _SonusSipSigPortStatPortNum_Type()
)
sonusSipSigPortStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatPortNum.setStatus("current")


class _SonusSipSigPortStatCountReset_Type(Integer32):
    """Custom type sonusSipSigPortStatCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unknown", 1))
    )


_SonusSipSigPortStatCountReset_Type.__name__ = "Integer32"
_SonusSipSigPortStatCountReset_Object = MibTableColumn
sonusSipSigPortStatCountReset = _SonusSipSigPortStatCountReset_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 4),
    _SonusSipSigPortStatCountReset_Type()
)
sonusSipSigPortStatCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipSigPortStatCountReset.setStatus("current")
_SonusSipSigPortStatCallRate_Type = Integer32
_SonusSipSigPortStatCallRate_Object = MibTableColumn
sonusSipSigPortStatCallRate = _SonusSipSigPortStatCallRate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 5),
    _SonusSipSigPortStatCallRate_Type()
)
sonusSipSigPortStatCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatCallRate.setStatus("current")
_SonusSipSigPortStatNumOrigCalls_Type = Integer32
_SonusSipSigPortStatNumOrigCalls_Object = MibTableColumn
sonusSipSigPortStatNumOrigCalls = _SonusSipSigPortStatNumOrigCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 6),
    _SonusSipSigPortStatNumOrigCalls_Type()
)
sonusSipSigPortStatNumOrigCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumOrigCalls.setStatus("current")
_SonusSipSigPortStatNumTermCalls_Type = Integer32
_SonusSipSigPortStatNumTermCalls_Object = MibTableColumn
sonusSipSigPortStatNumTermCalls = _SonusSipSigPortStatNumTermCalls_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 7),
    _SonusSipSigPortStatNumTermCalls_Type()
)
sonusSipSigPortStatNumTermCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumTermCalls.setStatus("current")
_SonusSipSigPortStatNumTxPdus_Type = Counter64
_SonusSipSigPortStatNumTxPdus_Object = MibTableColumn
sonusSipSigPortStatNumTxPdus = _SonusSipSigPortStatNumTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 8),
    _SonusSipSigPortStatNumTxPdus_Type()
)
sonusSipSigPortStatNumTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumTxPdus.setStatus("current")
_SonusSipSigPortStatNumRxPdus_Type = Counter64
_SonusSipSigPortStatNumRxPdus_Object = MibTableColumn
sonusSipSigPortStatNumRxPdus = _SonusSipSigPortStatNumRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 9),
    _SonusSipSigPortStatNumRxPdus_Type()
)
sonusSipSigPortStatNumRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumRxPdus.setStatus("current")
_SonusSipSigPortStatNumTxBytes_Type = Counter64
_SonusSipSigPortStatNumTxBytes_Object = MibTableColumn
sonusSipSigPortStatNumTxBytes = _SonusSipSigPortStatNumTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 10),
    _SonusSipSigPortStatNumTxBytes_Type()
)
sonusSipSigPortStatNumTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumTxBytes.setStatus("current")
_SonusSipSigPortStatNumRxBytes_Type = Counter64
_SonusSipSigPortStatNumRxBytes_Object = MibTableColumn
sonusSipSigPortStatNumRxBytes = _SonusSipSigPortStatNumRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 5, 1, 11),
    _SonusSipSigPortStatNumRxBytes_Type()
)
sonusSipSigPortStatNumRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipSigPortStatNumRxBytes.setStatus("current")
_SonusSipAcl_ObjectIdentity = ObjectIdentity
sonusSipAcl = _SonusSipAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6)
)
_SonusSipAclNextIndex_Type = Integer32
_SonusSipAclNextIndex_Object = MibScalar
sonusSipAclNextIndex = _SonusSipAclNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 1),
    _SonusSipAclNextIndex_Type()
)
sonusSipAclNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipAclNextIndex.setStatus("current")
_SonusSipAclTable_Object = MibTable
sonusSipAclTable = _SonusSipAclTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sonusSipAclTable.setStatus("current")
_SonusSipAclEntry_Object = MibTableRow
sonusSipAclEntry = _SonusSipAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1)
)
sonusSipAclEntry.setIndexNames(
    (0, "SONUS-SIP-SIGNALLING-MIB", "sonusSipRemoteAppSvrIndex"),
)
if mibBuilder.loadTexts:
    sonusSipAclEntry.setStatus("current")
_SonusSipRemoteAppSvrIndex_Type = Integer32
_SonusSipRemoteAppSvrIndex_Object = MibTableColumn
sonusSipRemoteAppSvrIndex = _SonusSipRemoteAppSvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 1),
    _SonusSipRemoteAppSvrIndex_Type()
)
sonusSipRemoteAppSvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSipRemoteAppSvrIndex.setStatus("current")
_SonusSipRemoteAppSvrName_Type = SonusName
_SonusSipRemoteAppSvrName_Object = MibTableColumn
sonusSipRemoteAppSvrName = _SonusSipRemoteAppSvrName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 2),
    _SonusSipRemoteAppSvrName_Type()
)
sonusSipRemoteAppSvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipRemoteAppSvrName.setStatus("current")
_SonusSipRemoteAppSvrIpAddress_Type = IpAddress
_SonusSipRemoteAppSvrIpAddress_Object = MibTableColumn
sonusSipRemoteAppSvrIpAddress = _SonusSipRemoteAppSvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 3),
    _SonusSipRemoteAppSvrIpAddress_Type()
)
sonusSipRemoteAppSvrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipRemoteAppSvrIpAddress.setStatus("current")
_SonusSipRemoteAppSvrRowStatus_Type = RowStatus
_SonusSipRemoteAppSvrRowStatus_Object = MibTableColumn
sonusSipRemoteAppSvrRowStatus = _SonusSipRemoteAppSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 1, 6, 2, 1, 4),
    _SonusSipRemoteAppSvrRowStatus_Type()
)
sonusSipRemoteAppSvrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSipRemoteAppSvrRowStatus.setStatus("current")
_SonusSipSignallingMIBNotifications_ObjectIdentity = ObjectIdentity
sonusSipSignallingMIBNotifications = _SonusSipSignallingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2)
)
_SonusSipSignallingMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusSipSignallingMIBNotificationsPrefix = _SonusSipSignallingMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0)
)
_SonusSipSignallingMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusSipSignallingMIBNotificationsObjects = _SonusSipSignallingMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 1)
)

# Managed Objects groups


# Notification objects

sonusSipCallSigPortOpenNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0, 1)
)
sonusSipCallSigPortOpenNotification.setObjects(
      *(("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIpAddress"),
        ("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortNum"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSipCallSigPortOpenNotification.setStatus(
        "current"
    )

sonusSipCallSigPortCloseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 7, 2, 0, 2)
)
sonusSipCallSigPortCloseNotification.setObjects(
      *(("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortIpAddress"),
        ("SONUS-SIP-SIGNALLING-MIB", "sonusSipSigPortNum"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusSipCallSigPortCloseNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-SIP-SIGNALLING-MIB",
    **{"sonusSipSignallingMIB": sonusSipSignallingMIB,
       "sonusSipSignallingMIBObjects": sonusSipSignallingMIBObjects,
       "sonusSipSigTimerObjects": sonusSipSigTimerObjects,
       "sonusSipSigTimerT1": sonusSipSigTimerT1,
       "sonusSipSigTimerT2": sonusSipSigTimerT2,
       "sonusSipSigTimerSessionKeepalive": sonusSipSigTimerSessionKeepalive,
       "sonusSipSigRetryObjects": sonusSipSigRetryObjects,
       "sonusSipSigNumOfRetry": sonusSipSigNumOfRetry,
       "sonusSipSigInviteRetry": sonusSipSigInviteRetry,
       "sonusSipSigPortTable": sonusSipSigPortTable,
       "sonusSipSigPortEntry": sonusSipSigPortEntry,
       "sonusSipSigPortIndex": sonusSipSigPortIndex,
       "sonusSipSigPortIpAddress": sonusSipSigPortIpAddress,
       "sonusSipSigPortNum": sonusSipSigPortNum,
       "sonusSipSigPortInterface": sonusSipSigPortInterface,
       "sonusSipSigPortRole": sonusSipSigPortRole,
       "sonusSipSigPortMode": sonusSipSigPortMode,
       "sonusSipSigPortState": sonusSipSigPortState,
       "sonusSipSigPortRowStatus": sonusSipSigPortRowStatus,
       "sonusSipSigPortAclState": sonusSipSigPortAclState,
       "sonusSipSigPortStatusTable": sonusSipSigPortStatusTable,
       "sonusSipSigPortStatusEntry": sonusSipSigPortStatusEntry,
       "sonusSipSigPortStatusIndex": sonusSipSigPortStatusIndex,
       "sonusSipSigPortStatusIpAddress": sonusSipSigPortStatusIpAddress,
       "sonusSipSigPortStatusNum": sonusSipSigPortStatusNum,
       "sonusSipSigPortStatusInterface": sonusSipSigPortStatusInterface,
       "sonusSipSigPortStatusRole": sonusSipSigPortStatusRole,
       "sonusSipSigPortStatusNif": sonusSipSigPortStatusNif,
       "sonusSipSigPortStatusState": sonusSipSigPortStatusState,
       "sonusSipSigPortStatTable": sonusSipSigPortStatTable,
       "sonusSipSigPortStatEntry": sonusSipSigPortStatEntry,
       "sonusSipSigPortStatIndex": sonusSipSigPortStatIndex,
       "sonusSipSigPortStatIpAddress": sonusSipSigPortStatIpAddress,
       "sonusSipSigPortStatPortNum": sonusSipSigPortStatPortNum,
       "sonusSipSigPortStatCountReset": sonusSipSigPortStatCountReset,
       "sonusSipSigPortStatCallRate": sonusSipSigPortStatCallRate,
       "sonusSipSigPortStatNumOrigCalls": sonusSipSigPortStatNumOrigCalls,
       "sonusSipSigPortStatNumTermCalls": sonusSipSigPortStatNumTermCalls,
       "sonusSipSigPortStatNumTxPdus": sonusSipSigPortStatNumTxPdus,
       "sonusSipSigPortStatNumRxPdus": sonusSipSigPortStatNumRxPdus,
       "sonusSipSigPortStatNumTxBytes": sonusSipSigPortStatNumTxBytes,
       "sonusSipSigPortStatNumRxBytes": sonusSipSigPortStatNumRxBytes,
       "sonusSipAcl": sonusSipAcl,
       "sonusSipAclNextIndex": sonusSipAclNextIndex,
       "sonusSipAclTable": sonusSipAclTable,
       "sonusSipAclEntry": sonusSipAclEntry,
       "sonusSipRemoteAppSvrIndex": sonusSipRemoteAppSvrIndex,
       "sonusSipRemoteAppSvrName": sonusSipRemoteAppSvrName,
       "sonusSipRemoteAppSvrIpAddress": sonusSipRemoteAppSvrIpAddress,
       "sonusSipRemoteAppSvrRowStatus": sonusSipRemoteAppSvrRowStatus,
       "sonusSipSignallingMIBNotifications": sonusSipSignallingMIBNotifications,
       "sonusSipSignallingMIBNotificationsPrefix": sonusSipSignallingMIBNotificationsPrefix,
       "sonusSipCallSigPortOpenNotification": sonusSipCallSigPortOpenNotification,
       "sonusSipCallSigPortCloseNotification": sonusSipCallSigPortCloseNotification,
       "sonusSipSignallingMIBNotificationsObjects": sonusSipSignallingMIBNotificationsObjects}
)
