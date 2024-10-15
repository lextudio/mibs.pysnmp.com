# SNMP MIB module (PDN-MPE-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:52 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(mpe_arp,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-arp")

(SwitchState,
 VnidRange) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState",
    "VnidRange")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class Bit32(Integer32):
    """Custom type Bit32 based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpePdnNetToMediaGenericMIBObjects_ObjectIdentity = ObjectIdentity
mpePdnNetToMediaGenericMIBObjects = _MpePdnNetToMediaGenericMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1)
)
_MpePdnNetTo8023MediaParams_ObjectIdentity = ObjectIdentity
mpePdnNetTo8023MediaParams = _MpePdnNetTo8023MediaParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1)
)
_MpePdnNetTo8023MediaParamsTable_Object = MibTable
mpePdnNetTo8023MediaParamsTable = _MpePdnNetTo8023MediaParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpePdnNetTo8023MediaParamsTable.setStatus("mandatory")
_MpePdnNetTo8023MediaParamsEntry_Object = MibTableRow
mpePdnNetTo8023MediaParamsEntry = _MpePdnNetTo8023MediaParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1)
)
mpePdnNetTo8023MediaParamsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpePdnNetTo8023MediaParamsEntry.setStatus("mandatory")


class _MpePdnNetTo8023MediaParamsCompEntryTimeout_Type(Integer32):
    """Custom type mpePdnNetTo8023MediaParamsCompEntryTimeout based on Integer32"""
    defaultValue = 20


_MpePdnNetTo8023MediaParamsCompEntryTimeout_Object = MibTableColumn
mpePdnNetTo8023MediaParamsCompEntryTimeout = _MpePdnNetTo8023MediaParamsCompEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 1),
    _MpePdnNetTo8023MediaParamsCompEntryTimeout_Type()
)
mpePdnNetTo8023MediaParamsCompEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnNetTo8023MediaParamsCompEntryTimeout.setStatus("mandatory")


class _MpePdnNetTo8023MediaParamsIncompEntryTimeout_Type(Integer32):
    """Custom type mpePdnNetTo8023MediaParamsIncompEntryTimeout based on Integer32"""
    defaultValue = 3


_MpePdnNetTo8023MediaParamsIncompEntryTimeout_Object = MibTableColumn
mpePdnNetTo8023MediaParamsIncompEntryTimeout = _MpePdnNetTo8023MediaParamsIncompEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 2),
    _MpePdnNetTo8023MediaParamsIncompEntryTimeout_Type()
)
mpePdnNetTo8023MediaParamsIncompEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnNetTo8023MediaParamsIncompEntryTimeout.setStatus("mandatory")


class _MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Type(Integer32):
    """Custom type mpePdnNetTo8023MediaParamsDefRouteEntryTimeout based on Integer32"""
    defaultValue = 1


_MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Object = MibTableColumn
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout = _MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 1, 1, 1, 3),
    _MpePdnNetTo8023MediaParamsDefRouteEntryTimeout_Type()
)
mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnNetTo8023MediaParamsDefRouteEntryTimeout.setStatus("mandatory")
_MpePdnNetTo8023MediaConfig_ObjectIdentity = ObjectIdentity
mpePdnNetTo8023MediaConfig = _MpePdnNetTo8023MediaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 1, 2)
)
_MpePdnNetToMediaMIBTraps_ObjectIdentity = ObjectIdentity
mpePdnNetToMediaMIBTraps = _MpePdnNetToMediaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 27, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-ARP-MIB",
    **{"Bit32": Bit32,
       "mpePdnNetToMediaGenericMIBObjects": mpePdnNetToMediaGenericMIBObjects,
       "mpePdnNetTo8023MediaParams": mpePdnNetTo8023MediaParams,
       "mpePdnNetTo8023MediaParamsTable": mpePdnNetTo8023MediaParamsTable,
       "mpePdnNetTo8023MediaParamsEntry": mpePdnNetTo8023MediaParamsEntry,
       "mpePdnNetTo8023MediaParamsCompEntryTimeout": mpePdnNetTo8023MediaParamsCompEntryTimeout,
       "mpePdnNetTo8023MediaParamsIncompEntryTimeout": mpePdnNetTo8023MediaParamsIncompEntryTimeout,
       "mpePdnNetTo8023MediaParamsDefRouteEntryTimeout": mpePdnNetTo8023MediaParamsDefRouteEntryTimeout,
       "mpePdnNetTo8023MediaConfig": mpePdnNetTo8023MediaConfig,
       "mpePdnNetToMediaMIBTraps": mpePdnNetToMediaMIBTraps}
)
