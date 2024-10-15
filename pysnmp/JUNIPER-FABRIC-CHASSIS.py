# SNMP MIB module (JUNIPER-FABRIC-CHASSIS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-FABRIC-CHASSIS
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

(JnxChassisId,) = mibBuilder.importSymbols(
    "JUNIPER-MIB",
    "JnxChassisId")

(jnxDcfMibRoot,
 jnxFabricChassisOKTraps,
 jnxFabricChassisTraps) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxDcfMibRoot",
    "jnxFabricChassisOKTraps",
    "jnxFabricChassisTraps")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxFabricAnatomy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2)
)
jnxFabricAnatomy.setRevisions(
        ("2012-09-13 00:00",
         "2012-07-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxFabricDeviceId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class JnxFabricContainersFamily(Integer32, TextualConvention):
    status = "current"
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
        *(("directorGroupDevice", 4),
          ("fabricChassis", 1),
          ("fabricNode", 2),
          ("ufabric", 3))
    )



# MIB Managed Objects in the order of their OIDs

_JnxFabricAnatomyScalars_ObjectIdentity = ObjectIdentity
jnxFabricAnatomyScalars = _JnxFabricAnatomyScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1)
)
_JnxFabricClass_Type = ObjectIdentifier
_JnxFabricClass_Object = MibScalar
jnxFabricClass = _JnxFabricClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 1),
    _JnxFabricClass_Type()
)
jnxFabricClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricClass.setStatus("current")


class _JnxFabricDescr_Type(DisplayString):
    """Custom type jnxFabricDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDescr_Type.__name__ = "DisplayString"
_JnxFabricDescr_Object = MibScalar
jnxFabricDescr = _JnxFabricDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 2),
    _JnxFabricDescr_Type()
)
jnxFabricDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDescr.setStatus("current")


class _JnxFabricSerialNo_Type(DisplayString):
    """Custom type jnxFabricSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricSerialNo_Type.__name__ = "DisplayString"
_JnxFabricSerialNo_Object = MibScalar
jnxFabricSerialNo = _JnxFabricSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 3),
    _JnxFabricSerialNo_Type()
)
jnxFabricSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricSerialNo.setStatus("current")


class _JnxFabricRevision_Type(DisplayString):
    """Custom type jnxFabricRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricRevision_Type.__name__ = "DisplayString"
_JnxFabricRevision_Object = MibScalar
jnxFabricRevision = _JnxFabricRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 4),
    _JnxFabricRevision_Type()
)
jnxFabricRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRevision.setStatus("current")


class _JnxFabricFirmwareRevision_Type(DisplayString):
    """Custom type jnxFabricFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricFirmwareRevision_Type.__name__ = "DisplayString"
_JnxFabricFirmwareRevision_Object = MibScalar
jnxFabricFirmwareRevision = _JnxFabricFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 5),
    _JnxFabricFirmwareRevision_Type()
)
jnxFabricFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFirmwareRevision.setStatus("current")
_JnxFabricLastInstalled_Type = TimeTicks
_JnxFabricLastInstalled_Object = MibScalar
jnxFabricLastInstalled = _JnxFabricLastInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 6),
    _JnxFabricLastInstalled_Type()
)
jnxFabricLastInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricLastInstalled.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricLastInstalled.setUnits("centi-seconds")
_JnxFabricContentsLastChange_Type = TimeTicks
_JnxFabricContentsLastChange_Object = MibScalar
jnxFabricContentsLastChange = _JnxFabricContentsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 7),
    _JnxFabricContentsLastChange_Type()
)
jnxFabricContentsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsLastChange.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricContentsLastChange.setUnits("centi-seconds")
_JnxFabricFilledLastChange_Type = TimeTicks
_JnxFabricFilledLastChange_Object = MibScalar
jnxFabricFilledLastChange = _JnxFabricFilledLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 1, 8),
    _JnxFabricFilledLastChange_Type()
)
jnxFabricFilledLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledLastChange.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricFilledLastChange.setUnits("centi-seconds")
_JnxFabricAnatomyTables_ObjectIdentity = ObjectIdentity
jnxFabricAnatomyTables = _JnxFabricAnatomyTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2)
)
_JnxFabricDeviceTable_Object = MibTable
jnxFabricDeviceTable = _JnxFabricDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxFabricDeviceTable.setStatus("current")
_JnxFabricDeviceEntry_Object = MibTableRow
jnxFabricDeviceEntry = _JnxFabricDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1)
)
jnxFabricDeviceEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
)
if mibBuilder.loadTexts:
    jnxFabricDeviceEntry.setStatus("current")
_JnxFabricDeviceIndex_Type = JnxFabricDeviceId
_JnxFabricDeviceIndex_Object = MibTableColumn
jnxFabricDeviceIndex = _JnxFabricDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 1),
    _JnxFabricDeviceIndex_Type()
)
jnxFabricDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceIndex.setStatus("current")
_JnxFabricDeviceEntryContainersFamily_Type = JnxFabricContainersFamily
_JnxFabricDeviceEntryContainersFamily_Object = MibTableColumn
jnxFabricDeviceEntryContainersFamily = _JnxFabricDeviceEntryContainersFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 2),
    _JnxFabricDeviceEntryContainersFamily_Type()
)
jnxFabricDeviceEntryContainersFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryContainersFamily.setStatus("current")
_JnxFabricDeviceEntryClass_Type = ObjectIdentifier
_JnxFabricDeviceEntryClass_Object = MibTableColumn
jnxFabricDeviceEntryClass = _JnxFabricDeviceEntryClass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 3),
    _JnxFabricDeviceEntryClass_Type()
)
jnxFabricDeviceEntryClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryClass.setStatus("current")
_JnxFabricDeviceEntryModel_Type = ObjectIdentifier
_JnxFabricDeviceEntryModel_Object = MibTableColumn
jnxFabricDeviceEntryModel = _JnxFabricDeviceEntryModel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 4),
    _JnxFabricDeviceEntryModel_Type()
)
jnxFabricDeviceEntryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryModel.setStatus("current")


class _JnxFabricDeviceEntryDescr_Type(DisplayString):
    """Custom type jnxFabricDeviceEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDeviceEntryDescr_Type.__name__ = "DisplayString"
_JnxFabricDeviceEntryDescr_Object = MibTableColumn
jnxFabricDeviceEntryDescr = _JnxFabricDeviceEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 5),
    _JnxFabricDeviceEntryDescr_Type()
)
jnxFabricDeviceEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryDescr.setStatus("current")


class _JnxFabricDeviceEntrySerialNo_Type(DisplayString):
    """Custom type jnxFabricDeviceEntrySerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDeviceEntrySerialNo_Type.__name__ = "DisplayString"
_JnxFabricDeviceEntrySerialNo_Object = MibTableColumn
jnxFabricDeviceEntrySerialNo = _JnxFabricDeviceEntrySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 6),
    _JnxFabricDeviceEntrySerialNo_Type()
)
jnxFabricDeviceEntrySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntrySerialNo.setStatus("current")


class _JnxFabricDeviceEntryName_Type(DisplayString):
    """Custom type jnxFabricDeviceEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDeviceEntryName_Type.__name__ = "DisplayString"
_JnxFabricDeviceEntryName_Object = MibTableColumn
jnxFabricDeviceEntryName = _JnxFabricDeviceEntryName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 7),
    _JnxFabricDeviceEntryName_Type()
)
jnxFabricDeviceEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryName.setStatus("current")


class _JnxFabricDeviceEntryRevision_Type(DisplayString):
    """Custom type jnxFabricDeviceEntryRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDeviceEntryRevision_Type.__name__ = "DisplayString"
_JnxFabricDeviceEntryRevision_Object = MibTableColumn
jnxFabricDeviceEntryRevision = _JnxFabricDeviceEntryRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 8),
    _JnxFabricDeviceEntryRevision_Type()
)
jnxFabricDeviceEntryRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryRevision.setStatus("current")


class _JnxFabricDeviceEntryFirmwareRevision_Type(DisplayString):
    """Custom type jnxFabricDeviceEntryFirmwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricDeviceEntryFirmwareRevision_Type.__name__ = "DisplayString"
_JnxFabricDeviceEntryFirmwareRevision_Object = MibTableColumn
jnxFabricDeviceEntryFirmwareRevision = _JnxFabricDeviceEntryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 9),
    _JnxFabricDeviceEntryFirmwareRevision_Type()
)
jnxFabricDeviceEntryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryFirmwareRevision.setStatus("current")
_JnxFabricDeviceEntryInstalled_Type = TimeTicks
_JnxFabricDeviceEntryInstalled_Object = MibTableColumn
jnxFabricDeviceEntryInstalled = _JnxFabricDeviceEntryInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 10),
    _JnxFabricDeviceEntryInstalled_Type()
)
jnxFabricDeviceEntryInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryInstalled.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryInstalled.setUnits("centi-seconds")
_JnxFabricDeviceEntryContentsLastChange_Type = TimeTicks
_JnxFabricDeviceEntryContentsLastChange_Object = MibTableColumn
jnxFabricDeviceEntryContentsLastChange = _JnxFabricDeviceEntryContentsLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 11),
    _JnxFabricDeviceEntryContentsLastChange_Type()
)
jnxFabricDeviceEntryContentsLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryContentsLastChange.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryContentsLastChange.setUnits("centi-seconds")
_JnxFabricDeviceEntryFilledLastChange_Type = TimeTicks
_JnxFabricDeviceEntryFilledLastChange_Object = MibTableColumn
jnxFabricDeviceEntryFilledLastChange = _JnxFabricDeviceEntryFilledLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 12),
    _JnxFabricDeviceEntryFilledLastChange_Type()
)
jnxFabricDeviceEntryFilledLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryFilledLastChange.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryFilledLastChange.setUnits("centi-seconds")
_JnxFabricDeviceEntryKernelMemoryUsedPercent_Type = Integer32
_JnxFabricDeviceEntryKernelMemoryUsedPercent_Object = MibTableColumn
jnxFabricDeviceEntryKernelMemoryUsedPercent = _JnxFabricDeviceEntryKernelMemoryUsedPercent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 1, 1, 13),
    _JnxFabricDeviceEntryKernelMemoryUsedPercent_Type()
)
jnxFabricDeviceEntryKernelMemoryUsedPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricDeviceEntryKernelMemoryUsedPercent.setStatus("current")
_JnxFabricContainersTable_Object = MibTable
jnxFabricContainersTable = _JnxFabricContainersTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2)
)
if mibBuilder.loadTexts:
    jnxFabricContainersTable.setStatus("current")
_JnxFabricContainersEntry_Object = MibTableRow
jnxFabricContainersEntry = _JnxFabricContainersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1)
)
jnxFabricContainersEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContainersFamily"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContainersIndex"),
)
if mibBuilder.loadTexts:
    jnxFabricContainersEntry.setStatus("current")
_JnxFabricContainersFamily_Type = JnxFabricContainersFamily
_JnxFabricContainersFamily_Object = MibTableColumn
jnxFabricContainersFamily = _JnxFabricContainersFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 1),
    _JnxFabricContainersFamily_Type()
)
jnxFabricContainersFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersFamily.setStatus("current")


class _JnxFabricContainersIndex_Type(Integer32):
    """Custom type jnxFabricContainersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricContainersIndex_Type.__name__ = "Integer32"
_JnxFabricContainersIndex_Object = MibTableColumn
jnxFabricContainersIndex = _JnxFabricContainersIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 2),
    _JnxFabricContainersIndex_Type()
)
jnxFabricContainersIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersIndex.setStatus("current")


class _JnxFabricContainersView_Type(Bits):
    """Custom type jnxFabricContainersView based on Bits"""
    namedValues = NamedValues(
        *(("viewBottom", 3),
          ("viewFront", 0),
          ("viewLeftHandSide", 4),
          ("viewRear", 1),
          ("viewRightHandSide", 5),
          ("viewTop", 2))
    )

_JnxFabricContainersView_Type.__name__ = "Bits"
_JnxFabricContainersView_Object = MibTableColumn
jnxFabricContainersView = _JnxFabricContainersView_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 3),
    _JnxFabricContainersView_Type()
)
jnxFabricContainersView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersView.setStatus("current")


class _JnxFabricContainersLevel_Type(Integer32):
    """Custom type jnxFabricContainersLevel based on Integer32"""
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
        *(("level0", 0),
          ("level1", 1),
          ("level2", 2),
          ("level3", 3))
    )


_JnxFabricContainersLevel_Type.__name__ = "Integer32"
_JnxFabricContainersLevel_Object = MibTableColumn
jnxFabricContainersLevel = _JnxFabricContainersLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 4),
    _JnxFabricContainersLevel_Type()
)
jnxFabricContainersLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersLevel.setStatus("current")
_JnxFabricContainersWithin_Type = Integer32
_JnxFabricContainersWithin_Object = MibTableColumn
jnxFabricContainersWithin = _JnxFabricContainersWithin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 5),
    _JnxFabricContainersWithin_Type()
)
jnxFabricContainersWithin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersWithin.setStatus("current")
_JnxFabricContainersType_Type = ObjectIdentifier
_JnxFabricContainersType_Object = MibTableColumn
jnxFabricContainersType = _JnxFabricContainersType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 6),
    _JnxFabricContainersType_Type()
)
jnxFabricContainersType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersType.setStatus("current")


class _JnxFabricContainersDescr_Type(DisplayString):
    """Custom type jnxFabricContainersDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContainersDescr_Type.__name__ = "DisplayString"
_JnxFabricContainersDescr_Object = MibTableColumn
jnxFabricContainersDescr = _JnxFabricContainersDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 7),
    _JnxFabricContainersDescr_Type()
)
jnxFabricContainersDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersDescr.setStatus("current")
_JnxFabricContainersCount_Type = Integer32
_JnxFabricContainersCount_Object = MibTableColumn
jnxFabricContainersCount = _JnxFabricContainersCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 2, 1, 8),
    _JnxFabricContainersCount_Type()
)
jnxFabricContainersCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContainersCount.setStatus("current")
_JnxFabricContentsTable_Object = MibTable
jnxFabricContentsTable = _JnxFabricContentsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3)
)
if mibBuilder.loadTexts:
    jnxFabricContentsTable.setStatus("current")
_JnxFabricContentsEntry_Object = MibTableRow
jnxFabricContentsEntry = _JnxFabricContentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1)
)
jnxFabricContentsEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
)
if mibBuilder.loadTexts:
    jnxFabricContentsEntry.setStatus("current")


class _JnxFabricContentsContainerIndex_Type(Integer32):
    """Custom type jnxFabricContentsContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricContentsContainerIndex_Type.__name__ = "Integer32"
_JnxFabricContentsContainerIndex_Object = MibTableColumn
jnxFabricContentsContainerIndex = _JnxFabricContentsContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 1),
    _JnxFabricContentsContainerIndex_Type()
)
jnxFabricContentsContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsContainerIndex.setStatus("current")


class _JnxFabricContentsL1Index_Type(Integer32):
    """Custom type jnxFabricContentsL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricContentsL1Index_Type.__name__ = "Integer32"
_JnxFabricContentsL1Index_Object = MibTableColumn
jnxFabricContentsL1Index = _JnxFabricContentsL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 2),
    _JnxFabricContentsL1Index_Type()
)
jnxFabricContentsL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsL1Index.setStatus("current")


class _JnxFabricContentsL2Index_Type(Integer32):
    """Custom type jnxFabricContentsL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricContentsL2Index_Type.__name__ = "Integer32"
_JnxFabricContentsL2Index_Object = MibTableColumn
jnxFabricContentsL2Index = _JnxFabricContentsL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 3),
    _JnxFabricContentsL2Index_Type()
)
jnxFabricContentsL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsL2Index.setStatus("current")


class _JnxFabricContentsL3Index_Type(Integer32):
    """Custom type jnxFabricContentsL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricContentsL3Index_Type.__name__ = "Integer32"
_JnxFabricContentsL3Index_Object = MibTableColumn
jnxFabricContentsL3Index = _JnxFabricContentsL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 4),
    _JnxFabricContentsL3Index_Type()
)
jnxFabricContentsL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsL3Index.setStatus("current")
_JnxFabricContentsType_Type = ObjectIdentifier
_JnxFabricContentsType_Object = MibTableColumn
jnxFabricContentsType = _JnxFabricContentsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 5),
    _JnxFabricContentsType_Type()
)
jnxFabricContentsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsType.setStatus("current")


class _JnxFabricContentsDescr_Type(DisplayString):
    """Custom type jnxFabricContentsDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsDescr_Type.__name__ = "DisplayString"
_JnxFabricContentsDescr_Object = MibTableColumn
jnxFabricContentsDescr = _JnxFabricContentsDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 6),
    _JnxFabricContentsDescr_Type()
)
jnxFabricContentsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsDescr.setStatus("current")


class _JnxFabricContentsSerialNo_Type(DisplayString):
    """Custom type jnxFabricContentsSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsSerialNo_Type.__name__ = "DisplayString"
_JnxFabricContentsSerialNo_Object = MibTableColumn
jnxFabricContentsSerialNo = _JnxFabricContentsSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 7),
    _JnxFabricContentsSerialNo_Type()
)
jnxFabricContentsSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsSerialNo.setStatus("current")


class _JnxFabricContentsRevision_Type(DisplayString):
    """Custom type jnxFabricContentsRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsRevision_Type.__name__ = "DisplayString"
_JnxFabricContentsRevision_Object = MibTableColumn
jnxFabricContentsRevision = _JnxFabricContentsRevision_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 8),
    _JnxFabricContentsRevision_Type()
)
jnxFabricContentsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsRevision.setStatus("current")
_JnxFabricContentsInstalled_Type = TimeTicks
_JnxFabricContentsInstalled_Object = MibTableColumn
jnxFabricContentsInstalled = _JnxFabricContentsInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 9),
    _JnxFabricContentsInstalled_Type()
)
jnxFabricContentsInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsInstalled.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricContentsInstalled.setUnits("centi-seconds")


class _JnxFabricContentsPartNo_Type(DisplayString):
    """Custom type jnxFabricContentsPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsPartNo_Type.__name__ = "DisplayString"
_JnxFabricContentsPartNo_Object = MibTableColumn
jnxFabricContentsPartNo = _JnxFabricContentsPartNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 10),
    _JnxFabricContentsPartNo_Type()
)
jnxFabricContentsPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsPartNo.setStatus("current")
_JnxFabricContentsChassisId_Type = JnxChassisId
_JnxFabricContentsChassisId_Object = MibTableColumn
jnxFabricContentsChassisId = _JnxFabricContentsChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 11),
    _JnxFabricContentsChassisId_Type()
)
jnxFabricContentsChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsChassisId.setStatus("current")


class _JnxFabricContentsChassisDescr_Type(DisplayString):
    """Custom type jnxFabricContentsChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsChassisDescr_Type.__name__ = "DisplayString"
_JnxFabricContentsChassisDescr_Object = MibTableColumn
jnxFabricContentsChassisDescr = _JnxFabricContentsChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 12),
    _JnxFabricContentsChassisDescr_Type()
)
jnxFabricContentsChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsChassisDescr.setStatus("current")


class _JnxFabricContentsChassisCleiCode_Type(DisplayString):
    """Custom type jnxFabricContentsChassisCleiCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricContentsChassisCleiCode_Type.__name__ = "DisplayString"
_JnxFabricContentsChassisCleiCode_Object = MibTableColumn
jnxFabricContentsChassisCleiCode = _JnxFabricContentsChassisCleiCode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 3, 1, 13),
    _JnxFabricContentsChassisCleiCode_Type()
)
jnxFabricContentsChassisCleiCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricContentsChassisCleiCode.setStatus("current")
_JnxFabricFilledTable_Object = MibTable
jnxFabricFilledTable = _JnxFabricFilledTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4)
)
if mibBuilder.loadTexts:
    jnxFabricFilledTable.setStatus("current")
_JnxFabricFilledEntry_Object = MibTableRow
jnxFabricFilledEntry = _JnxFabricFilledEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1)
)
jnxFabricFilledEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFilledContainerIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFilledL1Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFilledL2Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFilledL3Index"),
)
if mibBuilder.loadTexts:
    jnxFabricFilledEntry.setStatus("current")


class _JnxFabricFilledContainerIndex_Type(Integer32):
    """Custom type jnxFabricFilledContainerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricFilledContainerIndex_Type.__name__ = "Integer32"
_JnxFabricFilledContainerIndex_Object = MibTableColumn
jnxFabricFilledContainerIndex = _JnxFabricFilledContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 1),
    _JnxFabricFilledContainerIndex_Type()
)
jnxFabricFilledContainerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledContainerIndex.setStatus("current")


class _JnxFabricFilledL1Index_Type(Integer32):
    """Custom type jnxFabricFilledL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFilledL1Index_Type.__name__ = "Integer32"
_JnxFabricFilledL1Index_Object = MibTableColumn
jnxFabricFilledL1Index = _JnxFabricFilledL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 2),
    _JnxFabricFilledL1Index_Type()
)
jnxFabricFilledL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledL1Index.setStatus("current")


class _JnxFabricFilledL2Index_Type(Integer32):
    """Custom type jnxFabricFilledL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFilledL2Index_Type.__name__ = "Integer32"
_JnxFabricFilledL2Index_Object = MibTableColumn
jnxFabricFilledL2Index = _JnxFabricFilledL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 3),
    _JnxFabricFilledL2Index_Type()
)
jnxFabricFilledL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledL2Index.setStatus("current")


class _JnxFabricFilledL3Index_Type(Integer32):
    """Custom type jnxFabricFilledL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFilledL3Index_Type.__name__ = "Integer32"
_JnxFabricFilledL3Index_Object = MibTableColumn
jnxFabricFilledL3Index = _JnxFabricFilledL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 4),
    _JnxFabricFilledL3Index_Type()
)
jnxFabricFilledL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledL3Index.setStatus("current")


class _JnxFabricFilledDescr_Type(DisplayString):
    """Custom type jnxFabricFilledDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricFilledDescr_Type.__name__ = "DisplayString"
_JnxFabricFilledDescr_Object = MibTableColumn
jnxFabricFilledDescr = _JnxFabricFilledDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 5),
    _JnxFabricFilledDescr_Type()
)
jnxFabricFilledDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledDescr.setStatus("current")


class _JnxFabricFilledState_Type(Integer32):
    """Custom type jnxFabricFilledState based on Integer32"""
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


_JnxFabricFilledState_Type.__name__ = "Integer32"
_JnxFabricFilledState_Object = MibTableColumn
jnxFabricFilledState = _JnxFabricFilledState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 6),
    _JnxFabricFilledState_Type()
)
jnxFabricFilledState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledState.setStatus("current")
_JnxFabricFilledChassisId_Type = JnxChassisId
_JnxFabricFilledChassisId_Object = MibTableColumn
jnxFabricFilledChassisId = _JnxFabricFilledChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 7),
    _JnxFabricFilledChassisId_Type()
)
jnxFabricFilledChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledChassisId.setStatus("current")


class _JnxFabricFilledChassisDescr_Type(DisplayString):
    """Custom type jnxFabricFilledChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricFilledChassisDescr_Type.__name__ = "DisplayString"
_JnxFabricFilledChassisDescr_Object = MibTableColumn
jnxFabricFilledChassisDescr = _JnxFabricFilledChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 4, 1, 8),
    _JnxFabricFilledChassisDescr_Type()
)
jnxFabricFilledChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFilledChassisDescr.setStatus("current")
_JnxFabricOperatingTable_Object = MibTable
jnxFabricOperatingTable = _JnxFabricOperatingTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5)
)
if mibBuilder.loadTexts:
    jnxFabricOperatingTable.setStatus("current")
_JnxFabricOperatingEntry_Object = MibTableRow
jnxFabricOperatingEntry = _JnxFabricOperatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1)
)
jnxFabricOperatingEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingContentsIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingL1Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingL2Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingL3Index"),
)
if mibBuilder.loadTexts:
    jnxFabricOperatingEntry.setStatus("current")


class _JnxFabricOperatingContentsIndex_Type(Integer32):
    """Custom type jnxFabricOperatingContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricOperatingContentsIndex_Type.__name__ = "Integer32"
_JnxFabricOperatingContentsIndex_Object = MibTableColumn
jnxFabricOperatingContentsIndex = _JnxFabricOperatingContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 1),
    _JnxFabricOperatingContentsIndex_Type()
)
jnxFabricOperatingContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingContentsIndex.setStatus("current")


class _JnxFabricOperatingL1Index_Type(Integer32):
    """Custom type jnxFabricOperatingL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricOperatingL1Index_Type.__name__ = "Integer32"
_JnxFabricOperatingL1Index_Object = MibTableColumn
jnxFabricOperatingL1Index = _JnxFabricOperatingL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 2),
    _JnxFabricOperatingL1Index_Type()
)
jnxFabricOperatingL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingL1Index.setStatus("current")


class _JnxFabricOperatingL2Index_Type(Integer32):
    """Custom type jnxFabricOperatingL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricOperatingL2Index_Type.__name__ = "Integer32"
_JnxFabricOperatingL2Index_Object = MibTableColumn
jnxFabricOperatingL2Index = _JnxFabricOperatingL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 3),
    _JnxFabricOperatingL2Index_Type()
)
jnxFabricOperatingL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingL2Index.setStatus("current")


class _JnxFabricOperatingL3Index_Type(Integer32):
    """Custom type jnxFabricOperatingL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricOperatingL3Index_Type.__name__ = "Integer32"
_JnxFabricOperatingL3Index_Object = MibTableColumn
jnxFabricOperatingL3Index = _JnxFabricOperatingL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 4),
    _JnxFabricOperatingL3Index_Type()
)
jnxFabricOperatingL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingL3Index.setStatus("current")


class _JnxFabricOperatingDescr_Type(DisplayString):
    """Custom type jnxFabricOperatingDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricOperatingDescr_Type.__name__ = "DisplayString"
_JnxFabricOperatingDescr_Object = MibTableColumn
jnxFabricOperatingDescr = _JnxFabricOperatingDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 5),
    _JnxFabricOperatingDescr_Type()
)
jnxFabricOperatingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingDescr.setStatus("current")


class _JnxFabricOperatingState_Type(Integer32):
    """Custom type jnxFabricOperatingState based on Integer32"""
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


_JnxFabricOperatingState_Type.__name__ = "Integer32"
_JnxFabricOperatingState_Object = MibTableColumn
jnxFabricOperatingState = _JnxFabricOperatingState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 6),
    _JnxFabricOperatingState_Type()
)
jnxFabricOperatingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingState.setStatus("current")
_JnxFabricOperatingTemp_Type = Integer32
_JnxFabricOperatingTemp_Object = MibTableColumn
jnxFabricOperatingTemp = _JnxFabricOperatingTemp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 7),
    _JnxFabricOperatingTemp_Type()
)
jnxFabricOperatingTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingTemp.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricOperatingTemp.setUnits("Celsius (degrees C)")
_JnxFabricOperatingCPU_Type = Integer32
_JnxFabricOperatingCPU_Object = MibTableColumn
jnxFabricOperatingCPU = _JnxFabricOperatingCPU_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 8),
    _JnxFabricOperatingCPU_Type()
)
jnxFabricOperatingCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingCPU.setStatus("current")
_JnxFabricOperatingISR_Type = Integer32
_JnxFabricOperatingISR_Object = MibTableColumn
jnxFabricOperatingISR = _JnxFabricOperatingISR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 9),
    _JnxFabricOperatingISR_Type()
)
jnxFabricOperatingISR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingISR.setStatus("current")
_JnxFabricOperatingDRAMSize_Type = Integer32
_JnxFabricOperatingDRAMSize_Object = MibTableColumn
jnxFabricOperatingDRAMSize = _JnxFabricOperatingDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 10),
    _JnxFabricOperatingDRAMSize_Type()
)
jnxFabricOperatingDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingDRAMSize.setStatus("deprecated")
_JnxFabricOperatingBuffer_Type = Integer32
_JnxFabricOperatingBuffer_Object = MibTableColumn
jnxFabricOperatingBuffer = _JnxFabricOperatingBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 11),
    _JnxFabricOperatingBuffer_Type()
)
jnxFabricOperatingBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingBuffer.setStatus("current")
_JnxFabricOperatingHeap_Type = Integer32
_JnxFabricOperatingHeap_Object = MibTableColumn
jnxFabricOperatingHeap = _JnxFabricOperatingHeap_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 12),
    _JnxFabricOperatingHeap_Type()
)
jnxFabricOperatingHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingHeap.setStatus("current")
_JnxFabricOperatingUpTime_Type = TimeTicks
_JnxFabricOperatingUpTime_Object = MibTableColumn
jnxFabricOperatingUpTime = _JnxFabricOperatingUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 13),
    _JnxFabricOperatingUpTime_Type()
)
jnxFabricOperatingUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingUpTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricOperatingUpTime.setUnits("centi-seconds")
_JnxFabricOperatingLastRestart_Type = TimeTicks
_JnxFabricOperatingLastRestart_Object = MibTableColumn
jnxFabricOperatingLastRestart = _JnxFabricOperatingLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 14),
    _JnxFabricOperatingLastRestart_Type()
)
jnxFabricOperatingLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingLastRestart.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricOperatingLastRestart.setUnits("centi-seconds")
_JnxFabricOperatingMemory_Type = Integer32
_JnxFabricOperatingMemory_Object = MibTableColumn
jnxFabricOperatingMemory = _JnxFabricOperatingMemory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 15),
    _JnxFabricOperatingMemory_Type()
)
jnxFabricOperatingMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingMemory.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricOperatingMemory.setUnits("Megabytes")


class _JnxFabricOperatingStateOrdered_Type(Integer32):
    """Custom type jnxFabricOperatingStateOrdered based on Integer32"""
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


_JnxFabricOperatingStateOrdered_Type.__name__ = "Integer32"
_JnxFabricOperatingStateOrdered_Object = MibTableColumn
jnxFabricOperatingStateOrdered = _JnxFabricOperatingStateOrdered_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 16),
    _JnxFabricOperatingStateOrdered_Type()
)
jnxFabricOperatingStateOrdered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingStateOrdered.setStatus("current")
_JnxFabricOperatingChassisId_Type = JnxChassisId
_JnxFabricOperatingChassisId_Object = MibTableColumn
jnxFabricOperatingChassisId = _JnxFabricOperatingChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 17),
    _JnxFabricOperatingChassisId_Type()
)
jnxFabricOperatingChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingChassisId.setStatus("current")


class _JnxFabricOperatingChassisDescr_Type(DisplayString):
    """Custom type jnxFabricOperatingChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricOperatingChassisDescr_Type.__name__ = "DisplayString"
_JnxFabricOperatingChassisDescr_Object = MibTableColumn
jnxFabricOperatingChassisDescr = _JnxFabricOperatingChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 18),
    _JnxFabricOperatingChassisDescr_Type()
)
jnxFabricOperatingChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingChassisDescr.setStatus("current")
_JnxFabricOperatingRestartTime_Type = DateAndTime
_JnxFabricOperatingRestartTime_Object = MibTableColumn
jnxFabricOperatingRestartTime = _JnxFabricOperatingRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 19),
    _JnxFabricOperatingRestartTime_Type()
)
jnxFabricOperatingRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperatingRestartTime.setStatus("current")
_JnxFabricOperating1MinLoadAvg_Type = Integer32
_JnxFabricOperating1MinLoadAvg_Object = MibTableColumn
jnxFabricOperating1MinLoadAvg = _JnxFabricOperating1MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 20),
    _JnxFabricOperating1MinLoadAvg_Type()
)
jnxFabricOperating1MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperating1MinLoadAvg.setStatus("current")
_JnxFabricOperating5MinLoadAvg_Type = Integer32
_JnxFabricOperating5MinLoadAvg_Object = MibTableColumn
jnxFabricOperating5MinLoadAvg = _JnxFabricOperating5MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 21),
    _JnxFabricOperating5MinLoadAvg_Type()
)
jnxFabricOperating5MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperating5MinLoadAvg.setStatus("current")
_JnxFabricOperating15MinLoadAvg_Type = Integer32
_JnxFabricOperating15MinLoadAvg_Object = MibTableColumn
jnxFabricOperating15MinLoadAvg = _JnxFabricOperating15MinLoadAvg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 5, 1, 22),
    _JnxFabricOperating15MinLoadAvg_Type()
)
jnxFabricOperating15MinLoadAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricOperating15MinLoadAvg.setStatus("current")
_JnxFabricRedundancyTable_Object = MibTable
jnxFabricRedundancyTable = _JnxFabricRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6)
)
if mibBuilder.loadTexts:
    jnxFabricRedundancyTable.setStatus("current")
_JnxFabricRedundancyEntry_Object = MibTableRow
jnxFabricRedundancyEntry = _JnxFabricRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1)
)
jnxFabricRedundancyEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyContentsIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL1Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL2Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL3Index"),
)
if mibBuilder.loadTexts:
    jnxFabricRedundancyEntry.setStatus("current")


class _JnxFabricRedundancyContentsIndex_Type(Integer32):
    """Custom type jnxFabricRedundancyContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricRedundancyContentsIndex_Type.__name__ = "Integer32"
_JnxFabricRedundancyContentsIndex_Object = MibTableColumn
jnxFabricRedundancyContentsIndex = _JnxFabricRedundancyContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 1),
    _JnxFabricRedundancyContentsIndex_Type()
)
jnxFabricRedundancyContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyContentsIndex.setStatus("current")


class _JnxFabricRedundancyL1Index_Type(Integer32):
    """Custom type jnxFabricRedundancyL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricRedundancyL1Index_Type.__name__ = "Integer32"
_JnxFabricRedundancyL1Index_Object = MibTableColumn
jnxFabricRedundancyL1Index = _JnxFabricRedundancyL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 2),
    _JnxFabricRedundancyL1Index_Type()
)
jnxFabricRedundancyL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyL1Index.setStatus("current")


class _JnxFabricRedundancyL2Index_Type(Integer32):
    """Custom type jnxFabricRedundancyL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricRedundancyL2Index_Type.__name__ = "Integer32"
_JnxFabricRedundancyL2Index_Object = MibTableColumn
jnxFabricRedundancyL2Index = _JnxFabricRedundancyL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 3),
    _JnxFabricRedundancyL2Index_Type()
)
jnxFabricRedundancyL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyL2Index.setStatus("current")


class _JnxFabricRedundancyL3Index_Type(Integer32):
    """Custom type jnxFabricRedundancyL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricRedundancyL3Index_Type.__name__ = "Integer32"
_JnxFabricRedundancyL3Index_Object = MibTableColumn
jnxFabricRedundancyL3Index = _JnxFabricRedundancyL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 4),
    _JnxFabricRedundancyL3Index_Type()
)
jnxFabricRedundancyL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyL3Index.setStatus("current")


class _JnxFabricRedundancyDescr_Type(DisplayString):
    """Custom type jnxFabricRedundancyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricRedundancyDescr_Type.__name__ = "DisplayString"
_JnxFabricRedundancyDescr_Object = MibTableColumn
jnxFabricRedundancyDescr = _JnxFabricRedundancyDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 5),
    _JnxFabricRedundancyDescr_Type()
)
jnxFabricRedundancyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyDescr.setStatus("current")


class _JnxFabricRedundancyConfig_Type(Integer32):
    """Custom type jnxFabricRedundancyConfig based on Integer32"""
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


_JnxFabricRedundancyConfig_Type.__name__ = "Integer32"
_JnxFabricRedundancyConfig_Object = MibTableColumn
jnxFabricRedundancyConfig = _JnxFabricRedundancyConfig_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 6),
    _JnxFabricRedundancyConfig_Type()
)
jnxFabricRedundancyConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyConfig.setStatus("current")


class _JnxFabricRedundancyState_Type(Integer32):
    """Custom type jnxFabricRedundancyState based on Integer32"""
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


_JnxFabricRedundancyState_Type.__name__ = "Integer32"
_JnxFabricRedundancyState_Object = MibTableColumn
jnxFabricRedundancyState = _JnxFabricRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 7),
    _JnxFabricRedundancyState_Type()
)
jnxFabricRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyState.setStatus("current")
_JnxFabricRedundancySwitchoverCount_Type = Counter32
_JnxFabricRedundancySwitchoverCount_Object = MibTableColumn
jnxFabricRedundancySwitchoverCount = _JnxFabricRedundancySwitchoverCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 8),
    _JnxFabricRedundancySwitchoverCount_Type()
)
jnxFabricRedundancySwitchoverCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancySwitchoverCount.setStatus("current")
_JnxFabricRedundancySwitchoverTime_Type = TimeTicks
_JnxFabricRedundancySwitchoverTime_Object = MibTableColumn
jnxFabricRedundancySwitchoverTime = _JnxFabricRedundancySwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 9),
    _JnxFabricRedundancySwitchoverTime_Type()
)
jnxFabricRedundancySwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancySwitchoverTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricRedundancySwitchoverTime.setUnits("centi-seconds")


class _JnxFabricRedundancySwitchoverReason_Type(Integer32):
    """Custom type jnxFabricRedundancySwitchoverReason based on Integer32"""
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


_JnxFabricRedundancySwitchoverReason_Type.__name__ = "Integer32"
_JnxFabricRedundancySwitchoverReason_Object = MibTableColumn
jnxFabricRedundancySwitchoverReason = _JnxFabricRedundancySwitchoverReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 10),
    _JnxFabricRedundancySwitchoverReason_Type()
)
jnxFabricRedundancySwitchoverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancySwitchoverReason.setStatus("current")
_JnxFabricRedundancyKeepaliveHeartbeat_Type = Integer32
_JnxFabricRedundancyKeepaliveHeartbeat_Object = MibTableColumn
jnxFabricRedundancyKeepaliveHeartbeat = _JnxFabricRedundancyKeepaliveHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 11),
    _JnxFabricRedundancyKeepaliveHeartbeat_Type()
)
jnxFabricRedundancyKeepaliveHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyKeepaliveHeartbeat.setStatus("current")
_JnxFabricRedundancyKeepaliveTimeout_Type = Integer32
_JnxFabricRedundancyKeepaliveTimeout_Object = MibTableColumn
jnxFabricRedundancyKeepaliveTimeout = _JnxFabricRedundancyKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 12),
    _JnxFabricRedundancyKeepaliveTimeout_Type()
)
jnxFabricRedundancyKeepaliveTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyKeepaliveTimeout.setStatus("current")
_JnxFabricRedundancyKeepaliveElapsed_Type = Integer32
_JnxFabricRedundancyKeepaliveElapsed_Object = MibTableColumn
jnxFabricRedundancyKeepaliveElapsed = _JnxFabricRedundancyKeepaliveElapsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 13),
    _JnxFabricRedundancyKeepaliveElapsed_Type()
)
jnxFabricRedundancyKeepaliveElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyKeepaliveElapsed.setStatus("current")
_JnxFabricRedundancyKeepaliveLoss_Type = Counter32
_JnxFabricRedundancyKeepaliveLoss_Object = MibTableColumn
jnxFabricRedundancyKeepaliveLoss = _JnxFabricRedundancyKeepaliveLoss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 14),
    _JnxFabricRedundancyKeepaliveLoss_Type()
)
jnxFabricRedundancyKeepaliveLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyKeepaliveLoss.setStatus("current")
_JnxFabricRedundancyChassisId_Type = JnxChassisId
_JnxFabricRedundancyChassisId_Object = MibTableColumn
jnxFabricRedundancyChassisId = _JnxFabricRedundancyChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 15),
    _JnxFabricRedundancyChassisId_Type()
)
jnxFabricRedundancyChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyChassisId.setStatus("current")


class _JnxFabricRedundancyChassisDescr_Type(DisplayString):
    """Custom type jnxFabricRedundancyChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricRedundancyChassisDescr_Type.__name__ = "DisplayString"
_JnxFabricRedundancyChassisDescr_Object = MibTableColumn
jnxFabricRedundancyChassisDescr = _JnxFabricRedundancyChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 6, 1, 16),
    _JnxFabricRedundancyChassisDescr_Type()
)
jnxFabricRedundancyChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricRedundancyChassisDescr.setStatus("current")
_JnxFabricFruTable_Object = MibTable
jnxFabricFruTable = _JnxFabricFruTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7)
)
if mibBuilder.loadTexts:
    jnxFabricFruTable.setStatus("current")
_JnxFabricFruEntry_Object = MibTableRow
jnxFabricFruEntry = _JnxFabricFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1)
)
jnxFabricFruEntry.setIndexNames(
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
    (0, "JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
)
if mibBuilder.loadTexts:
    jnxFabricFruEntry.setStatus("current")


class _JnxFabricFruContentsIndex_Type(Integer32):
    """Custom type jnxFabricFruContentsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JnxFabricFruContentsIndex_Type.__name__ = "Integer32"
_JnxFabricFruContentsIndex_Object = MibTableColumn
jnxFabricFruContentsIndex = _JnxFabricFruContentsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 1),
    _JnxFabricFruContentsIndex_Type()
)
jnxFabricFruContentsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruContentsIndex.setStatus("current")


class _JnxFabricFruL1Index_Type(Integer32):
    """Custom type jnxFabricFruL1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFruL1Index_Type.__name__ = "Integer32"
_JnxFabricFruL1Index_Object = MibTableColumn
jnxFabricFruL1Index = _JnxFabricFruL1Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 2),
    _JnxFabricFruL1Index_Type()
)
jnxFabricFruL1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruL1Index.setStatus("current")


class _JnxFabricFruL2Index_Type(Integer32):
    """Custom type jnxFabricFruL2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFruL2Index_Type.__name__ = "Integer32"
_JnxFabricFruL2Index_Object = MibTableColumn
jnxFabricFruL2Index = _JnxFabricFruL2Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 3),
    _JnxFabricFruL2Index_Type()
)
jnxFabricFruL2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruL2Index.setStatus("current")


class _JnxFabricFruL3Index_Type(Integer32):
    """Custom type jnxFabricFruL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFruL3Index_Type.__name__ = "Integer32"
_JnxFabricFruL3Index_Object = MibTableColumn
jnxFabricFruL3Index = _JnxFabricFruL3Index_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 4),
    _JnxFabricFruL3Index_Type()
)
jnxFabricFruL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruL3Index.setStatus("current")


class _JnxFabricFruName_Type(DisplayString):
    """Custom type jnxFabricFruName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricFruName_Type.__name__ = "DisplayString"
_JnxFabricFruName_Object = MibTableColumn
jnxFabricFruName = _JnxFabricFruName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 5),
    _JnxFabricFruName_Type()
)
jnxFabricFruName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruName.setStatus("current")


class _JnxFabricFruType_Type(Integer32):
    """Custom type jnxFabricFruType based on Integer32"""
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


_JnxFabricFruType_Type.__name__ = "Integer32"
_JnxFabricFruType_Object = MibTableColumn
jnxFabricFruType = _JnxFabricFruType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 6),
    _JnxFabricFruType_Type()
)
jnxFabricFruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruType.setStatus("current")


class _JnxFabricFruSlot_Type(Integer32):
    """Custom type jnxFabricFruSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxFabricFruSlot_Type.__name__ = "Integer32"
_JnxFabricFruSlot_Object = MibTableColumn
jnxFabricFruSlot = _JnxFabricFruSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 7),
    _JnxFabricFruSlot_Type()
)
jnxFabricFruSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruSlot.setStatus("current")


class _JnxFabricFruState_Type(Integer32):
    """Custom type jnxFabricFruState based on Integer32"""
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


_JnxFabricFruState_Type.__name__ = "Integer32"
_JnxFabricFruState_Object = MibTableColumn
jnxFabricFruState = _JnxFabricFruState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 8),
    _JnxFabricFruState_Type()
)
jnxFabricFruState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruState.setStatus("current")
_JnxFabricFruTemp_Type = Integer32
_JnxFabricFruTemp_Object = MibTableColumn
jnxFabricFruTemp = _JnxFabricFruTemp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 9),
    _JnxFabricFruTemp_Type()
)
jnxFabricFruTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruTemp.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricFruTemp.setUnits("Celsius (degrees C)")


class _JnxFabricFruOfflineReason_Type(Integer32):
    """Custom type jnxFabricFruOfflineReason based on Integer32"""
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
              74,
              75)
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
          ("fruFPCReducedFabricBW", 75),
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


_JnxFabricFruOfflineReason_Type.__name__ = "Integer32"
_JnxFabricFruOfflineReason_Object = MibTableColumn
jnxFabricFruOfflineReason = _JnxFabricFruOfflineReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 10),
    _JnxFabricFruOfflineReason_Type()
)
jnxFabricFruOfflineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruOfflineReason.setStatus("current")
_JnxFabricFruLastPowerOff_Type = TimeTicks
_JnxFabricFruLastPowerOff_Object = MibTableColumn
jnxFabricFruLastPowerOff = _JnxFabricFruLastPowerOff_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 11),
    _JnxFabricFruLastPowerOff_Type()
)
jnxFabricFruLastPowerOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruLastPowerOff.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricFruLastPowerOff.setUnits("centi-seconds")
_JnxFabricFruLastPowerOn_Type = TimeTicks
_JnxFabricFruLastPowerOn_Object = MibTableColumn
jnxFabricFruLastPowerOn = _JnxFabricFruLastPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 12),
    _JnxFabricFruLastPowerOn_Type()
)
jnxFabricFruLastPowerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruLastPowerOn.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricFruLastPowerOn.setUnits("centi-seconds")
_JnxFabricFruPowerUpTime_Type = TimeTicks
_JnxFabricFruPowerUpTime_Object = MibTableColumn
jnxFabricFruPowerUpTime = _JnxFabricFruPowerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 13),
    _JnxFabricFruPowerUpTime_Type()
)
jnxFabricFruPowerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruPowerUpTime.setStatus("current")
if mibBuilder.loadTexts:
    jnxFabricFruPowerUpTime.setUnits("centi-seconds")
_JnxFabricFruChassisId_Type = JnxChassisId
_JnxFabricFruChassisId_Object = MibTableColumn
jnxFabricFruChassisId = _JnxFabricFruChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 14),
    _JnxFabricFruChassisId_Type()
)
jnxFabricFruChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruChassisId.setStatus("current")


class _JnxFabricFruChassisDescr_Type(DisplayString):
    """Custom type jnxFabricFruChassisDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JnxFabricFruChassisDescr_Type.__name__ = "DisplayString"
_JnxFabricFruChassisDescr_Object = MibTableColumn
jnxFabricFruChassisDescr = _JnxFabricFruChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 15),
    _JnxFabricFruChassisDescr_Type()
)
jnxFabricFruChassisDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruChassisDescr.setStatus("current")


class _JnxFabricFruPsdAssignment_Type(Integer32):
    """Custom type jnxFabricFruPsdAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_JnxFabricFruPsdAssignment_Type.__name__ = "Integer32"
_JnxFabricFruPsdAssignment_Object = MibTableColumn
jnxFabricFruPsdAssignment = _JnxFabricFruPsdAssignment_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 42, 2, 2, 7, 1, 16),
    _JnxFabricFruPsdAssignment_Type()
)
jnxFabricFruPsdAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxFabricFruPsdAssignment.setStatus("current")

# Managed Objects groups


# Notification objects

jnxFabricPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 1)
)
jnxFabricPowerSupplyFailure.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFabricPowerSupplyFailure.setStatus(
        "current"
    )

jnxFabricFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 2)
)
jnxFabricFanFailure.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFabricFanFailure.setStatus(
        "current"
    )

jnxFabricOverTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 3)
)
jnxFabricOverTemperature.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingTemp"))
)
if mibBuilder.loadTexts:
    jnxFabricOverTemperature.setStatus(
        "current"
    )

jnxFabricRedundancySwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 4)
)
jnxFabricRedundancySwitchover.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyConfig"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancyState"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancySwitchoverCount"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancySwitchoverTime"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricRedundancySwitchoverReason"))
)
if mibBuilder.loadTexts:
    jnxFabricRedundancySwitchover.setStatus(
        "current"
    )

jnxFabricFruRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 5)
)
jnxFabricFruRemoval.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruRemoval.setStatus(
        "current"
    )

jnxFabricFruInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 6)
)
jnxFabricFruInsertion.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruInsertion.setStatus(
        "current"
    )

jnxFabricFruPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 7)
)
jnxFabricFruPowerOff.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruOfflineReason"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOff"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFabricFruPowerOff.setStatus(
        "current"
    )

jnxFabricFruPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 8)
)
jnxFabricFruPowerOn.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruOfflineReason"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOff"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFabricFruPowerOn.setStatus(
        "current"
    )

jnxFabricFruFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 9)
)
jnxFabricFruFailed.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruFailed.setStatus(
        "current"
    )

jnxFabricFruOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 10)
)
jnxFabricFruOffline.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruOfflineReason"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOff"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruLastPowerOn"))
)
if mibBuilder.loadTexts:
    jnxFabricFruOffline.setStatus(
        "current"
    )

jnxFabricFruOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 11)
)
jnxFabricFruOnline.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruOnline.setStatus(
        "current"
    )

jnxFabricFruCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 12)
)
jnxFabricFruCheck.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruCheck.setStatus(
        "current"
    )

jnxFabricFEBSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 13)
)
jnxFabricFEBSwitchover.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFEBSwitchover.setStatus(
        "current"
    )

jnxFabricHardDiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 14)
)
jnxFabricHardDiskFailed.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricHardDiskFailed.setStatus(
        "current"
    )

jnxFabricHardDiskMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 15)
)
jnxFabricHardDiskMissing.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricHardDiskMissing.setStatus(
        "current"
    )

jnxFabricBootFromBackup = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 19, 16)
)
jnxFabricBootFromBackup.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricBootFromBackup.setStatus(
        "current"
    )

jnxFabricPowerSupplyOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 20, 1)
)
jnxFabricPowerSupplyOK.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFabricPowerSupplyOK.setStatus(
        "current"
    )

jnxFabricFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 20, 2)
)
jnxFabricFanOK.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingState"))
)
if mibBuilder.loadTexts:
    jnxFabricFanOK.setStatus(
        "current"
    )

jnxFabricTemperatureOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 20, 3)
)
jnxFabricTemperatureOK.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsContainerIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricContentsDescr"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricOperatingTemp"))
)
if mibBuilder.loadTexts:
    jnxFabricTemperatureOK.setStatus(
        "current"
    )

jnxFabricFruOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 20, 4)
)
jnxFabricFruOK.setObjects(
      *(("JUNIPER-FABRIC-CHASSIS", "jnxFabricDeviceIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruContentsIndex"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL1Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL2Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruL3Index"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruName"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruType"),
        ("JUNIPER-FABRIC-CHASSIS", "jnxFabricFruSlot"))
)
if mibBuilder.loadTexts:
    jnxFabricFruOK.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-FABRIC-CHASSIS",
    **{"JnxFabricDeviceId": JnxFabricDeviceId,
       "JnxFabricContainersFamily": JnxFabricContainersFamily,
       "jnxFabricAnatomy": jnxFabricAnatomy,
       "jnxFabricAnatomyScalars": jnxFabricAnatomyScalars,
       "jnxFabricClass": jnxFabricClass,
       "jnxFabricDescr": jnxFabricDescr,
       "jnxFabricSerialNo": jnxFabricSerialNo,
       "jnxFabricRevision": jnxFabricRevision,
       "jnxFabricFirmwareRevision": jnxFabricFirmwareRevision,
       "jnxFabricLastInstalled": jnxFabricLastInstalled,
       "jnxFabricContentsLastChange": jnxFabricContentsLastChange,
       "jnxFabricFilledLastChange": jnxFabricFilledLastChange,
       "jnxFabricAnatomyTables": jnxFabricAnatomyTables,
       "jnxFabricDeviceTable": jnxFabricDeviceTable,
       "jnxFabricDeviceEntry": jnxFabricDeviceEntry,
       "jnxFabricDeviceIndex": jnxFabricDeviceIndex,
       "jnxFabricDeviceEntryContainersFamily": jnxFabricDeviceEntryContainersFamily,
       "jnxFabricDeviceEntryClass": jnxFabricDeviceEntryClass,
       "jnxFabricDeviceEntryModel": jnxFabricDeviceEntryModel,
       "jnxFabricDeviceEntryDescr": jnxFabricDeviceEntryDescr,
       "jnxFabricDeviceEntrySerialNo": jnxFabricDeviceEntrySerialNo,
       "jnxFabricDeviceEntryName": jnxFabricDeviceEntryName,
       "jnxFabricDeviceEntryRevision": jnxFabricDeviceEntryRevision,
       "jnxFabricDeviceEntryFirmwareRevision": jnxFabricDeviceEntryFirmwareRevision,
       "jnxFabricDeviceEntryInstalled": jnxFabricDeviceEntryInstalled,
       "jnxFabricDeviceEntryContentsLastChange": jnxFabricDeviceEntryContentsLastChange,
       "jnxFabricDeviceEntryFilledLastChange": jnxFabricDeviceEntryFilledLastChange,
       "jnxFabricDeviceEntryKernelMemoryUsedPercent": jnxFabricDeviceEntryKernelMemoryUsedPercent,
       "jnxFabricContainersTable": jnxFabricContainersTable,
       "jnxFabricContainersEntry": jnxFabricContainersEntry,
       "jnxFabricContainersFamily": jnxFabricContainersFamily,
       "jnxFabricContainersIndex": jnxFabricContainersIndex,
       "jnxFabricContainersView": jnxFabricContainersView,
       "jnxFabricContainersLevel": jnxFabricContainersLevel,
       "jnxFabricContainersWithin": jnxFabricContainersWithin,
       "jnxFabricContainersType": jnxFabricContainersType,
       "jnxFabricContainersDescr": jnxFabricContainersDescr,
       "jnxFabricContainersCount": jnxFabricContainersCount,
       "jnxFabricContentsTable": jnxFabricContentsTable,
       "jnxFabricContentsEntry": jnxFabricContentsEntry,
       "jnxFabricContentsContainerIndex": jnxFabricContentsContainerIndex,
       "jnxFabricContentsL1Index": jnxFabricContentsL1Index,
       "jnxFabricContentsL2Index": jnxFabricContentsL2Index,
       "jnxFabricContentsL3Index": jnxFabricContentsL3Index,
       "jnxFabricContentsType": jnxFabricContentsType,
       "jnxFabricContentsDescr": jnxFabricContentsDescr,
       "jnxFabricContentsSerialNo": jnxFabricContentsSerialNo,
       "jnxFabricContentsRevision": jnxFabricContentsRevision,
       "jnxFabricContentsInstalled": jnxFabricContentsInstalled,
       "jnxFabricContentsPartNo": jnxFabricContentsPartNo,
       "jnxFabricContentsChassisId": jnxFabricContentsChassisId,
       "jnxFabricContentsChassisDescr": jnxFabricContentsChassisDescr,
       "jnxFabricContentsChassisCleiCode": jnxFabricContentsChassisCleiCode,
       "jnxFabricFilledTable": jnxFabricFilledTable,
       "jnxFabricFilledEntry": jnxFabricFilledEntry,
       "jnxFabricFilledContainerIndex": jnxFabricFilledContainerIndex,
       "jnxFabricFilledL1Index": jnxFabricFilledL1Index,
       "jnxFabricFilledL2Index": jnxFabricFilledL2Index,
       "jnxFabricFilledL3Index": jnxFabricFilledL3Index,
       "jnxFabricFilledDescr": jnxFabricFilledDescr,
       "jnxFabricFilledState": jnxFabricFilledState,
       "jnxFabricFilledChassisId": jnxFabricFilledChassisId,
       "jnxFabricFilledChassisDescr": jnxFabricFilledChassisDescr,
       "jnxFabricOperatingTable": jnxFabricOperatingTable,
       "jnxFabricOperatingEntry": jnxFabricOperatingEntry,
       "jnxFabricOperatingContentsIndex": jnxFabricOperatingContentsIndex,
       "jnxFabricOperatingL1Index": jnxFabricOperatingL1Index,
       "jnxFabricOperatingL2Index": jnxFabricOperatingL2Index,
       "jnxFabricOperatingL3Index": jnxFabricOperatingL3Index,
       "jnxFabricOperatingDescr": jnxFabricOperatingDescr,
       "jnxFabricOperatingState": jnxFabricOperatingState,
       "jnxFabricOperatingTemp": jnxFabricOperatingTemp,
       "jnxFabricOperatingCPU": jnxFabricOperatingCPU,
       "jnxFabricOperatingISR": jnxFabricOperatingISR,
       "jnxFabricOperatingDRAMSize": jnxFabricOperatingDRAMSize,
       "jnxFabricOperatingBuffer": jnxFabricOperatingBuffer,
       "jnxFabricOperatingHeap": jnxFabricOperatingHeap,
       "jnxFabricOperatingUpTime": jnxFabricOperatingUpTime,
       "jnxFabricOperatingLastRestart": jnxFabricOperatingLastRestart,
       "jnxFabricOperatingMemory": jnxFabricOperatingMemory,
       "jnxFabricOperatingStateOrdered": jnxFabricOperatingStateOrdered,
       "jnxFabricOperatingChassisId": jnxFabricOperatingChassisId,
       "jnxFabricOperatingChassisDescr": jnxFabricOperatingChassisDescr,
       "jnxFabricOperatingRestartTime": jnxFabricOperatingRestartTime,
       "jnxFabricOperating1MinLoadAvg": jnxFabricOperating1MinLoadAvg,
       "jnxFabricOperating5MinLoadAvg": jnxFabricOperating5MinLoadAvg,
       "jnxFabricOperating15MinLoadAvg": jnxFabricOperating15MinLoadAvg,
       "jnxFabricRedundancyTable": jnxFabricRedundancyTable,
       "jnxFabricRedundancyEntry": jnxFabricRedundancyEntry,
       "jnxFabricRedundancyContentsIndex": jnxFabricRedundancyContentsIndex,
       "jnxFabricRedundancyL1Index": jnxFabricRedundancyL1Index,
       "jnxFabricRedundancyL2Index": jnxFabricRedundancyL2Index,
       "jnxFabricRedundancyL3Index": jnxFabricRedundancyL3Index,
       "jnxFabricRedundancyDescr": jnxFabricRedundancyDescr,
       "jnxFabricRedundancyConfig": jnxFabricRedundancyConfig,
       "jnxFabricRedundancyState": jnxFabricRedundancyState,
       "jnxFabricRedundancySwitchoverCount": jnxFabricRedundancySwitchoverCount,
       "jnxFabricRedundancySwitchoverTime": jnxFabricRedundancySwitchoverTime,
       "jnxFabricRedundancySwitchoverReason": jnxFabricRedundancySwitchoverReason,
       "jnxFabricRedundancyKeepaliveHeartbeat": jnxFabricRedundancyKeepaliveHeartbeat,
       "jnxFabricRedundancyKeepaliveTimeout": jnxFabricRedundancyKeepaliveTimeout,
       "jnxFabricRedundancyKeepaliveElapsed": jnxFabricRedundancyKeepaliveElapsed,
       "jnxFabricRedundancyKeepaliveLoss": jnxFabricRedundancyKeepaliveLoss,
       "jnxFabricRedundancyChassisId": jnxFabricRedundancyChassisId,
       "jnxFabricRedundancyChassisDescr": jnxFabricRedundancyChassisDescr,
       "jnxFabricFruTable": jnxFabricFruTable,
       "jnxFabricFruEntry": jnxFabricFruEntry,
       "jnxFabricFruContentsIndex": jnxFabricFruContentsIndex,
       "jnxFabricFruL1Index": jnxFabricFruL1Index,
       "jnxFabricFruL2Index": jnxFabricFruL2Index,
       "jnxFabricFruL3Index": jnxFabricFruL3Index,
       "jnxFabricFruName": jnxFabricFruName,
       "jnxFabricFruType": jnxFabricFruType,
       "jnxFabricFruSlot": jnxFabricFruSlot,
       "jnxFabricFruState": jnxFabricFruState,
       "jnxFabricFruTemp": jnxFabricFruTemp,
       "jnxFabricFruOfflineReason": jnxFabricFruOfflineReason,
       "jnxFabricFruLastPowerOff": jnxFabricFruLastPowerOff,
       "jnxFabricFruLastPowerOn": jnxFabricFruLastPowerOn,
       "jnxFabricFruPowerUpTime": jnxFabricFruPowerUpTime,
       "jnxFabricFruChassisId": jnxFabricFruChassisId,
       "jnxFabricFruChassisDescr": jnxFabricFruChassisDescr,
       "jnxFabricFruPsdAssignment": jnxFabricFruPsdAssignment,
       "jnxFabricPowerSupplyFailure": jnxFabricPowerSupplyFailure,
       "jnxFabricFanFailure": jnxFabricFanFailure,
       "jnxFabricOverTemperature": jnxFabricOverTemperature,
       "jnxFabricRedundancySwitchover": jnxFabricRedundancySwitchover,
       "jnxFabricFruRemoval": jnxFabricFruRemoval,
       "jnxFabricFruInsertion": jnxFabricFruInsertion,
       "jnxFabricFruPowerOff": jnxFabricFruPowerOff,
       "jnxFabricFruPowerOn": jnxFabricFruPowerOn,
       "jnxFabricFruFailed": jnxFabricFruFailed,
       "jnxFabricFruOffline": jnxFabricFruOffline,
       "jnxFabricFruOnline": jnxFabricFruOnline,
       "jnxFabricFruCheck": jnxFabricFruCheck,
       "jnxFabricFEBSwitchover": jnxFabricFEBSwitchover,
       "jnxFabricHardDiskFailed": jnxFabricHardDiskFailed,
       "jnxFabricHardDiskMissing": jnxFabricHardDiskMissing,
       "jnxFabricBootFromBackup": jnxFabricBootFromBackup,
       "jnxFabricPowerSupplyOK": jnxFabricPowerSupplyOK,
       "jnxFabricFanOK": jnxFabricFanOK,
       "jnxFabricTemperatureOK": jnxFabricTemperatureOK,
       "jnxFabricFruOK": jnxFabricFruOK}
)
