# SNMP MIB module (PNNI-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PNNI-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:07 2024
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

(extensions,) = mibBuilder.importSymbols(
    "CENTILLION-ROOT-MIB",
    "extensions")

(lecsConfIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "lecsConfIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnPnniExt_ObjectIdentity = ObjectIdentity
cnPnniExt = _CnPnniExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 5)
)
_CnPnniMainExt_ObjectIdentity = ObjectIdentity
cnPnniMainExt = _CnPnniMainExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 1)
)


class _CnPnniAdminStatus_Type(Integer32):
    """Custom type cnPnniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CnPnniAdminStatus_Type.__name__ = "Integer32"
_CnPnniAdminStatus_Object = MibScalar
cnPnniAdminStatus = _CnPnniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 1, 1),
    _CnPnniAdminStatus_Type()
)
cnPnniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnPnniAdminStatus.setStatus("mandatory")
_CnPnniCurNodes_Type = Integer32
_CnPnniCurNodes_Object = MibScalar
cnPnniCurNodes = _CnPnniCurNodes_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 1, 2),
    _CnPnniCurNodes_Type()
)
cnPnniCurNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnPnniCurNodes.setStatus("mandatory")
_CnPnnilecsExt_ObjectIdentity = ObjectIdentity
cnPnnilecsExt = _CnPnnilecsExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 2)
)
_LecsConfExtTable_Object = MibTable
lecsConfExtTable = _LecsConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lecsConfExtTable.setStatus("mandatory")
_LecsConfExtEntry_Object = MibTableRow
lecsConfExtEntry = _LecsConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 2, 1, 1)
)
lecsConfExtEntry.setIndexNames(
    (0, "LAN-EMULATION-ELAN-MIB", "lecsConfIndex"),
)
if mibBuilder.loadTexts:
    lecsConfExtEntry.setStatus("mandatory")


class _LecsConfExtScope_Type(Integer32):
    """Custom type lecsConfExtScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )


_LecsConfExtScope_Type.__name__ = "Integer32"
_LecsConfExtScope_Object = MibTableColumn
lecsConfExtScope = _LecsConfExtScope_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 2, 1, 1, 1),
    _LecsConfExtScope_Type()
)
lecsConfExtScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lecsConfExtScope.setStatus("mandatory")
_CnPnniTdbOverload_ObjectIdentity = ObjectIdentity
cnPnniTdbOverload = _CnPnniTdbOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 3)
)
_CnPnniMemConsumptionLowwater_Type = Integer32
_CnPnniMemConsumptionLowwater_Object = MibScalar
cnPnniMemConsumptionLowwater = _CnPnniMemConsumptionLowwater_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 3, 1),
    _CnPnniMemConsumptionLowwater_Type()
)
cnPnniMemConsumptionLowwater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnPnniMemConsumptionLowwater.setStatus("mandatory")
_CnPnniMemConsumptionHighwater_Type = Integer32
_CnPnniMemConsumptionHighwater_Object = MibScalar
cnPnniMemConsumptionHighwater = _CnPnniMemConsumptionHighwater_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 3, 2),
    _CnPnniMemConsumptionHighwater_Type()
)
cnPnniMemConsumptionHighwater.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnPnniMemConsumptionHighwater.setStatus("mandatory")
_CnPnniOverLoadRetryTime_Type = Integer32
_CnPnniOverLoadRetryTime_Object = MibScalar
cnPnniOverLoadRetryTime = _CnPnniOverLoadRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 930, 3, 5, 3, 3),
    _CnPnniOverLoadRetryTime_Type()
)
cnPnniOverLoadRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnPnniOverLoadRetryTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PNNI-EXT-MIB",
    **{"cnPnniExt": cnPnniExt,
       "cnPnniMainExt": cnPnniMainExt,
       "cnPnniAdminStatus": cnPnniAdminStatus,
       "cnPnniCurNodes": cnPnniCurNodes,
       "cnPnnilecsExt": cnPnnilecsExt,
       "lecsConfExtTable": lecsConfExtTable,
       "lecsConfExtEntry": lecsConfExtEntry,
       "lecsConfExtScope": lecsConfExtScope,
       "cnPnniTdbOverload": cnPnniTdbOverload,
       "cnPnniMemConsumptionLowwater": cnPnniMemConsumptionLowwater,
       "cnPnniMemConsumptionHighwater": cnPnniMemConsumptionHighwater,
       "cnPnniOverLoadRetryTime": cnPnniOverLoadRetryTime}
)
