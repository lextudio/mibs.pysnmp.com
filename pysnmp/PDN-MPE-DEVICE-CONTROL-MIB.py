# SNMP MIB module (PDN-MPE-DEVICE-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-DEVICE-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:54 2024
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

(pdn_mpe,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-mpe")

(ResetStates,) = mibBuilder.importSymbols(
    "PDN-TC",
    "ResetStates")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

mpeDevControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10)
)
mpeDevControl.setRevisions(
        ("1902-04-29 00:00",
         "1902-04-09 09:05",
         "1900-11-21 18:00",
         "1900-10-26 14:00",
         "1900-10-18 18:30",
         "1900-10-06 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpeDevControlMIBObjects_ObjectIdentity = ObjectIdentity
mpeDevControlMIBObjects = _MpeDevControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1)
)
_MpeDevHwControl_ObjectIdentity = ObjectIdentity
mpeDevHwControl = _MpeDevHwControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1)
)
_MpeDevControlTable_Object = MibTable
mpeDevControlTable = _MpeDevControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpeDevControlTable.setStatus("current")
_MpeDevControlEntry_Object = MibTableRow
mpeDevControlEntry = _MpeDevControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1, 1)
)
mpeDevControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeDevControlEntry.setStatus("current")
_MpeDevControlReset_Type = ResetStates
_MpeDevControlReset_Object = MibTableColumn
mpeDevControlReset = _MpeDevControlReset_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 1, 1, 1),
    _MpeDevControlReset_Type()
)
mpeDevControlReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevControlReset.setStatus("current")
_MpeDevControlSelfTestTable_Object = MibTable
mpeDevControlSelfTestTable = _MpeDevControlSelfTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mpeDevControlSelfTestTable.setStatus("current")
_MpeDevControlSelfTestEntry_Object = MibTableRow
mpeDevControlSelfTestEntry = _MpeDevControlSelfTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2, 1)
)
mpeDevControlSelfTestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeDevControlSelfTestEntry.setStatus("current")


class _MpeDevControlExtendedSelfTest_Type(Integer32):
    """Custom type mpeDevControlExtendedSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableExtendSelfTestAndReset", 2),
          ("noOp", 1))
    )


_MpeDevControlExtendedSelfTest_Type.__name__ = "Integer32"
_MpeDevControlExtendedSelfTest_Object = MibTableColumn
mpeDevControlExtendedSelfTest = _MpeDevControlExtendedSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 1, 2, 1, 1),
    _MpeDevControlExtendedSelfTest_Type()
)
mpeDevControlExtendedSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeDevControlExtendedSelfTest.setStatus("current")
_MpeDevFileXferConfig_ObjectIdentity = ObjectIdentity
mpeDevFileXferConfig = _MpeDevFileXferConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2)
)
_MpeDevFileXferConfigTable_Object = MibTable
mpeDevFileXferConfigTable = _MpeDevFileXferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpeDevFileXferConfigTable.setStatus("current")
_MpeDevFileXferConfigEntry_Object = MibTableRow
mpeDevFileXferConfigEntry = _MpeDevFileXferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1)
)
mpeDevFileXferConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeDevFileXferConfigEntry.setStatus("current")
_MpeDevFileXferFileName_Type = DisplayString
_MpeDevFileXferFileName_Object = MibTableColumn
mpeDevFileXferFileName = _MpeDevFileXferFileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 1),
    _MpeDevFileXferFileName_Type()
)
mpeDevFileXferFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferFileName.setStatus("current")


class _MpeDevFileXferCopyProtocol_Type(Integer32):
    """Custom type mpeDevFileXferCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 2),
          ("tftp", 1))
    )


_MpeDevFileXferCopyProtocol_Type.__name__ = "Integer32"
_MpeDevFileXferCopyProtocol_Object = MibTableColumn
mpeDevFileXferCopyProtocol = _MpeDevFileXferCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 2),
    _MpeDevFileXferCopyProtocol_Type()
)
mpeDevFileXferCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferCopyProtocol.setStatus("current")


class _MpeDevFileXferFileType_Type(Integer32):
    """Custom type mpeDevFileXferFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("firmware", 1))
    )


_MpeDevFileXferFileType_Type.__name__ = "Integer32"
_MpeDevFileXferFileType_Object = MibTableColumn
mpeDevFileXferFileType = _MpeDevFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 3),
    _MpeDevFileXferFileType_Type()
)
mpeDevFileXferFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferFileType.setStatus("current")
_MpeDevFileXferServerIpAddress_Type = IpAddress
_MpeDevFileXferServerIpAddress_Object = MibTableColumn
mpeDevFileXferServerIpAddress = _MpeDevFileXferServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 4),
    _MpeDevFileXferServerIpAddress_Type()
)
mpeDevFileXferServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferServerIpAddress.setStatus("current")
_MpeDevFileXferUserName_Type = DisplayString
_MpeDevFileXferUserName_Object = MibTableColumn
mpeDevFileXferUserName = _MpeDevFileXferUserName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 5),
    _MpeDevFileXferUserName_Type()
)
mpeDevFileXferUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferUserName.setStatus("current")
_MpeDevFileXferUserPassword_Type = DisplayString
_MpeDevFileXferUserPassword_Object = MibTableColumn
mpeDevFileXferUserPassword = _MpeDevFileXferUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 6),
    _MpeDevFileXferUserPassword_Type()
)
mpeDevFileXferUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferUserPassword.setStatus("current")


class _MpeDevFileXferOperation_Type(Integer32):
    """Custom type mpeDevFileXferOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_MpeDevFileXferOperation_Type.__name__ = "Integer32"
_MpeDevFileXferOperation_Object = MibTableColumn
mpeDevFileXferOperation = _MpeDevFileXferOperation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 7),
    _MpeDevFileXferOperation_Type()
)
mpeDevFileXferOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferOperation.setStatus("current")
_MpeDevFileXferPktsSent_Type = Counter32
_MpeDevFileXferPktsSent_Object = MibTableColumn
mpeDevFileXferPktsSent = _MpeDevFileXferPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 8),
    _MpeDevFileXferPktsSent_Type()
)
mpeDevFileXferPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferPktsSent.setStatus("current")
_MpeDevFileXferPktsRecv_Type = Counter32
_MpeDevFileXferPktsRecv_Object = MibTableColumn
mpeDevFileXferPktsRecv = _MpeDevFileXferPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 9),
    _MpeDevFileXferPktsRecv_Type()
)
mpeDevFileXferPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferPktsRecv.setStatus("current")
_MpeDevFileXferOctetsSent_Type = Counter32
_MpeDevFileXferOctetsSent_Object = MibTableColumn
mpeDevFileXferOctetsSent = _MpeDevFileXferOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 10),
    _MpeDevFileXferOctetsSent_Type()
)
mpeDevFileXferOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferOctetsSent.setStatus("current")
_MpeDevFileXferOctetsRecv_Type = Counter32
_MpeDevFileXferOctetsRecv_Object = MibTableColumn
mpeDevFileXferOctetsRecv = _MpeDevFileXferOctetsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 11),
    _MpeDevFileXferOctetsRecv_Type()
)
mpeDevFileXferOctetsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferOctetsRecv.setStatus("current")


class _MpeDevFileXferOwnerString_Type(OctetString):
    """Custom type mpeDevFileXferOwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpeDevFileXferOwnerString_Type.__name__ = "OctetString"
_MpeDevFileXferOwnerString_Object = MibTableColumn
mpeDevFileXferOwnerString = _MpeDevFileXferOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 12),
    _MpeDevFileXferOwnerString_Type()
)
mpeDevFileXferOwnerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferOwnerString.setStatus("current")


class _MpeDevFileXferStatus_Type(Integer32):
    """Custom type mpeDevFileXferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inprogress", 4),
          ("none", 1),
          ("success", 2))
    )


_MpeDevFileXferStatus_Type.__name__ = "Integer32"
_MpeDevFileXferStatus_Object = MibTableColumn
mpeDevFileXferStatus = _MpeDevFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 13),
    _MpeDevFileXferStatus_Type()
)
mpeDevFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferStatus.setStatus("current")
_MpeDevFileXferErrorStatus_Type = Integer32
_MpeDevFileXferErrorStatus_Object = MibTableColumn
mpeDevFileXferErrorStatus = _MpeDevFileXferErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 14),
    _MpeDevFileXferErrorStatus_Type()
)
mpeDevFileXferErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferErrorStatus.setStatus("current")


class _MpeDevFileXferSendEvent_Type(Integer32):
    """Custom type mpeDevFileXferSendEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpeDevFileXferSendEvent_Type.__name__ = "Integer32"
_MpeDevFileXferSendEvent_Object = MibTableColumn
mpeDevFileXferSendEvent = _MpeDevFileXferSendEvent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 15),
    _MpeDevFileXferSendEvent_Type()
)
mpeDevFileXferSendEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferSendEvent.setStatus("current")
_MpeDevFileXferRowStatus_Type = RowStatus
_MpeDevFileXferRowStatus_Object = MibTableColumn
mpeDevFileXferRowStatus = _MpeDevFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 16),
    _MpeDevFileXferRowStatus_Type()
)
mpeDevFileXferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferRowStatus.setStatus("current")
_MpeDevFileXferXferTime_Type = TimeTicks
_MpeDevFileXferXferTime_Object = MibTableColumn
mpeDevFileXferXferTime = _MpeDevFileXferXferTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 17),
    _MpeDevFileXferXferTime_Type()
)
mpeDevFileXferXferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFileXferXferTime.setStatus("current")


class _MpeDevFileXferFileFormat_Type(Integer32):
    """Custom type mpeDevFileXferFileFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("binary", 2))
    )


_MpeDevFileXferFileFormat_Type.__name__ = "Integer32"
_MpeDevFileXferFileFormat_Object = MibTableColumn
mpeDevFileXferFileFormat = _MpeDevFileXferFileFormat_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 2, 1, 1, 18),
    _MpeDevFileXferFileFormat_Type()
)
mpeDevFileXferFileFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFileXferFileFormat.setStatus("current")
_MpeDevFirmwareControl_ObjectIdentity = ObjectIdentity
mpeDevFirmwareControl = _MpeDevFirmwareControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3)
)
_MpeDevFirmwareControlTable_Object = MibTable
mpeDevFirmwareControlTable = _MpeDevFirmwareControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mpeDevFirmwareControlTable.setStatus("current")
_MpeDevFirmwareControlEntry_Object = MibTableRow
mpeDevFirmwareControlEntry = _MpeDevFirmwareControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1)
)
mpeDevFirmwareControlEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlIndex"),
)
if mibBuilder.loadTexts:
    mpeDevFirmwareControlEntry.setStatus("current")
_MpeDevFirmwareControlIndex_Type = Integer32
_MpeDevFirmwareControlIndex_Object = MibTableColumn
mpeDevFirmwareControlIndex = _MpeDevFirmwareControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 1),
    _MpeDevFirmwareControlIndex_Type()
)
mpeDevFirmwareControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFirmwareControlIndex.setStatus("current")


class _MpeDevFirmwareControlRelease_Type(DisplayString):
    """Custom type mpeDevFirmwareControlRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MpeDevFirmwareControlRelease_Type.__name__ = "DisplayString"
_MpeDevFirmwareControlRelease_Object = MibTableColumn
mpeDevFirmwareControlRelease = _MpeDevFirmwareControlRelease_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 2),
    _MpeDevFirmwareControlRelease_Type()
)
mpeDevFirmwareControlRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFirmwareControlRelease.setStatus("current")


class _MpeDevFirmwareControlOperStatus_Type(Integer32):
    """Custom type mpeDevFirmwareControlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("unknown", 3),
          ("valid", 1))
    )


_MpeDevFirmwareControlOperStatus_Type.__name__ = "Integer32"
_MpeDevFirmwareControlOperStatus_Object = MibTableColumn
mpeDevFirmwareControlOperStatus = _MpeDevFirmwareControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 3),
    _MpeDevFirmwareControlOperStatus_Type()
)
mpeDevFirmwareControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevFirmwareControlOperStatus.setStatus("current")


class _MpeDevFirmwareControlAdminStatus_Type(Integer32):
    """Custom type mpeDevFirmwareControlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpeDevFirmwareControlAdminStatus_Type.__name__ = "Integer32"
_MpeDevFirmwareControlAdminStatus_Object = MibTableColumn
mpeDevFirmwareControlAdminStatus = _MpeDevFirmwareControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 3, 1, 1, 4),
    _MpeDevFirmwareControlAdminStatus_Type()
)
mpeDevFirmwareControlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpeDevFirmwareControlAdminStatus.setStatus("current")
_MpeDevTestControl_ObjectIdentity = ObjectIdentity
mpeDevTestControl = _MpeDevTestControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4)
)
_MpeDevControlTestTable_Object = MibTable
mpeDevControlTestTable = _MpeDevControlTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3)
)
if mibBuilder.loadTexts:
    mpeDevControlTestTable.setStatus("current")
_MpeDevControlTestEntry_Object = MibTableRow
mpeDevControlTestEntry = _MpeDevControlTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1)
)
mpeDevControlTestEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeDevControlTestEntry.setStatus("current")


class _MpeDevControlTestType_Type(Integer32):
    """Custom type mpeDevControlTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("lampTest", 1)
    )


_MpeDevControlTestType_Type.__name__ = "Integer32"
_MpeDevControlTestType_Object = MibTableColumn
mpeDevControlTestType = _MpeDevControlTestType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 1),
    _MpeDevControlTestType_Type()
)
mpeDevControlTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeDevControlTestType.setStatus("current")


class _MpeDevControlTestStatus_Type(Integer32):
    """Custom type mpeDevControlTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_MpeDevControlTestStatus_Type.__name__ = "Integer32"
_MpeDevControlTestStatus_Object = MibTableColumn
mpeDevControlTestStatus = _MpeDevControlTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 2),
    _MpeDevControlTestStatus_Type()
)
mpeDevControlTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeDevControlTestStatus.setStatus("current")


class _MpeDevControlTestCmd_Type(Integer32):
    """Custom type mpeDevControlTestCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_MpeDevControlTestCmd_Type.__name__ = "Integer32"
_MpeDevControlTestCmd_Object = MibTableColumn
mpeDevControlTestCmd = _MpeDevControlTestCmd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 1, 4, 3, 1, 3),
    _MpeDevControlTestCmd_Type()
)
mpeDevControlTestCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeDevControlTestCmd.setStatus("current")
_MpeDevControlMIBTraps_ObjectIdentity = ObjectIdentity
mpeDevControlMIBTraps = _MpeDevControlMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2)
)
_MpeDevControlMIBTrapsV2_ObjectIdentity = ObjectIdentity
mpeDevControlMIBTrapsV2 = _MpeDevControlMIBTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2, 0)
)
if mibBuilder.loadTexts:
    mpeDevControlMIBTrapsV2.setStatus("current")
_MpeDevControlMIBGroups_ObjectIdentity = ObjectIdentity
mpeDevControlMIBGroups = _MpeDevControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3)
)

# Managed Objects groups

mpeDevHwControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 1)
)
mpeDevHwControlGroup.setObjects(
      *(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlReset"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlExtendedSelfTest"))
)
if mibBuilder.loadTexts:
    mpeDevHwControlGroup.setStatus("current")

mpeDevFileXferConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 2)
)
mpeDevFileXferConfigGroup.setObjects(
      *(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileName"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferCopyProtocol"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileType"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferServerIpAddress"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferUserName"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferUserPassword"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOperation"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferPktsSent"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferPktsRecv"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOctetsSent"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOctetsRecv"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOwnerString"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferErrorStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferSendEvent"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferRowStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferXferTime"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileFormat"))
)
if mibBuilder.loadTexts:
    mpeDevFileXferConfigGroup.setStatus("current")

mpeDevFirmwareControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 3)
)
mpeDevFirmwareControlGroup.setObjects(
      *(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlIndex"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlRelease"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlOperStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFirmwareControlAdminStatus"))
)
if mibBuilder.loadTexts:
    mpeDevFirmwareControlGroup.setStatus("current")

mpeDevTestControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 4)
)
mpeDevTestControlGroup.setObjects(
      *(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestType"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevControlTestCmd"))
)
if mibBuilder.loadTexts:
    mpeDevTestControlGroup.setStatus("current")


# Notification objects

mpeDevFileXferEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 2, 0, 1)
)
mpeDevFileXferEvent.setObjects(
      *(("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferErrorStatus"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferOperation"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileType"),
        ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferFileName"))
)
if mibBuilder.loadTexts:
    mpeDevFileXferEvent.setStatus(
        "current"
    )


# Notifications groups

mpeDevFileXferEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 10, 3, 5)
)
mpeDevFileXferEventGroup.setObjects(
    ("PDN-MPE-DEVICE-CONTROL-MIB", "mpeDevFileXferEvent")
)
if mibBuilder.loadTexts:
    mpeDevFileXferEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-DEVICE-CONTROL-MIB",
    **{"mpeDevControl": mpeDevControl,
       "mpeDevControlMIBObjects": mpeDevControlMIBObjects,
       "mpeDevHwControl": mpeDevHwControl,
       "mpeDevControlTable": mpeDevControlTable,
       "mpeDevControlEntry": mpeDevControlEntry,
       "mpeDevControlReset": mpeDevControlReset,
       "mpeDevControlSelfTestTable": mpeDevControlSelfTestTable,
       "mpeDevControlSelfTestEntry": mpeDevControlSelfTestEntry,
       "mpeDevControlExtendedSelfTest": mpeDevControlExtendedSelfTest,
       "mpeDevFileXferConfig": mpeDevFileXferConfig,
       "mpeDevFileXferConfigTable": mpeDevFileXferConfigTable,
       "mpeDevFileXferConfigEntry": mpeDevFileXferConfigEntry,
       "mpeDevFileXferFileName": mpeDevFileXferFileName,
       "mpeDevFileXferCopyProtocol": mpeDevFileXferCopyProtocol,
       "mpeDevFileXferFileType": mpeDevFileXferFileType,
       "mpeDevFileXferServerIpAddress": mpeDevFileXferServerIpAddress,
       "mpeDevFileXferUserName": mpeDevFileXferUserName,
       "mpeDevFileXferUserPassword": mpeDevFileXferUserPassword,
       "mpeDevFileXferOperation": mpeDevFileXferOperation,
       "mpeDevFileXferPktsSent": mpeDevFileXferPktsSent,
       "mpeDevFileXferPktsRecv": mpeDevFileXferPktsRecv,
       "mpeDevFileXferOctetsSent": mpeDevFileXferOctetsSent,
       "mpeDevFileXferOctetsRecv": mpeDevFileXferOctetsRecv,
       "mpeDevFileXferOwnerString": mpeDevFileXferOwnerString,
       "mpeDevFileXferStatus": mpeDevFileXferStatus,
       "mpeDevFileXferErrorStatus": mpeDevFileXferErrorStatus,
       "mpeDevFileXferSendEvent": mpeDevFileXferSendEvent,
       "mpeDevFileXferRowStatus": mpeDevFileXferRowStatus,
       "mpeDevFileXferXferTime": mpeDevFileXferXferTime,
       "mpeDevFileXferFileFormat": mpeDevFileXferFileFormat,
       "mpeDevFirmwareControl": mpeDevFirmwareControl,
       "mpeDevFirmwareControlTable": mpeDevFirmwareControlTable,
       "mpeDevFirmwareControlEntry": mpeDevFirmwareControlEntry,
       "mpeDevFirmwareControlIndex": mpeDevFirmwareControlIndex,
       "mpeDevFirmwareControlRelease": mpeDevFirmwareControlRelease,
       "mpeDevFirmwareControlOperStatus": mpeDevFirmwareControlOperStatus,
       "mpeDevFirmwareControlAdminStatus": mpeDevFirmwareControlAdminStatus,
       "mpeDevTestControl": mpeDevTestControl,
       "mpeDevControlTestTable": mpeDevControlTestTable,
       "mpeDevControlTestEntry": mpeDevControlTestEntry,
       "mpeDevControlTestType": mpeDevControlTestType,
       "mpeDevControlTestStatus": mpeDevControlTestStatus,
       "mpeDevControlTestCmd": mpeDevControlTestCmd,
       "mpeDevControlMIBTraps": mpeDevControlMIBTraps,
       "mpeDevControlMIBTrapsV2": mpeDevControlMIBTrapsV2,
       "mpeDevFileXferEvent": mpeDevFileXferEvent,
       "mpeDevControlMIBGroups": mpeDevControlMIBGroups,
       "mpeDevHwControlGroup": mpeDevHwControlGroup,
       "mpeDevFileXferConfigGroup": mpeDevFileXferConfigGroup,
       "mpeDevFirmwareControlGroup": mpeDevFirmwareControlGroup,
       "mpeDevTestControlGroup": mpeDevTestControlGroup,
       "mpeDevFileXferEventGroup": mpeDevFileXferEventGroup}
)
