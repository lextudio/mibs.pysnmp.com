# SNMP MIB module (GBNPlatformOAMMailalarm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GBNPlatformOAMMailalarm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:47:54 2024
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

(gbnPlatformOAM,) = mibBuilder.importSymbols(
    "GBNPlatformOAM-MIB",
    "gbnPlatformOAM")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnPlatformOAMMailalarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12)
)
gbnPlatformOAMMailalarm.setRevisions(
        ("1905-07-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _MailalarmState_Type(Integer32):
    """Custom type mailalarmState based on Integer32"""
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


_MailalarmState_Type.__name__ = "Integer32"
_MailalarmState_Object = MibScalar
mailalarmState = _MailalarmState_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 1),
    _MailalarmState_Type()
)
mailalarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmState.setStatus("current")
_MailalarmSrvAddr_Type = IpAddress
_MailalarmSrvAddr_Object = MibScalar
mailalarmSrvAddr = _MailalarmSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 2),
    _MailalarmSrvAddr_Type()
)
mailalarmSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmSrvAddr.setStatus("current")


class _MailalarmRceiverAddr_Type(OctetString):
    """Custom type mailalarmRceiverAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MailalarmRceiverAddr_Type.__name__ = "OctetString"
_MailalarmRceiverAddr_Object = MibScalar
mailalarmRceiverAddr = _MailalarmRceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 3),
    _MailalarmRceiverAddr_Type()
)
mailalarmRceiverAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmRceiverAddr.setStatus("current")


class _MailalarmLogLevel_Type(Integer32):
    """Custom type mailalarmLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MailalarmLogLevel_Type.__name__ = "Integer32"
_MailalarmLogLevel_Object = MibScalar
mailalarmLogLevel = _MailalarmLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 4),
    _MailalarmLogLevel_Type()
)
mailalarmLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmLogLevel.setStatus("current")


class _MailalarmSmtpAuthEnable_Type(Integer32):
    """Custom type mailalarmSmtpAuthEnable based on Integer32"""
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


_MailalarmSmtpAuthEnable_Type.__name__ = "Integer32"
_MailalarmSmtpAuthEnable_Object = MibScalar
mailalarmSmtpAuthEnable = _MailalarmSmtpAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 5),
    _MailalarmSmtpAuthEnable_Type()
)
mailalarmSmtpAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmSmtpAuthEnable.setStatus("current")


class _MailalarmSmtpUsername_Type(OctetString):
    """Custom type mailalarmSmtpUsername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MailalarmSmtpUsername_Type.__name__ = "OctetString"
_MailalarmSmtpUsername_Object = MibScalar
mailalarmSmtpUsername = _MailalarmSmtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 6),
    _MailalarmSmtpUsername_Type()
)
mailalarmSmtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmSmtpUsername.setStatus("current")


class _MailalarmSmtpPasswd_Type(OctetString):
    """Custom type mailalarmSmtpPasswd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MailalarmSmtpPasswd_Type.__name__ = "OctetString"
_MailalarmSmtpPasswd_Object = MibScalar
mailalarmSmtpPasswd = _MailalarmSmtpPasswd_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 7),
    _MailalarmSmtpPasswd_Type()
)
mailalarmSmtpPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmSmtpPasswd.setStatus("current")
_MailalarmCcAddrTable_Object = MibTable
mailalarmCcAddrTable = _MailalarmCcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 8)
)
if mibBuilder.loadTexts:
    mailalarmCcAddrTable.setStatus("current")
_MailalarmCcAddrEntry_Object = MibTableRow
mailalarmCcAddrEntry = _MailalarmCcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 8, 1)
)
mailalarmCcAddrEntry.setIndexNames(
    (0, "GBNPlatformOAMMailalarm-MIB", "mailalarmCcAddrIdx"),
)
if mibBuilder.loadTexts:
    mailalarmCcAddrEntry.setStatus("current")


class _MailalarmCcAddrIdx_Type(Integer32):
    """Custom type mailalarmCcAddrIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_MailalarmCcAddrIdx_Type.__name__ = "Integer32"
_MailalarmCcAddrIdx_Object = MibTableColumn
mailalarmCcAddrIdx = _MailalarmCcAddrIdx_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 8, 1, 1),
    _MailalarmCcAddrIdx_Type()
)
mailalarmCcAddrIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mailalarmCcAddrIdx.setStatus("current")


class _MailalarmCcAddr_Type(OctetString):
    """Custom type mailalarmCcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_MailalarmCcAddr_Type.__name__ = "OctetString"
_MailalarmCcAddr_Object = MibTableColumn
mailalarmCcAddr = _MailalarmCcAddr_Object(
    (1, 3, 6, 1, 4, 1, 13464, 1, 2, 1, 1, 12, 8, 1, 2),
    _MailalarmCcAddr_Type()
)
mailalarmCcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mailalarmCcAddr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GBNPlatformOAMMailalarm-MIB",
    **{"gbnPlatformOAMMailalarm": gbnPlatformOAMMailalarm,
       "mailalarmState": mailalarmState,
       "mailalarmSrvAddr": mailalarmSrvAddr,
       "mailalarmRceiverAddr": mailalarmRceiverAddr,
       "mailalarmLogLevel": mailalarmLogLevel,
       "mailalarmSmtpAuthEnable": mailalarmSmtpAuthEnable,
       "mailalarmSmtpUsername": mailalarmSmtpUsername,
       "mailalarmSmtpPasswd": mailalarmSmtpPasswd,
       "mailalarmCcAddrTable": mailalarmCcAddrTable,
       "mailalarmCcAddrEntry": mailalarmCcAddrEntry,
       "mailalarmCcAddrIdx": mailalarmCcAddrIdx,
       "mailalarmCcAddr": mailalarmCcAddr}
)
