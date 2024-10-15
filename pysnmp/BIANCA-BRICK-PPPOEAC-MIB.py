# SNMP MIB module (BIANCA-BRICK-PPPOEAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PPPOEAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:41 2024
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
 enterprises,
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
    "enterprises",
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

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Pppoe_ObjectIdentity = ObjectIdentity
pppoe = _Pppoe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 24)
)
_PppoeAcTable_Object = MibTable
pppoeAcTable = _PppoeAcTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 3)
)
if mibBuilder.loadTexts:
    pppoeAcTable.setStatus("mandatory")
_PppoeAcEntry_Object = MibTableRow
pppoeAcEntry = _PppoeAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 3, 1)
)
pppoeAcEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPPOEAC-MIB", "pppoeAcEthIfIndex"),
)
if mibBuilder.loadTexts:
    pppoeAcEntry.setStatus("mandatory")
_PppoeAcEthIfIndex_Type = Integer32
_PppoeAcEthIfIndex_Object = MibTableColumn
pppoeAcEthIfIndex = _PppoeAcEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 3, 1, 1),
    _PppoeAcEthIfIndex_Type()
)
pppoeAcEthIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcEthIfIndex.setStatus("mandatory")


class _PppoeAcChkService_Type(Integer32):
    """Custom type pppoeAcChkService based on Integer32"""
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
        *(("accept-all", 1),
          ("accept-from-list", 2),
          ("delete", 4))
    )


_PppoeAcChkService_Type.__name__ = "Integer32"
_PppoeAcChkService_Object = MibTableColumn
pppoeAcChkService = _PppoeAcChkService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 3, 1, 2),
    _PppoeAcChkService_Type()
)
pppoeAcChkService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcChkService.setStatus("mandatory")
_PppoeAcName_Type = DisplayString
_PppoeAcName_Object = MibTableColumn
pppoeAcName = _PppoeAcName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 3, 1, 3),
    _PppoeAcName_Type()
)
pppoeAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcName.setStatus("mandatory")
_PppoeAcServiceTable_Object = MibTable
pppoeAcServiceTable = _PppoeAcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 4)
)
if mibBuilder.loadTexts:
    pppoeAcServiceTable.setStatus("mandatory")
_PppoeAcServiceEntry_Object = MibTableRow
pppoeAcServiceEntry = _PppoeAcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 4, 1)
)
pppoeAcServiceEntry.setIndexNames(
    (0, "BIANCA-BRICK-PPPOEAC-MIB", "pppoeAcServiceEthIfIndex"),
)
if mibBuilder.loadTexts:
    pppoeAcServiceEntry.setStatus("mandatory")
_PppoeAcServiceEthIfIndex_Type = Integer32
_PppoeAcServiceEthIfIndex_Object = MibTableColumn
pppoeAcServiceEthIfIndex = _PppoeAcServiceEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 4, 1, 1),
    _PppoeAcServiceEthIfIndex_Type()
)
pppoeAcServiceEthIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcServiceEthIfIndex.setStatus("mandatory")
_PppoeAcServiceName_Type = DisplayString
_PppoeAcServiceName_Object = MibTableColumn
pppoeAcServiceName = _PppoeAcServiceName_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 4, 1, 2),
    _PppoeAcServiceName_Type()
)
pppoeAcServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcServiceName.setStatus("mandatory")


class _PppoeAcServiceStatus_Type(Integer32):
    """Custom type pppoeAcServiceStatus based on Integer32"""
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
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_PppoeAcServiceStatus_Type.__name__ = "Integer32"
_PppoeAcServiceStatus_Object = MibTableColumn
pppoeAcServiceStatus = _PppoeAcServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 24, 4, 1, 3),
    _PppoeAcServiceStatus_Type()
)
pppoeAcServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcServiceStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PPPOEAC-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "pppoe": pppoe,
       "pppoeAcTable": pppoeAcTable,
       "pppoeAcEntry": pppoeAcEntry,
       "pppoeAcEthIfIndex": pppoeAcEthIfIndex,
       "pppoeAcChkService": pppoeAcChkService,
       "pppoeAcName": pppoeAcName,
       "pppoeAcServiceTable": pppoeAcServiceTable,
       "pppoeAcServiceEntry": pppoeAcServiceEntry,
       "pppoeAcServiceEthIfIndex": pppoeAcServiceEthIfIndex,
       "pppoeAcServiceName": pppoeAcServiceName,
       "pppoeAcServiceStatus": pppoeAcServiceStatus}
)
