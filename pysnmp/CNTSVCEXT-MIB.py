# SNMP MIB module (CNTSVCEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CNTSVCEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:04 2024
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

(cntsvcExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "cntsvcExt")

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

apCntsvcExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApCntsvcTable_Object = MibTable
apCntsvcTable = _ApCntsvcTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2)
)
if mibBuilder.loadTexts:
    apCntsvcTable.setStatus("current")
_ApCntsvcEntry_Object = MibTableRow
apCntsvcEntry = _ApCntsvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1)
)
apCntsvcEntry.setIndexNames(
    (0, "CNTSVCEXT-MIB", "apCntsvcOwnName"),
    (0, "CNTSVCEXT-MIB", "apCntsvcCntName"),
    (0, "CNTSVCEXT-MIB", "apCntsvcSvcName"),
)
if mibBuilder.loadTexts:
    apCntsvcEntry.setStatus("current")


class _ApCntsvcOwnName_Type(DisplayString):
    """Custom type apCntsvcOwnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcOwnName_Type.__name__ = "DisplayString"
_ApCntsvcOwnName_Object = MibTableColumn
apCntsvcOwnName = _ApCntsvcOwnName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 1),
    _ApCntsvcOwnName_Type()
)
apCntsvcOwnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcOwnName.setStatus("current")


class _ApCntsvcCntName_Type(DisplayString):
    """Custom type apCntsvcCntName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcCntName_Type.__name__ = "DisplayString"
_ApCntsvcCntName_Object = MibTableColumn
apCntsvcCntName = _ApCntsvcCntName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 2),
    _ApCntsvcCntName_Type()
)
apCntsvcCntName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcCntName.setStatus("current")


class _ApCntsvcSvcName_Type(DisplayString):
    """Custom type apCntsvcSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ApCntsvcSvcName_Type.__name__ = "DisplayString"
_ApCntsvcSvcName_Object = MibTableColumn
apCntsvcSvcName = _ApCntsvcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 3),
    _ApCntsvcSvcName_Type()
)
apCntsvcSvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcSvcName.setStatus("current")


class _ApCntsvcHits_Type(Integer32):
    """Custom type apCntsvcHits based on Integer32"""
    defaultValue = 0


_ApCntsvcHits_Object = MibTableColumn
apCntsvcHits = _ApCntsvcHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 4),
    _ApCntsvcHits_Type()
)
apCntsvcHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcHits.setStatus("current")


class _ApCntsvcBytes_Type(Integer32):
    """Custom type apCntsvcBytes based on Integer32"""
    defaultValue = 0


_ApCntsvcBytes_Object = MibTableColumn
apCntsvcBytes = _ApCntsvcBytes_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 5),
    _ApCntsvcBytes_Type()
)
apCntsvcBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcBytes.setStatus("current")


class _ApCntsvcFrames_Type(Integer32):
    """Custom type apCntsvcFrames based on Integer32"""
    defaultValue = 0


_ApCntsvcFrames_Object = MibTableColumn
apCntsvcFrames = _ApCntsvcFrames_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 6),
    _ApCntsvcFrames_Type()
)
apCntsvcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcFrames.setStatus("current")


class _ApCntsvcBucket_Type(Integer32):
    """Custom type apCntsvcBucket based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ApCntsvcBucket_Type.__name__ = "Integer32"
_ApCntsvcBucket_Object = MibTableColumn
apCntsvcBucket = _ApCntsvcBucket_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 7),
    _ApCntsvcBucket_Type()
)
apCntsvcBucket.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcBucket.setStatus("current")
_ApCntsvcStatus_Type = RowStatus
_ApCntsvcStatus_Object = MibTableColumn
apCntsvcStatus = _ApCntsvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 8),
    _ApCntsvcStatus_Type()
)
apCntsvcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcStatus.setStatus("current")


class _ApCntsvcWeight_Type(Integer32):
    """Custom type apCntsvcWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApCntsvcWeight_Type.__name__ = "Integer32"
_ApCntsvcWeight_Object = MibTableColumn
apCntsvcWeight = _ApCntsvcWeight_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 9),
    _ApCntsvcWeight_Type()
)
apCntsvcWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apCntsvcWeight.setStatus("current")


class _ApCntsvcDnsHits_Type(Integer32):
    """Custom type apCntsvcDnsHits based on Integer32"""
    defaultValue = 0


_ApCntsvcDnsHits_Object = MibTableColumn
apCntsvcDnsHits = _ApCntsvcDnsHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 10),
    _ApCntsvcDnsHits_Type()
)
apCntsvcDnsHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDnsHits.setStatus("current")


class _ApCntsvcDnsProximityHits_Type(Integer32):
    """Custom type apCntsvcDnsProximityHits based on Integer32"""
    defaultValue = 0


_ApCntsvcDnsProximityHits_Object = MibTableColumn
apCntsvcDnsProximityHits = _ApCntsvcDnsProximityHits_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 11),
    _ApCntsvcDnsProximityHits_Type()
)
apCntsvcDnsProximityHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcDnsProximityHits.setStatus("current")


class _ApCntsvcState_Type(Integer32):
    """Custom type apCntsvcState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alive", 4),
          ("down", 2),
          ("suspended", 1))
    )


_ApCntsvcState_Type.__name__ = "Integer32"
_ApCntsvcState_Object = MibTableColumn
apCntsvcState = _ApCntsvcState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 18, 2, 1, 12),
    _ApCntsvcState_Type()
)
apCntsvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apCntsvcState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNTSVCEXT-MIB",
    **{"apCntsvcExtMib": apCntsvcExtMib,
       "apCntsvcTable": apCntsvcTable,
       "apCntsvcEntry": apCntsvcEntry,
       "apCntsvcOwnName": apCntsvcOwnName,
       "apCntsvcCntName": apCntsvcCntName,
       "apCntsvcSvcName": apCntsvcSvcName,
       "apCntsvcHits": apCntsvcHits,
       "apCntsvcBytes": apCntsvcBytes,
       "apCntsvcFrames": apCntsvcFrames,
       "apCntsvcBucket": apCntsvcBucket,
       "apCntsvcStatus": apCntsvcStatus,
       "apCntsvcWeight": apCntsvcWeight,
       "apCntsvcDnsHits": apCntsvcDnsHits,
       "apCntsvcDnsProximityHits": apCntsvcDnsProximityHits,
       "apCntsvcState": apCntsvcState}
)
