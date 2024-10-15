# SNMP MIB module (JUNIPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:01 2024
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

(jnxChassisOKTraps,
 jnxChassisTraps,
 jnxMibs) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxChassisOKTraps",
    "jnxChassisTraps",
    "jnxMibs")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp")


# MODULE-IDENTITY

jnxBoxAnatomy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1)
)
jnxBoxAnatomy.setRevisions(
        ("2010-10-22 00:00",
         "2004-03-23 00:00",
         "2004-06-30 00:00",
         "2004-09-17 00:00",
         "2005-07-18 00:00",
         "2005-07-19 00:00",
         "2006-11-20 00:00",
         "2008-07-31 00:00",
         "2008-08-01 00:00",
         "2008-12-31 00:00",
         "2009-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxChassisId(Integer32, TextualConvention):
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("jcs1", 8),
          ("jcs2", 9),
          ("jcs3", 10),
          ("jcs4", 11),
          ("lcc0", 4),
          ("lcc1", 5),
          ("lcc10", 25),
          ("lcc11", 26),
          ("lcc12", 27),
          ("lcc13", 28),
          ("lcc14", 29),
          ("lcc15", 30),
          ("lcc2", 6),
          ("lcc3", 7),
          ("lcc4", 19),
          ("lcc5", 20),
          ("lcc6", 21),
          ("lcc7", 22),
          ("lcc8", 23),
          ("lcc9", 24),
          ("member0", 31),
          ("member1", 32),
          ("member2", 33),
          ("member3", 34),
          ("member4", 35),
          ("member5", 36),
          ("member6", 37),
          ("member7", 38),
          ("node0", 12),
          ("node1", 13),
          ("scc", 3),
          ("sfc0", 14),
          ("sfc1", 15),
          ("sfc2", 16),
          ("sfc3", 17),
          ("sfc4", 18),
          ("singleChassis", 2),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_JnxBoxClass_Type = ObjectIdentifier
_JnxBoxClass_Object = MibScalar
jnxBoxClass = _JnxBoxClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 1),
    _JnxBoxClass_Type()
)
jnxBoxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxClass.setStatus("current")


class _JnxBoxDescr_Type(DisplayString):
    """Custom type jnxBoxDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxBoxDescr_Type.__name__ = "DisplayString"
_JnxBoxDescr_Object = MibScalar
jnxBoxDescr = _JnxBoxDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 2),
    _JnxBoxDescr_Type()
)
jnxBoxDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxDescr.setStatus("current")


class _JnxBoxSerialNo_Type(DisplayString):
    """Custom type jnxBoxSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxBoxSerialNo_Type.__name__ = "DisplayString"
_JnxBoxSerialNo_Object = MibScalar
jnxBoxSerialNo = _JnxBoxSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 3),
    _JnxBoxSerialNo_Type()
)
jnxBoxSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxSerialNo.setStatus("current")


class _JnxBoxRevision_Type(DisplayString):
    """Custom type jnxBoxRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxBoxRevision_Type.__name__ = "DisplayString"
_JnxBoxRevision_Object = MibScalar
jnxBoxRevision = _JnxBoxRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 4),
    _JnxBoxRevision_Type()
)
jnxBoxRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxRevision.setStatus("current")
_JnxBoxInstalled_Type = TimeStamp
_JnxBoxInstalled_Object = MibScalar
jnxBoxInstalled = _JnxBoxInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 5),
    _JnxBoxInstalled_Type()
)
jnxBoxInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxInstalled.setStatus("current")
_JnxContainersTable_Object = MibTable
jnxContainersTable = _JnxContainersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6)
)
if mibBuilder.loadTexts:
    jnxContainersTable.setStatus("current")
_JnxContainersEntry_Object = MibTableRow
jnxContainersEntry = _JnxContainersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1)
)
jnxContainersEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContainersIndex"),
)
if mibBuilder.loadTexts:
    jnxContainersEntry.setStatus("current")


class _JnxContainersIndex_Type(Integer32):
    """Custom type jnxContainersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxContainersIndex_Type.__name__ = "Integer32"
_JnxContainersIndex_Object = MibTableColumn
jnxContainersIndex = _JnxContainersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 1),
    _JnxContainersIndex_Type()
)
jnxContainersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersIndex.setStatus("current")


class _JnxContainersView_Type(Integer32):
    """Custom type jnxContainersView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_JnxContainersView_Type.__name__ = "Integer32"
_JnxContainersView_Object = MibTableColumn
jnxContainersView = _JnxContainersView_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 2),
    _JnxContainersView_Type()
)
jnxContainersView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersView.setStatus("current")
_JnxContainersLevel_Type = Integer32
_JnxContainersLevel_Object = MibTableColumn
jnxContainersLevel = _JnxContainersLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 3),
    _JnxContainersLevel_Type()
)
jnxContainersLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersLevel.setStatus("current")
_JnxContainersWithin_Type = Integer32
_JnxContainersWithin_Object = MibTableColumn
jnxContainersWithin = _JnxContainersWithin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 4),
    _JnxContainersWithin_Type()
)
jnxContainersWithin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersWithin.setStatus("current")
_JnxContainersType_Type = ObjectIdentifier
_JnxContainersType_Object = MibTableColumn
jnxContainersType = _JnxContainersType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 5),
    _JnxContainersType_Type()
)
jnxContainersType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersType.setStatus("current")


class _JnxContainersDescr_Type(DisplayString):
    """Custom type jnxContainersDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContainersDescr_Type.__name__ = "DisplayString"
_JnxContainersDescr_Object = MibTableColumn
jnxContainersDescr = _JnxContainersDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 6),
    _JnxContainersDescr_Type()
)
jnxContainersDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersDescr.setStatus("current")
_JnxContainersCount_Type = Integer32
_JnxContainersCount_Object = MibTableColumn
jnxContainersCount = _JnxContainersCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 6, 1, 7),
    _JnxContainersCount_Type()
)
jnxContainersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContainersCount.setStatus("current")
_JnxContentsLastChange_Type = TimeStamp
_JnxContentsLastChange_Object = MibScalar
jnxContentsLastChange = _JnxContentsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 7),
    _JnxContentsLastChange_Type()
)
jnxContentsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsLastChange.setStatus("current")
_JnxContentsTable_Object = MibTable
jnxContentsTable = _JnxContentsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8)
)
if mibBuilder.loadTexts:
    jnxContentsTable.setStatus("current")
_JnxContentsEntry_Object = MibTableRow
jnxContentsEntry = _JnxContentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1)
)
jnxContentsEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxContentsContainerIndex"),
    (0, "JUNIPER-MIB", "jnxContentsL1Index"),
    (0, "JUNIPER-MIB", "jnxContentsL2Index"),
    (0, "JUNIPER-MIB", "jnxContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxContentsEntry.setStatus("current")


class _JnxContentsContainerIndex_Type(Integer32):
    """Custom type jnxContentsContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxContentsContainerIndex_Type.__name__ = "Integer32"
_JnxContentsContainerIndex_Object = MibTableColumn
jnxContentsContainerIndex = _JnxContentsContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 1),
    _JnxContentsContainerIndex_Type()
)
jnxContentsContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsContainerIndex.setStatus("current")


class _JnxContentsL1Index_Type(Integer32):
    """Custom type jnxContentsL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxContentsL1Index_Type.__name__ = "Integer32"
_JnxContentsL1Index_Object = MibTableColumn
jnxContentsL1Index = _JnxContentsL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 2),
    _JnxContentsL1Index_Type()
)
jnxContentsL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsL1Index.setStatus("current")


class _JnxContentsL2Index_Type(Integer32):
    """Custom type jnxContentsL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxContentsL2Index_Type.__name__ = "Integer32"
_JnxContentsL2Index_Object = MibTableColumn
jnxContentsL2Index = _JnxContentsL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 3),
    _JnxContentsL2Index_Type()
)
jnxContentsL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsL2Index.setStatus("current")


class _JnxContentsL3Index_Type(Integer32):
    """Custom type jnxContentsL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxContentsL3Index_Type.__name__ = "Integer32"
_JnxContentsL3Index_Object = MibTableColumn
jnxContentsL3Index = _JnxContentsL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 4),
    _JnxContentsL3Index_Type()
)
jnxContentsL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsL3Index.setStatus("current")
_JnxContentsType_Type = ObjectIdentifier
_JnxContentsType_Object = MibTableColumn
jnxContentsType = _JnxContentsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 5),
    _JnxContentsType_Type()
)
jnxContentsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsType.setStatus("current")


class _JnxContentsDescr_Type(DisplayString):
    """Custom type jnxContentsDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsDescr_Type.__name__ = "DisplayString"
_JnxContentsDescr_Object = MibTableColumn
jnxContentsDescr = _JnxContentsDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 6),
    _JnxContentsDescr_Type()
)
jnxContentsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsDescr.setStatus("current")


class _JnxContentsSerialNo_Type(DisplayString):
    """Custom type jnxContentsSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsSerialNo_Type.__name__ = "DisplayString"
_JnxContentsSerialNo_Object = MibTableColumn
jnxContentsSerialNo = _JnxContentsSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 7),
    _JnxContentsSerialNo_Type()
)
jnxContentsSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsSerialNo.setStatus("current")


class _JnxContentsRevision_Type(DisplayString):
    """Custom type jnxContentsRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsRevision_Type.__name__ = "DisplayString"
_JnxContentsRevision_Object = MibTableColumn
jnxContentsRevision = _JnxContentsRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 8),
    _JnxContentsRevision_Type()
)
jnxContentsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsRevision.setStatus("current")
_JnxContentsInstalled_Type = TimeStamp
_JnxContentsInstalled_Object = MibTableColumn
jnxContentsInstalled = _JnxContentsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 9),
    _JnxContentsInstalled_Type()
)
jnxContentsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsInstalled.setStatus("current")


class _JnxContentsPartNo_Type(DisplayString):
    """Custom type jnxContentsPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsPartNo_Type.__name__ = "DisplayString"
_JnxContentsPartNo_Object = MibTableColumn
jnxContentsPartNo = _JnxContentsPartNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 10),
    _JnxContentsPartNo_Type()
)
jnxContentsPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsPartNo.setStatus("current")
_JnxContentsChassisId_Type = JnxChassisId
_JnxContentsChassisId_Object = MibTableColumn
jnxContentsChassisId = _JnxContentsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 11),
    _JnxContentsChassisId_Type()
)
jnxContentsChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsChassisId.setStatus("current")


class _JnxContentsChassisDescr_Type(DisplayString):
    """Custom type jnxContentsChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsChassisDescr_Type.__name__ = "DisplayString"
_JnxContentsChassisDescr_Object = MibTableColumn
jnxContentsChassisDescr = _JnxContentsChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 12),
    _JnxContentsChassisDescr_Type()
)
jnxContentsChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsChassisDescr.setStatus("current")


class _JnxContentsChassisCleiCode_Type(DisplayString):
    """Custom type jnxContentsChassisCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxContentsChassisCleiCode_Type.__name__ = "DisplayString"
_JnxContentsChassisCleiCode_Object = MibTableColumn
jnxContentsChassisCleiCode = _JnxContentsChassisCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 8, 1, 13),
    _JnxContentsChassisCleiCode_Type()
)
jnxContentsChassisCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxContentsChassisCleiCode.setStatus("current")
_JnxLEDLastChange_Type = TimeStamp
_JnxLEDLastChange_Object = MibScalar
jnxLEDLastChange = _JnxLEDLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 9),
    _JnxLEDLastChange_Type()
)
jnxLEDLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDLastChange.setStatus("deprecated")
_JnxLEDTable_Object = MibTable
jnxLEDTable = _JnxLEDTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10)
)
if mibBuilder.loadTexts:
    jnxLEDTable.setStatus("deprecated")
_JnxLEDEntry_Object = MibTableRow
jnxLEDEntry = _JnxLEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1)
)
jnxLEDEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxLEDAssociateTable"),
    (0, "JUNIPER-MIB", "jnxLEDAssociateIndex"),
    (0, "JUNIPER-MIB", "jnxLEDL1Index"),
    (0, "JUNIPER-MIB", "jnxLEDL2Index"),
    (0, "JUNIPER-MIB", "jnxLEDL3Index"),
)
if mibBuilder.loadTexts:
    jnxLEDEntry.setStatus("deprecated")


class _JnxLEDAssociateTable_Type(Integer32):
    """Custom type jnxLEDAssociateTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jnxContainersTable", 2),
          ("jnxContentsTable", 3),
          ("other", 1))
    )


_JnxLEDAssociateTable_Type.__name__ = "Integer32"
_JnxLEDAssociateTable_Object = MibTableColumn
jnxLEDAssociateTable = _JnxLEDAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 1),
    _JnxLEDAssociateTable_Type()
)
jnxLEDAssociateTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDAssociateTable.setStatus("deprecated")


class _JnxLEDAssociateIndex_Type(Integer32):
    """Custom type jnxLEDAssociateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxLEDAssociateIndex_Type.__name__ = "Integer32"
_JnxLEDAssociateIndex_Object = MibTableColumn
jnxLEDAssociateIndex = _JnxLEDAssociateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 2),
    _JnxLEDAssociateIndex_Type()
)
jnxLEDAssociateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDAssociateIndex.setStatus("deprecated")


class _JnxLEDL1Index_Type(Integer32):
    """Custom type jnxLEDL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxLEDL1Index_Type.__name__ = "Integer32"
_JnxLEDL1Index_Object = MibTableColumn
jnxLEDL1Index = _JnxLEDL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 3),
    _JnxLEDL1Index_Type()
)
jnxLEDL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDL1Index.setStatus("deprecated")


class _JnxLEDL2Index_Type(Integer32):
    """Custom type jnxLEDL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxLEDL2Index_Type.__name__ = "Integer32"
_JnxLEDL2Index_Object = MibTableColumn
jnxLEDL2Index = _JnxLEDL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 4),
    _JnxLEDL2Index_Type()
)
jnxLEDL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDL2Index.setStatus("deprecated")


class _JnxLEDL3Index_Type(Integer32):
    """Custom type jnxLEDL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxLEDL3Index_Type.__name__ = "Integer32"
_JnxLEDL3Index_Object = MibTableColumn
jnxLEDL3Index = _JnxLEDL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 5),
    _JnxLEDL3Index_Type()
)
jnxLEDL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDL3Index.setStatus("deprecated")
_JnxLEDOriginator_Type = ObjectIdentifier
_JnxLEDOriginator_Object = MibTableColumn
jnxLEDOriginator = _JnxLEDOriginator_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 6),
    _JnxLEDOriginator_Type()
)
jnxLEDOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDOriginator.setStatus("deprecated")


class _JnxLEDDescr_Type(DisplayString):
    """Custom type jnxLEDDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxLEDDescr_Type.__name__ = "DisplayString"
_JnxLEDDescr_Object = MibTableColumn
jnxLEDDescr = _JnxLEDDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 7),
    _JnxLEDDescr_Type()
)
jnxLEDDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDDescr.setStatus("deprecated")


class _JnxLEDState_Type(Integer32):
    """Custom type jnxLEDState based on Integer32"""
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
        *(("amber", 6),
          ("blue", 5),
          ("green", 2),
          ("other", 1),
          ("red", 4),
          ("yellow", 3))
    )


_JnxLEDState_Type.__name__ = "Integer32"
_JnxLEDState_Object = MibTableColumn
jnxLEDState = _JnxLEDState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 8),
    _JnxLEDState_Type()
)
jnxLEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDState.setStatus("deprecated")


class _JnxLEDStateOrdered_Type(Integer32):
    """Custom type jnxLEDStateOrdered based on Integer32"""
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
        *(("amber", 3),
          ("blue", 1),
          ("green", 2),
          ("other", 6),
          ("red", 5),
          ("yellow", 4))
    )


_JnxLEDStateOrdered_Type.__name__ = "Integer32"
_JnxLEDStateOrdered_Object = MibTableColumn
jnxLEDStateOrdered = _JnxLEDStateOrdered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 10, 1, 9),
    _JnxLEDStateOrdered_Type()
)
jnxLEDStateOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxLEDStateOrdered.setStatus("deprecated")
_JnxFilledLastChange_Type = TimeStamp
_JnxFilledLastChange_Object = MibScalar
jnxFilledLastChange = _JnxFilledLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 11),
    _JnxFilledLastChange_Type()
)
jnxFilledLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledLastChange.setStatus("current")
_JnxFilledTable_Object = MibTable
jnxFilledTable = _JnxFilledTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12)
)
if mibBuilder.loadTexts:
    jnxFilledTable.setStatus("current")
_JnxFilledEntry_Object = MibTableRow
jnxFilledEntry = _JnxFilledEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1)
)
jnxFilledEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxFilledContainerIndex"),
    (0, "JUNIPER-MIB", "jnxFilledL1Index"),
    (0, "JUNIPER-MIB", "jnxFilledL2Index"),
    (0, "JUNIPER-MIB", "jnxFilledL3Index"),
)
if mibBuilder.loadTexts:
    jnxFilledEntry.setStatus("current")


class _JnxFilledContainerIndex_Type(Integer32):
    """Custom type jnxFilledContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFilledContainerIndex_Type.__name__ = "Integer32"
_JnxFilledContainerIndex_Object = MibTableColumn
jnxFilledContainerIndex = _JnxFilledContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 1),
    _JnxFilledContainerIndex_Type()
)
jnxFilledContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledContainerIndex.setStatus("current")


class _JnxFilledL1Index_Type(Integer32):
    """Custom type jnxFilledL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFilledL1Index_Type.__name__ = "Integer32"
_JnxFilledL1Index_Object = MibTableColumn
jnxFilledL1Index = _JnxFilledL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 2),
    _JnxFilledL1Index_Type()
)
jnxFilledL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledL1Index.setStatus("current")


class _JnxFilledL2Index_Type(Integer32):
    """Custom type jnxFilledL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFilledL2Index_Type.__name__ = "Integer32"
_JnxFilledL2Index_Object = MibTableColumn
jnxFilledL2Index = _JnxFilledL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 3),
    _JnxFilledL2Index_Type()
)
jnxFilledL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledL2Index.setStatus("current")


class _JnxFilledL3Index_Type(Integer32):
    """Custom type jnxFilledL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFilledL3Index_Type.__name__ = "Integer32"
_JnxFilledL3Index_Object = MibTableColumn
jnxFilledL3Index = _JnxFilledL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 4),
    _JnxFilledL3Index_Type()
)
jnxFilledL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledL3Index.setStatus("current")


class _JnxFilledDescr_Type(DisplayString):
    """Custom type jnxFilledDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFilledDescr_Type.__name__ = "DisplayString"
_JnxFilledDescr_Object = MibTableColumn
jnxFilledDescr = _JnxFilledDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 5),
    _JnxFilledDescr_Type()
)
jnxFilledDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledDescr.setStatus("current")


class _JnxFilledState_Type(Integer32):
    """Custom type jnxFilledState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("filled", 3),
          ("unknown", 1))
    )


_JnxFilledState_Type.__name__ = "Integer32"
_JnxFilledState_Object = MibTableColumn
jnxFilledState = _JnxFilledState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 6),
    _JnxFilledState_Type()
)
jnxFilledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledState.setStatus("current")
_JnxFilledChassisId_Type = JnxChassisId
_JnxFilledChassisId_Object = MibTableColumn
jnxFilledChassisId = _JnxFilledChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 7),
    _JnxFilledChassisId_Type()
)
jnxFilledChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledChassisId.setStatus("current")


class _JnxFilledChassisDescr_Type(DisplayString):
    """Custom type jnxFilledChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFilledChassisDescr_Type.__name__ = "DisplayString"
_JnxFilledChassisDescr_Object = MibTableColumn
jnxFilledChassisDescr = _JnxFilledChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 12, 1, 8),
    _JnxFilledChassisDescr_Type()
)
jnxFilledChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFilledChassisDescr.setStatus("current")
_JnxOperatingTable_Object = MibTable
jnxOperatingTable = _JnxOperatingTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13)
)
if mibBuilder.loadTexts:
    jnxOperatingTable.setStatus("current")
_JnxOperatingEntry_Object = MibTableRow
jnxOperatingEntry = _JnxOperatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1)
)
jnxOperatingEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxOperatingContentsIndex"),
    (0, "JUNIPER-MIB", "jnxOperatingL1Index"),
    (0, "JUNIPER-MIB", "jnxOperatingL2Index"),
    (0, "JUNIPER-MIB", "jnxOperatingL3Index"),
)
if mibBuilder.loadTexts:
    jnxOperatingEntry.setStatus("current")


class _JnxOperatingContentsIndex_Type(Integer32):
    """Custom type jnxOperatingContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxOperatingContentsIndex_Type.__name__ = "Integer32"
_JnxOperatingContentsIndex_Object = MibTableColumn
jnxOperatingContentsIndex = _JnxOperatingContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 1),
    _JnxOperatingContentsIndex_Type()
)
jnxOperatingContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingContentsIndex.setStatus("current")


class _JnxOperatingL1Index_Type(Integer32):
    """Custom type jnxOperatingL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxOperatingL1Index_Type.__name__ = "Integer32"
_JnxOperatingL1Index_Object = MibTableColumn
jnxOperatingL1Index = _JnxOperatingL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 2),
    _JnxOperatingL1Index_Type()
)
jnxOperatingL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingL1Index.setStatus("current")


class _JnxOperatingL2Index_Type(Integer32):
    """Custom type jnxOperatingL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxOperatingL2Index_Type.__name__ = "Integer32"
_JnxOperatingL2Index_Object = MibTableColumn
jnxOperatingL2Index = _JnxOperatingL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 3),
    _JnxOperatingL2Index_Type()
)
jnxOperatingL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingL2Index.setStatus("current")


class _JnxOperatingL3Index_Type(Integer32):
    """Custom type jnxOperatingL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxOperatingL3Index_Type.__name__ = "Integer32"
_JnxOperatingL3Index_Object = MibTableColumn
jnxOperatingL3Index = _JnxOperatingL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 4),
    _JnxOperatingL3Index_Type()
)
jnxOperatingL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingL3Index.setStatus("current")


class _JnxOperatingDescr_Type(DisplayString):
    """Custom type jnxOperatingDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxOperatingDescr_Type.__name__ = "DisplayString"
_JnxOperatingDescr_Object = MibTableColumn
jnxOperatingDescr = _JnxOperatingDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 5),
    _JnxOperatingDescr_Type()
)
jnxOperatingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingDescr.setStatus("current")


class _JnxOperatingState_Type(Integer32):
    """Custom type jnxOperatingState based on Integer32"""
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
        *(("down", 6),
          ("ready", 3),
          ("reset", 4),
          ("running", 2),
          ("runningAtFullSpeed", 5),
          ("standby", 7),
          ("unknown", 1))
    )


_JnxOperatingState_Type.__name__ = "Integer32"
_JnxOperatingState_Object = MibTableColumn
jnxOperatingState = _JnxOperatingState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 6),
    _JnxOperatingState_Type()
)
jnxOperatingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingState.setStatus("current")
_JnxOperatingTemp_Type = Gauge32
_JnxOperatingTemp_Object = MibTableColumn
jnxOperatingTemp = _JnxOperatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 7),
    _JnxOperatingTemp_Type()
)
jnxOperatingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingTemp.setStatus("current")
_JnxOperatingCPU_Type = Gauge32
_JnxOperatingCPU_Object = MibTableColumn
jnxOperatingCPU = _JnxOperatingCPU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 8),
    _JnxOperatingCPU_Type()
)
jnxOperatingCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingCPU.setStatus("current")
_JnxOperatingISR_Type = Gauge32
_JnxOperatingISR_Object = MibTableColumn
jnxOperatingISR = _JnxOperatingISR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 9),
    _JnxOperatingISR_Type()
)
jnxOperatingISR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingISR.setStatus("current")
_JnxOperatingDRAMSize_Type = Integer32
_JnxOperatingDRAMSize_Object = MibTableColumn
jnxOperatingDRAMSize = _JnxOperatingDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 10),
    _JnxOperatingDRAMSize_Type()
)
jnxOperatingDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingDRAMSize.setStatus("deprecated")
_JnxOperatingBuffer_Type = Gauge32
_JnxOperatingBuffer_Object = MibTableColumn
jnxOperatingBuffer = _JnxOperatingBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 11),
    _JnxOperatingBuffer_Type()
)
jnxOperatingBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingBuffer.setStatus("current")
_JnxOperatingHeap_Type = Gauge32
_JnxOperatingHeap_Object = MibTableColumn
jnxOperatingHeap = _JnxOperatingHeap_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 12),
    _JnxOperatingHeap_Type()
)
jnxOperatingHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingHeap.setStatus("current")
_JnxOperatingUpTime_Type = TimeInterval
_JnxOperatingUpTime_Object = MibTableColumn
jnxOperatingUpTime = _JnxOperatingUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 13),
    _JnxOperatingUpTime_Type()
)
jnxOperatingUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingUpTime.setStatus("deprecated")
_JnxOperatingLastRestart_Type = TimeStamp
_JnxOperatingLastRestart_Object = MibTableColumn
jnxOperatingLastRestart = _JnxOperatingLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 14),
    _JnxOperatingLastRestart_Type()
)
jnxOperatingLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingLastRestart.setStatus("current")
_JnxOperatingMemory_Type = Integer32
_JnxOperatingMemory_Object = MibTableColumn
jnxOperatingMemory = _JnxOperatingMemory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 15),
    _JnxOperatingMemory_Type()
)
jnxOperatingMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingMemory.setStatus("current")


class _JnxOperatingStateOrdered_Type(Integer32):
    """Custom type jnxOperatingStateOrdered based on Integer32"""
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
        *(("down", 6),
          ("ready", 3),
          ("reset", 5),
          ("running", 1),
          ("runningAtFullSpeed", 4),
          ("standby", 2),
          ("unknown", 7))
    )


_JnxOperatingStateOrdered_Type.__name__ = "Integer32"
_JnxOperatingStateOrdered_Object = MibTableColumn
jnxOperatingStateOrdered = _JnxOperatingStateOrdered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 16),
    _JnxOperatingStateOrdered_Type()
)
jnxOperatingStateOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingStateOrdered.setStatus("current")
_JnxOperatingChassisId_Type = JnxChassisId
_JnxOperatingChassisId_Object = MibTableColumn
jnxOperatingChassisId = _JnxOperatingChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 17),
    _JnxOperatingChassisId_Type()
)
jnxOperatingChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingChassisId.setStatus("current")


class _JnxOperatingChassisDescr_Type(DisplayString):
    """Custom type jnxOperatingChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxOperatingChassisDescr_Type.__name__ = "DisplayString"
_JnxOperatingChassisDescr_Object = MibTableColumn
jnxOperatingChassisDescr = _JnxOperatingChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 18),
    _JnxOperatingChassisDescr_Type()
)
jnxOperatingChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingChassisDescr.setStatus("current")
_JnxOperatingRestartTime_Type = DateAndTime
_JnxOperatingRestartTime_Object = MibTableColumn
jnxOperatingRestartTime = _JnxOperatingRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 19),
    _JnxOperatingRestartTime_Type()
)
jnxOperatingRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperatingRestartTime.setStatus("current")
_JnxOperating1MinLoadAvg_Type = Gauge32
_JnxOperating1MinLoadAvg_Object = MibTableColumn
jnxOperating1MinLoadAvg = _JnxOperating1MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 20),
    _JnxOperating1MinLoadAvg_Type()
)
jnxOperating1MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperating1MinLoadAvg.setStatus("current")
_JnxOperating5MinLoadAvg_Type = Gauge32
_JnxOperating5MinLoadAvg_Object = MibTableColumn
jnxOperating5MinLoadAvg = _JnxOperating5MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 21),
    _JnxOperating5MinLoadAvg_Type()
)
jnxOperating5MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperating5MinLoadAvg.setStatus("current")
_JnxOperating15MinLoadAvg_Type = Gauge32
_JnxOperating15MinLoadAvg_Object = MibTableColumn
jnxOperating15MinLoadAvg = _JnxOperating15MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 13, 1, 22),
    _JnxOperating15MinLoadAvg_Type()
)
jnxOperating15MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxOperating15MinLoadAvg.setStatus("current")
_JnxRedundancyTable_Object = MibTable
jnxRedundancyTable = _JnxRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14)
)
if mibBuilder.loadTexts:
    jnxRedundancyTable.setStatus("current")
_JnxRedundancyEntry_Object = MibTableRow
jnxRedundancyEntry = _JnxRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1)
)
jnxRedundancyEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxRedundancyContentsIndex"),
    (0, "JUNIPER-MIB", "jnxRedundancyL1Index"),
    (0, "JUNIPER-MIB", "jnxRedundancyL2Index"),
    (0, "JUNIPER-MIB", "jnxRedundancyL3Index"),
)
if mibBuilder.loadTexts:
    jnxRedundancyEntry.setStatus("current")


class _JnxRedundancyContentsIndex_Type(Integer32):
    """Custom type jnxRedundancyContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxRedundancyContentsIndex_Type.__name__ = "Integer32"
_JnxRedundancyContentsIndex_Object = MibTableColumn
jnxRedundancyContentsIndex = _JnxRedundancyContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 1),
    _JnxRedundancyContentsIndex_Type()
)
jnxRedundancyContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyContentsIndex.setStatus("current")


class _JnxRedundancyL1Index_Type(Integer32):
    """Custom type jnxRedundancyL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxRedundancyL1Index_Type.__name__ = "Integer32"
_JnxRedundancyL1Index_Object = MibTableColumn
jnxRedundancyL1Index = _JnxRedundancyL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 2),
    _JnxRedundancyL1Index_Type()
)
jnxRedundancyL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyL1Index.setStatus("current")


class _JnxRedundancyL2Index_Type(Integer32):
    """Custom type jnxRedundancyL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxRedundancyL2Index_Type.__name__ = "Integer32"
_JnxRedundancyL2Index_Object = MibTableColumn
jnxRedundancyL2Index = _JnxRedundancyL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 3),
    _JnxRedundancyL2Index_Type()
)
jnxRedundancyL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyL2Index.setStatus("current")


class _JnxRedundancyL3Index_Type(Integer32):
    """Custom type jnxRedundancyL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxRedundancyL3Index_Type.__name__ = "Integer32"
_JnxRedundancyL3Index_Object = MibTableColumn
jnxRedundancyL3Index = _JnxRedundancyL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 4),
    _JnxRedundancyL3Index_Type()
)
jnxRedundancyL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyL3Index.setStatus("current")


class _JnxRedundancyDescr_Type(DisplayString):
    """Custom type jnxRedundancyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxRedundancyDescr_Type.__name__ = "DisplayString"
_JnxRedundancyDescr_Object = MibTableColumn
jnxRedundancyDescr = _JnxRedundancyDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 5),
    _JnxRedundancyDescr_Type()
)
jnxRedundancyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyDescr.setStatus("current")


class _JnxRedundancyConfig_Type(Integer32):
    """Custom type jnxRedundancyConfig based on Integer32"""
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
        *(("backup", 3),
          ("disabled", 4),
          ("master", 2),
          ("notApplicable", 5),
          ("unknown", 1))
    )


_JnxRedundancyConfig_Type.__name__ = "Integer32"
_JnxRedundancyConfig_Object = MibTableColumn
jnxRedundancyConfig = _JnxRedundancyConfig_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 6),
    _JnxRedundancyConfig_Type()
)
jnxRedundancyConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyConfig.setStatus("current")


class _JnxRedundancyState_Type(Integer32):
    """Custom type jnxRedundancyState based on Integer32"""
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
        *(("backup", 3),
          ("disabled", 4),
          ("master", 2),
          ("unknown", 1))
    )


_JnxRedundancyState_Type.__name__ = "Integer32"
_JnxRedundancyState_Object = MibTableColumn
jnxRedundancyState = _JnxRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 7),
    _JnxRedundancyState_Type()
)
jnxRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyState.setStatus("current")
_JnxRedundancySwitchoverCount_Type = Counter32
_JnxRedundancySwitchoverCount_Object = MibTableColumn
jnxRedundancySwitchoverCount = _JnxRedundancySwitchoverCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 8),
    _JnxRedundancySwitchoverCount_Type()
)
jnxRedundancySwitchoverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancySwitchoverCount.setStatus("current")
_JnxRedundancySwitchoverTime_Type = TimeStamp
_JnxRedundancySwitchoverTime_Object = MibTableColumn
jnxRedundancySwitchoverTime = _JnxRedundancySwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 9),
    _JnxRedundancySwitchoverTime_Type()
)
jnxRedundancySwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancySwitchoverTime.setStatus("current")


class _JnxRedundancySwitchoverReason_Type(Integer32):
    """Custom type jnxRedundancySwitchoverReason based on Integer32"""
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
        *(("autoSwitched", 4),
          ("neverSwitched", 2),
          ("other", 1),
          ("userSwitched", 3))
    )


_JnxRedundancySwitchoverReason_Type.__name__ = "Integer32"
_JnxRedundancySwitchoverReason_Object = MibTableColumn
jnxRedundancySwitchoverReason = _JnxRedundancySwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 10),
    _JnxRedundancySwitchoverReason_Type()
)
jnxRedundancySwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancySwitchoverReason.setStatus("current")
_JnxRedundancyKeepaliveHeartbeat_Type = Integer32
_JnxRedundancyKeepaliveHeartbeat_Object = MibTableColumn
jnxRedundancyKeepaliveHeartbeat = _JnxRedundancyKeepaliveHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 11),
    _JnxRedundancyKeepaliveHeartbeat_Type()
)
jnxRedundancyKeepaliveHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyKeepaliveHeartbeat.setStatus("current")
_JnxRedundancyKeepaliveTimeout_Type = Integer32
_JnxRedundancyKeepaliveTimeout_Object = MibTableColumn
jnxRedundancyKeepaliveTimeout = _JnxRedundancyKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 12),
    _JnxRedundancyKeepaliveTimeout_Type()
)
jnxRedundancyKeepaliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyKeepaliveTimeout.setStatus("current")
_JnxRedundancyKeepaliveElapsed_Type = Integer32
_JnxRedundancyKeepaliveElapsed_Object = MibTableColumn
jnxRedundancyKeepaliveElapsed = _JnxRedundancyKeepaliveElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 13),
    _JnxRedundancyKeepaliveElapsed_Type()
)
jnxRedundancyKeepaliveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyKeepaliveElapsed.setStatus("current")
_JnxRedundancyKeepaliveLoss_Type = Counter32
_JnxRedundancyKeepaliveLoss_Object = MibTableColumn
jnxRedundancyKeepaliveLoss = _JnxRedundancyKeepaliveLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 14),
    _JnxRedundancyKeepaliveLoss_Type()
)
jnxRedundancyKeepaliveLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyKeepaliveLoss.setStatus("current")
_JnxRedundancyChassisId_Type = JnxChassisId
_JnxRedundancyChassisId_Object = MibTableColumn
jnxRedundancyChassisId = _JnxRedundancyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 15),
    _JnxRedundancyChassisId_Type()
)
jnxRedundancyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyChassisId.setStatus("current")


class _JnxRedundancyChassisDescr_Type(DisplayString):
    """Custom type jnxRedundancyChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxRedundancyChassisDescr_Type.__name__ = "DisplayString"
_JnxRedundancyChassisDescr_Object = MibTableColumn
jnxRedundancyChassisDescr = _JnxRedundancyChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 14, 1, 16),
    _JnxRedundancyChassisDescr_Type()
)
jnxRedundancyChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRedundancyChassisDescr.setStatus("current")
_JnxFruTable_Object = MibTable
jnxFruTable = _JnxFruTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15)
)
if mibBuilder.loadTexts:
    jnxFruTable.setStatus("current")
_JnxFruEntry_Object = MibTableRow
jnxFruEntry = _JnxFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1)
)
jnxFruEntry.setIndexNames(
    (0, "JUNIPER-MIB", "jnxFruContentsIndex"),
    (0, "JUNIPER-MIB", "jnxFruL1Index"),
    (0, "JUNIPER-MIB", "jnxFruL2Index"),
    (0, "JUNIPER-MIB", "jnxFruL3Index"),
)
if mibBuilder.loadTexts:
    jnxFruEntry.setStatus("current")


class _JnxFruContentsIndex_Type(Integer32):
    """Custom type jnxFruContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFruContentsIndex_Type.__name__ = "Integer32"
_JnxFruContentsIndex_Object = MibTableColumn
jnxFruContentsIndex = _JnxFruContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 1),
    _JnxFruContentsIndex_Type()
)
jnxFruContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruContentsIndex.setStatus("current")


class _JnxFruL1Index_Type(Integer32):
    """Custom type jnxFruL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruL1Index_Type.__name__ = "Integer32"
_JnxFruL1Index_Object = MibTableColumn
jnxFruL1Index = _JnxFruL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 2),
    _JnxFruL1Index_Type()
)
jnxFruL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruL1Index.setStatus("current")


class _JnxFruL2Index_Type(Integer32):
    """Custom type jnxFruL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruL2Index_Type.__name__ = "Integer32"
_JnxFruL2Index_Object = MibTableColumn
jnxFruL2Index = _JnxFruL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 3),
    _JnxFruL2Index_Type()
)
jnxFruL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruL2Index.setStatus("current")


class _JnxFruL3Index_Type(Integer32):
    """Custom type jnxFruL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruL3Index_Type.__name__ = "Integer32"
_JnxFruL3Index_Object = MibTableColumn
jnxFruL3Index = _JnxFruL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 4),
    _JnxFruL3Index_Type()
)
jnxFruL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruL3Index.setStatus("current")


class _JnxFruName_Type(DisplayString):
    """Custom type jnxFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFruName_Type.__name__ = "DisplayString"
_JnxFruName_Object = MibTableColumn
jnxFruName = _JnxFruName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 5),
    _JnxFruName_Type()
)
jnxFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruName.setStatus("current")


class _JnxFruType_Type(Integer32):
    """Custom type jnxFruType based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("clockGenerator", 2),
          ("controlBoard", 5),
          ("craftInterfacePanel", 12),
          ("fan", 13),
          ("flexiblePicConcentrator", 3),
          ("forwardingEngineBoard", 15),
          ("frontPanelModule", 8),
          ("lineCardChassis", 14),
          ("other", 1),
          ("portInterfaceCard", 11),
          ("powerEntryModule", 7),
          ("processorMezzanineBoardForSIB", 10),
          ("protectedSystemDomain", 16),
          ("routingEngine", 6),
          ("switchInterfaceBoard", 9),
          ("switchingAndForwardingModule", 4))
    )


_JnxFruType_Type.__name__ = "Integer32"
_JnxFruType_Object = MibTableColumn
jnxFruType = _JnxFruType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 6),
    _JnxFruType_Type()
)
jnxFruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruType.setStatus("current")


class _JnxFruSlot_Type(Integer32):
    """Custom type jnxFruSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFruSlot_Type.__name__ = "Integer32"
_JnxFruSlot_Object = MibTableColumn
jnxFruSlot = _JnxFruSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 7),
    _JnxFruSlot_Type()
)
jnxFruSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruSlot.setStatus("current")


class _JnxFruState_Type(Integer32):
    """Custom type jnxFruState based on Integer32"""
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
        *(("announceOnline", 5),
          ("anounceOffline", 7),
          ("diagnostic", 9),
          ("empty", 2),
          ("offline", 8),
          ("online", 6),
          ("present", 3),
          ("ready", 4),
          ("standby", 10),
          ("unknown", 1))
    )


_JnxFruState_Type.__name__ = "Integer32"
_JnxFruState_Object = MibTableColumn
jnxFruState = _JnxFruState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 8),
    _JnxFruState_Type()
)
jnxFruState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruState.setStatus("current")
_JnxFruTemp_Type = Gauge32
_JnxFruTemp_Object = MibTableColumn
jnxFruTemp = _JnxFruTemp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 9),
    _JnxFruTemp_Type()
)
jnxFruTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruTemp.setStatus("current")


class _JnxFruOfflineReason_Type(Integer32):
    """Custom type jnxFruOfflineReason based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74)
        )
    )
    namedValues = NamedValues(
        *(("badVoltage", 74),
          ("buttonPress", 8),
          ("cliCommand", 7),
          ("cliRestart", 9),
          ("configHoldInReset", 6),
          ("configPowerOff", 5),
          ("cppDisconnect", 43),
          ("cpuNotBoot", 44),
          ("error", 3),
          ("febCfgChange", 68),
          ("febRddCfgChange", 26),
          ("fpcAppFailed", 50),
          ("fpcKernelCrash", 51),
          ("fpcMisconfig", 27),
          ("fpgaSpi4LinkDown", 41),
          ("fruAntiCounterfeitRetry", 64),
          ("fruChasdPowerRatingExceed", 33),
          ("fruConfigOffline", 34),
          ("fruFPCChassisClusterDisable", 65),
          ("fruFPCFabricDownOffline", 67),
          ("fruFabricDown", 63),
          ("fruFebOffline", 31),
          ("fruFebSwitch", 30),
          ("fruFpcUnsupported", 70),
          ("fruFwddReset", 29),
          ("fruInServSoftUpgradeError", 32),
          ("fruPfeReset", 60),
          ("fruReconnectFail", 28),
          ("fruReconnectNotReady", 61),
          ("fruResetThresholdExceeded", 72),
          ("fruServiceRestartRequest", 35),
          ("fruSfLinkDown", 62),
          ("hwAuthenticationFailure", 48),
          ("i3Spi4LinkDown", 42),
          ("lccHardRestart", 20),
          ("lccVersionMismatch", 21),
          ("majorErrors", 18),
          ("masterClockDown", 11),
          ("minorErrors", 19),
          ("noPower", 4),
          ("none", 2),
          ("overtempShutdown", 10),
          ("overvoltage", 24),
          ("packetSchedulingModeChange", 13),
          ("pfeVersionMismatch", 25),
          ("physicalRemoval", 14),
          ("picBounce", 73),
          ("powerCycle", 22),
          ("psdVersionMismatch", 71),
          ("rddPowerOff", 17),
          ("reconnect", 23),
          ("reconnectFpcFail", 49),
          ("routeLocalizationRoleChange", 69),
          ("rstOnSpcSpuFailure", 46),
          ("singleSfmModeChange", 12),
          ("softRstOnSpcSpuFailure", 47),
          ("sonetClockAbsent", 16),
          ("spuCoreDump", 40),
          ("spuCoreDumpComplete", 45),
          ("spuCoreDumpIncomplete", 58),
          ("spuFipsError", 66),
          ("spuFlowdCoreDumpComplete", 54),
          ("spuFlowdCoreDumpIncomplete", 53),
          ("spuFlowdDown", 37),
          ("spuFlowdDownNoCore", 52),
          ("spuIdpdCoreDumpComplete", 57),
          ("spuIdpdCoreDumpIncomplete", 56),
          ("spuIdpdDown", 59),
          ("spuIdpdDownNoCore", 55),
          ("spuResetRequest", 36),
          ("spuSpi4Down", 38),
          ("spuWatchdogTimeout", 39),
          ("unknown", 1),
          ("unresponsiveRestart", 15))
    )


_JnxFruOfflineReason_Type.__name__ = "Integer32"
_JnxFruOfflineReason_Object = MibTableColumn
jnxFruOfflineReason = _JnxFruOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 10),
    _JnxFruOfflineReason_Type()
)
jnxFruOfflineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruOfflineReason.setStatus("current")
_JnxFruLastPowerOff_Type = TimeStamp
_JnxFruLastPowerOff_Object = MibTableColumn
jnxFruLastPowerOff = _JnxFruLastPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 11),
    _JnxFruLastPowerOff_Type()
)
jnxFruLastPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruLastPowerOff.setStatus("current")
_JnxFruLastPowerOn_Type = TimeStamp
_JnxFruLastPowerOn_Object = MibTableColumn
jnxFruLastPowerOn = _JnxFruLastPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 12),
    _JnxFruLastPowerOn_Type()
)
jnxFruLastPowerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruLastPowerOn.setStatus("current")
_JnxFruPowerUpTime_Type = TimeInterval
_JnxFruPowerUpTime_Object = MibTableColumn
jnxFruPowerUpTime = _JnxFruPowerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 13),
    _JnxFruPowerUpTime_Type()
)
jnxFruPowerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruPowerUpTime.setStatus("current")
_JnxFruChassisId_Type = JnxChassisId
_JnxFruChassisId_Object = MibTableColumn
jnxFruChassisId = _JnxFruChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 14),
    _JnxFruChassisId_Type()
)
jnxFruChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruChassisId.setStatus("current")


class _JnxFruChassisDescr_Type(DisplayString):
    """Custom type jnxFruChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFruChassisDescr_Type.__name__ = "DisplayString"
_JnxFruChassisDescr_Object = MibTableColumn
jnxFruChassisDescr = _JnxFruChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 15),
    _JnxFruChassisDescr_Type()
)
jnxFruChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruChassisDescr.setStatus("current")


class _JnxFruPsdAssignment_Type(Integer32):
    """Custom type jnxFruPsdAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_JnxFruPsdAssignment_Type.__name__ = "Integer32"
_JnxFruPsdAssignment_Object = MibTableColumn
jnxFruPsdAssignment = _JnxFruPsdAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 15, 1, 16),
    _JnxFruPsdAssignment_Type()
)
jnxFruPsdAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFruPsdAssignment.setStatus("current")
_JnxBoxKernelMemoryUsedPercent_Type = Integer32
_JnxBoxKernelMemoryUsedPercent_Object = MibScalar
jnxBoxKernelMemoryUsedPercent = _JnxBoxKernelMemoryUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 16),
    _JnxBoxKernelMemoryUsedPercent_Type()
)
jnxBoxKernelMemoryUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxKernelMemoryUsedPercent.setStatus("current")


class _JnxBoxSystemDomainType_Type(Integer32):
    """Custom type jnxBoxSystemDomainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("protectedSystemDomain", 3),
          ("rootSystemDomain", 2))
    )


_JnxBoxSystemDomainType_Type.__name__ = "Integer32"
_JnxBoxSystemDomainType_Object = MibScalar
jnxBoxSystemDomainType = _JnxBoxSystemDomainType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 1, 17),
    _JnxBoxSystemDomainType_Type()
)
jnxBoxSystemDomainType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxBoxSystemDomainType.setStatus("current")

# Managed Objects groups


# Notification objects

jnxPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 1)
)
jnxPowerSupplyFailure.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingState"))
)
if mibBuilder.loadTexts:
    jnxPowerSupplyFailure.setStatus(
        "current"
    )

jnxFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 2)
)
jnxFanFailure.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFanFailure.setStatus(
        "current"
    )

jnxOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 3)
)
jnxOverTemperature.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingTemp"))
)
if mibBuilder.loadTexts:
    jnxOverTemperature.setStatus(
        "current"
    )

jnxRedundancySwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 4)
)
jnxRedundancySwitchover.setObjects(
      *(("JUNIPER-MIB", "jnxRedundancyContentsIndex"),
        ("JUNIPER-MIB", "jnxRedundancyL1Index"),
        ("JUNIPER-MIB", "jnxRedundancyL2Index"),
        ("JUNIPER-MIB", "jnxRedundancyL3Index"),
        ("JUNIPER-MIB", "jnxRedundancyDescr"),
        ("JUNIPER-MIB", "jnxRedundancyConfig"),
        ("JUNIPER-MIB", "jnxRedundancyState"),
        ("JUNIPER-MIB", "jnxRedundancySwitchoverCount"),
        ("JUNIPER-MIB", "jnxRedundancySwitchoverTime"),
        ("JUNIPER-MIB", "jnxRedundancySwitchoverReason"))
)
if mibBuilder.loadTexts:
    jnxRedundancySwitchover.setStatus(
        "current"
    )

jnxFruRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 5)
)
jnxFruRemoval.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruRemoval.setStatus(
        "current"
    )

jnxFruInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 6)
)
jnxFruInsertion.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruInsertion.setStatus(
        "current"
    )

jnxFruPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 7)
)
jnxFruPowerOff.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"),
        ("JUNIPER-MIB", "jnxFruOfflineReason"),
        ("JUNIPER-MIB", "jnxFruLastPowerOff"),
        ("JUNIPER-MIB", "jnxFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFruPowerOff.setStatus(
        "current"
    )

jnxFruPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 8)
)
jnxFruPowerOn.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"),
        ("JUNIPER-MIB", "jnxFruOfflineReason"),
        ("JUNIPER-MIB", "jnxFruLastPowerOff"),
        ("JUNIPER-MIB", "jnxFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFruPowerOn.setStatus(
        "current"
    )

jnxFruFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 9)
)
jnxFruFailed.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruFailed.setStatus(
        "current"
    )

jnxFruOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 10)
)
jnxFruOffline.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"),
        ("JUNIPER-MIB", "jnxFruOfflineReason"),
        ("JUNIPER-MIB", "jnxFruLastPowerOff"),
        ("JUNIPER-MIB", "jnxFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFruOffline.setStatus(
        "current"
    )

jnxFruOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 11)
)
jnxFruOnline.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruOnline.setStatus(
        "current"
    )

jnxFruCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 12)
)
jnxFruCheck.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruCheck.setStatus(
        "current"
    )

jnxFEBSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 13)
)
jnxFEBSwitchover.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFEBSwitchover.setStatus(
        "current"
    )

jnxHardDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 14)
)
jnxHardDiskFailed.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxHardDiskFailed.setStatus(
        "current"
    )

jnxHardDiskMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 15)
)
jnxHardDiskMissing.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxHardDiskMissing.setStatus(
        "current"
    )

jnxBootFromBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1, 16)
)
jnxBootFromBackup.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxBootFromBackup.setStatus(
        "current"
    )

jnxPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2, 1)
)
jnxPowerSupplyOK.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingState"))
)
if mibBuilder.loadTexts:
    jnxPowerSupplyOK.setStatus(
        "current"
    )

jnxFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2, 2)
)
jnxFanOK.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFanOK.setStatus(
        "current"
    )

jnxTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2, 3)
)
jnxTemperatureOK.setObjects(
      *(("JUNIPER-MIB", "jnxContentsContainerIndex"),
        ("JUNIPER-MIB", "jnxContentsL1Index"),
        ("JUNIPER-MIB", "jnxContentsL2Index"),
        ("JUNIPER-MIB", "jnxContentsL3Index"),
        ("JUNIPER-MIB", "jnxContentsDescr"),
        ("JUNIPER-MIB", "jnxOperatingTemp"))
)
if mibBuilder.loadTexts:
    jnxTemperatureOK.setStatus(
        "current"
    )

jnxFruOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2, 4)
)
jnxFruOK.setObjects(
      *(("JUNIPER-MIB", "jnxFruContentsIndex"),
        ("JUNIPER-MIB", "jnxFruL1Index"),
        ("JUNIPER-MIB", "jnxFruL2Index"),
        ("JUNIPER-MIB", "jnxFruL3Index"),
        ("JUNIPER-MIB", "jnxFruName"),
        ("JUNIPER-MIB", "jnxFruType"),
        ("JUNIPER-MIB", "jnxFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFruOK.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MIB",
    **{"JnxChassisId": JnxChassisId,
       "jnxBoxAnatomy": jnxBoxAnatomy,
       "jnxBoxClass": jnxBoxClass,
       "jnxBoxDescr": jnxBoxDescr,
       "jnxBoxSerialNo": jnxBoxSerialNo,
       "jnxBoxRevision": jnxBoxRevision,
       "jnxBoxInstalled": jnxBoxInstalled,
       "jnxContainersTable": jnxContainersTable,
       "jnxContainersEntry": jnxContainersEntry,
       "jnxContainersIndex": jnxContainersIndex,
       "jnxContainersView": jnxContainersView,
       "jnxContainersLevel": jnxContainersLevel,
       "jnxContainersWithin": jnxContainersWithin,
       "jnxContainersType": jnxContainersType,
       "jnxContainersDescr": jnxContainersDescr,
       "jnxContainersCount": jnxContainersCount,
       "jnxContentsLastChange": jnxContentsLastChange,
       "jnxContentsTable": jnxContentsTable,
       "jnxContentsEntry": jnxContentsEntry,
       "jnxContentsContainerIndex": jnxContentsContainerIndex,
       "jnxContentsL1Index": jnxContentsL1Index,
       "jnxContentsL2Index": jnxContentsL2Index,
       "jnxContentsL3Index": jnxContentsL3Index,
       "jnxContentsType": jnxContentsType,
       "jnxContentsDescr": jnxContentsDescr,
       "jnxContentsSerialNo": jnxContentsSerialNo,
       "jnxContentsRevision": jnxContentsRevision,
       "jnxContentsInstalled": jnxContentsInstalled,
       "jnxContentsPartNo": jnxContentsPartNo,
       "jnxContentsChassisId": jnxContentsChassisId,
       "jnxContentsChassisDescr": jnxContentsChassisDescr,
       "jnxContentsChassisCleiCode": jnxContentsChassisCleiCode,
       "jnxLEDLastChange": jnxLEDLastChange,
       "jnxLEDTable": jnxLEDTable,
       "jnxLEDEntry": jnxLEDEntry,
       "jnxLEDAssociateTable": jnxLEDAssociateTable,
       "jnxLEDAssociateIndex": jnxLEDAssociateIndex,
       "jnxLEDL1Index": jnxLEDL1Index,
       "jnxLEDL2Index": jnxLEDL2Index,
       "jnxLEDL3Index": jnxLEDL3Index,
       "jnxLEDOriginator": jnxLEDOriginator,
       "jnxLEDDescr": jnxLEDDescr,
       "jnxLEDState": jnxLEDState,
       "jnxLEDStateOrdered": jnxLEDStateOrdered,
       "jnxFilledLastChange": jnxFilledLastChange,
       "jnxFilledTable": jnxFilledTable,
       "jnxFilledEntry": jnxFilledEntry,
       "jnxFilledContainerIndex": jnxFilledContainerIndex,
       "jnxFilledL1Index": jnxFilledL1Index,
       "jnxFilledL2Index": jnxFilledL2Index,
       "jnxFilledL3Index": jnxFilledL3Index,
       "jnxFilledDescr": jnxFilledDescr,
       "jnxFilledState": jnxFilledState,
       "jnxFilledChassisId": jnxFilledChassisId,
       "jnxFilledChassisDescr": jnxFilledChassisDescr,
       "jnxOperatingTable": jnxOperatingTable,
       "jnxOperatingEntry": jnxOperatingEntry,
       "jnxOperatingContentsIndex": jnxOperatingContentsIndex,
       "jnxOperatingL1Index": jnxOperatingL1Index,
       "jnxOperatingL2Index": jnxOperatingL2Index,
       "jnxOperatingL3Index": jnxOperatingL3Index,
       "jnxOperatingDescr": jnxOperatingDescr,
       "jnxOperatingState": jnxOperatingState,
       "jnxOperatingTemp": jnxOperatingTemp,
       "jnxOperatingCPU": jnxOperatingCPU,
       "jnxOperatingISR": jnxOperatingISR,
       "jnxOperatingDRAMSize": jnxOperatingDRAMSize,
       "jnxOperatingBuffer": jnxOperatingBuffer,
       "jnxOperatingHeap": jnxOperatingHeap,
       "jnxOperatingUpTime": jnxOperatingUpTime,
       "jnxOperatingLastRestart": jnxOperatingLastRestart,
       "jnxOperatingMemory": jnxOperatingMemory,
       "jnxOperatingStateOrdered": jnxOperatingStateOrdered,
       "jnxOperatingChassisId": jnxOperatingChassisId,
       "jnxOperatingChassisDescr": jnxOperatingChassisDescr,
       "jnxOperatingRestartTime": jnxOperatingRestartTime,
       "jnxOperating1MinLoadAvg": jnxOperating1MinLoadAvg,
       "jnxOperating5MinLoadAvg": jnxOperating5MinLoadAvg,
       "jnxOperating15MinLoadAvg": jnxOperating15MinLoadAvg,
       "jnxRedundancyTable": jnxRedundancyTable,
       "jnxRedundancyEntry": jnxRedundancyEntry,
       "jnxRedundancyContentsIndex": jnxRedundancyContentsIndex,
       "jnxRedundancyL1Index": jnxRedundancyL1Index,
       "jnxRedundancyL2Index": jnxRedundancyL2Index,
       "jnxRedundancyL3Index": jnxRedundancyL3Index,
       "jnxRedundancyDescr": jnxRedundancyDescr,
       "jnxRedundancyConfig": jnxRedundancyConfig,
       "jnxRedundancyState": jnxRedundancyState,
       "jnxRedundancySwitchoverCount": jnxRedundancySwitchoverCount,
       "jnxRedundancySwitchoverTime": jnxRedundancySwitchoverTime,
       "jnxRedundancySwitchoverReason": jnxRedundancySwitchoverReason,
       "jnxRedundancyKeepaliveHeartbeat": jnxRedundancyKeepaliveHeartbeat,
       "jnxRedundancyKeepaliveTimeout": jnxRedundancyKeepaliveTimeout,
       "jnxRedundancyKeepaliveElapsed": jnxRedundancyKeepaliveElapsed,
       "jnxRedundancyKeepaliveLoss": jnxRedundancyKeepaliveLoss,
       "jnxRedundancyChassisId": jnxRedundancyChassisId,
       "jnxRedundancyChassisDescr": jnxRedundancyChassisDescr,
       "jnxFruTable": jnxFruTable,
       "jnxFruEntry": jnxFruEntry,
       "jnxFruContentsIndex": jnxFruContentsIndex,
       "jnxFruL1Index": jnxFruL1Index,
       "jnxFruL2Index": jnxFruL2Index,
       "jnxFruL3Index": jnxFruL3Index,
       "jnxFruName": jnxFruName,
       "jnxFruType": jnxFruType,
       "jnxFruSlot": jnxFruSlot,
       "jnxFruState": jnxFruState,
       "jnxFruTemp": jnxFruTemp,
       "jnxFruOfflineReason": jnxFruOfflineReason,
       "jnxFruLastPowerOff": jnxFruLastPowerOff,
       "jnxFruLastPowerOn": jnxFruLastPowerOn,
       "jnxFruPowerUpTime": jnxFruPowerUpTime,
       "jnxFruChassisId": jnxFruChassisId,
       "jnxFruChassisDescr": jnxFruChassisDescr,
       "jnxFruPsdAssignment": jnxFruPsdAssignment,
       "jnxBoxKernelMemoryUsedPercent": jnxBoxKernelMemoryUsedPercent,
       "jnxBoxSystemDomainType": jnxBoxSystemDomainType,
       "jnxPowerSupplyFailure": jnxPowerSupplyFailure,
       "jnxFanFailure": jnxFanFailure,
       "jnxOverTemperature": jnxOverTemperature,
       "jnxRedundancySwitchover": jnxRedundancySwitchover,
       "jnxFruRemoval": jnxFruRemoval,
       "jnxFruInsertion": jnxFruInsertion,
       "jnxFruPowerOff": jnxFruPowerOff,
       "jnxFruPowerOn": jnxFruPowerOn,
       "jnxFruFailed": jnxFruFailed,
       "jnxFruOffline": jnxFruOffline,
       "jnxFruOnline": jnxFruOnline,
       "jnxFruCheck": jnxFruCheck,
       "jnxFEBSwitchover": jnxFEBSwitchover,
       "jnxHardDiskFailed": jnxHardDiskFailed,
       "jnxHardDiskMissing": jnxHardDiskMissing,
       "jnxBootFromBackup": jnxBootFromBackup,
       "jnxPowerSupplyOK": jnxPowerSupplyOK,
       "jnxFanOK": jnxFanOK,
       "jnxTemperatureOK": jnxTemperatureOK,
       "jnxFruOK": jnxFruOK}
)
