# SNMP MIB module (HPN-ICF-SPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:53 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(IEEE8021SpbmSPsourceId,) = mibBuilder.importSymbols(
    "IEEE8021-SPB-MIB",
    "IEEE8021SpbmSPsourceId")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfSpb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128)
)
hpnicfSpb.setRevisions(
        ("2012-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSpbObjects_ObjectIdentity = ObjectIdentity
hpnicfSpbObjects = _HpnicfSpbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1)
)
_HpnicfSpbSysObjects_ObjectIdentity = ObjectIdentity
hpnicfSpbSysObjects = _HpnicfSpbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 1)
)


class _HpnicfSpbSysStatus_Type(Integer32):
    """Custom type hpnicfSpbSysStatus based on Integer32"""
    defaultValue = 2

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


_HpnicfSpbSysStatus_Type.__name__ = "Integer32"
_HpnicfSpbSysStatus_Object = MibScalar
hpnicfSpbSysStatus = _HpnicfSpbSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 1, 1),
    _HpnicfSpbSysStatus_Type()
)
hpnicfSpbSysStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSpbSysStatus.setStatus("current")


class _HpnicfSpbMulticastBVlanStatus_Type(Integer32):
    """Custom type hpnicfSpbMulticastBVlanStatus based on Integer32"""
    defaultValue = 2

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


_HpnicfSpbMulticastBVlanStatus_Type.__name__ = "Integer32"
_HpnicfSpbMulticastBVlanStatus_Object = MibScalar
hpnicfSpbMulticastBVlanStatus = _HpnicfSpbMulticastBVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 1, 2),
    _HpnicfSpbMulticastBVlanStatus_Type()
)
hpnicfSpbMulticastBVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSpbMulticastBVlanStatus.setStatus("current")
_HpnicfSpbConfig_ObjectIdentity = ObjectIdentity
hpnicfSpbConfig = _HpnicfSpbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2)
)
_HpnicfSpbIfTable_Object = MibTable
hpnicfSpbIfTable = _HpnicfSpbIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfSpbIfTable.setStatus("current")
_HpnicfSpbIfEntry_Object = MibTableRow
hpnicfSpbIfEntry = _HpnicfSpbIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 1, 1)
)
hpnicfSpbIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfSpbIfEntry.setStatus("current")


class _HpnicfSpbIfStatus_Type(Integer32):
    """Custom type hpnicfSpbIfStatus based on Integer32"""
    defaultValue = 2

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


_HpnicfSpbIfStatus_Type.__name__ = "Integer32"
_HpnicfSpbIfStatus_Object = MibTableColumn
hpnicfSpbIfStatus = _HpnicfSpbIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 1, 1, 1),
    _HpnicfSpbIfStatus_Type()
)
hpnicfSpbIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSpbIfStatus.setStatus("current")
_HpnicfSpbSrvTable_Object = MibTable
hpnicfSpbSrvTable = _HpnicfSpbSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfSpbSrvTable.setStatus("current")
_HpnicfSpbSrvEntry_Object = MibTableRow
hpnicfSpbSrvEntry = _HpnicfSpbSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2, 1)
)
hpnicfSpbSrvEntry.setIndexNames(
    (0, "HPN-ICF-SPB-MIB", "hpnicfSpbSrvTableEntryTopIx"),
    (0, "HPN-ICF-SPB-MIB", "hpnicfSpbSrvTableEntryIsid"),
)
if mibBuilder.loadTexts:
    hpnicfSpbSrvEntry.setStatus("current")
_HpnicfSpbSrvTableEntryTopIx_Type = Unsigned32
_HpnicfSpbSrvTableEntryTopIx_Object = MibTableColumn
hpnicfSpbSrvTableEntryTopIx = _HpnicfSpbSrvTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2, 1, 1),
    _HpnicfSpbSrvTableEntryTopIx_Type()
)
hpnicfSpbSrvTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSpbSrvTableEntryTopIx.setStatus("current")


class _HpnicfSpbSrvTableEntryIsid_Type(Unsigned32):
    """Custom type hpnicfSpbSrvTableEntryIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 16777215),
    )


_HpnicfSpbSrvTableEntryIsid_Type.__name__ = "Unsigned32"
_HpnicfSpbSrvTableEntryIsid_Object = MibTableColumn
hpnicfSpbSrvTableEntryIsid = _HpnicfSpbSrvTableEntryIsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2, 1, 2),
    _HpnicfSpbSrvTableEntryIsid_Type()
)
hpnicfSpbSrvTableEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSpbSrvTableEntryIsid.setStatus("current")
_HpnicfSpbSrvTableEntryBaseVid_Type = VlanIdOrNone
_HpnicfSpbSrvTableEntryBaseVid_Object = MibTableColumn
hpnicfSpbSrvTableEntryBaseVid = _HpnicfSpbSrvTableEntryBaseVid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2, 1, 3),
    _HpnicfSpbSrvTableEntryBaseVid_Type()
)
hpnicfSpbSrvTableEntryBaseVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSpbSrvTableEntryBaseVid.setStatus("current")


class _HpnicfSpbSrvTableEntryMode_Type(Integer32):
    """Custom type hpnicfSpbSrvTableEntryMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headEnd", 1),
          ("tandem", 2))
    )


_HpnicfSpbSrvTableEntryMode_Type.__name__ = "Integer32"
_HpnicfSpbSrvTableEntryMode_Object = MibTableColumn
hpnicfSpbSrvTableEntryMode = _HpnicfSpbSrvTableEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 2, 2, 1, 4),
    _HpnicfSpbSrvTableEntryMode_Type()
)
hpnicfSpbSrvTableEntryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSpbSrvTableEntryMode.setStatus("current")
_HpnicfSpbTrap_ObjectIdentity = ObjectIdentity
hpnicfSpbTrap = _HpnicfSpbTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3)
)
_HpnicfSpbTraps_ObjectIdentity = ObjectIdentity
hpnicfSpbTraps = _HpnicfSpbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 0)
)
_HpnicfSpbTrapsObjects_ObjectIdentity = ObjectIdentity
hpnicfSpbTrapsObjects = _HpnicfSpbTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 1)
)
_HpnicfSpbConflictSysID_Type = MacAddress
_HpnicfSpbConflictSysID_Object = MibScalar
hpnicfSpbConflictSysID = _HpnicfSpbConflictSysID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 1, 1),
    _HpnicfSpbConflictSysID_Type()
)
hpnicfSpbConflictSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSpbConflictSysID.setStatus("current")
_HpnicfSpbConflictSPSourceID_Type = IEEE8021SpbmSPsourceId
_HpnicfSpbConflictSPSourceID_Object = MibScalar
hpnicfSpbConflictSPSourceID = _HpnicfSpbConflictSPSourceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 1, 2),
    _HpnicfSpbConflictSPSourceID_Type()
)
hpnicfSpbConflictSPSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSpbConflictSPSourceID.setStatus("current")
_HpnicfSpbConflictBMac_Type = MacAddress
_HpnicfSpbConflictBMac_Object = MibScalar
hpnicfSpbConflictBMac = _HpnicfSpbConflictBMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 1, 3),
    _HpnicfSpbConflictBMac_Type()
)
hpnicfSpbConflictBMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfSpbConflictBMac.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfSpbSPSourceConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 0, 1)
)
hpnicfSpbSPSourceConflictTrap.setObjects(
      *(("HPN-ICF-SPB-MIB", "hpnicfSpbConflictSysID"),
        ("HPN-ICF-SPB-MIB", "hpnicfSpbConflictSPSourceID"))
)
if mibBuilder.loadTexts:
    hpnicfSpbSPSourceConflictTrap.setStatus(
        "current"
    )

hpnicfSpbBMacConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 128, 1, 3, 0, 2)
)
hpnicfSpbBMacConflictTrap.setObjects(
      *(("HPN-ICF-SPB-MIB", "hpnicfSpbConflictSysID"),
        ("HPN-ICF-SPB-MIB", "hpnicfSpbConflictBMac"))
)
if mibBuilder.loadTexts:
    hpnicfSpbBMacConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SPB-MIB",
    **{"hpnicfSpb": hpnicfSpb,
       "hpnicfSpbObjects": hpnicfSpbObjects,
       "hpnicfSpbSysObjects": hpnicfSpbSysObjects,
       "hpnicfSpbSysStatus": hpnicfSpbSysStatus,
       "hpnicfSpbMulticastBVlanStatus": hpnicfSpbMulticastBVlanStatus,
       "hpnicfSpbConfig": hpnicfSpbConfig,
       "hpnicfSpbIfTable": hpnicfSpbIfTable,
       "hpnicfSpbIfEntry": hpnicfSpbIfEntry,
       "hpnicfSpbIfStatus": hpnicfSpbIfStatus,
       "hpnicfSpbSrvTable": hpnicfSpbSrvTable,
       "hpnicfSpbSrvEntry": hpnicfSpbSrvEntry,
       "hpnicfSpbSrvTableEntryTopIx": hpnicfSpbSrvTableEntryTopIx,
       "hpnicfSpbSrvTableEntryIsid": hpnicfSpbSrvTableEntryIsid,
       "hpnicfSpbSrvTableEntryBaseVid": hpnicfSpbSrvTableEntryBaseVid,
       "hpnicfSpbSrvTableEntryMode": hpnicfSpbSrvTableEntryMode,
       "hpnicfSpbTrap": hpnicfSpbTrap,
       "hpnicfSpbTraps": hpnicfSpbTraps,
       "hpnicfSpbSPSourceConflictTrap": hpnicfSpbSPSourceConflictTrap,
       "hpnicfSpbBMacConflictTrap": hpnicfSpbBMacConflictTrap,
       "hpnicfSpbTrapsObjects": hpnicfSpbTrapsObjects,
       "hpnicfSpbConflictSysID": hpnicfSpbConflictSysID,
       "hpnicfSpbConflictSPSourceID": hpnicfSpbConflictSPSourceID,
       "hpnicfSpbConflictBMac": hpnicfSpbConflictBMac}
)
