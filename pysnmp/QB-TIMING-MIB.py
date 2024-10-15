# SNMP MIB module (QB-TIMING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-TIMING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:47 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qbTimingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class QbTimingCableLength(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("length0to110ft", 1),
          ("length110to220ft", 2),
          ("length220to330ft", 3),
          ("length330to440ft", 4),
          ("length440to550ft", 5),
          ("length550to660ft", 6),
          ("lengthGreater660ft", 7))
    )



class QbTimingFraming(Integer32, TextualConvention):
    status = "current"
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
        *(("dsx1D4", 3),
          ("dsx1DS2M12", 10),
          ("dsx1E1", 4),
          ("dsx1E1CRC", 5),
          ("dsx1E1CRCMF", 7),
          ("dsx1E1MF", 6),
          ("dsx1E1Unframed", 9),
          ("dsx1ESF", 2),
          ("dsx1SF", 12),
          ("dsx1Unframed", 8),
          ("dsx2E2", 11),
          ("other", 1))
    )



class QbTimingPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("timing-port1", 1),
          ("timing-port2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_QbTimingObjects_ObjectIdentity = ObjectIdentity
qbTimingObjects = _QbTimingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1)
)
_QbTimingGroup_ObjectIdentity = ObjectIdentity
qbTimingGroup = _QbTimingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1)
)


class _QbTimingModeAdminStatus_Type(Integer32):
    """Custom type qbTimingModeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("freerun", 1),
          ("holdover", 8),
          ("loop", 3))
    )


_QbTimingModeAdminStatus_Type.__name__ = "Integer32"
_QbTimingModeAdminStatus_Object = MibScalar
qbTimingModeAdminStatus = _QbTimingModeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 1),
    _QbTimingModeAdminStatus_Type()
)
qbTimingModeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingModeAdminStatus.setStatus("current")


class _QbTimingModeOperStatus_Type(Integer32):
    """Custom type qbTimingModeOperStatus based on Integer32"""
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
        *(("external", 2),
          ("freerun", 1),
          ("holdoverAuto", 5),
          ("holdoverMntc", 4),
          ("loop", 3),
          ("notOperational", 6))
    )


_QbTimingModeOperStatus_Type.__name__ = "Integer32"
_QbTimingModeOperStatus_Object = MibScalar
qbTimingModeOperStatus = _QbTimingModeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 2),
    _QbTimingModeOperStatus_Type()
)
qbTimingModeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbTimingModeOperStatus.setStatus("current")


class _QbTimingOutputMode_Type(Integer32):
    """Custom type qbTimingOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("lock", 2),
          ("track", 3))
    )


_QbTimingOutputMode_Type.__name__ = "Integer32"
_QbTimingOutputMode_Object = MibScalar
qbTimingOutputMode = _QbTimingOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 3),
    _QbTimingOutputMode_Type()
)
qbTimingOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingOutputMode.setStatus("current")


class _QbTimingHoldoverCtl_Type(Integer32):
    """Custom type qbTimingHoldoverCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearholdover", 2),
          ("holdover", 1))
    )


_QbTimingHoldoverCtl_Type.__name__ = "Integer32"
_QbTimingHoldoverCtl_Object = MibScalar
qbTimingHoldoverCtl = _QbTimingHoldoverCtl_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 4),
    _QbTimingHoldoverCtl_Type()
)
qbTimingHoldoverCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingHoldoverCtl.setStatus("current")


class _QbTimingSourceStatus_Type(Integer32):
    """Custom type qbTimingSourceStatus based on Integer32"""
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


_QbTimingSourceStatus_Type.__name__ = "Integer32"
_QbTimingSourceStatus_Object = MibScalar
qbTimingSourceStatus = _QbTimingSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 5),
    _QbTimingSourceStatus_Type()
)
qbTimingSourceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingSourceStatus.setStatus("current")


class _QbTimingInLineRef_Type(InterfaceIndexOrZero):
    """Custom type qbTimingInLineRef based on InterfaceIndexOrZero"""
    defaultValue = 0


_QbTimingInLineRef_Object = MibScalar
qbTimingInLineRef = _QbTimingInLineRef_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 6),
    _QbTimingInLineRef_Type()
)
qbTimingInLineRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingInLineRef.setStatus("current")


class _QbTimingOutLineRef_Type(InterfaceIndexOrZero):
    """Custom type qbTimingOutLineRef based on InterfaceIndexOrZero"""
    defaultValue = 0


_QbTimingOutLineRef_Object = MibScalar
qbTimingOutLineRef = _QbTimingOutLineRef_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 7),
    _QbTimingOutLineRef_Type()
)
qbTimingOutLineRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingOutLineRef.setStatus("current")
_QbTimingPortTable_Object = MibTable
qbTimingPortTable = _QbTimingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8)
)
if mibBuilder.loadTexts:
    qbTimingPortTable.setStatus("current")
_QbTimingPortEntry_Object = MibTableRow
qbTimingPortEntry = _QbTimingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1)
)
qbTimingPortEntry.setIndexNames(
    (0, "QB-TIMING-MIB", "qbTimingPort"),
)
if mibBuilder.loadTexts:
    qbTimingPortEntry.setStatus("current")
_QbTimingPort_Type = QbTimingPort
_QbTimingPort_Object = MibTableColumn
qbTimingPort = _QbTimingPort_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 1),
    _QbTimingPort_Type()
)
qbTimingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qbTimingPort.setStatus("current")
_QbTimingPortName_Type = DisplayString
_QbTimingPortName_Object = MibTableColumn
qbTimingPortName = _QbTimingPortName_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 2),
    _QbTimingPortName_Type()
)
qbTimingPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbTimingPortName.setStatus("current")


class _QbTimingPortFormat_Type(Integer32):
    """Custom type qbTimingPortFormat based on Integer32"""
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
        *(("ds1", 1),
          ("e1", 2),
          ("noValue", 3))
    )


_QbTimingPortFormat_Type.__name__ = "Integer32"
_QbTimingPortFormat_Object = MibTableColumn
qbTimingPortFormat = _QbTimingPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 3),
    _QbTimingPortFormat_Type()
)
qbTimingPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingPortFormat.setStatus("current")


class _QbTimingPortLineCoding_Type(Integer32):
    """Custom type qbTimingPortLineCoding based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dsx1AMI", 5),
          ("dsx1B6ZS", 7),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("dsx1ZBTSI", 4),
          ("other", 6))
    )


_QbTimingPortLineCoding_Type.__name__ = "Integer32"
_QbTimingPortLineCoding_Object = MibTableColumn
qbTimingPortLineCoding = _QbTimingPortLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 4),
    _QbTimingPortLineCoding_Type()
)
qbTimingPortLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingPortLineCoding.setStatus("current")


class _QbTimingPortFraming_Type(QbTimingFraming):
    """Custom type qbTimingPortFraming based on QbTimingFraming"""


_QbTimingPortFraming_Object = MibTableColumn
qbTimingPortFraming = _QbTimingPortFraming_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 5),
    _QbTimingPortFraming_Type()
)
qbTimingPortFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingPortFraming.setStatus("current")


class _QbTimingPortCableLength_Type(QbTimingCableLength):
    """Custom type qbTimingPortCableLength based on QbTimingCableLength"""
    defaultValue = 1


_QbTimingPortCableLength_Object = MibTableColumn
qbTimingPortCableLength = _QbTimingPortCableLength_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 6),
    _QbTimingPortCableLength_Type()
)
qbTimingPortCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingPortCableLength.setStatus("current")


class _QbTimingPortImpedanceMode_Type(Integer32):
    """Custom type qbTimingPortImpedanceMode based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(75, 75),
        ValueRangeConstraint(120, 120),
    )


_QbTimingPortImpedanceMode_Type.__name__ = "Integer32"
_QbTimingPortImpedanceMode_Object = MibTableColumn
qbTimingPortImpedanceMode = _QbTimingPortImpedanceMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 7),
    _QbTimingPortImpedanceMode_Type()
)
qbTimingPortImpedanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbTimingPortImpedanceMode.setStatus("current")
if mibBuilder.loadTexts:
    qbTimingPortImpedanceMode.setUnits("in ohms")


class _QbTimingPortOperStatus_Type(Integer32):
    """Custom type qbTimingPortOperStatus based on Integer32"""
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
        *(("down", 2),
          ("eqpFailure", 4),
          ("los", 3),
          ("up", 1))
    )


_QbTimingPortOperStatus_Type.__name__ = "Integer32"
_QbTimingPortOperStatus_Object = MibTableColumn
qbTimingPortOperStatus = _QbTimingPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 8),
    _QbTimingPortOperStatus_Type()
)
qbTimingPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbTimingPortOperStatus.setStatus("current")


class _QbTimingPortInOperStatus_Type(Integer32):
    """Custom type qbTimingPortInOperStatus based on Integer32"""
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
        *(("down", 2),
          ("eqpFailure", 4),
          ("los", 3),
          ("up", 1))
    )


_QbTimingPortInOperStatus_Type.__name__ = "Integer32"
_QbTimingPortInOperStatus_Object = MibTableColumn
qbTimingPortInOperStatus = _QbTimingPortInOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 9),
    _QbTimingPortInOperStatus_Type()
)
qbTimingPortInOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbTimingPortInOperStatus.setStatus("current")
_QbTimingTables_ObjectIdentity = ObjectIdentity
qbTimingTables = _QbTimingTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 2)
)
_QbTimingConformance_ObjectIdentity = ObjectIdentity
qbTimingConformance = _QbTimingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 3)
)
_QbTimingCompliances_ObjectIdentity = ObjectIdentity
qbTimingCompliances = _QbTimingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 1)
)
_QbTimingGroups_ObjectIdentity = ObjectIdentity
qbTimingGroups = _QbTimingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 2)
)

# Managed Objects groups

qbTimingAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 2, 1)
)
qbTimingAllGroup.setObjects(
      *(("QB-TIMING-MIB", "qbTimingModeAdminStatus"),
        ("QB-TIMING-MIB", "qbTimingModeOperStatus"),
        ("QB-TIMING-MIB", "qbTimingOutputMode"),
        ("QB-TIMING-MIB", "qbTimingSourceStatus"),
        ("QB-TIMING-MIB", "qbTimingHoldoverCtl"),
        ("QB-TIMING-MIB", "qbTimingSourceStatus"),
        ("QB-TIMING-MIB", "qbTimingInLineRef"),
        ("QB-TIMING-MIB", "qbTimingOutLineRef"),
        ("QB-TIMING-MIB", "qbTimingPortName"),
        ("QB-TIMING-MIB", "qbTimingPortFormat"),
        ("QB-TIMING-MIB", "qbTimingPortLineCoding"),
        ("QB-TIMING-MIB", "qbTimingPortFraming"),
        ("QB-TIMING-MIB", "qbTimingPortCableLength"),
        ("QB-TIMING-MIB", "qbTimingPortImpedanceMode"),
        ("QB-TIMING-MIB", "qbTimingPortOperStatus"))
)
if mibBuilder.loadTexts:
    qbTimingAllGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbTimingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qbTimingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-TIMING-MIB",
    **{"QbTimingCableLength": QbTimingCableLength,
       "QbTimingFraming": QbTimingFraming,
       "QbTimingPort": QbTimingPort,
       "qbTimingMIB": qbTimingMIB,
       "qbTimingObjects": qbTimingObjects,
       "qbTimingGroup": qbTimingGroup,
       "qbTimingModeAdminStatus": qbTimingModeAdminStatus,
       "qbTimingModeOperStatus": qbTimingModeOperStatus,
       "qbTimingOutputMode": qbTimingOutputMode,
       "qbTimingHoldoverCtl": qbTimingHoldoverCtl,
       "qbTimingSourceStatus": qbTimingSourceStatus,
       "qbTimingInLineRef": qbTimingInLineRef,
       "qbTimingOutLineRef": qbTimingOutLineRef,
       "qbTimingPortTable": qbTimingPortTable,
       "qbTimingPortEntry": qbTimingPortEntry,
       "qbTimingPort": qbTimingPort,
       "qbTimingPortName": qbTimingPortName,
       "qbTimingPortFormat": qbTimingPortFormat,
       "qbTimingPortLineCoding": qbTimingPortLineCoding,
       "qbTimingPortFraming": qbTimingPortFraming,
       "qbTimingPortCableLength": qbTimingPortCableLength,
       "qbTimingPortImpedanceMode": qbTimingPortImpedanceMode,
       "qbTimingPortOperStatus": qbTimingPortOperStatus,
       "qbTimingPortInOperStatus": qbTimingPortInOperStatus,
       "qbTimingTables": qbTimingTables,
       "qbTimingConformance": qbTimingConformance,
       "qbTimingCompliances": qbTimingCompliances,
       "qbTimingCompliance": qbTimingCompliance,
       "qbTimingGroups": qbTimingGroups,
       "qbTimingAllGroup": qbTimingAllGroup}
)
