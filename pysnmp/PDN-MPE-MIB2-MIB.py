# SNMP MIB module (PDN-MPE-MIB2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-MIB2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:56 2024
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

(mpe_mib2,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "mpe-mib2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpeMib2MIBObjects_ObjectIdentity = ObjectIdentity
mpeMib2MIBObjects = _MpeMib2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1)
)
_MpeSystem_ObjectIdentity = ObjectIdentity
mpeSystem = _MpeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1)
)
_MpeSystemsTable_Object = MibTable
mpeSystemsTable = _MpeSystemsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpeSystemsTable.setStatus("mandatory")
_MpeSystemsEntry_Object = MibTableRow
mpeSystemsEntry = _MpeSystemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1)
)
mpeSystemsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeSystemsEntry.setStatus("mandatory")


class _MpeSysDescr_Type(DisplayString):
    """Custom type mpeSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeSysDescr_Type.__name__ = "DisplayString"
_MpeSysDescr_Object = MibTableColumn
mpeSysDescr = _MpeSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 1),
    _MpeSysDescr_Type()
)
mpeSysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysDescr.setStatus("mandatory")
_MpeSysObjectID_Type = ObjectIdentifier
_MpeSysObjectID_Object = MibTableColumn
mpeSysObjectID = _MpeSysObjectID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 2),
    _MpeSysObjectID_Type()
)
mpeSysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysObjectID.setStatus("mandatory")
_MpeSysUpTime_Type = TimeTicks
_MpeSysUpTime_Object = MibTableColumn
mpeSysUpTime = _MpeSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 3),
    _MpeSysUpTime_Type()
)
mpeSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysUpTime.setStatus("mandatory")


class _MpeSysContact_Type(DisplayString):
    """Custom type mpeSysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeSysContact_Type.__name__ = "DisplayString"
_MpeSysContact_Object = MibTableColumn
mpeSysContact = _MpeSysContact_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 4),
    _MpeSysContact_Type()
)
mpeSysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysContact.setStatus("mandatory")


class _MpeSysName_Type(DisplayString):
    """Custom type mpeSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeSysName_Type.__name__ = "DisplayString"
_MpeSysName_Object = MibTableColumn
mpeSysName = _MpeSysName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 5),
    _MpeSysName_Type()
)
mpeSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysName.setStatus("mandatory")


class _MpeSysLocation_Type(DisplayString):
    """Custom type mpeSysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeSysLocation_Type.__name__ = "DisplayString"
_MpeSysLocation_Object = MibTableColumn
mpeSysLocation = _MpeSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 6),
    _MpeSysLocation_Type()
)
mpeSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeSysLocation.setStatus("mandatory")


class _MpeSysServices_Type(Integer32):
    """Custom type mpeSysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MpeSysServices_Type.__name__ = "Integer32"
_MpeSysServices_Object = MibTableColumn
mpeSysServices = _MpeSysServices_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 1, 1, 1, 1, 7),
    _MpeSysServices_Type()
)
mpeSysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeSysServices.setStatus("mandatory")
_MpeMib2MIBTraps_ObjectIdentity = ObjectIdentity
mpeMib2MIBTraps = _MpeMib2MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-MIB2-MIB",
    **{"mpeMib2MIBObjects": mpeMib2MIBObjects,
       "mpeSystem": mpeSystem,
       "mpeSystemsTable": mpeSystemsTable,
       "mpeSystemsEntry": mpeSystemsEntry,
       "mpeSysDescr": mpeSysDescr,
       "mpeSysObjectID": mpeSysObjectID,
       "mpeSysUpTime": mpeSysUpTime,
       "mpeSysContact": mpeSysContact,
       "mpeSysName": mpeSysName,
       "mpeSysLocation": mpeSysLocation,
       "mpeSysServices": mpeSysServices,
       "mpeMib2MIBTraps": mpeMib2MIBTraps}
)
