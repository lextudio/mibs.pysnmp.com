# SNMP MIB module (HOT-DOMAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HOT-DOMAIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:49 2024
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

(ent_8800,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "ent-8800")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDomain_ObjectIdentity = ObjectIdentity
pdnDomain = _PdnDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6)
)
_PdnCardConfig_ObjectIdentity = ObjectIdentity
pdnCardConfig = _PdnCardConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1)
)
_PdnCardConfigTable_Object = MibTable
pdnCardConfigTable = _PdnCardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    pdnCardConfigTable.setStatus("mandatory")
_PdnCardConfigEntry_Object = MibTableRow
pdnCardConfigEntry = _PdnCardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1)
)
pdnCardConfigEntry.setIndexNames(
    (0, "HOT-DOMAIN-MIB", "pdnCardConfigVnidId"),
)
if mibBuilder.loadTexts:
    pdnCardConfigEntry.setStatus("mandatory")


class _PdnCardConfigVnidId_Type(Integer32):
    """Custom type pdnCardConfigVnidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_PdnCardConfigVnidId_Type.__name__ = "Integer32"
_PdnCardConfigVnidId_Object = MibTableColumn
pdnCardConfigVnidId = _PdnCardConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 1),
    _PdnCardConfigVnidId_Type()
)
pdnCardConfigVnidId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigVnidId.setStatus("mandatory")
_PdnCardConfigDomainName_Type = DisplayString
_PdnCardConfigDomainName_Object = MibTableColumn
pdnCardConfigDomainName = _PdnCardConfigDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 2),
    _PdnCardConfigDomainName_Type()
)
pdnCardConfigDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigDomainName.setStatus("mandatory")


class _PdnCardConfigMuxFwd_Type(Integer32):
    """Custom type pdnCardConfigMuxFwd based on Integer32"""
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


_PdnCardConfigMuxFwd_Type.__name__ = "Integer32"
_PdnCardConfigMuxFwd_Object = MibTableColumn
pdnCardConfigMuxFwd = _PdnCardConfigMuxFwd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 3),
    _PdnCardConfigMuxFwd_Type()
)
pdnCardConfigMuxFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigMuxFwd.setStatus("mandatory")


class _PdnCardConfigIPFiltering_Type(Integer32):
    """Custom type pdnCardConfigIPFiltering based on Integer32"""
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


_PdnCardConfigIPFiltering_Type.__name__ = "Integer32"
_PdnCardConfigIPFiltering_Object = MibTableColumn
pdnCardConfigIPFiltering = _PdnCardConfigIPFiltering_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 4),
    _PdnCardConfigIPFiltering_Type()
)
pdnCardConfigIPFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigIPFiltering.setStatus("mandatory")


class _PdnCardConfigIPScoping_Type(Integer32):
    """Custom type pdnCardConfigIPScoping based on Integer32"""
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


_PdnCardConfigIPScoping_Type.__name__ = "Integer32"
_PdnCardConfigIPScoping_Object = MibTableColumn
pdnCardConfigIPScoping = _PdnCardConfigIPScoping_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 5),
    _PdnCardConfigIPScoping_Type()
)
pdnCardConfigIPScoping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigIPScoping.setStatus("mandatory")


class _PdnCardConfigDbUpdate_Type(Integer32):
    """Custom type pdnCardConfigDbUpdate based on Integer32"""
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
          ("nop", 1),
          ("update", 2))
    )


_PdnCardConfigDbUpdate_Type.__name__ = "Integer32"
_PdnCardConfigDbUpdate_Object = MibTableColumn
pdnCardConfigDbUpdate = _PdnCardConfigDbUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 1, 1, 1, 6),
    _PdnCardConfigDbUpdate_Type()
)
pdnCardConfigDbUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardConfigDbUpdate.setStatus("mandatory")
_PdnPortConfig_ObjectIdentity = ObjectIdentity
pdnPortConfig = _PdnPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2)
)
_PdnPortConfigTable_Object = MibTable
pdnPortConfigTable = _PdnPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigTable.setStatus("mandatory")
_PdnPortConfigEntry_Object = MibTableRow
pdnPortConfigEntry = _PdnPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1)
)
pdnPortConfigEntry.setIndexNames(
    (0, "HOT-DOMAIN-MIB", "pdnPortConfigVNID"),
    (0, "HOT-DOMAIN-MIB", "pdnPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    pdnPortConfigEntry.setStatus("mandatory")


class _PdnPortConfigVNID_Type(Integer32):
    """Custom type pdnPortConfigVNID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PdnPortConfigVNID_Type.__name__ = "Integer32"
_PdnPortConfigVNID_Object = MibTableColumn
pdnPortConfigVNID = _PdnPortConfigVNID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1, 1),
    _PdnPortConfigVNID_Type()
)
pdnPortConfigVNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPortConfigVNID.setStatus("mandatory")
_PdnPortConfigIfIndex_Type = Integer32
_PdnPortConfigIfIndex_Object = MibTableColumn
pdnPortConfigIfIndex = _PdnPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1, 2),
    _PdnPortConfigIfIndex_Type()
)
pdnPortConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnPortConfigIfIndex.setStatus("mandatory")


class _PdnPortConfigCfg_Type(Integer32):
    """Custom type pdnPortConfigCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("de-activate", 2))
    )


_PdnPortConfigCfg_Type.__name__ = "Integer32"
_PdnPortConfigCfg_Object = MibTableColumn
pdnPortConfigCfg = _PdnPortConfigCfg_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1, 3),
    _PdnPortConfigCfg_Type()
)
pdnPortConfigCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigCfg.setStatus("mandatory")
_PdnPortConfigDefNHR_Type = IpAddress
_PdnPortConfigDefNHR_Object = MibTableColumn
pdnPortConfigDefNHR = _PdnPortConfigDefNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1, 4),
    _PdnPortConfigDefNHR_Type()
)
pdnPortConfigDefNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigDefNHR.setStatus("mandatory")


class _PdnPortConfigMode_Type(Integer32):
    """Custom type pdnPortConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("explicit", 2),
          ("implicit", 1),
          ("no-tagging", 3))
    )


_PdnPortConfigMode_Type.__name__ = "Integer32"
_PdnPortConfigMode_Object = MibTableColumn
pdnPortConfigMode = _PdnPortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 2, 1, 1, 5),
    _PdnPortConfigMode_Type()
)
pdnPortConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigMode.setStatus("mandatory")
_PdnClientConfig_ObjectIdentity = ObjectIdentity
pdnClientConfig = _PdnClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3)
)
_PdnClientConfigTable_Object = MibTable
pdnClientConfigTable = _PdnClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1)
)
if mibBuilder.loadTexts:
    pdnClientConfigTable.setStatus("mandatory")
_PdnClientConfigEntry_Object = MibTableRow
pdnClientConfigEntry = _PdnClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1)
)
pdnClientConfigEntry.setIndexNames(
    (0, "HOT-DOMAIN-MIB", "pdnClientConfigIfIndex"),
    (0, "HOT-DOMAIN-MIB", "pdnClientConfigClientIndex"),
)
if mibBuilder.loadTexts:
    pdnClientConfigEntry.setStatus("mandatory")
_PdnClientConfigIfIndex_Type = Integer32
_PdnClientConfigIfIndex_Object = MibTableColumn
pdnClientConfigIfIndex = _PdnClientConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 1),
    _PdnClientConfigIfIndex_Type()
)
pdnClientConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigIfIndex.setStatus("mandatory")


class _PdnClientConfigClientIndex_Type(Integer32):
    """Custom type pdnClientConfigClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_PdnClientConfigClientIndex_Type.__name__ = "Integer32"
_PdnClientConfigClientIndex_Object = MibTableColumn
pdnClientConfigClientIndex = _PdnClientConfigClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 2),
    _PdnClientConfigClientIndex_Type()
)
pdnClientConfigClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigClientIndex.setStatus("mandatory")
_PdnClientConfigAddr_Type = IpAddress
_PdnClientConfigAddr_Object = MibTableColumn
pdnClientConfigAddr = _PdnClientConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 3),
    _PdnClientConfigAddr_Type()
)
pdnClientConfigAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnClientConfigAddr.setStatus("mandatory")
_PdnClientConfigNHR_Type = IpAddress
_PdnClientConfigNHR_Object = MibTableColumn
pdnClientConfigNHR = _PdnClientConfigNHR_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 4),
    _PdnClientConfigNHR_Type()
)
pdnClientConfigNHR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnClientConfigNHR.setStatus("mandatory")


class _PdnClientConfigVnidId_Type(Integer32):
    """Custom type pdnClientConfigVnidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PdnClientConfigVnidId_Type.__name__ = "Integer32"
_PdnClientConfigVnidId_Object = MibTableColumn
pdnClientConfigVnidId = _PdnClientConfigVnidId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 5),
    _PdnClientConfigVnidId_Type()
)
pdnClientConfigVnidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigVnidId.setStatus("mandatory")


class _PdnClientConfigType_Type(Integer32):
    """Custom type pdnClientConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_PdnClientConfigType_Type.__name__ = "Integer32"
_PdnClientConfigType_Object = MibTableColumn
pdnClientConfigType = _PdnClientConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 6),
    _PdnClientConfigType_Type()
)
pdnClientConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigType.setStatus("mandatory")
_PdnClientConfigLeaseTime_Type = Integer32
_PdnClientConfigLeaseTime_Object = MibTableColumn
pdnClientConfigLeaseTime = _PdnClientConfigLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 7),
    _PdnClientConfigLeaseTime_Type()
)
pdnClientConfigLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigLeaseTime.setStatus("mandatory")
_PdnClientConfigLeaseRemainTime_Type = Integer32
_PdnClientConfigLeaseRemainTime_Object = MibTableColumn
pdnClientConfigLeaseRemainTime = _PdnClientConfigLeaseRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 8),
    _PdnClientConfigLeaseRemainTime_Type()
)
pdnClientConfigLeaseRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigLeaseRemainTime.setStatus("mandatory")
_PdnClientConfigMacAddr_Type = MacAddress
_PdnClientConfigMacAddr_Object = MibTableColumn
pdnClientConfigMacAddr = _PdnClientConfigMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 9),
    _PdnClientConfigMacAddr_Type()
)
pdnClientConfigMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigMacAddr.setStatus("mandatory")
_PdnClientConfigSubnetMask_Type = IpAddress
_PdnClientConfigSubnetMask_Object = MibTableColumn
pdnClientConfigSubnetMask = _PdnClientConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 3, 1, 1, 10),
    _PdnClientConfigSubnetMask_Type()
)
pdnClientConfigSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnClientConfigSubnetMask.setStatus("mandatory")
_PdnCardGeneralParams_ObjectIdentity = ObjectIdentity
pdnCardGeneralParams = _PdnCardGeneralParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 4)
)


class _PdnCardGeneralParamsVNIDMode_Type(Integer32):
    """Custom type pdnCardGeneralParamsVNIDMode based on Integer32"""
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


_PdnCardGeneralParamsVNIDMode_Type.__name__ = "Integer32"
_PdnCardGeneralParamsVNIDMode_Object = MibScalar
pdnCardGeneralParamsVNIDMode = _PdnCardGeneralParamsVNIDMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 3, 6, 4, 1),
    _PdnCardGeneralParamsVNIDMode_Type()
)
pdnCardGeneralParamsVNIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCardGeneralParamsVNIDMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HOT-DOMAIN-MIB",
    **{"MacAddress": MacAddress,
       "pdnDomain": pdnDomain,
       "pdnCardConfig": pdnCardConfig,
       "pdnCardConfigTable": pdnCardConfigTable,
       "pdnCardConfigEntry": pdnCardConfigEntry,
       "pdnCardConfigVnidId": pdnCardConfigVnidId,
       "pdnCardConfigDomainName": pdnCardConfigDomainName,
       "pdnCardConfigMuxFwd": pdnCardConfigMuxFwd,
       "pdnCardConfigIPFiltering": pdnCardConfigIPFiltering,
       "pdnCardConfigIPScoping": pdnCardConfigIPScoping,
       "pdnCardConfigDbUpdate": pdnCardConfigDbUpdate,
       "pdnPortConfig": pdnPortConfig,
       "pdnPortConfigTable": pdnPortConfigTable,
       "pdnPortConfigEntry": pdnPortConfigEntry,
       "pdnPortConfigVNID": pdnPortConfigVNID,
       "pdnPortConfigIfIndex": pdnPortConfigIfIndex,
       "pdnPortConfigCfg": pdnPortConfigCfg,
       "pdnPortConfigDefNHR": pdnPortConfigDefNHR,
       "pdnPortConfigMode": pdnPortConfigMode,
       "pdnClientConfig": pdnClientConfig,
       "pdnClientConfigTable": pdnClientConfigTable,
       "pdnClientConfigEntry": pdnClientConfigEntry,
       "pdnClientConfigIfIndex": pdnClientConfigIfIndex,
       "pdnClientConfigClientIndex": pdnClientConfigClientIndex,
       "pdnClientConfigAddr": pdnClientConfigAddr,
       "pdnClientConfigNHR": pdnClientConfigNHR,
       "pdnClientConfigVnidId": pdnClientConfigVnidId,
       "pdnClientConfigType": pdnClientConfigType,
       "pdnClientConfigLeaseTime": pdnClientConfigLeaseTime,
       "pdnClientConfigLeaseRemainTime": pdnClientConfigLeaseRemainTime,
       "pdnClientConfigMacAddr": pdnClientConfigMacAddr,
       "pdnClientConfigSubnetMask": pdnClientConfigSubnetMask,
       "pdnCardGeneralParams": pdnCardGeneralParams,
       "pdnCardGeneralParamsVNIDMode": pdnCardGeneralParamsVNIDMode}
)
