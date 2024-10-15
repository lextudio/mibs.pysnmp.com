# SNMP MIB module (FUJITSU-EXTENDED-NONOS-AWN-MIB-V06) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FUJITSU-EXTENDED-NONOS-AWN-MIB-V06
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:43 2024
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
 enterprises,
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
    "enterprises",
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

_Fujitsu_ObjectIdentity = ObjectIdentity
fujitsu = _Fujitsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1)
)
_Nonos_ObjectIdentity = ObjectIdentity
nonos = _Nonos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127)
)
_Awn_ObjectIdentity = ObjectIdentity
awn = _Awn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29)
)
_AwnSystem_ObjectIdentity = ObjectIdentity
awnSystem = _AwnSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1)
)
_AwnSysNode_ObjectIdentity = ObjectIdentity
awnSysNode = _AwnSysNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 1)
)


class _AwnSysNodeInformation_Type(OctetString):
    """Custom type awnSysNodeInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_AwnSysNodeInformation_Type.__name__ = "OctetString"
_AwnSysNodeInformation_Object = MibScalar
awnSysNodeInformation = _AwnSysNodeInformation_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 1, 1),
    _AwnSysNodeInformation_Type()
)
awnSysNodeInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysNodeInformation.setStatus("mandatory")


class _AwnSysNodeCommonStatus_Type(OctetString):
    """Custom type awnSysNodeCommonStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_AwnSysNodeCommonStatus_Type.__name__ = "OctetString"
_AwnSysNodeCommonStatus_Object = MibScalar
awnSysNodeCommonStatus = _AwnSysNodeCommonStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 1, 2),
    _AwnSysNodeCommonStatus_Type()
)
awnSysNodeCommonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysNodeCommonStatus.setStatus("mandatory")


class _AwnSysNodeClk_Type(OctetString):
    """Custom type awnSysNodeClk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AwnSysNodeClk_Type.__name__ = "OctetString"
_AwnSysNodeClk_Object = MibScalar
awnSysNodeClk = _AwnSysNodeClk_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 1, 3),
    _AwnSysNodeClk_Type()
)
awnSysNodeClk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysNodeClk.setStatus("mandatory")
_AwnSysCom_ObjectIdentity = ObjectIdentity
awnSysCom = _AwnSysCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 2)
)


class _AwnSysComDevice_Type(OctetString):
    """Custom type awnSysComDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_AwnSysComDevice_Type.__name__ = "OctetString"
_AwnSysComDevice_Object = MibScalar
awnSysComDevice = _AwnSysComDevice_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 2, 1),
    _AwnSysComDevice_Type()
)
awnSysComDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysComDevice.setStatus("mandatory")


class _AwnSysComPort_Type(OctetString):
    """Custom type awnSysComPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(192, 192),
    )


_AwnSysComPort_Type.__name__ = "OctetString"
_AwnSysComPort_Object = MibScalar
awnSysComPort = _AwnSysComPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 2, 2),
    _AwnSysComPort_Type()
)
awnSysComPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysComPort.setStatus("mandatory")


class _AwnSysComDevice2_Type(OctetString):
    """Custom type awnSysComDevice2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(68, 68),
    )


_AwnSysComDevice2_Type.__name__ = "OctetString"
_AwnSysComDevice2_Object = MibScalar
awnSysComDevice2 = _AwnSysComDevice2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 2, 3),
    _AwnSysComDevice2_Type()
)
awnSysComDevice2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysComDevice2.setStatus("mandatory")


class _AwnSysComPort2_Type(OctetString):
    """Custom type awnSysComPort2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(120, 120),
    )


_AwnSysComPort2_Type.__name__ = "OctetString"
_AwnSysComPort2_Object = MibScalar
awnSysComPort2 = _AwnSysComPort2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 2, 4),
    _AwnSysComPort2_Type()
)
awnSysComPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysComPort2.setStatus("mandatory")
_AwnSysLs_ObjectIdentity = ObjectIdentity
awnSysLs = _AwnSysLs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3)
)
_AwnSysLsTable_Object = MibTable
awnSysLsTable = _AwnSysLsTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1)
)
if mibBuilder.loadTexts:
    awnSysLsTable.setStatus("mandatory")
_AwnSysLsEntry_Object = MibTableRow
awnSysLsEntry = _AwnSysLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1)
)
awnSysLsEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysLsUnit"),
)
if mibBuilder.loadTexts:
    awnSysLsEntry.setStatus("mandatory")


class _AwnSysLsUnit_Type(Integer32):
    """Custom type awnSysLsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysLsUnit_Type.__name__ = "Integer32"
_AwnSysLsUnit_Object = MibTableColumn
awnSysLsUnit = _AwnSysLsUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1, 1),
    _AwnSysLsUnit_Type()
)
awnSysLsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLsUnit.setStatus("mandatory")


class _AwnSysLsDevice_Type(OctetString):
    """Custom type awnSysLsDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_AwnSysLsDevice_Type.__name__ = "OctetString"
_AwnSysLsDevice_Object = MibTableColumn
awnSysLsDevice = _AwnSysLsDevice_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1, 2),
    _AwnSysLsDevice_Type()
)
awnSysLsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLsDevice.setStatus("mandatory")


class _AwnSysLsPort_Type(OctetString):
    """Custom type awnSysLsPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(560, 560),
    )


_AwnSysLsPort_Type.__name__ = "OctetString"
_AwnSysLsPort_Object = MibTableColumn
awnSysLsPort = _AwnSysLsPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1, 3),
    _AwnSysLsPort_Type()
)
awnSysLsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLsPort.setStatus("mandatory")


class _AwnSysLsDevice2_Type(OctetString):
    """Custom type awnSysLsDevice2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )


_AwnSysLsDevice2_Type.__name__ = "OctetString"
_AwnSysLsDevice2_Object = MibScalar
awnSysLsDevice2 = _AwnSysLsDevice2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1, 4),
    _AwnSysLsDevice2_Type()
)
awnSysLsDevice2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLsDevice2.setStatus("mandatory")


class _AwnSysLsPort2_Type(OctetString):
    """Custom type awnSysLsPort2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(720, 720),
    )


_AwnSysLsPort2_Type.__name__ = "OctetString"
_AwnSysLsPort2_Object = MibScalar
awnSysLsPort2 = _AwnSysLsPort2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 3, 1, 1, 5),
    _AwnSysLsPort2_Type()
)
awnSysLsPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLsPort2.setStatus("mandatory")
_AwnSysLine_ObjectIdentity = ObjectIdentity
awnSysLine = _AwnSysLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4)
)
_AwnSysLineTable_Object = MibTable
awnSysLineTable = _AwnSysLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1)
)
if mibBuilder.loadTexts:
    awnSysLineTable.setStatus("mandatory")
_AwnSysLineEntry_Object = MibTableRow
awnSysLineEntry = _AwnSysLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1)
)
awnSysLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysLineUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysLineCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysLinePort"),
)
if mibBuilder.loadTexts:
    awnSysLineEntry.setStatus("mandatory")


class _AwnSysLineUnit_Type(Integer32):
    """Custom type awnSysLineUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysLineUnit_Type.__name__ = "Integer32"
_AwnSysLineUnit_Object = MibTableColumn
awnSysLineUnit = _AwnSysLineUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1, 1),
    _AwnSysLineUnit_Type()
)
awnSysLineUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLineUnit.setStatus("mandatory")


class _AwnSysLineCard_Type(Integer32):
    """Custom type awnSysLineCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnSysLineCard_Type.__name__ = "Integer32"
_AwnSysLineCard_Object = MibTableColumn
awnSysLineCard = _AwnSysLineCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1, 2),
    _AwnSysLineCard_Type()
)
awnSysLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLineCard.setStatus("mandatory")


class _AwnSysLinePort_Type(Integer32):
    """Custom type awnSysLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysLinePort_Type.__name__ = "Integer32"
_AwnSysLinePort_Object = MibTableColumn
awnSysLinePort = _AwnSysLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1, 3),
    _AwnSysLinePort_Type()
)
awnSysLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLinePort.setStatus("mandatory")


class _AwnSysLineChannel_Type(OctetString):
    """Custom type awnSysLineChannel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(384, 384),
    )


_AwnSysLineChannel_Type.__name__ = "OctetString"
_AwnSysLineChannel_Object = MibTableColumn
awnSysLineChannel = _AwnSysLineChannel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1, 4),
    _AwnSysLineChannel_Type()
)
awnSysLineChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLineChannel.setStatus("mandatory")


class _AwnSysLineMegalink_Type(OctetString):
    """Custom type awnSysLineMegalink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_AwnSysLineMegalink_Type.__name__ = "OctetString"
_AwnSysLineMegalink_Object = MibTableColumn
awnSysLineMegalink = _AwnSysLineMegalink_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 4, 1, 1, 5),
    _AwnSysLineMegalink_Type()
)
awnSysLineMegalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysLineMegalink.setStatus("mandatory")
_AwnSysError_ObjectIdentity = ObjectIdentity
awnSysError = _AwnSysError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 5)
)
_AwnSysErrorLog_Type = DisplayString
_AwnSysErrorLog_Object = MibScalar
awnSysErrorLog = _AwnSysErrorLog_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 5, 1),
    _AwnSysErrorLog_Type()
)
awnSysErrorLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysErrorLog.setStatus("mandatory")
_AwnSysChannel_ObjectIdentity = ObjectIdentity
awnSysChannel = _AwnSysChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6)
)
_AwnSysChannelTable_Object = MibTable
awnSysChannelTable = _AwnSysChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1)
)
if mibBuilder.loadTexts:
    awnSysChannelTable.setStatus("mandatory")
_AwnSysChannelEntry_Object = MibTableRow
awnSysChannelEntry = _AwnSysChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1)
)
awnSysChannelEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysChannelUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysChannelCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysChannelPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysChannelTimeslot"),
)
if mibBuilder.loadTexts:
    awnSysChannelEntry.setStatus("mandatory")


class _AwnSysChannelUnit_Type(Integer32):
    """Custom type awnSysChannelUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysChannelUnit_Type.__name__ = "Integer32"
_AwnSysChannelUnit_Object = MibTableColumn
awnSysChannelUnit = _AwnSysChannelUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 1),
    _AwnSysChannelUnit_Type()
)
awnSysChannelUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelUnit.setStatus("mandatory")


class _AwnSysChannelCard_Type(Integer32):
    """Custom type awnSysChannelCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnSysChannelCard_Type.__name__ = "Integer32"
_AwnSysChannelCard_Object = MibTableColumn
awnSysChannelCard = _AwnSysChannelCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 2),
    _AwnSysChannelCard_Type()
)
awnSysChannelCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelCard.setStatus("mandatory")


class _AwnSysChannelPort_Type(Integer32):
    """Custom type awnSysChannelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysChannelPort_Type.__name__ = "Integer32"
_AwnSysChannelPort_Object = MibTableColumn
awnSysChannelPort = _AwnSysChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 3),
    _AwnSysChannelPort_Type()
)
awnSysChannelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelPort.setStatus("mandatory")


class _AwnSysChannelTimeslot_Type(Integer32):
    """Custom type awnSysChannelTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnSysChannelTimeslot_Type.__name__ = "Integer32"
_AwnSysChannelTimeslot_Object = MibTableColumn
awnSysChannelTimeslot = _AwnSysChannelTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 4),
    _AwnSysChannelTimeslot_Type()
)
awnSysChannelTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelTimeslot.setStatus("mandatory")


class _AwnSysChannelBackup_Type(OctetString):
    """Custom type awnSysChannelBackup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(576, 576),
    )


_AwnSysChannelBackup_Type.__name__ = "OctetString"
_AwnSysChannelBackup_Object = MibTableColumn
awnSysChannelBackup = _AwnSysChannelBackup_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 5),
    _AwnSysChannelBackup_Type()
)
awnSysChannelBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelBackup.setStatus("mandatory")


class _AwnSysChannelBackup2_Type(OctetString):
    """Custom type awnSysChannelBackup2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_AwnSysChannelBackup2_Type.__name__ = "OctetString"
_AwnSysChannelBackup2_Object = MibTableColumn
awnSysChannelBackup2 = _AwnSysChannelBackup2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 6, 1, 1, 6),
    _AwnSysChannelBackup2_Type()
)
awnSysChannelBackup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysChannelBackup2.setStatus("mandatory")
_AwnSysEvent_ObjectIdentity = ObjectIdentity
awnSysEvent = _AwnSysEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 7)
)
_AwnSysEventTable_Object = MibTable
awnSysEventTable = _AwnSysEventTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 7, 1)
)
if mibBuilder.loadTexts:
    awnSysEventTable.setStatus("mandatory")
_AwnSysEventEntry_Object = MibTableRow
awnSysEventEntry = _AwnSysEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    awnSysEventEntry.setStatus("mandatory")
_AwnSysEventThreshold_Type = DisplayString
_AwnSysEventThreshold_Object = MibTableColumn
awnSysEventThreshold = _AwnSysEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 7, 1, 1, 1),
    _AwnSysEventThreshold_Type()
)
awnSysEventThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awnSysEventThreshold.setStatus("mandatory")
_AwnSysPort_ObjectIdentity = ObjectIdentity
awnSysPort = _AwnSysPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8)
)
_AwnSysPortTable_Object = MibTable
awnSysPortTable = _AwnSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1)
)
if mibBuilder.loadTexts:
    awnSysPortTable.setStatus("mandatory")
_AwnSysPortEntry_Object = MibTableRow
awnSysPortEntry = _AwnSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1)
)
awnSysPortEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysPortSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysPortAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysPortPort"),
)
if mibBuilder.loadTexts:
    awnSysPortEntry.setStatus("mandatory")


class _AwnSysPortSlot_Type(Integer32):
    """Custom type awnSysPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnSysPortSlot_Type.__name__ = "Integer32"
_AwnSysPortSlot_Object = MibTableColumn
awnSysPortSlot = _AwnSysPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1, 1),
    _AwnSysPortSlot_Type()
)
awnSysPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysPortSlot.setStatus("mandatory")


class _AwnSysPortAdapter_Type(Integer32):
    """Custom type awnSysPortAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnSysPortAdapter_Type.__name__ = "Integer32"
_AwnSysPortAdapter_Object = MibTableColumn
awnSysPortAdapter = _AwnSysPortAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1, 2),
    _AwnSysPortAdapter_Type()
)
awnSysPortAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysPortAdapter.setStatus("mandatory")


class _AwnSysPortPort_Type(Integer32):
    """Custom type awnSysPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnSysPortPort_Type.__name__ = "Integer32"
_AwnSysPortPort_Object = MibTableColumn
awnSysPortPort = _AwnSysPortPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1, 3),
    _AwnSysPortPort_Type()
)
awnSysPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysPortPort.setStatus("mandatory")


class _AwnSysPortMegalink_Type(OctetString):
    """Custom type awnSysPortMegalink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(244, 244),
    )


_AwnSysPortMegalink_Type.__name__ = "OctetString"
_AwnSysPortMegalink_Object = MibTableColumn
awnSysPortMegalink = _AwnSysPortMegalink_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1, 4),
    _AwnSysPortMegalink_Type()
)
awnSysPortMegalink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysPortMegalink.setStatus("mandatory")


class _AwnSysPortMegalink2_Type(OctetString):
    """Custom type awnSysPortMegalink2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_AwnSysPortMegalink2_Type.__name__ = "OctetString"
_AwnSysPortMegalink2_Object = MibTableColumn
awnSysPortMegalink2 = _AwnSysPortMegalink2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 8, 1, 1, 5),
    _AwnSysPortMegalink2_Type()
)
awnSysPortMegalink2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysPortMegalink2.setStatus("mandatory")
_AwnSysConnComVcc_ObjectIdentity = ObjectIdentity
awnSysConnComVcc = _AwnSysConnComVcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9)
)
_AwnSysConnComVccTable_Object = MibTable
awnSysConnComVccTable = _AwnSysConnComVccTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1)
)
if mibBuilder.loadTexts:
    awnSysConnComVccTable.setStatus("mandatory")
_AwnSysConnComVccEntry_Object = MibTableRow
awnSysConnComVccEntry = _AwnSysConnComVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1)
)
awnSysConnComVccEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnComVccSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnComVccAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnComVccPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnComVccVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnComVccVci"),
)
if mibBuilder.loadTexts:
    awnSysConnComVccEntry.setStatus("mandatory")


class _AwnSysConnComVccSlot_Type(Integer32):
    """Custom type awnSysConnComVccSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnSysConnComVccSlot_Type.__name__ = "Integer32"
_AwnSysConnComVccSlot_Object = MibTableColumn
awnSysConnComVccSlot = _AwnSysConnComVccSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 1),
    _AwnSysConnComVccSlot_Type()
)
awnSysConnComVccSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccSlot.setStatus("mandatory")


class _AwnSysConnComVccAdapter_Type(Integer32):
    """Custom type awnSysConnComVccAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnSysConnComVccAdapter_Type.__name__ = "Integer32"
_AwnSysConnComVccAdapter_Object = MibTableColumn
awnSysConnComVccAdapter = _AwnSysConnComVccAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 2),
    _AwnSysConnComVccAdapter_Type()
)
awnSysConnComVccAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccAdapter.setStatus("mandatory")


class _AwnSysConnComVccPort_Type(Integer32):
    """Custom type awnSysConnComVccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnSysConnComVccPort_Type.__name__ = "Integer32"
_AwnSysConnComVccPort_Object = MibTableColumn
awnSysConnComVccPort = _AwnSysConnComVccPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 3),
    _AwnSysConnComVccPort_Type()
)
awnSysConnComVccPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccPort.setStatus("mandatory")


class _AwnSysConnComVccVpi_Type(Integer32):
    """Custom type awnSysConnComVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnSysConnComVccVpi_Type.__name__ = "Integer32"
_AwnSysConnComVccVpi_Object = MibTableColumn
awnSysConnComVccVpi = _AwnSysConnComVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 4),
    _AwnSysConnComVccVpi_Type()
)
awnSysConnComVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccVpi.setStatus("mandatory")


class _AwnSysConnComVccVci_Type(Integer32):
    """Custom type awnSysConnComVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AwnSysConnComVccVci_Type.__name__ = "Integer32"
_AwnSysConnComVccVci_Object = MibTableColumn
awnSysConnComVccVci = _AwnSysConnComVccVci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 5),
    _AwnSysConnComVccVci_Type()
)
awnSysConnComVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccVci.setStatus("mandatory")


class _AwnSysConnComVccState_Type(OctetString):
    """Custom type awnSysConnComVccState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_AwnSysConnComVccState_Type.__name__ = "OctetString"
_AwnSysConnComVccState_Object = MibTableColumn
awnSysConnComVccState = _AwnSysConnComVccState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 9, 1, 1, 6),
    _AwnSysConnComVccState_Type()
)
awnSysConnComVccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnComVccState.setStatus("mandatory")
_AwnSysConnLsVcc_ObjectIdentity = ObjectIdentity
awnSysConnLsVcc = _AwnSysConnLsVcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10)
)
_AwnSysConnLsVccTable_Object = MibTable
awnSysConnLsVccTable = _AwnSysConnLsVccTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1)
)
if mibBuilder.loadTexts:
    awnSysConnLsVccTable.setStatus("mandatory")
_AwnSysConnLsVccEntry_Object = MibTableRow
awnSysConnLsVccEntry = _AwnSysConnLsVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1)
)
awnSysConnLsVccEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccTimeslot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnSysConnLsVccVci"),
)
if mibBuilder.loadTexts:
    awnSysConnLsVccEntry.setStatus("mandatory")


class _AwnSysConnLsVccUnit_Type(Integer32):
    """Custom type awnSysConnLsVccUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysConnLsVccUnit_Type.__name__ = "Integer32"
_AwnSysConnLsVccUnit_Object = MibTableColumn
awnSysConnLsVccUnit = _AwnSysConnLsVccUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 1),
    _AwnSysConnLsVccUnit_Type()
)
awnSysConnLsVccUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccUnit.setStatus("mandatory")


class _AwnSysConnLSVccCard_Type(Integer32):
    """Custom type awnSysConnLSVccCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnSysConnLSVccCard_Type.__name__ = "Integer32"
_AwnSysConnLSVccCard_Object = MibScalar
awnSysConnLSVccCard = _AwnSysConnLSVccCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 2),
    _AwnSysConnLSVccCard_Type()
)
awnSysConnLSVccCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLSVccCard.setStatus("mandatory")


class _AwnSysConnLsVccPort_Type(Integer32):
    """Custom type awnSysConnLsVccPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnSysConnLsVccPort_Type.__name__ = "Integer32"
_AwnSysConnLsVccPort_Object = MibTableColumn
awnSysConnLsVccPort = _AwnSysConnLsVccPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 3),
    _AwnSysConnLsVccPort_Type()
)
awnSysConnLsVccPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccPort.setStatus("mandatory")


class _AwnSysConnLsVccTimeslot_Type(Integer32):
    """Custom type awnSysConnLsVccTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AwnSysConnLsVccTimeslot_Type.__name__ = "Integer32"
_AwnSysConnLsVccTimeslot_Object = MibTableColumn
awnSysConnLsVccTimeslot = _AwnSysConnLsVccTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 4),
    _AwnSysConnLsVccTimeslot_Type()
)
awnSysConnLsVccTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccTimeslot.setStatus("mandatory")


class _AwnSysConnLsVccVpi_Type(Integer32):
    """Custom type awnSysConnLsVccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnSysConnLsVccVpi_Type.__name__ = "Integer32"
_AwnSysConnLsVccVpi_Object = MibTableColumn
awnSysConnLsVccVpi = _AwnSysConnLsVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 5),
    _AwnSysConnLsVccVpi_Type()
)
awnSysConnLsVccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccVpi.setStatus("mandatory")


class _AwnSysConnLsVccVci_Type(Integer32):
    """Custom type awnSysConnLsVccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AwnSysConnLsVccVci_Type.__name__ = "Integer32"
_AwnSysConnLsVccVci_Object = MibTableColumn
awnSysConnLsVccVci = _AwnSysConnLsVccVci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 6),
    _AwnSysConnLsVccVci_Type()
)
awnSysConnLsVccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccVci.setStatus("mandatory")


class _AwnSysConnLsVccState_Type(OctetString):
    """Custom type awnSysConnLsVccState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_AwnSysConnLsVccState_Type.__name__ = "OctetString"
_AwnSysConnLsVccState_Object = MibTableColumn
awnSysConnLsVccState = _AwnSysConnLsVccState_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 10, 1, 1, 7),
    _AwnSysConnLsVccState_Type()
)
awnSysConnLsVccState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnSysConnLsVccState.setStatus("mandatory")
_AwnSysBackIpAddr_ObjectIdentity = ObjectIdentity
awnSysBackIpAddr = _AwnSysBackIpAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 1, 11)
)
_AwnStatistics_ObjectIdentity = ObjectIdentity
awnStatistics = _AwnStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2)
)
_AwnStatisticsSw_ObjectIdentity = ObjectIdentity
awnStatisticsSw = _AwnStatisticsSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 1)
)


class _AwnStatisticsSwport_Type(OctetString):
    """Custom type awnStatisticsSwport based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AwnStatisticsSwport_Type.__name__ = "OctetString"
_AwnStatisticsSwport_Object = MibScalar
awnStatisticsSwport = _AwnStatisticsSwport_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 1, 1),
    _AwnStatisticsSwport_Type()
)
awnStatisticsSwport.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awnStatisticsSwport.setStatus("obsolete")
_AwnStatisticsLine_ObjectIdentity = ObjectIdentity
awnStatisticsLine = _AwnStatisticsLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2)
)
_AwnStatisticsLineTable_Object = MibTable
awnStatisticsLineTable = _AwnStatisticsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLineTable.setStatus("obsolete")
_AwnStatisticsLineEntry_Object = MibTableRow
awnStatisticsLineEntry = _AwnStatisticsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1)
)
awnStatisticsLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLineUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLineCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLinePort"),
)
if mibBuilder.loadTexts:
    awnStatisticsLineEntry.setStatus("obsolete")
_AwnStatisticsLineUnit_Type = Integer32
_AwnStatisticsLineUnit_Object = MibTableColumn
awnStatisticsLineUnit = _AwnStatisticsLineUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 1),
    _AwnStatisticsLineUnit_Type()
)
awnStatisticsLineUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLineUnit.setStatus("obsolete")
_AwnStatisticsLineCard_Type = Integer32
_AwnStatisticsLineCard_Object = MibTableColumn
awnStatisticsLineCard = _AwnStatisticsLineCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 2),
    _AwnStatisticsLineCard_Type()
)
awnStatisticsLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLineCard.setStatus("obsolete")
_AwnStatisticsLinePort_Type = Integer32
_AwnStatisticsLinePort_Object = MibTableColumn
awnStatisticsLinePort = _AwnStatisticsLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 3),
    _AwnStatisticsLinePort_Type()
)
awnStatisticsLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLinePort.setStatus("obsolete")


class _AwnStatisticsLinePriWan_Type(OctetString):
    """Custom type awnStatisticsLinePriWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AwnStatisticsLinePriWan_Type.__name__ = "OctetString"
_AwnStatisticsLinePriWan_Object = MibTableColumn
awnStatisticsLinePriWan = _AwnStatisticsLinePriWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 4),
    _AwnStatisticsLinePriWan_Type()
)
awnStatisticsLinePriWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLinePriWan.setStatus("obsolete")


class _AwnStatisticsLineSriWan_Type(OctetString):
    """Custom type awnStatisticsLineSriWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AwnStatisticsLineSriWan_Type.__name__ = "OctetString"
_AwnStatisticsLineSriWan_Object = MibTableColumn
awnStatisticsLineSriWan = _AwnStatisticsLineSriWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 5),
    _AwnStatisticsLineSriWan_Type()
)
awnStatisticsLineSriWan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    awnStatisticsLineSriWan.setStatus("obsolete")


class _AwnStatisticsLineBriWan_Type(OctetString):
    """Custom type awnStatisticsLineBriWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )


_AwnStatisticsLineBriWan_Type.__name__ = "OctetString"
_AwnStatisticsLineBriWan_Object = MibTableColumn
awnStatisticsLineBriWan = _AwnStatisticsLineBriWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 2, 1, 1, 6),
    _AwnStatisticsLineBriWan_Type()
)
awnStatisticsLineBriWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLineBriWan.setStatus("obsolete")
_AwnStatisticsComLine_ObjectIdentity = ObjectIdentity
awnStatisticsComLine = _AwnStatisticsComLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3)
)
_AwnStatisticsComLineTable_Object = MibTable
awnStatisticsComLineTable = _AwnStatisticsComLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComLineTable.setStatus("mandatory")
_AwnStatisticsComLineEntry_Object = MibTableRow
awnStatisticsComLineEntry = _AwnStatisticsComLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1)
)
awnStatisticsComLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComLineSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComLineAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComLinePort"),
)
if mibBuilder.loadTexts:
    awnStatisticsComLineEntry.setStatus("mandatory")


class _AwnStatisticsComLineSlot_Type(Integer32):
    """Custom type awnStatisticsComLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComLineSlot_Type.__name__ = "Integer32"
_AwnStatisticsComLineSlot_Object = MibTableColumn
awnStatisticsComLineSlot = _AwnStatisticsComLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1, 1),
    _AwnStatisticsComLineSlot_Type()
)
awnStatisticsComLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComLineSlot.setStatus("mandatory")


class _AwnStatisticsComLineAdapter_Type(Integer32):
    """Custom type awnStatisticsComLineAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComLineAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComLineAdapter_Object = MibTableColumn
awnStatisticsComLineAdapter = _AwnStatisticsComLineAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1, 2),
    _AwnStatisticsComLineAdapter_Type()
)
awnStatisticsComLineAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComLineAdapter.setStatus("mandatory")


class _AwnStatisticsComLinePort_Type(Integer32):
    """Custom type awnStatisticsComLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComLinePort_Type.__name__ = "Integer32"
_AwnStatisticsComLinePort_Object = MibTableColumn
awnStatisticsComLinePort = _AwnStatisticsComLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1, 3),
    _AwnStatisticsComLinePort_Type()
)
awnStatisticsComLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComLinePort.setStatus("mandatory")


class _AwnStatisticsComLineAtm_Type(OctetString):
    """Custom type awnStatisticsComLineAtm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(132, 132),
    )


_AwnStatisticsComLineAtm_Type.__name__ = "OctetString"
_AwnStatisticsComLineAtm_Object = MibTableColumn
awnStatisticsComLineAtm = _AwnStatisticsComLineAtm_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1, 4),
    _AwnStatisticsComLineAtm_Type()
)
awnStatisticsComLineAtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComLineAtm.setStatus("mandatory")


class _AwnStatisticsComLan_Type(OctetString):
    """Custom type awnStatisticsComLan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(264, 264),
    )


_AwnStatisticsComLan_Type.__name__ = "OctetString"
_AwnStatisticsComLan_Object = MibTableColumn
awnStatisticsComLan = _AwnStatisticsComLan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 3, 1, 1, 5),
    _AwnStatisticsComLan_Type()
)
awnStatisticsComLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComLan.setStatus("mandatory")
_AwnStatisticsLsLine_ObjectIdentity = ObjectIdentity
awnStatisticsLsLine = _AwnStatisticsLsLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4)
)
_AwnStatisticsLsLineTable_Object = MibTable
awnStatisticsLsLineTable = _AwnStatisticsLsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsLineTable.setStatus("mandatory")
_AwnStatisticsLsLineEntry_Object = MibTableRow
awnStatisticsLsLineEntry = _AwnStatisticsLsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1)
)
awnStatisticsLsLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsLineUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsLineCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsLinePort"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsLineEntry.setStatus("mandatory")


class _AwnStatisticsLsLineUnit_Type(Integer32):
    """Custom type awnStatisticsLsLineUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsLineUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsLineUnit_Object = MibScalar
awnStatisticsLsLineUnit = _AwnStatisticsLsLineUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 1),
    _AwnStatisticsLsLineUnit_Type()
)
awnStatisticsLsLineUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineUnit.setStatus("mandatory")


class _AwnStatisticsLsLineCard_Type(Integer32):
    """Custom type awnStatisticsLsLineCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsLineCard_Type.__name__ = "Integer32"
_AwnStatisticsLsLineCard_Object = MibScalar
awnStatisticsLsLineCard = _AwnStatisticsLsLineCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 2),
    _AwnStatisticsLsLineCard_Type()
)
awnStatisticsLsLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineCard.setStatus("mandatory")


class _AwnStatisticsLsLinePort_Type(Integer32):
    """Custom type awnStatisticsLsLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsLinePort_Type.__name__ = "Integer32"
_AwnStatisticsLsLinePort_Object = MibTableColumn
awnStatisticsLsLinePort = _AwnStatisticsLsLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 3),
    _AwnStatisticsLsLinePort_Type()
)
awnStatisticsLsLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLinePort.setStatus("mandatory")


class _AwnStatisticsLsLinePriWan_Type(OctetString):
    """Custom type awnStatisticsLsLinePriWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(504, 504),
    )


_AwnStatisticsLsLinePriWan_Type.__name__ = "OctetString"
_AwnStatisticsLsLinePriWan_Object = MibTableColumn
awnStatisticsLsLinePriWan = _AwnStatisticsLsLinePriWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 4),
    _AwnStatisticsLsLinePriWan_Type()
)
awnStatisticsLsLinePriWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLinePriWan.setStatus("mandatory")


class _AwnStatisticsLsLineBriWan_Type(OctetString):
    """Custom type awnStatisticsLsLineBriWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(120, 120),
    )


_AwnStatisticsLsLineBriWan_Type.__name__ = "OctetString"
_AwnStatisticsLsLineBriWan_Object = MibTableColumn
awnStatisticsLsLineBriWan = _AwnStatisticsLsLineBriWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 5),
    _AwnStatisticsLsLineBriWan_Type()
)
awnStatisticsLsLineBriWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineBriWan.setStatus("mandatory")


class _AwnStatisticsLsLinePriBup_Type(OctetString):
    """Custom type awnStatisticsLsLinePriBup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(120, 120),
    )


_AwnStatisticsLsLinePriBup_Type.__name__ = "OctetString"
_AwnStatisticsLsLinePriBup_Object = MibTableColumn
awnStatisticsLsLinePriBup = _AwnStatisticsLsLinePriBup_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 6),
    _AwnStatisticsLsLinePriBup_Type()
)
awnStatisticsLsLinePriBup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLinePriBup.setStatus("mandatory")


class _AwnStatisticsLsLineFrclad_Type(OctetString):
    """Custom type awnStatisticsLsLineFrclad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(504, 504),
    )


_AwnStatisticsLsLineFrclad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFrclad_Object = MibTableColumn
awnStatisticsLsLineFrclad = _AwnStatisticsLsLineFrclad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 7),
    _AwnStatisticsLsLineFrclad_Type()
)
awnStatisticsLsLineFrclad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFrclad.setStatus("mandatory")


class _AwnStatisticsLsLineFrclad2_Type(OctetString):
    """Custom type awnStatisticsLsLineFrclad2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(584, 584),
    )


_AwnStatisticsLsLineFrclad2_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFrclad2_Object = MibTableColumn
awnStatisticsLsLineFrclad2 = _AwnStatisticsLsLineFrclad2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 8),
    _AwnStatisticsLsLineFrclad2_Type()
)
awnStatisticsLsLineFrclad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFrclad2.setStatus("mandatory")


class _AwnStatisticsLsLineFrclad3_Type(OctetString):
    """Custom type awnStatisticsLsLineFrclad3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(584, 584),
    )


_AwnStatisticsLsLineFrclad3_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFrclad3_Object = MibTableColumn
awnStatisticsLsLineFrclad3 = _AwnStatisticsLsLineFrclad3_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 9),
    _AwnStatisticsLsLineFrclad3_Type()
)
awnStatisticsLsLineFrclad3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFrclad3.setStatus("mandatory")


class _AwnStatisticsLsLineLineDif_Type(OctetString):
    """Custom type awnStatisticsLsLineLineDif based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_AwnStatisticsLsLineLineDif_Type.__name__ = "OctetString"
_AwnStatisticsLsLineLineDif_Object = MibScalar
awnStatisticsLsLineLineDif = _AwnStatisticsLsLineLineDif_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 10),
    _AwnStatisticsLsLineLineDif_Type()
)
awnStatisticsLsLineLineDif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineLineDif.setStatus("mandatory")


class _AwnStatisticsLsLineDifFrclad_Type(OctetString):
    """Custom type awnStatisticsLsLineDifFrclad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(160, 160),
    )


_AwnStatisticsLsLineDifFrclad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineDifFrclad_Object = MibTableColumn
awnStatisticsLsLineDifFrclad = _AwnStatisticsLsLineDifFrclad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 11),
    _AwnStatisticsLsLineDifFrclad_Type()
)
awnStatisticsLsLineDifFrclad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineDifFrclad.setStatus("mandatory")


class _AwnStatisticsLsLinePriCes_Type(OctetString):
    """Custom type awnStatisticsLsLinePriCes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(328, 328),
    )


_AwnStatisticsLsLinePriCes_Type.__name__ = "OctetString"
_AwnStatisticsLsLinePriCes_Object = MibTableColumn
awnStatisticsLsLinePriCes = _AwnStatisticsLsLinePriCes_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 12),
    _AwnStatisticsLsLinePriCes_Type()
)
awnStatisticsLsLinePriCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLinePriCes.setStatus("mandatory")


class _AwnStatisticsLsLineDtkCodec_Type(OctetString):
    """Custom type awnStatisticsLsLineDtkCodec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(724, 724),
    )


_AwnStatisticsLsLineDtkCodec_Type.__name__ = "OctetString"
_AwnStatisticsLsLineDtkCodec_Object = MibTableColumn
awnStatisticsLsLineDtkCodec = _AwnStatisticsLsLineDtkCodec_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 13),
    _AwnStatisticsLsLineDtkCodec_Type()
)
awnStatisticsLsLineDtkCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineDtkCodec.setStatus("mandatory")


class _AwnStatisticsLsLineDtkDclad_Type(OctetString):
    """Custom type awnStatisticsLsLineDtkDclad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(600, 600),
    )


_AwnStatisticsLsLineDtkDclad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineDtkDclad_Object = MibTableColumn
awnStatisticsLsLineDtkDclad = _AwnStatisticsLsLineDtkDclad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 14),
    _AwnStatisticsLsLineDtkDclad_Type()
)
awnStatisticsLsLineDtkDclad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineDtkDclad.setStatus("mandatory")


class _AwnStatisticsLsLineDtkDclad2_Type(OctetString):
    """Custom type awnStatisticsLsLineDtkDclad2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(352, 352),
    )


_AwnStatisticsLsLineDtkDclad2_Type.__name__ = "OctetString"
_AwnStatisticsLsLineDtkDclad2_Object = MibTableColumn
awnStatisticsLsLineDtkDclad2 = _AwnStatisticsLsLineDtkDclad2_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 15),
    _AwnStatisticsLsLineDtkDclad2_Type()
)
awnStatisticsLsLineDtkDclad2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineDtkDclad2.setStatus("mandatory")


class _AwnStatisticsLsLineOdtCodec_Type(OctetString):
    """Custom type awnStatisticsLsLineOdtCodec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )


_AwnStatisticsLsLineOdtCodec_Type.__name__ = "OctetString"
_AwnStatisticsLsLineOdtCodec_Object = MibTableColumn
awnStatisticsLsLineOdtCodec = _AwnStatisticsLsLineOdtCodec_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 16),
    _AwnStatisticsLsLineOdtCodec_Type()
)
awnStatisticsLsLineOdtCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineOdtCodec.setStatus("mandatory")


class _AwnStatisticsLsLineOdtDclad_Type(OctetString):
    """Custom type awnStatisticsLsLineOdtDclad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_AwnStatisticsLsLineOdtDclad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineOdtDclad_Object = MibTableColumn
awnStatisticsLsLineOdtDclad = _AwnStatisticsLsLineOdtDclad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 17),
    _AwnStatisticsLsLineOdtDclad_Type()
)
awnStatisticsLsLineOdtDclad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineOdtDclad.setStatus("mandatory")


class _AwnStatisticsLsLineSriCes_Type(OctetString):
    """Custom type awnStatisticsLsLineSriCes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(112, 112),
    )


_AwnStatisticsLsLineSriCes_Type.__name__ = "OctetString"
_AwnStatisticsLsLineSriCes_Object = MibTableColumn
awnStatisticsLsLineSriCes = _AwnStatisticsLsLineSriCes_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 18),
    _AwnStatisticsLsLineSriCes_Type()
)
awnStatisticsLsLineSriCes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineSriCes.setStatus("mandatory")


class _AwnStatisticsLsLineBriBup_Type(OctetString):
    """Custom type awnStatisticsLsLineBriBup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(120, 120),
    )


_AwnStatisticsLsLineBriBup_Type.__name__ = "OctetString"
_AwnStatisticsLsLineBriBup_Object = MibTableColumn
awnStatisticsLsLineBriBup = _AwnStatisticsLsLineBriBup_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 19),
    _AwnStatisticsLsLineBriBup_Type()
)
awnStatisticsLsLineBriBup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineBriBup.setStatus("mandatory")


class _AwnStatisticsLsLineLrcrad_Type(OctetString):
    """Custom type awnStatisticsLsLineLrcrad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(124, 124),
    )


_AwnStatisticsLsLineLrcrad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineLrcrad_Object = MibScalar
awnStatisticsLsLineLrcrad = _AwnStatisticsLsLineLrcrad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 20),
    _AwnStatisticsLsLineLrcrad_Type()
)
awnStatisticsLsLineLrcrad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineLrcrad.setStatus("mandatory")


class _AwnStatisticsLsLine45Mwan_Type(OctetString):
    """Custom type awnStatisticsLsLine45Mwan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(152, 152),
    )


_AwnStatisticsLsLine45Mwan_Type.__name__ = "OctetString"
_AwnStatisticsLsLine45Mwan_Object = MibTableColumn
awnStatisticsLsLine45Mwan = _AwnStatisticsLsLine45Mwan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 21),
    _AwnStatisticsLsLine45Mwan_Type()
)
awnStatisticsLsLine45Mwan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLine45Mwan.setStatus("mandatory")


class _AwnStatisticsLsLineOdtCodecS_Type(OctetString):
    """Custom type awnStatisticsLsLineOdtCodecS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(144, 144),
    )


_AwnStatisticsLsLineOdtCodecS_Type.__name__ = "OctetString"
_AwnStatisticsLsLineOdtCodecS_Object = MibTableColumn
awnStatisticsLsLineOdtCodecS = _AwnStatisticsLsLineOdtCodecS_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 22),
    _AwnStatisticsLsLineOdtCodecS_Type()
)
awnStatisticsLsLineOdtCodecS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineOdtCodecS.setStatus("mandatory")


class _AwnStatisticsLsLinePriWan24_Type(OctetString):
    """Custom type awnStatisticsLsLinePriWan24 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(500, 500),
    )


_AwnStatisticsLsLinePriWan24_Type.__name__ = "OctetString"
_AwnStatisticsLsLinePriWan24_Object = MibTableColumn
awnStatisticsLsLinePriWan24 = _AwnStatisticsLsLinePriWan24_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 23),
    _AwnStatisticsLsLinePriWan24_Type()
)
awnStatisticsLsLinePriWan24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLinePriWan24.setStatus("mandatory")


class _AwnStatisticsLsLineFfclad24a_Type(OctetString):
    """Custom type awnStatisticsLsLineFfclad24a based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(496, 496),
    )


_AwnStatisticsLsLineFfclad24a_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFfclad24a_Object = MibTableColumn
awnStatisticsLsLineFfclad24a = _AwnStatisticsLsLineFfclad24a_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 24),
    _AwnStatisticsLsLineFfclad24a_Type()
)
awnStatisticsLsLineFfclad24a.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFfclad24a.setStatus("mandatory")


class _AwnStatisticsLsLineFfclad24b_Type(OctetString):
    """Custom type awnStatisticsLsLineFfclad24b based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(584, 584),
    )


_AwnStatisticsLsLineFfclad24b_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFfclad24b_Object = MibTableColumn
awnStatisticsLsLineFfclad24b = _AwnStatisticsLsLineFfclad24b_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 25),
    _AwnStatisticsLsLineFfclad24b_Type()
)
awnStatisticsLsLineFfclad24b.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFfclad24b.setStatus("mandatory")


class _AwnStatisticsLsLineFfclad24c_Type(OctetString):
    """Custom type awnStatisticsLsLineFfclad24c based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(588, 588),
    )


_AwnStatisticsLsLineFfclad24c_Type.__name__ = "OctetString"
_AwnStatisticsLsLineFfclad24c_Object = MibTableColumn
awnStatisticsLsLineFfclad24c = _AwnStatisticsLsLineFfclad24c_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 26),
    _AwnStatisticsLsLineFfclad24c_Type()
)
awnStatisticsLsLineFfclad24c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineFfclad24c.setStatus("mandatory")


class _AwnStatisticsLsLineVxaWan_Type(OctetString):
    """Custom type awnStatisticsLsLineVxaWan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(116, 116),
    )


_AwnStatisticsLsLineVxaWan_Type.__name__ = "OctetString"
_AwnStatisticsLsLineVxaWan_Object = MibTableColumn
awnStatisticsLsLineVxaWan = _AwnStatisticsLsLineVxaWan_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 27),
    _AwnStatisticsLsLineVxaWan_Type()
)
awnStatisticsLsLineVxaWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineVxaWan.setStatus("mandatory")


class _AwnStatisticsLsLineBriClad_Type(OctetString):
    """Custom type awnStatisticsLsLineBriClad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(160, 160),
    )


_AwnStatisticsLsLineBriClad_Type.__name__ = "OctetString"
_AwnStatisticsLsLineBriClad_Object = MibTableColumn
awnStatisticsLsLineBriClad = _AwnStatisticsLsLineBriClad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 4, 1, 1, 28),
    _AwnStatisticsLsLineBriClad_Type()
)
awnStatisticsLsLineBriClad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsLineBriClad.setStatus("mandatory")
_AwnStatisticsComNniPort_ObjectIdentity = ObjectIdentity
awnStatisticsComNniPort = _AwnStatisticsComNniPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5)
)
_AwnStatisticsComNniPortTable_Object = MibTable
awnStatisticsComNniPortTable = _AwnStatisticsComNniPortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComNniPortTable.setStatus("mandatory")
_AwnStatisticsComNniPortEntry_Object = MibTableRow
awnStatisticsComNniPortEntry = _AwnStatisticsComNniPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1, 1)
)
awnStatisticsComNniPortEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortPort"),
)
if mibBuilder.loadTexts:
    awnStatisticsComNniPortEntry.setStatus("mandatory")


class _AwnStatisticsComNniPortSlot_Type(Integer32):
    """Custom type awnStatisticsComNniPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniPortSlot_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortSlot_Object = MibTableColumn
awnStatisticsComNniPortSlot = _AwnStatisticsComNniPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1, 1, 1),
    _AwnStatisticsComNniPortSlot_Type()
)
awnStatisticsComNniPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortSlot.setStatus("mandatory")


class _AwnStatisticsComNniPortAdapter_Type(Integer32):
    """Custom type awnStatisticsComNniPortAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComNniPortAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortAdapter_Object = MibTableColumn
awnStatisticsComNniPortAdapter = _AwnStatisticsComNniPortAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1, 1, 2),
    _AwnStatisticsComNniPortAdapter_Type()
)
awnStatisticsComNniPortAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortAdapter.setStatus("mandatory")


class _AwnStatisticsComNniPortPort_Type(Integer32):
    """Custom type awnStatisticsComNniPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniPortPort_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortPort_Object = MibTableColumn
awnStatisticsComNniPortPort = _AwnStatisticsComNniPortPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1, 1, 3),
    _AwnStatisticsComNniPortPort_Type()
)
awnStatisticsComNniPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortPort.setStatus("mandatory")


class _AwnStatisticsComNniPortData_Type(OctetString):
    """Custom type awnStatisticsComNniPortData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(456, 456),
    )


_AwnStatisticsComNniPortData_Type.__name__ = "OctetString"
_AwnStatisticsComNniPortData_Object = MibTableColumn
awnStatisticsComNniPortData = _AwnStatisticsComNniPortData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 5, 1, 1, 4),
    _AwnStatisticsComNniPortData_Type()
)
awnStatisticsComNniPortData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortData.setStatus("mandatory")
_AwnStatisticsComNniVp_ObjectIdentity = ObjectIdentity
awnStatisticsComNniVp = _AwnStatisticsComNniVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6)
)
_AwnStatisticsComNniVpTable_Object = MibTable
awnStatisticsComNniVpTable = _AwnStatisticsComNniVpTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComNniVpTable.setStatus("mandatory")
_AwnStatisticsComNniVpEntry_Object = MibTableRow
awnStatisticsComNniVpEntry = _AwnStatisticsComNniVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1)
)
awnStatisticsComNniVpEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpVpi"),
)
if mibBuilder.loadTexts:
    awnStatisticsComNniVpEntry.setStatus("mandatory")


class _AwnStatisticsComNniVpSlot_Type(Integer32):
    """Custom type awnStatisticsComNniVpSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniVpSlot_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpSlot_Object = MibTableColumn
awnStatisticsComNniVpSlot = _AwnStatisticsComNniVpSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1, 1),
    _AwnStatisticsComNniVpSlot_Type()
)
awnStatisticsComNniVpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpSlot.setStatus("mandatory")


class _AwnStatisticsComNniVpAdapter_Type(Integer32):
    """Custom type awnStatisticsComNniVpAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComNniVpAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpAdapter_Object = MibTableColumn
awnStatisticsComNniVpAdapter = _AwnStatisticsComNniVpAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1, 2),
    _AwnStatisticsComNniVpAdapter_Type()
)
awnStatisticsComNniVpAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpAdapter.setStatus("mandatory")


class _AwnStatisticsComNniVpPort_Type(Integer32):
    """Custom type awnStatisticsComNniVpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniVpPort_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpPort_Object = MibTableColumn
awnStatisticsComNniVpPort = _AwnStatisticsComNniVpPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1, 3),
    _AwnStatisticsComNniVpPort_Type()
)
awnStatisticsComNniVpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpPort.setStatus("mandatory")


class _AwnStatisticsComNniVpVpi_Type(Integer32):
    """Custom type awnStatisticsComNniVpVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AwnStatisticsComNniVpVpi_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpVpi_Object = MibTableColumn
awnStatisticsComNniVpVpi = _AwnStatisticsComNniVpVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1, 4),
    _AwnStatisticsComNniVpVpi_Type()
)
awnStatisticsComNniVpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpVpi.setStatus("mandatory")


class _AwnStatisticsComNniVptData_Type(OctetString):
    """Custom type awnStatisticsComNniVptData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(456, 456),
    )


_AwnStatisticsComNniVptData_Type.__name__ = "OctetString"
_AwnStatisticsComNniVptData_Object = MibScalar
awnStatisticsComNniVptData = _AwnStatisticsComNniVptData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 6, 1, 1, 5),
    _AwnStatisticsComNniVptData_Type()
)
awnStatisticsComNniVptData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVptData.setStatus("mandatory")
_AwnStatisticsLsWanTs_ObjectIdentity = ObjectIdentity
awnStatisticsLsWanTs = _AwnStatisticsLsWanTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7)
)
_AwnStatisticsLsWanTsTable_Object = MibTable
awnStatisticsLsWanTsTable = _AwnStatisticsLsWanTsTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsTable.setStatus("mandatory")
_AwnStatisticsLsWanTsEntry_Object = MibTableRow
awnStatisticsLsWanTsEntry = _AwnStatisticsLsWanTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1)
)
awnStatisticsLsWanTsEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsTs"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsEntry.setStatus("mandatory")


class _AwnStatisticsLsWanTsUnit_Type(Integer32):
    """Custom type awnStatisticsLsWanTsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanTsUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsUnit_Object = MibTableColumn
awnStatisticsLsWanTsUnit = _AwnStatisticsLsWanTsUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1, 1),
    _AwnStatisticsLsWanTsUnit_Type()
)
awnStatisticsLsWanTsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsUnit.setStatus("mandatory")


class _AwnStatisticsLsWanTsCard_Type(Integer32):
    """Custom type awnStatisticsLsWanTsCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsWanTsCard_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsCard_Object = MibTableColumn
awnStatisticsLsWanTsCard = _AwnStatisticsLsWanTsCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1, 2),
    _AwnStatisticsLsWanTsCard_Type()
)
awnStatisticsLsWanTsCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsCard.setStatus("mandatory")


class _AwnStatisticsLsWanTsPort_Type(Integer32):
    """Custom type awnStatisticsLsWanTsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanTsPort_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsPort_Object = MibTableColumn
awnStatisticsLsWanTsPort = _AwnStatisticsLsWanTsPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1, 3),
    _AwnStatisticsLsWanTsPort_Type()
)
awnStatisticsLsWanTsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsPort.setStatus("mandatory")


class _AwnStatisticsLsWanTsTs_Type(Integer32):
    """Custom type awnStatisticsLsWanTsTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsLsWanTsTs_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsTs_Object = MibTableColumn
awnStatisticsLsWanTsTs = _AwnStatisticsLsWanTsTs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1, 4),
    _AwnStatisticsLsWanTsTs_Type()
)
awnStatisticsLsWanTsTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsTs.setStatus("mandatory")


class _AwnStatisticsLsWanTsData_Type(OctetString):
    """Custom type awnStatisticsLsWanTsData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(456, 456),
    )


_AwnStatisticsLsWanTsData_Type.__name__ = "OctetString"
_AwnStatisticsLsWanTsData_Object = MibTableColumn
awnStatisticsLsWanTsData = _AwnStatisticsLsWanTsData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 7, 1, 1, 5),
    _AwnStatisticsLsWanTsData_Type()
)
awnStatisticsLsWanTsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsData.setStatus("mandatory")
_AwnStatisticsComNniPortRt_ObjectIdentity = ObjectIdentity
awnStatisticsComNniPortRt = _AwnStatisticsComNniPortRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8)
)
_AwnStatisticsComNniPortRtTable_Object = MibTable
awnStatisticsComNniPortRtTable = _AwnStatisticsComNniPortRtTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtTable.setStatus("mandatory")
_AwnStatisticsComNniPortRtEntry_Object = MibTableRow
awnStatisticsComNniPortRtEntry = _AwnStatisticsComNniPortRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1)
)
awnStatisticsComNniPortRtEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortRtSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortRtAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortRtPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortRtCategory"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniPortRtType"),
)
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtEntry.setStatus("mandatory")


class _AwnStatisticsComNniPortRtSlot_Type(Integer32):
    """Custom type awnStatisticsComNniPortRtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniPortRtSlot_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortRtSlot_Object = MibTableColumn
awnStatisticsComNniPortRtSlot = _AwnStatisticsComNniPortRtSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 1),
    _AwnStatisticsComNniPortRtSlot_Type()
)
awnStatisticsComNniPortRtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtSlot.setStatus("mandatory")


class _AwnStatisticsComNniPortRtAdapter_Type(Integer32):
    """Custom type awnStatisticsComNniPortRtAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComNniPortRtAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortRtAdapter_Object = MibTableColumn
awnStatisticsComNniPortRtAdapter = _AwnStatisticsComNniPortRtAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 2),
    _AwnStatisticsComNniPortRtAdapter_Type()
)
awnStatisticsComNniPortRtAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtAdapter.setStatus("mandatory")


class _AwnStatisticsComNniPortRtPort_Type(Integer32):
    """Custom type awnStatisticsComNniPortRtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniPortRtPort_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortRtPort_Object = MibTableColumn
awnStatisticsComNniPortRtPort = _AwnStatisticsComNniPortRtPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 3),
    _AwnStatisticsComNniPortRtPort_Type()
)
awnStatisticsComNniPortRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtPort.setStatus("mandatory")


class _AwnStatisticsComNniPortRtCategory_Type(Integer32):
    """Custom type awnStatisticsComNniPortRtCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AwnStatisticsComNniPortRtCategory_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortRtCategory_Object = MibTableColumn
awnStatisticsComNniPortRtCategory = _AwnStatisticsComNniPortRtCategory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 4),
    _AwnStatisticsComNniPortRtCategory_Type()
)
awnStatisticsComNniPortRtCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtCategory.setStatus("mandatory")


class _AwnStatisticsComNniPortRtType_Type(Integer32):
    """Custom type awnStatisticsComNniPortRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsComNniPortRtType_Type.__name__ = "Integer32"
_AwnStatisticsComNniPortRtType_Object = MibTableColumn
awnStatisticsComNniPortRtType = _AwnStatisticsComNniPortRtType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 5),
    _AwnStatisticsComNniPortRtType_Type()
)
awnStatisticsComNniPortRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtType.setStatus("mandatory")


class _AwnStatisticsComNniPortRtData_Type(Gauge32):
    """Custom type awnStatisticsComNniPortRtData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AwnStatisticsComNniPortRtData_Type.__name__ = "Gauge32"
_AwnStatisticsComNniPortRtData_Object = MibTableColumn
awnStatisticsComNniPortRtData = _AwnStatisticsComNniPortRtData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 8, 1, 1, 6),
    _AwnStatisticsComNniPortRtData_Type()
)
awnStatisticsComNniPortRtData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniPortRtData.setStatus("mandatory")
_AwnStatisticsComNniVpRt_ObjectIdentity = ObjectIdentity
awnStatisticsComNniVpRt = _AwnStatisticsComNniVpRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9)
)
_AwnStatisticsComNniVpRtTable_Object = MibTable
awnStatisticsComNniVpRtTable = _AwnStatisticsComNniVpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtTable.setStatus("mandatory")
_AwnStatisticsComNniVpRtEntry_Object = MibTableRow
awnStatisticsComNniVpRtEntry = _AwnStatisticsComNniVpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1)
)
awnStatisticsComNniVpRtEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtCategory"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComNniVpRtType"),
)
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtEntry.setStatus("mandatory")


class _AwnStatisticsComNniVpRtSlot_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniVpRtSlot_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtSlot_Object = MibScalar
awnStatisticsComNniVpRtSlot = _AwnStatisticsComNniVpRtSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 1),
    _AwnStatisticsComNniVpRtSlot_Type()
)
awnStatisticsComNniVpRtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtSlot.setStatus("mandatory")


class _AwnStatisticsComNniVpRtAdapter_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComNniVpRtAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtAdapter_Object = MibTableColumn
awnStatisticsComNniVpRtAdapter = _AwnStatisticsComNniVpRtAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 2),
    _AwnStatisticsComNniVpRtAdapter_Type()
)
awnStatisticsComNniVpRtAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtAdapter.setStatus("mandatory")


class _AwnStatisticsComNniVpRtPort_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComNniVpRtPort_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtPort_Object = MibTableColumn
awnStatisticsComNniVpRtPort = _AwnStatisticsComNniVpRtPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 3),
    _AwnStatisticsComNniVpRtPort_Type()
)
awnStatisticsComNniVpRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtPort.setStatus("mandatory")


class _AwnStatisticsComNniVpRtVpi_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnStatisticsComNniVpRtVpi_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtVpi_Object = MibTableColumn
awnStatisticsComNniVpRtVpi = _AwnStatisticsComNniVpRtVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 4),
    _AwnStatisticsComNniVpRtVpi_Type()
)
awnStatisticsComNniVpRtVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtVpi.setStatus("mandatory")


class _AwnStatisticsComNniVpRtCategory_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AwnStatisticsComNniVpRtCategory_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtCategory_Object = MibTableColumn
awnStatisticsComNniVpRtCategory = _AwnStatisticsComNniVpRtCategory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 5),
    _AwnStatisticsComNniVpRtCategory_Type()
)
awnStatisticsComNniVpRtCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtCategory.setStatus("mandatory")


class _AwnStatisticsComNniVpRtType_Type(Integer32):
    """Custom type awnStatisticsComNniVpRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsComNniVpRtType_Type.__name__ = "Integer32"
_AwnStatisticsComNniVpRtType_Object = MibTableColumn
awnStatisticsComNniVpRtType = _AwnStatisticsComNniVpRtType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 6),
    _AwnStatisticsComNniVpRtType_Type()
)
awnStatisticsComNniVpRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtType.setStatus("mandatory")


class _AwnStatisticsComNniVpRtData_Type(Gauge32):
    """Custom type awnStatisticsComNniVpRtData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AwnStatisticsComNniVpRtData_Type.__name__ = "Gauge32"
_AwnStatisticsComNniVpRtData_Object = MibTableColumn
awnStatisticsComNniVpRtData = _AwnStatisticsComNniVpRtData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 9, 1, 1, 7),
    _AwnStatisticsComNniVpRtData_Type()
)
awnStatisticsComNniVpRtData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComNniVpRtData.setStatus("mandatory")
_AwnStatisticsLsWanTsRt_ObjectIdentity = ObjectIdentity
awnStatisticsLsWanTsRt = _AwnStatisticsLsWanTsRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10)
)
_AwnStatisticsLsWanTsRtTable_Object = MibTable
awnStatisticsLsWanTsRtTable = _AwnStatisticsLsWanTsRtTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtTable.setStatus("mandatory")
_AwnStatisticsLsWanTsRtEntry_Object = MibTableRow
awnStatisticsLsWanTsRtEntry = _AwnStatisticsLsWanTsRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1)
)
awnStatisticsLsWanTsRtEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtTs"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtCategory"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanTsRtType"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtEntry.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtUnit_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanTsRtUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtUnit_Object = MibTableColumn
awnStatisticsLsWanTsRtUnit = _AwnStatisticsLsWanTsRtUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 1),
    _AwnStatisticsLsWanTsRtUnit_Type()
)
awnStatisticsLsWanTsRtUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtUnit.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtCard_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsWanTsRtCard_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtCard_Object = MibTableColumn
awnStatisticsLsWanTsRtCard = _AwnStatisticsLsWanTsRtCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 2),
    _AwnStatisticsLsWanTsRtCard_Type()
)
awnStatisticsLsWanTsRtCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtCard.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtPort_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanTsRtPort_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtPort_Object = MibTableColumn
awnStatisticsLsWanTsRtPort = _AwnStatisticsLsWanTsRtPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 3),
    _AwnStatisticsLsWanTsRtPort_Type()
)
awnStatisticsLsWanTsRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtPort.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtTs_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsLsWanTsRtTs_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtTs_Object = MibTableColumn
awnStatisticsLsWanTsRtTs = _AwnStatisticsLsWanTsRtTs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 4),
    _AwnStatisticsLsWanTsRtTs_Type()
)
awnStatisticsLsWanTsRtTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtTs.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtCategory_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AwnStatisticsLsWanTsRtCategory_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtCategory_Object = MibTableColumn
awnStatisticsLsWanTsRtCategory = _AwnStatisticsLsWanTsRtCategory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 5),
    _AwnStatisticsLsWanTsRtCategory_Type()
)
awnStatisticsLsWanTsRtCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtCategory.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtType_Type(Integer32):
    """Custom type awnStatisticsLsWanTsRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsLsWanTsRtType_Type.__name__ = "Integer32"
_AwnStatisticsLsWanTsRtType_Object = MibTableColumn
awnStatisticsLsWanTsRtType = _AwnStatisticsLsWanTsRtType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 6),
    _AwnStatisticsLsWanTsRtType_Type()
)
awnStatisticsLsWanTsRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtType.setStatus("mandatory")


class _AwnStatisticsLsWanTsRtData_Type(Gauge32):
    """Custom type awnStatisticsLsWanTsRtData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AwnStatisticsLsWanTsRtData_Type.__name__ = "Gauge32"
_AwnStatisticsLsWanTsRtData_Object = MibTableColumn
awnStatisticsLsWanTsRtData = _AwnStatisticsLsWanTsRtData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 10, 1, 1, 7),
    _AwnStatisticsLsWanTsRtData_Type()
)
awnStatisticsLsWanTsRtData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanTsRtData.setStatus("mandatory")
_AwnStatisticsVccAtmLine_ObjectIdentity = ObjectIdentity
awnStatisticsVccAtmLine = _AwnStatisticsVccAtmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11)
)
_AwnStatisticsVccAtmLineTable_Object = MibTable
awnStatisticsVccAtmLineTable = _AwnStatisticsVccAtmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineTable.setStatus("mandatory")
_AwnStatisticsVccAtmLineEntry_Object = MibTableRow
awnStatisticsVccAtmLineEntry = _AwnStatisticsVccAtmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1)
)
awnStatisticsVccAtmLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLineSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLineAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLinePort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLineVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLineVci"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccAtmLineType"),
)
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineEntry.setStatus("mandatory")


class _AwnStatisticsVccAtmLineSlot_Type(Integer32):
    """Custom type awnStatisticsVccAtmLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsVccAtmLineSlot_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLineSlot_Object = MibTableColumn
awnStatisticsVccAtmLineSlot = _AwnStatisticsVccAtmLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 1),
    _AwnStatisticsVccAtmLineSlot_Type()
)
awnStatisticsVccAtmLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineSlot.setStatus("mandatory")


class _AwnStatisticsVccAtmLineAdapter_Type(Integer32):
    """Custom type awnStatisticsVccAtmLineAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsVccAtmLineAdapter_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLineAdapter_Object = MibTableColumn
awnStatisticsVccAtmLineAdapter = _AwnStatisticsVccAtmLineAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 2),
    _AwnStatisticsVccAtmLineAdapter_Type()
)
awnStatisticsVccAtmLineAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineAdapter.setStatus("mandatory")


class _AwnStatisticsVccAtmLinePort_Type(Integer32):
    """Custom type awnStatisticsVccAtmLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsVccAtmLinePort_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLinePort_Object = MibTableColumn
awnStatisticsVccAtmLinePort = _AwnStatisticsVccAtmLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 3),
    _AwnStatisticsVccAtmLinePort_Type()
)
awnStatisticsVccAtmLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLinePort.setStatus("mandatory")


class _AwnStatisticsVccAtmLineVpi_Type(Integer32):
    """Custom type awnStatisticsVccAtmLineVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnStatisticsVccAtmLineVpi_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLineVpi_Object = MibTableColumn
awnStatisticsVccAtmLineVpi = _AwnStatisticsVccAtmLineVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 4),
    _AwnStatisticsVccAtmLineVpi_Type()
)
awnStatisticsVccAtmLineVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineVpi.setStatus("mandatory")


class _AwnStatisticsVccAtmLineVci_Type(Integer32):
    """Custom type awnStatisticsVccAtmLineVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 4095),
    )


_AwnStatisticsVccAtmLineVci_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLineVci_Object = MibTableColumn
awnStatisticsVccAtmLineVci = _AwnStatisticsVccAtmLineVci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 5),
    _AwnStatisticsVccAtmLineVci_Type()
)
awnStatisticsVccAtmLineVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineVci.setStatus("mandatory")


class _AwnStatisticsVccAtmLineType_Type(Integer32):
    """Custom type awnStatisticsVccAtmLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsVccAtmLineType_Type.__name__ = "Integer32"
_AwnStatisticsVccAtmLineType_Object = MibTableColumn
awnStatisticsVccAtmLineType = _AwnStatisticsVccAtmLineType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 6),
    _AwnStatisticsVccAtmLineType_Type()
)
awnStatisticsVccAtmLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineType.setStatus("mandatory")


class _AwnStatisticsVccAtmLineData_Type(Gauge32):
    """Custom type awnStatisticsVccAtmLineData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AwnStatisticsVccAtmLineData_Type.__name__ = "Gauge32"
_AwnStatisticsVccAtmLineData_Object = MibTableColumn
awnStatisticsVccAtmLineData = _AwnStatisticsVccAtmLineData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 11, 1, 1, 7),
    _AwnStatisticsVccAtmLineData_Type()
)
awnStatisticsVccAtmLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccAtmLineData.setStatus("mandatory")
_AwnStatisticsVpcAtmLine_ObjectIdentity = ObjectIdentity
awnStatisticsVpcAtmLine = _AwnStatisticsVpcAtmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12)
)
_AwnStatisticsVpcAtmLineTable_Object = MibTable
awnStatisticsVpcAtmLineTable = _AwnStatisticsVpcAtmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineTable.setStatus("mandatory")
_AwnStatisticsVpcAtmLineEntry_Object = MibTableRow
awnStatisticsVpcAtmLineEntry = _AwnStatisticsVpcAtmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1)
)
awnStatisticsVpcAtmLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVpcAtmLineSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVpcAtmLineAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVpcAtmLinePort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVpcAtmLineVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVpcAtmLineType"),
)
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineEntry.setStatus("mandatory")


class _AwnStatisticsVpcAtmLineSlot_Type(Integer32):
    """Custom type awnStatisticsVpcAtmLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsVpcAtmLineSlot_Type.__name__ = "Integer32"
_AwnStatisticsVpcAtmLineSlot_Object = MibTableColumn
awnStatisticsVpcAtmLineSlot = _AwnStatisticsVpcAtmLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 1),
    _AwnStatisticsVpcAtmLineSlot_Type()
)
awnStatisticsVpcAtmLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineSlot.setStatus("mandatory")


class _AwnStatisticsVpcAtmLineAdapter_Type(Integer32):
    """Custom type awnStatisticsVpcAtmLineAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsVpcAtmLineAdapter_Type.__name__ = "Integer32"
_AwnStatisticsVpcAtmLineAdapter_Object = MibTableColumn
awnStatisticsVpcAtmLineAdapter = _AwnStatisticsVpcAtmLineAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 2),
    _AwnStatisticsVpcAtmLineAdapter_Type()
)
awnStatisticsVpcAtmLineAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineAdapter.setStatus("mandatory")


class _AwnStatisticsVpcAtmLinePort_Type(Integer32):
    """Custom type awnStatisticsVpcAtmLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsVpcAtmLinePort_Type.__name__ = "Integer32"
_AwnStatisticsVpcAtmLinePort_Object = MibTableColumn
awnStatisticsVpcAtmLinePort = _AwnStatisticsVpcAtmLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 3),
    _AwnStatisticsVpcAtmLinePort_Type()
)
awnStatisticsVpcAtmLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLinePort.setStatus("mandatory")


class _AwnStatisticsVpcAtmLineVpi_Type(Integer32):
    """Custom type awnStatisticsVpcAtmLineVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnStatisticsVpcAtmLineVpi_Type.__name__ = "Integer32"
_AwnStatisticsVpcAtmLineVpi_Object = MibTableColumn
awnStatisticsVpcAtmLineVpi = _AwnStatisticsVpcAtmLineVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 4),
    _AwnStatisticsVpcAtmLineVpi_Type()
)
awnStatisticsVpcAtmLineVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineVpi.setStatus("mandatory")


class _AwnStatisticsVpcAtmLineType_Type(Integer32):
    """Custom type awnStatisticsVpcAtmLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsVpcAtmLineType_Type.__name__ = "Integer32"
_AwnStatisticsVpcAtmLineType_Object = MibTableColumn
awnStatisticsVpcAtmLineType = _AwnStatisticsVpcAtmLineType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 5),
    _AwnStatisticsVpcAtmLineType_Type()
)
awnStatisticsVpcAtmLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineType.setStatus("mandatory")


class _AwnStatisticsVpcAtmLineData_Type(Gauge32):
    """Custom type awnStatisticsVpcAtmLineData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AwnStatisticsVpcAtmLineData_Type.__name__ = "Gauge32"
_AwnStatisticsVpcAtmLineData_Object = MibTableColumn
awnStatisticsVpcAtmLineData = _AwnStatisticsVpcAtmLineData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 12, 1, 1, 6),
    _AwnStatisticsVpcAtmLineData_Type()
)
awnStatisticsVpcAtmLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVpcAtmLineData.setStatus("mandatory")
_AwnStatisticsVccWanTs_ObjectIdentity = ObjectIdentity
awnStatisticsVccWanTs = _AwnStatisticsVccWanTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13)
)
_AwnStatisticsVccWanTsTable_Object = MibTable
awnStatisticsVccWanTsTable = _AwnStatisticsVccWanTsTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsTable.setStatus("mandatory")
_AwnStatisticsVccWanTsEntry_Object = MibTableRow
awnStatisticsVccWanTsEntry = _AwnStatisticsVccWanTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1)
)
awnStatisticsVccWanTsEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsTs"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsVci"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccWanTsType"),
)
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsEntry.setStatus("mandatory")


class _AwnStatisticsVccWanTsUnit_Type(Integer32):
    """Custom type awnStatisticsVccWanTsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccWanTsUnit_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsUnit_Object = MibTableColumn
awnStatisticsVccWanTsUnit = _AwnStatisticsVccWanTsUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 1),
    _AwnStatisticsVccWanTsUnit_Type()
)
awnStatisticsVccWanTsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsUnit.setStatus("mandatory")


class _AwnStatisticsVccWanTsCard_Type(Integer32):
    """Custom type awnStatisticsVccWanTsCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsVccWanTsCard_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsCard_Object = MibTableColumn
awnStatisticsVccWanTsCard = _AwnStatisticsVccWanTsCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 2),
    _AwnStatisticsVccWanTsCard_Type()
)
awnStatisticsVccWanTsCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsCard.setStatus("mandatory")


class _AwnStatisticsVccWanTsPort_Type(Integer32):
    """Custom type awnStatisticsVccWanTsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccWanTsPort_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsPort_Object = MibTableColumn
awnStatisticsVccWanTsPort = _AwnStatisticsVccWanTsPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 3),
    _AwnStatisticsVccWanTsPort_Type()
)
awnStatisticsVccWanTsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsPort.setStatus("mandatory")


class _AwnStatisticsVccWanTsTs_Type(Integer32):
    """Custom type awnStatisticsVccWanTsTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsVccWanTsTs_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsTs_Object = MibTableColumn
awnStatisticsVccWanTsTs = _AwnStatisticsVccWanTsTs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 4),
    _AwnStatisticsVccWanTsTs_Type()
)
awnStatisticsVccWanTsTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsTs.setStatus("mandatory")


class _AwnStatisticsVccWanTsVpi_Type(Integer32):
    """Custom type awnStatisticsVccWanTsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnStatisticsVccWanTsVpi_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsVpi_Object = MibTableColumn
awnStatisticsVccWanTsVpi = _AwnStatisticsVccWanTsVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 5),
    _AwnStatisticsVccWanTsVpi_Type()
)
awnStatisticsVccWanTsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsVpi.setStatus("mandatory")


class _AwnStatisticsVccWanTsVci_Type(Integer32):
    """Custom type awnStatisticsVccWanTsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AwnStatisticsVccWanTsVci_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsVci_Object = MibTableColumn
awnStatisticsVccWanTsVci = _AwnStatisticsVccWanTsVci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 6),
    _AwnStatisticsVccWanTsVci_Type()
)
awnStatisticsVccWanTsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsVci.setStatus("mandatory")


class _AwnStatisticsVccWanTsType_Type(Integer32):
    """Custom type awnStatisticsVccWanTsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsVccWanTsType_Type.__name__ = "Integer32"
_AwnStatisticsVccWanTsType_Object = MibTableColumn
awnStatisticsVccWanTsType = _AwnStatisticsVccWanTsType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 7),
    _AwnStatisticsVccWanTsType_Type()
)
awnStatisticsVccWanTsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsType.setStatus("mandatory")


class _AwnStatisticsVccWanTsData_Type(Gauge32):
    """Custom type awnStatisticsVccWanTsData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AwnStatisticsVccWanTsData_Type.__name__ = "Gauge32"
_AwnStatisticsVccWanTsData_Object = MibTableColumn
awnStatisticsVccWanTsData = _AwnStatisticsVccWanTsData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 13, 1, 1, 8),
    _AwnStatisticsVccWanTsData_Type()
)
awnStatisticsVccWanTsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccWanTsData.setStatus("mandatory")
_AwnStatisticsVccFrLine_ObjectIdentity = ObjectIdentity
awnStatisticsVccFrLine = _AwnStatisticsVccFrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14)
)
_AwnStatisticsVccFrLineTable_Object = MibTable
awnStatisticsVccFrLineTable = _AwnStatisticsVccFrLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineTable.setStatus("mandatory")
_AwnStatisticsVccFrLineEntry_Object = MibTableRow
awnStatisticsVccFrLineEntry = _AwnStatisticsVccFrLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1)
)
awnStatisticsVccFrLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLineUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLineCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLinePort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLineTimeslot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLineDlci"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFrLineType"),
)
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineEntry.setStatus("mandatory")


class _AwnStatisticsVccFrLineUnit_Type(Integer32):
    """Custom type awnStatisticsVccFrLineUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccFrLineUnit_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLineUnit_Object = MibTableColumn
awnStatisticsVccFrLineUnit = _AwnStatisticsVccFrLineUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 1),
    _AwnStatisticsVccFrLineUnit_Type()
)
awnStatisticsVccFrLineUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineUnit.setStatus("mandatory")


class _AwnStatisticsVccFrLineCard_Type(Integer32):
    """Custom type awnStatisticsVccFrLineCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsVccFrLineCard_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLineCard_Object = MibTableColumn
awnStatisticsVccFrLineCard = _AwnStatisticsVccFrLineCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 2),
    _AwnStatisticsVccFrLineCard_Type()
)
awnStatisticsVccFrLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineCard.setStatus("mandatory")


class _AwnStatisticsVccFrLinePort_Type(Integer32):
    """Custom type awnStatisticsVccFrLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccFrLinePort_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLinePort_Object = MibTableColumn
awnStatisticsVccFrLinePort = _AwnStatisticsVccFrLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 3),
    _AwnStatisticsVccFrLinePort_Type()
)
awnStatisticsVccFrLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLinePort.setStatus("mandatory")


class _AwnStatisticsVccFrLineTimeslot_Type(Integer32):
    """Custom type awnStatisticsVccFrLineTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsVccFrLineTimeslot_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLineTimeslot_Object = MibTableColumn
awnStatisticsVccFrLineTimeslot = _AwnStatisticsVccFrLineTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 4),
    _AwnStatisticsVccFrLineTimeslot_Type()
)
awnStatisticsVccFrLineTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineTimeslot.setStatus("mandatory")


class _AwnStatisticsVccFrLineDlci_Type(Integer32):
    """Custom type awnStatisticsVccFrLineDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AwnStatisticsVccFrLineDlci_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLineDlci_Object = MibTableColumn
awnStatisticsVccFrLineDlci = _AwnStatisticsVccFrLineDlci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 5),
    _AwnStatisticsVccFrLineDlci_Type()
)
awnStatisticsVccFrLineDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineDlci.setStatus("mandatory")


class _AwnStatisticsVccFrLineType_Type(Integer32):
    """Custom type awnStatisticsVccFrLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsVccFrLineType_Type.__name__ = "Integer32"
_AwnStatisticsVccFrLineType_Object = MibTableColumn
awnStatisticsVccFrLineType = _AwnStatisticsVccFrLineType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 6),
    _AwnStatisticsVccFrLineType_Type()
)
awnStatisticsVccFrLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineType.setStatus("mandatory")


class _AwnStatisticsVccFrLineData_Type(Gauge32):
    """Custom type awnStatisticsVccFrLineData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AwnStatisticsVccFrLineData_Type.__name__ = "Gauge32"
_AwnStatisticsVccFrLineData_Object = MibTableColumn
awnStatisticsVccFrLineData = _AwnStatisticsVccFrLineData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 14, 1, 1, 7),
    _AwnStatisticsVccFrLineData_Type()
)
awnStatisticsVccFrLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFrLineData.setStatus("mandatory")
_AwnStatisticsVccFfLine_ObjectIdentity = ObjectIdentity
awnStatisticsVccFfLine = _AwnStatisticsVccFfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15)
)
_AwnStatisticsVccFfLineTable_Object = MibTable
awnStatisticsVccFfLineTable = _AwnStatisticsVccFfLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineTable.setStatus("mandatory")
_AwnStatisticsVccFfLineEntry_Object = MibTableRow
awnStatisticsVccFfLineEntry = _AwnStatisticsVccFfLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1)
)
awnStatisticsVccFfLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFfLineUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFfLineCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFfLinePort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFfLineTimeslot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsVccFfLineType"),
)
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineEntry.setStatus("mandatory")


class _AwnStatisticsVccFfLineUnit_Type(Integer32):
    """Custom type awnStatisticsVccFfLineUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccFfLineUnit_Type.__name__ = "Integer32"
_AwnStatisticsVccFfLineUnit_Object = MibTableColumn
awnStatisticsVccFfLineUnit = _AwnStatisticsVccFfLineUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 1),
    _AwnStatisticsVccFfLineUnit_Type()
)
awnStatisticsVccFfLineUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineUnit.setStatus("mandatory")


class _AwnStatisticsVccFfLineCard_Type(Integer32):
    """Custom type awnStatisticsVccFfLineCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsVccFfLineCard_Type.__name__ = "Integer32"
_AwnStatisticsVccFfLineCard_Object = MibTableColumn
awnStatisticsVccFfLineCard = _AwnStatisticsVccFfLineCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 2),
    _AwnStatisticsVccFfLineCard_Type()
)
awnStatisticsVccFfLineCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineCard.setStatus("mandatory")


class _AwnStatisticsVccFfLinePort_Type(Integer32):
    """Custom type awnStatisticsVccFfLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsVccFfLinePort_Type.__name__ = "Integer32"
_AwnStatisticsVccFfLinePort_Object = MibTableColumn
awnStatisticsVccFfLinePort = _AwnStatisticsVccFfLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 3),
    _AwnStatisticsVccFfLinePort_Type()
)
awnStatisticsVccFfLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLinePort.setStatus("mandatory")


class _AwnStatisticsVccFfLineTimeslot_Type(Integer32):
    """Custom type awnStatisticsVccFfLineTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsVccFfLineTimeslot_Type.__name__ = "Integer32"
_AwnStatisticsVccFfLineTimeslot_Object = MibTableColumn
awnStatisticsVccFfLineTimeslot = _AwnStatisticsVccFfLineTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 4),
    _AwnStatisticsVccFfLineTimeslot_Type()
)
awnStatisticsVccFfLineTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineTimeslot.setStatus("mandatory")


class _AwnStatisticsVccFfLineType_Type(Integer32):
    """Custom type awnStatisticsVccFfLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsVccFfLineType_Type.__name__ = "Integer32"
_AwnStatisticsVccFfLineType_Object = MibTableColumn
awnStatisticsVccFfLineType = _AwnStatisticsVccFfLineType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 5),
    _AwnStatisticsVccFfLineType_Type()
)
awnStatisticsVccFfLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineType.setStatus("mandatory")


class _AwnStatisticsVccFfLineData_Type(Gauge32):
    """Custom type awnStatisticsVccFfLineData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AwnStatisticsVccFfLineData_Type.__name__ = "Gauge32"
_AwnStatisticsVccFfLineData_Object = MibTableColumn
awnStatisticsVccFfLineData = _AwnStatisticsVccFfLineData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 15, 1, 1, 6),
    _AwnStatisticsVccFfLineData_Type()
)
awnStatisticsVccFfLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsVccFfLineData.setStatus("mandatory")
_AwnStatisticsLsWanVp_ObjectIdentity = ObjectIdentity
awnStatisticsLsWanVp = _AwnStatisticsLsWanVp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16)
)
_AwnStatisticsLsWanVpTable_Object = MibTable
awnStatisticsLsWanVpTable = _AwnStatisticsLsWanVpTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpTable.setStatus("mandatory")
_AwnStatisticsLsWanVpEntry_Object = MibTableRow
awnStatisticsLsWanVpEntry = _AwnStatisticsLsWanVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1)
)
awnStatisticsLsWanVpEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpVpi"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpEntry.setStatus("mandatory")


class _AwnStatisticsLsWanVpUnit_Type(Integer32):
    """Custom type awnStatisticsLsWanVpUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanVpUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpUnit_Object = MibTableColumn
awnStatisticsLsWanVpUnit = _AwnStatisticsLsWanVpUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1, 1),
    _AwnStatisticsLsWanVpUnit_Type()
)
awnStatisticsLsWanVpUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpUnit.setStatus("mandatory")


class _AwnStatisticsLsWanVpCard_Type(Integer32):
    """Custom type awnStatisticsLsWanVpCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsWanVpCard_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpCard_Object = MibTableColumn
awnStatisticsLsWanVpCard = _AwnStatisticsLsWanVpCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1, 2),
    _AwnStatisticsLsWanVpCard_Type()
)
awnStatisticsLsWanVpCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpCard.setStatus("mandatory")


class _AwnStatisticsLsWanVpPort_Type(Integer32):
    """Custom type awnStatisticsLsWanVpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanVpPort_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpPort_Object = MibTableColumn
awnStatisticsLsWanVpPort = _AwnStatisticsLsWanVpPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1, 3),
    _AwnStatisticsLsWanVpPort_Type()
)
awnStatisticsLsWanVpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpPort.setStatus("mandatory")


class _AwnStatisticsLsWanVpVpi_Type(Integer32):
    """Custom type awnStatisticsLsWanVpVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_AwnStatisticsLsWanVpVpi_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpVpi_Object = MibTableColumn
awnStatisticsLsWanVpVpi = _AwnStatisticsLsWanVpVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1, 4),
    _AwnStatisticsLsWanVpVpi_Type()
)
awnStatisticsLsWanVpVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpVpi.setStatus("mandatory")


class _AwnStatisticsLsWanVpData_Type(OctetString):
    """Custom type awnStatisticsLsWanVpData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(456, 456),
    )


_AwnStatisticsLsWanVpData_Type.__name__ = "OctetString"
_AwnStatisticsLsWanVpData_Object = MibTableColumn
awnStatisticsLsWanVpData = _AwnStatisticsLsWanVpData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 16, 1, 1, 5),
    _AwnStatisticsLsWanVpData_Type()
)
awnStatisticsLsWanVpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpData.setStatus("mandatory")
_AwnStatisticsLsWanVpRt_ObjectIdentity = ObjectIdentity
awnStatisticsLsWanVpRt = _AwnStatisticsLsWanVpRt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17)
)
_AwnStatisticsLsWanVpRtTable_Object = MibTable
awnStatisticsLsWanVpRtTable = _AwnStatisticsLsWanVpRtTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtTable.setStatus("mandatory")
_AwnStatisticsLsWanVpRtEntry_Object = MibTableRow
awnStatisticsLsWanVpRtEntry = _AwnStatisticsLsWanVpRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1)
)
awnStatisticsLsWanVpRtEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtVpi"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtCategory"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsWanVpRtType"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtEntry.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtUnit_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsWanVpRtUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtUnit_Object = MibTableColumn
awnStatisticsLsWanVpRtUnit = _AwnStatisticsLsWanVpRtUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 1),
    _AwnStatisticsLsWanVpRtUnit_Type()
)
awnStatisticsLsWanVpRtUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtUnit.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtCard_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsWanVpRtCard_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtCard_Object = MibTableColumn
awnStatisticsLsWanVpRtCard = _AwnStatisticsLsWanVpRtCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 2),
    _AwnStatisticsLsWanVpRtCard_Type()
)
awnStatisticsLsWanVpRtCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtCard.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtPort_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AwnStatisticsLsWanVpRtPort_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtPort_Object = MibTableColumn
awnStatisticsLsWanVpRtPort = _AwnStatisticsLsWanVpRtPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 3),
    _AwnStatisticsLsWanVpRtPort_Type()
)
awnStatisticsLsWanVpRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtPort.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtVpi_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_AwnStatisticsLsWanVpRtVpi_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtVpi_Object = MibTableColumn
awnStatisticsLsWanVpRtVpi = _AwnStatisticsLsWanVpRtVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 4),
    _AwnStatisticsLsWanVpRtVpi_Type()
)
awnStatisticsLsWanVpRtVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtVpi.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtCategory_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_AwnStatisticsLsWanVpRtCategory_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtCategory_Object = MibTableColumn
awnStatisticsLsWanVpRtCategory = _AwnStatisticsLsWanVpRtCategory_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 5),
    _AwnStatisticsLsWanVpRtCategory_Type()
)
awnStatisticsLsWanVpRtCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtCategory.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtType_Type(Integer32):
    """Custom type awnStatisticsLsWanVpRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AwnStatisticsLsWanVpRtType_Type.__name__ = "Integer32"
_AwnStatisticsLsWanVpRtType_Object = MibTableColumn
awnStatisticsLsWanVpRtType = _AwnStatisticsLsWanVpRtType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 6),
    _AwnStatisticsLsWanVpRtType_Type()
)
awnStatisticsLsWanVpRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtType.setStatus("mandatory")


class _AwnStatisticsLsWanVpRtData_Type(Gauge32):
    """Custom type awnStatisticsLsWanVpRtData based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AwnStatisticsLsWanVpRtData_Type.__name__ = "Gauge32"
_AwnStatisticsLsWanVpRtData_Object = MibTableColumn
awnStatisticsLsWanVpRtData = _AwnStatisticsLsWanVpRtData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 17, 1, 1, 7),
    _AwnStatisticsLsWanVpRtData_Type()
)
awnStatisticsLsWanVpRtData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsWanVpRtData.setStatus("mandatory")
_AwnStatisticsComAtmLine_ObjectIdentity = ObjectIdentity
awnStatisticsComAtmLine = _AwnStatisticsComAtmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18)
)
_AwnStatisticsComAtmLineTable_Object = MibTable
awnStatisticsComAtmLineTable = _AwnStatisticsComAtmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineTable.setStatus("mandatory")
_AwnStatisticsComAtmLineEntry_Object = MibTableRow
awnStatisticsComAtmLineEntry = _AwnStatisticsComAtmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1)
)
awnStatisticsComAtmLineEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComAtmLineSlot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComAtmLineAdapter"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComAtmLinePort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsComAtmLineVpi"),
)
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineEntry.setStatus("mandatory")


class _AwnStatisticsComAtmLineSlot_Type(Integer32):
    """Custom type awnStatisticsComAtmLineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComAtmLineSlot_Type.__name__ = "Integer32"
_AwnStatisticsComAtmLineSlot_Object = MibTableColumn
awnStatisticsComAtmLineSlot = _AwnStatisticsComAtmLineSlot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1, 1),
    _AwnStatisticsComAtmLineSlot_Type()
)
awnStatisticsComAtmLineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineSlot.setStatus("mandatory")


class _AwnStatisticsComAtmLineAdapter_Type(Integer32):
    """Custom type awnStatisticsComAtmLineAdapter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AwnStatisticsComAtmLineAdapter_Type.__name__ = "Integer32"
_AwnStatisticsComAtmLineAdapter_Object = MibTableColumn
awnStatisticsComAtmLineAdapter = _AwnStatisticsComAtmLineAdapter_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1, 2),
    _AwnStatisticsComAtmLineAdapter_Type()
)
awnStatisticsComAtmLineAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineAdapter.setStatus("mandatory")


class _AwnStatisticsComAtmLinePort_Type(Integer32):
    """Custom type awnStatisticsComAtmLinePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AwnStatisticsComAtmLinePort_Type.__name__ = "Integer32"
_AwnStatisticsComAtmLinePort_Object = MibTableColumn
awnStatisticsComAtmLinePort = _AwnStatisticsComAtmLinePort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1, 3),
    _AwnStatisticsComAtmLinePort_Type()
)
awnStatisticsComAtmLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComAtmLinePort.setStatus("mandatory")


class _AwnStatisticsComAtmLineVpi_Type(Integer32):
    """Custom type awnStatisticsComAtmLineVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AwnStatisticsComAtmLineVpi_Type.__name__ = "Integer32"
_AwnStatisticsComAtmLineVpi_Object = MibTableColumn
awnStatisticsComAtmLineVpi = _AwnStatisticsComAtmLineVpi_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1, 4),
    _AwnStatisticsComAtmLineVpi_Type()
)
awnStatisticsComAtmLineVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineVpi.setStatus("mandatory")


class _AwnStatisticsComAtmLineData_Type(OctetString):
    """Custom type awnStatisticsComAtmLineData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(104, 104),
    )


_AwnStatisticsComAtmLineData_Type.__name__ = "OctetString"
_AwnStatisticsComAtmLineData_Object = MibScalar
awnStatisticsComAtmLineData = _AwnStatisticsComAtmLineData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 18, 1, 1, 5),
    _AwnStatisticsComAtmLineData_Type()
)
awnStatisticsComAtmLineData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsComAtmLineData.setStatus("mandatory")
_AwnStatisticsLsTs_ObjectIdentity = ObjectIdentity
awnStatisticsLsTs = _AwnStatisticsLsTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19)
)
_AwnStatisticsLsTsTable_Object = MibTable
awnStatisticsLsTsTable = _AwnStatisticsLsTsTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsLsTsTable.setStatus("mandatory")
_AwnStatisticsLsTsEntry_Object = MibTableRow
awnStatisticsLsTsEntry = _AwnStatisticsLsTsEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1)
)
awnStatisticsLsTsEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsTsUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsTsCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsTsPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsLsTsTs"),
)
if mibBuilder.loadTexts:
    awnStatisticsLsTsEntry.setStatus("mandatory")


class _AwnStatisticsLsTsUnit_Type(Integer32):
    """Custom type awnStatisticsLsTsUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsTsUnit_Type.__name__ = "Integer32"
_AwnStatisticsLsTsUnit_Object = MibTableColumn
awnStatisticsLsTsUnit = _AwnStatisticsLsTsUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1, 1),
    _AwnStatisticsLsTsUnit_Type()
)
awnStatisticsLsTsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsTsUnit.setStatus("mandatory")


class _AwnStatisticsLsTsCard_Type(Integer32):
    """Custom type awnStatisticsLsTsCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsLsTsCard_Type.__name__ = "Integer32"
_AwnStatisticsLsTsCard_Object = MibTableColumn
awnStatisticsLsTsCard = _AwnStatisticsLsTsCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1, 2),
    _AwnStatisticsLsTsCard_Type()
)
awnStatisticsLsTsCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsTsCard.setStatus("mandatory")


class _AwnStatisticsLsTsPort_Type(Integer32):
    """Custom type awnStatisticsLsTsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsLsTsPort_Type.__name__ = "Integer32"
_AwnStatisticsLsTsPort_Object = MibTableColumn
awnStatisticsLsTsPort = _AwnStatisticsLsTsPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1, 3),
    _AwnStatisticsLsTsPort_Type()
)
awnStatisticsLsTsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsTsPort.setStatus("mandatory")


class _AwnStatisticsLsTsTs_Type(Integer32):
    """Custom type awnStatisticsLsTsTs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_AwnStatisticsLsTsTs_Type.__name__ = "Integer32"
_AwnStatisticsLsTsTs_Object = MibTableColumn
awnStatisticsLsTsTs = _AwnStatisticsLsTsTs_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1, 4),
    _AwnStatisticsLsTsTs_Type()
)
awnStatisticsLsTsTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsTsTs.setStatus("mandatory")


class _AwnStatisticsLsTsData_Type(OctetString):
    """Custom type awnStatisticsLsTsData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(104, 104),
    )


_AwnStatisticsLsTsData_Type.__name__ = "OctetString"
_AwnStatisticsLsTsData_Object = MibTableColumn
awnStatisticsLsTsData = _AwnStatisticsLsTsData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 19, 1, 1, 5),
    _AwnStatisticsLsTsData_Type()
)
awnStatisticsLsTsData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsLsTsData.setStatus("mandatory")
_AwnStatisticsSys_ObjectIdentity = ObjectIdentity
awnStatisticsSys = _AwnStatisticsSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 20)
)


class _AwnStatisticsSysDroppedCells_Type(OctetString):
    """Custom type awnStatisticsSysDroppedCells based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_AwnStatisticsSysDroppedCells_Type.__name__ = "OctetString"
_AwnStatisticsSysDroppedCells_Object = MibScalar
awnStatisticsSysDroppedCells = _AwnStatisticsSysDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 20, 1),
    _AwnStatisticsSysDroppedCells_Type()
)
awnStatisticsSysDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsSysDroppedCells.setStatus("mandatory")
_AwnStatisticsIpFrame_ObjectIdentity = ObjectIdentity
awnStatisticsIpFrame = _AwnStatisticsIpFrame_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 21)
)
_AwnStatisticsIpFrameTable_Object = MibTable
awnStatisticsIpFrameTable = _AwnStatisticsIpFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 21, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsIpFrameTable.setStatus("mandatory")
_AwnStatisticsIpFrameEntry_Object = MibTableRow
awnStatisticsIpFrameEntry = _AwnStatisticsIpFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 21, 1, 1)
)
awnStatisticsIpFrameEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsIpFrameAddr"),
)
if mibBuilder.loadTexts:
    awnStatisticsIpFrameEntry.setStatus("mandatory")
_AwnStatisticsIpFrameAddr_Type = IpAddress
_AwnStatisticsIpFrameAddr_Object = MibTableColumn
awnStatisticsIpFrameAddr = _AwnStatisticsIpFrameAddr_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 21, 1, 1, 1),
    _AwnStatisticsIpFrameAddr_Type()
)
awnStatisticsIpFrameAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsIpFrameAddr.setStatus("mandatory")


class _AwnStatisticsIpFrameData_Type(OctetString):
    """Custom type awnStatisticsIpFrameData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(108, 108),
    )


_AwnStatisticsIpFrameData_Type.__name__ = "OctetString"
_AwnStatisticsIpFrameData_Object = MibTableColumn
awnStatisticsIpFrameData = _AwnStatisticsIpFrameData_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 21, 1, 1, 2),
    _AwnStatisticsIpFrameData_Type()
)
awnStatisticsIpFrameData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsIpFrameData.setStatus("mandatory")
_AwnStatisticsDlci_ObjectIdentity = ObjectIdentity
awnStatisticsDlci = _AwnStatisticsDlci_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22)
)
_AwnStatisticsDlciTable_Object = MibTable
awnStatisticsDlciTable = _AwnStatisticsDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1)
)
if mibBuilder.loadTexts:
    awnStatisticsDlciTable.setStatus("mandatory")
_AwnStatisticsDlciEntry_Object = MibTableRow
awnStatisticsDlciEntry = _AwnStatisticsDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1)
)
awnStatisticsDlciEntry.setIndexNames(
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsDlciUnit"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsDlciCard"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsDlciPort"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsDlciTimeslot"),
    (0, "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06", "awnStatisticsDlciDlci"),
)
if mibBuilder.loadTexts:
    awnStatisticsDlciEntry.setStatus("mandatory")


class _AwnStatisticsDlciUnit_Type(Integer32):
    """Custom type awnStatisticsDlciUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsDlciUnit_Type.__name__ = "Integer32"
_AwnStatisticsDlciUnit_Object = MibTableColumn
awnStatisticsDlciUnit = _AwnStatisticsDlciUnit_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 1),
    _AwnStatisticsDlciUnit_Type()
)
awnStatisticsDlciUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciUnit.setStatus("mandatory")


class _AwnStatisticsDlciCard_Type(Integer32):
    """Custom type awnStatisticsDlciCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AwnStatisticsDlciCard_Type.__name__ = "Integer32"
_AwnStatisticsDlciCard_Object = MibTableColumn
awnStatisticsDlciCard = _AwnStatisticsDlciCard_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 2),
    _AwnStatisticsDlciCard_Type()
)
awnStatisticsDlciCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciCard.setStatus("mandatory")


class _AwnStatisticsDlciPort_Type(Integer32):
    """Custom type awnStatisticsDlciPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AwnStatisticsDlciPort_Type.__name__ = "Integer32"
_AwnStatisticsDlciPort_Object = MibTableColumn
awnStatisticsDlciPort = _AwnStatisticsDlciPort_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 3),
    _AwnStatisticsDlciPort_Type()
)
awnStatisticsDlciPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciPort.setStatus("mandatory")


class _AwnStatisticsDlciTimeslot_Type(Integer32):
    """Custom type awnStatisticsDlciTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AwnStatisticsDlciTimeslot_Type.__name__ = "Integer32"
_AwnStatisticsDlciTimeslot_Object = MibTableColumn
awnStatisticsDlciTimeslot = _AwnStatisticsDlciTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 4),
    _AwnStatisticsDlciTimeslot_Type()
)
awnStatisticsDlciTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciTimeslot.setStatus("mandatory")


class _AwnStatisticsDlciDlci_Type(Integer32):
    """Custom type awnStatisticsDlciDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AwnStatisticsDlciDlci_Type.__name__ = "Integer32"
_AwnStatisticsDlciDlci_Object = MibTableColumn
awnStatisticsDlciDlci = _AwnStatisticsDlciDlci_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 5),
    _AwnStatisticsDlciDlci_Type()
)
awnStatisticsDlciDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciDlci.setStatus("mandatory")


class _AwnStatisticsDlciBriClad_Type(OctetString):
    """Custom type awnStatisticsDlciBriClad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(168, 168),
    )


_AwnStatisticsDlciBriClad_Type.__name__ = "OctetString"
_AwnStatisticsDlciBriClad_Object = MibTableColumn
awnStatisticsDlciBriClad = _AwnStatisticsDlciBriClad_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 2, 22, 1, 1, 6),
    _AwnStatisticsDlciBriClad_Type()
)
awnStatisticsDlciBriClad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnStatisticsDlciBriClad.setStatus("mandatory")
_AwnIlmi_ObjectIdentity = ObjectIdentity
awnIlmi = _AwnIlmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 3)
)
_AwnIlmiIns_ObjectIdentity = ObjectIdentity
awnIlmiIns = _AwnIlmiIns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 3, 1)
)
_AwnIlmiInsRouteadd_Type = Integer32
_AwnIlmiInsRouteadd_Object = MibScalar
awnIlmiInsRouteadd = _AwnIlmiInsRouteadd_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 3, 1, 1),
    _AwnIlmiInsRouteadd_Type()
)
awnIlmiInsRouteadd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnIlmiInsRouteadd.setStatus("mandatory")
_AwnIlmiInsRoutedel_Type = Integer32
_AwnIlmiInsRoutedel_Object = MibScalar
awnIlmiInsRoutedel = _AwnIlmiInsRoutedel_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 127, 29, 3, 1, 2),
    _AwnIlmiInsRoutedel_Type()
)
awnIlmiInsRoutedel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    awnIlmiInsRoutedel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUJITSU-EXTENDED-NONOS-AWN-MIB-V06",
    **{"fujitsu": fujitsu,
       "product": product,
       "nonos": nonos,
       "awn": awn,
       "awnSystem": awnSystem,
       "awnSysNode": awnSysNode,
       "awnSysNodeInformation": awnSysNodeInformation,
       "awnSysNodeCommonStatus": awnSysNodeCommonStatus,
       "awnSysNodeClk": awnSysNodeClk,
       "awnSysCom": awnSysCom,
       "awnSysComDevice": awnSysComDevice,
       "awnSysComPort": awnSysComPort,
       "awnSysComDevice2": awnSysComDevice2,
       "awnSysComPort2": awnSysComPort2,
       "awnSysLs": awnSysLs,
       "awnSysLsTable": awnSysLsTable,
       "awnSysLsEntry": awnSysLsEntry,
       "awnSysLsUnit": awnSysLsUnit,
       "awnSysLsDevice": awnSysLsDevice,
       "awnSysLsPort": awnSysLsPort,
       "awnSysLsDevice2": awnSysLsDevice2,
       "awnSysLsPort2": awnSysLsPort2,
       "awnSysLine": awnSysLine,
       "awnSysLineTable": awnSysLineTable,
       "awnSysLineEntry": awnSysLineEntry,
       "awnSysLineUnit": awnSysLineUnit,
       "awnSysLineCard": awnSysLineCard,
       "awnSysLinePort": awnSysLinePort,
       "awnSysLineChannel": awnSysLineChannel,
       "awnSysLineMegalink": awnSysLineMegalink,
       "awnSysError": awnSysError,
       "awnSysErrorLog": awnSysErrorLog,
       "awnSysChannel": awnSysChannel,
       "awnSysChannelTable": awnSysChannelTable,
       "awnSysChannelEntry": awnSysChannelEntry,
       "awnSysChannelUnit": awnSysChannelUnit,
       "awnSysChannelCard": awnSysChannelCard,
       "awnSysChannelPort": awnSysChannelPort,
       "awnSysChannelTimeslot": awnSysChannelTimeslot,
       "awnSysChannelBackup": awnSysChannelBackup,
       "awnSysChannelBackup2": awnSysChannelBackup2,
       "awnSysEvent": awnSysEvent,
       "awnSysEventTable": awnSysEventTable,
       "awnSysEventEntry": awnSysEventEntry,
       "awnSysEventThreshold": awnSysEventThreshold,
       "awnSysPort": awnSysPort,
       "awnSysPortTable": awnSysPortTable,
       "awnSysPortEntry": awnSysPortEntry,
       "awnSysPortSlot": awnSysPortSlot,
       "awnSysPortAdapter": awnSysPortAdapter,
       "awnSysPortPort": awnSysPortPort,
       "awnSysPortMegalink": awnSysPortMegalink,
       "awnSysPortMegalink2": awnSysPortMegalink2,
       "awnSysConnComVcc": awnSysConnComVcc,
       "awnSysConnComVccTable": awnSysConnComVccTable,
       "awnSysConnComVccEntry": awnSysConnComVccEntry,
       "awnSysConnComVccSlot": awnSysConnComVccSlot,
       "awnSysConnComVccAdapter": awnSysConnComVccAdapter,
       "awnSysConnComVccPort": awnSysConnComVccPort,
       "awnSysConnComVccVpi": awnSysConnComVccVpi,
       "awnSysConnComVccVci": awnSysConnComVccVci,
       "awnSysConnComVccState": awnSysConnComVccState,
       "awnSysConnLsVcc": awnSysConnLsVcc,
       "awnSysConnLsVccTable": awnSysConnLsVccTable,
       "awnSysConnLsVccEntry": awnSysConnLsVccEntry,
       "awnSysConnLsVccUnit": awnSysConnLsVccUnit,
       "awnSysConnLSVccCard": awnSysConnLSVccCard,
       "awnSysConnLsVccPort": awnSysConnLsVccPort,
       "awnSysConnLsVccTimeslot": awnSysConnLsVccTimeslot,
       "awnSysConnLsVccVpi": awnSysConnLsVccVpi,
       "awnSysConnLsVccVci": awnSysConnLsVccVci,
       "awnSysConnLsVccState": awnSysConnLsVccState,
       "awnSysBackIpAddr": awnSysBackIpAddr,
       "awnStatistics": awnStatistics,
       "awnStatisticsSw": awnStatisticsSw,
       "awnStatisticsSwport": awnStatisticsSwport,
       "awnStatisticsLine": awnStatisticsLine,
       "awnStatisticsLineTable": awnStatisticsLineTable,
       "awnStatisticsLineEntry": awnStatisticsLineEntry,
       "awnStatisticsLineUnit": awnStatisticsLineUnit,
       "awnStatisticsLineCard": awnStatisticsLineCard,
       "awnStatisticsLinePort": awnStatisticsLinePort,
       "awnStatisticsLinePriWan": awnStatisticsLinePriWan,
       "awnStatisticsLineSriWan": awnStatisticsLineSriWan,
       "awnStatisticsLineBriWan": awnStatisticsLineBriWan,
       "awnStatisticsComLine": awnStatisticsComLine,
       "awnStatisticsComLineTable": awnStatisticsComLineTable,
       "awnStatisticsComLineEntry": awnStatisticsComLineEntry,
       "awnStatisticsComLineSlot": awnStatisticsComLineSlot,
       "awnStatisticsComLineAdapter": awnStatisticsComLineAdapter,
       "awnStatisticsComLinePort": awnStatisticsComLinePort,
       "awnStatisticsComLineAtm": awnStatisticsComLineAtm,
       "awnStatisticsComLan": awnStatisticsComLan,
       "awnStatisticsLsLine": awnStatisticsLsLine,
       "awnStatisticsLsLineTable": awnStatisticsLsLineTable,
       "awnStatisticsLsLineEntry": awnStatisticsLsLineEntry,
       "awnStatisticsLsLineUnit": awnStatisticsLsLineUnit,
       "awnStatisticsLsLineCard": awnStatisticsLsLineCard,
       "awnStatisticsLsLinePort": awnStatisticsLsLinePort,
       "awnStatisticsLsLinePriWan": awnStatisticsLsLinePriWan,
       "awnStatisticsLsLineBriWan": awnStatisticsLsLineBriWan,
       "awnStatisticsLsLinePriBup": awnStatisticsLsLinePriBup,
       "awnStatisticsLsLineFrclad": awnStatisticsLsLineFrclad,
       "awnStatisticsLsLineFrclad2": awnStatisticsLsLineFrclad2,
       "awnStatisticsLsLineFrclad3": awnStatisticsLsLineFrclad3,
       "awnStatisticsLsLineLineDif": awnStatisticsLsLineLineDif,
       "awnStatisticsLsLineDifFrclad": awnStatisticsLsLineDifFrclad,
       "awnStatisticsLsLinePriCes": awnStatisticsLsLinePriCes,
       "awnStatisticsLsLineDtkCodec": awnStatisticsLsLineDtkCodec,
       "awnStatisticsLsLineDtkDclad": awnStatisticsLsLineDtkDclad,
       "awnStatisticsLsLineDtkDclad2": awnStatisticsLsLineDtkDclad2,
       "awnStatisticsLsLineOdtCodec": awnStatisticsLsLineOdtCodec,
       "awnStatisticsLsLineOdtDclad": awnStatisticsLsLineOdtDclad,
       "awnStatisticsLsLineSriCes": awnStatisticsLsLineSriCes,
       "awnStatisticsLsLineBriBup": awnStatisticsLsLineBriBup,
       "awnStatisticsLsLineLrcrad": awnStatisticsLsLineLrcrad,
       "awnStatisticsLsLine45Mwan": awnStatisticsLsLine45Mwan,
       "awnStatisticsLsLineOdtCodecS": awnStatisticsLsLineOdtCodecS,
       "awnStatisticsLsLinePriWan24": awnStatisticsLsLinePriWan24,
       "awnStatisticsLsLineFfclad24a": awnStatisticsLsLineFfclad24a,
       "awnStatisticsLsLineFfclad24b": awnStatisticsLsLineFfclad24b,
       "awnStatisticsLsLineFfclad24c": awnStatisticsLsLineFfclad24c,
       "awnStatisticsLsLineVxaWan": awnStatisticsLsLineVxaWan,
       "awnStatisticsLsLineBriClad": awnStatisticsLsLineBriClad,
       "awnStatisticsComNniPort": awnStatisticsComNniPort,
       "awnStatisticsComNniPortTable": awnStatisticsComNniPortTable,
       "awnStatisticsComNniPortEntry": awnStatisticsComNniPortEntry,
       "awnStatisticsComNniPortSlot": awnStatisticsComNniPortSlot,
       "awnStatisticsComNniPortAdapter": awnStatisticsComNniPortAdapter,
       "awnStatisticsComNniPortPort": awnStatisticsComNniPortPort,
       "awnStatisticsComNniPortData": awnStatisticsComNniPortData,
       "awnStatisticsComNniVp": awnStatisticsComNniVp,
       "awnStatisticsComNniVpTable": awnStatisticsComNniVpTable,
       "awnStatisticsComNniVpEntry": awnStatisticsComNniVpEntry,
       "awnStatisticsComNniVpSlot": awnStatisticsComNniVpSlot,
       "awnStatisticsComNniVpAdapter": awnStatisticsComNniVpAdapter,
       "awnStatisticsComNniVpPort": awnStatisticsComNniVpPort,
       "awnStatisticsComNniVpVpi": awnStatisticsComNniVpVpi,
       "awnStatisticsComNniVptData": awnStatisticsComNniVptData,
       "awnStatisticsLsWanTs": awnStatisticsLsWanTs,
       "awnStatisticsLsWanTsTable": awnStatisticsLsWanTsTable,
       "awnStatisticsLsWanTsEntry": awnStatisticsLsWanTsEntry,
       "awnStatisticsLsWanTsUnit": awnStatisticsLsWanTsUnit,
       "awnStatisticsLsWanTsCard": awnStatisticsLsWanTsCard,
       "awnStatisticsLsWanTsPort": awnStatisticsLsWanTsPort,
       "awnStatisticsLsWanTsTs": awnStatisticsLsWanTsTs,
       "awnStatisticsLsWanTsData": awnStatisticsLsWanTsData,
       "awnStatisticsComNniPortRt": awnStatisticsComNniPortRt,
       "awnStatisticsComNniPortRtTable": awnStatisticsComNniPortRtTable,
       "awnStatisticsComNniPortRtEntry": awnStatisticsComNniPortRtEntry,
       "awnStatisticsComNniPortRtSlot": awnStatisticsComNniPortRtSlot,
       "awnStatisticsComNniPortRtAdapter": awnStatisticsComNniPortRtAdapter,
       "awnStatisticsComNniPortRtPort": awnStatisticsComNniPortRtPort,
       "awnStatisticsComNniPortRtCategory": awnStatisticsComNniPortRtCategory,
       "awnStatisticsComNniPortRtType": awnStatisticsComNniPortRtType,
       "awnStatisticsComNniPortRtData": awnStatisticsComNniPortRtData,
       "awnStatisticsComNniVpRt": awnStatisticsComNniVpRt,
       "awnStatisticsComNniVpRtTable": awnStatisticsComNniVpRtTable,
       "awnStatisticsComNniVpRtEntry": awnStatisticsComNniVpRtEntry,
       "awnStatisticsComNniVpRtSlot": awnStatisticsComNniVpRtSlot,
       "awnStatisticsComNniVpRtAdapter": awnStatisticsComNniVpRtAdapter,
       "awnStatisticsComNniVpRtPort": awnStatisticsComNniVpRtPort,
       "awnStatisticsComNniVpRtVpi": awnStatisticsComNniVpRtVpi,
       "awnStatisticsComNniVpRtCategory": awnStatisticsComNniVpRtCategory,
       "awnStatisticsComNniVpRtType": awnStatisticsComNniVpRtType,
       "awnStatisticsComNniVpRtData": awnStatisticsComNniVpRtData,
       "awnStatisticsLsWanTsRt": awnStatisticsLsWanTsRt,
       "awnStatisticsLsWanTsRtTable": awnStatisticsLsWanTsRtTable,
       "awnStatisticsLsWanTsRtEntry": awnStatisticsLsWanTsRtEntry,
       "awnStatisticsLsWanTsRtUnit": awnStatisticsLsWanTsRtUnit,
       "awnStatisticsLsWanTsRtCard": awnStatisticsLsWanTsRtCard,
       "awnStatisticsLsWanTsRtPort": awnStatisticsLsWanTsRtPort,
       "awnStatisticsLsWanTsRtTs": awnStatisticsLsWanTsRtTs,
       "awnStatisticsLsWanTsRtCategory": awnStatisticsLsWanTsRtCategory,
       "awnStatisticsLsWanTsRtType": awnStatisticsLsWanTsRtType,
       "awnStatisticsLsWanTsRtData": awnStatisticsLsWanTsRtData,
       "awnStatisticsVccAtmLine": awnStatisticsVccAtmLine,
       "awnStatisticsVccAtmLineTable": awnStatisticsVccAtmLineTable,
       "awnStatisticsVccAtmLineEntry": awnStatisticsVccAtmLineEntry,
       "awnStatisticsVccAtmLineSlot": awnStatisticsVccAtmLineSlot,
       "awnStatisticsVccAtmLineAdapter": awnStatisticsVccAtmLineAdapter,
       "awnStatisticsVccAtmLinePort": awnStatisticsVccAtmLinePort,
       "awnStatisticsVccAtmLineVpi": awnStatisticsVccAtmLineVpi,
       "awnStatisticsVccAtmLineVci": awnStatisticsVccAtmLineVci,
       "awnStatisticsVccAtmLineType": awnStatisticsVccAtmLineType,
       "awnStatisticsVccAtmLineData": awnStatisticsVccAtmLineData,
       "awnStatisticsVpcAtmLine": awnStatisticsVpcAtmLine,
       "awnStatisticsVpcAtmLineTable": awnStatisticsVpcAtmLineTable,
       "awnStatisticsVpcAtmLineEntry": awnStatisticsVpcAtmLineEntry,
       "awnStatisticsVpcAtmLineSlot": awnStatisticsVpcAtmLineSlot,
       "awnStatisticsVpcAtmLineAdapter": awnStatisticsVpcAtmLineAdapter,
       "awnStatisticsVpcAtmLinePort": awnStatisticsVpcAtmLinePort,
       "awnStatisticsVpcAtmLineVpi": awnStatisticsVpcAtmLineVpi,
       "awnStatisticsVpcAtmLineType": awnStatisticsVpcAtmLineType,
       "awnStatisticsVpcAtmLineData": awnStatisticsVpcAtmLineData,
       "awnStatisticsVccWanTs": awnStatisticsVccWanTs,
       "awnStatisticsVccWanTsTable": awnStatisticsVccWanTsTable,
       "awnStatisticsVccWanTsEntry": awnStatisticsVccWanTsEntry,
       "awnStatisticsVccWanTsUnit": awnStatisticsVccWanTsUnit,
       "awnStatisticsVccWanTsCard": awnStatisticsVccWanTsCard,
       "awnStatisticsVccWanTsPort": awnStatisticsVccWanTsPort,
       "awnStatisticsVccWanTsTs": awnStatisticsVccWanTsTs,
       "awnStatisticsVccWanTsVpi": awnStatisticsVccWanTsVpi,
       "awnStatisticsVccWanTsVci": awnStatisticsVccWanTsVci,
       "awnStatisticsVccWanTsType": awnStatisticsVccWanTsType,
       "awnStatisticsVccWanTsData": awnStatisticsVccWanTsData,
       "awnStatisticsVccFrLine": awnStatisticsVccFrLine,
       "awnStatisticsVccFrLineTable": awnStatisticsVccFrLineTable,
       "awnStatisticsVccFrLineEntry": awnStatisticsVccFrLineEntry,
       "awnStatisticsVccFrLineUnit": awnStatisticsVccFrLineUnit,
       "awnStatisticsVccFrLineCard": awnStatisticsVccFrLineCard,
       "awnStatisticsVccFrLinePort": awnStatisticsVccFrLinePort,
       "awnStatisticsVccFrLineTimeslot": awnStatisticsVccFrLineTimeslot,
       "awnStatisticsVccFrLineDlci": awnStatisticsVccFrLineDlci,
       "awnStatisticsVccFrLineType": awnStatisticsVccFrLineType,
       "awnStatisticsVccFrLineData": awnStatisticsVccFrLineData,
       "awnStatisticsVccFfLine": awnStatisticsVccFfLine,
       "awnStatisticsVccFfLineTable": awnStatisticsVccFfLineTable,
       "awnStatisticsVccFfLineEntry": awnStatisticsVccFfLineEntry,
       "awnStatisticsVccFfLineUnit": awnStatisticsVccFfLineUnit,
       "awnStatisticsVccFfLineCard": awnStatisticsVccFfLineCard,
       "awnStatisticsVccFfLinePort": awnStatisticsVccFfLinePort,
       "awnStatisticsVccFfLineTimeslot": awnStatisticsVccFfLineTimeslot,
       "awnStatisticsVccFfLineType": awnStatisticsVccFfLineType,
       "awnStatisticsVccFfLineData": awnStatisticsVccFfLineData,
       "awnStatisticsLsWanVp": awnStatisticsLsWanVp,
       "awnStatisticsLsWanVpTable": awnStatisticsLsWanVpTable,
       "awnStatisticsLsWanVpEntry": awnStatisticsLsWanVpEntry,
       "awnStatisticsLsWanVpUnit": awnStatisticsLsWanVpUnit,
       "awnStatisticsLsWanVpCard": awnStatisticsLsWanVpCard,
       "awnStatisticsLsWanVpPort": awnStatisticsLsWanVpPort,
       "awnStatisticsLsWanVpVpi": awnStatisticsLsWanVpVpi,
       "awnStatisticsLsWanVpData": awnStatisticsLsWanVpData,
       "awnStatisticsLsWanVpRt": awnStatisticsLsWanVpRt,
       "awnStatisticsLsWanVpRtTable": awnStatisticsLsWanVpRtTable,
       "awnStatisticsLsWanVpRtEntry": awnStatisticsLsWanVpRtEntry,
       "awnStatisticsLsWanVpRtUnit": awnStatisticsLsWanVpRtUnit,
       "awnStatisticsLsWanVpRtCard": awnStatisticsLsWanVpRtCard,
       "awnStatisticsLsWanVpRtPort": awnStatisticsLsWanVpRtPort,
       "awnStatisticsLsWanVpRtVpi": awnStatisticsLsWanVpRtVpi,
       "awnStatisticsLsWanVpRtCategory": awnStatisticsLsWanVpRtCategory,
       "awnStatisticsLsWanVpRtType": awnStatisticsLsWanVpRtType,
       "awnStatisticsLsWanVpRtData": awnStatisticsLsWanVpRtData,
       "awnStatisticsComAtmLine": awnStatisticsComAtmLine,
       "awnStatisticsComAtmLineTable": awnStatisticsComAtmLineTable,
       "awnStatisticsComAtmLineEntry": awnStatisticsComAtmLineEntry,
       "awnStatisticsComAtmLineSlot": awnStatisticsComAtmLineSlot,
       "awnStatisticsComAtmLineAdapter": awnStatisticsComAtmLineAdapter,
       "awnStatisticsComAtmLinePort": awnStatisticsComAtmLinePort,
       "awnStatisticsComAtmLineVpi": awnStatisticsComAtmLineVpi,
       "awnStatisticsComAtmLineData": awnStatisticsComAtmLineData,
       "awnStatisticsLsTs": awnStatisticsLsTs,
       "awnStatisticsLsTsTable": awnStatisticsLsTsTable,
       "awnStatisticsLsTsEntry": awnStatisticsLsTsEntry,
       "awnStatisticsLsTsUnit": awnStatisticsLsTsUnit,
       "awnStatisticsLsTsCard": awnStatisticsLsTsCard,
       "awnStatisticsLsTsPort": awnStatisticsLsTsPort,
       "awnStatisticsLsTsTs": awnStatisticsLsTsTs,
       "awnStatisticsLsTsData": awnStatisticsLsTsData,
       "awnStatisticsSys": awnStatisticsSys,
       "awnStatisticsSysDroppedCells": awnStatisticsSysDroppedCells,
       "awnStatisticsIpFrame": awnStatisticsIpFrame,
       "awnStatisticsIpFrameTable": awnStatisticsIpFrameTable,
       "awnStatisticsIpFrameEntry": awnStatisticsIpFrameEntry,
       "awnStatisticsIpFrameAddr": awnStatisticsIpFrameAddr,
       "awnStatisticsIpFrameData": awnStatisticsIpFrameData,
       "awnStatisticsDlci": awnStatisticsDlci,
       "awnStatisticsDlciTable": awnStatisticsDlciTable,
       "awnStatisticsDlciEntry": awnStatisticsDlciEntry,
       "awnStatisticsDlciUnit": awnStatisticsDlciUnit,
       "awnStatisticsDlciCard": awnStatisticsDlciCard,
       "awnStatisticsDlciPort": awnStatisticsDlciPort,
       "awnStatisticsDlciTimeslot": awnStatisticsDlciTimeslot,
       "awnStatisticsDlciDlci": awnStatisticsDlciDlci,
       "awnStatisticsDlciBriClad": awnStatisticsDlciBriClad,
       "awnIlmi": awnIlmi,
       "awnIlmiIns": awnIlmiIns,
       "awnIlmiInsRouteadd": awnIlmiInsRouteadd,
       "awnIlmiInsRoutedel": awnIlmiInsRoutedel}
)
