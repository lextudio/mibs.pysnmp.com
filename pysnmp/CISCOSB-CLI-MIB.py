# SNMP MIB module (CISCOSB-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-CLI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:03 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCli = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52)
)
rlCli.setRevisions(
        ("2010-05-25 00:00",
         "2007-01-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlCliMibVersion_Type = Integer32
_RlCliMibVersion_Object = MibScalar
rlCliMibVersion = _RlCliMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 1),
    _RlCliMibVersion_Type()
)
rlCliMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliMibVersion.setStatus("current")


class _RlCliPassword_Type(DisplayString):
    """Custom type rlCliPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlCliPassword_Type.__name__ = "DisplayString"
_RlCliPassword_Object = MibScalar
rlCliPassword = _RlCliPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 2),
    _RlCliPassword_Type()
)
rlCliPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliPassword.setStatus("current")


class _RlCliTimer_Type(Integer32):
    """Custom type rlCliTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RlCliTimer_Type.__name__ = "Integer32"
_RlCliTimer_Object = MibScalar
rlCliTimer = _RlCliTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 3),
    _RlCliTimer_Type()
)
rlCliTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliTimer.setStatus("current")
_RlCliFileEnable_Type = TruthValue
_RlCliFileEnable_Object = MibScalar
rlCliFileEnable = _RlCliFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 4),
    _RlCliFileEnable_Type()
)
rlCliFileEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCliFileEnable.setStatus("current")
_RlCliFileEnableAfterReset_Type = TruthValue
_RlCliFileEnableAfterReset_Object = MibScalar
rlCliFileEnableAfterReset = _RlCliFileEnableAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 5),
    _RlCliFileEnableAfterReset_Type()
)
rlCliFileEnableAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCliFileEnableAfterReset.setStatus("current")
_RlCLIremoteCLIsupport_ObjectIdentity = ObjectIdentity
rlCLIremoteCLIsupport = _RlCLIremoteCLIsupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6)
)


class _RlCLIremoteCLIcommand_Type(Integer32):
    """Custom type rlCLIremoteCLIcommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("applySentCLI", 3),
          ("deleteCommandsCLI", 4),
          ("releaseRemoteCLI", 2),
          ("setEchoModeCLI", 5),
          ("takeRemoteCLI", 1),
          ("unsetEchoModeCLI", 6))
    )


_RlCLIremoteCLIcommand_Type.__name__ = "Integer32"
_RlCLIremoteCLIcommand_Object = MibScalar
rlCLIremoteCLIcommand = _RlCLIremoteCLIcommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 1),
    _RlCLIremoteCLIcommand_Type()
)
rlCLIremoteCLIcommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommand.setStatus("current")


class _RlCLIremoteCLIexecutionState_Type(Integer32):
    """Custom type rlCLIremoteCLIexecutionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("done", 6),
          ("free", 1),
          ("inProcess", 3),
          ("notActive", 2),
          ("outputAvailable", 4),
          ("waitingForOutputRetrieval", 5))
    )


_RlCLIremoteCLIexecutionState_Type.__name__ = "Integer32"
_RlCLIremoteCLIexecutionState_Object = MibScalar
rlCLIremoteCLIexecutionState = _RlCLIremoteCLIexecutionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 2),
    _RlCLIremoteCLIexecutionState_Type()
)
rlCLIremoteCLIexecutionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIexecutionState.setStatus("current")
_RlCLIremoteCLIexecutionCommandIndex_Type = Unsigned32
_RlCLIremoteCLIexecutionCommandIndex_Object = MibScalar
rlCLIremoteCLIexecutionCommandIndex = _RlCLIremoteCLIexecutionCommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 3),
    _RlCLIremoteCLIexecutionCommandIndex_Type()
)
rlCLIremoteCLIexecutionCommandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIexecutionCommandIndex.setStatus("current")


class _RlCLIremoteCLImode_Type(Integer32):
    """Custom type rlCLIremoteCLImode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleteCLIOutputOnGet", 1),
          ("keepCLIOutputOnGet", 2))
    )


_RlCLIremoteCLImode_Type.__name__ = "Integer32"
_RlCLIremoteCLImode_Object = MibScalar
rlCLIremoteCLImode = _RlCLIremoteCLImode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 4),
    _RlCLIremoteCLImode_Type()
)
rlCLIremoteCLImode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCLIremoteCLImode.setStatus("current")
_RlCLIremoteCLIcommandsTable_Object = MibTable
rlCLIremoteCLIcommandsTable = _RlCLIremoteCLIcommandsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5)
)
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandsTable.setStatus("current")
_RlCLIremoteCLIcommandsEntry_Object = MibTableRow
rlCLIremoteCLIcommandsEntry = _RlCLIremoteCLIcommandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1)
)
rlCLIremoteCLIcommandsEntry.setIndexNames(
    (0, "CISCOSB-CLI-MIB", "rlCLIremoteCLIcommandIndex"),
    (0, "CISCOSB-CLI-MIB", "rlCLIremoteCLIcommandPartNumber"),
)
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandsEntry.setStatus("current")


class _RlCLIremoteCLIcommandIndex_Type(Unsigned32):
    """Custom type rlCLIremoteCLIcommandIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlCLIremoteCLIcommandIndex_Type.__name__ = "Unsigned32"
_RlCLIremoteCLIcommandIndex_Object = MibTableColumn
rlCLIremoteCLIcommandIndex = _RlCLIremoteCLIcommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1, 1),
    _RlCLIremoteCLIcommandIndex_Type()
)
rlCLIremoteCLIcommandIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandIndex.setStatus("current")


class _RlCLIremoteCLIcommandPartNumber_Type(Unsigned32):
    """Custom type rlCLIremoteCLIcommandPartNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlCLIremoteCLIcommandPartNumber_Type.__name__ = "Unsigned32"
_RlCLIremoteCLIcommandPartNumber_Object = MibTableColumn
rlCLIremoteCLIcommandPartNumber = _RlCLIremoteCLIcommandPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1, 2),
    _RlCLIremoteCLIcommandPartNumber_Type()
)
rlCLIremoteCLIcommandPartNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandPartNumber.setStatus("current")
_RlCLIremoteCLIcommandPart_Type = OctetString
_RlCLIremoteCLIcommandPart_Object = MibTableColumn
rlCLIremoteCLIcommandPart = _RlCLIremoteCLIcommandPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1, 3),
    _RlCLIremoteCLIcommandPart_Type()
)
rlCLIremoteCLIcommandPart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandPart.setStatus("current")
_RlCLIremoteCLIcommandStatus_Type = RowStatus
_RlCLIremoteCLIcommandStatus_Object = MibTableColumn
rlCLIremoteCLIcommandStatus = _RlCLIremoteCLIcommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1, 4),
    _RlCLIremoteCLIcommandStatus_Type()
)
rlCLIremoteCLIcommandStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlCLIremoteCLIcommandStatus.setStatus("current")
_RlCLIremoteCLIactivationStatus_Type = Integer32
_RlCLIremoteCLIactivationStatus_Object = MibTableColumn
rlCLIremoteCLIactivationStatus = _RlCLIremoteCLIactivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 5, 1, 5),
    _RlCLIremoteCLIactivationStatus_Type()
)
rlCLIremoteCLIactivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIactivationStatus.setStatus("current")
_RlCLIremoteCLIoutputsTable_Object = MibTable
rlCLIremoteCLIoutputsTable = _RlCLIremoteCLIoutputsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6)
)
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputsTable.setStatus("current")
_RlCLIremoteCLIoutputsEntry_Object = MibTableRow
rlCLIremoteCLIoutputsEntry = _RlCLIremoteCLIoutputsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1)
)
rlCLIremoteCLIoutputsEntry.setIndexNames(
    (0, "CISCOSB-CLI-MIB", "rlCLIremoteCLIoutputRowIndex"),
    (0, "CISCOSB-CLI-MIB", "rlCLIremoteCLIoutputRowPartNumber"),
)
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputsEntry.setStatus("current")


class _RlCLIremoteCLIoutputRowIndex_Type(Unsigned32):
    """Custom type rlCLIremoteCLIoutputRowIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlCLIremoteCLIoutputRowIndex_Type.__name__ = "Unsigned32"
_RlCLIremoteCLIoutputRowIndex_Object = MibTableColumn
rlCLIremoteCLIoutputRowIndex = _RlCLIremoteCLIoutputRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1, 1),
    _RlCLIremoteCLIoutputRowIndex_Type()
)
rlCLIremoteCLIoutputRowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputRowIndex.setStatus("current")


class _RlCLIremoteCLIoutputRowPartNumber_Type(Unsigned32):
    """Custom type rlCLIremoteCLIoutputRowPartNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RlCLIremoteCLIoutputRowPartNumber_Type.__name__ = "Unsigned32"
_RlCLIremoteCLIoutputRowPartNumber_Object = MibTableColumn
rlCLIremoteCLIoutputRowPartNumber = _RlCLIremoteCLIoutputRowPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1, 2),
    _RlCLIremoteCLIoutputRowPartNumber_Type()
)
rlCLIremoteCLIoutputRowPartNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputRowPartNumber.setStatus("current")
_RlCLIremoteCLIoutputRowPart_Type = OctetString
_RlCLIremoteCLIoutputRowPart_Object = MibTableColumn
rlCLIremoteCLIoutputRowPart = _RlCLIremoteCLIoutputRowPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1, 3),
    _RlCLIremoteCLIoutputRowPart_Type()
)
rlCLIremoteCLIoutputRowPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputRowPart.setStatus("current")
_RlCLIremoteCLIoutputRowStatus_Type = RowStatus
_RlCLIremoteCLIoutputRowStatus_Object = MibTableColumn
rlCLIremoteCLIoutputRowStatus = _RlCLIremoteCLIoutputRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1, 4),
    _RlCLIremoteCLIoutputRowStatus_Type()
)
rlCLIremoteCLIoutputRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputRowStatus.setStatus("current")
_RlCLIremoteCLIoutputCommandNumber_Type = Integer32
_RlCLIremoteCLIoutputCommandNumber_Object = MibTableColumn
rlCLIremoteCLIoutputCommandNumber = _RlCLIremoteCLIoutputCommandNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 6, 1, 5),
    _RlCLIremoteCLIoutputCommandNumber_Type()
)
rlCLIremoteCLIoutputCommandNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIoutputCommandNumber.setStatus("current")
_RlCLIremoteCLIinstance_Type = Integer32
_RlCLIremoteCLIinstance_Object = MibScalar
rlCLIremoteCLIinstance = _RlCLIremoteCLIinstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 52, 6, 7),
    _RlCLIremoteCLIinstance_Type()
)
rlCLIremoteCLIinstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCLIremoteCLIinstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-CLI-MIB",
    **{"rlCli": rlCli,
       "rlCliMibVersion": rlCliMibVersion,
       "rlCliPassword": rlCliPassword,
       "rlCliTimer": rlCliTimer,
       "rlCliFileEnable": rlCliFileEnable,
       "rlCliFileEnableAfterReset": rlCliFileEnableAfterReset,
       "rlCLIremoteCLIsupport": rlCLIremoteCLIsupport,
       "rlCLIremoteCLIcommand": rlCLIremoteCLIcommand,
       "rlCLIremoteCLIexecutionState": rlCLIremoteCLIexecutionState,
       "rlCLIremoteCLIexecutionCommandIndex": rlCLIremoteCLIexecutionCommandIndex,
       "rlCLIremoteCLImode": rlCLIremoteCLImode,
       "rlCLIremoteCLIcommandsTable": rlCLIremoteCLIcommandsTable,
       "rlCLIremoteCLIcommandsEntry": rlCLIremoteCLIcommandsEntry,
       "rlCLIremoteCLIcommandIndex": rlCLIremoteCLIcommandIndex,
       "rlCLIremoteCLIcommandPartNumber": rlCLIremoteCLIcommandPartNumber,
       "rlCLIremoteCLIcommandPart": rlCLIremoteCLIcommandPart,
       "rlCLIremoteCLIcommandStatus": rlCLIremoteCLIcommandStatus,
       "rlCLIremoteCLIactivationStatus": rlCLIremoteCLIactivationStatus,
       "rlCLIremoteCLIoutputsTable": rlCLIremoteCLIoutputsTable,
       "rlCLIremoteCLIoutputsEntry": rlCLIremoteCLIoutputsEntry,
       "rlCLIremoteCLIoutputRowIndex": rlCLIremoteCLIoutputRowIndex,
       "rlCLIremoteCLIoutputRowPartNumber": rlCLIremoteCLIoutputRowPartNumber,
       "rlCLIremoteCLIoutputRowPart": rlCLIremoteCLIoutputRowPart,
       "rlCLIremoteCLIoutputRowStatus": rlCLIremoteCLIoutputRowStatus,
       "rlCLIremoteCLIoutputCommandNumber": rlCLIremoteCLIoutputCommandNumber,
       "rlCLIremoteCLIinstance": rlCLIremoteCLIinstance}
)
