# SNMP MIB module (PDN-MPE-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:55 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mpe_domain,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-domain")

(ClientState,
 SwitchState,
 VnidRange,
 VnidTaggingState) = mibBuilder.importSymbols(
    "PDN-TC",
    "ClientState",
    "SwitchState",
    "VnidRange",
    "VnidTaggingState")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpePdnDomainMIBObjects_ObjectIdentity = ObjectIdentity
mpePdnDomainMIBObjects = _MpePdnDomainMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1)
)
_MpePdnCardGeneralParams_ObjectIdentity = ObjectIdentity
mpePdnCardGeneralParams = _MpePdnCardGeneralParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1)
)
_MpePdnCardGeneralParamsTable_Object = MibTable
mpePdnCardGeneralParamsTable = _MpePdnCardGeneralParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpePdnCardGeneralParamsTable.setStatus("mandatory")
_MpePdnCardGeneralParamsEntry_Object = MibTableRow
mpePdnCardGeneralParamsEntry = _MpePdnCardGeneralParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1)
)
mpePdnCardGeneralParamsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpePdnCardGeneralParamsEntry.setStatus("mandatory")
_MpePdnCardGeneralParamsVNIDMode_Type = VnidTaggingState
_MpePdnCardGeneralParamsVNIDMode_Object = MibTableColumn
mpePdnCardGeneralParamsVNIDMode = _MpePdnCardGeneralParamsVNIDMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1, 1),
    _MpePdnCardGeneralParamsVNIDMode_Type()
)
mpePdnCardGeneralParamsVNIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardGeneralParamsVNIDMode.setStatus("mandatory")
_MpePdnCardGeneralParamsAdditionalClientsAvailable_Type = Integer32
_MpePdnCardGeneralParamsAdditionalClientsAvailable_Object = MibTableColumn
mpePdnCardGeneralParamsAdditionalClientsAvailable = _MpePdnCardGeneralParamsAdditionalClientsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 1, 1, 1, 2),
    _MpePdnCardGeneralParamsAdditionalClientsAvailable_Type()
)
mpePdnCardGeneralParamsAdditionalClientsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnCardGeneralParamsAdditionalClientsAvailable.setStatus("mandatory")
_MpePdnCardConfig_ObjectIdentity = ObjectIdentity
mpePdnCardConfig = _MpePdnCardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2)
)
_MpePdnCardConfigTable_Object = MibTable
mpePdnCardConfigTable = _MpePdnCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpePdnCardConfigTable.setStatus("mandatory")
_MpePdnCardConfigEntry_Object = MibTableRow
mpePdnCardConfigEntry = _MpePdnCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1)
)
mpePdnCardConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-MPE-DOMAIN-MIB", "mpePdnCardConfigVnidId"),
)
if mibBuilder.loadTexts:
    mpePdnCardConfigEntry.setStatus("mandatory")
_MpePdnCardConfigVnidId_Type = VnidRange
_MpePdnCardConfigVnidId_Object = MibTableColumn
mpePdnCardConfigVnidId = _MpePdnCardConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 1),
    _MpePdnCardConfigVnidId_Type()
)
mpePdnCardConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpePdnCardConfigVnidId.setStatus("mandatory")
_MpePdnCardConfigDomainName_Type = DisplayString
_MpePdnCardConfigDomainName_Object = MibTableColumn
mpePdnCardConfigDomainName = _MpePdnCardConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 2),
    _MpePdnCardConfigDomainName_Type()
)
mpePdnCardConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigDomainName.setStatus("mandatory")
_MpePdnCardConfigMuxFwd_Type = SwitchState
_MpePdnCardConfigMuxFwd_Object = MibTableColumn
mpePdnCardConfigMuxFwd = _MpePdnCardConfigMuxFwd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 3),
    _MpePdnCardConfigMuxFwd_Type()
)
mpePdnCardConfigMuxFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigMuxFwd.setStatus("mandatory")
_MpePdnCardConfigIPFiltering_Type = SwitchState
_MpePdnCardConfigIPFiltering_Object = MibTableColumn
mpePdnCardConfigIPFiltering = _MpePdnCardConfigIPFiltering_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 4),
    _MpePdnCardConfigIPFiltering_Type()
)
mpePdnCardConfigIPFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigIPFiltering.setStatus("mandatory")
_MpePdnCardConfigIPScoping_Type = SwitchState
_MpePdnCardConfigIPScoping_Object = MibTableColumn
mpePdnCardConfigIPScoping = _MpePdnCardConfigIPScoping_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 5),
    _MpePdnCardConfigIPScoping_Type()
)
mpePdnCardConfigIPScoping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigIPScoping.setStatus("mandatory")
_MpePdnCardConfigVnidAuth_Type = SwitchState
_MpePdnCardConfigVnidAuth_Object = MibTableColumn
mpePdnCardConfigVnidAuth = _MpePdnCardConfigVnidAuth_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 6),
    _MpePdnCardConfigVnidAuth_Type()
)
mpePdnCardConfigVnidAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigVnidAuth.setStatus("mandatory")
_MpePdnCardConfigRowStatus_Type = RowStatus
_MpePdnCardConfigRowStatus_Object = MibTableColumn
mpePdnCardConfigRowStatus = _MpePdnCardConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 1, 2, 1, 1, 7),
    _MpePdnCardConfigRowStatus_Type()
)
mpePdnCardConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpePdnCardConfigRowStatus.setStatus("mandatory")
_MpePdnDomainMIBTraps_ObjectIdentity = ObjectIdentity
mpePdnDomainMIBTraps = _MpePdnDomainMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 22, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-DOMAIN-MIB",
    **{"mpePdnDomainMIBObjects": mpePdnDomainMIBObjects,
       "mpePdnCardGeneralParams": mpePdnCardGeneralParams,
       "mpePdnCardGeneralParamsTable": mpePdnCardGeneralParamsTable,
       "mpePdnCardGeneralParamsEntry": mpePdnCardGeneralParamsEntry,
       "mpePdnCardGeneralParamsVNIDMode": mpePdnCardGeneralParamsVNIDMode,
       "mpePdnCardGeneralParamsAdditionalClientsAvailable": mpePdnCardGeneralParamsAdditionalClientsAvailable,
       "mpePdnCardConfig": mpePdnCardConfig,
       "mpePdnCardConfigTable": mpePdnCardConfigTable,
       "mpePdnCardConfigEntry": mpePdnCardConfigEntry,
       "mpePdnCardConfigVnidId": mpePdnCardConfigVnidId,
       "mpePdnCardConfigDomainName": mpePdnCardConfigDomainName,
       "mpePdnCardConfigMuxFwd": mpePdnCardConfigMuxFwd,
       "mpePdnCardConfigIPFiltering": mpePdnCardConfigIPFiltering,
       "mpePdnCardConfigIPScoping": mpePdnCardConfigIPScoping,
       "mpePdnCardConfigVnidAuth": mpePdnCardConfigVnidAuth,
       "mpePdnCardConfigRowStatus": mpePdnCardConfigRowStatus,
       "mpePdnDomainMIBTraps": mpePdnDomainMIBTraps}
)
