# SNMP MIB module (SYSAPPL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYSAPPL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:52 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

sysApplMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 54)
)
sysApplMIB.setRevisions(
        ("2006-01-06 00:00",
         "1997-10-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RunState(Integer32, TextualConvention):
    status = "current"
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
        *(("exiting", 4),
          ("other", 5),
          ("runnable", 2),
          ("running", 1),
          ("waiting", 3))
    )



class LongUtf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "1024a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



class Utf8String(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SysApplOBJ_ObjectIdentity = ObjectIdentity
sysApplOBJ = _SysApplOBJ_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 1)
)
_SysApplInstalled_ObjectIdentity = ObjectIdentity
sysApplInstalled = _SysApplInstalled_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 1, 1)
)
_SysApplInstallPkgTable_Object = MibTable
sysApplInstallPkgTable = _SysApplInstallPkgTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sysApplInstallPkgTable.setStatus("current")
_SysApplInstallPkgEntry_Object = MibTableRow
sysApplInstallPkgEntry = _SysApplInstallPkgEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1)
)
sysApplInstallPkgEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"),
)
if mibBuilder.loadTexts:
    sysApplInstallPkgEntry.setStatus("current")


class _SysApplInstallPkgIndex_Type(Unsigned32):
    """Custom type sysApplInstallPkgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplInstallPkgIndex_Type.__name__ = "Unsigned32"
_SysApplInstallPkgIndex_Object = MibTableColumn
sysApplInstallPkgIndex = _SysApplInstallPkgIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 1),
    _SysApplInstallPkgIndex_Type()
)
sysApplInstallPkgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplInstallPkgIndex.setStatus("current")
_SysApplInstallPkgManufacturer_Type = Utf8String
_SysApplInstallPkgManufacturer_Object = MibTableColumn
sysApplInstallPkgManufacturer = _SysApplInstallPkgManufacturer_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 2),
    _SysApplInstallPkgManufacturer_Type()
)
sysApplInstallPkgManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgManufacturer.setStatus("current")
_SysApplInstallPkgProductName_Type = Utf8String
_SysApplInstallPkgProductName_Object = MibTableColumn
sysApplInstallPkgProductName = _SysApplInstallPkgProductName_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 3),
    _SysApplInstallPkgProductName_Type()
)
sysApplInstallPkgProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgProductName.setStatus("current")
_SysApplInstallPkgVersion_Type = Utf8String
_SysApplInstallPkgVersion_Object = MibTableColumn
sysApplInstallPkgVersion = _SysApplInstallPkgVersion_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 4),
    _SysApplInstallPkgVersion_Type()
)
sysApplInstallPkgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgVersion.setStatus("current")
_SysApplInstallPkgSerialNumber_Type = Utf8String
_SysApplInstallPkgSerialNumber_Object = MibTableColumn
sysApplInstallPkgSerialNumber = _SysApplInstallPkgSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 5),
    _SysApplInstallPkgSerialNumber_Type()
)
sysApplInstallPkgSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgSerialNumber.setStatus("current")
_SysApplInstallPkgDate_Type = DateAndTime
_SysApplInstallPkgDate_Object = MibTableColumn
sysApplInstallPkgDate = _SysApplInstallPkgDate_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 6),
    _SysApplInstallPkgDate_Type()
)
sysApplInstallPkgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgDate.setStatus("current")
_SysApplInstallPkgLocation_Type = LongUtf8String
_SysApplInstallPkgLocation_Object = MibTableColumn
sysApplInstallPkgLocation = _SysApplInstallPkgLocation_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 7),
    _SysApplInstallPkgLocation_Type()
)
sysApplInstallPkgLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallPkgLocation.setStatus("current")
_SysApplInstallElmtTable_Object = MibTable
sysApplInstallElmtTable = _SysApplInstallElmtTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sysApplInstallElmtTable.setStatus("current")
_SysApplInstallElmtEntry_Object = MibTableRow
sysApplInstallElmtEntry = _SysApplInstallElmtEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1)
)
sysApplInstallElmtEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"),
    (0, "SYSAPPL-MIB", "sysApplInstallElmtIndex"),
)
if mibBuilder.loadTexts:
    sysApplInstallElmtEntry.setStatus("current")


class _SysApplInstallElmtIndex_Type(Unsigned32):
    """Custom type sysApplInstallElmtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplInstallElmtIndex_Type.__name__ = "Unsigned32"
_SysApplInstallElmtIndex_Object = MibTableColumn
sysApplInstallElmtIndex = _SysApplInstallElmtIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 1),
    _SysApplInstallElmtIndex_Type()
)
sysApplInstallElmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplInstallElmtIndex.setStatus("current")
_SysApplInstallElmtName_Type = Utf8String
_SysApplInstallElmtName_Object = MibTableColumn
sysApplInstallElmtName = _SysApplInstallElmtName_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 2),
    _SysApplInstallElmtName_Type()
)
sysApplInstallElmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtName.setStatus("current")


class _SysApplInstallElmtType_Type(Integer32):
    """Custom type sysApplInstallElmtType based on Integer32"""
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
        *(("application", 5),
          ("deviceDriver", 4),
          ("nonexecutable", 2),
          ("operatingSystem", 3),
          ("unknown", 1))
    )


_SysApplInstallElmtType_Type.__name__ = "Integer32"
_SysApplInstallElmtType_Object = MibTableColumn
sysApplInstallElmtType = _SysApplInstallElmtType_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 3),
    _SysApplInstallElmtType_Type()
)
sysApplInstallElmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtType.setStatus("current")
_SysApplInstallElmtDate_Type = DateAndTime
_SysApplInstallElmtDate_Object = MibTableColumn
sysApplInstallElmtDate = _SysApplInstallElmtDate_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 4),
    _SysApplInstallElmtDate_Type()
)
sysApplInstallElmtDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtDate.setStatus("current")
_SysApplInstallElmtPath_Type = LongUtf8String
_SysApplInstallElmtPath_Object = MibTableColumn
sysApplInstallElmtPath = _SysApplInstallElmtPath_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 5),
    _SysApplInstallElmtPath_Type()
)
sysApplInstallElmtPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtPath.setStatus("current")
_SysApplInstallElmtSizeHigh_Type = Unsigned32
_SysApplInstallElmtSizeHigh_Object = MibTableColumn
sysApplInstallElmtSizeHigh = _SysApplInstallElmtSizeHigh_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 6),
    _SysApplInstallElmtSizeHigh_Type()
)
sysApplInstallElmtSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtSizeHigh.setStatus("current")
_SysApplInstallElmtSizeLow_Type = Unsigned32
_SysApplInstallElmtSizeLow_Object = MibTableColumn
sysApplInstallElmtSizeLow = _SysApplInstallElmtSizeLow_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 7),
    _SysApplInstallElmtSizeLow_Type()
)
sysApplInstallElmtSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtSizeLow.setStatus("current")


class _SysApplInstallElmtRole_Type(OctetString):
    """Custom type sysApplInstallElmtRole based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SysApplInstallElmtRole_Type.__name__ = "OctetString"
_SysApplInstallElmtRole_Object = MibTableColumn
sysApplInstallElmtRole = _SysApplInstallElmtRole_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 8),
    _SysApplInstallElmtRole_Type()
)
sysApplInstallElmtRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplInstallElmtRole.setStatus("current")
_SysApplInstallElmtModifyDate_Type = DateAndTime
_SysApplInstallElmtModifyDate_Object = MibTableColumn
sysApplInstallElmtModifyDate = _SysApplInstallElmtModifyDate_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 9),
    _SysApplInstallElmtModifyDate_Type()
)
sysApplInstallElmtModifyDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtModifyDate.setStatus("current")
_SysApplInstallElmtCurSizeHigh_Type = Unsigned32
_SysApplInstallElmtCurSizeHigh_Object = MibTableColumn
sysApplInstallElmtCurSizeHigh = _SysApplInstallElmtCurSizeHigh_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 10),
    _SysApplInstallElmtCurSizeHigh_Type()
)
sysApplInstallElmtCurSizeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtCurSizeHigh.setStatus("current")
_SysApplInstallElmtCurSizeLow_Type = Unsigned32
_SysApplInstallElmtCurSizeLow_Object = MibTableColumn
sysApplInstallElmtCurSizeLow = _SysApplInstallElmtCurSizeLow_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 11),
    _SysApplInstallElmtCurSizeLow_Type()
)
sysApplInstallElmtCurSizeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplInstallElmtCurSizeLow.setStatus("current")
_SysApplRun_ObjectIdentity = ObjectIdentity
sysApplRun = _SysApplRun_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 1, 2)
)
_SysApplRunTable_Object = MibTable
sysApplRunTable = _SysApplRunTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sysApplRunTable.setStatus("current")
_SysApplRunEntry_Object = MibTableRow
sysApplRunEntry = _SysApplRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1)
)
sysApplRunEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"),
    (0, "SYSAPPL-MIB", "sysApplRunIndex"),
)
if mibBuilder.loadTexts:
    sysApplRunEntry.setStatus("current")


class _SysApplRunIndex_Type(Unsigned32):
    """Custom type sysApplRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplRunIndex_Type.__name__ = "Unsigned32"
_SysApplRunIndex_Object = MibTableColumn
sysApplRunIndex = _SysApplRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 1),
    _SysApplRunIndex_Type()
)
sysApplRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplRunIndex.setStatus("current")
_SysApplRunStarted_Type = DateAndTime
_SysApplRunStarted_Object = MibTableColumn
sysApplRunStarted = _SysApplRunStarted_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 2),
    _SysApplRunStarted_Type()
)
sysApplRunStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplRunStarted.setStatus("current")
_SysApplRunCurrentState_Type = RunState
_SysApplRunCurrentState_Object = MibTableColumn
sysApplRunCurrentState = _SysApplRunCurrentState_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 3),
    _SysApplRunCurrentState_Type()
)
sysApplRunCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplRunCurrentState.setStatus("current")
_SysApplPastRunTable_Object = MibTable
sysApplPastRunTable = _SysApplPastRunTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sysApplPastRunTable.setStatus("current")
_SysApplPastRunEntry_Object = MibTableRow
sysApplPastRunEntry = _SysApplPastRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1)
)
sysApplPastRunEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"),
    (0, "SYSAPPL-MIB", "sysApplPastRunIndex"),
)
if mibBuilder.loadTexts:
    sysApplPastRunEntry.setStatus("current")


class _SysApplPastRunIndex_Type(Unsigned32):
    """Custom type sysApplPastRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplPastRunIndex_Type.__name__ = "Unsigned32"
_SysApplPastRunIndex_Object = MibTableColumn
sysApplPastRunIndex = _SysApplPastRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 1),
    _SysApplPastRunIndex_Type()
)
sysApplPastRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplPastRunIndex.setStatus("current")
_SysApplPastRunStarted_Type = DateAndTime
_SysApplPastRunStarted_Object = MibTableColumn
sysApplPastRunStarted = _SysApplPastRunStarted_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 2),
    _SysApplPastRunStarted_Type()
)
sysApplPastRunStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplPastRunStarted.setStatus("current")


class _SysApplPastRunExitState_Type(Integer32):
    """Custom type sysApplPastRunExitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("failed", 2),
          ("other", 3))
    )


_SysApplPastRunExitState_Type.__name__ = "Integer32"
_SysApplPastRunExitState_Object = MibTableColumn
sysApplPastRunExitState = _SysApplPastRunExitState_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 3),
    _SysApplPastRunExitState_Type()
)
sysApplPastRunExitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplPastRunExitState.setStatus("current")
_SysApplPastRunTimeEnded_Type = DateAndTime
_SysApplPastRunTimeEnded_Object = MibTableColumn
sysApplPastRunTimeEnded = _SysApplPastRunTimeEnded_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 4),
    _SysApplPastRunTimeEnded_Type()
)
sysApplPastRunTimeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplPastRunTimeEnded.setStatus("current")
_SysApplElmtRunTable_Object = MibTable
sysApplElmtRunTable = _SysApplElmtRunTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sysApplElmtRunTable.setStatus("current")
_SysApplElmtRunEntry_Object = MibTableRow
sysApplElmtRunEntry = _SysApplElmtRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1)
)
sysApplElmtRunEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplElmtRunInstallPkg"),
    (0, "SYSAPPL-MIB", "sysApplElmtRunInvocID"),
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
)
if mibBuilder.loadTexts:
    sysApplElmtRunEntry.setStatus("current")


class _SysApplElmtRunInstallPkg_Type(Unsigned32):
    """Custom type sysApplElmtRunInstallPkg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtRunInstallPkg_Type.__name__ = "Unsigned32"
_SysApplElmtRunInstallPkg_Object = MibTableColumn
sysApplElmtRunInstallPkg = _SysApplElmtRunInstallPkg_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 1),
    _SysApplElmtRunInstallPkg_Type()
)
sysApplElmtRunInstallPkg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplElmtRunInstallPkg.setStatus("current")


class _SysApplElmtRunInvocID_Type(Unsigned32):
    """Custom type sysApplElmtRunInvocID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtRunInvocID_Type.__name__ = "Unsigned32"
_SysApplElmtRunInvocID_Object = MibTableColumn
sysApplElmtRunInvocID = _SysApplElmtRunInvocID_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 2),
    _SysApplElmtRunInvocID_Type()
)
sysApplElmtRunInvocID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplElmtRunInvocID.setStatus("current")


class _SysApplElmtRunIndex_Type(Unsigned32):
    """Custom type sysApplElmtRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtRunIndex_Type.__name__ = "Unsigned32"
_SysApplElmtRunIndex_Object = MibTableColumn
sysApplElmtRunIndex = _SysApplElmtRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 3),
    _SysApplElmtRunIndex_Type()
)
sysApplElmtRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplElmtRunIndex.setStatus("current")


class _SysApplElmtRunInstallID_Type(Unsigned32):
    """Custom type sysApplElmtRunInstallID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtRunInstallID_Type.__name__ = "Unsigned32"
_SysApplElmtRunInstallID_Object = MibTableColumn
sysApplElmtRunInstallID = _SysApplElmtRunInstallID_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 4),
    _SysApplElmtRunInstallID_Type()
)
sysApplElmtRunInstallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunInstallID.setStatus("current")
_SysApplElmtRunTimeStarted_Type = DateAndTime
_SysApplElmtRunTimeStarted_Object = MibTableColumn
sysApplElmtRunTimeStarted = _SysApplElmtRunTimeStarted_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 5),
    _SysApplElmtRunTimeStarted_Type()
)
sysApplElmtRunTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunTimeStarted.setStatus("current")
_SysApplElmtRunState_Type = RunState
_SysApplElmtRunState_Object = MibTableColumn
sysApplElmtRunState = _SysApplElmtRunState_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 6),
    _SysApplElmtRunState_Type()
)
sysApplElmtRunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunState.setStatus("current")
_SysApplElmtRunName_Type = LongUtf8String
_SysApplElmtRunName_Object = MibTableColumn
sysApplElmtRunName = _SysApplElmtRunName_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 7),
    _SysApplElmtRunName_Type()
)
sysApplElmtRunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunName.setStatus("current")
_SysApplElmtRunParameters_Type = Utf8String
_SysApplElmtRunParameters_Object = MibTableColumn
sysApplElmtRunParameters = _SysApplElmtRunParameters_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 8),
    _SysApplElmtRunParameters_Type()
)
sysApplElmtRunParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunParameters.setStatus("current")
_SysApplElmtRunCPU_Type = TimeTicks
_SysApplElmtRunCPU_Object = MibTableColumn
sysApplElmtRunCPU = _SysApplElmtRunCPU_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 9),
    _SysApplElmtRunCPU_Type()
)
sysApplElmtRunCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunCPU.setStatus("current")
_SysApplElmtRunMemory_Type = Gauge32
_SysApplElmtRunMemory_Object = MibTableColumn
sysApplElmtRunMemory = _SysApplElmtRunMemory_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 10),
    _SysApplElmtRunMemory_Type()
)
sysApplElmtRunMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunMemory.setStatus("current")
if mibBuilder.loadTexts:
    sysApplElmtRunMemory.setUnits("Kbytes")
_SysApplElmtRunNumFiles_Type = Gauge32
_SysApplElmtRunNumFiles_Object = MibTableColumn
sysApplElmtRunNumFiles = _SysApplElmtRunNumFiles_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 11),
    _SysApplElmtRunNumFiles_Type()
)
sysApplElmtRunNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunNumFiles.setStatus("current")
_SysApplElmtRunUser_Type = Utf8String
_SysApplElmtRunUser_Object = MibTableColumn
sysApplElmtRunUser = _SysApplElmtRunUser_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 12),
    _SysApplElmtRunUser_Type()
)
sysApplElmtRunUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtRunUser.setStatus("current")
_SysApplElmtPastRunTable_Object = MibTable
sysApplElmtPastRunTable = _SysApplElmtPastRunTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sysApplElmtPastRunTable.setStatus("current")
_SysApplElmtPastRunEntry_Object = MibTableRow
sysApplElmtPastRunEntry = _SysApplElmtPastRunEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1)
)
sysApplElmtPastRunEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"),
    (0, "SYSAPPL-MIB", "sysApplElmtPastRunInvocID"),
    (0, "SYSAPPL-MIB", "sysApplElmtPastRunIndex"),
)
if mibBuilder.loadTexts:
    sysApplElmtPastRunEntry.setStatus("current")


class _SysApplElmtPastRunInvocID_Type(Unsigned32):
    """Custom type sysApplElmtPastRunInvocID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplElmtPastRunInvocID_Type.__name__ = "Unsigned32"
_SysApplElmtPastRunInvocID_Object = MibTableColumn
sysApplElmtPastRunInvocID = _SysApplElmtPastRunInvocID_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 1),
    _SysApplElmtPastRunInvocID_Type()
)
sysApplElmtPastRunInvocID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplElmtPastRunInvocID.setStatus("current")


class _SysApplElmtPastRunIndex_Type(Unsigned32):
    """Custom type sysApplElmtPastRunIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtPastRunIndex_Type.__name__ = "Unsigned32"
_SysApplElmtPastRunIndex_Object = MibTableColumn
sysApplElmtPastRunIndex = _SysApplElmtPastRunIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 2),
    _SysApplElmtPastRunIndex_Type()
)
sysApplElmtPastRunIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplElmtPastRunIndex.setStatus("current")


class _SysApplElmtPastRunInstallID_Type(Unsigned32):
    """Custom type sysApplElmtPastRunInstallID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SysApplElmtPastRunInstallID_Type.__name__ = "Unsigned32"
_SysApplElmtPastRunInstallID_Object = MibTableColumn
sysApplElmtPastRunInstallID = _SysApplElmtPastRunInstallID_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 3),
    _SysApplElmtPastRunInstallID_Type()
)
sysApplElmtPastRunInstallID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunInstallID.setStatus("current")
_SysApplElmtPastRunTimeStarted_Type = DateAndTime
_SysApplElmtPastRunTimeStarted_Object = MibTableColumn
sysApplElmtPastRunTimeStarted = _SysApplElmtPastRunTimeStarted_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 4),
    _SysApplElmtPastRunTimeStarted_Type()
)
sysApplElmtPastRunTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunTimeStarted.setStatus("current")
_SysApplElmtPastRunTimeEnded_Type = DateAndTime
_SysApplElmtPastRunTimeEnded_Object = MibTableColumn
sysApplElmtPastRunTimeEnded = _SysApplElmtPastRunTimeEnded_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 5),
    _SysApplElmtPastRunTimeEnded_Type()
)
sysApplElmtPastRunTimeEnded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunTimeEnded.setStatus("current")
_SysApplElmtPastRunName_Type = LongUtf8String
_SysApplElmtPastRunName_Object = MibTableColumn
sysApplElmtPastRunName = _SysApplElmtPastRunName_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 6),
    _SysApplElmtPastRunName_Type()
)
sysApplElmtPastRunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunName.setStatus("current")
_SysApplElmtPastRunParameters_Type = Utf8String
_SysApplElmtPastRunParameters_Object = MibTableColumn
sysApplElmtPastRunParameters = _SysApplElmtPastRunParameters_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 7),
    _SysApplElmtPastRunParameters_Type()
)
sysApplElmtPastRunParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunParameters.setStatus("current")
_SysApplElmtPastRunCPU_Type = TimeTicks
_SysApplElmtPastRunCPU_Object = MibTableColumn
sysApplElmtPastRunCPU = _SysApplElmtPastRunCPU_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 8),
    _SysApplElmtPastRunCPU_Type()
)
sysApplElmtPastRunCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunCPU.setStatus("current")


class _SysApplElmtPastRunMemory_Type(Unsigned32):
    """Custom type sysApplElmtPastRunMemory based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtPastRunMemory_Type.__name__ = "Unsigned32"
_SysApplElmtPastRunMemory_Object = MibTableColumn
sysApplElmtPastRunMemory = _SysApplElmtPastRunMemory_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 9),
    _SysApplElmtPastRunMemory_Type()
)
sysApplElmtPastRunMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunMemory.setStatus("current")
if mibBuilder.loadTexts:
    sysApplElmtPastRunMemory.setUnits("Kbytes")


class _SysApplElmtPastRunNumFiles_Type(Unsigned32):
    """Custom type sysApplElmtPastRunNumFiles based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElmtPastRunNumFiles_Type.__name__ = "Unsigned32"
_SysApplElmtPastRunNumFiles_Object = MibTableColumn
sysApplElmtPastRunNumFiles = _SysApplElmtPastRunNumFiles_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 10),
    _SysApplElmtPastRunNumFiles_Type()
)
sysApplElmtPastRunNumFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunNumFiles.setStatus("current")
_SysApplElmtPastRunUser_Type = Utf8String
_SysApplElmtPastRunUser_Object = MibTableColumn
sysApplElmtPastRunUser = _SysApplElmtPastRunUser_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 11),
    _SysApplElmtPastRunUser_Type()
)
sysApplElmtPastRunUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElmtPastRunUser.setStatus("current")


class _SysApplPastRunMaxRows_Type(Unsigned32):
    """Custom type sysApplPastRunMaxRows based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplPastRunMaxRows_Type.__name__ = "Unsigned32"
_SysApplPastRunMaxRows_Object = MibScalar
sysApplPastRunMaxRows = _SysApplPastRunMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 5),
    _SysApplPastRunMaxRows_Type()
)
sysApplPastRunMaxRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplPastRunMaxRows.setStatus("current")
_SysApplPastRunTableRemItems_Type = Counter32
_SysApplPastRunTableRemItems_Object = MibScalar
sysApplPastRunTableRemItems = _SysApplPastRunTableRemItems_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 6),
    _SysApplPastRunTableRemItems_Type()
)
sysApplPastRunTableRemItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplPastRunTableRemItems.setStatus("current")


class _SysApplPastRunTblTimeLimit_Type(Unsigned32):
    """Custom type sysApplPastRunTblTimeLimit based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplPastRunTblTimeLimit_Type.__name__ = "Unsigned32"
_SysApplPastRunTblTimeLimit_Object = MibScalar
sysApplPastRunTblTimeLimit = _SysApplPastRunTblTimeLimit_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 7),
    _SysApplPastRunTblTimeLimit_Type()
)
sysApplPastRunTblTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplPastRunTblTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    sysApplPastRunTblTimeLimit.setUnits("seconds")


class _SysApplElemPastRunMaxRows_Type(Unsigned32):
    """Custom type sysApplElemPastRunMaxRows based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElemPastRunMaxRows_Type.__name__ = "Unsigned32"
_SysApplElemPastRunMaxRows_Object = MibScalar
sysApplElemPastRunMaxRows = _SysApplElemPastRunMaxRows_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 8),
    _SysApplElemPastRunMaxRows_Type()
)
sysApplElemPastRunMaxRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplElemPastRunMaxRows.setStatus("current")
_SysApplElemPastRunTableRemItems_Type = Counter32
_SysApplElemPastRunTableRemItems_Object = MibScalar
sysApplElemPastRunTableRemItems = _SysApplElemPastRunTableRemItems_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 9),
    _SysApplElemPastRunTableRemItems_Type()
)
sysApplElemPastRunTableRemItems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplElemPastRunTableRemItems.setStatus("current")


class _SysApplElemPastRunTblTimeLimit_Type(Unsigned32):
    """Custom type sysApplElemPastRunTblTimeLimit based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplElemPastRunTblTimeLimit_Type.__name__ = "Unsigned32"
_SysApplElemPastRunTblTimeLimit_Object = MibScalar
sysApplElemPastRunTblTimeLimit = _SysApplElemPastRunTblTimeLimit_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 10),
    _SysApplElemPastRunTblTimeLimit_Type()
)
sysApplElemPastRunTblTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplElemPastRunTblTimeLimit.setStatus("current")
if mibBuilder.loadTexts:
    sysApplElemPastRunTblTimeLimit.setUnits("seconds")


class _SysApplAgentPollInterval_Type(Unsigned32):
    """Custom type sysApplAgentPollInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplAgentPollInterval_Type.__name__ = "Unsigned32"
_SysApplAgentPollInterval_Object = MibScalar
sysApplAgentPollInterval = _SysApplAgentPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 2, 11),
    _SysApplAgentPollInterval_Type()
)
sysApplAgentPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysApplAgentPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    sysApplAgentPollInterval.setUnits("seconds")
_SysApplMap_ObjectIdentity = ObjectIdentity
sysApplMap = _SysApplMap_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 1, 3)
)
_SysApplMapTable_Object = MibTable
sysApplMapTable = _SysApplMapTable_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 3, 1)
)
if mibBuilder.loadTexts:
    sysApplMapTable.setStatus("current")
_SysApplMapEntry_Object = MibTableRow
sysApplMapEntry = _SysApplMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1)
)
sysApplMapEntry.setIndexNames(
    (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"),
    (0, "SYSAPPL-MIB", "sysApplElmtRunInvocID"),
    (0, "SYSAPPL-MIB", "sysApplMapInstallElmtIndex"),
)
if mibBuilder.loadTexts:
    sysApplMapEntry.setStatus("current")


class _SysApplMapInstallElmtIndex_Type(Unsigned32):
    """Custom type sysApplMapInstallElmtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplMapInstallElmtIndex_Type.__name__ = "Unsigned32"
_SysApplMapInstallElmtIndex_Object = MibTableColumn
sysApplMapInstallElmtIndex = _SysApplMapInstallElmtIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1, 1),
    _SysApplMapInstallElmtIndex_Type()
)
sysApplMapInstallElmtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysApplMapInstallElmtIndex.setStatus("current")


class _SysApplMapInstallPkgIndex_Type(Unsigned32):
    """Custom type sysApplMapInstallPkgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SysApplMapInstallPkgIndex_Type.__name__ = "Unsigned32"
_SysApplMapInstallPkgIndex_Object = MibTableColumn
sysApplMapInstallPkgIndex = _SysApplMapInstallPkgIndex_Object(
    (1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1, 2),
    _SysApplMapInstallPkgIndex_Type()
)
sysApplMapInstallPkgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysApplMapInstallPkgIndex.setStatus("current")
_SysApplNotifications_ObjectIdentity = ObjectIdentity
sysApplNotifications = _SysApplNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 2)
)
_SysApplConformance_ObjectIdentity = ObjectIdentity
sysApplConformance = _SysApplConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 3)
)
_SysApplMIBCompliances_ObjectIdentity = ObjectIdentity
sysApplMIBCompliances = _SysApplMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 3, 1)
)
_SysApplMIBGroups_ObjectIdentity = ObjectIdentity
sysApplMIBGroups = _SysApplMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 54, 3, 2)
)

# Managed Objects groups

sysApplInstalledGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 54, 3, 2, 1)
)
sysApplInstalledGroup.setObjects(
      *(("SYSAPPL-MIB", "sysApplInstallPkgManufacturer"),
        ("SYSAPPL-MIB", "sysApplInstallPkgProductName"),
        ("SYSAPPL-MIB", "sysApplInstallPkgVersion"),
        ("SYSAPPL-MIB", "sysApplInstallPkgSerialNumber"),
        ("SYSAPPL-MIB", "sysApplInstallPkgDate"),
        ("SYSAPPL-MIB", "sysApplInstallPkgLocation"),
        ("SYSAPPL-MIB", "sysApplInstallElmtName"),
        ("SYSAPPL-MIB", "sysApplInstallElmtType"),
        ("SYSAPPL-MIB", "sysApplInstallElmtDate"),
        ("SYSAPPL-MIB", "sysApplInstallElmtPath"),
        ("SYSAPPL-MIB", "sysApplInstallElmtSizeHigh"),
        ("SYSAPPL-MIB", "sysApplInstallElmtSizeLow"),
        ("SYSAPPL-MIB", "sysApplInstallElmtRole"),
        ("SYSAPPL-MIB", "sysApplInstallElmtModifyDate"),
        ("SYSAPPL-MIB", "sysApplInstallElmtCurSizeHigh"),
        ("SYSAPPL-MIB", "sysApplInstallElmtCurSizeLow"))
)
if mibBuilder.loadTexts:
    sysApplInstalledGroup.setStatus("current")

sysApplRunGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 54, 3, 2, 2)
)
sysApplRunGroup.setObjects(
      *(("SYSAPPL-MIB", "sysApplRunStarted"),
        ("SYSAPPL-MIB", "sysApplRunCurrentState"),
        ("SYSAPPL-MIB", "sysApplPastRunStarted"),
        ("SYSAPPL-MIB", "sysApplPastRunExitState"),
        ("SYSAPPL-MIB", "sysApplPastRunTimeEnded"),
        ("SYSAPPL-MIB", "sysApplElmtRunInstallID"),
        ("SYSAPPL-MIB", "sysApplElmtRunTimeStarted"),
        ("SYSAPPL-MIB", "sysApplElmtRunState"),
        ("SYSAPPL-MIB", "sysApplElmtRunName"),
        ("SYSAPPL-MIB", "sysApplElmtRunParameters"),
        ("SYSAPPL-MIB", "sysApplElmtRunCPU"),
        ("SYSAPPL-MIB", "sysApplElmtRunMemory"),
        ("SYSAPPL-MIB", "sysApplElmtRunNumFiles"),
        ("SYSAPPL-MIB", "sysApplElmtRunUser"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunInstallID"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunTimeStarted"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunTimeEnded"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunName"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunParameters"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunCPU"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunMemory"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunNumFiles"),
        ("SYSAPPL-MIB", "sysApplElmtPastRunUser"),
        ("SYSAPPL-MIB", "sysApplPastRunMaxRows"),
        ("SYSAPPL-MIB", "sysApplPastRunTableRemItems"),
        ("SYSAPPL-MIB", "sysApplPastRunTblTimeLimit"),
        ("SYSAPPL-MIB", "sysApplElemPastRunMaxRows"),
        ("SYSAPPL-MIB", "sysApplElemPastRunTableRemItems"),
        ("SYSAPPL-MIB", "sysApplElemPastRunTblTimeLimit"),
        ("SYSAPPL-MIB", "sysApplAgentPollInterval"))
)
if mibBuilder.loadTexts:
    sysApplRunGroup.setStatus("current")

sysApplMapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 54, 3, 2, 3)
)
sysApplMapGroup.setObjects(
    ("SYSAPPL-MIB", "sysApplMapInstallPkgIndex")
)
if mibBuilder.loadTexts:
    sysApplMapGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sysApplMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 54, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sysApplMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSAPPL-MIB",
    **{"RunState": RunState,
       "LongUtf8String": LongUtf8String,
       "Utf8String": Utf8String,
       "sysApplMIB": sysApplMIB,
       "sysApplOBJ": sysApplOBJ,
       "sysApplInstalled": sysApplInstalled,
       "sysApplInstallPkgTable": sysApplInstallPkgTable,
       "sysApplInstallPkgEntry": sysApplInstallPkgEntry,
       "sysApplInstallPkgIndex": sysApplInstallPkgIndex,
       "sysApplInstallPkgManufacturer": sysApplInstallPkgManufacturer,
       "sysApplInstallPkgProductName": sysApplInstallPkgProductName,
       "sysApplInstallPkgVersion": sysApplInstallPkgVersion,
       "sysApplInstallPkgSerialNumber": sysApplInstallPkgSerialNumber,
       "sysApplInstallPkgDate": sysApplInstallPkgDate,
       "sysApplInstallPkgLocation": sysApplInstallPkgLocation,
       "sysApplInstallElmtTable": sysApplInstallElmtTable,
       "sysApplInstallElmtEntry": sysApplInstallElmtEntry,
       "sysApplInstallElmtIndex": sysApplInstallElmtIndex,
       "sysApplInstallElmtName": sysApplInstallElmtName,
       "sysApplInstallElmtType": sysApplInstallElmtType,
       "sysApplInstallElmtDate": sysApplInstallElmtDate,
       "sysApplInstallElmtPath": sysApplInstallElmtPath,
       "sysApplInstallElmtSizeHigh": sysApplInstallElmtSizeHigh,
       "sysApplInstallElmtSizeLow": sysApplInstallElmtSizeLow,
       "sysApplInstallElmtRole": sysApplInstallElmtRole,
       "sysApplInstallElmtModifyDate": sysApplInstallElmtModifyDate,
       "sysApplInstallElmtCurSizeHigh": sysApplInstallElmtCurSizeHigh,
       "sysApplInstallElmtCurSizeLow": sysApplInstallElmtCurSizeLow,
       "sysApplRun": sysApplRun,
       "sysApplRunTable": sysApplRunTable,
       "sysApplRunEntry": sysApplRunEntry,
       "sysApplRunIndex": sysApplRunIndex,
       "sysApplRunStarted": sysApplRunStarted,
       "sysApplRunCurrentState": sysApplRunCurrentState,
       "sysApplPastRunTable": sysApplPastRunTable,
       "sysApplPastRunEntry": sysApplPastRunEntry,
       "sysApplPastRunIndex": sysApplPastRunIndex,
       "sysApplPastRunStarted": sysApplPastRunStarted,
       "sysApplPastRunExitState": sysApplPastRunExitState,
       "sysApplPastRunTimeEnded": sysApplPastRunTimeEnded,
       "sysApplElmtRunTable": sysApplElmtRunTable,
       "sysApplElmtRunEntry": sysApplElmtRunEntry,
       "sysApplElmtRunInstallPkg": sysApplElmtRunInstallPkg,
       "sysApplElmtRunInvocID": sysApplElmtRunInvocID,
       "sysApplElmtRunIndex": sysApplElmtRunIndex,
       "sysApplElmtRunInstallID": sysApplElmtRunInstallID,
       "sysApplElmtRunTimeStarted": sysApplElmtRunTimeStarted,
       "sysApplElmtRunState": sysApplElmtRunState,
       "sysApplElmtRunName": sysApplElmtRunName,
       "sysApplElmtRunParameters": sysApplElmtRunParameters,
       "sysApplElmtRunCPU": sysApplElmtRunCPU,
       "sysApplElmtRunMemory": sysApplElmtRunMemory,
       "sysApplElmtRunNumFiles": sysApplElmtRunNumFiles,
       "sysApplElmtRunUser": sysApplElmtRunUser,
       "sysApplElmtPastRunTable": sysApplElmtPastRunTable,
       "sysApplElmtPastRunEntry": sysApplElmtPastRunEntry,
       "sysApplElmtPastRunInvocID": sysApplElmtPastRunInvocID,
       "sysApplElmtPastRunIndex": sysApplElmtPastRunIndex,
       "sysApplElmtPastRunInstallID": sysApplElmtPastRunInstallID,
       "sysApplElmtPastRunTimeStarted": sysApplElmtPastRunTimeStarted,
       "sysApplElmtPastRunTimeEnded": sysApplElmtPastRunTimeEnded,
       "sysApplElmtPastRunName": sysApplElmtPastRunName,
       "sysApplElmtPastRunParameters": sysApplElmtPastRunParameters,
       "sysApplElmtPastRunCPU": sysApplElmtPastRunCPU,
       "sysApplElmtPastRunMemory": sysApplElmtPastRunMemory,
       "sysApplElmtPastRunNumFiles": sysApplElmtPastRunNumFiles,
       "sysApplElmtPastRunUser": sysApplElmtPastRunUser,
       "sysApplPastRunMaxRows": sysApplPastRunMaxRows,
       "sysApplPastRunTableRemItems": sysApplPastRunTableRemItems,
       "sysApplPastRunTblTimeLimit": sysApplPastRunTblTimeLimit,
       "sysApplElemPastRunMaxRows": sysApplElemPastRunMaxRows,
       "sysApplElemPastRunTableRemItems": sysApplElemPastRunTableRemItems,
       "sysApplElemPastRunTblTimeLimit": sysApplElemPastRunTblTimeLimit,
       "sysApplAgentPollInterval": sysApplAgentPollInterval,
       "sysApplMap": sysApplMap,
       "sysApplMapTable": sysApplMapTable,
       "sysApplMapEntry": sysApplMapEntry,
       "sysApplMapInstallElmtIndex": sysApplMapInstallElmtIndex,
       "sysApplMapInstallPkgIndex": sysApplMapInstallPkgIndex,
       "sysApplNotifications": sysApplNotifications,
       "sysApplConformance": sysApplConformance,
       "sysApplMIBCompliances": sysApplMIBCompliances,
       "sysApplMIBCompliance": sysApplMIBCompliance,
       "sysApplMIBGroups": sysApplMIBGroups,
       "sysApplInstalledGroup": sysApplInstalledGroup,
       "sysApplRunGroup": sysApplRunGroup,
       "sysApplMapGroup": sysApplMapGroup}
)
