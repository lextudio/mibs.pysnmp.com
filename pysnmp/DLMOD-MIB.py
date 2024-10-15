# SNMP MIB module (DLMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLMOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:37 2024
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

(ucdavis,) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdavis")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlmod_ObjectIdentity = ObjectIdentity
dlmod = _Dlmod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 14)
)
_DlmodNextIndex_Type = Integer32
_DlmodNextIndex_Object = MibScalar
dlmodNextIndex = _DlmodNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 1),
    _DlmodNextIndex_Type()
)
dlmodNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodNextIndex.setStatus("current")
_DlmodTable_Object = MibTable
dlmodTable = _DlmodTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2)
)
if mibBuilder.loadTexts:
    dlmodTable.setStatus("current")
_DlmodEntry_Object = MibTableRow
dlmodEntry = _DlmodEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1)
)
dlmodEntry.setIndexNames(
    (0, "DLMOD-MIB", "dlmodIndex"),
)
if mibBuilder.loadTexts:
    dlmodEntry.setStatus("current")


class _DlmodIndex_Type(Integer32):
    """Custom type dlmodIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlmodIndex_Type.__name__ = "Integer32"
_DlmodIndex_Object = MibTableColumn
dlmodIndex = _DlmodIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 1),
    _DlmodIndex_Type()
)
dlmodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodIndex.setStatus("current")


class _DlmodName_Type(DisplayString):
    """Custom type dlmodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodName_Type.__name__ = "DisplayString"
_DlmodName_Object = MibTableColumn
dlmodName = _DlmodName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 2),
    _DlmodName_Type()
)
dlmodName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodName.setStatus("current")


class _DlmodPath_Type(DisplayString):
    """Custom type dlmodPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodPath_Type.__name__ = "DisplayString"
_DlmodPath_Object = MibTableColumn
dlmodPath = _DlmodPath_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 3),
    _DlmodPath_Type()
)
dlmodPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodPath.setStatus("current")


class _DlmodError_Type(DisplayString):
    """Custom type dlmodError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlmodError_Type.__name__ = "DisplayString"
_DlmodError_Object = MibTableColumn
dlmodError = _DlmodError_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 4),
    _DlmodError_Type()
)
dlmodError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlmodError.setStatus("current")


class _DlmodStatus_Type(Integer32):
    """Custom type dlmodStatus based on Integer32"""
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
        *(("create", 6),
          ("delete", 7),
          ("error", 3),
          ("load", 4),
          ("loaded", 1),
          ("unload", 5),
          ("unloaded", 2))
    )


_DlmodStatus_Type.__name__ = "Integer32"
_DlmodStatus_Object = MibTableColumn
dlmodStatus = _DlmodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 14, 2, 1, 5),
    _DlmodStatus_Type()
)
dlmodStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlmodStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLMOD-MIB",
    **{"dlmod": dlmod,
       "dlmodNextIndex": dlmodNextIndex,
       "dlmodTable": dlmodTable,
       "dlmodEntry": dlmodEntry,
       "dlmodIndex": dlmodIndex,
       "dlmodName": dlmodName,
       "dlmodPath": dlmodPath,
       "dlmodError": dlmodError,
       "dlmodStatus": dlmodStatus}
)
