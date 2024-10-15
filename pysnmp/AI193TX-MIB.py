# SNMP MIB module (AI193TX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AI193TX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:04 2024
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

aiTX1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_Ai193_ObjectIdentity = ObjectIdentity
ai193 = _Ai193_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193)
)
_Ai193Ver7_ObjectIdentity = ObjectIdentity
ai193Ver7 = _Ai193Ver7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7)
)
_Ai193Ver71_ObjectIdentity = ObjectIdentity
ai193Ver71 = _Ai193Ver71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 1)
)
_Ai193Ver72_ObjectIdentity = ObjectIdentity
ai193Ver72 = _Ai193Ver72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 2)
)
_Ai193Ver73_ObjectIdentity = ObjectIdentity
ai193Ver73 = _Ai193Ver73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 3)
)
_Ai193Ver74_ObjectIdentity = ObjectIdentity
ai193Ver74 = _Ai193Ver74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 4)
)
_Ai193Ver75_ObjectIdentity = ObjectIdentity
ai193Ver75 = _Ai193Ver75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 5)
)
_Ai193Ver76_ObjectIdentity = ObjectIdentity
ai193Ver76 = _Ai193Ver76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 6)
)
_Ai193Ver77_ObjectIdentity = ObjectIdentity
ai193Ver77 = _Ai193Ver77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 7)
)
_Ai193Ver78_ObjectIdentity = ObjectIdentity
ai193Ver78 = _Ai193Ver78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 8)
)
_Ai193Ver79_ObjectIdentity = ObjectIdentity
ai193Ver79 = _Ai193Ver79_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 9)
)
_Ai193Ver710_ObjectIdentity = ObjectIdentity
ai193Ver710 = _Ai193Ver710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 193, 7, 10)
)
_AiTX1System_ObjectIdentity = ObjectIdentity
aiTX1System = _AiTX1System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14, 1)
)


class _AiTX1Interface_Type(Integer32):
    """Custom type aiTX1Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frontpanel", 2),
          ("irb", 1))
    )


_AiTX1Interface_Type.__name__ = "Integer32"
_AiTX1Interface_Object = MibScalar
aiTX1Interface = _AiTX1Interface_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 1, 1),
    _AiTX1Interface_Type()
)
aiTX1Interface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1Interface.setStatus("mandatory")
_AiTX1Calls_ObjectIdentity = ObjectIdentity
aiTX1Calls = _AiTX1Calls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 14, 2)
)
_AiTX1NumCalls_Type = Integer32
_AiTX1NumCalls_Object = MibScalar
aiTX1NumCalls = _AiTX1NumCalls_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 1),
    _AiTX1NumCalls_Type()
)
aiTX1NumCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1NumCalls.setStatus("mandatory")
_AiTX1CallTable_Object = MibTable
aiTX1CallTable = _AiTX1CallTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2)
)
if mibBuilder.loadTexts:
    aiTX1CallTable.setStatus("mandatory")
_AiTX1CallTableEntry_Object = MibTableRow
aiTX1CallTableEntry = _AiTX1CallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1)
)
aiTX1CallTableEntry.setIndexNames(
    (0, "AI193TX-MIB", "aiTX1CallIndex"),
)
if mibBuilder.loadTexts:
    aiTX1CallTableEntry.setStatus("mandatory")
_AiTX1CallIndex_Type = Integer32
_AiTX1CallIndex_Object = MibTableColumn
aiTX1CallIndex = _AiTX1CallIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 1),
    _AiTX1CallIndex_Type()
)
aiTX1CallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallIndex.setStatus("mandatory")


class _AiTX1CallStatus_Type(Integer32):
    """Custom type aiTX1CallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 9))
    )


_AiTX1CallStatus_Type.__name__ = "Integer32"
_AiTX1CallStatus_Object = MibTableColumn
aiTX1CallStatus = _AiTX1CallStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 2),
    _AiTX1CallStatus_Type()
)
aiTX1CallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallStatus.setStatus("mandatory")


class _AiTX1CallSource_Type(Integer32):
    """Custom type aiTX1CallSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2))
    )


_AiTX1CallSource_Type.__name__ = "Integer32"
_AiTX1CallSource_Object = MibTableColumn
aiTX1CallSource = _AiTX1CallSource_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 3),
    _AiTX1CallSource_Type()
)
aiTX1CallSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallSource.setStatus("mandatory")
_AiTX1CallSrcAddress_Type = IpAddress
_AiTX1CallSrcAddress_Object = MibTableColumn
aiTX1CallSrcAddress = _AiTX1CallSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 4),
    _AiTX1CallSrcAddress_Type()
)
aiTX1CallSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallSrcAddress.setStatus("mandatory")
_AiTX1CallDestAddress_Type = IpAddress
_AiTX1CallDestAddress_Object = MibTableColumn
aiTX1CallDestAddress = _AiTX1CallDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 5),
    _AiTX1CallDestAddress_Type()
)
aiTX1CallDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallDestAddress.setStatus("mandatory")
_AiTX1CallPacketsSent_Type = Integer32
_AiTX1CallPacketsSent_Object = MibTableColumn
aiTX1CallPacketsSent = _AiTX1CallPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 6),
    _AiTX1CallPacketsSent_Type()
)
aiTX1CallPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallPacketsSent.setStatus("mandatory")
_AiTX1CallPktsRcvd_Type = Integer32
_AiTX1CallPktsRcvd_Object = MibTableColumn
aiTX1CallPktsRcvd = _AiTX1CallPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 7),
    _AiTX1CallPktsRcvd_Type()
)
aiTX1CallPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallPktsRcvd.setStatus("mandatory")
_AiTX1CalledPort_Type = Integer32
_AiTX1CalledPort_Object = MibTableColumn
aiTX1CalledPort = _AiTX1CalledPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 8),
    _AiTX1CalledPort_Type()
)
aiTX1CalledPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CalledPort.setStatus("mandatory")
_AiTX1CallingPort_Type = Integer32
_AiTX1CallingPort_Object = MibTableColumn
aiTX1CallingPort = _AiTX1CallingPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 9),
    _AiTX1CallingPort_Type()
)
aiTX1CallingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallingPort.setStatus("mandatory")
_AiTX1CallUserData_Type = DisplayString
_AiTX1CallUserData_Object = MibTableColumn
aiTX1CallUserData = _AiTX1CallUserData_Object(
    (1, 3, 6, 1, 4, 1, 539, 14, 2, 2, 1, 10),
    _AiTX1CallUserData_Type()
)
aiTX1CallUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiTX1CallUserData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AI193TX-MIB",
    **{"aii": aii,
       "aiSystemOID": aiSystemOID,
       "ai193": ai193,
       "ai193Ver7": ai193Ver7,
       "ai193Ver71": ai193Ver71,
       "ai193Ver72": ai193Ver72,
       "ai193Ver73": ai193Ver73,
       "ai193Ver74": ai193Ver74,
       "ai193Ver75": ai193Ver75,
       "ai193Ver76": ai193Ver76,
       "ai193Ver77": ai193Ver77,
       "ai193Ver78": ai193Ver78,
       "ai193Ver79": ai193Ver79,
       "ai193Ver710": ai193Ver710,
       "aiTX1": aiTX1,
       "aiTX1System": aiTX1System,
       "aiTX1Interface": aiTX1Interface,
       "aiTX1Calls": aiTX1Calls,
       "aiTX1NumCalls": aiTX1NumCalls,
       "aiTX1CallTable": aiTX1CallTable,
       "aiTX1CallTableEntry": aiTX1CallTableEntry,
       "aiTX1CallIndex": aiTX1CallIndex,
       "aiTX1CallStatus": aiTX1CallStatus,
       "aiTX1CallSource": aiTX1CallSource,
       "aiTX1CallSrcAddress": aiTX1CallSrcAddress,
       "aiTX1CallDestAddress": aiTX1CallDestAddress,
       "aiTX1CallPacketsSent": aiTX1CallPacketsSent,
       "aiTX1CallPktsRcvd": aiTX1CallPktsRcvd,
       "aiTX1CalledPort": aiTX1CalledPort,
       "aiTX1CallingPort": aiTX1CallingPort,
       "aiTX1CallUserData": aiTX1CallUserData}
)
