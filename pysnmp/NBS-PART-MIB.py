# SNMP MIB module (NBS-PART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-PART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:57 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(NbsTcPartIndex,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcPartIndex",
    "nbs")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nbsPartMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 231)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsPartHardGrp_ObjectIdentity = ObjectIdentity
nbsPartHardGrp = _NbsPartHardGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 231, 1)
)
if mibBuilder.loadTexts:
    nbsPartHardGrp.setStatus("current")
_NbsPartHardTable_Object = MibTable
nbsPartHardTable = _NbsPartHardTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1)
)
if mibBuilder.loadTexts:
    nbsPartHardTable.setStatus("current")
_NbsPartHardEntry_Object = MibTableRow
nbsPartHardEntry = _NbsPartHardEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1)
)
nbsPartHardEntry.setIndexNames(
    (0, "NBS-PART-MIB", "nbsPartHardIfIndex"),
    (0, "NBS-PART-MIB", "nbsPartHardPartIndex"),
)
if mibBuilder.loadTexts:
    nbsPartHardEntry.setStatus("current")
_NbsPartHardIfIndex_Type = InterfaceIndex
_NbsPartHardIfIndex_Object = MibTableColumn
nbsPartHardIfIndex = _NbsPartHardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 1),
    _NbsPartHardIfIndex_Type()
)
nbsPartHardIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartHardIfIndex.setStatus("current")
_NbsPartHardPartIndex_Type = NbsTcPartIndex
_NbsPartHardPartIndex_Object = MibTableColumn
nbsPartHardPartIndex = _NbsPartHardPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 2),
    _NbsPartHardPartIndex_Type()
)
nbsPartHardPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartHardPartIndex.setStatus("current")


class _NbsPartHardDescription_Type(DisplayString):
    """Custom type nbsPartHardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsPartHardDescription_Type.__name__ = "DisplayString"
_NbsPartHardDescription_Object = MibTableColumn
nbsPartHardDescription = _NbsPartHardDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 10),
    _NbsPartHardDescription_Type()
)
nbsPartHardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardDescription.setStatus("current")


class _NbsPartHardSerialNumber_Type(DisplayString):
    """Custom type nbsPartHardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsPartHardSerialNumber_Type.__name__ = "DisplayString"
_NbsPartHardSerialNumber_Object = MibTableColumn
nbsPartHardSerialNumber = _NbsPartHardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 11),
    _NbsPartHardSerialNumber_Type()
)
nbsPartHardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardSerialNumber.setStatus("current")


class _NbsPartHardProductionId_Type(DisplayString):
    """Custom type nbsPartHardProductionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsPartHardProductionId_Type.__name__ = "DisplayString"
_NbsPartHardProductionId_Object = MibTableColumn
nbsPartHardProductionId = _NbsPartHardProductionId_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 20),
    _NbsPartHardProductionId_Type()
)
nbsPartHardProductionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardProductionId.setStatus("current")


class _NbsPartHardVendor_Type(DisplayString):
    """Custom type nbsPartHardVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsPartHardVendor_Type.__name__ = "DisplayString"
_NbsPartHardVendor_Object = MibTableColumn
nbsPartHardVendor = _NbsPartHardVendor_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 30),
    _NbsPartHardVendor_Type()
)
nbsPartHardVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardVendor.setStatus("current")


class _NbsPartHardModel_Type(DisplayString):
    """Custom type nbsPartHardModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsPartHardModel_Type.__name__ = "DisplayString"
_NbsPartHardModel_Object = MibTableColumn
nbsPartHardModel = _NbsPartHardModel_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 31),
    _NbsPartHardModel_Type()
)
nbsPartHardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardModel.setStatus("current")


class _NbsPartHardWareRev_Type(DisplayString):
    """Custom type nbsPartHardWareRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsPartHardWareRev_Type.__name__ = "DisplayString"
_NbsPartHardWareRev_Object = MibTableColumn
nbsPartHardWareRev = _NbsPartHardWareRev_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 1, 1, 1, 32),
    _NbsPartHardWareRev_Type()
)
nbsPartHardWareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartHardWareRev.setStatus("current")
_NbsPartFirmGrp_ObjectIdentity = ObjectIdentity
nbsPartFirmGrp = _NbsPartFirmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 231, 2)
)
if mibBuilder.loadTexts:
    nbsPartFirmGrp.setStatus("current")
_NbsPartFirmTable_Object = MibTable
nbsPartFirmTable = _NbsPartFirmTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1)
)
if mibBuilder.loadTexts:
    nbsPartFirmTable.setStatus("current")
_NbsPartFirmEntry_Object = MibTableRow
nbsPartFirmEntry = _NbsPartFirmEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1)
)
nbsPartFirmEntry.setIndexNames(
    (0, "NBS-PART-MIB", "nbsPartFirmIfIndex"),
    (0, "NBS-PART-MIB", "nbsPartFirmPartIndex"),
)
if mibBuilder.loadTexts:
    nbsPartFirmEntry.setStatus("current")
_NbsPartFirmIfIndex_Type = InterfaceIndex
_NbsPartFirmIfIndex_Object = MibTableColumn
nbsPartFirmIfIndex = _NbsPartFirmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 1),
    _NbsPartFirmIfIndex_Type()
)
nbsPartFirmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartFirmIfIndex.setStatus("current")
_NbsPartFirmPartIndex_Type = NbsTcPartIndex
_NbsPartFirmPartIndex_Object = MibTableColumn
nbsPartFirmPartIndex = _NbsPartFirmPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 2),
    _NbsPartFirmPartIndex_Type()
)
nbsPartFirmPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartFirmPartIndex.setStatus("current")


class _NbsPartFirmFpgaRev_Type(DisplayString):
    """Custom type nbsPartFirmFpgaRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsPartFirmFpgaRev_Type.__name__ = "DisplayString"
_NbsPartFirmFpgaRev_Object = MibTableColumn
nbsPartFirmFpgaRev = _NbsPartFirmFpgaRev_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 13),
    _NbsPartFirmFpgaRev_Type()
)
nbsPartFirmFpgaRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartFirmFpgaRev.setStatus("current")
_NbsPartFirmSwMajor_Type = Integer32
_NbsPartFirmSwMajor_Object = MibTableColumn
nbsPartFirmSwMajor = _NbsPartFirmSwMajor_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 14),
    _NbsPartFirmSwMajor_Type()
)
nbsPartFirmSwMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartFirmSwMajor.setStatus("current")
_NbsPartFirmSwMinor_Type = Integer32
_NbsPartFirmSwMinor_Object = MibTableColumn
nbsPartFirmSwMinor = _NbsPartFirmSwMinor_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 15),
    _NbsPartFirmSwMinor_Type()
)
nbsPartFirmSwMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartFirmSwMinor.setStatus("current")
_NbsPartFirmSwBuild_Type = Integer32
_NbsPartFirmSwBuild_Object = MibTableColumn
nbsPartFirmSwBuild = _NbsPartFirmSwBuild_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 16),
    _NbsPartFirmSwBuild_Type()
)
nbsPartFirmSwBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartFirmSwBuild.setStatus("current")
_NbsPartFirmWareIndex_Type = Integer32
_NbsPartFirmWareIndex_Object = MibTableColumn
nbsPartFirmWareIndex = _NbsPartFirmWareIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 2, 1, 1, 30),
    _NbsPartFirmWareIndex_Type()
)
nbsPartFirmWareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartFirmWareIndex.setStatus("current")
_NbsPartProgGrp_ObjectIdentity = ObjectIdentity
nbsPartProgGrp = _NbsPartProgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 231, 3)
)
if mibBuilder.loadTexts:
    nbsPartProgGrp.setStatus("current")
_NbsPartProgTable_Object = MibTable
nbsPartProgTable = _NbsPartProgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1)
)
if mibBuilder.loadTexts:
    nbsPartProgTable.setStatus("current")
_NbsPartProgEntry_Object = MibTableRow
nbsPartProgEntry = _NbsPartProgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1)
)
nbsPartProgEntry.setIndexNames(
    (0, "NBS-PART-MIB", "nbsPartProgIfIndex"),
    (0, "NBS-PART-MIB", "nbsPartProgPartIndex"),
)
if mibBuilder.loadTexts:
    nbsPartProgEntry.setStatus("current")
_NbsPartProgIfIndex_Type = InterfaceIndex
_NbsPartProgIfIndex_Object = MibTableColumn
nbsPartProgIfIndex = _NbsPartProgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 1),
    _NbsPartProgIfIndex_Type()
)
nbsPartProgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartProgIfIndex.setStatus("current")
_NbsPartProgPartIndex_Type = NbsTcPartIndex
_NbsPartProgPartIndex_Object = MibTableColumn
nbsPartProgPartIndex = _NbsPartProgPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 2),
    _NbsPartProgPartIndex_Type()
)
nbsPartProgPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsPartProgPartIndex.setStatus("current")


class _NbsPartProgFirmwareCaps_Type(OctetString):
    """Custom type nbsPartProgFirmwareCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsPartProgFirmwareCaps_Type.__name__ = "OctetString"
_NbsPartProgFirmwareCaps_Object = MibTableColumn
nbsPartProgFirmwareCaps = _NbsPartProgFirmwareCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 10),
    _NbsPartProgFirmwareCaps_Type()
)
nbsPartProgFirmwareCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartProgFirmwareCaps.setStatus("current")


class _NbsPartProgFirmwareLoad_Type(OctetString):
    """Custom type nbsPartProgFirmwareLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsPartProgFirmwareLoad_Type.__name__ = "OctetString"
_NbsPartProgFirmwareLoad_Object = MibTableColumn
nbsPartProgFirmwareLoad = _NbsPartProgFirmwareLoad_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 20),
    _NbsPartProgFirmwareLoad_Type()
)
nbsPartProgFirmwareLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPartProgFirmwareLoad.setStatus("current")
_NbsPartProgLoader_Type = Integer32
_NbsPartProgLoader_Object = MibTableColumn
nbsPartProgLoader = _NbsPartProgLoader_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 21),
    _NbsPartProgLoader_Type()
)
nbsPartProgLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartProgLoader.setStatus("current")
_NbsPartProgNVAreaAdmin_Type = Integer32
_NbsPartProgNVAreaAdmin_Object = MibTableColumn
nbsPartProgNVAreaAdmin = _NbsPartProgNVAreaAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 22),
    _NbsPartProgNVAreaAdmin_Type()
)
nbsPartProgNVAreaAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsPartProgNVAreaAdmin.setStatus("current")


class _NbsPartProgNVAreaOper_Type(Integer32):
    """Custom type nbsPartProgNVAreaOper based on Integer32"""
    defaultValue = -1


_NbsPartProgNVAreaOper_Object = MibTableColumn
nbsPartProgNVAreaOper = _NbsPartProgNVAreaOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 23),
    _NbsPartProgNVAreaOper_Type()
)
nbsPartProgNVAreaOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartProgNVAreaOper.setStatus("current")
_NbsPartProgNVAreaStart_Type = Integer32
_NbsPartProgNVAreaStart_Object = MibTableColumn
nbsPartProgNVAreaStart = _NbsPartProgNVAreaStart_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 30),
    _NbsPartProgNVAreaStart_Type()
)
nbsPartProgNVAreaStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartProgNVAreaStart.setStatus("current")
_NbsPartProgNVAreaBanks_Type = Integer32
_NbsPartProgNVAreaBanks_Object = MibTableColumn
nbsPartProgNVAreaBanks = _NbsPartProgNVAreaBanks_Object(
    (1, 3, 6, 1, 4, 1, 629, 231, 3, 1, 1, 31),
    _NbsPartProgNVAreaBanks_Type()
)
nbsPartProgNVAreaBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsPartProgNVAreaBanks.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-PART-MIB",
    **{"nbsPartMib": nbsPartMib,
       "nbsPartHardGrp": nbsPartHardGrp,
       "nbsPartHardTable": nbsPartHardTable,
       "nbsPartHardEntry": nbsPartHardEntry,
       "nbsPartHardIfIndex": nbsPartHardIfIndex,
       "nbsPartHardPartIndex": nbsPartHardPartIndex,
       "nbsPartHardDescription": nbsPartHardDescription,
       "nbsPartHardSerialNumber": nbsPartHardSerialNumber,
       "nbsPartHardProductionId": nbsPartHardProductionId,
       "nbsPartHardVendor": nbsPartHardVendor,
       "nbsPartHardModel": nbsPartHardModel,
       "nbsPartHardWareRev": nbsPartHardWareRev,
       "nbsPartFirmGrp": nbsPartFirmGrp,
       "nbsPartFirmTable": nbsPartFirmTable,
       "nbsPartFirmEntry": nbsPartFirmEntry,
       "nbsPartFirmIfIndex": nbsPartFirmIfIndex,
       "nbsPartFirmPartIndex": nbsPartFirmPartIndex,
       "nbsPartFirmFpgaRev": nbsPartFirmFpgaRev,
       "nbsPartFirmSwMajor": nbsPartFirmSwMajor,
       "nbsPartFirmSwMinor": nbsPartFirmSwMinor,
       "nbsPartFirmSwBuild": nbsPartFirmSwBuild,
       "nbsPartFirmWareIndex": nbsPartFirmWareIndex,
       "nbsPartProgGrp": nbsPartProgGrp,
       "nbsPartProgTable": nbsPartProgTable,
       "nbsPartProgEntry": nbsPartProgEntry,
       "nbsPartProgIfIndex": nbsPartProgIfIndex,
       "nbsPartProgPartIndex": nbsPartProgPartIndex,
       "nbsPartProgFirmwareCaps": nbsPartProgFirmwareCaps,
       "nbsPartProgFirmwareLoad": nbsPartProgFirmwareLoad,
       "nbsPartProgLoader": nbsPartProgLoader,
       "nbsPartProgNVAreaAdmin": nbsPartProgNVAreaAdmin,
       "nbsPartProgNVAreaOper": nbsPartProgNVAreaOper,
       "nbsPartProgNVAreaStart": nbsPartProgNVAreaStart,
       "nbsPartProgNVAreaBanks": nbsPartProgNVAreaBanks}
)
