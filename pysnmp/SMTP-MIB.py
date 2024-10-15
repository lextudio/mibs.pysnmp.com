# SNMP MIB module (SMTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SMTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:40 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swSMTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 29)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSMTPCtrl_ObjectIdentity = ObjectIdentity
swSMTPCtrl = _SwSMTPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1)
)


class _SmtpStatus_Type(Integer32):
    """Custom type smtpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SmtpStatus_Type.__name__ = "Integer32"
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("current")
_SmtpSrvAddr_Type = IpAddress
_SmtpSrvAddr_Object = MibScalar
smtpSrvAddr = _SmtpSrvAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 2),
    _SmtpSrvAddr_Type()
)
smtpSrvAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSrvAddr.setStatus("current")


class _SmtpSrvPort_Type(Integer32):
    """Custom type smtpSrvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SmtpSrvPort_Type.__name__ = "Integer32"
_SmtpSrvPort_Object = MibScalar
smtpSrvPort = _SmtpSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 3),
    _SmtpSrvPort_Type()
)
smtpSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSrvPort.setStatus("current")


class _SmtpSelfMailAddr_Type(DisplayString):
    """Custom type smtpSelfMailAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SmtpSelfMailAddr_Type.__name__ = "DisplayString"
_SmtpSelfMailAddr_Object = MibScalar
smtpSelfMailAddr = _SmtpSelfMailAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 4),
    _SmtpSelfMailAddr_Type()
)
smtpSelfMailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSelfMailAddr.setStatus("current")


class _SmtpTestMsgSubject_Type(DisplayString):
    """Custom type smtpTestMsgSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SmtpTestMsgSubject_Type.__name__ = "DisplayString"
_SmtpTestMsgSubject_Object = MibScalar
smtpTestMsgSubject = _SmtpTestMsgSubject_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 5),
    _SmtpTestMsgSubject_Type()
)
smtpTestMsgSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTestMsgSubject.setStatus("current")


class _SmtpTestMsgContent_Type(DisplayString):
    """Custom type smtpTestMsgContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SmtpTestMsgContent_Type.__name__ = "DisplayString"
_SmtpTestMsgContent_Object = MibScalar
smtpTestMsgContent = _SmtpTestMsgContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 6),
    _SmtpTestMsgContent_Type()
)
smtpTestMsgContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpTestMsgContent.setStatus("current")


class _SmtpSendTestMsg_Type(Integer32):
    """Custom type smtpSendTestMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("send", 1))
    )


_SmtpSendTestMsg_Type.__name__ = "Integer32"
_SmtpSendTestMsg_Object = MibScalar
smtpSendTestMsg = _SmtpSendTestMsg_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 7),
    _SmtpSendTestMsg_Type()
)
smtpSendTestMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSendTestMsg.setStatus("current")
_SwSMTPInfo_ObjectIdentity = ObjectIdentity
swSMTPInfo = _SwSMTPInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 2)
)


class _SmtpSendTestStatus_Type(Integer32):
    """Custom type smtpSendTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("in-processing", 3),
          ("success", 1))
    )


_SmtpSendTestStatus_Type.__name__ = "Integer32"
_SmtpSendTestStatus_Object = MibScalar
smtpSendTestStatus = _SmtpSendTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 2, 1),
    _SmtpSendTestStatus_Type()
)
smtpSendTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpSendTestStatus.setStatus("current")
_SwSMTPMgmt_ObjectIdentity = ObjectIdentity
swSMTPMgmt = _SwSMTPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3)
)
_SmtpMailReceiverTable_Object = MibTable
smtpMailReceiverTable = _SmtpMailReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1)
)
if mibBuilder.loadTexts:
    smtpMailReceiverTable.setStatus("current")
_SmtpReceiverAddrEntry_Object = MibTableRow
smtpReceiverAddrEntry = _SmtpReceiverAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1)
)
smtpReceiverAddrEntry.setIndexNames(
    (0, "SMTP-MIB", "smtpMailReceiverAddrIndex"),
)
if mibBuilder.loadTexts:
    smtpReceiverAddrEntry.setStatus("current")


class _SmtpMailReceiverAddrIndex_Type(Integer32):
    """Custom type smtpMailReceiverAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SmtpMailReceiverAddrIndex_Type.__name__ = "Integer32"
_SmtpMailReceiverAddrIndex_Object = MibTableColumn
smtpMailReceiverAddrIndex = _SmtpMailReceiverAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 1),
    _SmtpMailReceiverAddrIndex_Type()
)
smtpMailReceiverAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpMailReceiverAddrIndex.setStatus("current")


class _SmtpMailReceiverAddr_Type(DisplayString):
    """Custom type smtpMailReceiverAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SmtpMailReceiverAddr_Type.__name__ = "DisplayString"
_SmtpMailReceiverAddr_Object = MibTableColumn
smtpMailReceiverAddr = _SmtpMailReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 2),
    _SmtpMailReceiverAddr_Type()
)
smtpMailReceiverAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpMailReceiverAddr.setStatus("current")
_SmtpMailReceiverAddrState_Type = RowStatus
_SmtpMailReceiverAddrState_Object = MibTableColumn
smtpMailReceiverAddrState = _SmtpMailReceiverAddrState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 3),
    _SmtpMailReceiverAddrState_Type()
)
smtpMailReceiverAddrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpMailReceiverAddrState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMTP-MIB",
    **{"VlanId": VlanId,
       "PortList": PortList,
       "MacAddress": MacAddress,
       "swSMTPMIB": swSMTPMIB,
       "swSMTPCtrl": swSMTPCtrl,
       "smtpStatus": smtpStatus,
       "smtpSrvAddr": smtpSrvAddr,
       "smtpSrvPort": smtpSrvPort,
       "smtpSelfMailAddr": smtpSelfMailAddr,
       "smtpTestMsgSubject": smtpTestMsgSubject,
       "smtpTestMsgContent": smtpTestMsgContent,
       "smtpSendTestMsg": smtpSendTestMsg,
       "swSMTPInfo": swSMTPInfo,
       "smtpSendTestStatus": smtpSendTestStatus,
       "swSMTPMgmt": swSMTPMgmt,
       "smtpMailReceiverTable": smtpMailReceiverTable,
       "smtpReceiverAddrEntry": smtpReceiverAddrEntry,
       "smtpMailReceiverAddrIndex": smtpMailReceiverAddrIndex,
       "smtpMailReceiverAddr": smtpMailReceiverAddr,
       "smtpMailReceiverAddrState": smtpMailReceiverAddrState}
)
