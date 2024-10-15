# SNMP MIB module (CNTDNSEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNTDNSEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:02 2024
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

(cntdnsExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cntdnsExt")

(apCntName,
 apCntOwner) = mibBuilder.importSymbols(
    "CNTEXT-MIB",
    "apCntName",
    "apCntOwner")

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

apCntdnsExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCntdnsTable_Object = MibTable
apCntdnsTable = _ApCntdnsTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2)
)
if mibBuilder.loadTexts:
    apCntdnsTable.setStatus("current")
_ApCntdnsEntry_Object = MibTableRow
apCntdnsEntry = _ApCntdnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1)
)
apCntdnsEntry.setIndexNames(
    (0, "CNTEXT-MIB", "apCntOwner"),
    (0, "CNTEXT-MIB", "apCntName"),
    (0, "CNTDNSEXT-MIB", "apCntdnsName"),
)
if mibBuilder.loadTexts:
    apCntdnsEntry.setStatus("current")


class _ApCntdnsName_Type(DisplayString):
    """Custom type apCntdnsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntdnsName_Type.__name__ = "DisplayString"
_ApCntdnsName_Object = MibTableColumn
apCntdnsName = _ApCntdnsName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 1),
    _ApCntdnsName_Type()
)
apCntdnsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsName.setStatus("current")


class _ApCntdnsNameLen_Type(Integer32):
    """Custom type apCntdnsNameLen based on Integer32"""
    defaultValue = 0


_ApCntdnsNameLen_Object = MibTableColumn
apCntdnsNameLen = _ApCntdnsNameLen_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 2),
    _ApCntdnsNameLen_Type()
)
apCntdnsNameLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsNameLen.setStatus("current")


class _ApCntdnsHits_Type(Integer32):
    """Custom type apCntdnsHits based on Integer32"""
    defaultValue = 0


_ApCntdnsHits_Object = MibTableColumn
apCntdnsHits = _ApCntdnsHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 3),
    _ApCntdnsHits_Type()
)
apCntdnsHits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsHits.setStatus("current")


class _ApCntdnsLoad_Type(Integer32):
    """Custom type apCntdnsLoad based on Integer32"""
    defaultValue = 0


_ApCntdnsLoad_Object = MibTableColumn
apCntdnsLoad = _ApCntdnsLoad_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 4),
    _ApCntdnsLoad_Type()
)
apCntdnsLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsLoad.setStatus("current")


class _ApCntdnsTtl_Type(Integer32):
    """Custom type apCntdnsTtl based on Integer32"""
    defaultValue = 0


_ApCntdnsTtl_Object = MibTableColumn
apCntdnsTtl = _ApCntdnsTtl_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 5),
    _ApCntdnsTtl_Type()
)
apCntdnsTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsTtl.setStatus("current")
_ApCntdnsStatus_Type = RowStatus
_ApCntdnsStatus_Object = MibTableColumn
apCntdnsStatus = _ApCntdnsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 41, 2, 1, 6),
    _ApCntdnsStatus_Type()
)
apCntdnsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntdnsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNTDNSEXT-MIB",
    **{"apCntdnsExtMib": apCntdnsExtMib,
       "apCntdnsTable": apCntdnsTable,
       "apCntdnsEntry": apCntdnsEntry,
       "apCntdnsName": apCntdnsName,
       "apCntdnsNameLen": apCntdnsNameLen,
       "apCntdnsHits": apCntdnsHits,
       "apCntdnsLoad": apCntdnsLoad,
       "apCntdnsTtl": apCntdnsTtl,
       "apCntdnsStatus": apCntdnsStatus}
)
