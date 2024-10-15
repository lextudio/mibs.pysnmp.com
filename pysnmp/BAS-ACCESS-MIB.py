# SNMP MIB module (BAS-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:14 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAccessControl) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAccessControl")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

basAccessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasAccessTable_Object = MibTable
basAccessTable = _BasAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1)
)
if mibBuilder.loadTexts:
    basAccessTable.setStatus("current")
_BasAccessEntry_Object = MibTableRow
basAccessEntry = _BasAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1)
)
basAccessEntry.setIndexNames(
    (0, "BAS-ACCESS-MIB", "basAccessChassis"),
    (0, "BAS-ACCESS-MIB", "basAccessSlot"),
    (0, "BAS-ACCESS-MIB", "basAccessInterface"),
    (0, "BAS-ACCESS-MIB", "basAccessLPort"),
    (0, "BAS-ACCESS-MIB", "basAccessIndex"),
)
if mibBuilder.loadTexts:
    basAccessEntry.setStatus("current")
_BasAccessChassis_Type = BasChassisId
_BasAccessChassis_Object = MibTableColumn
basAccessChassis = _BasAccessChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 1),
    _BasAccessChassis_Type()
)
basAccessChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAccessChassis.setStatus("current")
_BasAccessSlot_Type = BasSlotId
_BasAccessSlot_Object = MibTableColumn
basAccessSlot = _BasAccessSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 2),
    _BasAccessSlot_Type()
)
basAccessSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAccessSlot.setStatus("current")
_BasAccessInterface_Type = BasInterfaceId
_BasAccessInterface_Object = MibTableColumn
basAccessInterface = _BasAccessInterface_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 3),
    _BasAccessInterface_Type()
)
basAccessInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAccessInterface.setStatus("current")
_BasAccessLPort_Type = BasLogicalPortId
_BasAccessLPort_Object = MibTableColumn
basAccessLPort = _BasAccessLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 4),
    _BasAccessLPort_Type()
)
basAccessLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAccessLPort.setStatus("current")
_BasAccessIndex_Type = Integer32
_BasAccessIndex_Object = MibTableColumn
basAccessIndex = _BasAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 5),
    _BasAccessIndex_Type()
)
basAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basAccessIndex.setStatus("current")


class _BasAccessCommName_Type(OctetString):
    """Custom type basAccessCommName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BasAccessCommName_Type.__name__ = "OctetString"
_BasAccessCommName_Object = MibTableColumn
basAccessCommName = _BasAccessCommName_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 6),
    _BasAccessCommName_Type()
)
basAccessCommName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basAccessCommName.setStatus("current")
_BasAccessIpAddress_Type = IpAddress
_BasAccessIpAddress_Object = MibTableColumn
basAccessIpAddress = _BasAccessIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 7),
    _BasAccessIpAddress_Type()
)
basAccessIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basAccessIpAddress.setStatus("current")


class _BasAccessProfile_Type(Integer32):
    """Custom type basAccessProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BasAccessProfile_Type.__name__ = "Integer32"
_BasAccessProfile_Object = MibTableColumn
basAccessProfile = _BasAccessProfile_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 8),
    _BasAccessProfile_Type()
)
basAccessProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basAccessProfile.setStatus("current")
_BasAccessStatus_Type = RowStatus
_BasAccessStatus_Object = MibTableColumn
basAccessStatus = _BasAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 10, 1, 1, 1, 9),
    _BasAccessStatus_Type()
)
basAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    basAccessStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ACCESS-MIB",
    **{"basAccessMIB": basAccessMIB,
       "basAccessTable": basAccessTable,
       "basAccessEntry": basAccessEntry,
       "basAccessChassis": basAccessChassis,
       "basAccessSlot": basAccessSlot,
       "basAccessInterface": basAccessInterface,
       "basAccessLPort": basAccessLPort,
       "basAccessIndex": basAccessIndex,
       "basAccessCommName": basAccessCommName,
       "basAccessIpAddress": basAccessIpAddress,
       "basAccessProfile": basAccessProfile,
       "basAccessStatus": basAccessStatus}
)
