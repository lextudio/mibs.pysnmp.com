# SNMP MIB module (OMNITRON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNITRON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:43 2024
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

(OstModeType,
 OstPortList,
 OstPortNumber,
 OstVlanId,
 icAgent,
 omnitron) = mibBuilder.importSymbols(
    "OMNITRON-TC-MIB",
    "OstModeType",
    "OstPortList",
    "OstPortNumber",
    "OstVlanId",
    "icAgent",
    "omnitron")

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
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

omnitronMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 3)
)
omnitronMIB.setRevisions(
        ("2015-10-21 12:00",
         "2015-01-19 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1)
)
chassisEntry.setIndexNames(
    (0, "OMNITRON-MIB", "chassisnum"),
    (0, "OMNITRON-MIB", "slotnum"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")


class _Chassisnum_Type(Integer32):
    """Custom type chassisnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Chassisnum_Type.__name__ = "Integer32"
_Chassisnum_Object = MibTableColumn
chassisnum = _Chassisnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 1),
    _Chassisnum_Type()
)
chassisnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisnum.setStatus("current")


class _Slotnum_Type(Integer32):
    """Custom type slotnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_Slotnum_Type.__name__ = "Integer32"
_Slotnum_Object = MibTableColumn
slotnum = _Slotnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 2),
    _Slotnum_Type()
)
slotnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotnum.setStatus("current")


class _Chassistype_Type(Integer32):
    """Custom type chassistype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Chassistype_Type.__name__ = "Integer32"
_Chassistype_Object = MibTableColumn
chassistype = _Chassistype_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 3),
    _Chassistype_Type()
)
chassistype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassistype.setStatus("current")


class _Prodtype_Type(Integer32):
    """Custom type prodtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Prodtype_Type.__name__ = "Integer32"
_Prodtype_Object = MibTableColumn
prodtype = _Prodtype_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 4),
    _Prodtype_Type()
)
prodtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodtype.setStatus("current")


class _Chassisname_Type(DisplayString):
    """Custom type chassisname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Chassisname_Type.__name__ = "DisplayString"
_Chassisname_Object = MibTableColumn
chassisname = _Chassisname_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 5),
    _Chassisname_Type()
)
chassisname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisname.setStatus("current")


class _Partnum_Type(DisplayString):
    """Custom type partnum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Partnum_Type.__name__ = "DisplayString"
_Partnum_Object = MibTableColumn
partnum = _Partnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 6),
    _Partnum_Type()
)
partnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    partnum.setStatus("current")


class _Serialnum_Type(DisplayString):
    """Custom type serialnum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Serialnum_Type.__name__ = "DisplayString"
_Serialnum_Object = MibTableColumn
serialnum = _Serialnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 7),
    _Serialnum_Type()
)
serialnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialnum.setStatus("current")


class _Manufdate_Type(DisplayString):
    """Custom type manufdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Manufdate_Type.__name__ = "DisplayString"
_Manufdate_Object = MibTableColumn
manufdate = _Manufdate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 8),
    _Manufdate_Type()
)
manufdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufdate.setStatus("current")


class _Softrev_Type(Integer32):
    """Custom type softrev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Softrev_Type.__name__ = "Integer32"
_Softrev_Object = MibTableColumn
softrev = _Softrev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 9),
    _Softrev_Type()
)
softrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softrev.setStatus("current")


class _Prodrev_Type(Integer32):
    """Custom type prodrev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Prodrev_Type.__name__ = "Integer32"
_Prodrev_Object = MibTableColumn
prodrev = _Prodrev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 10),
    _Prodrev_Type()
)
prodrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prodrev.setStatus("current")
_Ledstat_Type = Integer32
_Ledstat_Object = MibTableColumn
ledstat = _Ledstat_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 11),
    _Ledstat_Type()
)
ledstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledstat.setStatus("current")
_Switchstat_Type = Integer32
_Switchstat_Object = MibTableColumn
switchstat = _Switchstat_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 12),
    _Switchstat_Type()
)
switchstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchstat.setStatus("current")
_Extended1_Type = Integer32
_Extended1_Object = MibTableColumn
extended1 = _Extended1_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 13),
    _Extended1_Type()
)
extended1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended1.setStatus("current")
_Extended2_Type = Integer32
_Extended2_Object = MibTableColumn
extended2 = _Extended2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 14),
    _Extended2_Type()
)
extended2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended2.setStatus("current")
_Extended3_Type = Integer32
_Extended3_Object = MibTableColumn
extended3 = _Extended3_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 15),
    _Extended3_Type()
)
extended3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended3.setStatus("current")
_Extended4_Type = Integer32
_Extended4_Object = MibTableColumn
extended4 = _Extended4_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 16),
    _Extended4_Type()
)
extended4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended4.setStatus("current")
_Extended5_Type = Integer32
_Extended5_Object = MibTableColumn
extended5 = _Extended5_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 17),
    _Extended5_Type()
)
extended5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended5.setStatus("current")
_Extended6_Type = Integer32
_Extended6_Object = MibTableColumn
extended6 = _Extended6_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 18),
    _Extended6_Type()
)
extended6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extended6.setStatus("current")
_Resetmod_Type = Integer32
_Resetmod_Object = MibTableColumn
resetmod = _Resetmod_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 19),
    _Resetmod_Type()
)
resetmod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetmod.setStatus("current")
_Wrswitch_Type = Integer32
_Wrswitch_Object = MibTableColumn
wrswitch = _Wrswitch_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 20),
    _Wrswitch_Type()
)
wrswitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wrswitch.setStatus("current")


class _Modulename_Type(DisplayString):
    """Custom type modulename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Modulename_Type.__name__ = "DisplayString"
_Modulename_Object = MibTableColumn
modulename = _Modulename_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 1, 1, 21),
    _Modulename_Type()
)
modulename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modulename.setStatus("current")


class _Chassis_Type(Integer32):
    """Custom type chassis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Chassis_Type.__name__ = "Integer32"
_Chassis_Object = MibScalar
chassis = _Chassis_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 6),
    _Chassis_Type()
)
chassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis.setStatus("current")


class _SelfSlot_Type(Integer32):
    """Custom type selfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_SelfSlot_Type.__name__ = "Integer32"
_SelfSlot_Object = MibScalar
selfSlot = _SelfSlot_Object(
    (1, 3, 6, 1, 4, 1, 7342, 1, 8),
    _SelfSlot_Type()
)
selfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfSlot.setStatus("current")
_ProdAgent_ObjectIdentity = ObjectIdentity
prodAgent = _ProdAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 2)
)
_EnhancedchassisTable_ObjectIdentity = ObjectIdentity
enhancedchassisTable = _EnhancedchassisTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1)
)


class _ModuleCount_Type(Integer32):
    """Custom type moduleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_ModuleCount_Type.__name__ = "Integer32"
_ModuleCount_Object = MibScalar
moduleCount = _ModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 1),
    _ModuleCount_Type()
)
moduleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleCount.setStatus("current")
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1)
)
moduleEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _Modchassnum_Type(Integer32):
    """Custom type modchassnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Modchassnum_Type.__name__ = "Integer32"
_Modchassnum_Object = MibTableColumn
modchassnum = _Modchassnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 1),
    _Modchassnum_Type()
)
modchassnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modchassnum.setStatus("current")


class _Modslotnum_Type(Integer32):
    """Custom type modslotnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 22),
    )


_Modslotnum_Type.__name__ = "Integer32"
_Modslotnum_Object = MibTableColumn
modslotnum = _Modslotnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 2),
    _Modslotnum_Type()
)
modslotnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modslotnum.setStatus("current")


class _Modchasstype_Type(Integer32):
    """Custom type modchasstype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Modchasstype_Type.__name__ = "Integer32"
_Modchasstype_Object = MibTableColumn
modchasstype = _Modchasstype_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 3),
    _Modchasstype_Type()
)
modchasstype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modchasstype.setStatus("current")


class _Modprodtype_Type(Integer32):
    """Custom type modprodtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Modprodtype_Type.__name__ = "Integer32"
_Modprodtype_Object = MibTableColumn
modprodtype = _Modprodtype_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 4),
    _Modprodtype_Type()
)
modprodtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modprodtype.setStatus("current")
_Modsoftrev_Type = Integer32
_Modsoftrev_Object = MibTableColumn
modsoftrev = _Modsoftrev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 5),
    _Modsoftrev_Type()
)
modsoftrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modsoftrev.setStatus("current")
_Modprodrev_Type = Integer32
_Modprodrev_Object = MibTableColumn
modprodrev = _Modprodrev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 6),
    _Modprodrev_Type()
)
modprodrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modprodrev.setStatus("current")
_Modreset_Type = Integer32
_Modreset_Object = MibTableColumn
modreset = _Modreset_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 7),
    _Modreset_Type()
)
modreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modreset.setStatus("current")
_Modnumports_Type = Integer32
_Modnumports_Object = MibTableColumn
modnumports = _Modnumports_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 8),
    _Modnumports_Type()
)
modnumports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modnumports.setStatus("current")


class _Modchassname_Type(DisplayString):
    """Custom type modchassname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Modchassname_Type.__name__ = "DisplayString"
_Modchassname_Object = MibTableColumn
modchassname = _Modchassname_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 9),
    _Modchassname_Type()
)
modchassname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modchassname.setStatus("current")


class _Modpartnum_Type(DisplayString):
    """Custom type modpartnum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Modpartnum_Type.__name__ = "DisplayString"
_Modpartnum_Object = MibTableColumn
modpartnum = _Modpartnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 10),
    _Modpartnum_Type()
)
modpartnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modpartnum.setStatus("current")


class _Modserialnum_Type(DisplayString):
    """Custom type modserialnum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Modserialnum_Type.__name__ = "DisplayString"
_Modserialnum_Object = MibTableColumn
modserialnum = _Modserialnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 11),
    _Modserialnum_Type()
)
modserialnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modserialnum.setStatus("current")


class _Modmanufdate_Type(DisplayString):
    """Custom type modmanufdate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Modmanufdate_Type.__name__ = "DisplayString"
_Modmanufdate_Object = MibTableColumn
modmanufdate = _Modmanufdate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 12),
    _Modmanufdate_Type()
)
modmanufdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modmanufdate.setStatus("current")


class _Modname_Type(DisplayString):
    """Custom type modname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Modname_Type.__name__ = "DisplayString"
_Modname_Object = MibTableColumn
modname = _Modname_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 13),
    _Modname_Type()
)
modname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modname.setStatus("current")
_Modportvlan_Type = Integer32
_Modportvlan_Object = MibTableColumn
modportvlan = _Modportvlan_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 14),
    _Modportvlan_Type()
)
modportvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modportvlan.setStatus("current")
_Modextfeaturebits_Type = Integer32
_Modextfeaturebits_Object = MibTableColumn
modextfeaturebits = _Modextfeaturebits_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 15),
    _Modextfeaturebits_Type()
)
modextfeaturebits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modextfeaturebits.setStatus("current")
_Modswbuildnum_Type = Integer32
_Modswbuildnum_Object = MibTableColumn
modswbuildnum = _Modswbuildnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 16),
    _Modswbuildnum_Type()
)
modswbuildnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modswbuildnum.setStatus("current")


class _Modenable802dot1qProcessing_Type(Integer32):
    """Custom type modenable802dot1qProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modenable802dot1qProcessing_Type.__name__ = "Integer32"
_Modenable802dot1qProcessing_Object = MibTableColumn
modenable802dot1qProcessing = _Modenable802dot1qProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 17),
    _Modenable802dot1qProcessing_Type()
)
modenable802dot1qProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modenable802dot1qProcessing.setStatus("current")


class _Modtagsubstitution_Type(Integer32):
    """Custom type modtagsubstitution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modtagsubstitution_Type.__name__ = "Integer32"
_Modtagsubstitution_Object = MibTableColumn
modtagsubstitution = _Modtagsubstitution_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 18),
    _Modtagsubstitution_Type()
)
modtagsubstitution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modtagsubstitution.setStatus("current")


class _ModcommitVLANchanges_Type(Integer32):
    """Custom type modcommitVLANchanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ModcommitVLANchanges_Type.__name__ = "Integer32"
_ModcommitVLANchanges_Object = MibTableColumn
modcommitVLANchanges = _ModcommitVLANchanges_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 19),
    _ModcommitVLANchanges_Type()
)
modcommitVLANchanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modcommitVLANchanges.setStatus("current")


class _ModvlanTableClear_Type(Integer32):
    """Custom type modvlanTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ModvlanTableClear_Type.__name__ = "Integer32"
_ModvlanTableClear_Object = MibTableColumn
modvlanTableClear = _ModvlanTableClear_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 20),
    _ModvlanTableClear_Type()
)
modvlanTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modvlanTableClear.setStatus("current")


class _ModcommitNMMCfgChanges_Type(Integer32):
    """Custom type modcommitNMMCfgChanges based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ModcommitNMMCfgChanges_Type.__name__ = "Integer32"
_ModcommitNMMCfgChanges_Object = MibTableColumn
modcommitNMMCfgChanges = _ModcommitNMMCfgChanges_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 21),
    _ModcommitNMMCfgChanges_Type()
)
modcommitNMMCfgChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modcommitNMMCfgChanges.setStatus("current")
_ModLM80volts_Type = Integer32
_ModLM80volts_Object = MibTableColumn
modLM80volts = _ModLM80volts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 22),
    _ModLM80volts_Type()
)
modLM80volts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modLM80volts.setStatus("current")
_ModLM80currents_Type = Integer32
_ModLM80currents_Object = MibTableColumn
modLM80currents = _ModLM80currents_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 23),
    _ModLM80currents_Type()
)
modLM80currents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modLM80currents.setStatus("current")
_ModLM80misc_Type = Integer32
_ModLM80misc_Object = MibTableColumn
modLM80misc = _ModLM80misc_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 24),
    _ModLM80misc_Type()
)
modLM80misc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modLM80misc.setStatus("current")


class _ModRestoreFactoryDefaults_Type(Integer32):
    """Custom type modRestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_ModRestoreFactoryDefaults_Type.__name__ = "Integer32"
_ModRestoreFactoryDefaults_Object = MibTableColumn
modRestoreFactoryDefaults = _ModRestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 25),
    _ModRestoreFactoryDefaults_Type()
)
modRestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modRestoreFactoryDefaults.setStatus("current")


class _CoreStatusOnly_Type(Integer32):
    """Custom type coreStatusOnly based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CoreStatusOnly_Type.__name__ = "Integer32"
_CoreStatusOnly_Object = MibTableColumn
coreStatusOnly = _CoreStatusOnly_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 26),
    _CoreStatusOnly_Type()
)
coreStatusOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coreStatusOnly.setStatus("current")


class _IngressPolicingType_Type(Integer32):
    """Custom type ingressPolicingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IngressPolicingType_Type.__name__ = "Integer32"
_IngressPolicingType_Object = MibTableColumn
ingressPolicingType = _IngressPolicingType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 27),
    _IngressPolicingType_Type()
)
ingressPolicingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressPolicingType.setStatus("current")
_Vlanservicetag_Type = Integer32
_Vlanservicetag_Object = MibTableColumn
vlanservicetag = _Vlanservicetag_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 28),
    _Vlanservicetag_Type()
)
vlanservicetag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanservicetag.setStatus("current")
_DefaultForwardingMap_Type = Integer32
_DefaultForwardingMap_Object = MibTableColumn
defaultForwardingMap = _DefaultForwardingMap_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 29),
    _DefaultForwardingMap_Type()
)
defaultForwardingMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultForwardingMap.setStatus("current")


class _ModFpgaRev_Type(DisplayString):
    """Custom type modFpgaRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModFpgaRev_Type.__name__ = "DisplayString"
_ModFpgaRev_Object = MibTableColumn
modFpgaRev = _ModFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 30),
    _ModFpgaRev_Type()
)
modFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFpgaRev.setStatus("current")


class _ModExpPartNumber_Type(DisplayString):
    """Custom type modExpPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ModExpPartNumber_Type.__name__ = "DisplayString"
_ModExpPartNumber_Object = MibTableColumn
modExpPartNumber = _ModExpPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 31),
    _ModExpPartNumber_Type()
)
modExpPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modExpPartNumber.setStatus("current")


class _ModExpSoftwareRev_Type(DisplayString):
    """Custom type modExpSoftwareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ModExpSoftwareRev_Type.__name__ = "DisplayString"
_ModExpSoftwareRev_Object = MibTableColumn
modExpSoftwareRev = _ModExpSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 32),
    _ModExpSoftwareRev_Type()
)
modExpSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modExpSoftwareRev.setStatus("current")
_ModExpLedStatus_Type = OctetString
_ModExpLedStatus_Object = MibTableColumn
modExpLedStatus = _ModExpLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 33),
    _ModExpLedStatus_Type()
)
modExpLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modExpLedStatus.setStatus("current")


class _ModHwRev_Type(DisplayString):
    """Custom type modHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModHwRev_Type.__name__ = "DisplayString"
_ModHwRev_Object = MibTableColumn
modHwRev = _ModHwRev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 34),
    _ModHwRev_Type()
)
modHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modHwRev.setStatus("current")


class _ModPcbRev_Type(DisplayString):
    """Custom type modPcbRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ModPcbRev_Type.__name__ = "DisplayString"
_ModPcbRev_Object = MibTableColumn
modPcbRev = _ModPcbRev_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 2, 1, 35),
    _ModPcbRev_Type()
)
modPcbRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modPcbRev.setStatus("current")
_ModuleMgtCfgTable_Object = MibTable
moduleMgtCfgTable = _ModuleMgtCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3)
)
if mibBuilder.loadTexts:
    moduleMgtCfgTable.setStatus("current")
_ModuleMgtCfgEntry_Object = MibTableRow
moduleMgtCfgEntry = _ModuleMgtCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1)
)
moduleMgtCfgEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
)
if mibBuilder.loadTexts:
    moduleMgtCfgEntry.setStatus("current")


class _SysAdminStatus_Type(Integer32):
    """Custom type sysAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SysAdminStatus_Type.__name__ = "Integer32"
_SysAdminStatus_Object = MibTableColumn
sysAdminStatus = _SysAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 1),
    _SysAdminStatus_Type()
)
sysAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminStatus.setStatus("current")


class _SysDateTime_Type(DisplayString):
    """Custom type sysDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )


_SysDateTime_Type.__name__ = "DisplayString"
_SysDateTime_Object = MibTableColumn
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 2),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")


class _MacAddr_Type(DisplayString):
    """Custom type macAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_MacAddr_Type.__name__ = "DisplayString"
_MacAddr_Object = MibTableColumn
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 3),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibTableColumn
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 4),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_Subnetmask_Type = IpAddress
_Subnetmask_Object = MibTableColumn
subnetmask = _Subnetmask_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 5),
    _Subnetmask_Type()
)
subnetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetmask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibTableColumn
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 6),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")


class _ReadCommunity_Type(DisplayString):
    """Custom type readCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ReadCommunity_Type.__name__ = "DisplayString"
_ReadCommunity_Object = MibTableColumn
readCommunity = _ReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 7),
    _ReadCommunity_Type()
)
readCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readCommunity.setStatus("current")


class _WriteCommunity_Type(DisplayString):
    """Custom type writeCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WriteCommunity_Type.__name__ = "DisplayString"
_WriteCommunity_Object = MibTableColumn
writeCommunity = _WriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 8),
    _WriteCommunity_Type()
)
writeCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writeCommunity.setStatus("current")


class _Mychassnum_Type(Integer32):
    """Custom type mychassnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 19),
    )


_Mychassnum_Type.__name__ = "Integer32"
_Mychassnum_Object = MibTableColumn
mychassnum = _Mychassnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 9),
    _Mychassnum_Type()
)
mychassnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mychassnum.setStatus("current")


class _Mmname_Type(DisplayString):
    """Custom type mmname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Mmname_Type.__name__ = "DisplayString"
_Mmname_Object = MibTableColumn
mmname = _Mmname_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 10),
    _Mmname_Type()
)
mmname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mmname.setStatus("current")
_Traphost1_Type = IpAddress
_Traphost1_Object = MibTableColumn
traphost1 = _Traphost1_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 11),
    _Traphost1_Type()
)
traphost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost1.setStatus("current")
_Traphost2_Type = IpAddress
_Traphost2_Object = MibTableColumn
traphost2 = _Traphost2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 12),
    _Traphost2_Type()
)
traphost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost2.setStatus("current")
_Traphost3_Type = IpAddress
_Traphost3_Object = MibTableColumn
traphost3 = _Traphost3_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 13),
    _Traphost3_Type()
)
traphost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost3.setStatus("current")
_Traphost4_Type = IpAddress
_Traphost4_Object = MibTableColumn
traphost4 = _Traphost4_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 14),
    _Traphost4_Type()
)
traphost4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost4.setStatus("current")
_Traphost5_Type = IpAddress
_Traphost5_Object = MibTableColumn
traphost5 = _Traphost5_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 15),
    _Traphost5_Type()
)
traphost5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost5.setStatus("current")
_Traphost6_Type = IpAddress
_Traphost6_Object = MibTableColumn
traphost6 = _Traphost6_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 16),
    _Traphost6_Type()
)
traphost6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost6.setStatus("current")
_Traphost7_Type = IpAddress
_Traphost7_Object = MibTableColumn
traphost7 = _Traphost7_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 17),
    _Traphost7_Type()
)
traphost7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost7.setStatus("current")
_Traphost8_Type = IpAddress
_Traphost8_Object = MibTableColumn
traphost8 = _Traphost8_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 18),
    _Traphost8_Type()
)
traphost8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    traphost8.setStatus("current")


class _Sysloc_Type(DisplayString):
    """Custom type sysloc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Sysloc_Type.__name__ = "DisplayString"
_Sysloc_Object = MibTableColumn
sysloc = _Sysloc_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 19),
    _Sysloc_Type()
)
sysloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysloc.setStatus("current")


class _Syscon_Type(DisplayString):
    """Custom type syscon based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Syscon_Type.__name__ = "DisplayString"
_Syscon_Object = MibTableColumn
syscon = _Syscon_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 20),
    _Syscon_Type()
)
syscon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syscon.setStatus("current")


class _Serialpass_Type(DisplayString):
    """Custom type serialpass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Serialpass_Type.__name__ = "DisplayString"
_Serialpass_Object = MibTableColumn
serialpass = _Serialpass_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 21),
    _Serialpass_Type()
)
serialpass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialpass.setStatus("current")


class _Telnetpass_Type(DisplayString):
    """Custom type telnetpass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Telnetpass_Type.__name__ = "DisplayString"
_Telnetpass_Object = MibTableColumn
telnetpass = _Telnetpass_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 22),
    _Telnetpass_Type()
)
telnetpass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetpass.setStatus("current")


class _Ftppasswrd_Type(DisplayString):
    """Custom type ftppasswrd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Ftppasswrd_Type.__name__ = "DisplayString"
_Ftppasswrd_Object = MibTableColumn
ftppasswrd = _Ftppasswrd_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 23),
    _Ftppasswrd_Type()
)
ftppasswrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftppasswrd.setStatus("current")


class _KeepAliveInterval_Type(Integer32):
    """Custom type keepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_KeepAliveInterval_Type.__name__ = "Integer32"
_KeepAliveInterval_Object = MibTableColumn
keepAliveInterval = _KeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 24),
    _KeepAliveInterval_Type()
)
keepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keepAliveInterval.setStatus("current")
_VlanIdOst_Type = OstVlanId
_VlanIdOst_Object = MibTableColumn
vlanIdOst = _VlanIdOst_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 25),
    _VlanIdOst_Type()
)
vlanIdOst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdOst.setStatus("current")


class _NmmCfgSerialBaudrate_Type(Integer32):
    """Custom type nmmCfgSerialBaudrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_NmmCfgSerialBaudrate_Type.__name__ = "Integer32"
_NmmCfgSerialBaudrate_Object = MibTableColumn
nmmCfgSerialBaudrate = _NmmCfgSerialBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 26),
    _NmmCfgSerialBaudrate_Type()
)
nmmCfgSerialBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmmCfgSerialBaudrate.setStatus("current")


class _EnabledFunctions_Type(Integer32):
    """Custom type enabledFunctions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnabledFunctions_Type.__name__ = "Integer32"
_EnabledFunctions_Object = MibTableColumn
enabledFunctions = _EnabledFunctions_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 27),
    _EnabledFunctions_Type()
)
enabledFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enabledFunctions.setStatus("current")


class _EnableSNMPFunction_Type(Integer32):
    """Custom type enableSNMPFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnableSNMPFunction_Type.__name__ = "Integer32"
_EnableSNMPFunction_Object = MibTableColumn
enableSNMPFunction = _EnableSNMPFunction_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 28),
    _EnableSNMPFunction_Type()
)
enableSNMPFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPFunction.setStatus("current")
_NmmCfgState_Type = Integer32
_NmmCfgState_Object = MibTableColumn
nmmCfgState = _NmmCfgState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 29),
    _NmmCfgState_Type()
)
nmmCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmmCfgState.setStatus("current")


class _NmmSecureMode_Type(Integer32):
    """Custom type nmmSecureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NmmSecureMode_Type.__name__ = "Integer32"
_NmmSecureMode_Object = MibTableColumn
nmmSecureMode = _NmmSecureMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 30),
    _NmmSecureMode_Type()
)
nmmSecureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmmSecureMode.setStatus("current")


class _NmmSecureConnState_Type(Integer32):
    """Custom type nmmSecureConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_NmmSecureConnState_Type.__name__ = "Integer32"
_NmmSecureConnState_Object = MibTableColumn
nmmSecureConnState = _NmmSecureConnState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 31),
    _NmmSecureConnState_Type()
)
nmmSecureConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmmSecureConnState.setStatus("current")


class _NmmIpProtocolState_Type(Integer32):
    """Custom type nmmIpProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NmmIpProtocolState_Type.__name__ = "Integer32"
_NmmIpProtocolState_Object = MibTableColumn
nmmIpProtocolState = _NmmIpProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 32),
    _NmmIpProtocolState_Type()
)
nmmIpProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmmIpProtocolState.setStatus("current")


class _NmmIpDisabled_Type(Integer32):
    """Custom type nmmIpDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NmmIpDisabled_Type.__name__ = "Integer32"
_NmmIpDisabled_Object = MibTableColumn
nmmIpDisabled = _NmmIpDisabled_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 33),
    _NmmIpDisabled_Type()
)
nmmIpDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmmIpDisabled.setStatus("current")


class _VlanPri_Type(Integer32):
    """Custom type vlanPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanPri_Type.__name__ = "Integer32"
_VlanPri_Object = MibTableColumn
vlanPri = _VlanPri_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 34),
    _VlanPri_Type()
)
vlanPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPri.setStatus("current")


class _EnableSNMPWrites_Type(Integer32):
    """Custom type enableSNMPWrites based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnableSNMPWrites_Type.__name__ = "Integer32"
_EnableSNMPWrites_Object = MibTableColumn
enableSNMPWrites = _EnableSNMPWrites_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 35),
    _EnableSNMPWrites_Type()
)
enableSNMPWrites.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPWrites.setStatus("current")
_CpuVoltageIn_Type = Integer32
_CpuVoltageIn_Object = MibTableColumn
cpuVoltageIn = _CpuVoltageIn_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 36),
    _CpuVoltageIn_Type()
)
cpuVoltageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVoltageIn.setStatus("current")
_CpuVoltageOut_Type = Integer32
_CpuVoltageOut_Object = MibTableColumn
cpuVoltageOut = _CpuVoltageOut_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 37),
    _CpuVoltageOut_Type()
)
cpuVoltageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVoltageOut.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibTableColumn
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 38),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")


class _NmmSecureSlaveSlot_Type(Integer32):
    """Custom type nmmSecureSlaveSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_NmmSecureSlaveSlot_Type.__name__ = "Integer32"
_NmmSecureSlaveSlot_Object = MibTableColumn
nmmSecureSlaveSlot = _NmmSecureSlaveSlot_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 39),
    _NmmSecureSlaveSlot_Type()
)
nmmSecureSlaveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmmSecureSlaveSlot.setStatus("current")
_DhcpIpAddr_Type = IpAddress
_DhcpIpAddr_Object = MibTableColumn
dhcpIpAddr = _DhcpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 40),
    _DhcpIpAddr_Type()
)
dhcpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpIpAddr.setStatus("current")
_DhcpSubnetmask_Type = IpAddress
_DhcpSubnetmask_Object = MibTableColumn
dhcpSubnetmask = _DhcpSubnetmask_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 41),
    _DhcpSubnetmask_Type()
)
dhcpSubnetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSubnetmask.setStatus("current")
_DhcpGateway_Type = IpAddress
_DhcpGateway_Object = MibTableColumn
dhcpGateway = _DhcpGateway_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 42),
    _DhcpGateway_Type()
)
dhcpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpGateway.setStatus("current")


class _NmmOAMmgmtMode_Type(Integer32):
    """Custom type nmmOAMmgmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NmmOAMmgmtMode_Type.__name__ = "Integer32"
_NmmOAMmgmtMode_Object = MibTableColumn
nmmOAMmgmtMode = _NmmOAMmgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 43),
    _NmmOAMmgmtMode_Type()
)
nmmOAMmgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmmOAMmgmtMode.setStatus("current")


class _Customertag_Type(Integer32):
    """Custom type customertag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Customertag_Type.__name__ = "Integer32"
_Customertag_Object = MibTableColumn
customertag = _Customertag_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 44),
    _Customertag_Type()
)
customertag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customertag.setStatus("current")


class _Servicetag_Type(Integer32):
    """Custom type servicetag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Servicetag_Type.__name__ = "Integer32"
_Servicetag_Object = MibTableColumn
servicetag = _Servicetag_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 45),
    _Servicetag_Type()
)
servicetag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    servicetag.setStatus("current")


class _CnodeControl_Type(Integer32):
    """Custom type cnodeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CnodeControl_Type.__name__ = "Integer32"
_CnodeControl_Object = MibTableColumn
cnodeControl = _CnodeControl_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 46),
    _CnodeControl_Type()
)
cnodeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnodeControl.setStatus("current")


class _CnodeCIR_Type(Integer32):
    """Custom type cnodeCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CnodeCIR_Type.__name__ = "Integer32"
_CnodeCIR_Object = MibTableColumn
cnodeCIR = _CnodeCIR_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 47),
    _CnodeCIR_Type()
)
cnodeCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnodeCIR.setStatus("current")


class _EnableSNMPv3Function_Type(Integer32):
    """Custom type enableSNMPv3Function based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_EnableSNMPv3Function_Type.__name__ = "Integer32"
_EnableSNMPv3Function_Object = MibTableColumn
enableSNMPv3Function = _EnableSNMPv3Function_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 48),
    _EnableSNMPv3Function_Type()
)
enableSNMPv3Function.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSNMPv3Function.setStatus("current")


class _SlaveWrite_Type(Integer32):
    """Custom type slaveWrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SlaveWrite_Type.__name__ = "Integer32"
_SlaveWrite_Object = MibTableColumn
slaveWrite = _SlaveWrite_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 49),
    _SlaveWrite_Type()
)
slaveWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveWrite.setStatus("current")


class _SnmpTrapType_Type(Integer32):
    """Custom type snmpTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SnmpTrapType_Type.__name__ = "Integer32"
_SnmpTrapType_Object = MibTableColumn
snmpTrapType = _SnmpTrapType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 50),
    _SnmpTrapType_Type()
)
snmpTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapType.setStatus("current")


class _CapsMask_Type(Unsigned32):
    """Custom type capsMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CapsMask_Type.__name__ = "Unsigned32"
_CapsMask_Object = MibTableColumn
capsMask = _CapsMask_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 51),
    _CapsMask_Type()
)
capsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsMask.setStatus("current")


class _SlaveTraps_Type(Integer32):
    """Custom type slaveTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SlaveTraps_Type.__name__ = "Integer32"
_SlaveTraps_Object = MibTableColumn
slaveTraps = _SlaveTraps_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 52),
    _SlaveTraps_Type()
)
slaveTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveTraps.setStatus("current")


class _SlaveTrapsForward_Type(Integer32):
    """Custom type slaveTrapsForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_SlaveTrapsForward_Type.__name__ = "Integer32"
_SlaveTrapsForward_Object = MibTableColumn
slaveTrapsForward = _SlaveTrapsForward_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 53),
    _SlaveTrapsForward_Type()
)
slaveTrapsForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaveTrapsForward.setStatus("current")
_IpAddr2_Type = IpAddress
_IpAddr2_Object = MibTableColumn
ipAddr2 = _IpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 54),
    _IpAddr2_Type()
)
ipAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr2.setStatus("current")
_Subnetmask2_Type = IpAddress
_Subnetmask2_Object = MibTableColumn
subnetmask2 = _Subnetmask2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 55),
    _Subnetmask2_Type()
)
subnetmask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetmask2.setStatus("current")
_Gateway2_Type = IpAddress
_Gateway2_Object = MibTableColumn
gateway2 = _Gateway2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 56),
    _Gateway2_Type()
)
gateway2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway2.setStatus("current")


class _IpaddrEVCassociation_Type(DisplayString):
    """Custom type ipaddrEVCassociation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_IpaddrEVCassociation_Type.__name__ = "DisplayString"
_IpaddrEVCassociation_Object = MibTableColumn
ipaddrEVCassociation = _IpaddrEVCassociation_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 57),
    _IpaddrEVCassociation_Type()
)
ipaddrEVCassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipaddrEVCassociation.setStatus("current")


class _Ipaddr2EVCassociation_Type(DisplayString):
    """Custom type ipaddr2EVCassociation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_Ipaddr2EVCassociation_Type.__name__ = "DisplayString"
_Ipaddr2EVCassociation_Object = MibTableColumn
ipaddr2EVCassociation = _Ipaddr2EVCassociation_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 58),
    _Ipaddr2EVCassociation_Type()
)
ipaddr2EVCassociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipaddr2EVCassociation.setStatus("current")


class _BootpEnable_Type(TruthValue):
    """Custom type bootpEnable based on TruthValue"""
    defaultValue = 2


_BootpEnable_Object = MibTableColumn
bootpEnable = _BootpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 59),
    _BootpEnable_Type()
)
bootpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootpEnable.setStatus("current")


class _TftpEnable_Type(TruthValue):
    """Custom type tftpEnable based on TruthValue"""
    defaultValue = 2


_TftpEnable_Object = MibTableColumn
tftpEnable = _TftpEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 60),
    _TftpEnable_Type()
)
tftpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpEnable.setStatus("current")
_TftpServerIpAddress_Type = IpAddress
_TftpServerIpAddress_Object = MibTableColumn
tftpServerIpAddress = _TftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 61),
    _TftpServerIpAddress_Type()
)
tftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerIpAddress.setStatus("current")
_DhcptftpServerIpAddress_Type = IpAddress
_DhcptftpServerIpAddress_Object = MibTableColumn
dhcptftpServerIpAddress = _DhcptftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 62),
    _DhcptftpServerIpAddress_Type()
)
dhcptftpServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcptftpServerIpAddress.setStatus("current")


class _TftpFileName_Type(DisplayString):
    """Custom type tftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_TftpFileName_Type.__name__ = "DisplayString"
_TftpFileName_Object = MibTableColumn
tftpFileName = _TftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 63),
    _TftpFileName_Type()
)
tftpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFileName.setStatus("current")
_ModeType_Type = OstModeType
_ModeType_Object = MibTableColumn
modeType = _ModeType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 64),
    _ModeType_Type()
)
modeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modeType.setStatus("current")
_DhcpPortNumber_Type = Integer32
_DhcpPortNumber_Object = MibTableColumn
dhcpPortNumber = _DhcpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 65),
    _DhcpPortNumber_Type()
)
dhcpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPortNumber.setStatus("current")
_DhcpTagVid_Type = OstVlanId
_DhcpTagVid_Object = MibTableColumn
dhcpTagVid = _DhcpTagVid_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 66),
    _DhcpTagVid_Type()
)
dhcpTagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpTagVid.setStatus("current")


class _TrapSrcIpSelect_Type(Unsigned32):
    """Custom type trapSrcIpSelect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TrapSrcIpSelect_Type.__name__ = "Unsigned32"
_TrapSrcIpSelect_Object = MibTableColumn
trapSrcIpSelect = _TrapSrcIpSelect_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 67),
    _TrapSrcIpSelect_Type()
)
trapSrcIpSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSrcIpSelect.setStatus("current")
_MuxGroupDefaults_Type = TruthValue
_MuxGroupDefaults_Object = MibTableColumn
muxGroupDefaults = _MuxGroupDefaults_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 68),
    _MuxGroupDefaults_Type()
)
muxGroupDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    muxGroupDefaults.setStatus("current")


class _PortFwdCpu_Type(Integer32):
    """Custom type portFwdCpu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("backplaneA", 3),
          ("backplaneB", 4),
          ("port1", 1),
          ("port2", 2))
    )


_PortFwdCpu_Type.__name__ = "Integer32"
_PortFwdCpu_Object = MibTableColumn
portFwdCpu = _PortFwdCpu_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 69),
    _PortFwdCpu_Type()
)
portFwdCpu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFwdCpu.setStatus("current")


class _PortFwdCpuList_Type(OstPortList):
    """Custom type portFwdCpuList based on OstPortList"""
    defaultValue = OctetString("all")


_PortFwdCpuList_Object = MibTableColumn
portFwdCpuList = _PortFwdCpuList_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 3, 1, 70),
    _PortFwdCpuList_Type()
)
portFwdCpuList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFwdCpuList.setStatus("current")
_ModulePortsTable_Object = MibTable
modulePortsTable = _ModulePortsTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4)
)
if mibBuilder.loadTexts:
    modulePortsTable.setStatus("current")
_ModulePortsEntry_Object = MibTableRow
modulePortsEntry = _ModulePortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1)
)
modulePortsEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "portnum"),
)
if mibBuilder.loadTexts:
    modulePortsEntry.setStatus("current")
_Portnum_Type = OstPortNumber
_Portnum_Object = MibTableColumn
portnum = _Portnum_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 1),
    _Portnum_Type()
)
portnum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portnum.setStatus("current")


class _PortState_Type(Integer32):
    """Custom type portState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("undefined", 0),
          ("unused", 3))
    )


_PortState_Type.__name__ = "Integer32"
_PortState_Object = MibTableColumn
portState = _PortState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 2),
    _PortState_Type()
)
portState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portState.setStatus("current")
_PortEgressRate_Type = Integer32
_PortEgressRate_Object = MibTableColumn
portEgressRate = _PortEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 3),
    _PortEgressRate_Type()
)
portEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgressRate.setStatus("current")


class _Portpriority_Type(Integer32):
    """Custom type portpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Portpriority_Type.__name__ = "Integer32"
_Portpriority_Object = MibTableColumn
portpriority = _Portpriority_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 4),
    _Portpriority_Type()
)
portpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portpriority.setStatus("current")


class _PortcanonicalformatIndicator_Type(Integer32):
    """Custom type portcanonicalformatIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortcanonicalformatIndicator_Type.__name__ = "Integer32"
_PortcanonicalformatIndicator_Object = MibTableColumn
portcanonicalformatIndicator = _PortcanonicalformatIndicator_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 5),
    _PortcanonicalformatIndicator_Type()
)
portcanonicalformatIndicator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portcanonicalformatIndicator.setStatus("current")


class _Portvlanidentifier_Type(Integer32):
    """Custom type portvlanidentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Portvlanidentifier_Type.__name__ = "Integer32"
_Portvlanidentifier_Object = MibTableColumn
portvlanidentifier = _Portvlanidentifier_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 6),
    _Portvlanidentifier_Type()
)
portvlanidentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portvlanidentifier.setStatus("current")


class _Portmlistcriteria_Type(Integer32):
    """Custom type portmlistcriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Portmlistcriteria_Type.__name__ = "Integer32"
_Portmlistcriteria_Object = MibTableColumn
portmlistcriteria = _Portmlistcriteria_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 7),
    _Portmlistcriteria_Type()
)
portmlistcriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portmlistcriteria.setStatus("current")


class _Portingresssecurity_Type(Integer32):
    """Custom type portingresssecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Portingresssecurity_Type.__name__ = "Integer32"
_Portingresssecurity_Object = MibTableColumn
portingresssecurity = _Portingresssecurity_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 8),
    _Portingresssecurity_Type()
)
portingresssecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portingresssecurity.setStatus("current")


class _Portegresspolicy_Type(Integer32):
    """Custom type portegresspolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Portegresspolicy_Type.__name__ = "Integer32"
_Portegresspolicy_Object = MibTableColumn
portegresspolicy = _Portegresspolicy_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 9),
    _Portegresspolicy_Type()
)
portegresspolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portegresspolicy.setStatus("current")
_PortIngressRate_Type = Integer32
_PortIngressRate_Object = MibTableColumn
portIngressRate = _PortIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 10),
    _PortIngressRate_Type()
)
portIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIngressRate.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 11),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortUnidirectionalAhOamEnable_Type(Integer32):
    """Custom type portUnidirectionalAhOamEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortUnidirectionalAhOamEnable_Type.__name__ = "Integer32"
_PortUnidirectionalAhOamEnable_Object = MibTableColumn
portUnidirectionalAhOamEnable = _PortUnidirectionalAhOamEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 12),
    _PortUnidirectionalAhOamEnable_Type()
)
portUnidirectionalAhOamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portUnidirectionalAhOamEnable.setStatus("current")


class _PortIngressRateDropOrPause_Type(Integer32):
    """Custom type portIngressRateDropOrPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PortIngressRateDropOrPause_Type.__name__ = "Integer32"
_PortIngressRateDropOrPause_Object = MibTableColumn
portIngressRateDropOrPause = _PortIngressRateDropOrPause_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 13),
    _PortIngressRateDropOrPause_Type()
)
portIngressRateDropOrPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIngressRateDropOrPause.setStatus("current")


class _PortIngressRateCBS_Type(Integer32):
    """Custom type portIngressRateCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 256000),
    )


_PortIngressRateCBS_Type.__name__ = "Integer32"
_PortIngressRateCBS_Object = MibTableColumn
portIngressRateCBS = _PortIngressRateCBS_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 14),
    _PortIngressRateCBS_Type()
)
portIngressRateCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIngressRateCBS.setStatus("current")


class _PortL2CPmgntProcessing_Type(Integer32):
    """Custom type portL2CPmgntProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PortL2CPmgntProcessing_Type.__name__ = "Integer32"
_PortL2CPmgntProcessing_Object = MibTableColumn
portL2CPmgntProcessing = _PortL2CPmgntProcessing_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 15),
    _PortL2CPmgntProcessing_Type()
)
portL2CPmgntProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portL2CPmgntProcessing.setStatus("current")


class _PortEgressQosPolicy_Type(Integer32):
    """Custom type portEgressQosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PortEgressQosPolicy_Type.__name__ = "Integer32"
_PortEgressQosPolicy_Object = MibTableColumn
portEgressQosPolicy = _PortEgressQosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 16),
    _PortEgressQosPolicy_Type()
)
portEgressQosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEgressQosPolicy.setStatus("current")


class _PortAccessType_Type(Integer32):
    """Custom type portAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_PortAccessType_Type.__name__ = "Integer32"
_PortAccessType_Object = MibTableColumn
portAccessType = _PortAccessType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 17),
    _PortAccessType_Type()
)
portAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAccessType.setStatus("current")


class _PortStatsClear_Type(Integer32):
    """Custom type portStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortStatsClear_Type.__name__ = "Integer32"
_PortStatsClear_Object = MibTableColumn
portStatsClear = _PortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 18),
    _PortStatsClear_Type()
)
portStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portStatsClear.setStatus("current")


class _PortLinkState_Type(Integer32):
    """Custom type portLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_PortLinkState_Type.__name__ = "Integer32"
_PortLinkState_Object = MibTableColumn
portLinkState = _PortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 19),
    _PortLinkState_Type()
)
portLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkState.setStatus("current")


class _PortDuplex_Type(Integer32):
    """Custom type portDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 2),
          ("halfDuplex", 1),
          ("undefined", 0))
    )


_PortDuplex_Type.__name__ = "Integer32"
_PortDuplex_Object = MibTableColumn
portDuplex = _PortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 20),
    _PortDuplex_Type()
)
portDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDuplex.setStatus("current")


class _PortMacAddress_Type(DisplayString):
    """Custom type portMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_PortMacAddress_Type.__name__ = "DisplayString"
_PortMacAddress_Object = MibTableColumn
portMacAddress = _PortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 4, 1, 21),
    _PortMacAddress_Type()
)
portMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacAddress.setStatus("current")
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("current")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1)
)
portStatsEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "portnum"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("current")
_TxOctets_Type = Counter32
_TxOctets_Object = MibTableColumn
txOctets = _TxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 1),
    _TxOctets_Type()
)
txOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctets.setStatus("current")
_TxDropPkts_Type = Counter32
_TxDropPkts_Object = MibTableColumn
txDropPkts = _TxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 2),
    _TxDropPkts_Type()
)
txDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDropPkts.setStatus("current")
_TxBroadcastPkts_Type = Counter32
_TxBroadcastPkts_Object = MibTableColumn
txBroadcastPkts = _TxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 3),
    _TxBroadcastPkts_Type()
)
txBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBroadcastPkts.setStatus("current")
_TxMulticastPkts_Type = Counter32
_TxMulticastPkts_Object = MibTableColumn
txMulticastPkts = _TxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 4),
    _TxMulticastPkts_Type()
)
txMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMulticastPkts.setStatus("current")
_TxUnicastPkts_Type = Counter32
_TxUnicastPkts_Object = MibTableColumn
txUnicastPkts = _TxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 5),
    _TxUnicastPkts_Type()
)
txUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txUnicastPkts.setStatus("current")
_TxGoodPkts_Type = Counter32
_TxGoodPkts_Object = MibTableColumn
txGoodPkts = _TxGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 6),
    _TxGoodPkts_Type()
)
txGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txGoodPkts.setStatus("current")
_TxErrorPkts_Type = Counter32
_TxErrorPkts_Object = MibTableColumn
txErrorPkts = _TxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 7),
    _TxErrorPkts_Type()
)
txErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txErrorPkts.setStatus("current")
_TxPausePkts_Type = Counter32
_TxPausePkts_Object = MibTableColumn
txPausePkts = _TxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 8),
    _TxPausePkts_Type()
)
txPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPausePkts.setStatus("current")
_TxCollisions_Type = Counter32
_TxCollisions_Object = MibTableColumn
txCollisions = _TxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 9),
    _TxCollisions_Type()
)
txCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txCollisions.setStatus("current")
_TxSingleCollision_Type = Counter32
_TxSingleCollision_Object = MibTableColumn
txSingleCollision = _TxSingleCollision_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 10),
    _TxSingleCollision_Type()
)
txSingleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txSingleCollision.setStatus("current")
_TxMultipleCollision_Type = Counter32
_TxMultipleCollision_Object = MibTableColumn
txMultipleCollision = _TxMultipleCollision_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 11),
    _TxMultipleCollision_Type()
)
txMultipleCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txMultipleCollision.setStatus("current")
_TxDeferedTransmit_Type = Counter32
_TxDeferedTransmit_Object = MibTableColumn
txDeferedTransmit = _TxDeferedTransmit_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 12),
    _TxDeferedTransmit_Type()
)
txDeferedTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDeferedTransmit.setStatus("current")
_TxLateCollision_Type = Counter32
_TxLateCollision_Object = MibTableColumn
txLateCollision = _TxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 13),
    _TxLateCollision_Type()
)
txLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txLateCollision.setStatus("current")
_TxExcessiveCollision_Type = Counter32
_TxExcessiveCollision_Object = MibTableColumn
txExcessiveCollision = _TxExcessiveCollision_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 14),
    _TxExcessiveCollision_Type()
)
txExcessiveCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txExcessiveCollision.setStatus("current")
_TxDroppedEvents_Type = Counter32
_TxDroppedEvents_Object = MibTableColumn
txDroppedEvents = _TxDroppedEvents_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 15),
    _TxDroppedEvents_Type()
)
txDroppedEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDroppedEvents.setStatus("current")
_RxOctets_Type = Counter32
_RxOctets_Object = MibTableColumn
rxOctets = _RxOctets_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 16),
    _RxOctets_Type()
)
rxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctets.setStatus("current")
_RxDropPkts_Type = Counter32
_RxDropPkts_Object = MibTableColumn
rxDropPkts = _RxDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 17),
    _RxDropPkts_Type()
)
rxDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDropPkts.setStatus("current")
_RxBroadcastPkts_Type = Counter32
_RxBroadcastPkts_Object = MibTableColumn
rxBroadcastPkts = _RxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 18),
    _RxBroadcastPkts_Type()
)
rxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBroadcastPkts.setStatus("current")
_RxMulticastPkts_Type = Counter32
_RxMulticastPkts_Object = MibTableColumn
rxMulticastPkts = _RxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 19),
    _RxMulticastPkts_Type()
)
rxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxMulticastPkts.setStatus("current")
_RxUnicastPkts_Type = Counter32
_RxUnicastPkts_Object = MibTableColumn
rxUnicastPkts = _RxUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 20),
    _RxUnicastPkts_Type()
)
rxUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUnicastPkts.setStatus("current")
_RxGoodPkts_Type = Counter32
_RxGoodPkts_Object = MibTableColumn
rxGoodPkts = _RxGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 21),
    _RxGoodPkts_Type()
)
rxGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxGoodPkts.setStatus("current")
_RxTotalPkts_Type = Counter32
_RxTotalPkts_Object = MibTableColumn
rxTotalPkts = _RxTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 22),
    _RxTotalPkts_Type()
)
rxTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxTotalPkts.setStatus("current")
_RxErrorPkts_Type = Counter32
_RxErrorPkts_Object = MibTableColumn
rxErrorPkts = _RxErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 23),
    _RxErrorPkts_Type()
)
rxErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxErrorPkts.setStatus("current")
_RxPausePkts_Type = Counter32
_RxPausePkts_Object = MibTableColumn
rxPausePkts = _RxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 24),
    _RxPausePkts_Type()
)
rxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPausePkts.setStatus("current")
_RxUndersizePkts_Type = Counter32
_RxUndersizePkts_Object = MibTableColumn
rxUndersizePkts = _RxUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 25),
    _RxUndersizePkts_Type()
)
rxUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxUndersizePkts.setStatus("current")
_RxOversizePkts_Type = Counter32
_RxOversizePkts_Object = MibTableColumn
rxOversizePkts = _RxOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 26),
    _RxOversizePkts_Type()
)
rxOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOversizePkts.setStatus("current")
_RxFragments_Type = Counter32
_RxFragments_Object = MibTableColumn
rxFragments = _RxFragments_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 27),
    _RxFragments_Type()
)
rxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFragments.setStatus("current")
_RxJabbers_Type = Counter32
_RxJabbers_Object = MibTableColumn
rxJabbers = _RxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 28),
    _RxJabbers_Type()
)
rxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxJabbers.setStatus("current")
_RxAlignmentErrors_Type = Counter32
_RxAlignmentErrors_Object = MibTableColumn
rxAlignmentErrors = _RxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 29),
    _RxAlignmentErrors_Type()
)
rxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxAlignmentErrors.setStatus("current")
_RxFCSErrors_Type = Counter32
_RxFCSErrors_Object = MibTableColumn
rxFCSErrors = _RxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 30),
    _RxFCSErrors_Type()
)
rxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFCSErrors.setStatus("current")
_RxSymbolErrors_Type = Counter32
_RxSymbolErrors_Object = MibTableColumn
rxSymbolErrors = _RxSymbolErrors_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 31),
    _RxSymbolErrors_Type()
)
rxSymbolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxSymbolErrors.setStatus("current")
_RxCRCAlignErrors_Type = Counter32
_RxCRCAlignErrors_Object = MibTableColumn
rxCRCAlignErrors = _RxCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 32),
    _RxCRCAlignErrors_Type()
)
rxCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxCRCAlignErrors.setStatus("current")
_RxPackets64_Type = Counter32
_RxPackets64_Object = MibTableColumn
rxPackets64 = _RxPackets64_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 33),
    _RxPackets64_Type()
)
rxPackets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets64.setStatus("current")
_RxPackets65to127_Type = Counter32
_RxPackets65to127_Object = MibTableColumn
rxPackets65to127 = _RxPackets65to127_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 34),
    _RxPackets65to127_Type()
)
rxPackets65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets65to127.setStatus("current")
_RxPackets128to255_Type = Counter32
_RxPackets128to255_Object = MibTableColumn
rxPackets128to255 = _RxPackets128to255_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 35),
    _RxPackets128to255_Type()
)
rxPackets128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets128to255.setStatus("current")
_RxPackets256to511_Type = Counter32
_RxPackets256to511_Object = MibTableColumn
rxPackets256to511 = _RxPackets256to511_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 36),
    _RxPackets256to511_Type()
)
rxPackets256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets256to511.setStatus("current")
_RxPackets512to1023_Type = Counter32
_RxPackets512to1023_Object = MibTableColumn
rxPackets512to1023 = _RxPackets512to1023_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 37),
    _RxPackets512to1023_Type()
)
rxPackets512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets512to1023.setStatus("current")
_RxPackets1024to1518_Type = Counter32
_RxPackets1024to1518_Object = MibTableColumn
rxPackets1024to1518 = _RxPackets1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 38),
    _RxPackets1024to1518_Type()
)
rxPackets1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPackets1024to1518.setStatus("current")
_TxOctets64_Type = Counter64
_TxOctets64_Object = MibTableColumn
txOctets64 = _TxOctets64_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 39),
    _TxOctets64_Type()
)
txOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txOctets64.setStatus("current")
_RxOctets64_Type = Counter64
_RxOctets64_Object = MibTableColumn
rxOctets64 = _RxOctets64_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 5, 1, 40),
    _RxOctets64_Type()
)
rxOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxOctets64.setStatus("current")
_ModuleVLANTable_Object = MibTable
moduleVLANTable = _ModuleVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6)
)
if mibBuilder.loadTexts:
    moduleVLANTable.setStatus("current")
_ModuleVLANEntry_Object = MibTableRow
moduleVLANEntry = _ModuleVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1)
)
moduleVLANEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "index"),
)
if mibBuilder.loadTexts:
    moduleVLANEntry.setStatus("current")


class _Index_Type(Integer32):
    """Custom type index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Index_Type.__name__ = "Integer32"
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 1),
    _Index_Type()
)
index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    index.setStatus("current")


class _Validityflag_Type(Integer32):
    """Custom type validityflag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Validityflag_Type.__name__ = "Integer32"
_Validityflag_Object = MibTableColumn
validityflag = _Validityflag_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 2),
    _Validityflag_Type()
)
validityflag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validityflag.setStatus("current")


class _Vlanidentifier_Type(Integer32):
    """Custom type vlanidentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Vlanidentifier_Type.__name__ = "Integer32"
_Vlanidentifier_Object = MibTableColumn
vlanidentifier = _Vlanidentifier_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 3),
    _Vlanidentifier_Type()
)
vlanidentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanidentifier.setStatus("current")


class _Port1Membership_Type(Integer32):
    """Custom type port1Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port1Membership_Type.__name__ = "Integer32"
_Port1Membership_Object = MibTableColumn
port1Membership = _Port1Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 4),
    _Port1Membership_Type()
)
port1Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1Membership.setStatus("current")


class _Port2Membership_Type(Integer32):
    """Custom type port2Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port2Membership_Type.__name__ = "Integer32"
_Port2Membership_Object = MibTableColumn
port2Membership = _Port2Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 5),
    _Port2Membership_Type()
)
port2Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2Membership.setStatus("current")


class _Port3Membership_Type(Integer32):
    """Custom type port3Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port3Membership_Type.__name__ = "Integer32"
_Port3Membership_Object = MibTableColumn
port3Membership = _Port3Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 6),
    _Port3Membership_Type()
)
port3Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3Membership.setStatus("current")


class _Port4Membership_Type(Integer32):
    """Custom type port4Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port4Membership_Type.__name__ = "Integer32"
_Port4Membership_Object = MibTableColumn
port4Membership = _Port4Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 7),
    _Port4Membership_Type()
)
port4Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4Membership.setStatus("current")


class _Port5Membership_Type(Integer32):
    """Custom type port5Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port5Membership_Type.__name__ = "Integer32"
_Port5Membership_Object = MibTableColumn
port5Membership = _Port5Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 8),
    _Port5Membership_Type()
)
port5Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5Membership.setStatus("current")


class _Port6Membership_Type(Integer32):
    """Custom type port6Membership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Port6Membership_Type.__name__ = "Integer32"
_Port6Membership_Object = MibTableColumn
port6Membership = _Port6Membership_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 6, 1, 9),
    _Port6Membership_Type()
)
port6Membership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6Membership.setStatus("current")
_PortAHTable_Object = MibTable
portAHTable = _PortAHTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7)
)
if mibBuilder.loadTexts:
    portAHTable.setStatus("current")
_PortAHEntry_Object = MibTableRow
portAHEntry = _PortAHEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1)
)
portAHEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "portnum"),
)
if mibBuilder.loadTexts:
    portAHEntry.setStatus("current")


class _AhEnabled_Type(Integer32):
    """Custom type ahEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AhEnabled_Type.__name__ = "Integer32"
_AhEnabled_Object = MibTableColumn
ahEnabled = _AhEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 1),
    _AhEnabled_Type()
)
ahEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahEnabled.setStatus("current")


class _AhLpbkMode_Type(Integer32):
    """Custom type ahLpbkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AhLpbkMode_Type.__name__ = "Integer32"
_AhLpbkMode_Object = MibTableColumn
ahLpbkMode = _AhLpbkMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 2),
    _AhLpbkMode_Type()
)
ahLpbkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahLpbkMode.setStatus("current")


class _AhLocalMode_Type(Integer32):
    """Custom type ahLocalMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AhLocalMode_Type.__name__ = "Integer32"
_AhLocalMode_Object = MibTableColumn
ahLocalMode = _AhLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 3),
    _AhLocalMode_Type()
)
ahLocalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahLocalMode.setStatus("current")


class _AhRemoteMode_Type(Integer32):
    """Custom type ahRemoteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AhRemoteMode_Type.__name__ = "Integer32"
_AhRemoteMode_Object = MibTableColumn
ahRemoteMode = _AhRemoteMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 4),
    _AhRemoteMode_Type()
)
ahRemoteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteMode.setStatus("current")


class _AhLocalMuxState_Type(Integer32):
    """Custom type ahLocalMuxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AhLocalMuxState_Type.__name__ = "Integer32"
_AhLocalMuxState_Object = MibTableColumn
ahLocalMuxState = _AhLocalMuxState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 5),
    _AhLocalMuxState_Type()
)
ahLocalMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLocalMuxState.setStatus("current")


class _AhRemoteMuxState_Type(Integer32):
    """Custom type ahRemoteMuxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AhRemoteMuxState_Type.__name__ = "Integer32"
_AhRemoteMuxState_Object = MibTableColumn
ahRemoteMuxState = _AhRemoteMuxState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 6),
    _AhRemoteMuxState_Type()
)
ahRemoteMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteMuxState.setStatus("current")


class _AhLocalParserState_Type(Integer32):
    """Custom type ahLocalParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AhLocalParserState_Type.__name__ = "Integer32"
_AhLocalParserState_Object = MibTableColumn
ahLocalParserState = _AhLocalParserState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 7),
    _AhLocalParserState_Type()
)
ahLocalParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLocalParserState.setStatus("current")


class _AhRemoteParserState_Type(Integer32):
    """Custom type ahRemoteParserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AhRemoteParserState_Type.__name__ = "Integer32"
_AhRemoteParserState_Object = MibTableColumn
ahRemoteParserState = _AhRemoteParserState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 8),
    _AhRemoteParserState_Type()
)
ahRemoteParserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteParserState.setStatus("current")


class _AhLocalSupportVar_Type(Integer32):
    """Custom type ahLocalSupportVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AhLocalSupportVar_Type.__name__ = "Integer32"
_AhLocalSupportVar_Object = MibTableColumn
ahLocalSupportVar = _AhLocalSupportVar_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 9),
    _AhLocalSupportVar_Type()
)
ahLocalSupportVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLocalSupportVar.setStatus("current")


class _AhLocalLinkFlags_Type(Integer32):
    """Custom type ahLocalLinkFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AhLocalLinkFlags_Type.__name__ = "Integer32"
_AhLocalLinkFlags_Object = MibTableColumn
ahLocalLinkFlags = _AhLocalLinkFlags_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 10),
    _AhLocalLinkFlags_Type()
)
ahLocalLinkFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLocalLinkFlags.setStatus("current")


class _AhLocalLpbkTimeout_Type(Integer32):
    """Custom type ahLocalLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AhLocalLpbkTimeout_Type.__name__ = "Integer32"
_AhLocalLpbkTimeout_Object = MibTableColumn
ahLocalLpbkTimeout = _AhLocalLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 11),
    _AhLocalLpbkTimeout_Type()
)
ahLocalLpbkTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahLocalLpbkTimeout.setStatus("current")


class _AhRemoteSupportVar_Type(Integer32):
    """Custom type ahRemoteSupportVar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AhRemoteSupportVar_Type.__name__ = "Integer32"
_AhRemoteSupportVar_Object = MibTableColumn
ahRemoteSupportVar = _AhRemoteSupportVar_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 12),
    _AhRemoteSupportVar_Type()
)
ahRemoteSupportVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteSupportVar.setStatus("current")


class _AhRemoteLinkFlags_Type(Integer32):
    """Custom type ahRemoteLinkFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AhRemoteLinkFlags_Type.__name__ = "Integer32"
_AhRemoteLinkFlags_Object = MibTableColumn
ahRemoteLinkFlags = _AhRemoteLinkFlags_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 13),
    _AhRemoteLinkFlags_Type()
)
ahRemoteLinkFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteLinkFlags.setStatus("current")


class _AhRemoteLpbkTimeout_Type(Integer32):
    """Custom type ahRemoteLpbkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AhRemoteLpbkTimeout_Type.__name__ = "Integer32"
_AhRemoteLpbkTimeout_Object = MibTableColumn
ahRemoteLpbkTimeout = _AhRemoteLpbkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 14),
    _AhRemoteLpbkTimeout_Type()
)
ahRemoteLpbkTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteLpbkTimeout.setStatus("current")


class _AhLocalOUI_Type(OctetString):
    """Custom type ahLocalOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AhLocalOUI_Type.__name__ = "OctetString"
_AhLocalOUI_Object = MibTableColumn
ahLocalOUI = _AhLocalOUI_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 15),
    _AhLocalOUI_Type()
)
ahLocalOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahLocalOUI.setStatus("current")


class _AhRemoteOUI_Type(OctetString):
    """Custom type ahRemoteOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_AhRemoteOUI_Type.__name__ = "OctetString"
_AhRemoteOUI_Object = MibTableColumn
ahRemoteOUI = _AhRemoteOUI_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 16),
    _AhRemoteOUI_Type()
)
ahRemoteOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteOUI.setStatus("current")


class _AhErroredSymbolPeriodWindow_Type(Unsigned32):
    """Custom type ahErroredSymbolPeriodWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AhErroredSymbolPeriodWindow_Type.__name__ = "Unsigned32"
_AhErroredSymbolPeriodWindow_Object = MibTableColumn
ahErroredSymbolPeriodWindow = _AhErroredSymbolPeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 17),
    _AhErroredSymbolPeriodWindow_Type()
)
ahErroredSymbolPeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredSymbolPeriodWindow.setStatus("current")
_AhErroredSymbolPeriodThreshold_Type = Unsigned32
_AhErroredSymbolPeriodThreshold_Object = MibTableColumn
ahErroredSymbolPeriodThreshold = _AhErroredSymbolPeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 18),
    _AhErroredSymbolPeriodThreshold_Type()
)
ahErroredSymbolPeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredSymbolPeriodThreshold.setStatus("current")


class _AhErroredFrameWindow_Type(Unsigned32):
    """Custom type ahErroredFrameWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AhErroredFrameWindow_Type.__name__ = "Unsigned32"
_AhErroredFrameWindow_Object = MibTableColumn
ahErroredFrameWindow = _AhErroredFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 19),
    _AhErroredFrameWindow_Type()
)
ahErroredFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFrameWindow.setStatus("current")


class _AhErroredFrameThreshold_Type(Unsigned32):
    """Custom type ahErroredFrameThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AhErroredFrameThreshold_Type.__name__ = "Unsigned32"
_AhErroredFrameThreshold_Object = MibTableColumn
ahErroredFrameThreshold = _AhErroredFrameThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 20),
    _AhErroredFrameThreshold_Type()
)
ahErroredFrameThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFrameThreshold.setStatus("current")


class _AhErroredFramePeriodWindow_Type(Unsigned32):
    """Custom type ahErroredFramePeriodWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AhErroredFramePeriodWindow_Type.__name__ = "Unsigned32"
_AhErroredFramePeriodWindow_Object = MibTableColumn
ahErroredFramePeriodWindow = _AhErroredFramePeriodWindow_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 21),
    _AhErroredFramePeriodWindow_Type()
)
ahErroredFramePeriodWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFramePeriodWindow.setStatus("current")


class _AhErroredFramePeriodThreshold_Type(Unsigned32):
    """Custom type ahErroredFramePeriodThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AhErroredFramePeriodThreshold_Type.__name__ = "Unsigned32"
_AhErroredFramePeriodThreshold_Object = MibTableColumn
ahErroredFramePeriodThreshold = _AhErroredFramePeriodThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 22),
    _AhErroredFramePeriodThreshold_Type()
)
ahErroredFramePeriodThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFramePeriodThreshold.setStatus("current")


class _AhErroredFrameSecondsWindow_Type(Unsigned32):
    """Custom type ahErroredFrameSecondsWindow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_AhErroredFrameSecondsWindow_Type.__name__ = "Unsigned32"
_AhErroredFrameSecondsWindow_Object = MibTableColumn
ahErroredFrameSecondsWindow = _AhErroredFrameSecondsWindow_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 23),
    _AhErroredFrameSecondsWindow_Type()
)
ahErroredFrameSecondsWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFrameSecondsWindow.setStatus("current")


class _AhErroredFrameSecondsThreshold_Type(Unsigned32):
    """Custom type ahErroredFrameSecondsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AhErroredFrameSecondsThreshold_Type.__name__ = "Unsigned32"
_AhErroredFrameSecondsThreshold_Object = MibTableColumn
ahErroredFrameSecondsThreshold = _AhErroredFrameSecondsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 24),
    _AhErroredFrameSecondsThreshold_Type()
)
ahErroredFrameSecondsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahErroredFrameSecondsThreshold.setStatus("current")


class _AhRemoteLinkPort_Type(Integer32):
    """Custom type ahRemoteLinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AhRemoteLinkPort_Type.__name__ = "Integer32"
_AhRemoteLinkPort_Object = MibTableColumn
ahRemoteLinkPort = _AhRemoteLinkPort_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 25),
    _AhRemoteLinkPort_Type()
)
ahRemoteLinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahRemoteLinkPort.setStatus("current")
_AhSymbolErrorRunningTotal_Type = Unsigned32
_AhSymbolErrorRunningTotal_Object = MibTableColumn
ahSymbolErrorRunningTotal = _AhSymbolErrorRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 26),
    _AhSymbolErrorRunningTotal_Type()
)
ahSymbolErrorRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSymbolErrorRunningTotal.setStatus("current")
_AhSymbolErrorEventTotal_Type = Unsigned32
_AhSymbolErrorEventTotal_Object = MibTableColumn
ahSymbolErrorEventTotal = _AhSymbolErrorEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 27),
    _AhSymbolErrorEventTotal_Type()
)
ahSymbolErrorEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahSymbolErrorEventTotal.setStatus("current")
_AhFrameErrorRunningTotal_Type = Unsigned32
_AhFrameErrorRunningTotal_Object = MibTableColumn
ahFrameErrorRunningTotal = _AhFrameErrorRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 28),
    _AhFrameErrorRunningTotal_Type()
)
ahFrameErrorRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFrameErrorRunningTotal.setStatus("current")
_AhFrameErrorEventTotal_Type = Unsigned32
_AhFrameErrorEventTotal_Object = MibTableColumn
ahFrameErrorEventTotal = _AhFrameErrorEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 29),
    _AhFrameErrorEventTotal_Type()
)
ahFrameErrorEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFrameErrorEventTotal.setStatus("current")
_AhFramePeriodRunningTotal_Type = Unsigned32
_AhFramePeriodRunningTotal_Object = MibTableColumn
ahFramePeriodRunningTotal = _AhFramePeriodRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 30),
    _AhFramePeriodRunningTotal_Type()
)
ahFramePeriodRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFramePeriodRunningTotal.setStatus("current")
_AhFramePeriodEventTotal_Type = Unsigned32
_AhFramePeriodEventTotal_Object = MibTableColumn
ahFramePeriodEventTotal = _AhFramePeriodEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 31),
    _AhFramePeriodEventTotal_Type()
)
ahFramePeriodEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFramePeriodEventTotal.setStatus("current")
_AhFrameSecondsSummaryRunningTotal_Type = Unsigned32
_AhFrameSecondsSummaryRunningTotal_Object = MibTableColumn
ahFrameSecondsSummaryRunningTotal = _AhFrameSecondsSummaryRunningTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 32),
    _AhFrameSecondsSummaryRunningTotal_Type()
)
ahFrameSecondsSummaryRunningTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFrameSecondsSummaryRunningTotal.setStatus("current")
_AhFrameSecondsSummaryEventTotal_Type = Unsigned32
_AhFrameSecondsSummaryEventTotal_Object = MibTableColumn
ahFrameSecondsSummaryEventTotal = _AhFrameSecondsSummaryEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 33),
    _AhFrameSecondsSummaryEventTotal_Type()
)
ahFrameSecondsSummaryEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ahFrameSecondsSummaryEventTotal.setStatus("current")
_AhClearStatistics_Type = TruthValue
_AhClearStatistics_Object = MibTableColumn
ahClearStatistics = _AhClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 34),
    _AhClearStatistics_Type()
)
ahClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahClearStatistics.setStatus("current")


class _AhTransmissionRate_Type(Unsigned32):
    """Custom type ahTransmissionRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_AhTransmissionRate_Type.__name__ = "Unsigned32"
_AhTransmissionRate_Object = MibTableColumn
ahTransmissionRate = _AhTransmissionRate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 35),
    _AhTransmissionRate_Type()
)
ahTransmissionRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahTransmissionRate.setStatus("current")
if mibBuilder.loadTexts:
    ahTransmissionRate.setUnits("Frames/sec")


class _AhCriticalEventMode_Type(Unsigned32):
    """Custom type ahCriticalEventMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AhCriticalEventMode_Type.__name__ = "Unsigned32"
_AhCriticalEventMode_Object = MibTableColumn
ahCriticalEventMode = _AhCriticalEventMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 36),
    _AhCriticalEventMode_Type()
)
ahCriticalEventMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahCriticalEventMode.setStatus("current")


class _AhCriticalEventTrapList_Type(OctetString):
    """Custom type ahCriticalEventTrapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AhCriticalEventTrapList_Type.__name__ = "OctetString"
_AhCriticalEventTrapList_Object = MibTableColumn
ahCriticalEventTrapList = _AhCriticalEventTrapList_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 7, 1, 37),
    _AhCriticalEventTrapList_Type()
)
ahCriticalEventTrapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ahCriticalEventTrapList.setStatus("current")
_PortSFPTable_Object = MibTable
portSFPTable = _PortSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8)
)
if mibBuilder.loadTexts:
    portSFPTable.setStatus("current")
_PortSFPEntry_Object = MibTableRow
portSFPEntry = _PortSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1)
)
portSFPEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "portnum"),
)
if mibBuilder.loadTexts:
    portSFPEntry.setStatus("current")


class _PortSFPstatus_Type(Integer32):
    """Custom type portSFPstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_PortSFPstatus_Type.__name__ = "Integer32"
_PortSFPstatus_Object = MibTableColumn
portSFPstatus = _PortSFPstatus_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 1),
    _PortSFPstatus_Type()
)
portSFPstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSFPstatus.setStatus("current")


class _PortSFPpageA0_Type(OctetString):
    """Custom type portSFPpageA0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_PortSFPpageA0_Type.__name__ = "OctetString"
_PortSFPpageA0_Object = MibTableColumn
portSFPpageA0 = _PortSFPpageA0_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 2),
    _PortSFPpageA0_Type()
)
portSFPpageA0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSFPpageA0.setStatus("current")


class _PortSFPpageA2_Type(OctetString):
    """Custom type portSFPpageA2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_PortSFPpageA2_Type.__name__ = "OctetString"
_PortSFPpageA2_Object = MibTableColumn
portSFPpageA2 = _PortSFPpageA2_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 3),
    _PortSFPpageA2_Type()
)
portSFPpageA2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSFPpageA2.setStatus("current")


class _PortSfpBitRate_Type(OctetString):
    """Custom type portSfpBitRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpBitRate_Type.__name__ = "OctetString"
_PortSfpBitRate_Object = MibTableColumn
portSfpBitRate = _PortSfpBitRate_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 4),
    _PortSfpBitRate_Type()
)
portSfpBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpBitRate.setStatus("current")


class _PortSfpVendorName_Type(OctetString):
    """Custom type portSfpVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortSfpVendorName_Type.__name__ = "OctetString"
_PortSfpVendorName_Object = MibTableColumn
portSfpVendorName = _PortSfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 5),
    _PortSfpVendorName_Type()
)
portSfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVendorName.setStatus("current")


class _PortSfpVendorPartNumber_Type(OctetString):
    """Custom type portSfpVendorPartNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortSfpVendorPartNumber_Type.__name__ = "OctetString"
_PortSfpVendorPartNumber_Object = MibTableColumn
portSfpVendorPartNumber = _PortSfpVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 6),
    _PortSfpVendorPartNumber_Type()
)
portSfpVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVendorPartNumber.setStatus("current")


class _PortSfpVendorSerialNumber_Type(OctetString):
    """Custom type portSfpVendorSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortSfpVendorSerialNumber_Type.__name__ = "OctetString"
_PortSfpVendorSerialNumber_Object = MibTableColumn
portSfpVendorSerialNumber = _PortSfpVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 7),
    _PortSfpVendorSerialNumber_Type()
)
portSfpVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVendorSerialNumber.setStatus("current")


class _PortSfpDateCode_Type(OctetString):
    """Custom type portSfpDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortSfpDateCode_Type.__name__ = "OctetString"
_PortSfpDateCode_Object = MibTableColumn
portSfpDateCode = _PortSfpDateCode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 8),
    _PortSfpDateCode_Type()
)
portSfpDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpDateCode.setStatus("current")


class _PortSfpTemperature_Type(OctetString):
    """Custom type portSfpTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpTemperature_Type.__name__ = "OctetString"
_PortSfpTemperature_Object = MibTableColumn
portSfpTemperature = _PortSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 9),
    _PortSfpTemperature_Type()
)
portSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpTemperature.setStatus("current")


class _PortSfpVcc_Type(OctetString):
    """Custom type portSfpVcc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpVcc_Type.__name__ = "OctetString"
_PortSfpVcc_Object = MibTableColumn
portSfpVcc = _PortSfpVcc_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 10),
    _PortSfpVcc_Type()
)
portSfpVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpVcc.setStatus("current")


class _PortSfpBiasCurrent_Type(OctetString):
    """Custom type portSfpBiasCurrent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpBiasCurrent_Type.__name__ = "OctetString"
_PortSfpBiasCurrent_Object = MibTableColumn
portSfpBiasCurrent = _PortSfpBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 11),
    _PortSfpBiasCurrent_Type()
)
portSfpBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpBiasCurrent.setStatus("current")


class _PortSfpTxPower_Type(OctetString):
    """Custom type portSfpTxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpTxPower_Type.__name__ = "OctetString"
_PortSfpTxPower_Object = MibTableColumn
portSfpTxPower = _PortSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 12),
    _PortSfpTxPower_Type()
)
portSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpTxPower.setStatus("current")


class _PortSfpRxPower_Type(OctetString):
    """Custom type portSfpRxPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortSfpRxPower_Type.__name__ = "OctetString"
_PortSfpRxPower_Object = MibTableColumn
portSfpRxPower = _PortSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 8, 1, 13),
    _PortSfpRxPower_Type()
)
portSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSfpRxPower.setStatus("current")
_UserTable_Object = MibTable
userTable = _UserTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9)
)
if mibBuilder.loadTexts:
    userTable.setStatus("current")
_UserEntry_Object = MibTableRow
userEntry = _UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1)
)
userEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "userIndex"),
)
if mibBuilder.loadTexts:
    userEntry.setStatus("current")


class _UserIndex_Type(Integer32):
    """Custom type userIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UserIndex_Type.__name__ = "Integer32"
_UserIndex_Object = MibTableColumn
userIndex = _UserIndex_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 1),
    _UserIndex_Type()
)
userIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    userIndex.setStatus("current")


class _Snmpv3UserName_Type(DisplayString):
    """Custom type snmpv3UserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Snmpv3UserName_Type.__name__ = "DisplayString"
_Snmpv3UserName_Object = MibTableColumn
snmpv3UserName = _Snmpv3UserName_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 2),
    _Snmpv3UserName_Type()
)
snmpv3UserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserName.setStatus("current")


class _Snmpv3SecurityLevel_Type(Integer32):
    """Custom type snmpv3SecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Snmpv3SecurityLevel_Type.__name__ = "Integer32"
_Snmpv3SecurityLevel_Object = MibTableColumn
snmpv3SecurityLevel = _Snmpv3SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 3),
    _Snmpv3SecurityLevel_Type()
)
snmpv3SecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3SecurityLevel.setStatus("current")


class _Snmpv3AuthPassword_Type(OctetString):
    """Custom type snmpv3AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Snmpv3AuthPassword_Type.__name__ = "OctetString"
_Snmpv3AuthPassword_Object = MibTableColumn
snmpv3AuthPassword = _Snmpv3AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 4),
    _Snmpv3AuthPassword_Type()
)
snmpv3AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3AuthPassword.setStatus("current")


class _Snmpv3PrivPassword_Type(OctetString):
    """Custom type snmpv3PrivPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Snmpv3PrivPassword_Type.__name__ = "OctetString"
_Snmpv3PrivPassword_Object = MibTableColumn
snmpv3PrivPassword = _Snmpv3PrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 5),
    _Snmpv3PrivPassword_Type()
)
snmpv3PrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3PrivPassword.setStatus("current")


class _Snmpv3UserType_Type(Integer32):
    """Custom type snmpv3UserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Snmpv3UserType_Type.__name__ = "Integer32"
_Snmpv3UserType_Object = MibTableColumn
snmpv3UserType = _Snmpv3UserType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 9, 1, 6),
    _Snmpv3UserType_Type()
)
snmpv3UserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpv3UserType.setStatus("current")
_OstProtocolStatusTable_Object = MibTable
ostProtocolStatusTable = _OstProtocolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10)
)
if mibBuilder.loadTexts:
    ostProtocolStatusTable.setStatus("current")
_OstProtocolStatusEntry_Object = MibTableRow
ostProtocolStatusEntry = _OstProtocolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1)
)
ostProtocolStatusEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
    (0, "OMNITRON-MIB", "userIndex"),
    (0, "OMNITRON-MIB", "ostProtocolStatusIndex"),
)
if mibBuilder.loadTexts:
    ostProtocolStatusEntry.setStatus("current")
_OstProtocolStatusIndex_Type = Unsigned32
_OstProtocolStatusIndex_Object = MibTableColumn
ostProtocolStatusIndex = _OstProtocolStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 1),
    _OstProtocolStatusIndex_Type()
)
ostProtocolStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostProtocolStatusIndex.setStatus("current")


class _OstProtocolStatusType_Type(Integer32):
    """Custom type ostProtocolStatusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("serial", 1),
          ("telnet", 2))
    )


_OstProtocolStatusType_Type.__name__ = "Integer32"
_OstProtocolStatusType_Object = MibTableColumn
ostProtocolStatusType = _OstProtocolStatusType_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 2),
    _OstProtocolStatusType_Type()
)
ostProtocolStatusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostProtocolStatusType.setStatus("current")


class _OstProtocolStatusState_Type(Integer32):
    """Custom type ostProtocolStatusState based on Integer32"""
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
          ("inactive", 1),
          ("lockedout", 3))
    )


_OstProtocolStatusState_Type.__name__ = "Integer32"
_OstProtocolStatusState_Object = MibTableColumn
ostProtocolStatusState = _OstProtocolStatusState_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 3),
    _OstProtocolStatusState_Type()
)
ostProtocolStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostProtocolStatusState.setStatus("current")


class _OstProtocoManagementPort_Type(Integer32):
    """Custom type ostProtocoManagementPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgt1", 2),
          ("mgt2", 3),
          ("notDefined", 1))
    )


_OstProtocoManagementPort_Type.__name__ = "Integer32"
_OstProtocoManagementPort_Object = MibTableColumn
ostProtocoManagementPort = _OstProtocoManagementPort_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 4),
    _OstProtocoManagementPort_Type()
)
ostProtocoManagementPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostProtocoManagementPort.setStatus("current")
_OstProtocolStatusIpAddress_Type = IpAddress
_OstProtocolStatusIpAddress_Object = MibTableColumn
ostProtocolStatusIpAddress = _OstProtocolStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 5),
    _OstProtocolStatusIpAddress_Type()
)
ostProtocolStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostProtocolStatusIpAddress.setStatus("current")
_OstProtocolStatusSessionOpenLockTime_Type = TimeInterval
_OstProtocolStatusSessionOpenLockTime_Object = MibTableColumn
ostProtocolStatusSessionOpenLockTime = _OstProtocolStatusSessionOpenLockTime_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 10, 1, 6),
    _OstProtocolStatusSessionOpenLockTime_Type()
)
ostProtocolStatusSessionOpenLockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostProtocolStatusSessionOpenLockTime.setStatus("current")
_OstEnvironmentalStatusTable_Object = MibTable
ostEnvironmentalStatusTable = _OstEnvironmentalStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11)
)
if mibBuilder.loadTexts:
    ostEnvironmentalStatusTable.setStatus("current")
_OstEnvironmentalStatusEntry_Object = MibTableRow
ostEnvironmentalStatusEntry = _OstEnvironmentalStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1)
)
ostEnvironmentalStatusEntry.setIndexNames(
    (0, "OMNITRON-MIB", "modchassnum"),
    (0, "OMNITRON-MIB", "modslotnum"),
)
if mibBuilder.loadTexts:
    ostEnvironmentalStatusEntry.setStatus("current")


class _OstEnvironmentalPs1Status_Type(Integer32):
    """Custom type ostEnvironmentalPs1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installedNotPowered", 2),
          ("installedPowered", 3),
          ("notApplicable", 0),
          ("notInstalled", 1))
    )


_OstEnvironmentalPs1Status_Type.__name__ = "Integer32"
_OstEnvironmentalPs1Status_Object = MibTableColumn
ostEnvironmentalPs1Status = _OstEnvironmentalPs1Status_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 1),
    _OstEnvironmentalPs1Status_Type()
)
ostEnvironmentalPs1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1Status.setStatus("current")
_OstEnvironmentalPs1VoltageIn_Type = Integer32
_OstEnvironmentalPs1VoltageIn_Object = MibTableColumn
ostEnvironmentalPs1VoltageIn = _OstEnvironmentalPs1VoltageIn_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 2),
    _OstEnvironmentalPs1VoltageIn_Type()
)
ostEnvironmentalPs1VoltageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1VoltageIn.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1VoltageIn.setUnits("millivolts")
_OstEnvironmentalPs1VoltageOut_Type = Unsigned32
_OstEnvironmentalPs1VoltageOut_Object = MibTableColumn
ostEnvironmentalPs1VoltageOut = _OstEnvironmentalPs1VoltageOut_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 3),
    _OstEnvironmentalPs1VoltageOut_Type()
)
ostEnvironmentalPs1VoltageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1VoltageOut.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1VoltageOut.setUnits("millivolts")
_OstEnvironmentalPs1CurrentOut_Type = Unsigned32
_OstEnvironmentalPs1CurrentOut_Object = MibTableColumn
ostEnvironmentalPs1CurrentOut = _OstEnvironmentalPs1CurrentOut_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 4),
    _OstEnvironmentalPs1CurrentOut_Type()
)
ostEnvironmentalPs1CurrentOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1CurrentOut.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs1CurrentOut.setUnits("milliamps")


class _OstEnvironmentalPs2Status_Type(Integer32):
    """Custom type ostEnvironmentalPs2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installedNotPowered", 2),
          ("installedPowered", 3),
          ("notApplicable", 0),
          ("notInstalled", 1))
    )


_OstEnvironmentalPs2Status_Type.__name__ = "Integer32"
_OstEnvironmentalPs2Status_Object = MibTableColumn
ostEnvironmentalPs2Status = _OstEnvironmentalPs2Status_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 5),
    _OstEnvironmentalPs2Status_Type()
)
ostEnvironmentalPs2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2Status.setStatus("current")
_OstEnvironmentalPs2VoltageIn_Type = Integer32
_OstEnvironmentalPs2VoltageIn_Object = MibTableColumn
ostEnvironmentalPs2VoltageIn = _OstEnvironmentalPs2VoltageIn_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 6),
    _OstEnvironmentalPs2VoltageIn_Type()
)
ostEnvironmentalPs2VoltageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2VoltageIn.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2VoltageIn.setUnits("millivolts")
_OstEnvironmentalPs2VoltageOut_Type = Unsigned32
_OstEnvironmentalPs2VoltageOut_Object = MibTableColumn
ostEnvironmentalPs2VoltageOut = _OstEnvironmentalPs2VoltageOut_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 7),
    _OstEnvironmentalPs2VoltageOut_Type()
)
ostEnvironmentalPs2VoltageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2VoltageOut.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2VoltageOut.setUnits("millivolts")
_OstEnvironmentalPs2CurrentOut_Type = Unsigned32
_OstEnvironmentalPs2CurrentOut_Object = MibTableColumn
ostEnvironmentalPs2CurrentOut = _OstEnvironmentalPs2CurrentOut_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 8),
    _OstEnvironmentalPs2CurrentOut_Type()
)
ostEnvironmentalPs2CurrentOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2CurrentOut.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalPs2CurrentOut.setUnits("milliamps")
_OstEnvironmentalTemperature_Type = Integer32
_OstEnvironmentalTemperature_Object = MibTableColumn
ostEnvironmentalTemperature = _OstEnvironmentalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 9),
    _OstEnvironmentalTemperature_Type()
)
ostEnvironmentalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalTemperature.setUnits("degrees centigrade")


class _OstEnvironmentalFan1Status_Type(Integer32):
    """Custom type ostEnvironmentalFan1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installedNotPowered", 2),
          ("installedPowered", 3),
          ("notApplicable", 0),
          ("notInstalled", 1))
    )


_OstEnvironmentalFan1Status_Type.__name__ = "Integer32"
_OstEnvironmentalFan1Status_Object = MibTableColumn
ostEnvironmentalFan1Status = _OstEnvironmentalFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 10),
    _OstEnvironmentalFan1Status_Type()
)
ostEnvironmentalFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan1Status.setStatus("current")
_OstEnvironmentalFan1Speed_Type = Unsigned32
_OstEnvironmentalFan1Speed_Object = MibTableColumn
ostEnvironmentalFan1Speed = _OstEnvironmentalFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 11),
    _OstEnvironmentalFan1Speed_Type()
)
ostEnvironmentalFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalFan1Speed.setUnits("rpm")


class _OstEnvironmentalFan2Status_Type(Integer32):
    """Custom type ostEnvironmentalFan2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installedNotPowered", 2),
          ("installedPowered", 3),
          ("notApplicable", 0),
          ("notInstalled", 1))
    )


_OstEnvironmentalFan2Status_Type.__name__ = "Integer32"
_OstEnvironmentalFan2Status_Object = MibTableColumn
ostEnvironmentalFan2Status = _OstEnvironmentalFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 12),
    _OstEnvironmentalFan2Status_Type()
)
ostEnvironmentalFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan2Status.setStatus("current")
_OstEnvironmentalFan2Speed_Type = Unsigned32
_OstEnvironmentalFan2Speed_Object = MibTableColumn
ostEnvironmentalFan2Speed = _OstEnvironmentalFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 13),
    _OstEnvironmentalFan2Speed_Type()
)
ostEnvironmentalFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalFan2Speed.setUnits("rpm")


class _OstEnvironmentalFan3Status_Type(Integer32):
    """Custom type ostEnvironmentalFan3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installedNotPowered", 2),
          ("installedPowered", 3),
          ("notApplicable", 0),
          ("notInstalled", 1))
    )


_OstEnvironmentalFan3Status_Type.__name__ = "Integer32"
_OstEnvironmentalFan3Status_Object = MibTableColumn
ostEnvironmentalFan3Status = _OstEnvironmentalFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 14),
    _OstEnvironmentalFan3Status_Type()
)
ostEnvironmentalFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan3Status.setStatus("current")
_OstEnvironmentalFan3Speed_Type = Unsigned32
_OstEnvironmentalFan3Speed_Object = MibTableColumn
ostEnvironmentalFan3Speed = _OstEnvironmentalFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 7342, 2, 1, 11, 1, 15),
    _OstEnvironmentalFan3Speed_Type()
)
ostEnvironmentalFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostEnvironmentalFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    ostEnvironmentalFan3Speed.setUnits("rpm")
_OmnitronConformance_ObjectIdentity = ObjectIdentity
omnitronConformance = _OmnitronConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 4)
)
_OmnitronCompliances_ObjectIdentity = ObjectIdentity
omnitronCompliances = _OmnitronCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 4, 1)
)
_OmnitronGroups_ObjectIdentity = ObjectIdentity
omnitronGroups = _OmnitronGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 4, 2)
)
_OmnitronProducts_ObjectIdentity = ObjectIdentity
omnitronProducts = _OmnitronProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 5)
)
_ManagementModule_ObjectIdentity = ObjectIdentity
managementModule = _ManagementModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 5, 1)
)

# Managed Objects groups

omnitronGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7342, 4, 2, 1)
)
omnitronGroup.setObjects(
      *(("OMNITRON-MIB", "chassis"),
        ("OMNITRON-MIB", "selfSlot"),
        ("OMNITRON-MIB", "chassisnum"),
        ("OMNITRON-MIB", "slotnum"),
        ("OMNITRON-MIB", "chassistype"),
        ("OMNITRON-MIB", "prodtype"),
        ("OMNITRON-MIB", "chassisname"),
        ("OMNITRON-MIB", "partnum"),
        ("OMNITRON-MIB", "serialnum"),
        ("OMNITRON-MIB", "manufdate"),
        ("OMNITRON-MIB", "softrev"),
        ("OMNITRON-MIB", "prodrev"),
        ("OMNITRON-MIB", "ledstat"),
        ("OMNITRON-MIB", "switchstat"),
        ("OMNITRON-MIB", "extended1"),
        ("OMNITRON-MIB", "extended2"),
        ("OMNITRON-MIB", "extended3"),
        ("OMNITRON-MIB", "extended4"),
        ("OMNITRON-MIB", "extended5"),
        ("OMNITRON-MIB", "extended6"),
        ("OMNITRON-MIB", "resetmod"),
        ("OMNITRON-MIB", "wrswitch"),
        ("OMNITRON-MIB", "modulename"),
        ("OMNITRON-MIB", "moduleCount"),
        ("OMNITRON-MIB", "modchassnum"),
        ("OMNITRON-MIB", "modslotnum"),
        ("OMNITRON-MIB", "modchasstype"),
        ("OMNITRON-MIB", "modprodtype"),
        ("OMNITRON-MIB", "modsoftrev"),
        ("OMNITRON-MIB", "modprodrev"),
        ("OMNITRON-MIB", "modreset"),
        ("OMNITRON-MIB", "modnumports"),
        ("OMNITRON-MIB", "modchassname"),
        ("OMNITRON-MIB", "modpartnum"),
        ("OMNITRON-MIB", "modserialnum"),
        ("OMNITRON-MIB", "modmanufdate"),
        ("OMNITRON-MIB", "modname"),
        ("OMNITRON-MIB", "modportvlan"),
        ("OMNITRON-MIB", "modextfeaturebits"),
        ("OMNITRON-MIB", "modswbuildnum"),
        ("OMNITRON-MIB", "modenable802dot1qProcessing"),
        ("OMNITRON-MIB", "modtagsubstitution"),
        ("OMNITRON-MIB", "modcommitVLANchanges"),
        ("OMNITRON-MIB", "modvlanTableClear"),
        ("OMNITRON-MIB", "modcommitNMMCfgChanges"),
        ("OMNITRON-MIB", "modLM80volts"),
        ("OMNITRON-MIB", "modLM80currents"),
        ("OMNITRON-MIB", "modLM80misc"),
        ("OMNITRON-MIB", "modRestoreFactoryDefaults"),
        ("OMNITRON-MIB", "sysAdminStatus"),
        ("OMNITRON-MIB", "sysDateTime"),
        ("OMNITRON-MIB", "macAddr"),
        ("OMNITRON-MIB", "ipAddr"),
        ("OMNITRON-MIB", "subnetmask"),
        ("OMNITRON-MIB", "gateway"),
        ("OMNITRON-MIB", "readCommunity"),
        ("OMNITRON-MIB", "writeCommunity"),
        ("OMNITRON-MIB", "mychassnum"),
        ("OMNITRON-MIB", "mmname"),
        ("OMNITRON-MIB", "traphost1"),
        ("OMNITRON-MIB", "traphost2"),
        ("OMNITRON-MIB", "traphost3"),
        ("OMNITRON-MIB", "traphost4"),
        ("OMNITRON-MIB", "traphost5"),
        ("OMNITRON-MIB", "traphost6"),
        ("OMNITRON-MIB", "traphost7"),
        ("OMNITRON-MIB", "traphost8"),
        ("OMNITRON-MIB", "sysloc"),
        ("OMNITRON-MIB", "syscon"),
        ("OMNITRON-MIB", "serialpass"),
        ("OMNITRON-MIB", "telnetpass"),
        ("OMNITRON-MIB", "ftppasswrd"),
        ("OMNITRON-MIB", "keepAliveInterval"),
        ("OMNITRON-MIB", "vlanIdOst"),
        ("OMNITRON-MIB", "nmmCfgSerialBaudrate"),
        ("OMNITRON-MIB", "enabledFunctions"),
        ("OMNITRON-MIB", "enableSNMPFunction"),
        ("OMNITRON-MIB", "nmmCfgState"),
        ("OMNITRON-MIB", "nmmSecureMode"),
        ("OMNITRON-MIB", "nmmSecureConnState"),
        ("OMNITRON-MIB", "nmmIpProtocolState"),
        ("OMNITRON-MIB", "nmmIpDisabled"),
        ("OMNITRON-MIB", "vlanPri"),
        ("OMNITRON-MIB", "enableSNMPWrites"),
        ("OMNITRON-MIB", "cpuVoltageIn"),
        ("OMNITRON-MIB", "cpuVoltageOut"),
        ("OMNITRON-MIB", "cpuTemperature"),
        ("OMNITRON-MIB", "nmmSecureSlaveSlot"),
        ("OMNITRON-MIB", "dhcpIpAddr"),
        ("OMNITRON-MIB", "dhcpSubnetmask"),
        ("OMNITRON-MIB", "dhcpGateway"),
        ("OMNITRON-MIB", "nmmOAMmgmtMode"),
        ("OMNITRON-MIB", "customertag"),
        ("OMNITRON-MIB", "servicetag"),
        ("OMNITRON-MIB", "cnodeControl"),
        ("OMNITRON-MIB", "cnodeCIR"),
        ("OMNITRON-MIB", "enableSNMPv3Function"),
        ("OMNITRON-MIB", "slaveWrite"),
        ("OMNITRON-MIB", "snmpTrapType"),
        ("OMNITRON-MIB", "capsMask"),
        ("OMNITRON-MIB", "slaveTraps"),
        ("OMNITRON-MIB", "slaveTrapsForward"),
        ("OMNITRON-MIB", "coreStatusOnly"),
        ("OMNITRON-MIB", "ingressPolicingType"),
        ("OMNITRON-MIB", "vlanservicetag"),
        ("OMNITRON-MIB", "defaultForwardingMap"),
        ("OMNITRON-MIB", "modFpgaRev"),
        ("OMNITRON-MIB", "modExpPartNumber"),
        ("OMNITRON-MIB", "modExpSoftwareRev"),
        ("OMNITRON-MIB", "modExpLedStatus"),
        ("OMNITRON-MIB", "modHwRev"),
        ("OMNITRON-MIB", "modPcbRev"),
        ("OMNITRON-MIB", "ipAddr2"),
        ("OMNITRON-MIB", "subnetmask2"),
        ("OMNITRON-MIB", "gateway2"),
        ("OMNITRON-MIB", "ipaddrEVCassociation"),
        ("OMNITRON-MIB", "ipaddr2EVCassociation"),
        ("OMNITRON-MIB", "bootpEnable"),
        ("OMNITRON-MIB", "tftpEnable"),
        ("OMNITRON-MIB", "tftpServerIpAddress"),
        ("OMNITRON-MIB", "dhcptftpServerIpAddress"),
        ("OMNITRON-MIB", "tftpFileName"),
        ("OMNITRON-MIB", "modeType"),
        ("OMNITRON-MIB", "dhcpPortNumber"),
        ("OMNITRON-MIB", "dhcpTagVid"),
        ("OMNITRON-MIB", "trapSrcIpSelect"),
        ("OMNITRON-MIB", "muxGroupDefaults"),
        ("OMNITRON-MIB", "portFwdCpu"),
        ("OMNITRON-MIB", "portFwdCpuList"),
        ("OMNITRON-MIB", "portState"),
        ("OMNITRON-MIB", "portEgressRate"),
        ("OMNITRON-MIB", "portpriority"),
        ("OMNITRON-MIB", "portcanonicalformatIndicator"),
        ("OMNITRON-MIB", "portvlanidentifier"),
        ("OMNITRON-MIB", "portmlistcriteria"),
        ("OMNITRON-MIB", "portingresssecurity"),
        ("OMNITRON-MIB", "portegresspolicy"),
        ("OMNITRON-MIB", "portIngressRate"),
        ("OMNITRON-MIB", "portSpeed"),
        ("OMNITRON-MIB", "portUnidirectionalAhOamEnable"),
        ("OMNITRON-MIB", "portIngressRateDropOrPause"),
        ("OMNITRON-MIB", "portIngressRateCBS"),
        ("OMNITRON-MIB", "portL2CPmgntProcessing"),
        ("OMNITRON-MIB", "portEgressQosPolicy"),
        ("OMNITRON-MIB", "portAccessType"),
        ("OMNITRON-MIB", "portStatsClear"),
        ("OMNITRON-MIB", "portLinkState"),
        ("OMNITRON-MIB", "portDuplex"),
        ("OMNITRON-MIB", "portMacAddress"),
        ("OMNITRON-MIB", "txOctets"),
        ("OMNITRON-MIB", "txDropPkts"),
        ("OMNITRON-MIB", "txBroadcastPkts"),
        ("OMNITRON-MIB", "txMulticastPkts"),
        ("OMNITRON-MIB", "txUnicastPkts"),
        ("OMNITRON-MIB", "txGoodPkts"),
        ("OMNITRON-MIB", "txErrorPkts"),
        ("OMNITRON-MIB", "txPausePkts"),
        ("OMNITRON-MIB", "txCollisions"),
        ("OMNITRON-MIB", "txSingleCollision"),
        ("OMNITRON-MIB", "txMultipleCollision"),
        ("OMNITRON-MIB", "txDeferedTransmit"),
        ("OMNITRON-MIB", "txLateCollision"),
        ("OMNITRON-MIB", "txExcessiveCollision"),
        ("OMNITRON-MIB", "txDroppedEvents"),
        ("OMNITRON-MIB", "rxOctets"),
        ("OMNITRON-MIB", "rxDropPkts"),
        ("OMNITRON-MIB", "rxBroadcastPkts"),
        ("OMNITRON-MIB", "rxMulticastPkts"),
        ("OMNITRON-MIB", "rxUnicastPkts"),
        ("OMNITRON-MIB", "rxGoodPkts"),
        ("OMNITRON-MIB", "rxTotalPkts"),
        ("OMNITRON-MIB", "rxErrorPkts"),
        ("OMNITRON-MIB", "rxPausePkts"),
        ("OMNITRON-MIB", "rxUndersizePkts"),
        ("OMNITRON-MIB", "rxOversizePkts"),
        ("OMNITRON-MIB", "rxFragments"),
        ("OMNITRON-MIB", "rxJabbers"),
        ("OMNITRON-MIB", "rxAlignmentErrors"),
        ("OMNITRON-MIB", "rxFCSErrors"),
        ("OMNITRON-MIB", "rxSymbolErrors"),
        ("OMNITRON-MIB", "rxCRCAlignErrors"),
        ("OMNITRON-MIB", "rxPackets64"),
        ("OMNITRON-MIB", "rxPackets65to127"),
        ("OMNITRON-MIB", "rxPackets128to255"),
        ("OMNITRON-MIB", "rxPackets256to511"),
        ("OMNITRON-MIB", "rxPackets512to1023"),
        ("OMNITRON-MIB", "rxPackets1024to1518"),
        ("OMNITRON-MIB", "txOctets64"),
        ("OMNITRON-MIB", "rxOctets64"),
        ("OMNITRON-MIB", "validityflag"),
        ("OMNITRON-MIB", "vlanidentifier"),
        ("OMNITRON-MIB", "port1Membership"),
        ("OMNITRON-MIB", "port2Membership"),
        ("OMNITRON-MIB", "port3Membership"),
        ("OMNITRON-MIB", "port4Membership"),
        ("OMNITRON-MIB", "port5Membership"),
        ("OMNITRON-MIB", "port6Membership"),
        ("OMNITRON-MIB", "ahEnabled"),
        ("OMNITRON-MIB", "ahLpbkMode"),
        ("OMNITRON-MIB", "ahLocalMode"),
        ("OMNITRON-MIB", "ahRemoteMode"),
        ("OMNITRON-MIB", "ahLocalMuxState"),
        ("OMNITRON-MIB", "ahRemoteMuxState"),
        ("OMNITRON-MIB", "ahLocalParserState"),
        ("OMNITRON-MIB", "ahRemoteParserState"),
        ("OMNITRON-MIB", "ahLocalSupportVar"),
        ("OMNITRON-MIB", "ahLocalLinkFlags"),
        ("OMNITRON-MIB", "ahLocalLpbkTimeout"),
        ("OMNITRON-MIB", "ahRemoteSupportVar"),
        ("OMNITRON-MIB", "ahRemoteLinkFlags"),
        ("OMNITRON-MIB", "ahRemoteLpbkTimeout"),
        ("OMNITRON-MIB", "ahLocalOUI"),
        ("OMNITRON-MIB", "ahRemoteOUI"),
        ("OMNITRON-MIB", "ahErroredSymbolPeriodWindow"),
        ("OMNITRON-MIB", "ahErroredSymbolPeriodThreshold"),
        ("OMNITRON-MIB", "ahErroredFrameWindow"),
        ("OMNITRON-MIB", "ahErroredFrameThreshold"),
        ("OMNITRON-MIB", "ahErroredFramePeriodWindow"),
        ("OMNITRON-MIB", "ahErroredFramePeriodThreshold"),
        ("OMNITRON-MIB", "ahErroredFrameSecondsWindow"),
        ("OMNITRON-MIB", "ahErroredFrameSecondsThreshold"),
        ("OMNITRON-MIB", "ahRemoteLinkPort"),
        ("OMNITRON-MIB", "ahSymbolErrorRunningTotal"),
        ("OMNITRON-MIB", "ahSymbolErrorEventTotal"),
        ("OMNITRON-MIB", "ahFrameErrorRunningTotal"),
        ("OMNITRON-MIB", "ahFrameErrorEventTotal"),
        ("OMNITRON-MIB", "ahFramePeriodRunningTotal"),
        ("OMNITRON-MIB", "ahFramePeriodEventTotal"),
        ("OMNITRON-MIB", "ahFrameSecondsSummaryRunningTotal"),
        ("OMNITRON-MIB", "ahFrameSecondsSummaryEventTotal"),
        ("OMNITRON-MIB", "ahClearStatistics"),
        ("OMNITRON-MIB", "ahTransmissionRate"),
        ("OMNITRON-MIB", "ahCriticalEventMode"),
        ("OMNITRON-MIB", "ahCriticalEventTrapList"),
        ("OMNITRON-MIB", "snmpv3UserName"),
        ("OMNITRON-MIB", "snmpv3SecurityLevel"),
        ("OMNITRON-MIB", "snmpv3AuthPassword"),
        ("OMNITRON-MIB", "snmpv3PrivPassword"),
        ("OMNITRON-MIB", "snmpv3UserType"),
        ("OMNITRON-MIB", "ostProtocolStatusType"),
        ("OMNITRON-MIB", "ostProtocolStatusState"),
        ("OMNITRON-MIB", "ostProtocoManagementPort"),
        ("OMNITRON-MIB", "ostProtocolStatusIpAddress"),
        ("OMNITRON-MIB", "ostProtocolStatusSessionOpenLockTime"),
        ("OMNITRON-MIB", "ostEnvironmentalPs1Status"),
        ("OMNITRON-MIB", "ostEnvironmentalPs1VoltageIn"),
        ("OMNITRON-MIB", "ostEnvironmentalPs1VoltageOut"),
        ("OMNITRON-MIB", "ostEnvironmentalPs1CurrentOut"),
        ("OMNITRON-MIB", "ostEnvironmentalPs2Status"),
        ("OMNITRON-MIB", "ostEnvironmentalPs2VoltageIn"),
        ("OMNITRON-MIB", "ostEnvironmentalPs2VoltageOut"),
        ("OMNITRON-MIB", "ostEnvironmentalPs2CurrentOut"),
        ("OMNITRON-MIB", "ostEnvironmentalTemperature"),
        ("OMNITRON-MIB", "ostEnvironmentalFan1Status"),
        ("OMNITRON-MIB", "ostEnvironmentalFan1Speed"),
        ("OMNITRON-MIB", "ostEnvironmentalFan2Status"),
        ("OMNITRON-MIB", "ostEnvironmentalFan2Speed"),
        ("OMNITRON-MIB", "ostEnvironmentalFan3Status"),
        ("OMNITRON-MIB", "ostEnvironmentalFan3Speed"))
)
if mibBuilder.loadTexts:
    omnitronGroup.setStatus("current")

omnitronSFPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7342, 4, 2, 2)
)
omnitronSFPGroup.setObjects(
      *(("OMNITRON-MIB", "portSFPstatus"),
        ("OMNITRON-MIB", "portSFPpageA0"),
        ("OMNITRON-MIB", "portSFPpageA2"),
        ("OMNITRON-MIB", "portSfpBitRate"),
        ("OMNITRON-MIB", "portSfpVendorName"),
        ("OMNITRON-MIB", "portSfpVendorPartNumber"),
        ("OMNITRON-MIB", "portSfpVendorSerialNumber"),
        ("OMNITRON-MIB", "portSfpDateCode"),
        ("OMNITRON-MIB", "portSfpTemperature"),
        ("OMNITRON-MIB", "portSfpVcc"),
        ("OMNITRON-MIB", "portSfpBiasCurrent"),
        ("OMNITRON-MIB", "portSfpTxPower"),
        ("OMNITRON-MIB", "portSfpRxPower"))
)
if mibBuilder.loadTexts:
    omnitronSFPGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

omnitronCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7342, 4, 1, 1)
)
if mibBuilder.loadTexts:
    omnitronCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNITRON-MIB",
    **{"chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisnum": chassisnum,
       "slotnum": slotnum,
       "chassistype": chassistype,
       "prodtype": prodtype,
       "chassisname": chassisname,
       "partnum": partnum,
       "serialnum": serialnum,
       "manufdate": manufdate,
       "softrev": softrev,
       "prodrev": prodrev,
       "ledstat": ledstat,
       "switchstat": switchstat,
       "extended1": extended1,
       "extended2": extended2,
       "extended3": extended3,
       "extended4": extended4,
       "extended5": extended5,
       "extended6": extended6,
       "resetmod": resetmod,
       "wrswitch": wrswitch,
       "modulename": modulename,
       "chassis": chassis,
       "selfSlot": selfSlot,
       "prodAgent": prodAgent,
       "enhancedchassisTable": enhancedchassisTable,
       "moduleCount": moduleCount,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "modchassnum": modchassnum,
       "modslotnum": modslotnum,
       "modchasstype": modchasstype,
       "modprodtype": modprodtype,
       "modsoftrev": modsoftrev,
       "modprodrev": modprodrev,
       "modreset": modreset,
       "modnumports": modnumports,
       "modchassname": modchassname,
       "modpartnum": modpartnum,
       "modserialnum": modserialnum,
       "modmanufdate": modmanufdate,
       "modname": modname,
       "modportvlan": modportvlan,
       "modextfeaturebits": modextfeaturebits,
       "modswbuildnum": modswbuildnum,
       "modenable802dot1qProcessing": modenable802dot1qProcessing,
       "modtagsubstitution": modtagsubstitution,
       "modcommitVLANchanges": modcommitVLANchanges,
       "modvlanTableClear": modvlanTableClear,
       "modcommitNMMCfgChanges": modcommitNMMCfgChanges,
       "modLM80volts": modLM80volts,
       "modLM80currents": modLM80currents,
       "modLM80misc": modLM80misc,
       "modRestoreFactoryDefaults": modRestoreFactoryDefaults,
       "coreStatusOnly": coreStatusOnly,
       "ingressPolicingType": ingressPolicingType,
       "vlanservicetag": vlanservicetag,
       "defaultForwardingMap": defaultForwardingMap,
       "modFpgaRev": modFpgaRev,
       "modExpPartNumber": modExpPartNumber,
       "modExpSoftwareRev": modExpSoftwareRev,
       "modExpLedStatus": modExpLedStatus,
       "modHwRev": modHwRev,
       "modPcbRev": modPcbRev,
       "moduleMgtCfgTable": moduleMgtCfgTable,
       "moduleMgtCfgEntry": moduleMgtCfgEntry,
       "sysAdminStatus": sysAdminStatus,
       "sysDateTime": sysDateTime,
       "macAddr": macAddr,
       "ipAddr": ipAddr,
       "subnetmask": subnetmask,
       "gateway": gateway,
       "readCommunity": readCommunity,
       "writeCommunity": writeCommunity,
       "mychassnum": mychassnum,
       "mmname": mmname,
       "traphost1": traphost1,
       "traphost2": traphost2,
       "traphost3": traphost3,
       "traphost4": traphost4,
       "traphost5": traphost5,
       "traphost6": traphost6,
       "traphost7": traphost7,
       "traphost8": traphost8,
       "sysloc": sysloc,
       "syscon": syscon,
       "serialpass": serialpass,
       "telnetpass": telnetpass,
       "ftppasswrd": ftppasswrd,
       "keepAliveInterval": keepAliveInterval,
       "vlanIdOst": vlanIdOst,
       "nmmCfgSerialBaudrate": nmmCfgSerialBaudrate,
       "enabledFunctions": enabledFunctions,
       "enableSNMPFunction": enableSNMPFunction,
       "nmmCfgState": nmmCfgState,
       "nmmSecureMode": nmmSecureMode,
       "nmmSecureConnState": nmmSecureConnState,
       "nmmIpProtocolState": nmmIpProtocolState,
       "nmmIpDisabled": nmmIpDisabled,
       "vlanPri": vlanPri,
       "enableSNMPWrites": enableSNMPWrites,
       "cpuVoltageIn": cpuVoltageIn,
       "cpuVoltageOut": cpuVoltageOut,
       "cpuTemperature": cpuTemperature,
       "nmmSecureSlaveSlot": nmmSecureSlaveSlot,
       "dhcpIpAddr": dhcpIpAddr,
       "dhcpSubnetmask": dhcpSubnetmask,
       "dhcpGateway": dhcpGateway,
       "nmmOAMmgmtMode": nmmOAMmgmtMode,
       "customertag": customertag,
       "servicetag": servicetag,
       "cnodeControl": cnodeControl,
       "cnodeCIR": cnodeCIR,
       "enableSNMPv3Function": enableSNMPv3Function,
       "slaveWrite": slaveWrite,
       "snmpTrapType": snmpTrapType,
       "capsMask": capsMask,
       "slaveTraps": slaveTraps,
       "slaveTrapsForward": slaveTrapsForward,
       "ipAddr2": ipAddr2,
       "subnetmask2": subnetmask2,
       "gateway2": gateway2,
       "ipaddrEVCassociation": ipaddrEVCassociation,
       "ipaddr2EVCassociation": ipaddr2EVCassociation,
       "bootpEnable": bootpEnable,
       "tftpEnable": tftpEnable,
       "tftpServerIpAddress": tftpServerIpAddress,
       "dhcptftpServerIpAddress": dhcptftpServerIpAddress,
       "tftpFileName": tftpFileName,
       "modeType": modeType,
       "dhcpPortNumber": dhcpPortNumber,
       "dhcpTagVid": dhcpTagVid,
       "trapSrcIpSelect": trapSrcIpSelect,
       "muxGroupDefaults": muxGroupDefaults,
       "portFwdCpu": portFwdCpu,
       "portFwdCpuList": portFwdCpuList,
       "modulePortsTable": modulePortsTable,
       "modulePortsEntry": modulePortsEntry,
       "portnum": portnum,
       "portState": portState,
       "portEgressRate": portEgressRate,
       "portpriority": portpriority,
       "portcanonicalformatIndicator": portcanonicalformatIndicator,
       "portvlanidentifier": portvlanidentifier,
       "portmlistcriteria": portmlistcriteria,
       "portingresssecurity": portingresssecurity,
       "portegresspolicy": portegresspolicy,
       "portIngressRate": portIngressRate,
       "portSpeed": portSpeed,
       "portUnidirectionalAhOamEnable": portUnidirectionalAhOamEnable,
       "portIngressRateDropOrPause": portIngressRateDropOrPause,
       "portIngressRateCBS": portIngressRateCBS,
       "portL2CPmgntProcessing": portL2CPmgntProcessing,
       "portEgressQosPolicy": portEgressQosPolicy,
       "portAccessType": portAccessType,
       "portStatsClear": portStatsClear,
       "portLinkState": portLinkState,
       "portDuplex": portDuplex,
       "portMacAddress": portMacAddress,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "txOctets": txOctets,
       "txDropPkts": txDropPkts,
       "txBroadcastPkts": txBroadcastPkts,
       "txMulticastPkts": txMulticastPkts,
       "txUnicastPkts": txUnicastPkts,
       "txGoodPkts": txGoodPkts,
       "txErrorPkts": txErrorPkts,
       "txPausePkts": txPausePkts,
       "txCollisions": txCollisions,
       "txSingleCollision": txSingleCollision,
       "txMultipleCollision": txMultipleCollision,
       "txDeferedTransmit": txDeferedTransmit,
       "txLateCollision": txLateCollision,
       "txExcessiveCollision": txExcessiveCollision,
       "txDroppedEvents": txDroppedEvents,
       "rxOctets": rxOctets,
       "rxDropPkts": rxDropPkts,
       "rxBroadcastPkts": rxBroadcastPkts,
       "rxMulticastPkts": rxMulticastPkts,
       "rxUnicastPkts": rxUnicastPkts,
       "rxGoodPkts": rxGoodPkts,
       "rxTotalPkts": rxTotalPkts,
       "rxErrorPkts": rxErrorPkts,
       "rxPausePkts": rxPausePkts,
       "rxUndersizePkts": rxUndersizePkts,
       "rxOversizePkts": rxOversizePkts,
       "rxFragments": rxFragments,
       "rxJabbers": rxJabbers,
       "rxAlignmentErrors": rxAlignmentErrors,
       "rxFCSErrors": rxFCSErrors,
       "rxSymbolErrors": rxSymbolErrors,
       "rxCRCAlignErrors": rxCRCAlignErrors,
       "rxPackets64": rxPackets64,
       "rxPackets65to127": rxPackets65to127,
       "rxPackets128to255": rxPackets128to255,
       "rxPackets256to511": rxPackets256to511,
       "rxPackets512to1023": rxPackets512to1023,
       "rxPackets1024to1518": rxPackets1024to1518,
       "txOctets64": txOctets64,
       "rxOctets64": rxOctets64,
       "moduleVLANTable": moduleVLANTable,
       "moduleVLANEntry": moduleVLANEntry,
       "index": index,
       "validityflag": validityflag,
       "vlanidentifier": vlanidentifier,
       "port1Membership": port1Membership,
       "port2Membership": port2Membership,
       "port3Membership": port3Membership,
       "port4Membership": port4Membership,
       "port5Membership": port5Membership,
       "port6Membership": port6Membership,
       "portAHTable": portAHTable,
       "portAHEntry": portAHEntry,
       "ahEnabled": ahEnabled,
       "ahLpbkMode": ahLpbkMode,
       "ahLocalMode": ahLocalMode,
       "ahRemoteMode": ahRemoteMode,
       "ahLocalMuxState": ahLocalMuxState,
       "ahRemoteMuxState": ahRemoteMuxState,
       "ahLocalParserState": ahLocalParserState,
       "ahRemoteParserState": ahRemoteParserState,
       "ahLocalSupportVar": ahLocalSupportVar,
       "ahLocalLinkFlags": ahLocalLinkFlags,
       "ahLocalLpbkTimeout": ahLocalLpbkTimeout,
       "ahRemoteSupportVar": ahRemoteSupportVar,
       "ahRemoteLinkFlags": ahRemoteLinkFlags,
       "ahRemoteLpbkTimeout": ahRemoteLpbkTimeout,
       "ahLocalOUI": ahLocalOUI,
       "ahRemoteOUI": ahRemoteOUI,
       "ahErroredSymbolPeriodWindow": ahErroredSymbolPeriodWindow,
       "ahErroredSymbolPeriodThreshold": ahErroredSymbolPeriodThreshold,
       "ahErroredFrameWindow": ahErroredFrameWindow,
       "ahErroredFrameThreshold": ahErroredFrameThreshold,
       "ahErroredFramePeriodWindow": ahErroredFramePeriodWindow,
       "ahErroredFramePeriodThreshold": ahErroredFramePeriodThreshold,
       "ahErroredFrameSecondsWindow": ahErroredFrameSecondsWindow,
       "ahErroredFrameSecondsThreshold": ahErroredFrameSecondsThreshold,
       "ahRemoteLinkPort": ahRemoteLinkPort,
       "ahSymbolErrorRunningTotal": ahSymbolErrorRunningTotal,
       "ahSymbolErrorEventTotal": ahSymbolErrorEventTotal,
       "ahFrameErrorRunningTotal": ahFrameErrorRunningTotal,
       "ahFrameErrorEventTotal": ahFrameErrorEventTotal,
       "ahFramePeriodRunningTotal": ahFramePeriodRunningTotal,
       "ahFramePeriodEventTotal": ahFramePeriodEventTotal,
       "ahFrameSecondsSummaryRunningTotal": ahFrameSecondsSummaryRunningTotal,
       "ahFrameSecondsSummaryEventTotal": ahFrameSecondsSummaryEventTotal,
       "ahClearStatistics": ahClearStatistics,
       "ahTransmissionRate": ahTransmissionRate,
       "ahCriticalEventMode": ahCriticalEventMode,
       "ahCriticalEventTrapList": ahCriticalEventTrapList,
       "portSFPTable": portSFPTable,
       "portSFPEntry": portSFPEntry,
       "portSFPstatus": portSFPstatus,
       "portSFPpageA0": portSFPpageA0,
       "portSFPpageA2": portSFPpageA2,
       "portSfpBitRate": portSfpBitRate,
       "portSfpVendorName": portSfpVendorName,
       "portSfpVendorPartNumber": portSfpVendorPartNumber,
       "portSfpVendorSerialNumber": portSfpVendorSerialNumber,
       "portSfpDateCode": portSfpDateCode,
       "portSfpTemperature": portSfpTemperature,
       "portSfpVcc": portSfpVcc,
       "portSfpBiasCurrent": portSfpBiasCurrent,
       "portSfpTxPower": portSfpTxPower,
       "portSfpRxPower": portSfpRxPower,
       "userTable": userTable,
       "userEntry": userEntry,
       "userIndex": userIndex,
       "snmpv3UserName": snmpv3UserName,
       "snmpv3SecurityLevel": snmpv3SecurityLevel,
       "snmpv3AuthPassword": snmpv3AuthPassword,
       "snmpv3PrivPassword": snmpv3PrivPassword,
       "snmpv3UserType": snmpv3UserType,
       "ostProtocolStatusTable": ostProtocolStatusTable,
       "ostProtocolStatusEntry": ostProtocolStatusEntry,
       "ostProtocolStatusIndex": ostProtocolStatusIndex,
       "ostProtocolStatusType": ostProtocolStatusType,
       "ostProtocolStatusState": ostProtocolStatusState,
       "ostProtocoManagementPort": ostProtocoManagementPort,
       "ostProtocolStatusIpAddress": ostProtocolStatusIpAddress,
       "ostProtocolStatusSessionOpenLockTime": ostProtocolStatusSessionOpenLockTime,
       "ostEnvironmentalStatusTable": ostEnvironmentalStatusTable,
       "ostEnvironmentalStatusEntry": ostEnvironmentalStatusEntry,
       "ostEnvironmentalPs1Status": ostEnvironmentalPs1Status,
       "ostEnvironmentalPs1VoltageIn": ostEnvironmentalPs1VoltageIn,
       "ostEnvironmentalPs1VoltageOut": ostEnvironmentalPs1VoltageOut,
       "ostEnvironmentalPs1CurrentOut": ostEnvironmentalPs1CurrentOut,
       "ostEnvironmentalPs2Status": ostEnvironmentalPs2Status,
       "ostEnvironmentalPs2VoltageIn": ostEnvironmentalPs2VoltageIn,
       "ostEnvironmentalPs2VoltageOut": ostEnvironmentalPs2VoltageOut,
       "ostEnvironmentalPs2CurrentOut": ostEnvironmentalPs2CurrentOut,
       "ostEnvironmentalTemperature": ostEnvironmentalTemperature,
       "ostEnvironmentalFan1Status": ostEnvironmentalFan1Status,
       "ostEnvironmentalFan1Speed": ostEnvironmentalFan1Speed,
       "ostEnvironmentalFan2Status": ostEnvironmentalFan2Status,
       "ostEnvironmentalFan2Speed": ostEnvironmentalFan2Speed,
       "ostEnvironmentalFan3Status": ostEnvironmentalFan3Status,
       "ostEnvironmentalFan3Speed": ostEnvironmentalFan3Speed,
       "omnitronMIB": omnitronMIB,
       "omnitronConformance": omnitronConformance,
       "omnitronCompliances": omnitronCompliances,
       "omnitronCompliance": omnitronCompliance,
       "omnitronGroups": omnitronGroups,
       "omnitronGroup": omnitronGroup,
       "omnitronSFPGroup": omnitronSFPGroup,
       "omnitronProducts": omnitronProducts,
       "managementModule": managementModule}
)
