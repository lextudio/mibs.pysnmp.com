# SNMP MIB module (IPFWADM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFWADM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:53 2024
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

(ucdExperimental,
 ucdavis) = mibBuilder.importSymbols(
    "UCD-SNMP-MIB",
    "ucdExperimental",
    "ucdavis")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpFwAccTable_Object = MibTable
ipFwAccTable = _IpFwAccTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1)
)
if mibBuilder.loadTexts:
    ipFwAccTable.setStatus("mandatory")
_IpFwAccEntry_Object = MibTableRow
ipFwAccEntry = _IpFwAccEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1)
)
ipFwAccEntry.setIndexNames(
    (0, "IPFWADM-MIB", "ipFwAccIndex"),
)
if mibBuilder.loadTexts:
    ipFwAccEntry.setStatus("mandatory")
_IpFwAccIndex_Type = Integer32
_IpFwAccIndex_Object = MibTableColumn
ipFwAccIndex = _IpFwAccIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 1),
    _IpFwAccIndex_Type()
)
ipFwAccIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccIndex.setStatus("mandatory")
_IpFwAccSrcAddr_Type = IpAddress
_IpFwAccSrcAddr_Object = MibTableColumn
ipFwAccSrcAddr = _IpFwAccSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 2),
    _IpFwAccSrcAddr_Type()
)
ipFwAccSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcAddr.setStatus("mandatory")
_IpFwAccSrcNetMask_Type = IpAddress
_IpFwAccSrcNetMask_Object = MibTableColumn
ipFwAccSrcNetMask = _IpFwAccSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 3),
    _IpFwAccSrcNetMask_Type()
)
ipFwAccSrcNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcNetMask.setStatus("mandatory")
_IpFwAccDstAddr_Type = IpAddress
_IpFwAccDstAddr_Object = MibTableColumn
ipFwAccDstAddr = _IpFwAccDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 4),
    _IpFwAccDstAddr_Type()
)
ipFwAccDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstAddr.setStatus("mandatory")
_IpFwAccDstNetMask_Type = IpAddress
_IpFwAccDstNetMask_Object = MibTableColumn
ipFwAccDstNetMask = _IpFwAccDstNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 5),
    _IpFwAccDstNetMask_Type()
)
ipFwAccDstNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstNetMask.setStatus("mandatory")
_IpFwAccViaName_Type = DisplayString
_IpFwAccViaName_Object = MibTableColumn
ipFwAccViaName = _IpFwAccViaName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 6),
    _IpFwAccViaName_Type()
)
ipFwAccViaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccViaName.setStatus("mandatory")
_IpFwAccViaAddr_Type = IpAddress
_IpFwAccViaAddr_Object = MibTableColumn
ipFwAccViaAddr = _IpFwAccViaAddr_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 7),
    _IpFwAccViaAddr_Type()
)
ipFwAccViaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccViaAddr.setStatus("mandatory")


class _IpFwAccProto_Type(Integer32):
    """Custom type ipFwAccProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("icmp", 5),
          ("other", 1),
          ("tcp", 3),
          ("udp", 4))
    )


_IpFwAccProto_Type.__name__ = "Integer32"
_IpFwAccProto_Object = MibTableColumn
ipFwAccProto = _IpFwAccProto_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 8),
    _IpFwAccProto_Type()
)
ipFwAccProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccProto.setStatus("mandatory")


class _IpFwAccBidir_Type(Integer32):
    """Custom type ipFwAccBidir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 2),
          ("unidirectional", 1))
    )


_IpFwAccBidir_Type.__name__ = "Integer32"
_IpFwAccBidir_Object = MibTableColumn
ipFwAccBidir = _IpFwAccBidir_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 9),
    _IpFwAccBidir_Type()
)
ipFwAccBidir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccBidir.setStatus("mandatory")


class _IpFwAccDir_Type(Integer32):
    """Custom type ipFwAccDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("in", 2),
          ("out", 3))
    )


_IpFwAccDir_Type.__name__ = "Integer32"
_IpFwAccDir_Object = MibTableColumn
ipFwAccDir = _IpFwAccDir_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 10),
    _IpFwAccDir_Type()
)
ipFwAccDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDir.setStatus("mandatory")
_IpFwAccBytes_Type = Counter32
_IpFwAccBytes_Object = MibTableColumn
ipFwAccBytes = _IpFwAccBytes_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 11),
    _IpFwAccBytes_Type()
)
ipFwAccBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccBytes.setStatus("mandatory")
_IpFwAccPackets_Type = Counter32
_IpFwAccPackets_Object = MibTableColumn
ipFwAccPackets = _IpFwAccPackets_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 12),
    _IpFwAccPackets_Type()
)
ipFwAccPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPackets.setStatus("mandatory")
_IpFwAccNrSrcPorts_Type = Integer32
_IpFwAccNrSrcPorts_Object = MibTableColumn
ipFwAccNrSrcPorts = _IpFwAccNrSrcPorts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 13),
    _IpFwAccNrSrcPorts_Type()
)
ipFwAccNrSrcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccNrSrcPorts.setStatus("mandatory")
_IpFwAccNrDstPorts_Type = Integer32
_IpFwAccNrDstPorts_Object = MibTableColumn
ipFwAccNrDstPorts = _IpFwAccNrDstPorts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 14),
    _IpFwAccNrDstPorts_Type()
)
ipFwAccNrDstPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccNrDstPorts.setStatus("mandatory")


class _IpFwAccSrcIsRange_Type(Integer32):
    """Custom type ipFwAccSrcIsRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srchasnorange", 2),
          ("srchasrange", 1))
    )


_IpFwAccSrcIsRange_Type.__name__ = "Integer32"
_IpFwAccSrcIsRange_Object = MibTableColumn
ipFwAccSrcIsRange = _IpFwAccSrcIsRange_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 15),
    _IpFwAccSrcIsRange_Type()
)
ipFwAccSrcIsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccSrcIsRange.setStatus("mandatory")


class _IpFwAccDstIsRange_Type(Integer32):
    """Custom type ipFwAccDstIsRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsthasnorange", 2),
          ("dsthasrange", 1))
    )


_IpFwAccDstIsRange_Type.__name__ = "Integer32"
_IpFwAccDstIsRange_Object = MibTableColumn
ipFwAccDstIsRange = _IpFwAccDstIsRange_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 16),
    _IpFwAccDstIsRange_Type()
)
ipFwAccDstIsRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccDstIsRange.setStatus("mandatory")
_IpFwAccPort1_Type = Integer32
_IpFwAccPort1_Object = MibTableColumn
ipFwAccPort1 = _IpFwAccPort1_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 17),
    _IpFwAccPort1_Type()
)
ipFwAccPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort1.setStatus("mandatory")
_IpFwAccPort2_Type = Integer32
_IpFwAccPort2_Object = MibTableColumn
ipFwAccPort2 = _IpFwAccPort2_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 18),
    _IpFwAccPort2_Type()
)
ipFwAccPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort2.setStatus("mandatory")
_IpFwAccPort3_Type = Integer32
_IpFwAccPort3_Object = MibTableColumn
ipFwAccPort3 = _IpFwAccPort3_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 19),
    _IpFwAccPort3_Type()
)
ipFwAccPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort3.setStatus("mandatory")
_IpFwAccPort4_Type = Integer32
_IpFwAccPort4_Object = MibTableColumn
ipFwAccPort4 = _IpFwAccPort4_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 20),
    _IpFwAccPort4_Type()
)
ipFwAccPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort4.setStatus("mandatory")
_IpFwAccPort5_Type = Integer32
_IpFwAccPort5_Object = MibTableColumn
ipFwAccPort5 = _IpFwAccPort5_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 21),
    _IpFwAccPort5_Type()
)
ipFwAccPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort5.setStatus("mandatory")
_IpFwAccPort6_Type = Integer32
_IpFwAccPort6_Object = MibTableColumn
ipFwAccPort6 = _IpFwAccPort6_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 22),
    _IpFwAccPort6_Type()
)
ipFwAccPort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort6.setStatus("mandatory")
_IpFwAccPort7_Type = Integer32
_IpFwAccPort7_Object = MibTableColumn
ipFwAccPort7 = _IpFwAccPort7_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 23),
    _IpFwAccPort7_Type()
)
ipFwAccPort7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort7.setStatus("mandatory")
_IpFwAccPort8_Type = Integer32
_IpFwAccPort8_Object = MibTableColumn
ipFwAccPort8 = _IpFwAccPort8_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 24),
    _IpFwAccPort8_Type()
)
ipFwAccPort8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort8.setStatus("mandatory")
_IpFwAccPort9_Type = Integer32
_IpFwAccPort9_Object = MibTableColumn
ipFwAccPort9 = _IpFwAccPort9_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 25),
    _IpFwAccPort9_Type()
)
ipFwAccPort9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort9.setStatus("mandatory")
_IpFwAccPort10_Type = Integer32
_IpFwAccPort10_Object = MibTableColumn
ipFwAccPort10 = _IpFwAccPort10_Object(
    (1, 3, 6, 1, 4, 1, 2021, 13, 1, 1, 26),
    _IpFwAccPort10_Type()
)
ipFwAccPort10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFwAccPort10.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFWADM-MIB",
    **{"ipFwAccTable": ipFwAccTable,
       "ipFwAccEntry": ipFwAccEntry,
       "ipFwAccIndex": ipFwAccIndex,
       "ipFwAccSrcAddr": ipFwAccSrcAddr,
       "ipFwAccSrcNetMask": ipFwAccSrcNetMask,
       "ipFwAccDstAddr": ipFwAccDstAddr,
       "ipFwAccDstNetMask": ipFwAccDstNetMask,
       "ipFwAccViaName": ipFwAccViaName,
       "ipFwAccViaAddr": ipFwAccViaAddr,
       "ipFwAccProto": ipFwAccProto,
       "ipFwAccBidir": ipFwAccBidir,
       "ipFwAccDir": ipFwAccDir,
       "ipFwAccBytes": ipFwAccBytes,
       "ipFwAccPackets": ipFwAccPackets,
       "ipFwAccNrSrcPorts": ipFwAccNrSrcPorts,
       "ipFwAccNrDstPorts": ipFwAccNrDstPorts,
       "ipFwAccSrcIsRange": ipFwAccSrcIsRange,
       "ipFwAccDstIsRange": ipFwAccDstIsRange,
       "ipFwAccPort1": ipFwAccPort1,
       "ipFwAccPort2": ipFwAccPort2,
       "ipFwAccPort3": ipFwAccPort3,
       "ipFwAccPort4": ipFwAccPort4,
       "ipFwAccPort5": ipFwAccPort5,
       "ipFwAccPort6": ipFwAccPort6,
       "ipFwAccPort7": ipFwAccPort7,
       "ipFwAccPort8": ipFwAccPort8,
       "ipFwAccPort9": ipFwAccPort9,
       "ipFwAccPort10": ipFwAccPort10}
)
