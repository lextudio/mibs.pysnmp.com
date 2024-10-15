# SNMP MIB module (ACC-RLOAD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-RLOAD
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:54 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccRload_ObjectIdentity = ObjectIdentity
accRload = _AccRload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27)
)
_AccRlSourceTable_Object = MibTable
accRlSourceTable = _AccRlSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    accRlSourceTable.setStatus("mandatory")
_AccRlSourceEntry_Object = MibTableRow
accRlSourceEntry = _AccRlSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1)
)
accRlSourceEntry.setIndexNames(
    (0, "ACC-RLOAD", "accRlPriority"),
)
if mibBuilder.loadTexts:
    accRlSourceEntry.setStatus("mandatory")
_AccRlHostAddr_Type = IpAddress
_AccRlHostAddr_Object = MibTableColumn
accRlHostAddr = _AccRlHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 1),
    _AccRlHostAddr_Type()
)
accRlHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlHostAddr.setStatus("mandatory")
_AccRlFilename_Type = DisplayString
_AccRlFilename_Object = MibTableColumn
accRlFilename = _AccRlFilename_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 2),
    _AccRlFilename_Type()
)
accRlFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlFilename.setStatus("mandatory")
_AccRlPriority_Type = Integer32
_AccRlPriority_Object = MibTableColumn
accRlPriority = _AccRlPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 3),
    _AccRlPriority_Type()
)
accRlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlPriority.setStatus("mandatory")


class _AccNetload_Type(Integer32):
    """Custom type accNetload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccNetload_Type.__name__ = "Integer32"
_AccNetload_Object = MibScalar
accNetload = _AccNetload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 2),
    _AccNetload_Type()
)
accNetload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNetload.setStatus("mandatory")


class _AccDownload_Type(Integer32):
    """Custom type accDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccDownload_Type.__name__ = "Integer32"
_AccDownload_Object = MibScalar
accDownload = _AccDownload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 3),
    _AccDownload_Type()
)
accDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDownload.setStatus("mandatory")


class _AccPromload_Type(Integer32):
    """Custom type accPromload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccPromload_Type.__name__ = "Integer32"
_AccPromload_Object = MibScalar
accPromload = _AccPromload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 4),
    _AccPromload_Type()
)
accPromload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPromload.setStatus("mandatory")
_AccCfgLoad_ObjectIdentity = ObjectIdentity
accCfgLoad = _AccCfgLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5)
)
_AccCfgHost_Type = IpAddress
_AccCfgHost_Object = MibScalar
accCfgHost = _AccCfgHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 1),
    _AccCfgHost_Type()
)
accCfgHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgHost.setStatus("mandatory")
_AccCfgFile_Type = DisplayString
_AccCfgFile_Object = MibScalar
accCfgFile = _AccCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 2),
    _AccCfgFile_Type()
)
accCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgFile.setStatus("mandatory")


class _AccCfgDisp_Type(Integer32):
    """Custom type accCfgDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("reload", 2),
          ("reset", 1))
    )


_AccCfgDisp_Type.__name__ = "Integer32"
_AccCfgDisp_Object = MibScalar
accCfgDisp = _AccCfgDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 3),
    _AccCfgDisp_Type()
)
accCfgDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgDisp.setStatus("mandatory")
_AccTftpStat_ObjectIdentity = ObjectIdentity
accTftpStat = _AccTftpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6)
)


class _AccTftpStatus_Type(Integer32):
    """Custom type accTftpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 2),
          ("idle", 3),
          ("uploading", 1))
    )


_AccTftpStatus_Type.__name__ = "Integer32"
_AccTftpStatus_Object = MibScalar
accTftpStatus = _AccTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 1),
    _AccTftpStatus_Type()
)
accTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpStatus.setStatus("mandatory")
_AccTftpLocalFile_Type = DisplayString
_AccTftpLocalFile_Object = MibScalar
accTftpLocalFile = _AccTftpLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 2),
    _AccTftpLocalFile_Type()
)
accTftpLocalFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpLocalFile.setStatus("mandatory")
_AccTftpRemoteFile_Type = DisplayString
_AccTftpRemoteFile_Object = MibScalar
accTftpRemoteFile = _AccTftpRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 3),
    _AccTftpRemoteFile_Type()
)
accTftpRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpRemoteFile.setStatus("mandatory")
_AccTftpOctetsTransferred_Type = Integer32
_AccTftpOctetsTransferred_Object = MibScalar
accTftpOctetsTransferred = _AccTftpOctetsTransferred_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 4),
    _AccTftpOctetsTransferred_Type()
)
accTftpOctetsTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpOctetsTransferred.setStatus("mandatory")
_AccTftpLastMsg_Type = DisplayString
_AccTftpLastMsg_Object = MibScalar
accTftpLastMsg = _AccTftpLastMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 5),
    _AccTftpLastMsg_Type()
)
accTftpLastMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpLastMsg.setStatus("mandatory")
_AccTftpCmd_ObjectIdentity = ObjectIdentity
accTftpCmd = _AccTftpCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7)
)


class _AccTftpCmdReq_Type(Integer32):
    """Custom type accTftpCmdReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("get", 1)
    )


_AccTftpCmdReq_Type.__name__ = "Integer32"
_AccTftpCmdReq_Object = MibScalar
accTftpCmdReq = _AccTftpCmdReq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 1),
    _AccTftpCmdReq_Type()
)
accTftpCmdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdReq.setStatus("mandatory")
_AccTftpCmdHost_Type = IpAddress
_AccTftpCmdHost_Object = MibScalar
accTftpCmdHost = _AccTftpCmdHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 2),
    _AccTftpCmdHost_Type()
)
accTftpCmdHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdHost.setStatus("mandatory")
_AccTftpCmdRemote_Type = DisplayString
_AccTftpCmdRemote_Object = MibScalar
accTftpCmdRemote = _AccTftpCmdRemote_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 3),
    _AccTftpCmdRemote_Type()
)
accTftpCmdRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdRemote.setStatus("mandatory")
_AccTftpCmdLocal_Type = DisplayString
_AccTftpCmdLocal_Object = MibScalar
accTftpCmdLocal = _AccTftpCmdLocal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 4),
    _AccTftpCmdLocal_Type()
)
accTftpCmdLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdLocal.setStatus("mandatory")


class _AccTftpCmdForce_Type(Integer32):
    """Custom type accTftpCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overwrite", 1),
          ("safe", 2))
    )


_AccTftpCmdForce_Type.__name__ = "Integer32"
_AccTftpCmdForce_Object = MibScalar
accTftpCmdForce = _AccTftpCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 5),
    _AccTftpCmdForce_Type()
)
accTftpCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTftpCmdForce.setStatus("mandatory")
_AccTftpTraps_ObjectIdentity = ObjectIdentity
accTftpTraps = _AccTftpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8)
)
_AccTftpTrapMsg_Type = DisplayString
_AccTftpTrapMsg_Object = MibScalar
accTftpTrapMsg = _AccTftpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 1),
    _AccTftpTrapMsg_Type()
)
accTftpTrapMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTftpTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accRlodFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 1)
)
accRlodFailTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodFailTrap.setStatus(
        ""
    )

accRlodNofileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 2)
)
accRlodNofileTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodNofileTrap.setStatus(
        ""
    )

accRlodBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 3)
)
accRlodBusyTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodBusyTrap.setStatus(
        ""
    )

accRlodStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 4)
)
accRlodStartTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodStartTrap.setStatus(
        ""
    )

accRlodOpenFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 5)
)
accRlodOpenFailTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodOpenFailTrap.setStatus(
        ""
    )

accRlodWrFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 6)
)
accRlodWrFailTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodWrFailTrap.setStatus(
        ""
    )

accRlodRdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 7)
)
accRlodRdTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodRdTrap.setStatus(
        ""
    )

accRlodDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 8)
)
accRlodDoneTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodDoneTrap.setStatus(
        ""
    )

accRlodBadSumTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 9)
)
accRlodBadSumTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodBadSumTrap.setStatus(
        ""
    )

accRlodCkStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 10)
)
accRlodCkStartTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodCkStartTrap.setStatus(
        ""
    )

accRlodInvFilsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 11)
)
accRlodInvFilsTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodInvFilsTrap.setStatus(
        ""
    )

accRlodBadTypeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 12)
)
accRlodBadTypeTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodBadTypeTrap.setStatus(
        ""
    )

accRlodBadImagTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 13)
)
accRlodBadImagTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodBadImagTrap.setStatus(
        ""
    )

accRlodExceedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 14)
)
accRlodExceedTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodExceedTrap.setStatus(
        ""
    )

accRlodNoHostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 15)
)
accRlodNoHostTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodNoHostTrap.setStatus(
        ""
    )

accRlodValSumTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 16)
)
accRlodValSumTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodValSumTrap.setStatus(
        ""
    )

accRlodFileSysTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 17)
)
accRlodFileSysTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpLocalFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodFileSysTrap.setStatus(
        ""
    )

accRlodSafeFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 18)
)
accRlodSafeFileTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpLocalFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodSafeFileTrap.setStatus(
        ""
    )

accRlodActiveFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 19)
)
accRlodActiveFileTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodActiveFileTrap.setStatus(
        ""
    )

accRlodNoVolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 20)
)
accRlodNoVolTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodNoVolTrap.setStatus(
        ""
    )

accRlodBadFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 21)
)
accRlodBadFileTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpLocalFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodBadFileTrap.setStatus(
        ""
    )

accRlodLongFileNameTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 22)
)
accRlodLongFileNameTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpLocalFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodLongFileNameTrap.setStatus(
        ""
    )

accRlodNoFlashTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 23)
)
accRlodNoFlashTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodNoFlashTrap.setStatus(
        ""
    )

accRlodFilSySBusyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 24)
)
accRlodFilSySBusyTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodFilSySBusyTrap.setStatus(
        ""
    )

accRlodInCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 25)
)
accRlodInCompleteTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodInCompleteTrap.setStatus(
        ""
    )

accRlodAccDeniedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 26)
)
accRlodAccDeniedTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpRemoteFile"),
        ("ACC-RLOAD", "accRlHostAddr"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodAccDeniedTrap.setStatus(
        ""
    )

accRlodSameFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 27)
)
accRlodSameFileTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-RLOAD", "accTftpLocalFile"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodSameFileTrap.setStatus(
        ""
    )

accRlodAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 29)
)
accRlodAbortTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodAbortTrap.setStatus(
        ""
    )

accRlodTimedOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 8, 0, 30)
)
accRlodTimedOutTrap.setObjects(
      *(("ACC-RLOAD", "accTftpTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accRlodTimedOutTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-RLOAD",
    **{"accRload": accRload,
       "accRlSourceTable": accRlSourceTable,
       "accRlSourceEntry": accRlSourceEntry,
       "accRlHostAddr": accRlHostAddr,
       "accRlFilename": accRlFilename,
       "accRlPriority": accRlPriority,
       "accNetload": accNetload,
       "accDownload": accDownload,
       "accPromload": accPromload,
       "accCfgLoad": accCfgLoad,
       "accCfgHost": accCfgHost,
       "accCfgFile": accCfgFile,
       "accCfgDisp": accCfgDisp,
       "accTftpStat": accTftpStat,
       "accTftpStatus": accTftpStatus,
       "accTftpLocalFile": accTftpLocalFile,
       "accTftpRemoteFile": accTftpRemoteFile,
       "accTftpOctetsTransferred": accTftpOctetsTransferred,
       "accTftpLastMsg": accTftpLastMsg,
       "accTftpCmd": accTftpCmd,
       "accTftpCmdReq": accTftpCmdReq,
       "accTftpCmdHost": accTftpCmdHost,
       "accTftpCmdRemote": accTftpCmdRemote,
       "accTftpCmdLocal": accTftpCmdLocal,
       "accTftpCmdForce": accTftpCmdForce,
       "accTftpTraps": accTftpTraps,
       "accRlodFailTrap": accRlodFailTrap,
       "accRlodNofileTrap": accRlodNofileTrap,
       "accRlodBusyTrap": accRlodBusyTrap,
       "accRlodStartTrap": accRlodStartTrap,
       "accRlodOpenFailTrap": accRlodOpenFailTrap,
       "accRlodWrFailTrap": accRlodWrFailTrap,
       "accRlodRdTrap": accRlodRdTrap,
       "accRlodDoneTrap": accRlodDoneTrap,
       "accRlodBadSumTrap": accRlodBadSumTrap,
       "accRlodCkStartTrap": accRlodCkStartTrap,
       "accRlodInvFilsTrap": accRlodInvFilsTrap,
       "accRlodBadTypeTrap": accRlodBadTypeTrap,
       "accRlodBadImagTrap": accRlodBadImagTrap,
       "accRlodExceedTrap": accRlodExceedTrap,
       "accRlodNoHostTrap": accRlodNoHostTrap,
       "accRlodValSumTrap": accRlodValSumTrap,
       "accRlodFileSysTrap": accRlodFileSysTrap,
       "accRlodSafeFileTrap": accRlodSafeFileTrap,
       "accRlodActiveFileTrap": accRlodActiveFileTrap,
       "accRlodNoVolTrap": accRlodNoVolTrap,
       "accRlodBadFileTrap": accRlodBadFileTrap,
       "accRlodLongFileNameTrap": accRlodLongFileNameTrap,
       "accRlodNoFlashTrap": accRlodNoFlashTrap,
       "accRlodFilSySBusyTrap": accRlodFilSySBusyTrap,
       "accRlodInCompleteTrap": accRlodInCompleteTrap,
       "accRlodAccDeniedTrap": accRlodAccDeniedTrap,
       "accRlodSameFileTrap": accRlodSameFileTrap,
       "accRlodAbortTrap": accRlodAbortTrap,
       "accRlodTimedOutTrap": accRlodTimedOutTrap,
       "accTftpTrapMsg": accTftpTrapMsg}
)
