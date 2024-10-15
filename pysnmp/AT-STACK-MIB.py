# SNMP MIB module (AT-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:33 2024
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

(hostId,) = mibBuilder.importSymbols(
    "AT-SYSINFO-MIB",
    "hostId")

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

stack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120)
)
stack.setRevisions(
        ("2006-05-03 09:26",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _StackId_Type(Integer32):
    """Custom type stackId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_StackId_Type.__name__ = "Integer32"
_StackId_Object = MibScalar
stackId = _StackId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 1),
    _StackId_Type()
)
stackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackId.setStatus("current")


class _StackSnmpHost_Type(Integer32):
    """Custom type stackSnmpHost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_StackSnmpHost_Type.__name__ = "Integer32"
_StackSnmpHost_Object = MibScalar
stackSnmpHost = _StackSnmpHost_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 2),
    _StackSnmpHost_Type()
)
stackSnmpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackSnmpHost.setStatus("current")


class _StackStatus_Type(Integer32):
    """Custom type stackStatus based on Integer32"""
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


_StackStatus_Type.__name__ = "Integer32"
_StackStatus_Object = MibScalar
stackStatus = _StackStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 3),
    _StackStatus_Type()
)
stackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackStatus.setStatus("current")
_StackInterface_Type = DisplayString
_StackInterface_Object = MibScalar
stackInterface = _StackInterface_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 4),
    _StackInterface_Type()
)
stackInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackInterface.setStatus("current")


class _StackAuth_Type(Integer32):
    """Custom type stackAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("plaintext", 1))
    )


_StackAuth_Type.__name__ = "Integer32"
_StackAuth_Object = MibScalar
stackAuth = _StackAuth_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 5),
    _StackAuth_Type()
)
stackAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackAuth.setStatus("current")


class _StackPassword_Type(DisplayStringUnsized):
    """Custom type stackPassword based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_StackPassword_Type.__name__ = "DisplayStringUnsized"
_StackPassword_Object = MibScalar
stackPassword = _StackPassword_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 6),
    _StackPassword_Type()
)
stackPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackPassword.setStatus("current")
_Counters_ObjectIdentity = ObjectIdentity
counters = _Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7)
)
_DebugErrors_Type = Integer32
_DebugErrors_Object = MibScalar
debugErrors = _DebugErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 1),
    _DebugErrors_Type()
)
debugErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    debugErrors.setStatus("current")
_RxPkts_Type = Integer32
_RxPkts_Object = MibScalar
rxPkts = _RxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 2),
    _RxPkts_Type()
)
rxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPkts.setStatus("current")
_RxDiscards_Type = Integer32
_RxDiscards_Object = MibScalar
rxDiscards = _RxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 3),
    _RxDiscards_Type()
)
rxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiscards.setStatus("current")
_TxPkts_Type = Integer32
_TxPkts_Object = MibScalar
txPkts = _TxPkts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 4),
    _TxPkts_Type()
)
txPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPkts.setStatus("current")
_TxFails_Type = Integer32
_TxFails_Object = MibScalar
txFails = _TxFails_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 5),
    _TxFails_Type()
)
txFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFails.setStatus("current")
_SdrCount_Type = Integer32
_SdrCount_Object = MibScalar
sdrCount = _SdrCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 7, 6),
    _SdrCount_Type()
)
sdrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdrCount.setStatus("current")
_StackMemberTable_Object = MibTable
stackMemberTable = _StackMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8)
)
if mibBuilder.loadTexts:
    stackMemberTable.setStatus("current")
_StackMemberEntry_Object = MibTableRow
stackMemberEntry = _StackMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1)
)
stackMemberEntry.setIndexNames(
    (0, "AT-SYSINFO-MIB", "hostId"),
)
if mibBuilder.loadTexts:
    stackMemberEntry.setStatus("current")


class _MemberHostId_Type(Integer32):
    """Custom type memberHostId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MemberHostId_Type.__name__ = "Integer32"
_MemberHostId_Object = MibTableColumn
memberHostId = _MemberHostId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1, 1),
    _MemberHostId_Type()
)
memberHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberHostId.setStatus("current")
_MacAddress_Type = DisplayString
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1, 2),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _DedicatedMaster_Type(Integer32):
    """Custom type dedicatedMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DedicatedMaster_Type.__name__ = "Integer32"
_DedicatedMaster_Object = MibTableColumn
dedicatedMaster = _DedicatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1, 3),
    _DedicatedMaster_Type()
)
dedicatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dedicatedMaster.setStatus("current")


class _BackupDedicatedMaster_Type(Integer32):
    """Custom type backupDedicatedMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_BackupDedicatedMaster_Type.__name__ = "Integer32"
_BackupDedicatedMaster_Object = MibTableColumn
backupDedicatedMaster = _BackupDedicatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1, 4),
    _BackupDedicatedMaster_Type()
)
backupDedicatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupDedicatedMaster.setStatus("current")
_State_Type = DisplayString
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 120, 8, 1, 5),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-STACK-MIB",
    **{"stack": stack,
       "stackId": stackId,
       "stackSnmpHost": stackSnmpHost,
       "stackStatus": stackStatus,
       "stackInterface": stackInterface,
       "stackAuth": stackAuth,
       "stackPassword": stackPassword,
       "counters": counters,
       "debugErrors": debugErrors,
       "rxPkts": rxPkts,
       "rxDiscards": rxDiscards,
       "txPkts": txPkts,
       "txFails": txFails,
       "sdrCount": sdrCount,
       "stackMemberTable": stackMemberTable,
       "stackMemberEntry": stackMemberEntry,
       "memberHostId": memberHostId,
       "macAddress": macAddress,
       "dedicatedMaster": dedicatedMaster,
       "backupDedicatedMaster": backupDedicatedMaster,
       "state": state}
)
