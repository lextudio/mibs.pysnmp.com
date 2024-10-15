# SNMP MIB module (TPT-MULTIDV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-MULTIDV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:59 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(policyDVObjs,) = mibBuilder.importSymbols(
    "TPT-POLICY-MIB",
    "policyDVObjs")


# MODULE-IDENTITY

tpt_multidv_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2)
)
tpt_multidv_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DVIsActive(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )



# MIB Managed Objects in the order of their OIDs

_InstalledDVTable_Object = MibTable
installedDVTable = _InstalledDVTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    installedDVTable.setStatus("current")
_InstalledDVEntry_Object = MibTableRow
installedDVEntry = _InstalledDVEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1)
)
installedDVEntry.setIndexNames(
    (0, "TPT-MULTIDV-MIB", "installedDVIndex"),
)
if mibBuilder.loadTexts:
    installedDVEntry.setStatus("current")
_InstalledDVIndex_Type = Unsigned32
_InstalledDVIndex_Object = MibTableColumn
installedDVIndex = _InstalledDVIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 1),
    _InstalledDVIndex_Type()
)
installedDVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    installedDVIndex.setStatus("current")


class _InstalledDVVersion_Type(OctetString):
    """Custom type installedDVVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_InstalledDVVersion_Type.__name__ = "OctetString"
_InstalledDVVersion_Object = MibTableColumn
installedDVVersion = _InstalledDVVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 2),
    _InstalledDVVersion_Type()
)
installedDVVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedDVVersion.setStatus("current")
_InstalledDVIsActive_Type = DVIsActive
_InstalledDVIsActive_Object = MibTableColumn
installedDVIsActive = _InstalledDVIsActive_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 3),
    _InstalledDVIsActive_Type()
)
installedDVIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    installedDVIsActive.setStatus("current")
_AuxiliaryDVTable_Object = MibTable
auxiliaryDVTable = _AuxiliaryDVTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    auxiliaryDVTable.setStatus("current")
_AuxiliaryDVEntry_Object = MibTableRow
auxiliaryDVEntry = _AuxiliaryDVEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1)
)
auxiliaryDVEntry.setIndexNames(
    (0, "TPT-MULTIDV-MIB", "auxiliaryDVIndex"),
)
if mibBuilder.loadTexts:
    auxiliaryDVEntry.setStatus("current")
_AuxiliaryDVIndex_Type = Unsigned32
_AuxiliaryDVIndex_Object = MibTableColumn
auxiliaryDVIndex = _AuxiliaryDVIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 1),
    _AuxiliaryDVIndex_Type()
)
auxiliaryDVIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auxiliaryDVIndex.setStatus("current")


class _AuxiliaryDVType_Type(OctetString):
    """Custom type auxiliaryDVType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 49),
    )


_AuxiliaryDVType_Type.__name__ = "OctetString"
_AuxiliaryDVType_Object = MibTableColumn
auxiliaryDVType = _AuxiliaryDVType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 2),
    _AuxiliaryDVType_Type()
)
auxiliaryDVType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDVType.setStatus("current")


class _AuxiliaryDVName_Type(OctetString):
    """Custom type auxiliaryDVName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuxiliaryDVName_Type.__name__ = "OctetString"
_AuxiliaryDVName_Object = MibTableColumn
auxiliaryDVName = _AuxiliaryDVName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 3),
    _AuxiliaryDVName_Type()
)
auxiliaryDVName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDVName.setStatus("current")
_AuxiliaryDVVersion_Type = Integer32
_AuxiliaryDVVersion_Object = MibTableColumn
auxiliaryDVVersion = _AuxiliaryDVVersion_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 4),
    _AuxiliaryDVVersion_Type()
)
auxiliaryDVVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDVVersion.setStatus("current")


class _AuxiliaryDVPackage_Type(OctetString):
    """Custom type auxiliaryDVPackage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AuxiliaryDVPackage_Type.__name__ = "OctetString"
_AuxiliaryDVPackage_Object = MibTableColumn
auxiliaryDVPackage = _AuxiliaryDVPackage_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 5),
    _AuxiliaryDVPackage_Type()
)
auxiliaryDVPackage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auxiliaryDVPackage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-MULTIDV-MIB",
    **{"DVIsActive": DVIsActive,
       "tpt-multidv-objs": tpt_multidv_objs,
       "installedDVTable": installedDVTable,
       "installedDVEntry": installedDVEntry,
       "installedDVIndex": installedDVIndex,
       "installedDVVersion": installedDVVersion,
       "installedDVIsActive": installedDVIsActive,
       "auxiliaryDVTable": auxiliaryDVTable,
       "auxiliaryDVEntry": auxiliaryDVEntry,
       "auxiliaryDVIndex": auxiliaryDVIndex,
       "auxiliaryDVType": auxiliaryDVType,
       "auxiliaryDVName": auxiliaryDVName,
       "auxiliaryDVVersion": auxiliaryDVVersion,
       "auxiliaryDVPackage": auxiliaryDVPackage}
)
