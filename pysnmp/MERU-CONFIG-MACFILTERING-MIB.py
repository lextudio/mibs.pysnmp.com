# SNMP MIB module (MERU-CONFIG-MACFILTERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-MACFILTERING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:03 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlAclEnvState,) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlAclEnvState")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigMacFiltering = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwAcl_ObjectIdentity = ObjectIdentity
mwAcl = _MwAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1)
)
_MwAclEnvState_Type = MwlAclEnvState
_MwAclEnvState_Object = MibScalar
mwAclEnvState = _MwAclEnvState_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1, 1),
    _MwAclEnvState_Type()
)
mwAclEnvState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAclEnvState.setStatus("current")
_MwAclRadiusProfileName_Type = DisplayString
_MwAclRadiusProfileName_Object = MibScalar
mwAclRadiusProfileName = _MwAclRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1, 2),
    _MwAclRadiusProfileName_Type()
)
mwAclRadiusProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAclRadiusProfileName.setStatus("current")
_MwAclSecondaryRadiusProfileName_Type = DisplayString
_MwAclSecondaryRadiusProfileName_Object = MibScalar
mwAclSecondaryRadiusProfileName = _MwAclSecondaryRadiusProfileName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1, 3),
    _MwAclSecondaryRadiusProfileName_Type()
)
mwAclSecondaryRadiusProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAclSecondaryRadiusProfileName.setStatus("current")
_MwAclAccessAllowTable_Object = MibTable
mwAclAccessAllowTable = _MwAclAccessAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    mwAclAccessAllowTable.setStatus("current")
_MwAclAccessAllowEntry_Object = MibTableRow
mwAclAccessAllowEntry = _MwAclAccessAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1)
)
mwAclAccessAllowEntry.setIndexNames(
    (0, "MERU-CONFIG-MACFILTERING-MIB", "mwAclAccessAllowTableIndex"),
)
if mibBuilder.loadTexts:
    mwAclAccessAllowEntry.setStatus("current")
_MwAclAccessAllowTableIndex_Type = Integer32
_MwAclAccessAllowTableIndex_Object = MibTableColumn
mwAclAccessAllowTableIndex = _MwAclAccessAllowTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 1),
    _MwAclAccessAllowTableIndex_Type()
)
mwAclAccessAllowTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAclAccessAllowTableIndex.setStatus("current")
_MwAclAccessAllowMac_Type = MacAddress
_MwAclAccessAllowMac_Object = MibTableColumn
mwAclAccessAllowMac = _MwAclAccessAllowMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 2),
    _MwAclAccessAllowMac_Type()
)
mwAclAccessAllowMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowMac.setStatus("current")


class _MwAclAccessAllowDescr_Type(DisplayString):
    """Custom type mwAclAccessAllowDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MwAclAccessAllowDescr_Type.__name__ = "DisplayString"
_MwAclAccessAllowDescr_Object = MibTableColumn
mwAclAccessAllowDescr = _MwAclAccessAllowDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 3),
    _MwAclAccessAllowDescr_Type()
)
mwAclAccessAllowDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowDescr.setStatus("current")
_MwAclAccessAllowRowStatus_Type = RowStatus
_MwAclAccessAllowRowStatus_Object = MibTableColumn
mwAclAccessAllowRowStatus = _MwAclAccessAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 5),
    _MwAclAccessAllowRowStatus_Type()
)
mwAclAccessAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowRowStatus.setStatus("current")
_MwAclAccessDenyTable_Object = MibTable
mwAclAccessDenyTable = _MwAclAccessDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3)
)
if mibBuilder.loadTexts:
    mwAclAccessDenyTable.setStatus("current")
_MwAclAccessDenyEntry_Object = MibTableRow
mwAclAccessDenyEntry = _MwAclAccessDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1)
)
mwAclAccessDenyEntry.setIndexNames(
    (0, "MERU-CONFIG-MACFILTERING-MIB", "mwAclAccessDenyTableIndex"),
)
if mibBuilder.loadTexts:
    mwAclAccessDenyEntry.setStatus("current")
_MwAclAccessDenyTableIndex_Type = Integer32
_MwAclAccessDenyTableIndex_Object = MibTableColumn
mwAclAccessDenyTableIndex = _MwAclAccessDenyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 1),
    _MwAclAccessDenyTableIndex_Type()
)
mwAclAccessDenyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAclAccessDenyTableIndex.setStatus("current")
_MwAclAccessDenyMac_Type = MacAddress
_MwAclAccessDenyMac_Object = MibTableColumn
mwAclAccessDenyMac = _MwAclAccessDenyMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 2),
    _MwAclAccessDenyMac_Type()
)
mwAclAccessDenyMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyMac.setStatus("current")


class _MwAclAccessDenyDescr_Type(DisplayString):
    """Custom type mwAclAccessDenyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MwAclAccessDenyDescr_Type.__name__ = "DisplayString"
_MwAclAccessDenyDescr_Object = MibTableColumn
mwAclAccessDenyDescr = _MwAclAccessDenyDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 3),
    _MwAclAccessDenyDescr_Type()
)
mwAclAccessDenyDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyDescr.setStatus("current")
_MwAclAccessDenyRowStatus_Type = RowStatus
_MwAclAccessDenyRowStatus_Object = MibTableColumn
mwAclAccessDenyRowStatus = _MwAclAccessDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 5),
    _MwAclAccessDenyRowStatus_Type()
)
mwAclAccessDenyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-MACFILTERING-MIB",
    **{"mwConfigMacFiltering": mwConfigMacFiltering,
       "mwAcl": mwAcl,
       "mwAclEnvState": mwAclEnvState,
       "mwAclRadiusProfileName": mwAclRadiusProfileName,
       "mwAclSecondaryRadiusProfileName": mwAclSecondaryRadiusProfileName,
       "mwAclAccessAllowTable": mwAclAccessAllowTable,
       "mwAclAccessAllowEntry": mwAclAccessAllowEntry,
       "mwAclAccessAllowTableIndex": mwAclAccessAllowTableIndex,
       "mwAclAccessAllowMac": mwAclAccessAllowMac,
       "mwAclAccessAllowDescr": mwAclAccessAllowDescr,
       "mwAclAccessAllowRowStatus": mwAclAccessAllowRowStatus,
       "mwAclAccessDenyTable": mwAclAccessDenyTable,
       "mwAclAccessDenyEntry": mwAclAccessDenyEntry,
       "mwAclAccessDenyTableIndex": mwAclAccessDenyTableIndex,
       "mwAclAccessDenyMac": mwAclAccessDenyMac,
       "mwAclAccessDenyDescr": mwAclAccessDenyDescr,
       "mwAclAccessDenyRowStatus": mwAclAccessDenyRowStatus}
)
