# SNMP MIB module (AVAYA-APPL-MEM-MANAGER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-APPL-MEM-MANAGER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:29 2024
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

(avGatewayMibs,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "avGatewayMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

avApplMemManager = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvApplMemManagerGenConfig_ObjectIdentity = ObjectIdentity
avApplMemManagerGenConfig = _AvApplMemManagerGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1)
)
_AvApplMemManagerTotalRamSize_Type = Integer32
_AvApplMemManagerTotalRamSize_Object = MibScalar
avApplMemManagerTotalRamSize = _AvApplMemManagerTotalRamSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1, 1),
    _AvApplMemManagerTotalRamSize_Type()
)
avApplMemManagerTotalRamSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avApplMemManagerTotalRamSize.setStatus("current")
_AvApplMemManagerTotalNvRamSize_Type = Integer32
_AvApplMemManagerTotalNvRamSize_Object = MibScalar
avApplMemManagerTotalNvRamSize = _AvApplMemManagerTotalNvRamSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 1, 2),
    _AvApplMemManagerTotalNvRamSize_Type()
)
avApplMemManagerTotalNvRamSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avApplMemManagerTotalNvRamSize.setStatus("current")
_AvApplMemManagerTable_Object = MibTable
avApplMemManagerTable = _AvApplMemManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2)
)
if mibBuilder.loadTexts:
    avApplMemManagerTable.setStatus("current")
_AvApplMemManagerEntry_Object = MibTableRow
avApplMemManagerEntry = _AvApplMemManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1)
)
avApplMemManagerEntry.setIndexNames(
    (0, "AVAYA-APPL-MEM-MANAGER", "avApplMemManagerId"),
    (0, "AVAYA-APPL-MEM-MANAGER", "avApplMemManagerType"),
)
if mibBuilder.loadTexts:
    avApplMemManagerEntry.setStatus("current")
_AvApplMemManagerId_Type = Integer32
_AvApplMemManagerId_Object = MibTableColumn
avApplMemManagerId = _AvApplMemManagerId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 1),
    _AvApplMemManagerId_Type()
)
avApplMemManagerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avApplMemManagerId.setStatus("current")
_AvApplMemManagerType_Type = Integer32
_AvApplMemManagerType_Object = MibTableColumn
avApplMemManagerType = _AvApplMemManagerType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 2),
    _AvApplMemManagerType_Type()
)
avApplMemManagerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avApplMemManagerType.setStatus("current")
_AvApplMemManagerName_Type = DisplayString
_AvApplMemManagerName_Object = MibTableColumn
avApplMemManagerName = _AvApplMemManagerName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 3),
    _AvApplMemManagerName_Type()
)
avApplMemManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avApplMemManagerName.setStatus("current")
_AvApplMemManagerSize_Type = Integer32
_AvApplMemManagerSize_Object = MibTableColumn
avApplMemManagerSize = _AvApplMemManagerSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 4),
    _AvApplMemManagerSize_Type()
)
avApplMemManagerSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avApplMemManagerSize.setStatus("current")
_AvApplMemManagerMinSize_Type = Integer32
_AvApplMemManagerMinSize_Object = MibTableColumn
avApplMemManagerMinSize = _AvApplMemManagerMinSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 5),
    _AvApplMemManagerMinSize_Type()
)
avApplMemManagerMinSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avApplMemManagerMinSize.setStatus("current")
_AvApplMemManagerMaxSize_Type = Integer32
_AvApplMemManagerMaxSize_Object = MibTableColumn
avApplMemManagerMaxSize = _AvApplMemManagerMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 6, 3, 2, 1, 6),
    _AvApplMemManagerMaxSize_Type()
)
avApplMemManagerMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avApplMemManagerMaxSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-APPL-MEM-MANAGER",
    **{"avApplMemManager": avApplMemManager,
       "avApplMemManagerGenConfig": avApplMemManagerGenConfig,
       "avApplMemManagerTotalRamSize": avApplMemManagerTotalRamSize,
       "avApplMemManagerTotalNvRamSize": avApplMemManagerTotalNvRamSize,
       "avApplMemManagerTable": avApplMemManagerTable,
       "avApplMemManagerEntry": avApplMemManagerEntry,
       "avApplMemManagerId": avApplMemManagerId,
       "avApplMemManagerType": avApplMemManagerType,
       "avApplMemManagerName": avApplMemManagerName,
       "avApplMemManagerSize": avApplMemManagerSize,
       "avApplMemManagerMinSize": avApplMemManagerMinSize,
       "avApplMemManagerMaxSize": avApplMemManagerMaxSize}
)
