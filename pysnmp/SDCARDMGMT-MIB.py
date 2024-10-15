# SNMP MIB module (SDCARDMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SDCARDMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:10 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

(swTimeRangeMgmtRangeName,) = mibBuilder.importSymbols(
    "TIMERANGE-MIB",
    "swTimeRangeMgmtRangeName")


# MODULE-IDENTITY

swSDCardMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSDCardMgmtNotifications_ObjectIdentity = ObjectIdentity
swSDCardMgmtNotifications = _SwSDCardMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 0)
)
_SwSDCardMgmtMIBObjects_ObjectIdentity = ObjectIdentity
swSDCardMgmtMIBObjects = _SwSDCardMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1)
)
_SwSDCardMgmtGeneralGroup_ObjectIdentity = ObjectIdentity
swSDCardMgmtGeneralGroup = _SwSDCardMgmtGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 1)
)
_SwSDCardMgmtBackupCtrl_ObjectIdentity = ObjectIdentity
swSDCardMgmtBackupCtrl = _SwSDCardMgmtBackupCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2)
)
_SwSDCardMgmtBackupCtrlTable_Object = MibTable
swSDCardMgmtBackupCtrlTable = _SwSDCardMgmtBackupCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swSDCardMgmtBackupCtrlTable.setStatus("current")
_SwSDCardMgmtBackupCtrlEntry_Object = MibTableRow
swSDCardMgmtBackupCtrlEntry = _SwSDCardMgmtBackupCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1, 1)
)
swSDCardMgmtBackupCtrlEntry.setIndexNames(
    (0, "SDCARDMGMT-MIB", "swSDCardMgmtBackupType"),
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
    (0, "SDCARDMGMT-MIB", "swSDCardMgmtBackupFilename"),
)
if mibBuilder.loadTexts:
    swSDCardMgmtBackupCtrlEntry.setStatus("current")


class _SwSDCardMgmtBackupType_Type(Integer32):
    """Custom type swSDCardMgmtBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 1),
          ("log", 2))
    )


_SwSDCardMgmtBackupType_Type.__name__ = "Integer32"
_SwSDCardMgmtBackupType_Object = MibTableColumn
swSDCardMgmtBackupType = _SwSDCardMgmtBackupType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1, 1, 1),
    _SwSDCardMgmtBackupType_Type()
)
swSDCardMgmtBackupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSDCardMgmtBackupType.setStatus("current")


class _SwSDCardMgmtBackupFilename_Type(DisplayString):
    """Custom type swSDCardMgmtBackupFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwSDCardMgmtBackupFilename_Type.__name__ = "DisplayString"
_SwSDCardMgmtBackupFilename_Object = MibTableColumn
swSDCardMgmtBackupFilename = _SwSDCardMgmtBackupFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1, 1, 2),
    _SwSDCardMgmtBackupFilename_Type()
)
swSDCardMgmtBackupFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSDCardMgmtBackupFilename.setStatus("current")


class _SwSDCardMgmtBackupState_Type(Integer32):
    """Custom type swSDCardMgmtBackupState based on Integer32"""
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


_SwSDCardMgmtBackupState_Type.__name__ = "Integer32"
_SwSDCardMgmtBackupState_Object = MibTableColumn
swSDCardMgmtBackupState = _SwSDCardMgmtBackupState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1, 1, 3),
    _SwSDCardMgmtBackupState_Type()
)
swSDCardMgmtBackupState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSDCardMgmtBackupState.setStatus("current")
_SwSDCardMgmtBackupRowStatus_Type = RowStatus
_SwSDCardMgmtBackupRowStatus_Object = MibTableColumn
swSDCardMgmtBackupRowStatus = _SwSDCardMgmtBackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 2, 1, 1, 100),
    _SwSDCardMgmtBackupRowStatus_Type()
)
swSDCardMgmtBackupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSDCardMgmtBackupRowStatus.setStatus("current")
_SwSDCardMgmtExecCtrl_ObjectIdentity = ObjectIdentity
swSDCardMgmtExecCtrl = _SwSDCardMgmtExecCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3)
)
_SwSDCardMgmtExecCtrlTable_Object = MibTable
swSDCardMgmtExecCtrlTable = _SwSDCardMgmtExecCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1)
)
if mibBuilder.loadTexts:
    swSDCardMgmtExecCtrlTable.setStatus("current")
_SwSDCardMgmtExecCtrlEntry_Object = MibTableRow
swSDCardMgmtExecCtrlEntry = _SwSDCardMgmtExecCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1, 1)
)
swSDCardMgmtExecCtrlEntry.setIndexNames(
    (0, "TIMERANGE-MIB", "swTimeRangeMgmtRangeName"),
    (0, "SDCARDMGMT-MIB", "swSDCardMgmtExecFilename"),
)
if mibBuilder.loadTexts:
    swSDCardMgmtExecCtrlEntry.setStatus("current")


class _SwSDCardMgmtExecFilename_Type(DisplayString):
    """Custom type swSDCardMgmtExecFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwSDCardMgmtExecFilename_Type.__name__ = "DisplayString"
_SwSDCardMgmtExecFilename_Object = MibTableColumn
swSDCardMgmtExecFilename = _SwSDCardMgmtExecFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1, 1, 1),
    _SwSDCardMgmtExecFilename_Type()
)
swSDCardMgmtExecFilename.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swSDCardMgmtExecFilename.setStatus("current")


class _SwSDCardMgmtExecState_Type(Integer32):
    """Custom type swSDCardMgmtExecState based on Integer32"""
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


_SwSDCardMgmtExecState_Type.__name__ = "Integer32"
_SwSDCardMgmtExecState_Object = MibTableColumn
swSDCardMgmtExecState = _SwSDCardMgmtExecState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1, 1, 2),
    _SwSDCardMgmtExecState_Type()
)
swSDCardMgmtExecState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSDCardMgmtExecState.setStatus("current")
_SwSDCardMgmtExecIncrement_Type = TruthValue
_SwSDCardMgmtExecIncrement_Object = MibTableColumn
swSDCardMgmtExecIncrement = _SwSDCardMgmtExecIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1, 1, 3),
    _SwSDCardMgmtExecIncrement_Type()
)
swSDCardMgmtExecIncrement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSDCardMgmtExecIncrement.setStatus("current")
_SwSDCardMgmtExecRowStatus_Type = RowStatus
_SwSDCardMgmtExecRowStatus_Object = MibTableColumn
swSDCardMgmtExecRowStatus = _SwSDCardMgmtExecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 3, 1, 1, 100),
    _SwSDCardMgmtExecRowStatus_Type()
)
swSDCardMgmtExecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swSDCardMgmtExecRowStatus.setStatus("current")
_SwSDCardMgmtExecConfigCtrl_ObjectIdentity = ObjectIdentity
swSDCardMgmtExecConfigCtrl = _SwSDCardMgmtExecConfigCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 4)
)


class _SwSDCardMgmtExecConfigFilename_Type(DisplayString):
    """Custom type swSDCardMgmtExecConfigFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwSDCardMgmtExecConfigFilename_Type.__name__ = "DisplayString"
_SwSDCardMgmtExecConfigFilename_Object = MibScalar
swSDCardMgmtExecConfigFilename = _SwSDCardMgmtExecConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 4, 1),
    _SwSDCardMgmtExecConfigFilename_Type()
)
swSDCardMgmtExecConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSDCardMgmtExecConfigFilename.setStatus("current")
_SwSDCardMgmtExecConfigIncrement_Type = TruthValue
_SwSDCardMgmtExecConfigIncrement_Object = MibScalar
swSDCardMgmtExecConfigIncrement = _SwSDCardMgmtExecConfigIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 4, 2),
    _SwSDCardMgmtExecConfigIncrement_Type()
)
swSDCardMgmtExecConfigIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSDCardMgmtExecConfigIncrement.setStatus("current")


class _SwSDCardMgmtExecConfigAction_Type(Integer32):
    """Custom type swSDCardMgmtExecConfigAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwSDCardMgmtExecConfigAction_Type.__name__ = "Integer32"
_SwSDCardMgmtExecConfigAction_Object = MibScalar
swSDCardMgmtExecConfigAction = _SwSDCardMgmtExecConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 95, 1, 4, 3),
    _SwSDCardMgmtExecConfigAction_Type()
)
swSDCardMgmtExecConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSDCardMgmtExecConfigAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SDCARDMGMT-MIB",
    **{"swSDCardMgmtMIB": swSDCardMgmtMIB,
       "swSDCardMgmtNotifications": swSDCardMgmtNotifications,
       "swSDCardMgmtMIBObjects": swSDCardMgmtMIBObjects,
       "swSDCardMgmtGeneralGroup": swSDCardMgmtGeneralGroup,
       "swSDCardMgmtBackupCtrl": swSDCardMgmtBackupCtrl,
       "swSDCardMgmtBackupCtrlTable": swSDCardMgmtBackupCtrlTable,
       "swSDCardMgmtBackupCtrlEntry": swSDCardMgmtBackupCtrlEntry,
       "swSDCardMgmtBackupType": swSDCardMgmtBackupType,
       "swSDCardMgmtBackupFilename": swSDCardMgmtBackupFilename,
       "swSDCardMgmtBackupState": swSDCardMgmtBackupState,
       "swSDCardMgmtBackupRowStatus": swSDCardMgmtBackupRowStatus,
       "swSDCardMgmtExecCtrl": swSDCardMgmtExecCtrl,
       "swSDCardMgmtExecCtrlTable": swSDCardMgmtExecCtrlTable,
       "swSDCardMgmtExecCtrlEntry": swSDCardMgmtExecCtrlEntry,
       "swSDCardMgmtExecFilename": swSDCardMgmtExecFilename,
       "swSDCardMgmtExecState": swSDCardMgmtExecState,
       "swSDCardMgmtExecIncrement": swSDCardMgmtExecIncrement,
       "swSDCardMgmtExecRowStatus": swSDCardMgmtExecRowStatus,
       "swSDCardMgmtExecConfigCtrl": swSDCardMgmtExecConfigCtrl,
       "swSDCardMgmtExecConfigFilename": swSDCardMgmtExecConfigFilename,
       "swSDCardMgmtExecConfigIncrement": swSDCardMgmtExecConfigIncrement,
       "swSDCardMgmtExecConfigAction": swSDCardMgmtExecConfigAction}
)
