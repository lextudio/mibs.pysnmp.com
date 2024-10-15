# SNMP MIB module (SAMSUNG-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SAMSUNG-DIAGNOSTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:38 2024
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

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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

scmDiagnostics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ScmDiagnosticsDevice_ObjectIdentity = ObjectIdentity
scmDiagnosticsDevice = _ScmDiagnosticsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1)
)
_ScmDiagnosticsDeviceTable_Object = MibTable
scmDiagnosticsDeviceTable = _ScmDiagnosticsDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2)
)
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceTable.setStatus("current")
_ScmDiagnosticsDeviceEntry_Object = MibTableRow
scmDiagnosticsDeviceEntry = _ScmDiagnosticsDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1)
)
scmDiagnosticsDeviceEntry.setIndexNames(
    (0, "SAMSUNG-DIAGNOSTICS-MIB", "scmDiagnosticsDeviceIndex"),
)
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceEntry.setStatus("current")


class _ScmDiagnosticsDeviceIndex_Type(Integer32):
    """Custom type scmDiagnosticsDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmDiagnosticsDeviceIndex_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceIndex_Object = MibTableColumn
scmDiagnosticsDeviceIndex = _ScmDiagnosticsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 1),
    _ScmDiagnosticsDeviceIndex_Type()
)
scmDiagnosticsDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceIndex.setStatus("current")


class _ScmDiagnosticsDeviceItem_Type(DisplayString):
    """Custom type scmDiagnosticsDeviceItem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScmDiagnosticsDeviceItem_Type.__name__ = "DisplayString"
_ScmDiagnosticsDeviceItem_Object = MibTableColumn
scmDiagnosticsDeviceItem = _ScmDiagnosticsDeviceItem_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 2),
    _ScmDiagnosticsDeviceItem_Type()
)
scmDiagnosticsDeviceItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceItem.setStatus("current")


class _ScmDiagnosticsDeviceType_Type(Integer32):
    """Custom type scmDiagnosticsDeviceType based on Integer32"""
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
              21,
              22,
              23,
              24,
              25,
              26,
              41,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("cover", 3),
          ("fax", 21),
          ("finisher", 26),
          ("geeralPrinter", 4),
          ("input", 1),
          ("marker", 6),
          ("markerColorant", 8),
          ("markerSupplies", 7),
          ("mediaPath", 5),
          ("memory", 43),
          ("motor", 41),
          ("network", 23),
          ("output", 2),
          ("parallel", 25),
          ("scanner", 22),
          ("smps", 42),
          ("usb", 24))
    )


_ScmDiagnosticsDeviceType_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceType_Object = MibTableColumn
scmDiagnosticsDeviceType = _ScmDiagnosticsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 3),
    _ScmDiagnosticsDeviceType_Type()
)
scmDiagnosticsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceType.setStatus("current")


class _ScmDiagnosticsDeviceDescr_Type(DisplayString):
    """Custom type scmDiagnosticsDeviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ScmDiagnosticsDeviceDescr_Type.__name__ = "DisplayString"
_ScmDiagnosticsDeviceDescr_Object = MibTableColumn
scmDiagnosticsDeviceDescr = _ScmDiagnosticsDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 4),
    _ScmDiagnosticsDeviceDescr_Type()
)
scmDiagnosticsDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceDescr.setStatus("current")


class _ScmDiagnosticsDeviceID_Type(Integer32):
    """Custom type scmDiagnosticsDeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ScmDiagnosticsDeviceID_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceID_Object = MibTableColumn
scmDiagnosticsDeviceID = _ScmDiagnosticsDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 5),
    _ScmDiagnosticsDeviceID_Type()
)
scmDiagnosticsDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceID.setStatus("current")


class _ScmDiagnosticsDeviceStatus_Type(Integer32):
    """Custom type scmDiagnosticsDeviceStatus based on Integer32"""
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
        *(("down", 5),
          ("printing", 6),
          ("running", 2),
          ("testing", 4),
          ("unknown", 1),
          ("warning", 3))
    )


_ScmDiagnosticsDeviceStatus_Type.__name__ = "Integer32"
_ScmDiagnosticsDeviceStatus_Object = MibTableColumn
scmDiagnosticsDeviceStatus = _ScmDiagnosticsDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 6),
    _ScmDiagnosticsDeviceStatus_Type()
)
scmDiagnosticsDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceStatus.setStatus("current")
_ScmDiagnosticsDeviceErrors_Type = Counter32
_ScmDiagnosticsDeviceErrors_Object = MibTableColumn
scmDiagnosticsDeviceErrors = _ScmDiagnosticsDeviceErrors_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 7),
    _ScmDiagnosticsDeviceErrors_Type()
)
scmDiagnosticsDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmDiagnosticsDeviceErrors.setStatus("current")


class _ScmDiagnosticsRequest_Type(Integer32):
    """Custom type scmDiagnosticsRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ScmDiagnosticsRequest_Type.__name__ = "Integer32"
_ScmDiagnosticsRequest_Object = MibTableColumn
scmDiagnosticsRequest = _ScmDiagnosticsRequest_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 8),
    _ScmDiagnosticsRequest_Type()
)
scmDiagnosticsRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scmDiagnosticsRequest.setStatus("current")


class _ScmGenBaseDeviceImageFileName_Type(DisplayString):
    """Custom type scmGenBaseDeviceImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ScmGenBaseDeviceImageFileName_Type.__name__ = "DisplayString"
_ScmGenBaseDeviceImageFileName_Object = MibTableColumn
scmGenBaseDeviceImageFileName = _ScmGenBaseDeviceImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 64, 1, 2, 1, 999),
    _ScmGenBaseDeviceImageFileName_Type()
)
scmGenBaseDeviceImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmGenBaseDeviceImageFileName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-DIAGNOSTICS-MIB",
    **{"scmDiagnostics": scmDiagnostics,
       "scmDiagnosticsDevice": scmDiagnosticsDevice,
       "scmDiagnosticsDeviceTable": scmDiagnosticsDeviceTable,
       "scmDiagnosticsDeviceEntry": scmDiagnosticsDeviceEntry,
       "scmDiagnosticsDeviceIndex": scmDiagnosticsDeviceIndex,
       "scmDiagnosticsDeviceItem": scmDiagnosticsDeviceItem,
       "scmDiagnosticsDeviceType": scmDiagnosticsDeviceType,
       "scmDiagnosticsDeviceDescr": scmDiagnosticsDeviceDescr,
       "scmDiagnosticsDeviceID": scmDiagnosticsDeviceID,
       "scmDiagnosticsDeviceStatus": scmDiagnosticsDeviceStatus,
       "scmDiagnosticsDeviceErrors": scmDiagnosticsDeviceErrors,
       "scmDiagnosticsRequest": scmDiagnosticsRequest,
       "scmGenBaseDeviceImageFileName": scmGenBaseDeviceImageFileName}
)
