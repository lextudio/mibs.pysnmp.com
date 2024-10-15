# SNMP MIB module (BNET-ATM-TOPOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BNET-ATM-TOPOLOGY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:31 2024
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

(VpiInteger,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "VpiInteger")

(s5AtmTop,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5AtmTop")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BnetAtmTopGbl_ObjectIdentity = ObjectIdentity
bnetAtmTopGbl = _BnetAtmTopGbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1)
)


class _BnetAtmTopGblStatus_Type(Integer32):
    """Custom type bnetAtmTopGblStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("topOff", 2),
          ("topOn", 1))
    )


_BnetAtmTopGblStatus_Type.__name__ = "Integer32"
_BnetAtmTopGblStatus_Object = MibScalar
bnetAtmTopGblStatus = _BnetAtmTopGblStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1, 1),
    _BnetAtmTopGblStatus_Type()
)
bnetAtmTopGblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bnetAtmTopGblStatus.setStatus("mandatory")
_BnetAtmTopGblLstChg_Type = TimeTicks
_BnetAtmTopGblLstChg_Object = MibScalar
bnetAtmTopGblLstChg = _BnetAtmTopGblLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1, 2),
    _BnetAtmTopGblLstChg_Type()
)
bnetAtmTopGblLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopGblLstChg.setStatus("mandatory")


class _BnetAtmTopGblCurNum_Type(Integer32):
    """Custom type bnetAtmTopGblCurNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BnetAtmTopGblCurNum_Type.__name__ = "Integer32"
_BnetAtmTopGblCurNum_Object = MibScalar
bnetAtmTopGblCurNum = _BnetAtmTopGblCurNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1, 3),
    _BnetAtmTopGblCurNum_Type()
)
bnetAtmTopGblCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopGblCurNum.setStatus("mandatory")
_BnetAtmTopGblCurMibVer_Type = Integer32
_BnetAtmTopGblCurMibVer_Object = MibScalar
bnetAtmTopGblCurMibVer = _BnetAtmTopGblCurMibVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1, 4),
    _BnetAtmTopGblCurMibVer_Type()
)
bnetAtmTopGblCurMibVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopGblCurMibVer.setStatus("mandatory")


class _BnetAtmTopGblOperStatus_Type(Integer32):
    """Custom type bnetAtmTopGblOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("topOff", 2),
          ("topOn", 1),
          ("topUnavailable", 3))
    )


_BnetAtmTopGblOperStatus_Type.__name__ = "Integer32"
_BnetAtmTopGblOperStatus_Object = MibScalar
bnetAtmTopGblOperStatus = _BnetAtmTopGblOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 1, 5),
    _BnetAtmTopGblOperStatus_Type()
)
bnetAtmTopGblOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopGblOperStatus.setStatus("mandatory")
_BnetAtmTopLinks_ObjectIdentity = ObjectIdentity
bnetAtmTopLinks = _BnetAtmTopLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2)
)
_BnetAtmTopLinksTable_Object = MibTable
bnetAtmTopLinksTable = _BnetAtmTopLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1)
)
if mibBuilder.loadTexts:
    bnetAtmTopLinksTable.setStatus("mandatory")
_BnetAtmTopLinksEntry_Object = MibTableRow
bnetAtmTopLinksEntry = _BnetAtmTopLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1)
)
bnetAtmTopLinksEntry.setIndexNames(
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksSlotNumIndx"),
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksPortNumIndx"),
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksLcnIndx"),
)
if mibBuilder.loadTexts:
    bnetAtmTopLinksEntry.setStatus("mandatory")


class _BnetAtmTopLinksSlotNumIndx_Type(Integer32):
    """Custom type bnetAtmTopLinksSlotNumIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BnetAtmTopLinksSlotNumIndx_Type.__name__ = "Integer32"
_BnetAtmTopLinksSlotNumIndx_Object = MibTableColumn
bnetAtmTopLinksSlotNumIndx = _BnetAtmTopLinksSlotNumIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 1),
    _BnetAtmTopLinksSlotNumIndx_Type()
)
bnetAtmTopLinksSlotNumIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksSlotNumIndx.setStatus("mandatory")


class _BnetAtmTopLinksPortNumIndx_Type(Integer32):
    """Custom type bnetAtmTopLinksPortNumIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BnetAtmTopLinksPortNumIndx_Type.__name__ = "Integer32"
_BnetAtmTopLinksPortNumIndx_Object = MibTableColumn
bnetAtmTopLinksPortNumIndx = _BnetAtmTopLinksPortNumIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 2),
    _BnetAtmTopLinksPortNumIndx_Type()
)
bnetAtmTopLinksPortNumIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPortNumIndx.setStatus("mandatory")
_BnetAtmTopLinksLcnIndx_Type = VpiInteger
_BnetAtmTopLinksLcnIndx_Object = MibTableColumn
bnetAtmTopLinksLcnIndx = _BnetAtmTopLinksLcnIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 3),
    _BnetAtmTopLinksLcnIndx_Type()
)
bnetAtmTopLinksLcnIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksLcnIndx.setStatus("mandatory")


class _BnetAtmTopLinksTopoState_Type(Integer32):
    """Custom type bnetAtmTopLinksTopoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notParticipating", 2),
          ("participating", 3),
          ("unavailable", 1))
    )


_BnetAtmTopLinksTopoState_Type.__name__ = "Integer32"
_BnetAtmTopLinksTopoState_Object = MibTableColumn
bnetAtmTopLinksTopoState = _BnetAtmTopLinksTopoState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 4),
    _BnetAtmTopLinksTopoState_Type()
)
bnetAtmTopLinksTopoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksTopoState.setStatus("mandatory")


class _BnetAtmTopLinksPeerSlotNum_Type(Integer32):
    """Custom type bnetAtmTopLinksPeerSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BnetAtmTopLinksPeerSlotNum_Type.__name__ = "Integer32"
_BnetAtmTopLinksPeerSlotNum_Object = MibTableColumn
bnetAtmTopLinksPeerSlotNum = _BnetAtmTopLinksPeerSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 5),
    _BnetAtmTopLinksPeerSlotNum_Type()
)
bnetAtmTopLinksPeerSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPeerSlotNum.setStatus("mandatory")


class _BnetAtmTopLinksPeerPortNum_Type(Integer32):
    """Custom type bnetAtmTopLinksPeerPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BnetAtmTopLinksPeerPortNum_Type.__name__ = "Integer32"
_BnetAtmTopLinksPeerPortNum_Object = MibTableColumn
bnetAtmTopLinksPeerPortNum = _BnetAtmTopLinksPeerPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 6),
    _BnetAtmTopLinksPeerPortNum_Type()
)
bnetAtmTopLinksPeerPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPeerPortNum.setStatus("mandatory")
_BnetAtmTopLinksPeerIpAddr_Type = IpAddress
_BnetAtmTopLinksPeerIpAddr_Object = MibTableColumn
bnetAtmTopLinksPeerIpAddr = _BnetAtmTopLinksPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 7),
    _BnetAtmTopLinksPeerIpAddr_Type()
)
bnetAtmTopLinksPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPeerIpAddr.setStatus("mandatory")
_BnetAtmTopLinksPeerChassisType_Type = Integer32
_BnetAtmTopLinksPeerChassisType_Object = MibTableColumn
bnetAtmTopLinksPeerChassisType = _BnetAtmTopLinksPeerChassisType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 8),
    _BnetAtmTopLinksPeerChassisType_Type()
)
bnetAtmTopLinksPeerChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPeerChassisType.setStatus("mandatory")
_BnetAtmTopLinksPeerChassisSubType_Type = Integer32
_BnetAtmTopLinksPeerChassisSubType_Object = MibTableColumn
bnetAtmTopLinksPeerChassisSubType = _BnetAtmTopLinksPeerChassisSubType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 1, 1, 9),
    _BnetAtmTopLinksPeerChassisSubType_Type()
)
bnetAtmTopLinksPeerChassisSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksPeerChassisSubType.setStatus("mandatory")


class _BnetAtmTopLinksEosSize_Type(Integer32):
    """Custom type bnetAtmTopLinksEosSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_BnetAtmTopLinksEosSize_Type.__name__ = "Integer32"
_BnetAtmTopLinksEosSize_Object = MibScalar
bnetAtmTopLinksEosSize = _BnetAtmTopLinksEosSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 2),
    _BnetAtmTopLinksEosSize_Type()
)
bnetAtmTopLinksEosSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksEosSize.setStatus("mandatory")
_BnetAtmTopLinksEosTable_Object = MibTable
bnetAtmTopLinksEosTable = _BnetAtmTopLinksEosTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 3)
)
if mibBuilder.loadTexts:
    bnetAtmTopLinksEosTable.setStatus("mandatory")
_BnetAtmTopLinksEosEntry_Object = MibTableRow
bnetAtmTopLinksEosEntry = _BnetAtmTopLinksEosEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 3, 1)
)
bnetAtmTopLinksEosEntry.setIndexNames(
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksSlotNumIndx"),
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksPortNumIndx"),
    (0, "BNET-ATM-TOPOLOGY-MIB", "bnetAtmTopLinksLcnIndx"),
)
if mibBuilder.loadTexts:
    bnetAtmTopLinksEosEntry.setStatus("mandatory")


class _BnetAtmTopLinksEos_Type(OctetString):
    """Custom type bnetAtmTopLinksEos based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_BnetAtmTopLinksEos_Type.__name__ = "OctetString"
_BnetAtmTopLinksEos_Object = MibTableColumn
bnetAtmTopLinksEos = _BnetAtmTopLinksEos_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 14, 2, 3, 1, 1),
    _BnetAtmTopLinksEos_Type()
)
bnetAtmTopLinksEos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bnetAtmTopLinksEos.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BNET-ATM-TOPOLOGY-MIB",
    **{"bnetAtmTopGbl": bnetAtmTopGbl,
       "bnetAtmTopGblStatus": bnetAtmTopGblStatus,
       "bnetAtmTopGblLstChg": bnetAtmTopGblLstChg,
       "bnetAtmTopGblCurNum": bnetAtmTopGblCurNum,
       "bnetAtmTopGblCurMibVer": bnetAtmTopGblCurMibVer,
       "bnetAtmTopGblOperStatus": bnetAtmTopGblOperStatus,
       "bnetAtmTopLinks": bnetAtmTopLinks,
       "bnetAtmTopLinksTable": bnetAtmTopLinksTable,
       "bnetAtmTopLinksEntry": bnetAtmTopLinksEntry,
       "bnetAtmTopLinksSlotNumIndx": bnetAtmTopLinksSlotNumIndx,
       "bnetAtmTopLinksPortNumIndx": bnetAtmTopLinksPortNumIndx,
       "bnetAtmTopLinksLcnIndx": bnetAtmTopLinksLcnIndx,
       "bnetAtmTopLinksTopoState": bnetAtmTopLinksTopoState,
       "bnetAtmTopLinksPeerSlotNum": bnetAtmTopLinksPeerSlotNum,
       "bnetAtmTopLinksPeerPortNum": bnetAtmTopLinksPeerPortNum,
       "bnetAtmTopLinksPeerIpAddr": bnetAtmTopLinksPeerIpAddr,
       "bnetAtmTopLinksPeerChassisType": bnetAtmTopLinksPeerChassisType,
       "bnetAtmTopLinksPeerChassisSubType": bnetAtmTopLinksPeerChassisSubType,
       "bnetAtmTopLinksEosSize": bnetAtmTopLinksEosSize,
       "bnetAtmTopLinksEosTable": bnetAtmTopLinksEosTable,
       "bnetAtmTopLinksEosEntry": bnetAtmTopLinksEosEntry,
       "bnetAtmTopLinksEos": bnetAtmTopLinksEos}
)
