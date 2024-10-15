# SNMP MIB module (Wellfleet-RF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:59 2024
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

(wfIpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpRfRipImportTable_Object = MibTable
wfIpRfRipImportTable = _WfIpRfRipImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    wfIpRfRipImportTable.setStatus("mandatory")
_WfIpRfRipImportEntry_Object = MibTableRow
wfIpRfRipImportEntry = _WfIpRfRipImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1)
)
wfIpRfRipImportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfRipImportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipImportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipImportRipGateway"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipImportRipInterface"),
)
if mibBuilder.loadTexts:
    wfIpRfRipImportEntry.setStatus("mandatory")


class _WfIpRfRipImportCreate_Type(Integer32):
    """Custom type wfIpRfRipImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfRipImportCreate_Type.__name__ = "Integer32"
_WfIpRfRipImportCreate_Object = MibTableColumn
wfIpRfRipImportCreate = _WfIpRfRipImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 1),
    _WfIpRfRipImportCreate_Type()
)
wfIpRfRipImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportCreate.setStatus("mandatory")


class _WfIpRfRipImportEnable_Type(Integer32):
    """Custom type wfIpRfRipImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfRipImportEnable_Type.__name__ = "Integer32"
_WfIpRfRipImportEnable_Object = MibTableColumn
wfIpRfRipImportEnable = _WfIpRfRipImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 2),
    _WfIpRfRipImportEnable_Type()
)
wfIpRfRipImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportEnable.setStatus("mandatory")
_WfIpRfRipImportAddress_Type = IpAddress
_WfIpRfRipImportAddress_Object = MibTableColumn
wfIpRfRipImportAddress = _WfIpRfRipImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 3),
    _WfIpRfRipImportAddress_Type()
)
wfIpRfRipImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportAddress.setStatus("mandatory")
_WfIpRfRipImportMask_Type = IpAddress
_WfIpRfRipImportMask_Object = MibTableColumn
wfIpRfRipImportMask = _WfIpRfRipImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 4),
    _WfIpRfRipImportMask_Type()
)
wfIpRfRipImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportMask.setStatus("mandatory")


class _WfIpRfRipImportAction_Type(Integer32):
    """Custom type wfIpRfRipImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfRipImportAction_Type.__name__ = "Integer32"
_WfIpRfRipImportAction_Object = MibTableColumn
wfIpRfRipImportAction = _WfIpRfRipImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 5),
    _WfIpRfRipImportAction_Type()
)
wfIpRfRipImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportAction.setStatus("mandatory")


class _WfIpRfRipImportPreference_Type(Integer32):
    """Custom type wfIpRfRipImportPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpRfRipImportPreference_Type.__name__ = "Integer32"
_WfIpRfRipImportPreference_Object = MibTableColumn
wfIpRfRipImportPreference = _WfIpRfRipImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 6),
    _WfIpRfRipImportPreference_Type()
)
wfIpRfRipImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportPreference.setStatus("mandatory")
_WfIpRfRipImportRipGateway_Type = IpAddress
_WfIpRfRipImportRipGateway_Object = MibTableColumn
wfIpRfRipImportRipGateway = _WfIpRfRipImportRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 7),
    _WfIpRfRipImportRipGateway_Type()
)
wfIpRfRipImportRipGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportRipGateway.setStatus("mandatory")
_WfIpRfRipImportRipInterface_Type = IpAddress
_WfIpRfRipImportRipInterface_Object = MibTableColumn
wfIpRfRipImportRipInterface = _WfIpRfRipImportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 8),
    _WfIpRfRipImportRipInterface_Type()
)
wfIpRfRipImportRipInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipImportRipInterface.setStatus("mandatory")
_WfIpRfRipImportApplyMask_Type = IpAddress
_WfIpRfRipImportApplyMask_Object = MibTableColumn
wfIpRfRipImportApplyMask = _WfIpRfRipImportApplyMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 8, 1, 9),
    _WfIpRfRipImportApplyMask_Type()
)
wfIpRfRipImportApplyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipImportApplyMask.setStatus("mandatory")
_WfIpRfRipExportTable_Object = MibTable
wfIpRfRipExportTable = _WfIpRfRipExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9)
)
if mibBuilder.loadTexts:
    wfIpRfRipExportTable.setStatus("mandatory")
_WfIpRfRipExportEntry_Object = MibTableRow
wfIpRfRipExportEntry = _WfIpRfRipExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1)
)
wfIpRfRipExportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfRipExportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipExportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipExportFromProtocol"),
    (0, "Wellfleet-RF-MIB", "wfIpRfRipExportInterface"),
)
if mibBuilder.loadTexts:
    wfIpRfRipExportEntry.setStatus("mandatory")


class _WfIpRfRipExportCreate_Type(Integer32):
    """Custom type wfIpRfRipExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfRipExportCreate_Type.__name__ = "Integer32"
_WfIpRfRipExportCreate_Object = MibTableColumn
wfIpRfRipExportCreate = _WfIpRfRipExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 1),
    _WfIpRfRipExportCreate_Type()
)
wfIpRfRipExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportCreate.setStatus("mandatory")


class _WfIpRfRipExportEnable_Type(Integer32):
    """Custom type wfIpRfRipExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfRipExportEnable_Type.__name__ = "Integer32"
_WfIpRfRipExportEnable_Object = MibTableColumn
wfIpRfRipExportEnable = _WfIpRfRipExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 2),
    _WfIpRfRipExportEnable_Type()
)
wfIpRfRipExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportEnable.setStatus("mandatory")
_WfIpRfRipExportAddress_Type = IpAddress
_WfIpRfRipExportAddress_Object = MibTableColumn
wfIpRfRipExportAddress = _WfIpRfRipExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 3),
    _WfIpRfRipExportAddress_Type()
)
wfIpRfRipExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportAddress.setStatus("mandatory")
_WfIpRfRipExportMask_Type = IpAddress
_WfIpRfRipExportMask_Object = MibTableColumn
wfIpRfRipExportMask = _WfIpRfRipExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 4),
    _WfIpRfRipExportMask_Type()
)
wfIpRfRipExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportMask.setStatus("mandatory")


class _WfIpRfRipExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfRipExportFromProtocol based on Integer32"""
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
        *(("bgp3", 6),
          ("direct", 4),
          ("egp", 2),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfRipExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfRipExportFromProtocol_Object = MibTableColumn
wfIpRfRipExportFromProtocol = _WfIpRfRipExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 5),
    _WfIpRfRipExportFromProtocol_Type()
)
wfIpRfRipExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportFromProtocol.setStatus("mandatory")


class _WfIpRfRipExportAction_Type(Integer32):
    """Custom type wfIpRfRipExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 4),
          ("ignore", 3),
          ("propa", 2))
    )


_WfIpRfRipExportAction_Type.__name__ = "Integer32"
_WfIpRfRipExportAction_Object = MibTableColumn
wfIpRfRipExportAction = _WfIpRfRipExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 6),
    _WfIpRfRipExportAction_Type()
)
wfIpRfRipExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportAction.setStatus("mandatory")
_WfIpRfRipExportInterface_Type = IpAddress
_WfIpRfRipExportInterface_Object = MibTableColumn
wfIpRfRipExportInterface = _WfIpRfRipExportInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 7),
    _WfIpRfRipExportInterface_Type()
)
wfIpRfRipExportInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfRipExportInterface.setStatus("mandatory")


class _WfIpRfRipExportRipMetric_Type(Integer32):
    """Custom type wfIpRfRipExportRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpRfRipExportRipMetric_Type.__name__ = "Integer32"
_WfIpRfRipExportRipMetric_Object = MibTableColumn
wfIpRfRipExportRipMetric = _WfIpRfRipExportRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 9, 1, 8),
    _WfIpRfRipExportRipMetric_Type()
)
wfIpRfRipExportRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfRipExportRipMetric.setStatus("mandatory")
_WfIpRfOspfImportTable_Object = MibTable
wfIpRfOspfImportTable = _WfIpRfOspfImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10)
)
if mibBuilder.loadTexts:
    wfIpRfOspfImportTable.setStatus("mandatory")
_WfIpRfOspfImportEntry_Object = MibTableRow
wfIpRfOspfImportEntry = _WfIpRfOspfImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1)
)
wfIpRfOspfImportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfImportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfImportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfImportType"),
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfImportTag"),
)
if mibBuilder.loadTexts:
    wfIpRfOspfImportEntry.setStatus("mandatory")


class _WfIpRfOspfImportCreate_Type(Integer32):
    """Custom type wfIpRfOspfImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfOspfImportCreate_Type.__name__ = "Integer32"
_WfIpRfOspfImportCreate_Object = MibTableColumn
wfIpRfOspfImportCreate = _WfIpRfOspfImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 1),
    _WfIpRfOspfImportCreate_Type()
)
wfIpRfOspfImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportCreate.setStatus("mandatory")


class _WfIpRfOspfImportEnable_Type(Integer32):
    """Custom type wfIpRfOspfImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfOspfImportEnable_Type.__name__ = "Integer32"
_WfIpRfOspfImportEnable_Object = MibTableColumn
wfIpRfOspfImportEnable = _WfIpRfOspfImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 2),
    _WfIpRfOspfImportEnable_Type()
)
wfIpRfOspfImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportEnable.setStatus("mandatory")
_WfIpRfOspfImportAddress_Type = IpAddress
_WfIpRfOspfImportAddress_Object = MibTableColumn
wfIpRfOspfImportAddress = _WfIpRfOspfImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 3),
    _WfIpRfOspfImportAddress_Type()
)
wfIpRfOspfImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportAddress.setStatus("mandatory")
_WfIpRfOspfImportMask_Type = IpAddress
_WfIpRfOspfImportMask_Object = MibTableColumn
wfIpRfOspfImportMask = _WfIpRfOspfImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 4),
    _WfIpRfOspfImportMask_Type()
)
wfIpRfOspfImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportMask.setStatus("mandatory")


class _WfIpRfOspfImportAction_Type(Integer32):
    """Custom type wfIpRfOspfImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfOspfImportAction_Type.__name__ = "Integer32"
_WfIpRfOspfImportAction_Object = MibTableColumn
wfIpRfOspfImportAction = _WfIpRfOspfImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 5),
    _WfIpRfOspfImportAction_Type()
)
wfIpRfOspfImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportAction.setStatus("mandatory")


class _WfIpRfOspfImportPreference_Type(Integer32):
    """Custom type wfIpRfOspfImportPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpRfOspfImportPreference_Type.__name__ = "Integer32"
_WfIpRfOspfImportPreference_Object = MibTableColumn
wfIpRfOspfImportPreference = _WfIpRfOspfImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 6),
    _WfIpRfOspfImportPreference_Type()
)
wfIpRfOspfImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfImportPreference.setStatus("mandatory")
_WfIpRfOspfImportType_Type = Integer32
_WfIpRfOspfImportType_Object = MibTableColumn
wfIpRfOspfImportType = _WfIpRfOspfImportType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 7),
    _WfIpRfOspfImportType_Type()
)
wfIpRfOspfImportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportType.setStatus("mandatory")
_WfIpRfOspfImportTag_Type = Gauge32
_WfIpRfOspfImportTag_Object = MibTableColumn
wfIpRfOspfImportTag = _WfIpRfOspfImportTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 10, 1, 8),
    _WfIpRfOspfImportTag_Type()
)
wfIpRfOspfImportTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfImportTag.setStatus("mandatory")
_WfIpRfOspfExportTable_Object = MibTable
wfIpRfOspfExportTable = _WfIpRfOspfExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    wfIpRfOspfExportTable.setStatus("mandatory")
_WfIpRfOspfExportEntry_Object = MibTableRow
wfIpRfOspfExportEntry = _WfIpRfOspfExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1)
)
wfIpRfOspfExportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfExportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfExportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfOspfExportFromProtocol"),
)
if mibBuilder.loadTexts:
    wfIpRfOspfExportEntry.setStatus("mandatory")


class _WfIpRfOspfExportCreate_Type(Integer32):
    """Custom type wfIpRfOspfExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfOspfExportCreate_Type.__name__ = "Integer32"
_WfIpRfOspfExportCreate_Object = MibTableColumn
wfIpRfOspfExportCreate = _WfIpRfOspfExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 1),
    _WfIpRfOspfExportCreate_Type()
)
wfIpRfOspfExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportCreate.setStatus("mandatory")


class _WfIpRfOspfExportEnable_Type(Integer32):
    """Custom type wfIpRfOspfExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfOspfExportEnable_Type.__name__ = "Integer32"
_WfIpRfOspfExportEnable_Object = MibTableColumn
wfIpRfOspfExportEnable = _WfIpRfOspfExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 2),
    _WfIpRfOspfExportEnable_Type()
)
wfIpRfOspfExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportEnable.setStatus("mandatory")
_WfIpRfOspfExportAddress_Type = IpAddress
_WfIpRfOspfExportAddress_Object = MibTableColumn
wfIpRfOspfExportAddress = _WfIpRfOspfExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 3),
    _WfIpRfOspfExportAddress_Type()
)
wfIpRfOspfExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportAddress.setStatus("mandatory")
_WfIpRfOspfExportMask_Type = IpAddress
_WfIpRfOspfExportMask_Object = MibTableColumn
wfIpRfOspfExportMask = _WfIpRfOspfExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 4),
    _WfIpRfOspfExportMask_Type()
)
wfIpRfOspfExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportMask.setStatus("mandatory")


class _WfIpRfOspfExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfOspfExportFromProtocol based on Integer32"""
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
        *(("bgp3", 6),
          ("direct", 4),
          ("egp", 2),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfOspfExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfOspfExportFromProtocol_Object = MibTableColumn
wfIpRfOspfExportFromProtocol = _WfIpRfOspfExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 5),
    _WfIpRfOspfExportFromProtocol_Type()
)
wfIpRfOspfExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfOspfExportFromProtocol.setStatus("mandatory")


class _WfIpRfOspfExportAction_Type(Integer32):
    """Custom type wfIpRfOspfExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("propa", 2))
    )


_WfIpRfOspfExportAction_Type.__name__ = "Integer32"
_WfIpRfOspfExportAction_Object = MibTableColumn
wfIpRfOspfExportAction = _WfIpRfOspfExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 6),
    _WfIpRfOspfExportAction_Type()
)
wfIpRfOspfExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportAction.setStatus("mandatory")


class _WfIpRfOspfExportType_Type(Integer32):
    """Custom type wfIpRfOspfExportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfIpRfOspfExportType_Type.__name__ = "Integer32"
_WfIpRfOspfExportType_Object = MibTableColumn
wfIpRfOspfExportType = _WfIpRfOspfExportType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 7),
    _WfIpRfOspfExportType_Type()
)
wfIpRfOspfExportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportType.setStatus("mandatory")
_WfIpRfOspfExportTag_Type = Gauge32
_WfIpRfOspfExportTag_Object = MibTableColumn
wfIpRfOspfExportTag = _WfIpRfOspfExportTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 8),
    _WfIpRfOspfExportTag_Type()
)
wfIpRfOspfExportTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportTag.setStatus("mandatory")


class _WfIpRfOspfExportAutoTag_Type(Integer32):
    """Custom type wfIpRfOspfExportAutoTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfOspfExportAutoTag_Type.__name__ = "Integer32"
_WfIpRfOspfExportAutoTag_Object = MibTableColumn
wfIpRfOspfExportAutoTag = _WfIpRfOspfExportAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 11, 1, 9),
    _WfIpRfOspfExportAutoTag_Type()
)
wfIpRfOspfExportAutoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfOspfExportAutoTag.setStatus("mandatory")
_WfIpRfEgpImportTable_Object = MibTable
wfIpRfEgpImportTable = _WfIpRfEgpImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12)
)
if mibBuilder.loadTexts:
    wfIpRfEgpImportTable.setStatus("mandatory")
_WfIpRfEgpImportEntry_Object = MibTableRow
wfIpRfEgpImportEntry = _WfIpRfEgpImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1)
)
wfIpRfEgpImportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpImportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpImportPeer"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpImportAs"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpImportGateway"),
)
if mibBuilder.loadTexts:
    wfIpRfEgpImportEntry.setStatus("mandatory")


class _WfIpRfEgpImportCreate_Type(Integer32):
    """Custom type wfIpRfEgpImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfEgpImportCreate_Type.__name__ = "Integer32"
_WfIpRfEgpImportCreate_Object = MibTableColumn
wfIpRfEgpImportCreate = _WfIpRfEgpImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 1),
    _WfIpRfEgpImportCreate_Type()
)
wfIpRfEgpImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpImportCreate.setStatus("mandatory")


class _WfIpRfEgpImportEnable_Type(Integer32):
    """Custom type wfIpRfEgpImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfEgpImportEnable_Type.__name__ = "Integer32"
_WfIpRfEgpImportEnable_Object = MibTableColumn
wfIpRfEgpImportEnable = _WfIpRfEgpImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 2),
    _WfIpRfEgpImportEnable_Type()
)
wfIpRfEgpImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpImportEnable.setStatus("mandatory")
_WfIpRfEgpImportAddress_Type = IpAddress
_WfIpRfEgpImportAddress_Object = MibTableColumn
wfIpRfEgpImportAddress = _WfIpRfEgpImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 3),
    _WfIpRfEgpImportAddress_Type()
)
wfIpRfEgpImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpImportAddress.setStatus("mandatory")
_WfIpRfEgpImportMask_Type = IpAddress
_WfIpRfEgpImportMask_Object = MibTableColumn
wfIpRfEgpImportMask = _WfIpRfEgpImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 4),
    _WfIpRfEgpImportMask_Type()
)
wfIpRfEgpImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpImportMask.setStatus("mandatory")


class _WfIpRfEgpImportAction_Type(Integer32):
    """Custom type wfIpRfEgpImportAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfEgpImportAction_Type.__name__ = "Integer32"
_WfIpRfEgpImportAction_Object = MibTableColumn
wfIpRfEgpImportAction = _WfIpRfEgpImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 5),
    _WfIpRfEgpImportAction_Type()
)
wfIpRfEgpImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpImportAction.setStatus("mandatory")


class _WfIpRfEgpImportPreference_Type(Integer32):
    """Custom type wfIpRfEgpImportPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpRfEgpImportPreference_Type.__name__ = "Integer32"
_WfIpRfEgpImportPreference_Object = MibTableColumn
wfIpRfEgpImportPreference = _WfIpRfEgpImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 6),
    _WfIpRfEgpImportPreference_Type()
)
wfIpRfEgpImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpImportPreference.setStatus("mandatory")
_WfIpRfEgpImportPeer_Type = IpAddress
_WfIpRfEgpImportPeer_Object = MibTableColumn
wfIpRfEgpImportPeer = _WfIpRfEgpImportPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 7),
    _WfIpRfEgpImportPeer_Type()
)
wfIpRfEgpImportPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpImportPeer.setStatus("mandatory")
_WfIpRfEgpImportAs_Type = Integer32
_WfIpRfEgpImportAs_Object = MibTableColumn
wfIpRfEgpImportAs = _WfIpRfEgpImportAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 8),
    _WfIpRfEgpImportAs_Type()
)
wfIpRfEgpImportAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpImportAs.setStatus("mandatory")
_WfIpRfEgpImportGateway_Type = IpAddress
_WfIpRfEgpImportGateway_Object = MibTableColumn
wfIpRfEgpImportGateway = _WfIpRfEgpImportGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 12, 1, 9),
    _WfIpRfEgpImportGateway_Type()
)
wfIpRfEgpImportGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpImportGateway.setStatus("mandatory")
_WfIpRfEgpExportTable_Object = MibTable
wfIpRfEgpExportTable = _WfIpRfEgpExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13)
)
if mibBuilder.loadTexts:
    wfIpRfEgpExportTable.setStatus("mandatory")
_WfIpRfEgpExportEntry_Object = MibTableRow
wfIpRfEgpExportEntry = _WfIpRfEgpExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1)
)
wfIpRfEgpExportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportFromProtocol"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportPeer"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportOspfType"),
    (0, "Wellfleet-RF-MIB", "wfIpRfEgpExportOspfTag"),
)
if mibBuilder.loadTexts:
    wfIpRfEgpExportEntry.setStatus("mandatory")


class _WfIpRfEgpExportCreate_Type(Integer32):
    """Custom type wfIpRfEgpExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfEgpExportCreate_Type.__name__ = "Integer32"
_WfIpRfEgpExportCreate_Object = MibTableColumn
wfIpRfEgpExportCreate = _WfIpRfEgpExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 1),
    _WfIpRfEgpExportCreate_Type()
)
wfIpRfEgpExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpExportCreate.setStatus("mandatory")


class _WfIpRfEgpExportEnable_Type(Integer32):
    """Custom type wfIpRfEgpExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfEgpExportEnable_Type.__name__ = "Integer32"
_WfIpRfEgpExportEnable_Object = MibTableColumn
wfIpRfEgpExportEnable = _WfIpRfEgpExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 2),
    _WfIpRfEgpExportEnable_Type()
)
wfIpRfEgpExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpExportEnable.setStatus("mandatory")
_WfIpRfEgpExportAddress_Type = IpAddress
_WfIpRfEgpExportAddress_Object = MibTableColumn
wfIpRfEgpExportAddress = _WfIpRfEgpExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 3),
    _WfIpRfEgpExportAddress_Type()
)
wfIpRfEgpExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportAddress.setStatus("mandatory")
_WfIpRfEgpExportMask_Type = IpAddress
_WfIpRfEgpExportMask_Object = MibTableColumn
wfIpRfEgpExportMask = _WfIpRfEgpExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 4),
    _WfIpRfEgpExportMask_Type()
)
wfIpRfEgpExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportMask.setStatus("mandatory")


class _WfIpRfEgpExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfEgpExportFromProtocol based on Integer32"""
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
        *(("bgp3", 6),
          ("direct", 4),
          ("egp", 2),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfEgpExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfEgpExportFromProtocol_Object = MibTableColumn
wfIpRfEgpExportFromProtocol = _WfIpRfEgpExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 5),
    _WfIpRfEgpExportFromProtocol_Type()
)
wfIpRfEgpExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportFromProtocol.setStatus("mandatory")


class _WfIpRfEgpExportAction_Type(Integer32):
    """Custom type wfIpRfEgpExportAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 3),
          ("propa", 2))
    )


_WfIpRfEgpExportAction_Type.__name__ = "Integer32"
_WfIpRfEgpExportAction_Object = MibTableColumn
wfIpRfEgpExportAction = _WfIpRfEgpExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 6),
    _WfIpRfEgpExportAction_Type()
)
wfIpRfEgpExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpExportAction.setStatus("mandatory")
_WfIpRfEgpExportPeer_Type = IpAddress
_WfIpRfEgpExportPeer_Object = MibTableColumn
wfIpRfEgpExportPeer = _WfIpRfEgpExportPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 7),
    _WfIpRfEgpExportPeer_Type()
)
wfIpRfEgpExportPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportPeer.setStatus("mandatory")


class _WfIpRfEgpExportOspfType_Type(Integer32):
    """Custom type wfIpRfEgpExportOspfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfexttype1", 1),
          ("ospfexttype2", 2),
          ("ospfinttype", 3))
    )


_WfIpRfEgpExportOspfType_Type.__name__ = "Integer32"
_WfIpRfEgpExportOspfType_Object = MibTableColumn
wfIpRfEgpExportOspfType = _WfIpRfEgpExportOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 8),
    _WfIpRfEgpExportOspfType_Type()
)
wfIpRfEgpExportOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportOspfType.setStatus("mandatory")
_WfIpRfEgpExportOspfTag_Type = Integer32
_WfIpRfEgpExportOspfTag_Object = MibTableColumn
wfIpRfEgpExportOspfTag = _WfIpRfEgpExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 9),
    _WfIpRfEgpExportOspfTag_Type()
)
wfIpRfEgpExportOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfEgpExportOspfTag.setStatus("mandatory")
_WfIpRfEgpExportInterface_Type = IpAddress
_WfIpRfEgpExportInterface_Object = MibTableColumn
wfIpRfEgpExportInterface = _WfIpRfEgpExportInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 10),
    _WfIpRfEgpExportInterface_Type()
)
wfIpRfEgpExportInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpExportInterface.setStatus("mandatory")


class _WfIpRfEgpExportMetric_Type(Integer32):
    """Custom type wfIpRfEgpExportMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpRfEgpExportMetric_Type.__name__ = "Integer32"
_WfIpRfEgpExportMetric_Object = MibTableColumn
wfIpRfEgpExportMetric = _WfIpRfEgpExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 13, 1, 11),
    _WfIpRfEgpExportMetric_Type()
)
wfIpRfEgpExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfEgpExportMetric.setStatus("mandatory")
_WfIpRfBgp3ImportTable_Object = MibTable
wfIpRfBgp3ImportTable = _WfIpRfBgp3ImportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14)
)
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportTable.setStatus("mandatory")
_WfIpRfBgp3ImportEntry_Object = MibTableRow
wfIpRfBgp3ImportEntry = _WfIpRfBgp3ImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1)
)
wfIpRfBgp3ImportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportPeerAs"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportPeerAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportOrigAs"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ImportRouteOrigin"),
)
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportEntry.setStatus("mandatory")


class _WfIpRfBgp3ImportCreate_Type(Integer32):
    """Custom type wfIpRfBgp3ImportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfBgp3ImportCreate_Type.__name__ = "Integer32"
_WfIpRfBgp3ImportCreate_Object = MibTableColumn
wfIpRfBgp3ImportCreate = _WfIpRfBgp3ImportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 1),
    _WfIpRfBgp3ImportCreate_Type()
)
wfIpRfBgp3ImportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportCreate.setStatus("mandatory")


class _WfIpRfBgp3ImportEnable_Type(Integer32):
    """Custom type wfIpRfBgp3ImportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfBgp3ImportEnable_Type.__name__ = "Integer32"
_WfIpRfBgp3ImportEnable_Object = MibTableColumn
wfIpRfBgp3ImportEnable = _WfIpRfBgp3ImportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 2),
    _WfIpRfBgp3ImportEnable_Type()
)
wfIpRfBgp3ImportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportEnable.setStatus("mandatory")
_WfIpRfBgp3ImportAddress_Type = IpAddress
_WfIpRfBgp3ImportAddress_Object = MibTableColumn
wfIpRfBgp3ImportAddress = _WfIpRfBgp3ImportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 3),
    _WfIpRfBgp3ImportAddress_Type()
)
wfIpRfBgp3ImportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportAddress.setStatus("mandatory")
_WfIpRfBgp3ImportMask_Type = IpAddress
_WfIpRfBgp3ImportMask_Object = MibTableColumn
wfIpRfBgp3ImportMask = _WfIpRfBgp3ImportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 4),
    _WfIpRfBgp3ImportMask_Type()
)
wfIpRfBgp3ImportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportMask.setStatus("mandatory")


class _WfIpRfBgp3ImportAction_Type(Integer32):
    """Custom type wfIpRfBgp3ImportAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 3))
    )


_WfIpRfBgp3ImportAction_Type.__name__ = "Integer32"
_WfIpRfBgp3ImportAction_Object = MibTableColumn
wfIpRfBgp3ImportAction = _WfIpRfBgp3ImportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 5),
    _WfIpRfBgp3ImportAction_Type()
)
wfIpRfBgp3ImportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportAction.setStatus("mandatory")


class _WfIpRfBgp3ImportPreference_Type(Integer32):
    """Custom type wfIpRfBgp3ImportPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WfIpRfBgp3ImportPreference_Type.__name__ = "Integer32"
_WfIpRfBgp3ImportPreference_Object = MibTableColumn
wfIpRfBgp3ImportPreference = _WfIpRfBgp3ImportPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 6),
    _WfIpRfBgp3ImportPreference_Type()
)
wfIpRfBgp3ImportPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportPreference.setStatus("mandatory")
_WfIpRfBgp3ImportPeerAs_Type = Integer32
_WfIpRfBgp3ImportPeerAs_Object = MibTableColumn
wfIpRfBgp3ImportPeerAs = _WfIpRfBgp3ImportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 7),
    _WfIpRfBgp3ImportPeerAs_Type()
)
wfIpRfBgp3ImportPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportPeerAs.setStatus("mandatory")
_WfIpRfBgp3ImportPeerAddress_Type = IpAddress
_WfIpRfBgp3ImportPeerAddress_Object = MibTableColumn
wfIpRfBgp3ImportPeerAddress = _WfIpRfBgp3ImportPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 8),
    _WfIpRfBgp3ImportPeerAddress_Type()
)
wfIpRfBgp3ImportPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportPeerAddress.setStatus("mandatory")
_WfIpRfBgp3ImportOrigAs_Type = Integer32
_WfIpRfBgp3ImportOrigAs_Object = MibTableColumn
wfIpRfBgp3ImportOrigAs = _WfIpRfBgp3ImportOrigAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 9),
    _WfIpRfBgp3ImportOrigAs_Type()
)
wfIpRfBgp3ImportOrigAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportOrigAs.setStatus("mandatory")


class _WfIpRfBgp3ImportRouteOrigin_Type(Integer32):
    """Custom type wfIpRfBgp3ImportRouteOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_WfIpRfBgp3ImportRouteOrigin_Type.__name__ = "Integer32"
_WfIpRfBgp3ImportRouteOrigin_Object = MibTableColumn
wfIpRfBgp3ImportRouteOrigin = _WfIpRfBgp3ImportRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 10),
    _WfIpRfBgp3ImportRouteOrigin_Type()
)
wfIpRfBgp3ImportRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportRouteOrigin.setStatus("mandatory")


class _WfIpRfBgp3ImportBgp3Preference_Type(Gauge32):
    """Custom type wfIpRfBgp3ImportBgp3Preference based on Gauge32"""
    defaultValue = 1


_WfIpRfBgp3ImportBgp3Preference_Object = MibTableColumn
wfIpRfBgp3ImportBgp3Preference = _WfIpRfBgp3ImportBgp3Preference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 14, 1, 11),
    _WfIpRfBgp3ImportBgp3Preference_Type()
)
wfIpRfBgp3ImportBgp3Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ImportBgp3Preference.setStatus("mandatory")
_WfIpRfBgp3ExportTable_Object = MibTable
wfIpRfBgp3ExportTable = _WfIpRfBgp3ExportTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15)
)
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportTable.setStatus("mandatory")
_WfIpRfBgp3ExportEntry_Object = MibTableRow
wfIpRfBgp3ExportEntry = _WfIpRfBgp3ExportEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1)
)
wfIpRfBgp3ExportEntry.setIndexNames(
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportMask"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportFromProtocol"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportPeerAs"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportPeerAddress"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportOspfType"),
    (0, "Wellfleet-RF-MIB", "wfIpRfBgp3ExportOspfTag"),
)
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportEntry.setStatus("mandatory")


class _WfIpRfBgp3ExportCreate_Type(Integer32):
    """Custom type wfIpRfBgp3ExportCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfIpRfBgp3ExportCreate_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportCreate_Object = MibTableColumn
wfIpRfBgp3ExportCreate = _WfIpRfBgp3ExportCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 1),
    _WfIpRfBgp3ExportCreate_Type()
)
wfIpRfBgp3ExportCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportCreate.setStatus("mandatory")


class _WfIpRfBgp3ExportEnable_Type(Integer32):
    """Custom type wfIpRfBgp3ExportEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WfIpRfBgp3ExportEnable_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportEnable_Object = MibTableColumn
wfIpRfBgp3ExportEnable = _WfIpRfBgp3ExportEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 2),
    _WfIpRfBgp3ExportEnable_Type()
)
wfIpRfBgp3ExportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportEnable.setStatus("mandatory")
_WfIpRfBgp3ExportAddress_Type = IpAddress
_WfIpRfBgp3ExportAddress_Object = MibTableColumn
wfIpRfBgp3ExportAddress = _WfIpRfBgp3ExportAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 3),
    _WfIpRfBgp3ExportAddress_Type()
)
wfIpRfBgp3ExportAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportAddress.setStatus("mandatory")
_WfIpRfBgp3ExportMask_Type = IpAddress
_WfIpRfBgp3ExportMask_Object = MibTableColumn
wfIpRfBgp3ExportMask = _WfIpRfBgp3ExportMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 4),
    _WfIpRfBgp3ExportMask_Type()
)
wfIpRfBgp3ExportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportMask.setStatus("mandatory")


class _WfIpRfBgp3ExportFromProtocol_Type(Integer32):
    """Custom type wfIpRfBgp3ExportFromProtocol based on Integer32"""
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
        *(("bgp3", 6),
          ("direct", 4),
          ("egp", 2),
          ("ospf", 3),
          ("rip", 1),
          ("static", 5))
    )


_WfIpRfBgp3ExportFromProtocol_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportFromProtocol_Object = MibTableColumn
wfIpRfBgp3ExportFromProtocol = _WfIpRfBgp3ExportFromProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 5),
    _WfIpRfBgp3ExportFromProtocol_Type()
)
wfIpRfBgp3ExportFromProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportFromProtocol.setStatus("mandatory")


class _WfIpRfBgp3ExportAction_Type(Integer32):
    """Custom type wfIpRfBgp3ExportAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 4),
          ("ignore", 3),
          ("propa", 2))
    )


_WfIpRfBgp3ExportAction_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportAction_Object = MibTableColumn
wfIpRfBgp3ExportAction = _WfIpRfBgp3ExportAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 6),
    _WfIpRfBgp3ExportAction_Type()
)
wfIpRfBgp3ExportAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportAction.setStatus("mandatory")
_WfIpRfBgp3ExportPeerAs_Type = Integer32
_WfIpRfBgp3ExportPeerAs_Object = MibTableColumn
wfIpRfBgp3ExportPeerAs = _WfIpRfBgp3ExportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 7),
    _WfIpRfBgp3ExportPeerAs_Type()
)
wfIpRfBgp3ExportPeerAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportPeerAs.setStatus("mandatory")
_WfIpRfBgp3ExportPeerAddress_Type = IpAddress
_WfIpRfBgp3ExportPeerAddress_Object = MibTableColumn
wfIpRfBgp3ExportPeerAddress = _WfIpRfBgp3ExportPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 8),
    _WfIpRfBgp3ExportPeerAddress_Type()
)
wfIpRfBgp3ExportPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportPeerAddress.setStatus("mandatory")


class _WfIpRfBgp3ExportOspfType_Type(Integer32):
    """Custom type wfIpRfBgp3ExportOspfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ospfexttype1", 1),
          ("ospfexttype2", 2),
          ("ospfinttype", 3))
    )


_WfIpRfBgp3ExportOspfType_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportOspfType_Object = MibTableColumn
wfIpRfBgp3ExportOspfType = _WfIpRfBgp3ExportOspfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 9),
    _WfIpRfBgp3ExportOspfType_Type()
)
wfIpRfBgp3ExportOspfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportOspfType.setStatus("mandatory")
_WfIpRfBgp3ExportOspfTag_Type = Integer32
_WfIpRfBgp3ExportOspfTag_Object = MibTableColumn
wfIpRfBgp3ExportOspfTag = _WfIpRfBgp3ExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 10),
    _WfIpRfBgp3ExportOspfTag_Type()
)
wfIpRfBgp3ExportOspfTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportOspfTag.setStatus("mandatory")


class _WfIpRfBgp3ExportUseMetric_Type(Integer32):
    """Custom type wfIpRfBgp3ExportUseMetric based on Integer32"""
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
        *(("none", 1),
          ("originating", 3),
          ("specified", 2))
    )


_WfIpRfBgp3ExportUseMetric_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportUseMetric_Object = MibTableColumn
wfIpRfBgp3ExportUseMetric = _WfIpRfBgp3ExportUseMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 11),
    _WfIpRfBgp3ExportUseMetric_Type()
)
wfIpRfBgp3ExportUseMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportUseMetric.setStatus("mandatory")


class _WfIpRfBgp3ExportInterAsMetric_Type(Integer32):
    """Custom type wfIpRfBgp3ExportInterAsMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpRfBgp3ExportInterAsMetric_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportInterAsMetric_Object = MibTableColumn
wfIpRfBgp3ExportInterAsMetric = _WfIpRfBgp3ExportInterAsMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 12),
    _WfIpRfBgp3ExportInterAsMetric_Type()
)
wfIpRfBgp3ExportInterAsMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportInterAsMetric.setStatus("mandatory")


class _WfIpRfBgp3ExportOrigin_Type(Integer32):
    """Custom type wfIpRfBgp3ExportOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WfIpRfBgp3ExportOrigin_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportOrigin_Object = MibTableColumn
wfIpRfBgp3ExportOrigin = _WfIpRfBgp3ExportOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 13),
    _WfIpRfBgp3ExportOrigin_Type()
)
wfIpRfBgp3ExportOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportOrigin.setStatus("mandatory")


class _WfIpRfBgp3ExportNeighAs_Type(Integer32):
    """Custom type wfIpRfBgp3ExportNeighAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpRfBgp3ExportNeighAs_Type.__name__ = "Integer32"
_WfIpRfBgp3ExportNeighAs_Object = MibTableColumn
wfIpRfBgp3ExportNeighAs = _WfIpRfBgp3ExportNeighAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 15, 1, 14),
    _WfIpRfBgp3ExportNeighAs_Type()
)
wfIpRfBgp3ExportNeighAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpRfBgp3ExportNeighAs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RF-MIB",
    **{"wfIpRfRipImportTable": wfIpRfRipImportTable,
       "wfIpRfRipImportEntry": wfIpRfRipImportEntry,
       "wfIpRfRipImportCreate": wfIpRfRipImportCreate,
       "wfIpRfRipImportEnable": wfIpRfRipImportEnable,
       "wfIpRfRipImportAddress": wfIpRfRipImportAddress,
       "wfIpRfRipImportMask": wfIpRfRipImportMask,
       "wfIpRfRipImportAction": wfIpRfRipImportAction,
       "wfIpRfRipImportPreference": wfIpRfRipImportPreference,
       "wfIpRfRipImportRipGateway": wfIpRfRipImportRipGateway,
       "wfIpRfRipImportRipInterface": wfIpRfRipImportRipInterface,
       "wfIpRfRipImportApplyMask": wfIpRfRipImportApplyMask,
       "wfIpRfRipExportTable": wfIpRfRipExportTable,
       "wfIpRfRipExportEntry": wfIpRfRipExportEntry,
       "wfIpRfRipExportCreate": wfIpRfRipExportCreate,
       "wfIpRfRipExportEnable": wfIpRfRipExportEnable,
       "wfIpRfRipExportAddress": wfIpRfRipExportAddress,
       "wfIpRfRipExportMask": wfIpRfRipExportMask,
       "wfIpRfRipExportFromProtocol": wfIpRfRipExportFromProtocol,
       "wfIpRfRipExportAction": wfIpRfRipExportAction,
       "wfIpRfRipExportInterface": wfIpRfRipExportInterface,
       "wfIpRfRipExportRipMetric": wfIpRfRipExportRipMetric,
       "wfIpRfOspfImportTable": wfIpRfOspfImportTable,
       "wfIpRfOspfImportEntry": wfIpRfOspfImportEntry,
       "wfIpRfOspfImportCreate": wfIpRfOspfImportCreate,
       "wfIpRfOspfImportEnable": wfIpRfOspfImportEnable,
       "wfIpRfOspfImportAddress": wfIpRfOspfImportAddress,
       "wfIpRfOspfImportMask": wfIpRfOspfImportMask,
       "wfIpRfOspfImportAction": wfIpRfOspfImportAction,
       "wfIpRfOspfImportPreference": wfIpRfOspfImportPreference,
       "wfIpRfOspfImportType": wfIpRfOspfImportType,
       "wfIpRfOspfImportTag": wfIpRfOspfImportTag,
       "wfIpRfOspfExportTable": wfIpRfOspfExportTable,
       "wfIpRfOspfExportEntry": wfIpRfOspfExportEntry,
       "wfIpRfOspfExportCreate": wfIpRfOspfExportCreate,
       "wfIpRfOspfExportEnable": wfIpRfOspfExportEnable,
       "wfIpRfOspfExportAddress": wfIpRfOspfExportAddress,
       "wfIpRfOspfExportMask": wfIpRfOspfExportMask,
       "wfIpRfOspfExportFromProtocol": wfIpRfOspfExportFromProtocol,
       "wfIpRfOspfExportAction": wfIpRfOspfExportAction,
       "wfIpRfOspfExportType": wfIpRfOspfExportType,
       "wfIpRfOspfExportTag": wfIpRfOspfExportTag,
       "wfIpRfOspfExportAutoTag": wfIpRfOspfExportAutoTag,
       "wfIpRfEgpImportTable": wfIpRfEgpImportTable,
       "wfIpRfEgpImportEntry": wfIpRfEgpImportEntry,
       "wfIpRfEgpImportCreate": wfIpRfEgpImportCreate,
       "wfIpRfEgpImportEnable": wfIpRfEgpImportEnable,
       "wfIpRfEgpImportAddress": wfIpRfEgpImportAddress,
       "wfIpRfEgpImportMask": wfIpRfEgpImportMask,
       "wfIpRfEgpImportAction": wfIpRfEgpImportAction,
       "wfIpRfEgpImportPreference": wfIpRfEgpImportPreference,
       "wfIpRfEgpImportPeer": wfIpRfEgpImportPeer,
       "wfIpRfEgpImportAs": wfIpRfEgpImportAs,
       "wfIpRfEgpImportGateway": wfIpRfEgpImportGateway,
       "wfIpRfEgpExportTable": wfIpRfEgpExportTable,
       "wfIpRfEgpExportEntry": wfIpRfEgpExportEntry,
       "wfIpRfEgpExportCreate": wfIpRfEgpExportCreate,
       "wfIpRfEgpExportEnable": wfIpRfEgpExportEnable,
       "wfIpRfEgpExportAddress": wfIpRfEgpExportAddress,
       "wfIpRfEgpExportMask": wfIpRfEgpExportMask,
       "wfIpRfEgpExportFromProtocol": wfIpRfEgpExportFromProtocol,
       "wfIpRfEgpExportAction": wfIpRfEgpExportAction,
       "wfIpRfEgpExportPeer": wfIpRfEgpExportPeer,
       "wfIpRfEgpExportOspfType": wfIpRfEgpExportOspfType,
       "wfIpRfEgpExportOspfTag": wfIpRfEgpExportOspfTag,
       "wfIpRfEgpExportInterface": wfIpRfEgpExportInterface,
       "wfIpRfEgpExportMetric": wfIpRfEgpExportMetric,
       "wfIpRfBgp3ImportTable": wfIpRfBgp3ImportTable,
       "wfIpRfBgp3ImportEntry": wfIpRfBgp3ImportEntry,
       "wfIpRfBgp3ImportCreate": wfIpRfBgp3ImportCreate,
       "wfIpRfBgp3ImportEnable": wfIpRfBgp3ImportEnable,
       "wfIpRfBgp3ImportAddress": wfIpRfBgp3ImportAddress,
       "wfIpRfBgp3ImportMask": wfIpRfBgp3ImportMask,
       "wfIpRfBgp3ImportAction": wfIpRfBgp3ImportAction,
       "wfIpRfBgp3ImportPreference": wfIpRfBgp3ImportPreference,
       "wfIpRfBgp3ImportPeerAs": wfIpRfBgp3ImportPeerAs,
       "wfIpRfBgp3ImportPeerAddress": wfIpRfBgp3ImportPeerAddress,
       "wfIpRfBgp3ImportOrigAs": wfIpRfBgp3ImportOrigAs,
       "wfIpRfBgp3ImportRouteOrigin": wfIpRfBgp3ImportRouteOrigin,
       "wfIpRfBgp3ImportBgp3Preference": wfIpRfBgp3ImportBgp3Preference,
       "wfIpRfBgp3ExportTable": wfIpRfBgp3ExportTable,
       "wfIpRfBgp3ExportEntry": wfIpRfBgp3ExportEntry,
       "wfIpRfBgp3ExportCreate": wfIpRfBgp3ExportCreate,
       "wfIpRfBgp3ExportEnable": wfIpRfBgp3ExportEnable,
       "wfIpRfBgp3ExportAddress": wfIpRfBgp3ExportAddress,
       "wfIpRfBgp3ExportMask": wfIpRfBgp3ExportMask,
       "wfIpRfBgp3ExportFromProtocol": wfIpRfBgp3ExportFromProtocol,
       "wfIpRfBgp3ExportAction": wfIpRfBgp3ExportAction,
       "wfIpRfBgp3ExportPeerAs": wfIpRfBgp3ExportPeerAs,
       "wfIpRfBgp3ExportPeerAddress": wfIpRfBgp3ExportPeerAddress,
       "wfIpRfBgp3ExportOspfType": wfIpRfBgp3ExportOspfType,
       "wfIpRfBgp3ExportOspfTag": wfIpRfBgp3ExportOspfTag,
       "wfIpRfBgp3ExportUseMetric": wfIpRfBgp3ExportUseMetric,
       "wfIpRfBgp3ExportInterAsMetric": wfIpRfBgp3ExportInterAsMetric,
       "wfIpRfBgp3ExportOrigin": wfIpRfBgp3ExportOrigin,
       "wfIpRfBgp3ExportNeighAs": wfIpRfBgp3ExportNeighAs}
)
