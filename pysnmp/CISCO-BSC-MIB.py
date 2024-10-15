# SNMP MIB module (CISCO-BSC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BSC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoBscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36)
)
ciscoBscMIB.setRevisions(
        ("2004-08-25 00:00",
         "1997-01-25 00:00",
         "1995-08-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BscObjects_ObjectIdentity = ObjectIdentity
bscObjects = _BscObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1)
)
_BscPorts_ObjectIdentity = ObjectIdentity
bscPorts = _BscPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1)
)
_BscPortTable_Object = MibTable
bscPortTable = _BscPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1)
)
if mibBuilder.loadTexts:
    bscPortTable.setStatus("current")
_BscPortEntry_Object = MibTableRow
bscPortEntry = _BscPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1)
)
bscPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bscPortEntry.setStatus("current")


class _BscPortRole_Type(Integer32):
    """Custom type bscPortRole based on Integer32"""
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
        *(("contention", 3),
          ("dialContention", 4),
          ("generic", 5),
          ("primary", 1),
          ("secondary", 2))
    )


_BscPortRole_Type.__name__ = "Integer32"
_BscPortRole_Object = MibTableColumn
bscPortRole = _BscPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 1),
    _BscPortRole_Type()
)
bscPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortRole.setStatus("current")


class _BscPortCodeSet_Type(Integer32):
    """Custom type bscPortCodeSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("ebcdic", 1))
    )


_BscPortCodeSet_Type.__name__ = "Integer32"
_BscPortCodeSet_Object = MibTableColumn
bscPortCodeSet = _BscPortCodeSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 2),
    _BscPortCodeSet_Type()
)
bscPortCodeSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortCodeSet.setStatus("current")


class _BscPortPause_Type(Integer32):
    """Custom type bscPortPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BscPortPause_Type.__name__ = "Integer32"
_BscPortPause_Object = MibTableColumn
bscPortPause = _BscPortPause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 3),
    _BscPortPause_Type()
)
bscPortPause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortPause.setStatus("current")


class _BscPortServlim_Type(Integer32):
    """Custom type bscPortServlim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_BscPortServlim_Type.__name__ = "Integer32"
_BscPortServlim_Object = MibTableColumn
bscPortServlim = _BscPortServlim_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 4),
    _BscPortServlim_Type()
)
bscPortServlim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortServlim.setStatus("current")


class _BscPortPollTimeout_Type(Integer32):
    """Custom type bscPortPollTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BscPortPollTimeout_Type.__name__ = "Integer32"
_BscPortPollTimeout_Object = MibTableColumn
bscPortPollTimeout = _BscPortPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 5),
    _BscPortPollTimeout_Type()
)
bscPortPollTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortPollTimeout.setStatus("current")


class _BscPortRecoveryRetries_Type(Integer32):
    """Custom type bscPortRecoveryRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BscPortRecoveryRetries_Type.__name__ = "Integer32"
_BscPortRecoveryRetries_Object = MibTableColumn
bscPortRecoveryRetries = _BscPortRecoveryRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 6),
    _BscPortRecoveryRetries_Type()
)
bscPortRecoveryRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortRecoveryRetries.setStatus("current")
_BscPortUnknownControlUnitsReceived_Type = Counter32
_BscPortUnknownControlUnitsReceived_Object = MibTableColumn
bscPortUnknownControlUnitsReceived = _BscPortUnknownControlUnitsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 7),
    _BscPortUnknownControlUnitsReceived_Type()
)
bscPortUnknownControlUnitsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortUnknownControlUnitsReceived.setStatus("current")
_BscPortSoftErrors_Type = Counter32
_BscPortSoftErrors_Object = MibTableColumn
bscPortSoftErrors = _BscPortSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 8),
    _BscPortSoftErrors_Type()
)
bscPortSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortSoftErrors.setStatus("current")
_BscPortHardErrors_Type = Counter32
_BscPortHardErrors_Object = MibTableColumn
bscPortHardErrors = _BscPortHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 9),
    _BscPortHardErrors_Type()
)
bscPortHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortHardErrors.setStatus("current")
_BscPortProtocolViolations_Type = Counter32
_BscPortProtocolViolations_Object = MibTableColumn
bscPortProtocolViolations = _BscPortProtocolViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 10),
    _BscPortProtocolViolations_Type()
)
bscPortProtocolViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortProtocolViolations.setStatus("current")


class _BscPortHostTimeout_Type(Integer32):
    """Custom type bscPortHostTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_BscPortHostTimeout_Type.__name__ = "Integer32"
_BscPortHostTimeout_Object = MibTableColumn
bscPortHostTimeout = _BscPortHostTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 11),
    _BscPortHostTimeout_Type()
)
bscPortHostTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortHostTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bscPortHostTimeout.setUnits("deciseconds")
_BscPortSpecPoll_Type = TruthValue
_BscPortSpecPoll_Object = MibTableColumn
bscPortSpecPoll = _BscPortSpecPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 12),
    _BscPortSpecPoll_Type()
)
bscPortSpecPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortSpecPoll.setStatus("current")


class _BscPortVirtualAddress_Type(Integer32):
    """Custom type bscPortVirtualAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_BscPortVirtualAddress_Type.__name__ = "Integer32"
_BscPortVirtualAddress_Object = MibTableColumn
bscPortVirtualAddress = _BscPortVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 13),
    _BscPortVirtualAddress_Type()
)
bscPortVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortVirtualAddress.setStatus("current")


class _BscPortContentionDialTimeout_Type(Integer32):
    """Custom type bscPortContentionDialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_BscPortContentionDialTimeout_Type.__name__ = "Integer32"
_BscPortContentionDialTimeout_Object = MibTableColumn
bscPortContentionDialTimeout = _BscPortContentionDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 1, 1, 1, 14),
    _BscPortContentionDialTimeout_Type()
)
bscPortContentionDialTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscPortContentionDialTimeout.setStatus("current")
if mibBuilder.loadTexts:
    bscPortContentionDialTimeout.setUnits("seconds")
_BscControlUnits_ObjectIdentity = ObjectIdentity
bscControlUnits = _BscControlUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2)
)
_BscControlUnitTable_Object = MibTable
bscControlUnitTable = _BscControlUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bscControlUnitTable.setStatus("current")
_BscCUEntry_Object = MibTableRow
bscCUEntry = _BscCUEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1)
)
bscCUEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-BSC-MIB", "bscCUAddress"),
)
if mibBuilder.loadTexts:
    bscCUEntry.setStatus("current")


class _BscCUAddress_Type(Integer32):
    """Custom type bscCUAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BscCUAddress_Type.__name__ = "Integer32"
_BscCUAddress_Object = MibTableColumn
bscCUAddress = _BscCUAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 1),
    _BscCUAddress_Type()
)
bscCUAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bscCUAddress.setStatus("current")


class _BscCUState_Type(Integer32):
    """Custom type bscCUState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_BscCUState_Type.__name__ = "Integer32"
_BscCUState_Object = MibTableColumn
bscCUState = _BscCUState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 2),
    _BscCUState_Type()
)
bscCUState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUState.setStatus("current")
_BscCUBytesSent_Type = Counter32
_BscCUBytesSent_Object = MibTableColumn
bscCUBytesSent = _BscCUBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 3),
    _BscCUBytesSent_Type()
)
bscCUBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUBytesSent.setStatus("current")
_BscCUBytesReceived_Type = Counter32
_BscCUBytesReceived_Object = MibTableColumn
bscCUBytesReceived = _BscCUBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 4),
    _BscCUBytesReceived_Type()
)
bscCUBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUBytesReceived.setStatus("current")
_BscCUTotalFramesSent_Type = Counter32
_BscCUTotalFramesSent_Object = MibTableColumn
bscCUTotalFramesSent = _BscCUTotalFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 5),
    _BscCUTotalFramesSent_Type()
)
bscCUTotalFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUTotalFramesSent.setStatus("current")
_BscCUTotalFramesReceived_Type = Counter32
_BscCUTotalFramesReceived_Object = MibTableColumn
bscCUTotalFramesReceived = _BscCUTotalFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 6),
    _BscCUTotalFramesReceived_Type()
)
bscCUTotalFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUTotalFramesReceived.setStatus("current")
_BscCUDataFramesSent_Type = Counter32
_BscCUDataFramesSent_Object = MibTableColumn
bscCUDataFramesSent = _BscCUDataFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 7),
    _BscCUDataFramesSent_Type()
)
bscCUDataFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUDataFramesSent.setStatus("current")
_BscCUDataFramesReceived_Type = Counter32
_BscCUDataFramesReceived_Object = MibTableColumn
bscCUDataFramesReceived = _BscCUDataFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 8),
    _BscCUDataFramesReceived_Type()
)
bscCUDataFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUDataFramesReceived.setStatus("current")
_BscCUSoftErrors_Type = Counter32
_BscCUSoftErrors_Object = MibTableColumn
bscCUSoftErrors = _BscCUSoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 9),
    _BscCUSoftErrors_Type()
)
bscCUSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUSoftErrors.setStatus("current")
_BscCUHardErrors_Type = Counter32
_BscCUHardErrors_Object = MibTableColumn
bscCUHardErrors = _BscCUHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 10),
    _BscCUHardErrors_Type()
)
bscCUHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUHardErrors.setStatus("current")
_BscCUProtocolViolations_Type = Counter32
_BscCUProtocolViolations_Object = MibTableColumn
bscCUProtocolViolations = _BscCUProtocolViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 2, 1, 1, 11),
    _BscCUProtocolViolations_Type()
)
bscCUProtocolViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscCUProtocolViolations.setStatus("current")
_BscExtAddresses_ObjectIdentity = ObjectIdentity
bscExtAddresses = _BscExtAddresses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 3)
)
_BscExtAddressTable_Object = MibTable
bscExtAddressTable = _BscExtAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bscExtAddressTable.setStatus("current")
_BscExtAddressEntry_Object = MibTableRow
bscExtAddressEntry = _BscExtAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 3, 1, 1)
)
bscExtAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-BSC-MIB", "bscExtPollAddress"),
)
if mibBuilder.loadTexts:
    bscExtAddressEntry.setStatus("current")


class _BscExtPollAddress_Type(Integer32):
    """Custom type bscExtPollAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BscExtPollAddress_Type.__name__ = "Integer32"
_BscExtPollAddress_Object = MibTableColumn
bscExtPollAddress = _BscExtPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 3, 1, 1, 1),
    _BscExtPollAddress_Type()
)
bscExtPollAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bscExtPollAddress.setStatus("current")


class _BscExtSelectAddress_Type(Integer32):
    """Custom type bscExtSelectAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BscExtSelectAddress_Type.__name__ = "Integer32"
_BscExtSelectAddress_Object = MibTableColumn
bscExtSelectAddress = _BscExtSelectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 1, 3, 1, 1, 2),
    _BscExtSelectAddress_Type()
)
bscExtSelectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bscExtSelectAddress.setStatus("current")
_BscMibConformance_ObjectIdentity = ObjectIdentity
bscMibConformance = _BscMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3)
)
_BscMibCompliances_ObjectIdentity = ObjectIdentity
bscMibCompliances = _BscMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 1)
)
_BscMibGroups_ObjectIdentity = ObjectIdentity
bscMibGroups = _BscMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 2)
)

# Managed Objects groups

bscPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 2, 1)
)
bscPortsGroup.setObjects(
      *(("CISCO-BSC-MIB", "bscPortRole"),
        ("CISCO-BSC-MIB", "bscPortCodeSet"),
        ("CISCO-BSC-MIB", "bscPortPause"),
        ("CISCO-BSC-MIB", "bscPortServlim"),
        ("CISCO-BSC-MIB", "bscPortPollTimeout"),
        ("CISCO-BSC-MIB", "bscPortRecoveryRetries"),
        ("CISCO-BSC-MIB", "bscPortUnknownControlUnitsReceived"),
        ("CISCO-BSC-MIB", "bscPortSoftErrors"),
        ("CISCO-BSC-MIB", "bscPortHardErrors"),
        ("CISCO-BSC-MIB", "bscPortProtocolViolations"))
)
if mibBuilder.loadTexts:
    bscPortsGroup.setStatus("obsolete")

bscControlUnitsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 2, 2)
)
bscControlUnitsGroup.setObjects(
      *(("CISCO-BSC-MIB", "bscCUState"),
        ("CISCO-BSC-MIB", "bscCUBytesSent"),
        ("CISCO-BSC-MIB", "bscCUBytesReceived"),
        ("CISCO-BSC-MIB", "bscCUTotalFramesSent"),
        ("CISCO-BSC-MIB", "bscCUTotalFramesReceived"),
        ("CISCO-BSC-MIB", "bscCUDataFramesSent"),
        ("CISCO-BSC-MIB", "bscCUDataFramesReceived"),
        ("CISCO-BSC-MIB", "bscCUSoftErrors"),
        ("CISCO-BSC-MIB", "bscCUHardErrors"),
        ("CISCO-BSC-MIB", "bscCUProtocolViolations"))
)
if mibBuilder.loadTexts:
    bscControlUnitsGroup.setStatus("current")

bscPortsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 2, 3)
)
bscPortsGroupRev1.setObjects(
      *(("CISCO-BSC-MIB", "bscPortRole"),
        ("CISCO-BSC-MIB", "bscPortCodeSet"),
        ("CISCO-BSC-MIB", "bscPortPause"),
        ("CISCO-BSC-MIB", "bscPortServlim"),
        ("CISCO-BSC-MIB", "bscPortPollTimeout"),
        ("CISCO-BSC-MIB", "bscPortRecoveryRetries"),
        ("CISCO-BSC-MIB", "bscPortUnknownControlUnitsReceived"),
        ("CISCO-BSC-MIB", "bscPortSoftErrors"),
        ("CISCO-BSC-MIB", "bscPortHardErrors"),
        ("CISCO-BSC-MIB", "bscPortProtocolViolations"),
        ("CISCO-BSC-MIB", "bscPortHostTimeout"),
        ("CISCO-BSC-MIB", "bscPortSpecPoll"),
        ("CISCO-BSC-MIB", "bscPortVirtualAddress"),
        ("CISCO-BSC-MIB", "bscPortContentionDialTimeout"))
)
if mibBuilder.loadTexts:
    bscPortsGroupRev1.setStatus("current")

bscExtAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 2, 4)
)
bscExtAddressGroup.setObjects(
    ("CISCO-BSC-MIB", "bscExtSelectAddress")
)
if mibBuilder.loadTexts:
    bscExtAddressGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bscMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bscMibCompliance.setStatus(
        "obsolete"
    )

bscMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 36, 3, 1, 2)
)
if mibBuilder.loadTexts:
    bscMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BSC-MIB",
    **{"ciscoBscMIB": ciscoBscMIB,
       "bscObjects": bscObjects,
       "bscPorts": bscPorts,
       "bscPortTable": bscPortTable,
       "bscPortEntry": bscPortEntry,
       "bscPortRole": bscPortRole,
       "bscPortCodeSet": bscPortCodeSet,
       "bscPortPause": bscPortPause,
       "bscPortServlim": bscPortServlim,
       "bscPortPollTimeout": bscPortPollTimeout,
       "bscPortRecoveryRetries": bscPortRecoveryRetries,
       "bscPortUnknownControlUnitsReceived": bscPortUnknownControlUnitsReceived,
       "bscPortSoftErrors": bscPortSoftErrors,
       "bscPortHardErrors": bscPortHardErrors,
       "bscPortProtocolViolations": bscPortProtocolViolations,
       "bscPortHostTimeout": bscPortHostTimeout,
       "bscPortSpecPoll": bscPortSpecPoll,
       "bscPortVirtualAddress": bscPortVirtualAddress,
       "bscPortContentionDialTimeout": bscPortContentionDialTimeout,
       "bscControlUnits": bscControlUnits,
       "bscControlUnitTable": bscControlUnitTable,
       "bscCUEntry": bscCUEntry,
       "bscCUAddress": bscCUAddress,
       "bscCUState": bscCUState,
       "bscCUBytesSent": bscCUBytesSent,
       "bscCUBytesReceived": bscCUBytesReceived,
       "bscCUTotalFramesSent": bscCUTotalFramesSent,
       "bscCUTotalFramesReceived": bscCUTotalFramesReceived,
       "bscCUDataFramesSent": bscCUDataFramesSent,
       "bscCUDataFramesReceived": bscCUDataFramesReceived,
       "bscCUSoftErrors": bscCUSoftErrors,
       "bscCUHardErrors": bscCUHardErrors,
       "bscCUProtocolViolations": bscCUProtocolViolations,
       "bscExtAddresses": bscExtAddresses,
       "bscExtAddressTable": bscExtAddressTable,
       "bscExtAddressEntry": bscExtAddressEntry,
       "bscExtPollAddress": bscExtPollAddress,
       "bscExtSelectAddress": bscExtSelectAddress,
       "bscMibConformance": bscMibConformance,
       "bscMibCompliances": bscMibCompliances,
       "bscMibCompliance": bscMibCompliance,
       "bscMibComplianceRev1": bscMibComplianceRev1,
       "bscMibGroups": bscMibGroups,
       "bscPortsGroup": bscPortsGroup,
       "bscControlUnitsGroup": bscControlUnitsGroup,
       "bscPortsGroupRev1": bscPortsGroupRev1,
       "bscExtAddressGroup": bscExtAddressGroup}
)
