# SNMP MIB module (ISPGRPEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISPGRPEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:59 2024
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

(ispgrpExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "ispgrpExt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

apIspgrpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApIspgrpTable_Object = MibTable
apIspgrpTable = _ApIspgrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2)
)
if mibBuilder.loadTexts:
    apIspgrpTable.setStatus("current")
_ApIspgrpEntry_Object = MibTableRow
apIspgrpEntry = _ApIspgrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1)
)
apIspgrpEntry.setIndexNames(
    (0, "ISPGRPEXT-MIB", "apIspgrpName"),
)
if mibBuilder.loadTexts:
    apIspgrpEntry.setStatus("current")


class _ApIspgrpName_Type(DisplayString):
    """Custom type apIspgrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApIspgrpName_Type.__name__ = "DisplayString"
_ApIspgrpName_Object = MibTableColumn
apIspgrpName = _ApIspgrpName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 1),
    _ApIspgrpName_Type()
)
apIspgrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspgrpName.setStatus("current")
_ApIspgrpIndex_Type = Integer32
_ApIspgrpIndex_Object = MibTableColumn
apIspgrpIndex = _ApIspgrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 2),
    _ApIspgrpIndex_Type()
)
apIspgrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspgrpIndex.setStatus("current")


class _ApIspgrpTotalBwdth_Type(Integer32):
    """Custom type apIspgrpTotalBwdth based on Integer32"""
    defaultValue = 0


_ApIspgrpTotalBwdth_Object = MibTableColumn
apIspgrpTotalBwdth = _ApIspgrpTotalBwdth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 3),
    _ApIspgrpTotalBwdth_Type()
)
apIspgrpTotalBwdth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspgrpTotalBwdth.setStatus("current")


class _ApIspgrpWebHostPipeBwdth_Type(Integer32):
    """Custom type apIspgrpWebHostPipeBwdth based on Integer32"""
    defaultValue = 0


_ApIspgrpWebHostPipeBwdth_Object = MibTableColumn
apIspgrpWebHostPipeBwdth = _ApIspgrpWebHostPipeBwdth_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 4),
    _ApIspgrpWebHostPipeBwdth_Type()
)
apIspgrpWebHostPipeBwdth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspgrpWebHostPipeBwdth.setStatus("current")


class _ApIspgrpMode_Type(Integer32):
    """Custom type apIspgrpMode based on Integer32"""
    defaultValue = 1


_ApIspgrpMode_Object = MibTableColumn
apIspgrpMode = _ApIspgrpMode_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 5),
    _ApIspgrpMode_Type()
)
apIspgrpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspgrpMode.setStatus("current")
_ApIspgrpStatus_Type = RowStatus
_ApIspgrpStatus_Object = MibTableColumn
apIspgrpStatus = _ApIspgrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 2, 1, 6),
    _ApIspgrpStatus_Type()
)
apIspgrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspgrpStatus.setStatus("current")
_ApIspLinkTable_Object = MibTable
apIspLinkTable = _ApIspLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3)
)
if mibBuilder.loadTexts:
    apIspLinkTable.setStatus("current")
_ApIspLinkEntry_Object = MibTableRow
apIspLinkEntry = _ApIspLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1)
)
apIspLinkEntry.setIndexNames(
    (0, "ISPGRPEXT-MIB", "apIspName"),
    (0, "ISPGRPEXT-MIB", "apIspLinkifIndex"),
)
if mibBuilder.loadTexts:
    apIspLinkEntry.setStatus("current")


class _ApIspName_Type(DisplayString):
    """Custom type apIspName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ApIspName_Type.__name__ = "DisplayString"
_ApIspName_Object = MibTableColumn
apIspName = _ApIspName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 1),
    _ApIspName_Type()
)
apIspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspName.setStatus("current")
_ApIspLinkIndex_Type = Integer32
_ApIspLinkIndex_Object = MibTableColumn
apIspLinkIndex = _ApIspLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 2),
    _ApIspLinkIndex_Type()
)
apIspLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspLinkIndex.setStatus("current")
_ApIspLinkifIndex_Type = Integer32
_ApIspLinkifIndex_Object = MibTableColumn
apIspLinkifIndex = _ApIspLinkifIndex_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 3),
    _ApIspLinkifIndex_Type()
)
apIspLinkifIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspLinkifIndex.setStatus("current")


class _ApIspLinkBwdthAlloc_Type(Integer32):
    """Custom type apIspLinkBwdthAlloc based on Integer32"""
    defaultValue = 0


_ApIspLinkBwdthAlloc_Object = MibTableColumn
apIspLinkBwdthAlloc = _ApIspLinkBwdthAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 4),
    _ApIspLinkBwdthAlloc_Type()
)
apIspLinkBwdthAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspLinkBwdthAlloc.setStatus("current")


class _ApIspLinkBEBwdthAlloc_Type(Integer32):
    """Custom type apIspLinkBEBwdthAlloc based on Integer32"""
    defaultValue = 0


_ApIspLinkBEBwdthAlloc_Object = MibTableColumn
apIspLinkBEBwdthAlloc = _ApIspLinkBEBwdthAlloc_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 5),
    _ApIspLinkBEBwdthAlloc_Type()
)
apIspLinkBEBwdthAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apIspLinkBEBwdthAlloc.setStatus("current")
_ApIspLinkStatus_Type = RowStatus
_ApIspLinkStatus_Object = MibTableColumn
apIspLinkStatus = _ApIspLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 27, 3, 1, 6),
    _ApIspLinkStatus_Type()
)
apIspLinkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apIspLinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISPGRPEXT-MIB",
    **{"apIspgrpExtMib": apIspgrpExtMib,
       "apIspgrpTable": apIspgrpTable,
       "apIspgrpEntry": apIspgrpEntry,
       "apIspgrpName": apIspgrpName,
       "apIspgrpIndex": apIspgrpIndex,
       "apIspgrpTotalBwdth": apIspgrpTotalBwdth,
       "apIspgrpWebHostPipeBwdth": apIspgrpWebHostPipeBwdth,
       "apIspgrpMode": apIspgrpMode,
       "apIspgrpStatus": apIspgrpStatus,
       "apIspLinkTable": apIspLinkTable,
       "apIspLinkEntry": apIspLinkEntry,
       "apIspName": apIspName,
       "apIspLinkIndex": apIspLinkIndex,
       "apIspLinkifIndex": apIspLinkifIndex,
       "apIspLinkBwdthAlloc": apIspLinkBwdthAlloc,
       "apIspLinkBEBwdthAlloc": apIspLinkBEBwdthAlloc,
       "apIspLinkStatus": apIspLinkStatus}
)
