# SNMP MIB module (HH3C-SPB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SPB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:56 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cSpb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128)
)
hh3cSpb.setRevisions(
        ("2012-11-22 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSpbObjects_ObjectIdentity = ObjectIdentity
hh3cSpbObjects = _Hh3cSpbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1)
)
_Hh3cSpbSysObjects_ObjectIdentity = ObjectIdentity
hh3cSpbSysObjects = _Hh3cSpbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 1)
)


class _Hh3cSpbSysStatus_Type(Integer32):
    """Custom type hh3cSpbSysStatus based on Integer32"""
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


_Hh3cSpbSysStatus_Type.__name__ = "Integer32"
_Hh3cSpbSysStatus_Object = MibScalar
hh3cSpbSysStatus = _Hh3cSpbSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 1, 1),
    _Hh3cSpbSysStatus_Type()
)
hh3cSpbSysStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSpbSysStatus.setStatus("current")


class _Hh3cSpbMulticastBVlanStatus_Type(Integer32):
    """Custom type hh3cSpbMulticastBVlanStatus based on Integer32"""
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


_Hh3cSpbMulticastBVlanStatus_Type.__name__ = "Integer32"
_Hh3cSpbMulticastBVlanStatus_Object = MibScalar
hh3cSpbMulticastBVlanStatus = _Hh3cSpbMulticastBVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 1, 2),
    _Hh3cSpbMulticastBVlanStatus_Type()
)
hh3cSpbMulticastBVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSpbMulticastBVlanStatus.setStatus("current")
_Hh3cSpbConfig_ObjectIdentity = ObjectIdentity
hh3cSpbConfig = _Hh3cSpbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2)
)
_Hh3cSpbIfTable_Object = MibTable
hh3cSpbIfTable = _Hh3cSpbIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSpbIfTable.setStatus("current")
_Hh3cSpbIfEntry_Object = MibTableRow
hh3cSpbIfEntry = _Hh3cSpbIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 1, 1)
)
hh3cSpbIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cSpbIfEntry.setStatus("current")


class _Hh3cSpbIfStatus_Type(Integer32):
    """Custom type hh3cSpbIfStatus based on Integer32"""
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


_Hh3cSpbIfStatus_Type.__name__ = "Integer32"
_Hh3cSpbIfStatus_Object = MibTableColumn
hh3cSpbIfStatus = _Hh3cSpbIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 1, 1, 1),
    _Hh3cSpbIfStatus_Type()
)
hh3cSpbIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSpbIfStatus.setStatus("current")
_Hh3cSpbSrvTable_Object = MibTable
hh3cSpbSrvTable = _Hh3cSpbSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cSpbSrvTable.setStatus("current")
_Hh3cSpbSrvEntry_Object = MibTableRow
hh3cSpbSrvEntry = _Hh3cSpbSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2, 1)
)
hh3cSpbSrvEntry.setIndexNames(
    (0, "HH3C-SPB-MIB", "hh3cSpbSrvTableEntryTopIx"),
    (0, "HH3C-SPB-MIB", "hh3cSpbSrvTableEntryIsid"),
)
if mibBuilder.loadTexts:
    hh3cSpbSrvEntry.setStatus("current")
_Hh3cSpbSrvTableEntryTopIx_Type = Unsigned32
_Hh3cSpbSrvTableEntryTopIx_Object = MibTableColumn
hh3cSpbSrvTableEntryTopIx = _Hh3cSpbSrvTableEntryTopIx_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2, 1, 1),
    _Hh3cSpbSrvTableEntryTopIx_Type()
)
hh3cSpbSrvTableEntryTopIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSpbSrvTableEntryTopIx.setStatus("current")


class _Hh3cSpbSrvTableEntryIsid_Type(Unsigned32):
    """Custom type hh3cSpbSrvTableEntryIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(255, 16777215),
    )


_Hh3cSpbSrvTableEntryIsid_Type.__name__ = "Unsigned32"
_Hh3cSpbSrvTableEntryIsid_Object = MibTableColumn
hh3cSpbSrvTableEntryIsid = _Hh3cSpbSrvTableEntryIsid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2, 1, 2),
    _Hh3cSpbSrvTableEntryIsid_Type()
)
hh3cSpbSrvTableEntryIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSpbSrvTableEntryIsid.setStatus("current")
_Hh3cSpbSrvTableEntryBaseVid_Type = VlanIdOrNone
_Hh3cSpbSrvTableEntryBaseVid_Object = MibTableColumn
hh3cSpbSrvTableEntryBaseVid = _Hh3cSpbSrvTableEntryBaseVid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2, 1, 3),
    _Hh3cSpbSrvTableEntryBaseVid_Type()
)
hh3cSpbSrvTableEntryBaseVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSpbSrvTableEntryBaseVid.setStatus("current")


class _Hh3cSpbSrvTableEntryMode_Type(Integer32):
    """Custom type hh3cSpbSrvTableEntryMode based on Integer32"""
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


_Hh3cSpbSrvTableEntryMode_Type.__name__ = "Integer32"
_Hh3cSpbSrvTableEntryMode_Object = MibTableColumn
hh3cSpbSrvTableEntryMode = _Hh3cSpbSrvTableEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 2, 2, 1, 4),
    _Hh3cSpbSrvTableEntryMode_Type()
)
hh3cSpbSrvTableEntryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSpbSrvTableEntryMode.setStatus("current")
_Hh3cSpbTrap_ObjectIdentity = ObjectIdentity
hh3cSpbTrap = _Hh3cSpbTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3)
)
_Hh3cSpbTraps_ObjectIdentity = ObjectIdentity
hh3cSpbTraps = _Hh3cSpbTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 0)
)
_Hh3cSpbTrapsObjects_ObjectIdentity = ObjectIdentity
hh3cSpbTrapsObjects = _Hh3cSpbTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 1)
)
_Hh3cSpbConflictSysID_Type = MacAddress
_Hh3cSpbConflictSysID_Object = MibScalar
hh3cSpbConflictSysID = _Hh3cSpbConflictSysID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 1, 1),
    _Hh3cSpbConflictSysID_Type()
)
hh3cSpbConflictSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSpbConflictSysID.setStatus("current")
_Hh3cSpbConflictSPSourceID_Type = IEEE8021SpbmSPsourceId
_Hh3cSpbConflictSPSourceID_Object = MibScalar
hh3cSpbConflictSPSourceID = _Hh3cSpbConflictSPSourceID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 1, 2),
    _Hh3cSpbConflictSPSourceID_Type()
)
hh3cSpbConflictSPSourceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSpbConflictSPSourceID.setStatus("current")
_Hh3cSpbConflictBMac_Type = MacAddress
_Hh3cSpbConflictBMac_Object = MibScalar
hh3cSpbConflictBMac = _Hh3cSpbConflictBMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 1, 3),
    _Hh3cSpbConflictBMac_Type()
)
hh3cSpbConflictBMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cSpbConflictBMac.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cSpbSPSourceConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 0, 1)
)
hh3cSpbSPSourceConflictTrap.setObjects(
      *(("HH3C-SPB-MIB", "hh3cSpbConflictSysID"),
        ("HH3C-SPB-MIB", "hh3cSpbConflictSPSourceID"))
)
if mibBuilder.loadTexts:
    hh3cSpbSPSourceConflictTrap.setStatus(
        "current"
    )

hh3cSpbBMacConflictTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 128, 1, 3, 0, 2)
)
hh3cSpbBMacConflictTrap.setObjects(
      *(("HH3C-SPB-MIB", "hh3cSpbConflictSysID"),
        ("HH3C-SPB-MIB", "hh3cSpbConflictBMac"))
)
if mibBuilder.loadTexts:
    hh3cSpbBMacConflictTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SPB-MIB",
    **{"hh3cSpb": hh3cSpb,
       "hh3cSpbObjects": hh3cSpbObjects,
       "hh3cSpbSysObjects": hh3cSpbSysObjects,
       "hh3cSpbSysStatus": hh3cSpbSysStatus,
       "hh3cSpbMulticastBVlanStatus": hh3cSpbMulticastBVlanStatus,
       "hh3cSpbConfig": hh3cSpbConfig,
       "hh3cSpbIfTable": hh3cSpbIfTable,
       "hh3cSpbIfEntry": hh3cSpbIfEntry,
       "hh3cSpbIfStatus": hh3cSpbIfStatus,
       "hh3cSpbSrvTable": hh3cSpbSrvTable,
       "hh3cSpbSrvEntry": hh3cSpbSrvEntry,
       "hh3cSpbSrvTableEntryTopIx": hh3cSpbSrvTableEntryTopIx,
       "hh3cSpbSrvTableEntryIsid": hh3cSpbSrvTableEntryIsid,
       "hh3cSpbSrvTableEntryBaseVid": hh3cSpbSrvTableEntryBaseVid,
       "hh3cSpbSrvTableEntryMode": hh3cSpbSrvTableEntryMode,
       "hh3cSpbTrap": hh3cSpbTrap,
       "hh3cSpbTraps": hh3cSpbTraps,
       "hh3cSpbSPSourceConflictTrap": hh3cSpbSPSourceConflictTrap,
       "hh3cSpbBMacConflictTrap": hh3cSpbBMacConflictTrap,
       "hh3cSpbTrapsObjects": hh3cSpbTrapsObjects,
       "hh3cSpbConflictSysID": hh3cSpbConflictSysID,
       "hh3cSpbConflictSPSourceID": hh3cSpbConflictSPSourceID,
       "hh3cSpbConflictBMac": hh3cSpbConflictBMac}
)
