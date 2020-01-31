#
# PySNMP MIB module Nortel-Magellan-Passport-FrameRelayNniTraceMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-Magellan-Passport-FrameRelayNniTraceMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:27:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
frNniIndex, frNni = mibBuilder.importSymbols("Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex", "frNni")
RowStatus, StorageType, DisplayString, RowPointer, Unsigned32 = mibBuilder.importSymbols("Nortel-Magellan-Passport-StandardTextualConventionsMIB", "RowStatus", "StorageType", "DisplayString", "RowPointer", "Unsigned32")
NonReplicated, AsciiString = mibBuilder.importSymbols("Nortel-Magellan-Passport-TextualConventionsMIB", "NonReplicated", "AsciiString")
passportMIBs, = mibBuilder.importSymbols("Nortel-Magellan-Passport-UsefulDefinitionsMIB", "passportMIBs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity, Integer32, Counter64, MibIdentifier, Unsigned32, Gauge32, iso, ModuleIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity", "Integer32", "Counter64", "MibIdentifier", "Unsigned32", "Gauge32", "iso", "ModuleIdentity", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
frameRelayNniTraceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106))
frNniTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7))
frNniTraceRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1), )
if mibBuilder.loadTexts: frNniTraceRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceRowStatusTable.setDescription('This entry controls the addition and deletion of frNniTrace components.')
frNniTraceRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"))
if mibBuilder.loadTexts: frNniTraceRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceRowStatusEntry.setDescription('A single entry in the table represents a single frNniTrace component.')
frNniTraceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceRowStatus.setDescription('This variable is used as the basis for SNMP naming of frNniTrace components. These components can be added and deleted.')
frNniTraceComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
frNniTraceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceStorageType.setDescription('This variable represents the storage type value for the frNniTrace tables.')
frNniTraceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: frNniTraceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceIndex.setDescription('This variable represents the index for the frNniTrace tables.')
frNniTraceOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10), )
if mibBuilder.loadTexts: frNniTraceOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceOperationalTable.setDescription('This group provides the operational attributes for the Trace component.')
frNniTraceOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"))
if mibBuilder.loadTexts: frNniTraceOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceOperationalEntry.setDescription('An entry in the frNniTraceOperationalTable.')
frNniTraceReceiverName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 2), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceReceiverName.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceReceiverName.setDescription('This attribute should be set to the name of the desired trace receiver before starting a trace session. All available trace receivers are listed under the Trace Rcvr/<string> component. This attribute cannot be set while a trace is active.')
frNniTraceDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceDuration.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceDuration.setDescription('This attribute specifies the duration, in minutes, of a trace session. A value of 0 indicates unlimited duration in which case a trace session remains active until a stop command is issued. The default duration is 60 minutes. This attribute cannot be set while a trace is active.')
frNniTraceQueueLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceQueueLimit.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceQueueLimit.setDescription('This attribute specifies the total number of bytes of traced data which may be queued for transmission to the trace receiver. When this limit is exceeded, incoming traced frames are discarded. This attribute can be set while a trace is active and takes effect immediately.')
frNniTraceSession = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 10, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceSession.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceSession.setDescription('This attribute is set automatically. It identifies the Trace Session component which is forwarding the trace data. This attribute is empty unless a trace is active.')
frNniTraceFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2))
frNniTraceFilterRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1), )
if mibBuilder.loadTexts: frNniTraceFilterRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterRowStatusTable.setDescription('This entry controls the addition and deletion of frNniTraceFilter components.')
frNniTraceFilterRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceFilterIndex"))
if mibBuilder.loadTexts: frNniTraceFilterRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterRowStatusEntry.setDescription('A single entry in the table represents a single frNniTraceFilter component.')
frNniTraceFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceFilterRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterRowStatus.setDescription('This variable is used as the basis for SNMP naming of frNniTraceFilter components. These components cannot be added nor deleted.')
frNniTraceFilterComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceFilterComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
frNniTraceFilterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: frNniTraceFilterStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterStorageType.setDescription('This variable represents the storage type value for the frNniTraceFilter tables.')
frNniTraceFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: frNniTraceFilterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterIndex.setDescription('This variable represents the index for the frNniTraceFilter tables.')
frNniTraceFilterOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10), )
if mibBuilder.loadTexts: frNniTraceFilterOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterOperationalTable.setDescription('This group provides the operational attributes for the Frame Relay Trace Filter component.')
frNniTraceFilterOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1), ).setIndexNames((0, "Nortel-Magellan-Passport-FrameRelayNniMIB", "frNniIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceIndex"), (0, "Nortel-Magellan-Passport-FrameRelayNniTraceMIB", "frNniTraceFilterIndex"))
if mibBuilder.loadTexts: frNniTraceFilterOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterOperationalEntry.setDescription('An entry in the frNniTraceFilterOperationalTable.')
frNniTraceFilterTraceType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="e0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceFilterTraceType.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterTraceType.setDescription('This attribute specifies the level of filtering required for this trace session. A value of lmi indicates that Lmi frames are traced. A value of dlci indicates that frames from the Dlci specified by the tracedDlci attribute are traced. A value of badFrames indicates that bad received frames (overruns, CRC errors, aborts) are traced. The default is to trace all frames. This attribute can be set while a trace is active and takes effect immediately. Description of bits: lmi(0) dlci(1) badFrames(2)')
frNniTraceFilterTracedDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1007))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceFilterTracedDlci.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterTracedDlci.setDescription('This attribute specifies a particular Dlci to trace. A value of zero specifies that all Dlcis are to be traced. This attribute can be set while a trace is active and takes effect immediately.')
frNniTraceFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="c0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceFilterDirection.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterDirection.setDescription('This attribute specifies the direction of the data to be traced as viewed by the service. The values can be egress, and/or ingress. An egress value indicates frames outbound from the service. An ingress value indicates frames inbound to the service. This attribute can be set while a trace is active and takes effect immediately. Description of bits: egress(0) ingress(1)')
frNniTraceFilterTracedLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 70, 7, 2, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: frNniTraceFilterTracedLength.setStatus('mandatory')
if mibBuilder.loadTexts: frNniTraceFilterTracedLength.setDescription('This attribute specifies the maximum number of bytes to trace per frame starting from the byte following the frame flag. If the frame length is longer than the value specified by this attribute, then the traced frame is truncated. This attribute can be set while a trace is active and takes effect immediately.')
frameRelayNniTraceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1))
frameRelayNniTraceGroupBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4))
frameRelayNniTraceGroupBD01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4, 2))
frameRelayNniTraceGroupBD01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 1, 4, 2, 2))
frameRelayNniTraceCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3))
frameRelayNniTraceCapabilitiesBD = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4))
frameRelayNniTraceCapabilitiesBD01 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4, 2))
frameRelayNniTraceCapabilitiesBD01A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 106, 3, 4, 2, 2))
mibBuilder.exportSymbols("Nortel-Magellan-Passport-FrameRelayNniTraceMIB", frNniTraceDuration=frNniTraceDuration, frameRelayNniTraceMIB=frameRelayNniTraceMIB, frNniTraceFilterRowStatusEntry=frNniTraceFilterRowStatusEntry, frNniTraceComponentName=frNniTraceComponentName, frameRelayNniTraceGroupBD01=frameRelayNniTraceGroupBD01, frNniTraceFilterOperationalTable=frNniTraceFilterOperationalTable, frNniTraceFilterRowStatus=frNniTraceFilterRowStatus, frameRelayNniTraceGroup=frameRelayNniTraceGroup, frNniTraceStorageType=frNniTraceStorageType, frameRelayNniTraceCapabilities=frameRelayNniTraceCapabilities, frameRelayNniTraceCapabilitiesBD01=frameRelayNniTraceCapabilitiesBD01, frameRelayNniTraceGroupBD=frameRelayNniTraceGroupBD, frameRelayNniTraceGroupBD01A=frameRelayNniTraceGroupBD01A, frNniTraceFilterComponentName=frNniTraceFilterComponentName, frNniTraceFilterTracedLength=frNniTraceFilterTracedLength, frNniTraceIndex=frNniTraceIndex, frNniTraceFilterStorageType=frNniTraceFilterStorageType, frNniTraceRowStatus=frNniTraceRowStatus, frNniTrace=frNniTrace, frNniTraceReceiverName=frNniTraceReceiverName, frameRelayNniTraceCapabilitiesBD=frameRelayNniTraceCapabilitiesBD, frNniTraceRowStatusTable=frNniTraceRowStatusTable, frNniTraceOperationalEntry=frNniTraceOperationalEntry, frNniTraceFilterOperationalEntry=frNniTraceFilterOperationalEntry, frNniTraceQueueLimit=frNniTraceQueueLimit, frNniTraceFilterTraceType=frNniTraceFilterTraceType, frameRelayNniTraceCapabilitiesBD01A=frameRelayNniTraceCapabilitiesBD01A, frNniTraceFilterRowStatusTable=frNniTraceFilterRowStatusTable, frNniTraceRowStatusEntry=frNniTraceRowStatusEntry, frNniTraceSession=frNniTraceSession, frNniTraceFilterIndex=frNniTraceFilterIndex, frNniTraceFilterDirection=frNniTraceFilterDirection, frNniTraceOperationalTable=frNniTraceOperationalTable, frNniTraceFilterTracedDlci=frNniTraceFilterTracedDlci, frNniTraceFilter=frNniTraceFilter)