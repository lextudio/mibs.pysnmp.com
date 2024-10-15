# SNMP MIB module (CISCOSB-BONJOUR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-BONJOUR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:56 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

rlBonjour = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114)
)
rlBonjour.setRevisions(
        ("2009-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlBonjourServiceState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rlBonjourInactive", 1),
          ("rlBonjourNotPublished", 0),
          ("rlBonjourRegistering", 2),
          ("rlBonjourRunning", 3))
    )



class RlBonjourOperationState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )



class RlBonjourOperationReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bonjourDisabled", 4),
          ("exclude", 3),
          ("include", 1),
          ("l2InterfaceDown", 7),
          ("noIPaddress", 6),
          ("notExclude", 0),
          ("notInclude", 2),
          ("notPresent", 8),
          ("serviceDisabled", 5),
          ("unknown", 9))
    )



# MIB Managed Objects in the order of their OIDs



class _RlBonjourPublish_Type(Integer32):
    """Custom type rlBonjourPublish based on Integer32"""
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


_RlBonjourPublish_Type.__name__ = "Integer32"
_RlBonjourPublish_Object = MibScalar
rlBonjourPublish = _RlBonjourPublish_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 1),
    _RlBonjourPublish_Type()
)
rlBonjourPublish.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBonjourPublish.setStatus("current")
_RlBonjourStatusTable_Object = MibTable
rlBonjourStatusTable = _RlBonjourStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2)
)
if mibBuilder.loadTexts:
    rlBonjourStatusTable.setStatus("current")
_RlBonjourStatusEntry_Object = MibTableRow
rlBonjourStatusEntry = _RlBonjourStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2, 1)
)
rlBonjourStatusEntry.setIndexNames(
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourStatusServiceName"),
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourStatusIPInterfaceType"),
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourStatusIPInterfaceAddr"),
)
if mibBuilder.loadTexts:
    rlBonjourStatusEntry.setStatus("current")
_RlBonjourStatusServiceName_Type = DisplayString
_RlBonjourStatusServiceName_Object = MibTableColumn
rlBonjourStatusServiceName = _RlBonjourStatusServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2, 1, 1),
    _RlBonjourStatusServiceName_Type()
)
rlBonjourStatusServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourStatusServiceName.setStatus("current")
_RlBonjourStatusIPInterfaceType_Type = InetAddressType
_RlBonjourStatusIPInterfaceType_Object = MibTableColumn
rlBonjourStatusIPInterfaceType = _RlBonjourStatusIPInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2, 1, 2),
    _RlBonjourStatusIPInterfaceType_Type()
)
rlBonjourStatusIPInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourStatusIPInterfaceType.setStatus("current")
_RlBonjourStatusIPInterfaceAddr_Type = InetAddress
_RlBonjourStatusIPInterfaceAddr_Object = MibTableColumn
rlBonjourStatusIPInterfaceAddr = _RlBonjourStatusIPInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2, 1, 3),
    _RlBonjourStatusIPInterfaceAddr_Type()
)
rlBonjourStatusIPInterfaceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourStatusIPInterfaceAddr.setStatus("current")
_RlBonjourStatusState_Type = RlBonjourServiceState
_RlBonjourStatusState_Object = MibTableColumn
rlBonjourStatusState = _RlBonjourStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 2, 1, 4),
    _RlBonjourStatusState_Type()
)
rlBonjourStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBonjourStatusState.setStatus("current")
_RlBonjourStateTable_Object = MibTable
rlBonjourStateTable = _RlBonjourStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3)
)
if mibBuilder.loadTexts:
    rlBonjourStateTable.setStatus("current")
_RlBonjourStateEntry_Object = MibTableRow
rlBonjourStateEntry = _RlBonjourStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3, 1)
)
rlBonjourStateEntry.setIndexNames(
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourStateServiceName"),
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourStateL2Interface"),
)
if mibBuilder.loadTexts:
    rlBonjourStateEntry.setStatus("current")
_RlBonjourStateServiceName_Type = DisplayString
_RlBonjourStateServiceName_Object = MibTableColumn
rlBonjourStateServiceName = _RlBonjourStateServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3, 1, 1),
    _RlBonjourStateServiceName_Type()
)
rlBonjourStateServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourStateServiceName.setStatus("current")
_RlBonjourStateL2Interface_Type = InterfaceIndex
_RlBonjourStateL2Interface_Object = MibTableColumn
rlBonjourStateL2Interface = _RlBonjourStateL2Interface_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3, 1, 2),
    _RlBonjourStateL2Interface_Type()
)
rlBonjourStateL2Interface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourStateL2Interface.setStatus("current")
_RlBonjourStateOperationMode_Type = RlBonjourOperationState
_RlBonjourStateOperationMode_Object = MibTableColumn
rlBonjourStateOperationMode = _RlBonjourStateOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3, 1, 3),
    _RlBonjourStateOperationMode_Type()
)
rlBonjourStateOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBonjourStateOperationMode.setStatus("current")
_RlBonjourStateOperationReason_Type = RlBonjourOperationReason
_RlBonjourStateOperationReason_Object = MibTableColumn
rlBonjourStateOperationReason = _RlBonjourStateOperationReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 3, 1, 4),
    _RlBonjourStateOperationReason_Type()
)
rlBonjourStateOperationReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBonjourStateOperationReason.setStatus("current")
_RlBonjourL2Table_Object = MibTable
rlBonjourL2Table = _RlBonjourL2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 4)
)
if mibBuilder.loadTexts:
    rlBonjourL2Table.setStatus("current")
_RlBonjourL2Entry_Object = MibTableRow
rlBonjourL2Entry = _RlBonjourL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 4, 1)
)
rlBonjourL2Entry.setIndexNames(
    (0, "CISCOSB-BONJOUR-MIB", "rlBonjourL2Ifindex"),
)
if mibBuilder.loadTexts:
    rlBonjourL2Entry.setStatus("current")
_RlBonjourL2Ifindex_Type = InterfaceIndex
_RlBonjourL2Ifindex_Object = MibTableColumn
rlBonjourL2Ifindex = _RlBonjourL2Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 4, 1, 1),
    _RlBonjourL2Ifindex_Type()
)
rlBonjourL2Ifindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBonjourL2Ifindex.setStatus("current")
_RlBonjourL2RowStatus_Type = RowStatus
_RlBonjourL2RowStatus_Object = MibTableColumn
rlBonjourL2RowStatus = _RlBonjourL2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 4, 1, 2),
    _RlBonjourL2RowStatus_Type()
)
rlBonjourL2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBonjourL2RowStatus.setStatus("current")


class _RlBonjourL2Mode_Type(Integer32):
    """Custom type rlBonjourL2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_RlBonjourL2Mode_Type.__name__ = "Integer32"
_RlBonjourL2Mode_Object = MibScalar
rlBonjourL2Mode = _RlBonjourL2Mode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 5),
    _RlBonjourL2Mode_Type()
)
rlBonjourL2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBonjourL2Mode.setStatus("current")
_RlBonjourInstanceName_Type = Integer32
_RlBonjourInstanceName_Object = MibScalar
rlBonjourInstanceName = _RlBonjourInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 6),
    _RlBonjourInstanceName_Type()
)
rlBonjourInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBonjourInstanceName.setStatus("current")
_RlBonjourHostName_Type = Integer32
_RlBonjourHostName_Object = MibScalar
rlBonjourHostName = _RlBonjourHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 114, 7),
    _RlBonjourHostName_Type()
)
rlBonjourHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBonjourHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-BONJOUR-MIB",
    **{"RlBonjourServiceState": RlBonjourServiceState,
       "RlBonjourOperationState": RlBonjourOperationState,
       "RlBonjourOperationReason": RlBonjourOperationReason,
       "rlBonjour": rlBonjour,
       "rlBonjourPublish": rlBonjourPublish,
       "rlBonjourStatusTable": rlBonjourStatusTable,
       "rlBonjourStatusEntry": rlBonjourStatusEntry,
       "rlBonjourStatusServiceName": rlBonjourStatusServiceName,
       "rlBonjourStatusIPInterfaceType": rlBonjourStatusIPInterfaceType,
       "rlBonjourStatusIPInterfaceAddr": rlBonjourStatusIPInterfaceAddr,
       "rlBonjourStatusState": rlBonjourStatusState,
       "rlBonjourStateTable": rlBonjourStateTable,
       "rlBonjourStateEntry": rlBonjourStateEntry,
       "rlBonjourStateServiceName": rlBonjourStateServiceName,
       "rlBonjourStateL2Interface": rlBonjourStateL2Interface,
       "rlBonjourStateOperationMode": rlBonjourStateOperationMode,
       "rlBonjourStateOperationReason": rlBonjourStateOperationReason,
       "rlBonjourL2Table": rlBonjourL2Table,
       "rlBonjourL2Entry": rlBonjourL2Entry,
       "rlBonjourL2Ifindex": rlBonjourL2Ifindex,
       "rlBonjourL2RowStatus": rlBonjourL2RowStatus,
       "rlBonjourL2Mode": rlBonjourL2Mode,
       "rlBonjourInstanceName": rlBonjourInstanceName,
       "rlBonjourHostName": rlBonjourHostName}
)
