# SNMP MIB module (IBMACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMACCOUNTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:48 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_Ibmappn_ObjectIdentity = ObjectIdentity
ibmappn = _Ibmappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13)
)
_IbmappnSession_ObjectIdentity = ObjectIdentity
ibmappnSession = _IbmappnSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7)
)
_IbmappnSessIntermediate_ObjectIdentity = ObjectIdentity
ibmappnSessIntermediate = _IbmappnSessIntermediate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3)
)
_IbmappnIsAccounting_ObjectIdentity = ObjectIdentity
ibmappnIsAccounting = _IbmappnIsAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2)
)
_IbmappnIsAcGlobal_ObjectIdentity = ObjectIdentity
ibmappnIsAcGlobal = _IbmappnIsAcGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1)
)


class _IbmappnIsAcGlobeStatus_Type(Integer32):
    """Custom type ibmappnIsAcGlobeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeButFull", 3),
          ("activeNotFull", 2),
          ("notActive", 1))
    )


_IbmappnIsAcGlobeStatus_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeStatus_Object = MibScalar
ibmappnIsAcGlobeStatus = _IbmappnIsAcGlobeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 1),
    _IbmappnIsAcGlobeStatus_Type()
)
ibmappnIsAcGlobeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeStatus.setStatus("mandatory")


class _IbmappnIsAcGlobeByteThresh_Type(Integer32):
    """Custom type ibmappnIsAcGlobeByteThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcGlobeByteThresh_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeByteThresh_Object = MibScalar
ibmappnIsAcGlobeByteThresh = _IbmappnIsAcGlobeByteThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 2),
    _IbmappnIsAcGlobeByteThresh_Type()
)
ibmappnIsAcGlobeByteThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeByteThresh.setStatus("mandatory")


class _IbmappnIsAcGlobeCheckPt_Type(Integer32):
    """Custom type ibmappnIsAcGlobeCheckPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("yes", 2))
    )


_IbmappnIsAcGlobeCheckPt_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeCheckPt_Object = MibScalar
ibmappnIsAcGlobeCheckPt = _IbmappnIsAcGlobeCheckPt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 3),
    _IbmappnIsAcGlobeCheckPt_Type()
)
ibmappnIsAcGlobeCheckPt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeCheckPt.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcSecs_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcGlobeMgrUtcSecs_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcSecs_Object = MibScalar
ibmappnIsAcGlobeMgrUtcSecs = _IbmappnIsAcGlobeMgrUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 4),
    _IbmappnIsAcGlobeMgrUtcSecs_Type()
)
ibmappnIsAcGlobeMgrUtcSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcSecs.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcMins_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcGlobeMgrUtcMins_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcMins_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMins = _IbmappnIsAcGlobeMgrUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 5),
    _IbmappnIsAcGlobeMgrUtcMins_Type()
)
ibmappnIsAcGlobeMgrUtcMins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMins.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcHours_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_IbmappnIsAcGlobeMgrUtcHours_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcHours_Object = MibScalar
ibmappnIsAcGlobeMgrUtcHours = _IbmappnIsAcGlobeMgrUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 6),
    _IbmappnIsAcGlobeMgrUtcHours_Type()
)
ibmappnIsAcGlobeMgrUtcHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcHours.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcMdays_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcMdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnIsAcGlobeMgrUtcMdays_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcMdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMdays = _IbmappnIsAcGlobeMgrUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 7),
    _IbmappnIsAcGlobeMgrUtcMdays_Type()
)
ibmappnIsAcGlobeMgrUtcMdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMdays.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcGlobeMgrUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcMonths_Object = MibScalar
ibmappnIsAcGlobeMgrUtcMonths = _IbmappnIsAcGlobeMgrUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 8),
    _IbmappnIsAcGlobeMgrUtcMonths_Type()
)
ibmappnIsAcGlobeMgrUtcMonths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcMonths.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcYears_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcYears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IbmappnIsAcGlobeMgrUtcYears_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcYears_Object = MibScalar
ibmappnIsAcGlobeMgrUtcYears = _IbmappnIsAcGlobeMgrUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 9),
    _IbmappnIsAcGlobeMgrUtcYears_Type()
)
ibmappnIsAcGlobeMgrUtcYears.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcYears.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcWdays based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcGlobeMgrUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcWdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcWdays = _IbmappnIsAcGlobeMgrUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 10),
    _IbmappnIsAcGlobeMgrUtcWdays_Type()
)
ibmappnIsAcGlobeMgrUtcWdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcWdays.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrUtcYdays_Type(Integer32):
    """Custom type ibmappnIsAcGlobeMgrUtcYdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_IbmappnIsAcGlobeMgrUtcYdays_Type.__name__ = "Integer32"
_IbmappnIsAcGlobeMgrUtcYdays_Object = MibScalar
ibmappnIsAcGlobeMgrUtcYdays = _IbmappnIsAcGlobeMgrUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 11),
    _IbmappnIsAcGlobeMgrUtcYdays_Type()
)
ibmappnIsAcGlobeMgrUtcYdays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcYdays.setStatus("mandatory")
_IbmappnIsAcGlobeMgrUtcIsdst_Type = Integer32
_IbmappnIsAcGlobeMgrUtcIsdst_Object = MibScalar
ibmappnIsAcGlobeMgrUtcIsdst = _IbmappnIsAcGlobeMgrUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 12),
    _IbmappnIsAcGlobeMgrUtcIsdst_Type()
)
ibmappnIsAcGlobeMgrUtcIsdst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcGlobeMgrName_Type(DisplayString):
    """Custom type ibmappnIsAcGlobeMgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcGlobeMgrName_Type.__name__ = "DisplayString"
_IbmappnIsAcGlobeMgrName_Object = MibScalar
ibmappnIsAcGlobeMgrName = _IbmappnIsAcGlobeMgrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 1, 13),
    _IbmappnIsAcGlobeMgrName_Type()
)
ibmappnIsAcGlobeMgrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcGlobeMgrName.setStatus("mandatory")
_IbmappnIsAcBtypeTable_Object = MibTable
ibmappnIsAcBtypeTable = _IbmappnIsAcBtypeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeTable.setStatus("mandatory")
_IbmappnIsAcBtypeEntry_Object = MibTableRow
ibmappnIsAcBtypeEntry = _IbmappnIsAcBtypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1)
)
ibmappnIsAcBtypeEntry.setIndexNames(
    (0, "IBMACCOUNTING-MIB", "ibmappnIsAcBtypeMedia"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeEntry.setStatus("mandatory")


class _IbmappnIsAcBtypeMedia_Type(Integer32):
    """Custom type ibmappnIsAcBtypeMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dasd", 2),
          ("memory", 1))
    )


_IbmappnIsAcBtypeMedia_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeMedia_Object = MibTableColumn
ibmappnIsAcBtypeMedia = _IbmappnIsAcBtypeMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 1),
    _IbmappnIsAcBtypeMedia_Type()
)
ibmappnIsAcBtypeMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeMedia.setStatus("mandatory")


class _IbmappnIsAcBtypeActive_Type(Integer32):
    """Custom type ibmappnIsAcBtypeActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_IbmappnIsAcBtypeActive_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeActive_Object = MibTableColumn
ibmappnIsAcBtypeActive = _IbmappnIsAcBtypeActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 2),
    _IbmappnIsAcBtypeActive_Type()
)
ibmappnIsAcBtypeActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeActive.setStatus("mandatory")


class _IbmappnIsAcBtypeDirName_Type(DisplayString):
    """Custom type ibmappnIsAcBtypeDirName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IbmappnIsAcBtypeDirName_Type.__name__ = "DisplayString"
_IbmappnIsAcBtypeDirName_Object = MibTableColumn
ibmappnIsAcBtypeDirName = _IbmappnIsAcBtypeDirName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 3),
    _IbmappnIsAcBtypeDirName_Type()
)
ibmappnIsAcBtypeDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeDirName.setStatus("mandatory")


class _IbmappnIsAcBtypePrdMaxBufs_Type(Integer32):
    """Custom type ibmappnIsAcBtypePrdMaxBufs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypePrdMaxBufs_Type.__name__ = "Integer32"
_IbmappnIsAcBtypePrdMaxBufs_Object = MibTableColumn
ibmappnIsAcBtypePrdMaxBufs = _IbmappnIsAcBtypePrdMaxBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 4),
    _IbmappnIsAcBtypePrdMaxBufs_Type()
)
ibmappnIsAcBtypePrdMaxBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePrdMaxBufs.setStatus("mandatory")


class _IbmappnIsAcBtypeMaxBufs_Type(Integer32):
    """Custom type ibmappnIsAcBtypeMaxBufs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeMaxBufs_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeMaxBufs_Object = MibTableColumn
ibmappnIsAcBtypeMaxBufs = _IbmappnIsAcBtypeMaxBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 5),
    _IbmappnIsAcBtypeMaxBufs_Type()
)
ibmappnIsAcBtypeMaxBufs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeMaxBufs.setStatus("mandatory")
_IbmappnIsAcBtypeCurBufs_Type = Gauge32
_IbmappnIsAcBtypeCurBufs_Object = MibTableColumn
ibmappnIsAcBtypeCurBufs = _IbmappnIsAcBtypeCurBufs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 6),
    _IbmappnIsAcBtypeCurBufs_Type()
)
ibmappnIsAcBtypeCurBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeCurBufs.setStatus("mandatory")


class _IbmappnIsAcBtypePrdRecPerBuf_Type(Integer32):
    """Custom type ibmappnIsAcBtypePrdRecPerBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypePrdRecPerBuf_Type.__name__ = "Integer32"
_IbmappnIsAcBtypePrdRecPerBuf_Object = MibTableColumn
ibmappnIsAcBtypePrdRecPerBuf = _IbmappnIsAcBtypePrdRecPerBuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 7),
    _IbmappnIsAcBtypePrdRecPerBuf_Type()
)
ibmappnIsAcBtypePrdRecPerBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePrdRecPerBuf.setStatus("mandatory")


class _IbmappnIsAcBtypeRecPerBuf_Type(Integer32):
    """Custom type ibmappnIsAcBtypeRecPerBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeRecPerBuf_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeRecPerBuf_Object = MibTableColumn
ibmappnIsAcBtypeRecPerBuf = _IbmappnIsAcBtypeRecPerBuf_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 8),
    _IbmappnIsAcBtypeRecPerBuf_Type()
)
ibmappnIsAcBtypeRecPerBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeRecPerBuf.setStatus("mandatory")


class _IbmappnIsAcBtypeRecFormat_Type(Integer32):
    """Custom type ibmappnIsAcBtypeRecFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_IbmappnIsAcBtypeRecFormat_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeRecFormat_Object = MibTableColumn
ibmappnIsAcBtypeRecFormat = _IbmappnIsAcBtypeRecFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 9),
    _IbmappnIsAcBtypeRecFormat_Type()
)
ibmappnIsAcBtypeRecFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeRecFormat.setStatus("mandatory")


class _IbmappnIsAcBtypeFullAction_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halt", 1),
          ("wrap", 2))
    )


_IbmappnIsAcBtypeFullAction_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullAction_Object = MibTableColumn
ibmappnIsAcBtypeFullAction = _IbmappnIsAcBtypeFullAction_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 10),
    _IbmappnIsAcBtypeFullAction_Type()
)
ibmappnIsAcBtypeFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullAction.setStatus("mandatory")
_IbmappnIsAcBtypeFullTime_Type = TimeTicks
_IbmappnIsAcBtypeFullTime_Object = MibTableColumn
ibmappnIsAcBtypeFullTime = _IbmappnIsAcBtypeFullTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 11),
    _IbmappnIsAcBtypeFullTime_Type()
)
ibmappnIsAcBtypeFullTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullTime.setStatus("mandatory")


class _IbmappnIsAcBtypeFullReason_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullReason based on Integer32"""
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
        *(("ioErrors", 4),
          ("logicallyFull", 3),
          ("notFull", 1),
          ("physicallyFull", 2))
    )


_IbmappnIsAcBtypeFullReason_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullReason_Object = MibTableColumn
ibmappnIsAcBtypeFullReason = _IbmappnIsAcBtypeFullReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 12),
    _IbmappnIsAcBtypeFullReason_Type()
)
ibmappnIsAcBtypeFullReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullReason.setStatus("mandatory")


class _IbmappnIsAcBtypeFullWraps_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullWraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeFullWraps_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullWraps_Object = MibTableColumn
ibmappnIsAcBtypeFullWraps = _IbmappnIsAcBtypeFullWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 13),
    _IbmappnIsAcBtypeFullWraps_Type()
)
ibmappnIsAcBtypeFullWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullWraps.setStatus("mandatory")


class _IbmappnIsAcBtypeFullLosts_Type(Integer32):
    """Custom type ibmappnIsAcBtypeFullLosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeFullLosts_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeFullLosts_Object = MibTableColumn
ibmappnIsAcBtypeFullLosts = _IbmappnIsAcBtypeFullLosts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 14),
    _IbmappnIsAcBtypeFullLosts_Type()
)
ibmappnIsAcBtypeFullLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeFullLosts.setStatus("mandatory")


class _IbmappnIsAcBtypeErrorWraps_Type(Integer32):
    """Custom type ibmappnIsAcBtypeErrorWraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeErrorWraps_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeErrorWraps_Object = MibTableColumn
ibmappnIsAcBtypeErrorWraps = _IbmappnIsAcBtypeErrorWraps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 15),
    _IbmappnIsAcBtypeErrorWraps_Type()
)
ibmappnIsAcBtypeErrorWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeErrorWraps.setStatus("mandatory")


class _IbmappnIsAcBtypeErrorLosts_Type(Integer32):
    """Custom type ibmappnIsAcBtypeErrorLosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeErrorLosts_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeErrorLosts_Object = MibTableColumn
ibmappnIsAcBtypeErrorLosts = _IbmappnIsAcBtypeErrorLosts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 16),
    _IbmappnIsAcBtypeErrorLosts_Type()
)
ibmappnIsAcBtypeErrorLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeErrorLosts.setStatus("mandatory")


class _IbmappnIsAcBtypeCheckPts_Type(Integer32):
    """Custom type ibmappnIsAcBtypeCheckPts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeCheckPts_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeCheckPts_Object = MibTableColumn
ibmappnIsAcBtypeCheckPts = _IbmappnIsAcBtypeCheckPts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 17),
    _IbmappnIsAcBtypeCheckPts_Type()
)
ibmappnIsAcBtypeCheckPts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeCheckPts.setStatus("mandatory")


class _IbmappnIsAcBtypePurges_Type(Integer32):
    """Custom type ibmappnIsAcBtypePurges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypePurges_Type.__name__ = "Integer32"
_IbmappnIsAcBtypePurges_Object = MibTableColumn
ibmappnIsAcBtypePurges = _IbmappnIsAcBtypePurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 18),
    _IbmappnIsAcBtypePurges_Type()
)
ibmappnIsAcBtypePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypePurges.setStatus("mandatory")


class _IbmappnIsAcBtypeDeletes_Type(Integer32):
    """Custom type ibmappnIsAcBtypeDeletes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeDeletes_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeDeletes_Object = MibTableColumn
ibmappnIsAcBtypeDeletes = _IbmappnIsAcBtypeDeletes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 19),
    _IbmappnIsAcBtypeDeletes_Type()
)
ibmappnIsAcBtypeDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeDeletes.setStatus("mandatory")


class _IbmappnIsAcBtypeResets_Type(Integer32):
    """Custom type ibmappnIsAcBtypeResets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBtypeResets_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeResets_Object = MibTableColumn
ibmappnIsAcBtypeResets = _IbmappnIsAcBtypeResets_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 20),
    _IbmappnIsAcBtypeResets_Type()
)
ibmappnIsAcBtypeResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeResets.setStatus("mandatory")


class _IbmappnIsAcBtypeClearStats_Type(Integer32):
    """Custom type ibmappnIsAcBtypeClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("yes", 2))
    )


_IbmappnIsAcBtypeClearStats_Type.__name__ = "Integer32"
_IbmappnIsAcBtypeClearStats_Object = MibTableColumn
ibmappnIsAcBtypeClearStats = _IbmappnIsAcBtypeClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 2, 1, 21),
    _IbmappnIsAcBtypeClearStats_Type()
)
ibmappnIsAcBtypeClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBtypeClearStats.setStatus("mandatory")
_IbmappnIsAcBufTable_Object = MibTable
ibmappnIsAcBufTable = _IbmappnIsAcBufTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ibmappnIsAcBufTable.setStatus("mandatory")
_IbmappnIsAcBufEntry_Object = MibTableRow
ibmappnIsAcBufEntry = _IbmappnIsAcBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1)
)
ibmappnIsAcBufEntry.setIndexNames(
    (0, "IBMACCOUNTING-MIB", "ibmappnIsAcBufMedia"),
    (0, "IBMACCOUNTING-MIB", "ibmappnIsAcBufNumber"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcBufEntry.setStatus("mandatory")


class _IbmappnIsAcBufMedia_Type(Integer32):
    """Custom type ibmappnIsAcBufMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dasd", 2),
          ("memory", 1))
    )


_IbmappnIsAcBufMedia_Type.__name__ = "Integer32"
_IbmappnIsAcBufMedia_Object = MibTableColumn
ibmappnIsAcBufMedia = _IbmappnIsAcBufMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 1),
    _IbmappnIsAcBufMedia_Type()
)
ibmappnIsAcBufMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufMedia.setStatus("mandatory")


class _IbmappnIsAcBufNumber_Type(Integer32):
    """Custom type ibmappnIsAcBufNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBufNumber_Type.__name__ = "Integer32"
_IbmappnIsAcBufNumber_Object = MibTableColumn
ibmappnIsAcBufNumber = _IbmappnIsAcBufNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 2),
    _IbmappnIsAcBufNumber_Type()
)
ibmappnIsAcBufNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufNumber.setStatus("mandatory")


class _IbmappnIsAcBufState_Type(Integer32):
    """Custom type ibmappnIsAcBufState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("complete", 1),
          ("purge", 3))
    )


_IbmappnIsAcBufState_Type.__name__ = "Integer32"
_IbmappnIsAcBufState_Object = MibTableColumn
ibmappnIsAcBufState = _IbmappnIsAcBufState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 3),
    _IbmappnIsAcBufState_Type()
)
ibmappnIsAcBufState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBufState.setStatus("mandatory")


class _IbmappnIsAcBufRecFormat_Type(Integer32):
    """Custom type ibmappnIsAcBufRecFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_IbmappnIsAcBufRecFormat_Type.__name__ = "Integer32"
_IbmappnIsAcBufRecFormat_Object = MibTableColumn
ibmappnIsAcBufRecFormat = _IbmappnIsAcBufRecFormat_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 4),
    _IbmappnIsAcBufRecFormat_Type()
)
ibmappnIsAcBufRecFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufRecFormat.setStatus("mandatory")


class _IbmappnIsAcBufMaxRecords_Type(Integer32):
    """Custom type ibmappnIsAcBufMaxRecords based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBufMaxRecords_Type.__name__ = "Integer32"
_IbmappnIsAcBufMaxRecords_Object = MibTableColumn
ibmappnIsAcBufMaxRecords = _IbmappnIsAcBufMaxRecords_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 5),
    _IbmappnIsAcBufMaxRecords_Type()
)
ibmappnIsAcBufMaxRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufMaxRecords.setStatus("mandatory")


class _IbmappnIsAcBufOldestIndex_Type(Integer32):
    """Custom type ibmappnIsAcBufOldestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBufOldestIndex_Type.__name__ = "Integer32"
_IbmappnIsAcBufOldestIndex_Object = MibTableColumn
ibmappnIsAcBufOldestIndex = _IbmappnIsAcBufOldestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 6),
    _IbmappnIsAcBufOldestIndex_Type()
)
ibmappnIsAcBufOldestIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcBufOldestIndex.setStatus("mandatory")


class _IbmappnIsAcBufNewestIndex_Type(Integer32):
    """Custom type ibmappnIsAcBufNewestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcBufNewestIndex_Type.__name__ = "Integer32"
_IbmappnIsAcBufNewestIndex_Object = MibTableColumn
ibmappnIsAcBufNewestIndex = _IbmappnIsAcBufNewestIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 7),
    _IbmappnIsAcBufNewestIndex_Type()
)
ibmappnIsAcBufNewestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufNewestIndex.setStatus("mandatory")


class _IbmappnIsAcBufName_Type(DisplayString):
    """Custom type ibmappnIsAcBufName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_IbmappnIsAcBufName_Type.__name__ = "DisplayString"
_IbmappnIsAcBufName_Object = MibTableColumn
ibmappnIsAcBufName = _IbmappnIsAcBufName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 3, 1, 8),
    _IbmappnIsAcBufName_Type()
)
ibmappnIsAcBufName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcBufName.setStatus("mandatory")
_IbmappnIsAcTimeTable_Object = MibTable
ibmappnIsAcTimeTable = _IbmappnIsAcTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ibmappnIsAcTimeTable.setStatus("mandatory")
_IbmappnIsAcTimeEntry_Object = MibTableRow
ibmappnIsAcTimeEntry = _IbmappnIsAcTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1)
)
ibmappnIsAcTimeEntry.setIndexNames(
    (0, "IBMACCOUNTING-MIB", "ibmappnIsAcTimeIndex"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcTimeEntry.setStatus("mandatory")


class _IbmappnIsAcTimeIndex_Type(Integer32):
    """Custom type ibmappnIsAcTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcTimeIndex_Type.__name__ = "Integer32"
_IbmappnIsAcTimeIndex_Object = MibTableColumn
ibmappnIsAcTimeIndex = _IbmappnIsAcTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 1),
    _IbmappnIsAcTimeIndex_Type()
)
ibmappnIsAcTimeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeIndex.setStatus("mandatory")


class _IbmappnIsAcTimeEntryType_Type(Integer32):
    """Custom type ibmappnIsAcTimeEntryType based on Integer32"""
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
        *(("createdMedia", 3),
          ("endCollection", 2),
          ("managerSetTime", 6),
          ("recordFormatChanged", 7),
          ("startCollection", 1),
          ("timeChange", 5),
          ("timeReference", 8),
          ("wrappedMedia", 4))
    )


_IbmappnIsAcTimeEntryType_Type.__name__ = "Integer32"
_IbmappnIsAcTimeEntryType_Object = MibTableColumn
ibmappnIsAcTimeEntryType = _IbmappnIsAcTimeEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 2),
    _IbmappnIsAcTimeEntryType_Type()
)
ibmappnIsAcTimeEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeEntryType.setStatus("mandatory")


class _IbmappnIsAcTimeForMedia_Type(Integer32):
    """Custom type ibmappnIsAcTimeForMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("allMedias", 99),
          ("dasdMedia", 2),
          ("memoryMedia", 1))
    )


_IbmappnIsAcTimeForMedia_Type.__name__ = "Integer32"
_IbmappnIsAcTimeForMedia_Object = MibTableColumn
ibmappnIsAcTimeForMedia = _IbmappnIsAcTimeForMedia_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 3),
    _IbmappnIsAcTimeForMedia_Type()
)
ibmappnIsAcTimeForMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeForMedia.setStatus("mandatory")
_IbmappnIsAcTimeRecTime_Type = TimeTicks
_IbmappnIsAcTimeRecTime_Object = MibTableColumn
ibmappnIsAcTimeRecTime = _IbmappnIsAcTimeRecTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 4),
    _IbmappnIsAcTimeRecTime_Type()
)
ibmappnIsAcTimeRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeRecTime.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcSecs_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcTimeAgtUtcSecs_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcSecs_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcSecs = _IbmappnIsAcTimeAgtUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 5),
    _IbmappnIsAcTimeAgtUtcSecs_Type()
)
ibmappnIsAcTimeAgtUtcSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcSecs.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcMins_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcTimeAgtUtcMins_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcMins_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMins = _IbmappnIsAcTimeAgtUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 6),
    _IbmappnIsAcTimeAgtUtcMins_Type()
)
ibmappnIsAcTimeAgtUtcMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMins.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcHours_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_IbmappnIsAcTimeAgtUtcHours_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcHours_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcHours = _IbmappnIsAcTimeAgtUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 7),
    _IbmappnIsAcTimeAgtUtcHours_Type()
)
ibmappnIsAcTimeAgtUtcHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcHours.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcMdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcMdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IbmappnIsAcTimeAgtUtcMdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcMdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMdays = _IbmappnIsAcTimeAgtUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 8),
    _IbmappnIsAcTimeAgtUtcMdays_Type()
)
ibmappnIsAcTimeAgtUtcMdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMdays.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcTimeAgtUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcMonths_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcMonths = _IbmappnIsAcTimeAgtUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 9),
    _IbmappnIsAcTimeAgtUtcMonths_Type()
)
ibmappnIsAcTimeAgtUtcMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcMonths.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcYears_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcYears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IbmappnIsAcTimeAgtUtcYears_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcYears_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcYears = _IbmappnIsAcTimeAgtUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 10),
    _IbmappnIsAcTimeAgtUtcYears_Type()
)
ibmappnIsAcTimeAgtUtcYears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcYears.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcWdays based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcTimeAgtUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcWdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcWdays = _IbmappnIsAcTimeAgtUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 11),
    _IbmappnIsAcTimeAgtUtcWdays_Type()
)
ibmappnIsAcTimeAgtUtcWdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcWdays.setStatus("mandatory")


class _IbmappnIsAcTimeAgtUtcYdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeAgtUtcYdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_IbmappnIsAcTimeAgtUtcYdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeAgtUtcYdays_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcYdays = _IbmappnIsAcTimeAgtUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 12),
    _IbmappnIsAcTimeAgtUtcYdays_Type()
)
ibmappnIsAcTimeAgtUtcYdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcYdays.setStatus("mandatory")
_IbmappnIsAcTimeAgtUtcIsdst_Type = Integer32
_IbmappnIsAcTimeAgtUtcIsdst_Object = MibTableColumn
ibmappnIsAcTimeAgtUtcIsdst = _IbmappnIsAcTimeAgtUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 13),
    _IbmappnIsAcTimeAgtUtcIsdst_Type()
)
ibmappnIsAcTimeAgtUtcIsdst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcTimeAgtName_Type(DisplayString):
    """Custom type ibmappnIsAcTimeAgtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcTimeAgtName_Type.__name__ = "DisplayString"
_IbmappnIsAcTimeAgtName_Object = MibTableColumn
ibmappnIsAcTimeAgtName = _IbmappnIsAcTimeAgtName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 14),
    _IbmappnIsAcTimeAgtName_Type()
)
ibmappnIsAcTimeAgtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeAgtName.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcSecs_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcTimeMgrUtcSecs_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcSecs_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcSecs = _IbmappnIsAcTimeMgrUtcSecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 15),
    _IbmappnIsAcTimeMgrUtcSecs_Type()
)
ibmappnIsAcTimeMgrUtcSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcSecs.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcMins_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_IbmappnIsAcTimeMgrUtcMins_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcMins_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMins = _IbmappnIsAcTimeMgrUtcMins_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 16),
    _IbmappnIsAcTimeMgrUtcMins_Type()
)
ibmappnIsAcTimeMgrUtcMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMins.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcHours_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_IbmappnIsAcTimeMgrUtcHours_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcHours_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcHours = _IbmappnIsAcTimeMgrUtcHours_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 17),
    _IbmappnIsAcTimeMgrUtcHours_Type()
)
ibmappnIsAcTimeMgrUtcHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcHours.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcMdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcMdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnIsAcTimeMgrUtcMdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcMdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMdays = _IbmappnIsAcTimeMgrUtcMdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 18),
    _IbmappnIsAcTimeMgrUtcMdays_Type()
)
ibmappnIsAcTimeMgrUtcMdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMdays.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcMonths_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcMonths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )


_IbmappnIsAcTimeMgrUtcMonths_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcMonths_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcMonths = _IbmappnIsAcTimeMgrUtcMonths_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 19),
    _IbmappnIsAcTimeMgrUtcMonths_Type()
)
ibmappnIsAcTimeMgrUtcMonths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcMonths.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcYears_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcYears based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_IbmappnIsAcTimeMgrUtcYears_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcYears_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcYears = _IbmappnIsAcTimeMgrUtcYears_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 20),
    _IbmappnIsAcTimeMgrUtcYears_Type()
)
ibmappnIsAcTimeMgrUtcYears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcYears.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcWdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcWdays based on Integer32"""
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
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )


_IbmappnIsAcTimeMgrUtcWdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcWdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcWdays = _IbmappnIsAcTimeMgrUtcWdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 21),
    _IbmappnIsAcTimeMgrUtcWdays_Type()
)
ibmappnIsAcTimeMgrUtcWdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcWdays.setStatus("mandatory")


class _IbmappnIsAcTimeMgrUtcYdays_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrUtcYdays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_IbmappnIsAcTimeMgrUtcYdays_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrUtcYdays_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcYdays = _IbmappnIsAcTimeMgrUtcYdays_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 22),
    _IbmappnIsAcTimeMgrUtcYdays_Type()
)
ibmappnIsAcTimeMgrUtcYdays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcYdays.setStatus("mandatory")
_IbmappnIsAcTimeMgrUtcIsdst_Type = Integer32
_IbmappnIsAcTimeMgrUtcIsdst_Object = MibTableColumn
ibmappnIsAcTimeMgrUtcIsdst = _IbmappnIsAcTimeMgrUtcIsdst_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 23),
    _IbmappnIsAcTimeMgrUtcIsdst_Type()
)
ibmappnIsAcTimeMgrUtcIsdst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrUtcIsdst.setStatus("mandatory")


class _IbmappnIsAcTimeMgrName_Type(DisplayString):
    """Custom type ibmappnIsAcTimeMgrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_IbmappnIsAcTimeMgrName_Type.__name__ = "DisplayString"
_IbmappnIsAcTimeMgrName_Object = MibTableColumn
ibmappnIsAcTimeMgrName = _IbmappnIsAcTimeMgrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 24),
    _IbmappnIsAcTimeMgrName_Type()
)
ibmappnIsAcTimeMgrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrName.setStatus("mandatory")


class _IbmappnIsAcTimeMgrTimeValid_Type(Integer32):
    """Custom type ibmappnIsAcTimeMgrTimeValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notvalid", 1),
          ("valid", 2))
    )


_IbmappnIsAcTimeMgrTimeValid_Type.__name__ = "Integer32"
_IbmappnIsAcTimeMgrTimeValid_Object = MibTableColumn
ibmappnIsAcTimeMgrTimeValid = _IbmappnIsAcTimeMgrTimeValid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 4, 1, 25),
    _IbmappnIsAcTimeMgrTimeValid_Type()
)
ibmappnIsAcTimeMgrTimeValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnIsAcTimeMgrTimeValid.setStatus("mandatory")
_IbmappnIsAcDataTable_Object = MibTable
ibmappnIsAcDataTable = _IbmappnIsAcDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5)
)
if mibBuilder.loadTexts:
    ibmappnIsAcDataTable.setStatus("mandatory")
_IbmappnIsAcDataEntry_Object = MibTableRow
ibmappnIsAcDataEntry = _IbmappnIsAcDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1)
)
ibmappnIsAcDataEntry.setIndexNames(
    (0, "IBMACCOUNTING-MIB", "ibmappnIsAcIndex"),
)
if mibBuilder.loadTexts:
    ibmappnIsAcDataEntry.setStatus("mandatory")


class _IbmappnIsAcIndex_Type(Integer32):
    """Custom type ibmappnIsAcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IbmappnIsAcIndex_Type.__name__ = "Integer32"
_IbmappnIsAcIndex_Object = MibTableColumn
ibmappnIsAcIndex = _IbmappnIsAcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 1),
    _IbmappnIsAcIndex_Type()
)
ibmappnIsAcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcIndex.setStatus("mandatory")


class _IbmappnIsAcEntryType_Type(Integer32):
    """Custom type ibmappnIsAcEntryType based on Integer32"""
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
        *(("checkpointEntry", 4),
          ("endEntry", 2),
          ("startEntry", 1),
          ("thresholdEntry", 3))
    )


_IbmappnIsAcEntryType_Type.__name__ = "Integer32"
_IbmappnIsAcEntryType_Object = MibTableColumn
ibmappnIsAcEntryType = _IbmappnIsAcEntryType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 2),
    _IbmappnIsAcEntryType_Type()
)
ibmappnIsAcEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcEntryType.setStatus("mandatory")
_IbmappnIsAcRecTime_Type = TimeTicks
_IbmappnIsAcRecTime_Object = MibTableColumn
ibmappnIsAcRecTime = _IbmappnIsAcRecTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 3),
    _IbmappnIsAcRecTime_Type()
)
ibmappnIsAcRecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcRecTime.setStatus("mandatory")


class _IbmappnIsAcFqLuName_Type(DisplayString):
    """Custom type ibmappnIsAcFqLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcFqLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcFqLuName_Object = MibTableColumn
ibmappnIsAcFqLuName = _IbmappnIsAcFqLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 4),
    _IbmappnIsAcFqLuName_Type()
)
ibmappnIsAcFqLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcFqLuName.setStatus("mandatory")


class _IbmappnIsAcPcid_Type(OctetString):
    """Custom type ibmappnIsAcPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_IbmappnIsAcPcid_Type.__name__ = "OctetString"
_IbmappnIsAcPcid_Object = MibTableColumn
ibmappnIsAcPcid = _IbmappnIsAcPcid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 5),
    _IbmappnIsAcPcid_Type()
)
ibmappnIsAcPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcPcid.setStatus("mandatory")


class _IbmappnIsAcPriLuName_Type(DisplayString):
    """Custom type ibmappnIsAcPriLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcPriLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcPriLuName_Object = MibTableColumn
ibmappnIsAcPriLuName = _IbmappnIsAcPriLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 6),
    _IbmappnIsAcPriLuName_Type()
)
ibmappnIsAcPriLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcPriLuName.setStatus("mandatory")


class _IbmappnIsAcSecLuName_Type(DisplayString):
    """Custom type ibmappnIsAcSecLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnIsAcSecLuName_Type.__name__ = "DisplayString"
_IbmappnIsAcSecLuName_Object = MibTableColumn
ibmappnIsAcSecLuName = _IbmappnIsAcSecLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 7),
    _IbmappnIsAcSecLuName_Type()
)
ibmappnIsAcSecLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSecLuName.setStatus("mandatory")


class _IbmappnIsAcModeName_Type(DisplayString):
    """Custom type ibmappnIsAcModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsAcModeName_Type.__name__ = "DisplayString"
_IbmappnIsAcModeName_Object = MibTableColumn
ibmappnIsAcModeName = _IbmappnIsAcModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 8),
    _IbmappnIsAcModeName_Type()
)
ibmappnIsAcModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcModeName.setStatus("mandatory")


class _IbmappnIsAcCosName_Type(DisplayString):
    """Custom type ibmappnIsAcCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnIsAcCosName_Type.__name__ = "DisplayString"
_IbmappnIsAcCosName_Object = MibTableColumn
ibmappnIsAcCosName = _IbmappnIsAcCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 9),
    _IbmappnIsAcCosName_Type()
)
ibmappnIsAcCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcCosName.setStatus("mandatory")


class _IbmappnIsAcTransPriority_Type(Integer32):
    """Custom type ibmappnIsAcTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_IbmappnIsAcTransPriority_Type.__name__ = "Integer32"
_IbmappnIsAcTransPriority_Object = MibTableColumn
ibmappnIsAcTransPriority = _IbmappnIsAcTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 10),
    _IbmappnIsAcTransPriority_Type()
)
ibmappnIsAcTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcTransPriority.setStatus("mandatory")


class _IbmappnIsAcSessType_Type(Integer32):
    """Custom type ibmappnIsAcSessType based on Integer32"""
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
        *(("lu0thru3", 2),
          ("lu0thru3dlur", 4),
          ("lu62", 1),
          ("lu62dlur", 3))
    )


_IbmappnIsAcSessType_Type.__name__ = "Integer32"
_IbmappnIsAcSessType_Object = MibTableColumn
ibmappnIsAcSessType = _IbmappnIsAcSessType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 11),
    _IbmappnIsAcSessType_Type()
)
ibmappnIsAcSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessType.setStatus("mandatory")


class _IbmappnIsAcSessState_Type(Integer32):
    """Custom type ibmappnIsAcSessState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnIsAcSessState_Type.__name__ = "Integer32"
_IbmappnIsAcSessState_Object = MibTableColumn
ibmappnIsAcSessState = _IbmappnIsAcSessState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 12),
    _IbmappnIsAcSessState_Type()
)
ibmappnIsAcSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessState.setStatus("mandatory")
_IbmappnIsAcSessStartTime_Type = TimeTicks
_IbmappnIsAcSessStartTime_Object = MibTableColumn
ibmappnIsAcSessStartTime = _IbmappnIsAcSessStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 13),
    _IbmappnIsAcSessStartTime_Type()
)
ibmappnIsAcSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessStartTime.setStatus("mandatory")
_IbmappnIsAcSessUpTime_Type = TimeTicks
_IbmappnIsAcSessUpTime_Object = MibTableColumn
ibmappnIsAcSessUpTime = _IbmappnIsAcSessUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 14),
    _IbmappnIsAcSessUpTime_Type()
)
ibmappnIsAcSessUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcSessUpTime.setStatus("mandatory")
_IbmappnIsAcCtrUpTime_Type = TimeTicks
_IbmappnIsAcCtrUpTime_Object = MibTableColumn
ibmappnIsAcCtrUpTime = _IbmappnIsAcCtrUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 15),
    _IbmappnIsAcCtrUpTime_Type()
)
ibmappnIsAcCtrUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcCtrUpTime.setStatus("mandatory")


class _IbmappnIsAcEndReason_Type(OctetString):
    """Custom type ibmappnIsAcEndReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmappnIsAcEndReason_Type.__name__ = "OctetString"
_IbmappnIsAcEndReason_Object = MibTableColumn
ibmappnIsAcEndReason = _IbmappnIsAcEndReason_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 16),
    _IbmappnIsAcEndReason_Type()
)
ibmappnIsAcEndReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcEndReason.setStatus("mandatory")
_IbmappnIsAcP2SFmdPius_Type = Counter32
_IbmappnIsAcP2SFmdPius_Object = MibTableColumn
ibmappnIsAcP2SFmdPius = _IbmappnIsAcP2SFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 17),
    _IbmappnIsAcP2SFmdPius_Type()
)
ibmappnIsAcP2SFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SFmdPius.setStatus("mandatory")
_IbmappnIsAcS2PFmdPius_Type = Counter32
_IbmappnIsAcS2PFmdPius_Object = MibTableColumn
ibmappnIsAcS2PFmdPius = _IbmappnIsAcS2PFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 18),
    _IbmappnIsAcS2PFmdPius_Type()
)
ibmappnIsAcS2PFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PFmdPius.setStatus("mandatory")
_IbmappnIsAcP2SNonFmdPius_Type = Counter32
_IbmappnIsAcP2SNonFmdPius_Object = MibTableColumn
ibmappnIsAcP2SNonFmdPius = _IbmappnIsAcP2SNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 19),
    _IbmappnIsAcP2SNonFmdPius_Type()
)
ibmappnIsAcP2SNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SNonFmdPius.setStatus("mandatory")
_IbmappnIsAcS2PNonFmdPius_Type = Counter32
_IbmappnIsAcS2PNonFmdPius_Object = MibTableColumn
ibmappnIsAcS2PNonFmdPius = _IbmappnIsAcS2PNonFmdPius_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 20),
    _IbmappnIsAcS2PNonFmdPius_Type()
)
ibmappnIsAcS2PNonFmdPius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PNonFmdPius.setStatus("mandatory")
_IbmappnIsAcP2SFmdBytes_Type = Counter32
_IbmappnIsAcP2SFmdBytes_Object = MibTableColumn
ibmappnIsAcP2SFmdBytes = _IbmappnIsAcP2SFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 21),
    _IbmappnIsAcP2SFmdBytes_Type()
)
ibmappnIsAcP2SFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SFmdBytes.setStatus("mandatory")
_IbmappnIsAcS2PFmdBytes_Type = Counter32
_IbmappnIsAcS2PFmdBytes_Object = MibTableColumn
ibmappnIsAcS2PFmdBytes = _IbmappnIsAcS2PFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 22),
    _IbmappnIsAcS2PFmdBytes_Type()
)
ibmappnIsAcS2PFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PFmdBytes.setStatus("mandatory")
_IbmappnIsAcP2SNonFmdBytes_Type = Counter32
_IbmappnIsAcP2SNonFmdBytes_Object = MibTableColumn
ibmappnIsAcP2SNonFmdBytes = _IbmappnIsAcP2SNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 23),
    _IbmappnIsAcP2SNonFmdBytes_Type()
)
ibmappnIsAcP2SNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcP2SNonFmdBytes.setStatus("mandatory")
_IbmappnIsAcS2PNonFmdBytes_Type = Counter32
_IbmappnIsAcS2PNonFmdBytes_Object = MibTableColumn
ibmappnIsAcS2PNonFmdBytes = _IbmappnIsAcS2PNonFmdBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 24),
    _IbmappnIsAcS2PNonFmdBytes_Type()
)
ibmappnIsAcS2PNonFmdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcS2PNonFmdBytes.setStatus("mandatory")


class _IbmappnIsAcRouteInfo_Type(OctetString):
    """Custom type ibmappnIsAcRouteInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IbmappnIsAcRouteInfo_Type.__name__ = "OctetString"
_IbmappnIsAcRouteInfo_Object = MibTableColumn
ibmappnIsAcRouteInfo = _IbmappnIsAcRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 7, 3, 2, 5, 1, 25),
    _IbmappnIsAcRouteInfo_Type()
)
ibmappnIsAcRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnIsAcRouteInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMACCOUNTING-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmappn": ibmappn,
       "ibmappnSession": ibmappnSession,
       "ibmappnSessIntermediate": ibmappnSessIntermediate,
       "ibmappnIsAccounting": ibmappnIsAccounting,
       "ibmappnIsAcGlobal": ibmappnIsAcGlobal,
       "ibmappnIsAcGlobeStatus": ibmappnIsAcGlobeStatus,
       "ibmappnIsAcGlobeByteThresh": ibmappnIsAcGlobeByteThresh,
       "ibmappnIsAcGlobeCheckPt": ibmappnIsAcGlobeCheckPt,
       "ibmappnIsAcGlobeMgrUtcSecs": ibmappnIsAcGlobeMgrUtcSecs,
       "ibmappnIsAcGlobeMgrUtcMins": ibmappnIsAcGlobeMgrUtcMins,
       "ibmappnIsAcGlobeMgrUtcHours": ibmappnIsAcGlobeMgrUtcHours,
       "ibmappnIsAcGlobeMgrUtcMdays": ibmappnIsAcGlobeMgrUtcMdays,
       "ibmappnIsAcGlobeMgrUtcMonths": ibmappnIsAcGlobeMgrUtcMonths,
       "ibmappnIsAcGlobeMgrUtcYears": ibmappnIsAcGlobeMgrUtcYears,
       "ibmappnIsAcGlobeMgrUtcWdays": ibmappnIsAcGlobeMgrUtcWdays,
       "ibmappnIsAcGlobeMgrUtcYdays": ibmappnIsAcGlobeMgrUtcYdays,
       "ibmappnIsAcGlobeMgrUtcIsdst": ibmappnIsAcGlobeMgrUtcIsdst,
       "ibmappnIsAcGlobeMgrName": ibmappnIsAcGlobeMgrName,
       "ibmappnIsAcBtypeTable": ibmappnIsAcBtypeTable,
       "ibmappnIsAcBtypeEntry": ibmappnIsAcBtypeEntry,
       "ibmappnIsAcBtypeMedia": ibmappnIsAcBtypeMedia,
       "ibmappnIsAcBtypeActive": ibmappnIsAcBtypeActive,
       "ibmappnIsAcBtypeDirName": ibmappnIsAcBtypeDirName,
       "ibmappnIsAcBtypePrdMaxBufs": ibmappnIsAcBtypePrdMaxBufs,
       "ibmappnIsAcBtypeMaxBufs": ibmappnIsAcBtypeMaxBufs,
       "ibmappnIsAcBtypeCurBufs": ibmappnIsAcBtypeCurBufs,
       "ibmappnIsAcBtypePrdRecPerBuf": ibmappnIsAcBtypePrdRecPerBuf,
       "ibmappnIsAcBtypeRecPerBuf": ibmappnIsAcBtypeRecPerBuf,
       "ibmappnIsAcBtypeRecFormat": ibmappnIsAcBtypeRecFormat,
       "ibmappnIsAcBtypeFullAction": ibmappnIsAcBtypeFullAction,
       "ibmappnIsAcBtypeFullTime": ibmappnIsAcBtypeFullTime,
       "ibmappnIsAcBtypeFullReason": ibmappnIsAcBtypeFullReason,
       "ibmappnIsAcBtypeFullWraps": ibmappnIsAcBtypeFullWraps,
       "ibmappnIsAcBtypeFullLosts": ibmappnIsAcBtypeFullLosts,
       "ibmappnIsAcBtypeErrorWraps": ibmappnIsAcBtypeErrorWraps,
       "ibmappnIsAcBtypeErrorLosts": ibmappnIsAcBtypeErrorLosts,
       "ibmappnIsAcBtypeCheckPts": ibmappnIsAcBtypeCheckPts,
       "ibmappnIsAcBtypePurges": ibmappnIsAcBtypePurges,
       "ibmappnIsAcBtypeDeletes": ibmappnIsAcBtypeDeletes,
       "ibmappnIsAcBtypeResets": ibmappnIsAcBtypeResets,
       "ibmappnIsAcBtypeClearStats": ibmappnIsAcBtypeClearStats,
       "ibmappnIsAcBufTable": ibmappnIsAcBufTable,
       "ibmappnIsAcBufEntry": ibmappnIsAcBufEntry,
       "ibmappnIsAcBufMedia": ibmappnIsAcBufMedia,
       "ibmappnIsAcBufNumber": ibmappnIsAcBufNumber,
       "ibmappnIsAcBufState": ibmappnIsAcBufState,
       "ibmappnIsAcBufRecFormat": ibmappnIsAcBufRecFormat,
       "ibmappnIsAcBufMaxRecords": ibmappnIsAcBufMaxRecords,
       "ibmappnIsAcBufOldestIndex": ibmappnIsAcBufOldestIndex,
       "ibmappnIsAcBufNewestIndex": ibmappnIsAcBufNewestIndex,
       "ibmappnIsAcBufName": ibmappnIsAcBufName,
       "ibmappnIsAcTimeTable": ibmappnIsAcTimeTable,
       "ibmappnIsAcTimeEntry": ibmappnIsAcTimeEntry,
       "ibmappnIsAcTimeIndex": ibmappnIsAcTimeIndex,
       "ibmappnIsAcTimeEntryType": ibmappnIsAcTimeEntryType,
       "ibmappnIsAcTimeForMedia": ibmappnIsAcTimeForMedia,
       "ibmappnIsAcTimeRecTime": ibmappnIsAcTimeRecTime,
       "ibmappnIsAcTimeAgtUtcSecs": ibmappnIsAcTimeAgtUtcSecs,
       "ibmappnIsAcTimeAgtUtcMins": ibmappnIsAcTimeAgtUtcMins,
       "ibmappnIsAcTimeAgtUtcHours": ibmappnIsAcTimeAgtUtcHours,
       "ibmappnIsAcTimeAgtUtcMdays": ibmappnIsAcTimeAgtUtcMdays,
       "ibmappnIsAcTimeAgtUtcMonths": ibmappnIsAcTimeAgtUtcMonths,
       "ibmappnIsAcTimeAgtUtcYears": ibmappnIsAcTimeAgtUtcYears,
       "ibmappnIsAcTimeAgtUtcWdays": ibmappnIsAcTimeAgtUtcWdays,
       "ibmappnIsAcTimeAgtUtcYdays": ibmappnIsAcTimeAgtUtcYdays,
       "ibmappnIsAcTimeAgtUtcIsdst": ibmappnIsAcTimeAgtUtcIsdst,
       "ibmappnIsAcTimeAgtName": ibmappnIsAcTimeAgtName,
       "ibmappnIsAcTimeMgrUtcSecs": ibmappnIsAcTimeMgrUtcSecs,
       "ibmappnIsAcTimeMgrUtcMins": ibmappnIsAcTimeMgrUtcMins,
       "ibmappnIsAcTimeMgrUtcHours": ibmappnIsAcTimeMgrUtcHours,
       "ibmappnIsAcTimeMgrUtcMdays": ibmappnIsAcTimeMgrUtcMdays,
       "ibmappnIsAcTimeMgrUtcMonths": ibmappnIsAcTimeMgrUtcMonths,
       "ibmappnIsAcTimeMgrUtcYears": ibmappnIsAcTimeMgrUtcYears,
       "ibmappnIsAcTimeMgrUtcWdays": ibmappnIsAcTimeMgrUtcWdays,
       "ibmappnIsAcTimeMgrUtcYdays": ibmappnIsAcTimeMgrUtcYdays,
       "ibmappnIsAcTimeMgrUtcIsdst": ibmappnIsAcTimeMgrUtcIsdst,
       "ibmappnIsAcTimeMgrName": ibmappnIsAcTimeMgrName,
       "ibmappnIsAcTimeMgrTimeValid": ibmappnIsAcTimeMgrTimeValid,
       "ibmappnIsAcDataTable": ibmappnIsAcDataTable,
       "ibmappnIsAcDataEntry": ibmappnIsAcDataEntry,
       "ibmappnIsAcIndex": ibmappnIsAcIndex,
       "ibmappnIsAcEntryType": ibmappnIsAcEntryType,
       "ibmappnIsAcRecTime": ibmappnIsAcRecTime,
       "ibmappnIsAcFqLuName": ibmappnIsAcFqLuName,
       "ibmappnIsAcPcid": ibmappnIsAcPcid,
       "ibmappnIsAcPriLuName": ibmappnIsAcPriLuName,
       "ibmappnIsAcSecLuName": ibmappnIsAcSecLuName,
       "ibmappnIsAcModeName": ibmappnIsAcModeName,
       "ibmappnIsAcCosName": ibmappnIsAcCosName,
       "ibmappnIsAcTransPriority": ibmappnIsAcTransPriority,
       "ibmappnIsAcSessType": ibmappnIsAcSessType,
       "ibmappnIsAcSessState": ibmappnIsAcSessState,
       "ibmappnIsAcSessStartTime": ibmappnIsAcSessStartTime,
       "ibmappnIsAcSessUpTime": ibmappnIsAcSessUpTime,
       "ibmappnIsAcCtrUpTime": ibmappnIsAcCtrUpTime,
       "ibmappnIsAcEndReason": ibmappnIsAcEndReason,
       "ibmappnIsAcP2SFmdPius": ibmappnIsAcP2SFmdPius,
       "ibmappnIsAcS2PFmdPius": ibmappnIsAcS2PFmdPius,
       "ibmappnIsAcP2SNonFmdPius": ibmappnIsAcP2SNonFmdPius,
       "ibmappnIsAcS2PNonFmdPius": ibmappnIsAcS2PNonFmdPius,
       "ibmappnIsAcP2SFmdBytes": ibmappnIsAcP2SFmdBytes,
       "ibmappnIsAcS2PFmdBytes": ibmappnIsAcS2PFmdBytes,
       "ibmappnIsAcP2SNonFmdBytes": ibmappnIsAcP2SNonFmdBytes,
       "ibmappnIsAcS2PNonFmdBytes": ibmappnIsAcS2PNonFmdBytes,
       "ibmappnIsAcRouteInfo": ibmappnIsAcRouteInfo}
)
