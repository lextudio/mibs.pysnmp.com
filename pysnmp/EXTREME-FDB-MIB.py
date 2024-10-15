# SNMP MIB module (EXTREME-FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:20 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

extremeFdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeFdbMacFdbTable_Object = MibTable
extremeFdbMacFdbTable = _ExtremeFdbMacFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1)
)
if mibBuilder.loadTexts:
    extremeFdbMacFdbTable.setStatus("current")
_ExtremeFdbMacFdbEntry_Object = MibTableRow
extremeFdbMacFdbEntry = _ExtremeFdbMacFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1)
)
extremeFdbMacFdbEntry.setIndexNames(
    (0, "EXTREME-FDB-MIB", "extremeFdbMacFdbVlanIfIndex"),
    (0, "EXTREME-FDB-MIB", "extremeFdbMacFdbSequenceNumber"),
)
if mibBuilder.loadTexts:
    extremeFdbMacFdbEntry.setStatus("current")
_ExtremeFdbMacFdbVlanIfIndex_Type = Integer32
_ExtremeFdbMacFdbVlanIfIndex_Object = MibTableColumn
extremeFdbMacFdbVlanIfIndex = _ExtremeFdbMacFdbVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 1),
    _ExtremeFdbMacFdbVlanIfIndex_Type()
)
extremeFdbMacFdbVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeFdbMacFdbVlanIfIndex.setStatus("current")
_ExtremeFdbMacFdbSequenceNumber_Type = Integer32
_ExtremeFdbMacFdbSequenceNumber_Object = MibTableColumn
extremeFdbMacFdbSequenceNumber = _ExtremeFdbMacFdbSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 2),
    _ExtremeFdbMacFdbSequenceNumber_Type()
)
extremeFdbMacFdbSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeFdbMacFdbSequenceNumber.setStatus("current")
_ExtremeFdbMacFdbMacAddress_Type = MacAddress
_ExtremeFdbMacFdbMacAddress_Object = MibTableColumn
extremeFdbMacFdbMacAddress = _ExtremeFdbMacFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 3),
    _ExtremeFdbMacFdbMacAddress_Type()
)
extremeFdbMacFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbMacFdbMacAddress.setStatus("current")
_ExtremeFdbMacFdbPortIfIndex_Type = Integer32
_ExtremeFdbMacFdbPortIfIndex_Object = MibTableColumn
extremeFdbMacFdbPortIfIndex = _ExtremeFdbMacFdbPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 4),
    _ExtremeFdbMacFdbPortIfIndex_Type()
)
extremeFdbMacFdbPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbMacFdbPortIfIndex.setStatus("current")


class _ExtremeFdbMacFdbStatus_Type(Integer32):
    """Custom type extremeFdbMacFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_ExtremeFdbMacFdbStatus_Type.__name__ = "Integer32"
_ExtremeFdbMacFdbStatus_Object = MibTableColumn
extremeFdbMacFdbStatus = _ExtremeFdbMacFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 1, 1, 5),
    _ExtremeFdbMacFdbStatus_Type()
)
extremeFdbMacFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbMacFdbStatus.setStatus("current")
_ExtremeFdbIpFdbTable_Object = MibTable
extremeFdbIpFdbTable = _ExtremeFdbIpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2)
)
if mibBuilder.loadTexts:
    extremeFdbIpFdbTable.setStatus("current")
_ExtremeFdbIpFdbEntry_Object = MibTableRow
extremeFdbIpFdbEntry = _ExtremeFdbIpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1)
)
extremeFdbIpFdbEntry.setIndexNames(
    (0, "EXTREME-FDB-MIB", "extremeFdbIpFdbSequenceNumber"),
)
if mibBuilder.loadTexts:
    extremeFdbIpFdbEntry.setStatus("current")
_ExtremeFdbIpFdbSequenceNumber_Type = Integer32
_ExtremeFdbIpFdbSequenceNumber_Object = MibTableColumn
extremeFdbIpFdbSequenceNumber = _ExtremeFdbIpFdbSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 1),
    _ExtremeFdbIpFdbSequenceNumber_Type()
)
extremeFdbIpFdbSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeFdbIpFdbSequenceNumber.setStatus("current")
_ExtremeFdbIpFdbIPAddress_Type = IpAddress
_ExtremeFdbIpFdbIPAddress_Object = MibTableColumn
extremeFdbIpFdbIPAddress = _ExtremeFdbIpFdbIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 2),
    _ExtremeFdbIpFdbIPAddress_Type()
)
extremeFdbIpFdbIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbIpFdbIPAddress.setStatus("current")
_ExtremeFdbIpFdbMacAddress_Type = MacAddress
_ExtremeFdbIpFdbMacAddress_Object = MibTableColumn
extremeFdbIpFdbMacAddress = _ExtremeFdbIpFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 3),
    _ExtremeFdbIpFdbMacAddress_Type()
)
extremeFdbIpFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbIpFdbMacAddress.setStatus("current")
_ExtremeFdbIpFdbVlanIfIndex_Type = Integer32
_ExtremeFdbIpFdbVlanIfIndex_Object = MibTableColumn
extremeFdbIpFdbVlanIfIndex = _ExtremeFdbIpFdbVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 4),
    _ExtremeFdbIpFdbVlanIfIndex_Type()
)
extremeFdbIpFdbVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbIpFdbVlanIfIndex.setStatus("current")
_ExtremeFdbIpFdbPortIfIndex_Type = Integer32
_ExtremeFdbIpFdbPortIfIndex_Object = MibTableColumn
extremeFdbIpFdbPortIfIndex = _ExtremeFdbIpFdbPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 2, 1, 5),
    _ExtremeFdbIpFdbPortIfIndex_Type()
)
extremeFdbIpFdbPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbIpFdbPortIfIndex.setStatus("current")
_ExtremeFdbPermFdbTable_Object = MibTable
extremeFdbPermFdbTable = _ExtremeFdbPermFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3)
)
if mibBuilder.loadTexts:
    extremeFdbPermFdbTable.setStatus("current")
_ExtremeFdbPermFdbEntry_Object = MibTableRow
extremeFdbPermFdbEntry = _ExtremeFdbPermFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1)
)
extremeFdbPermFdbEntry.setIndexNames(
    (0, "EXTREME-FDB-MIB", "extremeFdbPermFdbFilterNum"),
    (0, "EXTREME-FDB-MIB", "extremeFdbPermFdbMacAddress"),
    (0, "EXTREME-FDB-MIB", "extremeFdbPermFdbVlanId"),
)
if mibBuilder.loadTexts:
    extremeFdbPermFdbEntry.setStatus("current")
_ExtremeFdbPermFdbFilterNum_Type = Integer32
_ExtremeFdbPermFdbFilterNum_Object = MibTableColumn
extremeFdbPermFdbFilterNum = _ExtremeFdbPermFdbFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 1),
    _ExtremeFdbPermFdbFilterNum_Type()
)
extremeFdbPermFdbFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbPermFdbFilterNum.setStatus("current")
_ExtremeFdbPermFdbMacAddress_Type = MacAddress
_ExtremeFdbPermFdbMacAddress_Object = MibTableColumn
extremeFdbPermFdbMacAddress = _ExtremeFdbPermFdbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 2),
    _ExtremeFdbPermFdbMacAddress_Type()
)
extremeFdbPermFdbMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbPermFdbMacAddress.setStatus("current")
_ExtremeFdbPermFdbVlanId_Type = Integer32
_ExtremeFdbPermFdbVlanId_Object = MibTableColumn
extremeFdbPermFdbVlanId = _ExtremeFdbPermFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 3),
    _ExtremeFdbPermFdbVlanId_Type()
)
extremeFdbPermFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbPermFdbVlanId.setStatus("current")
_ExtremeFdbPermFdbPortList_Type = PortList
_ExtremeFdbPermFdbPortList_Object = MibTableColumn
extremeFdbPermFdbPortList = _ExtremeFdbPermFdbPortList_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 4),
    _ExtremeFdbPermFdbPortList_Type()
)
extremeFdbPermFdbPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFdbPermFdbPortList.setStatus("current")


class _ExtremeFdbPermFdbFlags_Type(Bits):
    """Custom type extremeFdbPermFdbFlags based on Bits"""
    namedValues = NamedValues(
        ("isSecure", 0)
    )

_ExtremeFdbPermFdbFlags_Type.__name__ = "Bits"
_ExtremeFdbPermFdbFlags_Object = MibTableColumn
extremeFdbPermFdbFlags = _ExtremeFdbPermFdbFlags_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 5),
    _ExtremeFdbPermFdbFlags_Type()
)
extremeFdbPermFdbFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFdbPermFdbFlags.setStatus("current")
_ExtremeFdbPermFdbStatus_Type = RowStatus
_ExtremeFdbPermFdbStatus_Object = MibTableColumn
extremeFdbPermFdbStatus = _ExtremeFdbPermFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 3, 1, 6),
    _ExtremeFdbPermFdbStatus_Type()
)
extremeFdbPermFdbStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeFdbPermFdbStatus.setStatus("current")
_ExtremeFdbMacFdbCounterTable_Object = MibTable
extremeFdbMacFdbCounterTable = _ExtremeFdbMacFdbCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 5)
)
if mibBuilder.loadTexts:
    extremeFdbMacFdbCounterTable.setStatus("current")
_ExtremeFdbMacFdbCounterEntry_Object = MibTableRow
extremeFdbMacFdbCounterEntry = _ExtremeFdbMacFdbCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1)
)
extremeFdbMacFdbCounterEntry.setIndexNames(
    (0, "EXTREME-FDB-MIB", "extremeFdbMacFdbCounterPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeFdbMacFdbCounterEntry.setStatus("current")
_ExtremeFdbMacFdbCounterPortIfIndex_Type = Integer32
_ExtremeFdbMacFdbCounterPortIfIndex_Object = MibTableColumn
extremeFdbMacFdbCounterPortIfIndex = _ExtremeFdbMacFdbCounterPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1, 1),
    _ExtremeFdbMacFdbCounterPortIfIndex_Type()
)
extremeFdbMacFdbCounterPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeFdbMacFdbCounterPortIfIndex.setStatus("current")
_ExtremeFdbMacFdbCounterValue_Type = Counter64
_ExtremeFdbMacFdbCounterValue_Object = MibTableColumn
extremeFdbMacFdbCounterValue = _ExtremeFdbMacFdbCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 16, 5, 1, 2),
    _ExtremeFdbMacFdbCounterValue_Type()
)
extremeFdbMacFdbCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeFdbMacFdbCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-FDB-MIB",
    **{"extremeFdb": extremeFdb,
       "extremeFdbMacFdbTable": extremeFdbMacFdbTable,
       "extremeFdbMacFdbEntry": extremeFdbMacFdbEntry,
       "extremeFdbMacFdbVlanIfIndex": extremeFdbMacFdbVlanIfIndex,
       "extremeFdbMacFdbSequenceNumber": extremeFdbMacFdbSequenceNumber,
       "extremeFdbMacFdbMacAddress": extremeFdbMacFdbMacAddress,
       "extremeFdbMacFdbPortIfIndex": extremeFdbMacFdbPortIfIndex,
       "extremeFdbMacFdbStatus": extremeFdbMacFdbStatus,
       "extremeFdbIpFdbTable": extremeFdbIpFdbTable,
       "extremeFdbIpFdbEntry": extremeFdbIpFdbEntry,
       "extremeFdbIpFdbSequenceNumber": extremeFdbIpFdbSequenceNumber,
       "extremeFdbIpFdbIPAddress": extremeFdbIpFdbIPAddress,
       "extremeFdbIpFdbMacAddress": extremeFdbIpFdbMacAddress,
       "extremeFdbIpFdbVlanIfIndex": extremeFdbIpFdbVlanIfIndex,
       "extremeFdbIpFdbPortIfIndex": extremeFdbIpFdbPortIfIndex,
       "extremeFdbPermFdbTable": extremeFdbPermFdbTable,
       "extremeFdbPermFdbEntry": extremeFdbPermFdbEntry,
       "extremeFdbPermFdbFilterNum": extremeFdbPermFdbFilterNum,
       "extremeFdbPermFdbMacAddress": extremeFdbPermFdbMacAddress,
       "extremeFdbPermFdbVlanId": extremeFdbPermFdbVlanId,
       "extremeFdbPermFdbPortList": extremeFdbPermFdbPortList,
       "extremeFdbPermFdbFlags": extremeFdbPermFdbFlags,
       "extremeFdbPermFdbStatus": extremeFdbPermFdbStatus,
       "extremeFdbMacFdbCounterTable": extremeFdbMacFdbCounterTable,
       "extremeFdbMacFdbCounterEntry": extremeFdbMacFdbCounterEntry,
       "extremeFdbMacFdbCounterPortIfIndex": extremeFdbMacFdbCounterPortIfIndex,
       "extremeFdbMacFdbCounterValue": extremeFdbMacFdbCounterValue}
)
